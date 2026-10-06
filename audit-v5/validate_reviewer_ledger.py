"""Validate separate manual reviewer ledgers without rewriting author records."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

DECISIONS = {
    "ACCEPTED", "PARTIALLY_SUPPORTED", "UNSUPPORTED", "PERIOD_UNRESOLVED",
    "SOURCE_UNAVAILABLE", "UNKNOWN_AFTER_RESEARCH",
}


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def text_sha256(path: Path) -> str:
    """Git may change CRLF/LF on checkout; audit-authored text hashes use UTF-8/LF."""
    return hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()


def validate(root: Path, *, check_local_sources: bool = False) -> dict:
    errors = []
    queue = read_json(root / "audit-v5/generated/semantic-high-queue.json")["items"]
    qmap = {i["claim_id"]: i for i in queue}
    if len(qmap) != len(queue):
        errors.append("queue contains duplicate claim ids")
    authors = {}
    author_count = 0
    for path in sorted((root / "audit-v5/semantic").glob("author-[0-9][0-9][0-9].json")):
        batch = read_json(path)
        for item in batch["items"]:
            author_count += 1
            cid = item["claim_id"]
            if cid in authors:
                errors.append(f"duplicate author claim: {cid}")
            authors[cid] = (path, batch, item)
            if cid not in qmap or item.get("normalized_claim_hash") != qmap[cid]["normalized_claim_hash"]:
                errors.append(f"author/queue hash mismatch: {cid}")
            if item.get("final_state") is not None or item.get("independent_review") is not None:
                errors.append(f"author ledger has been finalised in place: {cid}")
    if set(authors) != set(qmap):
        errors.append("author and queue coverage differ")

    reviewed = {}
    review_paths = {}
    states = Counter()
    decisions = Counter()
    sources = {}
    now = datetime.now(timezone.utc)
    for path in sorted((root / "audit-v5/semantic").glob("reviewer-[0-9][0-9][0-9].json")):
        batch = read_json(path)
        if batch.get("schema") != "semantic-manual-independent-review-2":
            errors.append(f"unsupported reviewer schema: {path.name}")
        if len(batch["items"]) > 25 or batch.get("review_count") != len(batch["items"]):
            errors.append(f"invalid bounded batch size/count: {path.name}")
        if datetime.fromisoformat(batch["reviewed_at"].replace("Z", "+00:00")) > now:
            errors.append(f"future reviewer timestamp: {path.name}")
        manifest_path = root / batch["evidence_manifest"]
        if text_sha256(manifest_path) != batch["evidence_manifest_sha256"]:
            errors.append(f"evidence manifest changed: {path.name}")
        countercheck_path = root / batch["counterchecks"]
        if text_sha256(countercheck_path) != batch["counterchecks_sha256"]:
            errors.append(f"numeric counterchecks changed: {path.name}")
        manifest = read_json(manifest_path)
        manifest_sources = {s["source_id"]: s for s in manifest["sources"]}
        if len(manifest_sources) != len(manifest["sources"]):
            errors.append(f"duplicate source ids: {path.name}")
        for sid, source in manifest_sources.items():
            if sid in sources and any(source.get(k) != sources[sid].get(k) for k in ("url", "source_sha256", "local_source_path")):
                errors.append(f"conflicting source identity across batches: {sid}")
        sources.update(manifest_sources)
        for source in manifest_sources.values():
            note_path = root / source["inspection_note_path"]
            if not note_path.exists() or text_sha256(note_path) != source["inspection_note_sha256"]:
                errors.append(f"evidence inspection note changed/missing: {source['source_id']}")
            if not re.fullmatch(r"[0-9a-f]{64}", source.get("source_sha256", "")):
                errors.append(f"missing source content hash: {source['source_id']}")
            if datetime.fromisoformat(source["inspected_at"].replace("Z", "+00:00")) > now:
                errors.append(f"future inspection date: {source['source_id']}")
            if check_local_sources:
                raw = root / source["local_source_path"]
                if not raw.exists() or hashlib.sha256(raw.read_bytes()).hexdigest() != source["source_sha256"]:
                    errors.append(f"local raw source changed/missing: {source['source_id']}")
        for item in batch["items"]:
            cid = item["claim_id"]
            key = (cid, item["normalized_claim_hash"])
            if key in reviewed or cid in {k[0] for k in reviewed}:
                errors.append(f"duplicate reviewer claim: {cid}")
            reviewed[key] = item
            review_paths[key] = path
            if cid not in qmap or item["normalized_claim_hash"] != qmap[cid]["normalized_claim_hash"]:
                errors.append(f"reviewer/queue hash mismatch: {cid}")
                continue
            if item["claim"] != qmap[cid]["claim"]:
                errors.append(f"reviewer claim text changed: {cid}")
            if cid not in authors:
                errors.append(f"review without author lineage: {cid}")
                continue
            author_path, author_batch, author_item = authors[cid]
            if item["author_batch_id"] != author_batch["batch_id"] or item["author_decision"] != author_item["decision"]:
                errors.append(f"author snapshot mismatch: {cid}")
            if text_sha256(author_path) != item["author_batch_sha256"]:
                errors.append(f"author batch bytes changed since review: {cid}")
            decision = item["decision"]
            if decision not in DECISIONS:
                errors.append(f"invalid reviewer decision: {cid}")
            agree = decision == author_item["decision"]
            expected = decision if agree else "ESCALATED_REVIEW_DISAGREEMENT"
            if item["agrees_with_author"] != agree or item["final_state"] != expected:
                errors.append(f"final-state/decision agreement mismatch: {cid}")
            if item["status"] != ("FINALISED" if agree else "ESCALATED"):
                errors.append(f"final-state/status mismatch: {cid}")
            if not item.get("evidence") or not item.get("component_assessments"):
                errors.append(f"missing evidence/components: {cid}")
            for evidence in item["evidence"]:
                source = manifest_sources.get(evidence["source_id"])
                if source is None or evidence["source_sha256"] != source["source_sha256"] or evidence["url"] != source["url"]:
                    errors.append(f"broken evidence lineage: {cid}")
                if not evidence.get("period_binding") or not evidence.get("locator"):
                    errors.append(f"missing period/locator: {cid}")
            for component in item["component_assessments"]:
                if not set(component["source_ids"]) <= set(manifest_sources):
                    errors.append(f"unknown component source: {cid}")
                if component["assessment"].startswith("SUPPORTED") and not component["source_ids"]:
                    errors.append(f"supported component lacks a source: {cid}")
            states[item["final_state"]] += 1
            decisions[decision] += 1
        if dict(Counter(i["decision"] for i in batch["items"])) != batch["decision_counts"] or dict(Counter(i["final_state"] for i in batch["items"])) != batch["final_state_counts"]:
            errors.append(f"batch aggregate counts mismatch: {path.name}")
    # Component corrections are append-only overlays. They cannot promote a
    # decision or change a final state; adjudication needs a separate protocol.
    amendment_ids = set()
    amended_fields = {}
    amendment_refs = {}
    amendment_evidence = {}
    amendment_count = 0
    for path in sorted((root / "audit-v5/semantic").glob("reviewer-amendments-[0-9][0-9][0-9].json")):
        batch = read_json(path)
        if batch.get("schema") != "semantic-reviewer-component-amendment-1":
            errors.append(f"unsupported amendment schema: {path.name}")
        events = batch.get("events", [])
        if not 1 <= len(events) <= 25 or batch.get("event_count") != len(events):
            errors.append(f"invalid amendment batch size/count: {path.name}")
        for event in events:
            amendment_count += 1
            eid = event.get("event_id")
            if not eid or eid in amendment_ids:
                errors.append(f"duplicate/missing amendment id: {eid}")
            amendment_ids.add(eid)
            if datetime.fromisoformat(event["reviewed_at"].replace("Z", "+00:00")) > now:
                errors.append(f"future amendment timestamp: {eid}")
            key = (event["claim_id"], event["normalized_claim_hash"])
            item = reviewed.get(key)
            target = root / event["target_batch_path"]
            if item is None or target != review_paths.get(key):
                errors.append(f"amendment target/claim mismatch: {eid}")
                continue
            if not target.exists() or text_sha256(target) != event["target_batch_sha256"]:
                errors.append(f"amendment target hash mismatch: {eid}")
            amendment_refs.setdefault(key, []).append({
                "path": path.relative_to(root).as_posix(), "sha256": text_sha256(path), "event_id": eid,
            })
            amendment_evidence.setdefault(key, []).extend(event.get("evidence", []))
            for field in ("decision", "final_state", "status"):
                if event.get(field + "_before") != item[field] or event.get(field + "_after") != item[field]:
                    errors.append(f"component amendment changes decision/state: {eid}/{field}")
            for field in ("component_assessments", "gap_types", "proposed_text"):
                before = amended_fields.get((key, field), item.get(field))
                if event.get(field + "_before") != before:
                    errors.append(f"amendment before snapshot mismatch: {eid}/{field}")
                if field + "_after" not in event:
                    errors.append(f"missing amendment replacement: {eid}/{field}")
                amended_fields[(key, field)] = event.get(field + "_after")
            if not event.get("rationale") or not event.get("evidence"):
                errors.append(f"amendment lacks rationale/evidence: {eid}")
            for evidence in event.get("evidence", []):
                source = sources.get(evidence.get("source_id"))
                if source is None or any(evidence.get(k) != source.get(k) for k in ("url", "source_sha256")):
                    errors.append(f"amendment evidence lineage mismatch: {eid}")
                if not evidence.get("period_binding") or not evidence.get("locator"):
                    errors.append(f"amendment missing period/locator: {eid}")
                note = root / evidence["inspection_note_path"]
                if not note.exists() or text_sha256(note) != evidence.get("inspection_note_sha256"):
                    errors.append(f"amendment inspection note changed/missing: {eid}")
            for component in event.get("component_assessments_after", []):
                ids = component.get("source_ids", [])
                if not set(ids) <= set(sources) or (component["assessment"].startswith("SUPPORTED") and not ids):
                    errors.append(f"amendment component lacks valid sources: {eid}")
    accepted_keys = {(cid, i[2]["normalized_claim_hash"]) for cid, i in authors.items() if i[2]["decision"] == "ACCEPTED"}
    accepted_reviewed = accepted_keys & set(reviewed)
    accepted_decisions = Counter(reviewed[k]["decision"] for k in accepted_reviewed)
    index_path = root / "audit-v5/semantic/accepted-review-index.json"
    if index_path.exists():
        index = read_json(index_path)
        index_items = index.get("items", [])
        index_keys = {(i["claim_id"], i["normalized_claim_hash"]) for i in index_items}
        if index_keys != accepted_reviewed or len(index_items) != len(index_keys):
            errors.append("derived ACCEPTED index key coverage/uniqueness mismatch")
        if index.get("claim_count") != len(accepted_reviewed) or index.get("reviewer_decisions") != dict(accepted_decisions):
            errors.append("derived ACCEPTED index aggregate mismatch")
        cleared = sum(reviewed[k]["final_state"] == "ACCEPTED" for k in accepted_reviewed)
        if index.get("cleared_original_claims") != cleared or index.get("disagreements_pending_adjudication") != len(accepted_reviewed) - cleared:
            errors.append("derived ACCEPTED index final-state counts mismatch")
        for item in index_items:
            key = (item["claim_id"], item["normalized_claim_hash"])
            original = reviewed.get(key)
            if original is None:
                continue
            for field in ("claim", "decision", "final_state", "author_decision", "component_assessments", "gap_types", "proposed_text"):
                if item.get(field) != amended_fields.get((key, field), original.get(field)):
                    errors.append(f"derived index differs from effective ledger: {item['claim_id']}/{field}")
            target = review_paths[key]
            if item.get("reviewer_batch_path") != target.relative_to(root).as_posix() or item.get("reviewer_batch_sha256") != text_sha256(target):
                errors.append(f"derived index reviewer lineage mismatch: {item['claim_id']}")
            if item.get("amendments_applied") != amendment_refs.get(key, []) or item.get("evidence") != original.get("evidence", []) + amendment_evidence.get(key, []):
                errors.append(f"derived index amendment/evidence mismatch: {item['claim_id']}")
    checkpoint_path = root / "audit-v5/semantic/reviewer-checkpoint.json"
    if checkpoint_path.exists():
        checkpoint = read_json(checkpoint_path)
        checkpoint_keys = {(i["claim_id"], i["normalized_claim_hash"]) for i in checkpoint["reviewed_keys"]}
        if checkpoint_keys != set(reviewed) or len(checkpoint["reviewed_keys"]) != len(reviewed):
            errors.append("checkpoint/reviewer key coverage mismatch")
        for field, expected in {
            "queue_claims": len(queue), "independently_reviewed": len(reviewed),
            "remaining_review": len(qmap)-len(reviewed),
            "adjudication_pending": states["ESCALATED_REVIEW_DISAGREEMENT"],
            "final_accepted": states["ACCEPTED"],
        }.items():
            if checkpoint.get(field) != expected:
                errors.append(f"checkpoint count mismatch: {field}")
        if "component_amendments" in checkpoint and checkpoint["component_amendments"] != amendment_count:
            errors.append("checkpoint component amendment count mismatch")
        coverage = checkpoint.get("author_accepted_review")
        if coverage is not None and coverage != {
            "total": len(accepted_keys), "reviewed": len(accepted_reviewed),
            "remaining": len(accepted_keys - set(reviewed)), "reviewer_decisions": dict(accepted_decisions),
        }:
            errors.append("checkpoint author ACCEPTED coverage/count mismatch")
    return {
        "ok": not errors, "errors": errors, "queue_claims": len(queue),
        "author_items": author_count, "unique_author_claims": len(authors),
        "reviewer_claims": len(reviewed), "remaining_independent_review": len(qmap) - len(reviewed),
        "reviewer_decisions": dict(decisions), "reviewer_final_states": dict(states),
        "final_accepted": states["ACCEPTED"], "local_sources_checked": check_local_sources,
        "component_amendments": amendment_count,
        "author_accepted_reviewed": len(accepted_reviewed),
        "author_accepted_total": len(accepted_keys),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--check-local-sources", action="store_true")
    args = parser.parse_args()
    result = validate(args.root.resolve(), check_local_sources=args.check_local_sources)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
