from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from auditlib import _narrative_risk_text, normalize_text, risk_signals, scan_report

def claim_id(ticker: str, signal_type: str, claim: str) -> str:
    h=hashlib.sha256(normalize_text(claim).encode('utf-8')).hexdigest()[:16]
    return f'{ticker}:{signal_type}:{h}'

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',default='Pilot_Reports')
    ap.add_argument('--output',default='audit-v5/generated/semantic-high-queue.json')
    args=ap.parse_args()
    items=[]; counts=Counter(); seen=set(); issuers=set()
    for path in sorted(Path(args.root).rglob('*.md')):
        scan=scan_report(path)
        text=path.read_text(encoding='utf-8')
        for signal in risk_signals(_narrative_risk_text(text)):
            if signal['level']!='HIGH': continue
            cid=claim_id(scan.ticker or 'UNKNOWN',signal['type'],signal['claim'])
            if cid in seen: continue
            seen.add(cid); issuers.add(scan.ticker); counts[signal['type']]+=1
            items.append({'claim_id':cid,'ticker':scan.ticker,'company':scan.company,'path':path.as_posix(),'signal_type':signal['type'],'risk':'HIGH','claim':signal['claim'],'normalized_claim_hash':hashlib.sha256(normalize_text(signal['claim']).encode('utf-8')).hexdigest(),'status':'NEEDS_MODEL_REVIEW','evidence':[],'author_review':None,'independent_review':None,'final_state':None})
    payload={'schema':'semantic-high-queue-1','generated_at':datetime.now(timezone.utc).isoformat(),'policy_binding':'risk-calibration-v3+source-1-draft+protocol-1.2.0-draft','issuer_count':len(issuers),'claim_count':len(items),'signal_counts':dict(sorted(counts.items())),'items':items}
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in payload.items() if k!='items'},ensure_ascii=False,indent=2))
    if len(items)!=1410 or len(issuers)!=836: raise SystemExit(2)
    return 0

if __name__=='__main__': raise SystemExit(main())
