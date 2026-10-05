"""Append-only persistence helpers for transient semantic-source retrieval failures.

This module does not fetch sources or decide claim semantics. A later local
worker may append a second observation to an existing queue entry; it must not
replace the Codex Cloud observation.
"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import tempfile
from typing import Any


QUEUE_SCHEMA = "semantic-local-recheck-queue-1"
PENDING_STATE = "LOCAL_RECHECK_PENDING"


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def stable_recheck_id(
    claim_id: str,
    normalized_claim_hash: str,
    attempted_url: str,
    failure_signature: str,
) -> str:
    """Return a stable id for claim + exact URL + materially identical failure."""
    identity = {
        "claim_id": claim_id,
        "normalized_claim_hash": normalized_claim_hash,
        "attempted_url": attempted_url,
        "failure_signature": failure_signature,
    }
    return _sha256(_canonical_json(identity))


def _observation_id(observation: dict[str, Any]) -> str:
    return _sha256(_canonical_json(observation))


def _load_queue(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"schema": QUEUE_SCHEMA, "updated_at": None, "items": []}
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != QUEUE_SCHEMA or not isinstance(data.get("items"), list):
        raise ValueError(f"Unsupported local recheck queue: {path}")
    return data


def _write_queue(path: Path, queue: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    queue["updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(queue, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def append_observation(path: str | Path, recheck_id: str, observation: dict[str, Any]) -> bool:
    """Append an immutable observation; return False for an exact duplicate."""
    queue_path = Path(path)
    queue = _load_queue(queue_path)
    entry = next((item for item in queue["items"] if item.get("recheck_id") == recheck_id), None)
    if entry is None:
        raise KeyError(f"Unknown recheck id: {recheck_id}")
    observation = dict(observation)
    observation.setdefault("observation_id", _observation_id(observation))
    if any(x.get("observation_id") == observation["observation_id"] for x in entry["observations"]):
        return False
    entry["observations"].append(observation)
    _write_queue(queue_path, queue)
    return True


def record_failure(path: str | Path, failure: dict[str, Any]) -> tuple[str, bool]:
    """Idempotently add a pending failure and append its observation.

    Required failure fields: claim_id, normalized_claim_hash, issuer,
    claim_text, attempted_url, source_host, failure_signature,
    semantic_consequence, and observation.
    """
    required = (
        "claim_id", "normalized_claim_hash", "issuer", "claim_text",
        "attempted_url", "source_host", "failure_signature",
        "semantic_consequence", "observation",
    )
    missing = [key for key in required if key not in failure]
    if missing:
        raise ValueError(f"Missing failure fields: {', '.join(missing)}")

    recheck_id = stable_recheck_id(
        failure["claim_id"], failure["normalized_claim_hash"],
        failure["attempted_url"], failure["failure_signature"],
    )
    queue_path = Path(path)
    queue = _load_queue(queue_path)
    entry = next((item for item in queue["items"] if item.get("recheck_id") == recheck_id), None)
    identity = {
        "recheck_id": recheck_id,
        "claim_id": failure["claim_id"],
        "normalized_claim_hash": failure["normalized_claim_hash"],
        "issuer": failure["issuer"],
        "claim_text": failure["claim_text"],
        "attempted_url": failure["attempted_url"],
        "source_host": failure["source_host"],
        "failure_signature": failure["failure_signature"],
        "queue_state": PENDING_STATE,
        "semantic_consequence": failure["semantic_consequence"],
        "observations": [],
    }
    if entry is None:
        queue["items"].append(identity)
        entry = queue["items"][-1]
    else:
        for key, value in identity.items():
            if key != "observations" and entry.get(key) != value:
                raise ValueError(f"Conflicting data for existing recheck id {recheck_id}: {key}")

    observation = dict(failure["observation"])
    observation.setdefault("observation_id", _observation_id(observation))
    added = not any(x.get("observation_id") == observation["observation_id"] for x in entry["observations"])
    if added:
        entry["observations"].append(observation)
        _write_queue(queue_path, queue)
    return recheck_id, added
