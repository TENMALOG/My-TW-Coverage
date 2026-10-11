#!/usr/bin/env python3
"""Run isolated Hermes/Luna candidate reverifications and append checkpoints."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path, PureWindowsPath
import re
import stat
import subprocess
import sys
import tempfile
import threading
import time
from typing import Any

BASE = Path(__file__).resolve().parents[3]
ROOT = BASE / 'audit-v5/semantic/candidate-rerun'
CACHE = BASE / 'audit-v5/source-cache/candidate-rerun'
QUEUE_PATH = ROOT / 'queue.jsonl'
CHECKPOINT_PATH = ROOT / 'checkpoint.json'
MAX_TURNS = 8
RUN_BUDGET_SECONDS = 420
MODEL = 'gpt-6-luna'
REASONING = 'xhigh'
PROVIDER = 'openai-codex'
STOP_EVENT = threading.Event()

QUEUE_TEXT_FIELDS = (
    'claim_id', 'normalized_claim_hash', 'issuer_ticker', 'issuer_company',
    'report_path', 'claim', 'author_batch_id', 'author_batch_path',
    'author_batch_sha256', 'author_decision',
)
RESULT_CLAIM_IDENTITY_FIELDS = (
    'claim_id', 'normalized_claim_hash', 'issuer_ticker', 'issuer_company',
    'report_path', 'author_batch_id', 'author_batch_path',
    'author_batch_sha256', 'author_decision',
)
ALLOWED_VERDICTS = {'UNKNOWN', 'PARTIAL', 'CANDIDATE_ACCEPTED'}


class PathSafetyError(ValueError):
    """A requested output path is outside its owned tree or traverses a symlink."""


def validate_safe_destination(path: Path, allowed_root: Path, label: str) -> Path:
    """Reject output paths outside BASE or through existing symlink components."""
    base_path = BASE.resolve(strict=True)
    root_path = Path(os.path.abspath(allowed_root))
    destination = Path(os.path.abspath(path))
    try:
        root_path.relative_to(base_path)
        destination.relative_to(root_path)
        relative = destination.relative_to(base_path)
    except ValueError as exc:
        raise PathSafetyError(f'{label} path escapes BASE or its owned output subtree') from exc

    current = base_path
    for index, component in enumerate(relative.parts):
        current = current / component
        try:
            info = current.lstat()
        except FileNotFoundError:
            continue
        except OSError as exc:
            raise PathSafetyError(f'{label} path cannot be inspected safely: {current}') from exc
        if os.path.islink(current):
            raise PathSafetyError(f'{label} path contains a symlink: {current}')
        if index < len(relative.parts) - 1 and not current.is_dir():
            raise PathSafetyError(f'{label} parent is not a directory: {current}')

    try:
        resolved_root = root_path.resolve(strict=False)
        resolved_destination = destination.resolve(strict=False)
        resolved_root.relative_to(base_path)
        resolved_destination.relative_to(resolved_root)
    except (OSError, RuntimeError, ValueError) as exc:
        raise PathSafetyError(f'{label} path resolves outside its owned BASE subtree') from exc
    return destination


def safe_mkdir(path: Path, allowed_root: Path, label: str) -> None:
    destination = validate_safe_destination(path, allowed_root, label)
    try:
        destination.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        raise PathSafetyError(f'{label} directory could not be created safely: {destination}') from exc
    validate_safe_destination(destination, allowed_root, label)
    if not destination.is_dir():
        raise PathSafetyError(f'{label} destination is not a directory: {destination}')


def safe_write_bytes(path: Path, value: bytes, allowed_root: Path, label: str) -> None:
    destination = validate_safe_append_destination(path, allowed_root, label)
    safe_mkdir(destination.parent, allowed_root, f'{label} parent')
    validate_safe_append_destination(destination, allowed_root, label)
    nofollow = getattr(os, 'O_NOFOLLOW', None)
    if nofollow is None:
        raise PathSafetyError(f'{label} cannot be written safely: O_NOFOLLOW is unavailable')
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC | nofollow
    try:
        descriptor = os.open(destination, flags, 0o666)
    except OSError as exc:
        raise PathSafetyError(f'{label} destination could not be opened safely: {destination}') from exc
    with os.fdopen(descriptor, 'wb') as handle:
        handle.write(value)
        handle.flush()
        os.fsync(handle.fileno())


def validate_safe_append_destination(path: Path, allowed_root: Path, label: str) -> Path:
    """Validate a confined append target and reject existing non-file leaves."""
    destination = validate_safe_destination(path, allowed_root, label)
    try:
        info = destination.lstat()
    except FileNotFoundError:
        return destination
    except OSError as exc:
        raise PathSafetyError(f'{label} path cannot be inspected safely: {destination}') from exc
    if not stat.S_ISREG(info.st_mode):
        raise PathSafetyError(f'{label} destination is not a regular file: {destination}')
    return destination


def safe_append_bytes(path: Path, value: bytes, allowed_root: Path, label: str) -> None:
    """Append to a confined regular file without following or truncating its leaf."""
    destination = validate_safe_append_destination(path, allowed_root, label)
    safe_mkdir(destination.parent, allowed_root, f'{label} parent')
    destination = validate_safe_append_destination(destination, allowed_root, label)
    nofollow = getattr(os, 'O_NOFOLLOW', None)
    if nofollow is None:
        raise PathSafetyError(f'{label} cannot be appended safely: O_NOFOLLOW is unavailable')
    flags = os.O_WRONLY | os.O_APPEND | os.O_CREAT | nofollow | getattr(os, 'O_NONBLOCK', 0)
    try:
        descriptor = os.open(destination, flags, 0o666)
    except OSError as exc:
        raise PathSafetyError(f'{label} destination could not be opened safely: {destination}') from exc
    try:
        info = os.fstat(descriptor)
        if not stat.S_ISREG(info.st_mode):
            raise PathSafetyError(f'{label} destination is not a regular file: {destination}')
        # Recheck after workers finish and immediately before writing. The open
        # descriptor also has to match the currently named regular leaf.
        validate_safe_append_destination(destination, allowed_root, label)
        named_info = destination.lstat()
        if (not stat.S_ISREG(named_info.st_mode) or
                (named_info.st_dev, named_info.st_ino) != (info.st_dev, info.st_ino)):
            raise PathSafetyError(f'{label} destination changed before append: {destination}')
        with os.fdopen(descriptor, 'ab') as handle:
            descriptor = -1
            handle.write(value)
            handle.flush()
            os.fsync(handle.fileno())
    except OSError as exc:
        raise PathSafetyError(f'{label} destination could not be appended safely: {destination}') from exc
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def evidence_output_paths(rerun_id: str) -> tuple[Path, Path, Path]:
    evidence_root = ROOT / 'evidence'
    evidence_dir = evidence_root / rerun_id
    manifest_path = evidence_dir / 'manifest.json'
    notes_path = evidence_dir / 'notes.md'
    validate_safe_destination(evidence_root, BASE, 'Evidence root')
    validate_safe_destination(evidence_dir, evidence_root, 'Evidence directory')
    validate_safe_append_destination(manifest_path, evidence_root, 'Evidence manifest')
    validate_safe_append_destination(notes_path, evidence_root, 'Evidence notes')
    return evidence_dir, manifest_path, notes_path


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_queue() -> list[dict[str, Any]]:
    return [json.loads(line) for line in QUEUE_PATH.read_text().splitlines() if line.strip()]


def validate_queue_items(items: Any) -> dict[int, dict[str, Any]]:
    if not isinstance(items, list):
        raise ValueError('Frozen queue must be a JSONL list of objects')
    by_sequence: dict[int, dict[str, Any]] = {}
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f'Invalid frozen queue item at row {index}: expected an object')
        sequence = item.get('queue_sequence')
        if isinstance(sequence, bool) or not isinstance(sequence, int) or sequence <= 0:
            raise ValueError(f'Invalid queue_sequence at row {index}: expected a positive integer')
        if sequence in by_sequence:
            raise ValueError(f'Duplicate queue_sequence in frozen queue: {sequence}')
        for field in QUEUE_TEXT_FIELDS:
            value = item.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f'Invalid frozen queue item at row {index}: {field} must be a nonempty string')
        if re.fullmatch(r'[0-9]{4}', item['issuer_ticker']) is None:
            raise ValueError(f'Invalid issuer_ticker at queue row {index}: expected exactly four ASCII digits')
        by_sequence[sequence] = item
    return by_sequence


def validate_candidate_manifest(row: dict[str, Any], context: str) -> None:
    """Require a candidate's evidence IDs to exist in its safely bound manifest."""
    manifest_ref = row.get('evidence_manifest')
    if not isinstance(manifest_ref, str) or manifest_ref == '' or manifest_ref.isspace():
        raise ValueError(f'{context} CANDIDATE_ACCEPTED requires an evidence_manifest reference')
    if '\\' in manifest_ref or '\x00' in manifest_ref:
        raise ValueError(f'{context} has an invalid evidence_manifest path')

    relative_ref = Path(manifest_ref)
    windows_ref = PureWindowsPath(manifest_ref)
    if (relative_ref.is_absolute() or windows_ref.is_absolute() or windows_ref.drive or
            relative_ref.as_posix() != manifest_ref or '..' in relative_ref.parts):
        raise ValueError(f'{context} has an unsafe evidence_manifest path')

    try:
        base_path = BASE.resolve(strict=True)
        evidence_root = (ROOT / 'evidence').resolve(strict=True)
        manifest_path = (base_path / relative_ref).resolve(strict=True)
    except (OSError, RuntimeError, ValueError) as exc:
        raise ValueError(f'{context} evidence_manifest is missing or unreadable') from exc
    try:
        evidence_root.relative_to(base_path)
    except ValueError as exc:
        raise ValueError(f'{context} evidence subtree escapes BASE') from exc
    try:
        manifest_path.relative_to(evidence_root)
    except ValueError as exc:
        raise ValueError(f'{context} evidence_manifest escapes the workload evidence subtree') from exc
    if not manifest_path.is_file():
        raise ValueError(f'{context} evidence_manifest must be a file')

    try:
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f'{context} evidence_manifest is malformed or unreadable') from exc
    if not isinstance(manifest, dict):
        raise ValueError(f'{context} evidence_manifest must contain a JSON object')

    claim = row.get('claim')
    if (manifest.get('claim_id') != claim.get('claim_id') or
            manifest.get('normalized_claim_hash') != claim.get('normalized_claim_hash')):
        raise ValueError(f'{context} evidence_manifest claim identity mismatch')

    sources = manifest.get('sources')
    if not isinstance(sources, list) or not sources:
        raise ValueError(f'{context} evidence_manifest sources must be a nonempty list')
    source_ids: set[str] = set()
    for index, source in enumerate(sources, 1):
        if not isinstance(source, dict):
            raise ValueError(f'{context} evidence_manifest source {index} must be an object')
        source_id = source.get('source_id')
        if not isinstance(source_id, str) or source_id == '' or source_id.isspace():
            raise ValueError(f'{context} evidence_manifest source {index} has an invalid source_id')
        source_ids.add(source_id)

    for atom_index, atom in enumerate(row['atomic_claims'], 1):
        for evidence_id in atom['evidence_ids']:
            if evidence_id not in source_ids:
                raise ValueError(
                    f'{context} CANDIDATE_ACCEPTED atom {atom_index} has an unknown evidence_id: {evidence_id!r}'
                )


def validate_result_row(row: dict[str, Any], queue_by_sequence: dict[int, dict[str, Any]],
                        context: str) -> None:
    result_id = row.get('rerun_id')
    if (not isinstance(result_id, str) or
            not re.fullmatch(r'\w[\w.-]*', result_id)):
        raise ValueError(f'{context} requires a nonempty, safe rerun_id')
    batch_num(str(row.get('rerun_batch_id')))
    sequence = row.get('queue_sequence')
    if isinstance(sequence, bool) or not isinstance(sequence, int) or sequence <= 0:
        raise ValueError(f'Invalid {context} queue_sequence: expected a positive integer')
    if sequence not in queue_by_sequence:
        raise ValueError(f'{context} queue_sequence {sequence} is not present in frozen queue')
    verdict = row.get('verdict')
    if not isinstance(verdict, str) or verdict not in ALLOWED_VERDICTS:
        raise ValueError(f'Unsupported result verdict: {verdict!r}')
    if verdict == 'CANDIDATE_ACCEPTED':
        atoms = row.get('atomic_claims')
        fully_supported = (
            isinstance(atoms, list) and bool(atoms) and
            all(
                isinstance(atom, dict) and atom.get('status') == 'SUPPORTED' and
                isinstance(atom.get('evidence_ids'), list) and bool(atom['evidence_ids']) and
                all(isinstance(evidence_id, str) and evidence_id != '' and not evidence_id.isspace()
                    for evidence_id in atom['evidence_ids'])
                for atom in atoms
            )
        )
        if (row.get('candidate_accepted') is not True or
                row.get('requires_final_adjudication') is not True or not fully_supported):
            raise ValueError(
                f'{context} CANDIDATE_ACCEPTED requires a true final-adjudication gate and supported evidence'
            )
    recorded_claim = row.get('claim')
    queued_item = queue_by_sequence[sequence]
    if not isinstance(recorded_claim, dict) or any(
        recorded_claim.get(field) != queued_item[field]
        for field in RESULT_CLAIM_IDENTITY_FIELDS
    ):
        raise ValueError(f'{context} claim identity mismatch for queue_sequence {sequence}')
    original_text = recorded_claim.get('original_text')
    if (not isinstance(original_text, str) or
            re.sub(r'\s+', '', original_text) != re.sub(r'\s+', '', queued_item['claim'])):
        raise ValueError(f'{context} original claim text mismatch for queue_sequence {sequence}')
    if verdict == 'CANDIDATE_ACCEPTED':
        validate_candidate_manifest(row, context)


def batch_num(batch_id: str) -> int:
    match = re.fullmatch(r'rerun-(\d{3})', batch_id)
    if not match:
        raise ValueError(f'Invalid batch id: {batch_id!r}; expected rerun-NNN')
    return int(match.group(1))


def read_result_records(queue_items: list[dict[str, Any]] | None = None) -> list[tuple[dict[str, Any], bytes]]:
    queue_by_sequence = validate_queue_items(read_queue() if queue_items is None else queue_items)
    records = []
    seen_result_ids: set[str] = set()
    for path in sorted((ROOT / 'batches').glob('batch-*.jsonl')):
        with path.open('rb') as handle:
            physical_lines = handle.readlines()
        for line_number, raw_line in enumerate(physical_lines, 1):
            if not raw_line.strip():
                continue
            try:
                line = raw_line.decode('utf-8')
                row = json.loads(line)
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                raise ValueError(f'Malformed result ledger row at {path.name}:{line_number}') from exc
            if not isinstance(row, dict) or 'queue_sequence' not in row or 'verdict' not in row:
                raise ValueError(f'Invalid result ledger row at {path.name}:{line_number}')
            try:
                validate_result_row(row, queue_by_sequence, f'result ledger row at {path.name}:{line_number}')
            except ValueError as exc:
                raise ValueError(f'Invalid result ledger row at {path.name}:{line_number}: {exc}') from exc
            if row['rerun_id'] in seen_result_ids:
                raise ValueError(f'Duplicate rerun_id at {path.name}:{line_number}: {row["rerun_id"]}')
            seen_result_ids.add(row['rerun_id'])
            records.append((row, raw_line))
    return records


def read_result_rows(queue_items: list[dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    return [row for row, _raw_line in read_result_records(queue_items)]


def effective_result_projection(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return the latest appended row for each queue sequence, preserving first-seen order."""
    found: dict[int, dict[str, Any]] = {}
    for row in rows:
        found[row['queue_sequence']] = row
    return list(found.values())


def all_results(queue_items: list[dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    return effective_result_projection(read_result_rows(queue_items))


def atomic_write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f'.{path.name}.', suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write('\n')
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def checkpoint_from_results(checkpoint: dict[str, Any], rows: list[dict[str, Any]],
                            current_batch: str | None = None,
                            latest_result: dict[str, Any] | None = None,
                            latest_result_line: bytes | None = None) -> dict[str, Any]:
    effective = effective_result_projection(rows)
    queued_ids = {row['queue_sequence'] for row in effective}
    through = 0
    while through + 1 in queued_ids:
        through += 1
    counts = {'PARTIAL': 0, 'CANDIDATE_ACCEPTED': 0, 'UNKNOWN': 0}
    batch_counts: dict[str, int] = {}
    for row in effective:
        verdict = row['verdict']
        counts[verdict] = counts.get(verdict, 0) + 1
        batch_id = str(row['rerun_batch_id'])
        batch_counts[batch_id] = batch_counts.get(batch_id, 0) + 1
    updated = dict(checkpoint)
    updated.update({
        'updated_at': now_utc(),
        'processed': len(queued_ids),
        'remaining': int(checkpoint['queued']) - len(queued_ids),
        'verdict_counts': counts,
        'completed_through_sequence': through,
    })
    if current_batch is not None:
        updated['current_rerun_batch'] = current_batch
        updated['current_batch_processed'] = batch_counts.get(current_batch, 0)
    if latest_result is not None:
        updated['latest_result_id'] = latest_result['rerun_id']
        if latest_result_line is None:
            raise ValueError('Exact physical ledger bytes are required for latest-result hashing')
        updated['latest_result_sha256'] = sha_bytes(latest_result_line)
    else:
        updated.pop('latest_result_id', None)
        updated.pop('latest_result_sha256', None)
    return updated


def validate_checkpoint_queue_count(checkpoint: Any,
                                    queue_by_sequence: dict[int, dict[str, Any]]) -> None:
    if not isinstance(checkpoint, dict):
        raise ValueError('Checkpoint must contain a JSON object')
    queued = checkpoint.get('queued')
    if type(queued) is not int or queued < 0:
        raise ValueError('Invalid checkpoint queued value: expected a nonnegative integer')
    actual_count = len(queue_by_sequence)
    if queued != actual_count:
        raise ValueError(
            f'Checkpoint queued count mismatch: checkpoint queued={queued}, '
            f'frozen queue count={actual_count}'
        )


def reconcile_checkpoint(queue_items: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    """Rebuild stale checkpoint counters from the valid append-only ledger."""
    lock_path = ROOT / 'runtime' / 'persist.lock'
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open('a+') as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        checkpoint = json.loads(CHECKPOINT_PATH.read_text(encoding='utf-8'))
        frozen_items = read_queue() if queue_items is None else queue_items
        queue_by_sequence = validate_queue_items(frozen_items)
        validate_checkpoint_queue_count(checkpoint, queue_by_sequence)
        physical_records = read_result_records(frozen_items)
        if not physical_records and checkpoint.get('processed', 0) > 0:
            raise ValueError(
                'Checkpoint reports processed results but result ledger is empty; possible data loss or inconsistency.'
            )
        physical_rows = [row for row, _raw_line in physical_records]
        latest, latest_line = physical_records[-1] if physical_records else (None, None)
        current_batch = str(checkpoint.get('current_rerun_batch')) if checkpoint.get('current_rerun_batch') else None
        reconciled = checkpoint_from_results(
            checkpoint, physical_rows, current_batch, latest, latest_line
        )
        fields = ('processed', 'remaining', 'verdict_counts', 'completed_through_sequence',
                  'current_batch_processed', 'latest_result_id', 'latest_result_sha256')
        if any(checkpoint.get(key) != reconciled.get(key) for key in fields):
            atomic_write_json(CHECKPOINT_PATH, reconciled)
        else:
            reconciled['updated_at'] = checkpoint.get('updated_at')
        return reconciled


def make_prompt(item: dict[str, Any]) -> str:
    contract = """You are a re-verification candidate worker. This is one isolated claim context; do not use or infer facts from any other queue item.

Task contract:
- You are not the final acceptance authority. Never output final ACCEPTED.
- Allowed overall verdicts: UNKNOWN, PARTIAL, CANDIDATE_ACCEPTED. Use CANDIDATE_ACCEPTED only when the complete original wording is fully supported and set candidate_accepted=true and requires_final_adjudication=true.
- Break compound wording into atomic claims. For each atom bind source, period, market definition, denominator, and units. UNKNOWN is a successful result. Do not turn absence of evidence into negative evidence or substitute nearby years, sales mix, shipment/customer examples, channel mix, financed capacity, cumulative values, or a different market denominator for the claim.
- Prefer current official issuer disclosures and regulator/filing sources; attribute secondary sources. Search up to 8 focused tool/research turns, then stop with unresolved atoms as UNKNOWN. Do not invent sources, locators, dates, rankings, or measurements. Search snippets are discovery leads only. Never repeat an identical web query or the same failing tool call; after 3 non-progressing search calls, change the query, source, language, or method, or stop. If a tool loop guardrail/error occurs, return the required JSON with unresolved atoms UNKNOWN and explain the tool limitation. Always return the JSON object even if research tools fail.
- Do not edit files. Return only one valid JSON object. Required top-level fields: overall, candidate_accepted, requires_final_adjudication, research_exhausted, atomic_claims, revised_claim, source_caveats, research_stop_reason.
- atomic_claims is an array of objects with text, status (SUPPORTED/CONTRADICTED/UNKNOWN), period, note, and sources. Each source has source_title, url, publication_date (or null), effective_period (or null), source_level (3 official primary, 2 reputable secondary, 1 other/LLM summary), locator, and note.
- If no reliable evidence resolves an atom, mark UNKNOWN and explain the missing scope/period/denominator. CANDIDATE_ACCEPTED is only a candidate for later adjudication; never call it final ACCEPTED.
"""
    return contract + '\nIsolated queue item:\n' + json.dumps(item, ensure_ascii=False, separators=(',', ':')) + '\n'


def parse_response(stdout: str) -> dict[str, Any]:
    decoder = json.JSONDecoder()
    for index, char in enumerate(stdout):
        if char != '{':
            continue
        try:
            obj, _end = decoder.raw_decode(stdout[index:])
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict) and 'overall' in obj and 'atomic_claims' in obj:
            return obj
    raise ValueError('Hermes response did not contain the required JSON object')


def slug(text: str, fallback: str) -> str:
    value = re.sub(r'[^a-zA-Z0-9._-]+', '-', text.strip()).strip('-._').lower()
    return (value or fallback)[:72]


def normalize_sources(raw_sources: Any, atom: dict[str, Any], item: dict[str, Any]) -> list[dict[str, Any]]:
    if not isinstance(raw_sources, list):
        raw_sources = []
    # Accept the compact source shape used by the pilot as well.
    if not raw_sources and atom.get('url'):
        raw_sources = [{
            'source_title': atom.get('source_title'), 'url': atom.get('url'),
            'publication_date': atom.get('publication_date'),
            'effective_period': atom.get('period'), 'locator': atom.get('locator'),
            'note': atom.get('note'), 'source_level': atom.get('source_level')
        }]
    normalized = []
    for src in raw_sources:
        if not isinstance(src, dict):
            continue
        url = str(src.get('url') or '').strip()
        title = str(src.get('source_title') or src.get('title') or '').strip()
        if not url or not title:
            continue
        effective_period = src.get('effective_period') or src.get('period')
        normalized_source = {
            'title': title,
            'url': url,
            'source_level': src.get('source_level') if isinstance(src.get('source_level'), int) else None,
            'publication_date': src.get('publication_date'),
            'effective_period': effective_period,
            'locator': src.get('locator'),
            'source_sha256': src.get('source_sha256'),
            'raw_path': src.get('raw_path'),
            'raw_capture_status': 'referenced_by_Hermes_web_tool',
            'note': src.get('note')
        }
        stable_metadata = {
            key: value for key, value in normalized_source.items()
            if key != 'raw_capture_status'
        }
        binding_bytes = json.dumps(stable_metadata, ensure_ascii=False, sort_keys=True,
                                   separators=(',', ':')).encode('utf-8')
        source_id = 'src-' + hashlib.sha256(binding_bytes).hexdigest()[:20]
        normalized.append({'source_id': source_id, **normalized_source})
    return normalized


def relative_to_base(path: Path) -> str:
    try:
        return path.resolve().relative_to(BASE.resolve()).as_posix()
    except ValueError:
        return str(path)


def output_bytes(value: Any) -> bytes:
    if isinstance(value, bytes):
        return value
    if isinstance(value, bytearray):
        return bytes(value)
    return str(value or '').encode('utf-8')


def positive_seconds(value: str) -> int:
    try:
        seconds = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError('must be a positive integer number of seconds') from exc
    if seconds <= 0:
        raise argparse.ArgumentTypeError('must be a positive integer number of seconds')
    return seconds


def process_item(item: dict[str, Any], attempt_limit: int, run_batch_id: str,
                 superseding_pass: bool,
                 run_budget_seconds: int = RUN_BUDGET_SECONDS) -> tuple[dict[str, Any] | None, str | None]:
    sequence_by_id = validate_queue_items([item])
    seq = next(iter(sequence_by_id))
    batch_num(run_batch_id)
    ticker = item['issuer_ticker']
    rerun_id = f'{run_batch_id}-{seq:06d}' if superseding_pass else f'rerun-{seq:06d}'
    evidence_dir, manifest_path, notes_path = evidence_output_paths(rerun_id)
    cache_root = validate_safe_destination(CACHE, BASE, 'CACHE root').resolve(strict=False)
    candidate_dir = CACHE / ticker / str(seq) / run_batch_id
    source_dir = candidate_dir.resolve(strict=False)
    try:
        source_dir.relative_to(cache_root)
    except ValueError as exc:
        raise PathSafetyError('Candidate source_dir escapes CACHE') from exc
    validate_safe_destination(candidate_dir, CACHE, 'Candidate source_dir')
    prompt_path = candidate_dir / 'isolated-prompt.txt'
    prompt_bytes = make_prompt(item).encode('utf-8')
    validate_safe_append_destination(prompt_path, CACHE, 'Cache prompt')
    if STOP_EVENT.is_set():
        return None, 'SKIPPED_GLOBAL_STOP: another worker detected an auth or usage-limit failure.'
    safe_mkdir(source_dir, CACHE, 'Candidate source_dir')
    # Refuse symlinked previous artifacts too, even when a stdout symlink would
    # otherwise make the attempt counter advance past it.
    prior_attempts = []
    attempt_pattern = re.compile(r'hermes-attempt-(\d+)\.(?:stdout|stderr)\.txt')
    for path in source_dir.glob('hermes-attempt-*.*.txt'):
        match = attempt_pattern.fullmatch(path.name)
        if match:
            validate_safe_append_destination(path, source_dir, f'Cache attempt output {path.name}')
            prior_attempts.append(int(match.group(1)))
    first_attempt = max(prior_attempts, default=0) + 1
    attempt_numbers = range(first_attempt, first_attempt + attempt_limit)
    for attempt in attempt_numbers:
        validate_safe_append_destination(
            source_dir / f'hermes-attempt-{attempt}.stdout.txt',
            source_dir,
            'Cache attempt stdout',
        )
        validate_safe_append_destination(
            source_dir / f'hermes-attempt-{attempt}.stderr.txt',
            source_dir,
            'Cache attempt stderr',
        )
    safe_write_bytes(prompt_path, prompt_bytes, source_dir, 'Cache prompt')
    last_error = None
    response: dict[str, Any] | None = None
    raw_stdout = b''
    raw_stderr = b''
    successful_attempt: int | None = None
    for attempt in range(first_attempt, first_attempt + attempt_limit):
        stdout_path = source_dir / f'hermes-attempt-{attempt}.stdout.txt'
        stderr_path = source_dir / f'hermes-attempt-{attempt}.stderr.txt'
        validate_safe_append_destination(stdout_path, source_dir, 'Cache attempt stdout')
        validate_safe_append_destination(stderr_path, source_dir, 'Cache attempt stderr')
        command = [
            'hermes', 'chat', '--query-file', str(prompt_path), '--oneshot', '--quiet',
            '--provider', PROVIDER, '--model', MODEL, '--reasoning', REASONING, '--toolsets', 'web',
            '--max-turns', str(MAX_TURNS), '--run-budget', str(run_budget_seconds),
            '--ignore-rules'
        ]
        try:
            proc = subprocess.run(command, cwd=BASE, capture_output=True,
                                  timeout=run_budget_seconds + 45)
            raw_stdout, raw_stderr = output_bytes(proc.stdout), output_bytes(proc.stderr)
            validate_safe_append_destination(stdout_path, source_dir, 'Cache attempt stdout')
            validate_safe_append_destination(stderr_path, source_dir, 'Cache attempt stderr')
            safe_write_bytes(stdout_path, raw_stdout, source_dir, 'Cache attempt stdout')
            if raw_stderr:
                safe_write_bytes(stderr_path, raw_stderr, source_dir, 'Cache attempt stderr')
            tool_text = (raw_stdout + b'\n' + raw_stderr).decode('utf-8', errors='replace').lower()
            if 'http 429' in tool_text or 'usage limit has been reached' in tool_text or 'rate limit reached' in tool_text:
                STOP_EVENT.set()
                return None, 'GLOBAL_STOP: Hermes reported a 429 or usage-limit response; stop issuing requests and resume after quota reset.'
            if 'http 401' in tool_text or 'invalidated oauth token' in tool_text or 'unauthorized' in tool_text:
                STOP_EVENT.set()
                return None, 'GLOBAL_STOP: Hermes reported an authentication failure; stop issuing requests and restore auth before resuming.'
            response = parse_response(raw_stdout.decode('utf-8', errors='replace'))
            if proc.returncode != 0:
                last_error = f'Hermes exited with status {proc.returncode}; final JSON was still present.'
            else:
                last_error = None
            successful_attempt = attempt
            break
        except PathSafetyError:
            raise
        except Exception as exc:  # retain failure details and retry the isolated item
            last_error = f'{type(exc).__name__}: {exc}'
            if attempt < first_attempt + attempt_limit - 1:
                time.sleep(min(12 * attempt, 30))
    if response is None:
        return None, last_error or 'No response'

    atoms = response.get('atomic_claims')
    if not isinstance(atoms, list) or not atoms:
        return None, 'Response JSON contained no atomic_claims'
    clean_atoms = []
    manifest_sources: dict[str, dict[str, Any]] = {}
    for atom in atoms:
        if not isinstance(atom, dict) or not atom.get('text'):
            return None, 'An atomic claim was missing its text'
        status = str(atom.get('status', 'UNKNOWN')).upper()
        if status == 'ACCEPTED':
            status = 'SUPPORTED'
        if status not in {'SUPPORTED', 'CONTRADICTED', 'UNKNOWN'}:
            return None, f'Unexpected atom status: {status}'
        atom_sources = normalize_sources(atom.get('sources'), atom, item)
        if status == 'SUPPORTED' and not atom_sources:
            return None, 'SUPPORTED atom has no usable source URL/title; invalid worker output, not a factual UNKNOWN'
        for source in atom_sources:
            manifest_sources[source['source_id']] = source
        clean_atoms.append({
            'text':str(atom['text']),
            'status':status,
            'period':atom.get('period'),
            'evidence_ids':[src['source_id'] for src in atom_sources],
            'note':atom.get('note')
        })

    overall = str(response.get('overall', 'UNKNOWN')).upper()
    if overall in {'ACCEPTED', 'SUPPORTED'}:
        overall = 'CANDIDATE_ACCEPTED'
    if overall == 'PARTIALLY_SUPPORTED':
        overall = 'PARTIAL'
    if overall not in {'UNKNOWN', 'PARTIAL', 'CANDIDATE_ACCEPTED'}:
        return None, f'Unexpected overall verdict: {overall}'
    apparent_candidate = bool(response.get('candidate_accepted')) or bool(response.get('requires_final_adjudication'))
    if apparent_candidate:
        overall = 'CANDIDATE_ACCEPTED'
    if overall == 'CANDIDATE_ACCEPTED':
        fully_supported = all(a['status'] == 'SUPPORTED' and a['evidence_ids'] for a in clean_atoms)
        if not fully_supported:
            overall = 'PARTIAL' if any(a['status'] == 'SUPPORTED' for a in clean_atoms) else 'UNKNOWN'
    candidate = overall == 'CANDIDATE_ACCEPTED'
    revised = str(response.get('revised_claim') or '').strip() or None

    stdout_path = source_dir / f'hermes-attempt-{successful_attempt}.stdout.txt'
    execution = {
        'execution_batch_id':run_batch_id,
        'successful_attempt':successful_attempt,
        'hermes_raw_output':relative_to_base(stdout_path),
        'hermes_raw_output_sha256':sha_bytes(raw_stdout),
        'prompt_path':relative_to_base(prompt_path),
        'prompt_sha256':sha_bytes(prompt_bytes),
        'requested_provider':PROVIDER,
        'requested_model':MODEL,
        'requested_reasoning':REASONING,
        'requested_oneshot':True,
        'requested_toolsets':['web'],
        'requested_max_turns':MAX_TURNS,
        'observed_model':None,
        'resolved_model':None,
        'run_budget_seconds':run_budget_seconds,
        'subprocess_timeout_seconds':run_budget_seconds + 45,
        'warning':last_error,
    }

    manifest = {
        'schema':'semantic-candidate-evidence-manifest-1',
        'rerun_id':rerun_id,
        'claim_id':item['claim_id'],
        'normalized_claim_hash':item['normalized_claim_hash'],
        'accessed_date':now_utc()[:10],
        'sources':list(manifest_sources.values()),
        'search_notes':[
            f'Isolated Hermes CLI request configured for provider={PROVIDER}, model={MODEL}, reasoning={REASONING}, with web tools.',
            str(response.get('research_stop_reason') or 'No research stop reason returned.'),
            *[str(note) for note in (response.get('source_caveats') or [])]
        ],
        **execution,
    }
    notes_lines = [f'# 重驗筆記 — {item["issuer_company"]} / {item["claim_id"]}', '',
                   f'原始 claim：{item["claim"]}', '', '## 原子主張', '']
    for number, atom in enumerate(clean_atoms, 1):
        notes_lines.append(f'{number}. `{atom["status"]}` — {atom["text"]}')
        if atom.get('period'):
            notes_lines.append(f'   期間：{atom["period"]}')
        if atom.get('note'):
            notes_lines.append(f'   說明：{atom["note"]}')
        for source_id in atom['evidence_ids']:
            src = manifest_sources[source_id]
            notes_lines.append(f'   來源：[{src["title"]}]({src["url"]})；定位：{src.get("locator") or "未提供"}')
    notes_lines += ['', '## 判定', '', f'Overall `{overall}`。']
    if revised:
        notes_lines += ['', f'建議改寫：{revised}']
    caveats = response.get('source_caveats') or []
    if caveats:
        notes_lines += ['', '來源限制：']
        notes_lines.extend(f'- {caveat}' for caveat in caveats)
    notes_lines += ['', str(response.get('research_stop_reason') or ''), '',
                    '此紀錄來自獨立 Hermes 單筆重驗。只追加候選重驗結果，未修改原報告、作者決策或既有複核帳本。', '']
    # Validate every evidence destination again after the external request. The
    # no-follow leaf opens also refuse a symlink swapped in immediately before
    # each file write.
    evidence_dir, manifest_path, notes_path = evidence_output_paths(rerun_id)
    safe_mkdir(evidence_dir, ROOT / 'evidence', 'Evidence directory')
    evidence_output_paths(rerun_id)
    safe_write_bytes(
        manifest_path,
        (json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode('utf-8'),
        ROOT / 'evidence',
        'Evidence manifest',
    )
    safe_write_bytes(notes_path, '\n'.join(notes_lines).encode('utf-8'), ROOT / 'evidence', 'Evidence notes')

    result = {
        'schema':'semantic-candidate-rerun-result-1',
        'rerun_id':rerun_id,
        'queue_sequence':seq,
        'rerun_batch_id':run_batch_id,
        'worker_role':'reverification_candidate_worker',
        'model_identifier':None,
        **execution,
        'execution_warning':last_error,
        'reviewed_at':now_utc(),
        'claim':{
            'claim_id':item['claim_id'],
            'normalized_claim_hash':item['normalized_claim_hash'],
            'issuer_ticker':item['issuer_ticker'],
            'issuer_company':item['issuer_company'],
            'report_path':item['report_path'],
            'original_text':item['claim'],
            'author_batch_id':item['author_batch_id'],
            'author_batch_path':item['author_batch_path'],
            'author_batch_sha256':item['author_batch_sha256'],
            'author_decision':item['author_decision']
        },
        'atomic_claims':clean_atoms,
        'overall':overall,
        'revised_claim':revised,
        'revised_claim_status':'CANDIDATE_REQUIRES_FINAL_ADJUDICATION' if candidate else ('SUPPORTED_WITH_QUALIFIERS' if revised and overall == 'PARTIAL' else overall),
        'candidate_accepted':candidate,
        'requires_final_adjudication':candidate,
        'research_exhausted':bool(response.get('research_exhausted', False)),
        'research_stop_reason':response.get('research_stop_reason'),
        'source_caveats':caveats,
        'evidence_manifest':f'audit-v5/semantic/candidate-rerun/evidence/{rerun_id}/manifest.json',
        'inspection_notes':f'audit-v5/semantic/candidate-rerun/evidence/{rerun_id}/notes.md',
        'author_ledger_modified':False,
        'report_modified':False,
        'verdict':overall
    }
    return result, last_error


def persist_result(result: dict[str, Any], allow_superseding: bool = False) -> bool:
    verdict = result.get('verdict')
    if not isinstance(verdict, str) or verdict not in ALLOWED_VERDICTS:
        raise ValueError(f'Unsupported persistence verdict: {verdict!r}')
    if verdict == 'CANDIDATE_ACCEPTED':
        atoms = result.get('atomic_claims')
        fully_supported = (
            isinstance(atoms, list) and bool(atoms) and
            all(
                isinstance(atom, dict) and atom.get('status') == 'SUPPORTED' and
                isinstance(atom.get('evidence_ids'), list) and bool(atom['evidence_ids']) and
                all(isinstance(evidence_id, str) and evidence_id != '' and not evidence_id.isspace()
                    for evidence_id in atom['evidence_ids'])
                for atom in atoms
            )
        )
        if (result.get('candidate_accepted') is not True or
                result.get('requires_final_adjudication') is not True or not fully_supported):
            raise ValueError(
                'CANDIDATE_ACCEPTED requires a true final-adjudication gate and supported evidence'
            )
    queue_items = read_queue()
    queue_by_sequence = validate_queue_items(queue_items)
    validate_result_row(result, queue_by_sequence, 'new result')
    seq = result['queue_sequence']
    lock_path = ROOT / 'runtime' / 'persist.lock'
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open('a+') as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        checkpoint = json.loads(CHECKPOINT_PATH.read_text(encoding='utf-8'))
        validate_checkpoint_queue_count(checkpoint, queue_by_sequence)
        physical_rows = read_result_rows(queue_items)
        existing = effective_result_projection(physical_rows)
        if not existing and checkpoint.get('processed', 0) > 0:
            raise ValueError(
                'Checkpoint reports processed results but result ledger is empty; possible data loss or inconsistency.'
            )
        if any(row['queue_sequence'] == seq for row in existing) and not allow_superseding:
            return False
        prior = next((row for row in existing if row['queue_sequence'] == seq), None)
        if prior == result:
            return False
        if any(row['rerun_id'] == result['rerun_id'] for row in physical_rows):
            raise ValueError(f'Duplicate rerun_id cannot be appended: {result["rerun_id"]}')
        output_batch_num = batch_num(str(result['rerun_batch_id']))
        batch_path = ROOT / 'batches' / f'batch-{output_batch_num:03d}.jsonl'
        line = (json.dumps(result, ensure_ascii=False, separators=(',', ':')) + '\n').encode('utf-8')
        with batch_path.open('ab') as handle:
            handle.write(line)
            handle.flush()
            os.fsync(handle.fileno())
        effective = effective_result_projection(existing + [result])
        checkpoint = checkpoint_from_results(
            checkpoint, effective, str(result['rerun_batch_id']), result, line
        )
        atomic_write_json(CHECKPOINT_PATH, checkpoint)
        return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--attempts', type=int, default=2)
    parser.add_argument('--run-budget', type=positive_seconds, default=RUN_BUDGET_SECONDS,
                        metavar='SECONDS', help='Hermes per-run budget (default: 420 seconds).')
    parser.add_argument('--max-sequence', type=int, default=None)
    parser.add_argument('--rerun-sequences', default=None,
                        help='Explicit comma-separated sequence IDs/ranges to supersede, e.g. 1-50,793-795.')
    parser.add_argument('--batch-id', default=None,
                        help='Stable rerun-NNN ID; required with --rerun-sequences and reused on resume.')
    args = parser.parse_args()
    if not 1 <= args.workers <= 10:
        parser.error('--workers must be between 1 and 10')
    if args.rerun_sequences and not args.batch_id:
        parser.error('--batch-id rerun-NNN is required with --rerun-sequences so interrupted superseding passes can resume safely.')
    if args.rerun_sequences and args.max_sequence is not None:
        parser.error('--max-sequence cannot be combined with --rerun-sequences')
    try:
        queue = read_queue()
        queue_by_sequence = validate_queue_items(queue)
    except ValueError as exc:
        parser.error(f'Invalid frozen queue: {exc}')
    try:
        run_batch_id = args.batch_id or str(json.loads(CHECKPOINT_PATH.read_text())['current_rerun_batch'])
        run_batch_num = batch_num(run_batch_id)
    except (ValueError, KeyError) as exc:
        parser.error(str(exc))
    superseding_pass = bool(args.rerun_sequences)
    ROOT.joinpath('runtime').mkdir(parents=True, exist_ok=True)
    run_lock = (ROOT / 'runtime' / 'runner.lock').open('a+')
    try:
        fcntl.flock(run_lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print('Another candidate rerun batch process holds runner.lock.', file=sys.stderr)
        run_lock.close()
        return 2
    checkpoint = json.loads(CHECKPOINT_PATH.read_text())
    actual_queue_hash = sha_bytes(QUEUE_PATH.read_bytes())
    if actual_queue_hash != checkpoint['queue_sha256']:
        print('Frozen queue hash mismatch; aborting without writing results.', file=sys.stderr)
        run_lock.close()
        return 3
    if not superseding_pass and args.batch_id and run_batch_id != checkpoint.get('current_rerun_batch'):
        parser.error(f'Normal resume must use checkpoint batch {checkpoint.get("current_rerun_batch")}; use --rerun-sequences for a superseding pass.')
    checkpoint = reconcile_checkpoint(queue)
    latest = {row['queue_sequence']:row for row in all_results(queue)}
    if superseding_pass:
        try:
            requested = set()
            for part in args.rerun_sequences.split(','):
                part = part.strip()
                if not part:
                    continue
                bounds = part.split('-', 1)
                start = int(bounds[0])
                end = int(bounds[1]) if len(bounds) == 2 else start
                if start < 1 or end < start:
                    raise ValueError(f'Invalid sequence range: {part!r}')
                requested.update(range(start, end + 1))
        except ValueError as exc:
            parser.error(f'Invalid --rerun-sequences: {exc}')
        queued = set(queue_by_sequence)
        unknown = sorted(requested - queued)
        if unknown:
            parser.error(f'Sequence IDs not present in frozen queue: {unknown[:20]}')
        existing_batches = sorted((ROOT / 'batches').glob('batch-*.jsonl'))
        max_batch_num = max((int(path.stem.split('-')[-1]) for path in existing_batches), default=0)
        if run_batch_num not in {max_batch_num, max_batch_num + 1}:
            parser.error(f'--batch-id must be current batch rerun-{max_batch_num:03d} (resume) or next batch rerun-{max_batch_num + 1:03d}.')
        current_batch_path = ROOT / 'batches' / f'batch-{run_batch_num:03d}.jsonl'
        already_in_pass = set()
        if current_batch_path.exists():
            already_in_pass = {json.loads(line)['queue_sequence'] for line in current_batch_path.read_text().splitlines() if line.strip()}
        pending = [item for item in queue if item['queue_sequence'] in requested
                   and item['queue_sequence'] not in already_in_pass]
    else:
        done = set(latest)
        pending = [item for item in queue if item['queue_sequence'] not in done
                   and (args.max_sequence is None or item['queue_sequence'] <= args.max_sequence)]
    failure_path = CACHE / 'runner-failures.jsonl'
    if pending:
        try:
            validate_safe_destination(CACHE, BASE, 'CACHE root')
            validate_safe_destination(failure_path.parent, CACHE, 'Runner failure log parent')
            validate_safe_append_destination(failure_path, CACHE, 'Runner failure log')
        except PathSafetyError as exc:
            print(f'Refusing unsafe runner failure log destination: {exc}', file=sys.stderr)
            run_lock.close()
            return 1
    print(f'Starting {len(pending)} isolated claims with {args.workers} workers; provider={PROVIDER}, model={MODEL}, reasoning={REASONING}, max_turns={MAX_TURNS}, run_budget={args.run_budget}s, batch={run_batch_id}.', flush=True)
    failures = []
    completed_now = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        future_items = {pool.submit(process_item, item, args.attempts, run_batch_id, superseding_pass, args.run_budget): item for item in pending}
        for future in as_completed(future_items):
            item = future_items[future]
            try:
                result, warning = future.result()
                if result is None:
                    if warning and warning.startswith('SKIPPED_GLOBAL_STOP:'):
                        continue
                    failures.append({'sequence':item['queue_sequence'], 'claim_id':item['claim_id'], 'error':warning})
                    label = 'PAUSED' if warning and warning.startswith('GLOBAL_STOP:') else 'FAILED'
                    print(f'{label} seq={item["queue_sequence"]}: {warning}', flush=True)
                    continue
                wrote = persist_result(result, allow_superseding=superseding_pass)
                if wrote:
                    completed_now += 1
                    if warning:
                        print(f'COMPLETED seq={item["queue_sequence"]} verdict={result["verdict"]} (Hermes exit note: {warning})', flush=True)
                    else:
                        print(f'COMPLETED seq={item["queue_sequence"]} verdict={result["verdict"]}', flush=True)
            except Exception as exc:
                failures.append({'sequence':item['queue_sequence'], 'claim_id':item['claim_id'], 'error':f'{type(exc).__name__}: {exc}'})
                print(f'FAILED seq={item["queue_sequence"]}: {type(exc).__name__}: {exc}', flush=True)
    if failures:
        try:
            failure_rows = []
            for entry in failures:
                entry['failed_at'] = now_utc()
                failure_rows.append(json.dumps(entry, ensure_ascii=False) + '\n')
            safe_append_bytes(
                failure_path,
                ''.join(failure_rows).encode('utf-8'),
                CACHE,
                'Runner failure log',
            )
        except PathSafetyError as exc:
            print(f'Could not safely append runner failure log; run remains failed: {exc}', file=sys.stderr)
    summary = json.loads(CHECKPOINT_PATH.read_text())
    print(json.dumps({'completed_this_run':completed_now, 'failures_this_run':len(failures), 'processed':summary['processed'], 'remaining':summary['remaining'], 'verdict_counts':summary['verdict_counts']}, ensure_ascii=False), flush=True)
    run_lock.close()
    return 0 if not failures else 1

if __name__ == '__main__':
    raise SystemExit(main())
