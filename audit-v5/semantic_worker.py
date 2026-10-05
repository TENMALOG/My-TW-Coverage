from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from email.utils import parsedate_to_datetime
import json
import os
import tempfile
import time
import urllib.request
import urllib.error
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

API_URL = "https://api.openai.com/v1/responses"
QUEUE_PATH = Path("audit-v5/generated/semantic-high-queue.json")
STATE_PATH = Path("audit-v5/generated/semantic-worker-state.json")
STATUS_PATH = Path("audit-v5/AUDIT-STATUS.md")
AUTHOR_DIR = Path("audit-v5/semantic")
LOCAL_RECHECK_PATH = Path("audit-v5/semantic/local-recheck-queue.json")

DECISIONS = [
    "ACCEPTED",
    "PARTIALLY_SUPPORTED",
    "UNSUPPORTED",
    "PERIOD_UNRESOLVED",
    "SOURCE_UNAVAILABLE",
    "UNKNOWN_AFTER_RESEARCH",
]

SCHEMA = {
    "type": "object",
    "properties": {
        "decision": {"type": "string", "enum": DECISIONS},
        "rationale": {"type": "string"},
        "proposed_text": {"type": ["string", "null"]},
        "evidence": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "url": {"type": "string"},
                    "title": {"type": "string"},
                    "source_level": {"type": "integer", "minimum": 1, "maximum": 5},
                    "period_binding": {"type": "string"},
                    "note": {"type": "string"},
                },
                "required": ["url", "title", "source_level", "period_binding", "note"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["decision", "rationale", "proposed_text", "evidence"],
    "additionalProperties": False,
}

SYSTEM_PROMPT = """You are auditing factual claims in a Taiwan listed-company knowledge base.
Be conservative and evidence-driven.

Source priority:
1. TWSE / TPEx / MOPS / MOEA / government / regulator.
2. Formal issuer annual report, financial report, investor presentation, exchange filing.
3. Official issuer website/newsroom.
4. Reliable professional secondary source.
5. Other source only when clearly necessary.

Rules:
- Search the live web before deciding.
- Ranking, largest/first/only, market-share, exclusivity, major/core supplier/customer, revenue-share, Tier-1, design-in, profitability and historical identity claims require explicit support for the exact qualifier.
- A current undated page must not silently prove a historical-period claim.
- Search-result snippets alone are insufficient.
- If evidence supports only a weaker statement, use PARTIALLY_SUPPORTED and provide proposed_text.
- If authoritative evidence contradicts the material claim, use UNSUPPORTED.
- UNKNOWN_AFTER_RESEARCH is allowed after a real search.
- Do not invent URLs or source titles.
"""

REVIEWER_PROMPT = """You are an independent reviewer. Research the claim from scratch using live web search.
You do not know the author's decision. Apply the same strict evidentiary policy.
Return your own decision and evidence. Exact material qualifiers require exact evidence.
"""


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def norm_url(url: str) -> str:
    try:
        p = urlsplit(url)
        return urlunsplit((p.scheme.lower(), p.netloc.lower(), p.path.rstrip("/"), "", ""))
    except Exception:
        return url


def response_text(payload: dict[str, Any]) -> str:
    for item in payload.get("output", []):
        if item.get("type") != "message":
            continue
        for part in item.get("content", []):
            if part.get("type") == "output_text":
                return part.get("text", "")
    raise ValueError("response has no output_text")


def source_urls(payload: dict[str, Any]) -> set[str]:
    urls: set[str] = set()
    for item in payload.get("output", []):
        if item.get("type") == "web_search_call":
            action = item.get("action") or {}
            for src in action.get("sources") or []:
                if isinstance(src, dict) and src.get("url"):
                    urls.add(norm_url(str(src["url"])))
        if item.get("type") == "message":
            for part in item.get("content", []):
                for ann in part.get("annotations") or []:
                    if isinstance(ann, dict) and ann.get("type") == "url_citation" and ann.get("url"):
                        urls.add(norm_url(str(ann["url"])))
    return urls


def retry_delay(exc: Exception, attempt: int) -> float | None:
    """Return a bounded delay for retryable API/network errors, else None."""
    if isinstance(exc, urllib.error.HTTPError):
        if exc.code not in {429, 500, 502, 503, 504}:
            return None
        retry_after = exc.headers.get("Retry-After") if exc.headers else None
        if retry_after:
            try:
                return min(60.0, max(0.0, float(retry_after)))
            except ValueError:
                try:
                    when = parsedate_to_datetime(retry_after)
                    return min(60.0, max(0.0, when.timestamp() - time.time()))
                except (TypeError, ValueError, OverflowError):
                    pass
        return min(30.0, 2.0 ** (attempt + 1))
    if isinstance(exc, (urllib.error.URLError, TimeoutError, ConnectionError, OSError)):
        return min(30.0, 2.0 ** (attempt + 1))
    return None


def call_openai(api_key: str, model: str, effort: str, claim: dict[str, Any], role_prompt: str, retries: int = 3) -> dict[str, Any]:
    user = (
        f"Ticker: {claim.get('ticker')}\n"
        f"Company: {claim.get('company')}\n"
        f"Signal type: {claim.get('signal_type')}\n"
        f"Claim: {claim.get('claim')}\n"
        f"Repository path: {claim.get('path')}\n\n"
        "Research this exact claim. Prefer Taiwan official and issuer-primary sources. "
        "Return only the structured result."
    )
    body = {
        "model": model,
        "reasoning": {"effort": effort},
        "tools": [{"type": "web_search", "search_context_size": "medium"}],
        "tool_choice": "required",
        "include": ["web_search_call.action.sources"],
        "store": False,
        "input": [
            {"role": "system", "content": SYSTEM_PROMPT + "\n" + role_prompt},
            {"role": "user", "content": user},
        ],
        "text": {
            "format": {
                "type": "json_schema",
                "name": "semantic_claim_review",
                "strict": True,
                "schema": SCHEMA,
            }
        },
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(body).encode("utf-8"),
        method="POST",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    )
    last: Exception | None = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=240) as r:
                raw = json.loads(r.read().decode("utf-8"))
            parsed = json.loads(response_text(raw))
            consulted = source_urls(raw)
            validated = []
            rejected = []
            for ev in parsed.get("evidence", []):
                if norm_url(str(ev.get("url", ""))) in consulted:
                    validated.append(ev)
                else:
                    rejected.append(ev)
            parsed["evidence"] = validated
            parsed["rejected_unsourced_evidence"] = rejected
            parsed["consulted_source_urls"] = sorted(consulted)
            parsed["response_id"] = raw.get("id")
            parsed["model"] = model
            parsed["reasoning_effort"] = effort
            parsed["reviewed_at"] = now_iso()
            if parsed["decision"] in {"ACCEPTED", "PARTIALLY_SUPPORTED", "UNSUPPORTED"} and not validated:
                parsed["decision"] = "UNKNOWN_AFTER_RESEARCH"
                parsed["rationale"] = (
                    "Material decision lacked an evidence URL matching the actual web-search source list; "
                    "downgraded automatically. " + parsed.get("rationale", "")
                )
            return parsed
        except Exception as exc:
            last = exc
            delay = retry_delay(exc, attempt)
            if attempt + 1 < retries and delay is not None:
                time.sleep(delay)
            else:
                break
    raise RuntimeError(f"OpenAI Responses request failed after retries: {type(last).__name__}: {last}")


def atomic_write_json(path: Path, value: dict[str, Any]) -> None:
    """Coordinator-only durable JSON write using a same-directory replace."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        if os.name == "posix":
            directory_fd = os.open(path.parent, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
            try:
                os.fsync(directory_fd)
            finally:
                os.close(directory_fd)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def atomic_write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            stream.write(value)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        if os.name == "posix":
            directory_fd = os.open(path.parent, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
            try:
                os.fsync(directory_fd)
            finally:
                os.close(directory_fd)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def unique_claims(claims: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Keep the first queued occurrence of each authoritative stable claim ID."""
    unique: list[dict[str, Any]] = []
    seen: set[str] = set()
    for claim in claims:
        cid = claim.get("claim_id")
        if not cid or cid in seen:
            continue
        seen.add(cid)
        unique.append(claim)
    return unique


def process_batch(
    claims: list[dict[str, Any]], state: dict[str, Any],
    author_fn, reviewer_fn, author_concurrency: int, reviewer_concurrency: int,
    persist_state=None,
) -> dict[str, Any]:
    """Run bounded author and reviewer pools; mutate shared state only here."""
    claims = unique_claims(claims)
    started = now_iso()
    batch = {"started_at": started, "batch_started_at": started, "selected_claim_ids": [c["claim_id"] for c in claims], "results": []}
    timings: dict[str, list[float]] = {"author": [], "reviewer": []}
    counts = {"author_success": 0, "author_error": 0, "reviewer_success": 0, "reviewer_error": 0}

    for claim in claims:
        cid = claim["claim_id"]
        rec = state["results"].setdefault(cid, {"claim_id": cid, "author": None, "reviewer": None, "final_state": None, "status": "PENDING", "attempts": 0})
        rec["attempts"] = int(rec.get("attempts", 0)) + 1

    todo = [(c, state["results"][c["claim_id"]]) for c in claims if not state["results"][c["claim_id"]].get("author")]
    batch["author_count"] = len(todo)
    batch["effective_author_concurrency"] = min(max(1, author_concurrency), len(todo)) if todo else 0
    if todo:
        with ThreadPoolExecutor(max_workers=batch["effective_author_concurrency"], thread_name_prefix="semantic-author") as pool:
            futures = {pool.submit(_timed_call, author_fn, claim): claim for claim, _ in todo}
            for future in as_completed(futures):
                claim = futures[future]
                cid = claim["claim_id"]
                rec = state["results"][cid]
                try:
                    result, elapsed = future.result()
                    rec["author"] = result
                    rec["status"] = "REVIEWER_PENDING"
                    rec.pop("last_error", None)
                    timings["author"].append(elapsed)
                    counts["author_success"] += 1
                except Exception as exc:
                    rec["status"] = "AUTHOR_ERROR"
                    rec["last_error"] = f"{type(exc).__name__}: {exc}"
                    counts["author_error"] += 1
                if persist_state:
                    persist_state(state)

    # Previously authored claims remain eligible, while completed reviewers are never called again.
    reviewer_todo = [c for c in claims if state["results"][c["claim_id"]].get("author") and not state["results"][c["claim_id"]].get("reviewer")]
    for claim in claims:
        rec = state["results"][claim["claim_id"]]
        if rec.get("author") and not rec.get("reviewer"):
            rec["status"] = "REVIEWER_PENDING"
    batch["reviewer_count"] = len(reviewer_todo)
    batch["effective_reviewer_concurrency"] = min(max(1, reviewer_concurrency), len(reviewer_todo)) if reviewer_todo else 0
    if reviewer_todo:
        with ThreadPoolExecutor(max_workers=batch["effective_reviewer_concurrency"], thread_name_prefix="semantic-reviewer") as pool:
            futures = {pool.submit(_timed_call, reviewer_fn, claim): claim for claim in reviewer_todo}
            for future in as_completed(futures):
                claim = futures[future]
                cid = claim["claim_id"]
                rec = state["results"][cid]
                try:
                    result, elapsed = future.result()
                    rec["reviewer"] = result
                    final_state, agreement = finalise(rec["author"], result)
                    rec["final_state"] = final_state
                    rec["agreement"] = agreement
                    rec["status"] = "FINALISED" if final_state != "ESCALATED_REVIEW_DISAGREEMENT" else "ESCALATED"
                    rec.pop("last_error", None)
                    timings["reviewer"].append(elapsed)
                    counts["reviewer_success"] += 1
                except Exception as exc:
                    rec["status"] = "REVIEWER_ERROR"
                    rec["last_error"] = f"{type(exc).__name__}: {exc}"
                    counts["reviewer_error"] += 1
                if persist_state:
                    persist_state(state)

    batch.update(counts)
    batch["author_average_seconds"] = sum(timings["author"]) / len(timings["author"]) if timings["author"] else None
    batch["reviewer_average_seconds"] = sum(timings["reviewer"]) / len(timings["reviewer"]) if timings["reviewer"] else None
    batch["finished_at"] = now_iso()
    batch["batch_finished_at"] = batch["finished_at"]
    batch["batch_duration_seconds"] = max(0.0, (datetime.fromisoformat(batch["finished_at"]) - datetime.fromisoformat(started)).total_seconds())
    batch["results"] = [{"claim_id": c["claim_id"], "status": state["results"][c["claim_id"]].get("status"), "final_state": state["results"][c["claim_id"]].get("final_state")} for c in claims]
    state["updated_at"] = batch["finished_at"]
    return batch


def _timed_call(fn, claim: dict[str, Any]):
    start = time.monotonic()
    result = fn(claim)
    return result, time.monotonic() - start


def load_state(queue: dict[str, Any]) -> dict[str, Any]:
    if STATE_PATH.exists():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    else:
        state = {
            "schema": "semantic-worker-state-1",
            "created_at": now_iso(),
            "updated_at": now_iso(),
            "queue_claim_count": queue["claim_count"],
            "results": {},
            "batches": [],
        }

    for path in sorted(AUTHOR_DIR.glob("author-*.json")):
        try:
            batch = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        for item in batch.get("items", []):
            cid = item.get("claim_id")
            if not cid or cid in state["results"]:
                continue
            state["results"][cid] = {
                "claim_id": cid,
                "author": {
                    "decision": item.get("decision"),
                    "rationale": item.get("rationale", ""),
                    "proposed_text": item.get("proposed_text"),
                    "evidence": item.get("evidence", []),
                    "model": "manual-author",
                    "response_id": None,
                    "reviewed_at": batch.get("reviewed_at"),
                },
                "reviewer": None,
                "final_state": None,
                "status": "REVIEWER_PENDING",
                "attempts": 0,
                "source": str(path),
            }
    return state


def finalise(author: dict[str, Any], reviewer: dict[str, Any]) -> tuple[str, str]:
    ad = author["decision"]
    rd = reviewer["decision"]
    if ad == rd:
        return ad, "AUTHOR_REVIEWER_AGREE"
    return "ESCALATED_REVIEW_DISAGREEMENT", f"AUTHOR={ad};REVIEWER={rd}"


def select_claims(queue: dict[str, Any], state: dict[str, Any], batch_size: int) -> list[dict[str, Any]]:
    qmap = {x["claim_id"]: x for x in queue["items"]}
    selected: list[dict[str, Any]] = []
    for cid, rec in state["results"].items():
        if len(selected) >= batch_size:
            break
        if rec.get("status") == "REVIEWER_PENDING" and cid in qmap:
            selected.append(qmap[cid])

    selected_ids = {x["claim_id"] for x in selected}
    for claim in queue["items"]:
        if len(selected) >= batch_size:
            break
        cid = claim["claim_id"]
        if cid in selected_ids:
            continue
        rec = state["results"].get(cid)
        if rec is None or rec.get("status") in {"RETRY", "AUTHOR_ERROR", "REVIEWER_ERROR"}:
            selected.append(claim)
    return unique_claims(selected)


def render_status(queue: dict[str, Any], state: dict[str, Any], worker_cfg: dict[str, Any]) -> str:
    results = state["results"]
    status_counts = Counter(rec.get("status", "UNKNOWN") for rec in results.values())
    final_counts = Counter(rec.get("final_state") for rec in results.values() if rec.get("final_state"))
    author_done = sum(1 for rec in results.values() if rec.get("author"))
    reviewer_done = sum(1 for rec in results.values() if rec.get("reviewer"))
    final_done = sum(1 for rec in results.values() if rec.get("final_state"))
    total = int(queue["claim_count"])
    pct = (final_done / total * 100.0) if total else 0.0
    remaining = total - final_done

    lines = [
        "# Audit v5 Status", "",
        f"Updated: {state.get('updated_at')}", "",
        "## Semantic HIGH verification", "",
        f"- HIGH issuers: **{queue['issuer_count']}**",
        f"- Raw HIGH signals: **{queue['raw_signal_count']}**",
        f"- Unique HIGH claims: **{total}**",
        f"- Author-reviewed claims: **{author_done} / {total}**",
        f"- Independently reviewed claims: **{reviewer_done} / {total}**",
        f"- Finalised claims: **{final_done} / {total} ({pct:.2f}%)**",
        f"- Remaining: **{remaining}**", "",
        "### Worker", "",
        "- Enabled by workflow: **yes**",
        f"- Batch size: **{worker_cfg['batch_size']}**",
        f"- Author concurrency: **{worker_cfg['author_concurrency']}**",
        f"- Reviewer concurrency: **{worker_cfg['reviewer_concurrency']}**",
        f"- Author model: {worker_cfg['author_model']}",
        f"- Reviewer model: {worker_cfg['reviewer_model']}",
        f"- Schedule: {worker_cfg['schedule']}", "",
        "### Current states", "",
    ]
    for key, value in sorted(status_counts.items()):
        lines.append(f"- {key}: **{value}**")
    if not status_counts:
        lines.append("- No worker results yet.")
    lines += ["", "### Final decisions", ""]
    for key, value in sorted(final_counts.items()):
        lines.append(f"- {key}: **{value}**")
    if not final_counts:
        lines.append("- No final decisions yet.")
    latest_batch = (state.get("batches") or [])[-1] if state.get("batches") else None
    if latest_batch:
        lines += [
            "", "### Latest batch timing", "",
            f"- Duration: **{latest_batch.get('batch_duration_seconds', 0):.2f}s**",
            f"- Author calls / success / error: **{latest_batch.get('author_count', 0)} / {latest_batch.get('author_success', 0)} / {latest_batch.get('author_error', 0)}**",
            f"- Reviewer calls / success / error: **{latest_batch.get('reviewer_count', 0)} / {latest_batch.get('reviewer_success', 0)} / {latest_batch.get('reviewer_error', 0)}**",
        ]
    if LOCAL_RECHECK_PATH.exists():
        recheck = json.loads(LOCAL_RECHECK_PATH.read_text(encoding="utf-8"))
        items = recheck.get("items", [])
        status_counts = Counter(
            str(observation.get("http_status") or observation.get("error_type") or "unknown")
            for item in items for observation in item.get("observations", [])
        )
        claim_counts = Counter(item.get("claim_id") for item in items if item.get("queue_state") == "LOCAL_RECHECK_PENDING")
        lines += ["", "## Transient source rechecks", "", f"- `LOCAL_RECHECK_PENDING` URLs: **{len(items)}**"]
        for key, count in sorted(status_counts.items()):
            lines.append(f"- HTTP/error {key}: **{count}**")
        lines.append(f"- Affected claims: **{len(claim_counts)}**")
        for claim_id, count in sorted(claim_counts.items()):
            lines.append(f"- {claim_id}: **{count} URL(s)**")
        lines.append("- Home-network observations establish availability only; Cloud failure history and semantic decisions remain unchanged.")
    lines += [
        "", "## Financial Phase 1", "",
        "- Deterministic official comparison: **6,207 / 6,207 verified**",
        "- FINANCIAL_DIFFERENCE: **0**",
        "- METHOD_UNRESOLVED: **0**",
        "- SOURCE_DEFINITION_DIFFERENCE: **0**",
        "- REPO_VALUE_UNAVAILABLE: **0**", "",
        "The semantic worker only updates evidence/review ledgers and status. It does not silently rewrite issuer reports.", "",
    ]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-size", type=int, default=int(os.getenv("SEMANTIC_BATCH_SIZE", "4")))
    ap.add_argument("--author-concurrency", type=int, default=int(os.getenv("SEMANTIC_AUTHOR_CONCURRENCY", "4")))
    ap.add_argument("--reviewer-concurrency", type=int, default=int(os.getenv("SEMANTIC_REVIEWER_CONCURRENCY", "4")))
    ap.add_argument("--author-model", default=os.getenv("SEMANTIC_AUTHOR_MODEL", "gpt-5.5"))
    ap.add_argument("--reviewer-model", default=os.getenv("SEMANTIC_REVIEWER_MODEL", "gpt-5.5"))
    ap.add_argument("--author-effort", default=os.getenv("SEMANTIC_AUTHOR_EFFORT", "medium"))
    ap.add_argument("--reviewer-effort", default=os.getenv("SEMANTIC_REVIEWER_EFFORT", "high"))
    ap.add_argument("--schedule-label", default=os.getenv("SEMANTIC_SCHEDULE_LABEL", "every 30 minutes"))
    args = ap.parse_args()

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is not set. Add a GitHub Actions repository secret named OPENAI_API_KEY.")

    queue = json.loads(QUEUE_PATH.read_text(encoding="utf-8"))
    state = load_state(queue)
    claims = select_claims(queue, state, max(1, args.batch_size))
    run_id = os.getenv("GITHUB_RUN_ID", "local")
    def persist_current_state(current):
        # Stable key ordering avoids completion-order dependent JSON output.
        serializable = dict(current)
        serializable["results"] = {key: current["results"][key] for key in sorted(current["results"])}
        atomic_write_json(STATE_PATH, serializable)

    batch = process_batch(
        claims, state,
        lambda c: call_openai(api_key, args.author_model, args.author_effort, c, "You are the author/researcher."),
        lambda c: call_openai(api_key, args.reviewer_model, args.reviewer_effort, c, REVIEWER_PROMPT),
        max(1, args.author_concurrency), max(1, args.reviewer_concurrency),
        persist_state=persist_current_state,
    )
    batch["run_id"] = run_id
    state["batches"].append(batch)
    state["batches"] = state["batches"][-100:]
    persist_current_state(state)

    cfg = {"batch_size": args.batch_size, "author_concurrency": max(1, args.author_concurrency), "reviewer_concurrency": max(1, args.reviewer_concurrency), "author_model": args.author_model, "reviewer_model": args.reviewer_model, "schedule": args.schedule_label}
    atomic_write_text(STATUS_PATH, render_status(queue, state, cfg))

    out_dir = AUTHOR_DIR / "worker-batches"
    out_dir.mkdir(parents=True, exist_ok=True)
    atomic_write_json(out_dir / f"worker-{run_id}.json", batch)

    print(json.dumps({"selected": len(claims), "run_id": run_id, "batch_duration_seconds": batch["batch_duration_seconds"], "author_count": batch["author_count"], "author_success": batch["author_success"], "author_error": batch["author_error"], "reviewer_count": batch["reviewer_count"], "reviewer_success": batch["reviewer_success"], "reviewer_error": batch["reviewer_error"], "effective_author_concurrency": batch["effective_author_concurrency"], "effective_reviewer_concurrency": batch["effective_reviewer_concurrency"], "state_path": str(STATE_PATH), "status_path": str(STATUS_PATH)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
