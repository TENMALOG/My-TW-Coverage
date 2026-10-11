#!/usr/bin/env python3
"""One isolated read-only Codex research run per company (no prior verdicts supplied).

Outputs are research proposals only: ACCEPTED statements and new facts still need an
independent verification run and primary source review before publication.

  python run_company_research.py --batch company-research-aero-001 [--only 2630]
"""
from __future__ import annotations

import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from run_revision_batch import (BASE, CACHE_ROOT, CONTROLLER_SHA256, EFFORT, HERE, MODEL, digest, now, quota_hit, rel,
                                write_json)
import re
import shutil
import subprocess
import time

BUDGET_SECONDS = 1800

EVIDENCE = {
    "type": "object",
    "properties": {k: {"type": "string"} for k in
                   ("url", "title", "source_kind", "effective_period", "locator", "support_summary", "support_excerpt")}
    | {"publication_date": {"type": ["string", "null"]},
       "inspection_method": {"type": "string", "enum": ["captured_content", "live_full_page", "uninspected"]}},
    "required": ["url", "title", "source_kind", "publication_date", "effective_period", "locator",
                 "support_summary", "support_excerpt", "inspection_method"],
    "additionalProperties": False,
}
ATOM = {
    "type": "object",
    "properties": {"text": {"type": "string"}, "status": {"type": "string", "enum": ["SUPPORTED", "UNKNOWN", "CONTRADICTED"]},
                   "period": {"type": "string"}, "reason": {"type": "string"}, "evidence": {"type": "array", "items": EVIDENCE}},
    "required": ["text", "status", "period", "reason", "evidence"], "additionalProperties": False,
}


def schema(company, keys):
    return {
        "type": "object",
        "properties": {
            "ticker": {"type": "string", "enum": [company["ticker"]]},
            "company": {"type": "string", "enum": [company["company"]]},
            "identity_confirmation": {"type": "string"},
            "statements": {"type": "array", "items": {
                "type": "object",
                "properties": {
                    "key": {"type": "string", "enum": keys},
                    "verdict": {"type": "string", "enum": ["ACCEPTED", "PARTIALLY_SUPPORTED", "PERIOD_UNRESOLVED",
                                                           "UNKNOWN_AFTER_RESEARCH", "UNSUPPORTED"]},
                    "rationale": {"type": "string"},
                    "period_assessment": {"type": "string"},
                    "atomic_claims": {"type": "array", "items": ATOM},
                    "proposed_text": {"type": ["string", "null"]},
                    "contradictions": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["key", "verdict", "rationale", "period_assessment", "atomic_claims", "proposed_text",
                             "contradictions"],
                "additionalProperties": False}},
            "additional_facts": {"type": "array", "items": {
                "type": "object",
                "properties": {"topic": {"type": "string", "enum": ["業務與產品", "營收結構", "客戶", "供應商",
                                                                    "集團與轉投資", "重大合約", "沿革", "其他"]},
                               "text": {"type": "string"}, "period": {"type": "string"},
                               "evidence": {"type": "array", "items": EVIDENCE}},
                "required": ["topic", "text", "period", "evidence"], "additionalProperties": False}},
            "research_gaps": {"type": "array", "items": {"type": "string"}},
            "research_complete": {"type": "boolean"},
            "research_stop_reason": {"type": "string"},
        },
        "required": ["ticker", "company", "identity_confirmation", "statements", "additional_facts", "research_gaps",
                     "research_complete", "research_stop_reason"],
        "additionalProperties": False,
    }


def run_company(company, root, cache):
    adir = cache / 'companies' / company['ticker']
    attempt = 1
    while (adir / f'attempt-{attempt}').exists():
        attempt += 1
    adir = adir / f'attempt-{attempt}'; adir.mkdir(parents=True)
    report = BASE / company['report_path']
    payload = {**company, 'report_sha256': digest(report.read_bytes()), 'assessment_date': '2026-10-08'}
    prompt = (root / 'prompt-template.txt').read_text(encoding='utf-8') + json.dumps(payload, ensure_ascii=False)
    (adir / 'prompt.txt').write_text(prompt, encoding='utf-8')
    write_json(adir / 'output-schema.json', schema(company, [s['key'] for s in company['statements']]))
    final = adir / 'final.json'
    codex = shutil.which('codex') or shutil.which('codex.cmd')
    cmd = [codex, '--search', 'exec', '--ignore-user-config', '--ignore-rules', '--model', MODEL,
           '-c', f'model_reasoning_effort="{EFFORT}"', '-c', 'approval_policy="never"', '-c', 'windows.sandbox="unelevated"',
           '--sandbox', 'read-only', '--skip-git-repo-check', '--color', 'never', '--json',
           '--cd', str(adir), '--output-schema', str(adir / 'output-schema.json'),
           '--output-last-message', str(final), '-']
    started = time.time(); errors = []; code = None
    with open(adir / 'public-events.jsonl', 'wb') as out, open(adir / 'stderr.txt', 'wb') as err:
        try:
            code = subprocess.run(cmd, input=prompt.encode('utf-8'), stdout=out, stderr=err,
                                  timeout=BUDGET_SECONDS).returncode
        except subprocess.TimeoutExpired:
            errors.append(f'timeout after {BUDGET_SECONDS}s')
    text = (adir / 'public-events.jsonl').read_text(encoding='utf-8', errors='replace') + \
        (adir / 'stderr.txt').read_text(encoding='utf-8', errors='replace')
    if re.search(r'usage limit|rate limit|quota', text, re.I):
        errors.append('quota_or_rate_limit')
    if not (final.exists() and final.read_text(encoding='utf-8').strip()):
        errors.append('no final output')
    thread = re.search(r'"thread_id"\s*:\s*"([^"]+)"', text)
    execution = {'requested_model': MODEL, 'requested_effort': EFFORT, 'thread_id': thread.group(1) if thread else None,
                 'controller_sha256': digest(Path(__file__).read_bytes()), 'batch_controller_sha256': CONTROLLER_SHA256,
                 'command': [Path(c).name if i == 0 else c for i, c in enumerate(cmd)], 'process_exit_code': code,
                 'attempt': attempt, 'completed_at': now(), 'elapsed_seconds': round(time.time() - started),
                 'prompt_sha256': digest(prompt.encode('utf-8')), 'report_sha256': payload['report_sha256'],
                 'output_path': rel(final), 'output_sha256': digest(final.read_bytes()) if final.exists() else None,
                 'errors': errors}
    write_json(adir / 'execution.json', execution)
    print(company['ticker'], errors or 'ok', execution['elapsed_seconds'], 's', flush=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--batch', required=True)
    p.add_argument('--only', nargs='*')
    a = p.parse_args()
    root, cache = HERE / a.batch, CACHE_ROOT / a.batch
    data = json.loads((root / 'statements.json').read_text(encoding='utf-8'))
    todo = [c for c in data['companies'] if not a.only or c['ticker'] in a.only]
    with ThreadPoolExecutor(len(todo)) as ex:
        list(ex.map(lambda c: run_company(c, root, cache), todo))


if __name__ == '__main__':
    main()
