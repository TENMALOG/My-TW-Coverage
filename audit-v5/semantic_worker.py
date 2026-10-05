from __future__ import annotations

import argparse
import json
import os
import time
import urllib.request
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
            if attempt + 1 < retries:
                time.sleep(2 + attempt * 3)
    raise RuntimeError(f"OpenAI Responses request failed after retries: {type(last).__name__}: {last}")


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
    return selected


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
    batch = {"run_id": run_id, "started_at": now_iso(), "selected_claim_ids": [c["claim_id"] for c in claims], "results": []}

    for claim in claims:
        cid = claim["claim_id"]
        rec = state["results"].setdefault(cid, {"claim_id": cid, "author": None, "reviewer": None, "final_state": None, "status": "PENDING", "attempts": 0})
        rec["attempts"] = int(rec.get("attempts", 0)) + 1
        try:
            if not rec.get("author"):
                rec["author"] = call_openai(api_key, args.author_model, args.author_effort, claim, "You are the author/researcher.")
            rec["status"] = "REVIEWER_PENDING"
        except Exception as exc:
            rec["status"] = "AUTHOR_ERROR"
            rec["last_error"] = f"{type(exc).__name__}: {exc}"
            batch["results"].append({"claim_id": cid, "status": rec["status"]})
            continue

        try:
            rec["reviewer"] = call_openai(api_key, args.reviewer_model, args.reviewer_effort, claim, REVIEWER_PROMPT)
            final_state, agreement = finalise(rec["author"], rec["reviewer"])
            rec["final_state"] = final_state
            rec["agreement"] = agreement
            rec["status"] = "FINALISED" if final_state != "ESCALATED_REVIEW_DISAGREEMENT" else "ESCALATED"
            rec.pop("last_error", None)
        except Exception as exc:
            rec["status"] = "REVIEWER_ERROR"
            rec["last_error"] = f"{type(exc).__name__}: {exc}"

        batch["results"].append({"claim_id": cid, "status": rec["status"], "final_state": rec.get("final_state")})

    batch["finished_at"] = now_iso()
    state["updated_at"] = batch["finished_at"]
    state["batches"].append(batch)
    state["batches"] = state["batches"][-100:]
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    cfg = {"batch_size": args.batch_size, "author_model": args.author_model, "reviewer_model": args.reviewer_model, "schedule": args.schedule_label}
    STATUS_PATH.write_text(render_status(queue, state, cfg), encoding="utf-8")

    out_dir = AUTHOR_DIR / "worker-batches"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"worker-{run_id}.json").write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({"selected": len(claims), "run_id": run_id, "state_path": str(STATE_PATH), "status_path": str(STATUS_PATH)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
