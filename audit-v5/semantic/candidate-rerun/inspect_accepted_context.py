#!/usr/bin/env python3
"""Print pending accepted-source context for human/primary-agent inspection.

This does not approve, change or certify any verdict.
"""
import argparse
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent / 'adjudication'


def rows(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()] if path.exists() else []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=5)
    args = ap.parse_args()
    final = {row['claim_id']: row for row in rows(ROOT / 'results.jsonl')}
    checked = {row['claim_id']: row for row in rows(ROOT / 'primary-source-review.jsonl')}
    deferred = [identity for identity, row in final.items() if checked.get(identity, {}).get('status') == 'REVIEW_REQUIRED' and checked[identity].get('output_sha256') == row['output_sha256']]
    selected = [row for identity, row in final.items() if identity not in deferred and row['verdict'] == 'ACCEPTED' and
                not (checked.get(identity, {}).get('status') == 'PASS' and
                     checked[identity]['output_sha256'] == row['output_sha256'])][:args.limit]
    spec = importlib.util.spec_from_file_location('fc', ROOT.parent/'run_final_adjudication.py')
    controller = importlib.util.module_from_spec(spec); spec.loader.exec_module(controller)
    def normalize(text):
        return re.sub(r'[\s|]+', '', text)
    for row in selected:
        print('\nCLAIM', row['claim_id'], row['cohort'])
        print('ORIGINAL', row['original_claim']['original_text'])
        context = controller.report_context(row['original_claim'])
        print('REPORT CONTEXT', json.dumps(context, ensure_ascii=False))
        result = row['adjudication']
        print('PERIOD', result['period_assessment'])
        print('RATIONALE', result['rationale'])
        captures = {capture['url']: capture for capture in row['source_captures']}
        bodies = {}
        for atom in result['atomic_claims']:
            print('ATOM', atom['text'], atom['period'], atom['reason'])
            for evidence in atom['evidence']:
                print('SOURCE', evidence['url'], evidence['publication_date'], evidence['effective_period'], evidence['locator'])
                print('EXCERPT', evidence['support_excerpt'])
                capture = captures[evidence['url']]
                if capture.get('status') != 'captured':
                    print('UNCAPTURED'); continue
                if evidence['url'] not in bodies:
                    bodies[evidence['url']] = normalize(Path(capture['text_path']).read_text())
                body = bodies[evidence['url']]; excerpt = normalize(evidence['support_excerpt'])
                matches = list(re.finditer(re.escape(excerpt), body)) if excerpt else []
                if not matches:
                    print('NO MATCH'); continue
                for match in matches[:3]:
                    index = match.start()
                    pages = list(re.finditer(r'\[PDFPAGE(\d+)\]', body[:index]))
                    print('ACTUAL PDF PAGE', pages[-1].group(1) if pages else 'N/A', 'MATCHES', len(matches))
                    print('CONTEXT', body[max(0, index - 240):match.end() + 450])
    print('\nPENDING ACCEPTED PRINTED', len(selected), 'AWAITING FRESH REVIEW', len(deferred))


if __name__ == '__main__':
    main()
