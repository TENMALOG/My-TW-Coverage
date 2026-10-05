from __future__ import annotations

import argparse
import json
import os
import urllib.request
from pathlib import Path

ENDPOINT='https://models.github.ai/inference/chat/completions'
MODEL='openai/gpt-4.1'

def call_model(payload):
    token=os.environ['GITHUB_TOKEN']
    req=urllib.request.Request(ENDPOINT,data=json.dumps(payload).encode('utf-8'),method='POST',headers={'Authorization':f'Bearer {token}','Content-Type':'application/json','Accept':'application/json'})
    with urllib.request.urlopen(req,timeout=120) as r:
        body=r.read().decode('utf-8',errors='replace')
        print('github-models status',r.status,'content-type',r.headers.get('content-type'),'body-prefix',repr(body[:300]))
        return json.loads(body)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--author',required=True); ap.add_argument('--output',required=True); args=ap.parse_args()
    queue=json.loads(Path('audit-v5/generated/semantic-high-queue.json').read_text(encoding='utf-8'))
    qmap={x['claim_id']:x for x in queue['items']}
    author=json.loads(Path(args.author).read_text(encoding='utf-8'))
    reviews=[]
    for item in author['items']:
        claim=qmap[item['claim_id']]
        evidence='\n'.join(f"- L{e['source_level']} {e['title']}: {e['note']} URL={e['url']}" for e in item.get('evidence',[]))
        prompt=f'''You are the independent reviewer for a high-risk Taiwan equity factual claim. Judge only whether the recorded inspected evidence entails the exact claim. Do not assume facts not present in the evidence notes. Search snippets are not evidence.\n\nCLAIM: {claim['claim']}\nSIGNAL: {claim['signal_type']}\nAUTHOR DECISION: {item['decision']}\nAUTHOR RATIONALE: {item.get('rationale','')}\nPROPOSED TEXT: {item.get('proposed_text','')}\nEVIDENCE:\n{evidence}\n\nReturn strict JSON with keys decision, agrees_with_author, rationale. decision must be one of ACCEPTED, PARTIALLY_SUPPORTED, UNSUPPORTED, PERIOD_UNRESOLVED, SOURCE_UNAVAILABLE, UNKNOWN_AFTER_RESEARCH.'''
        resp=call_model({'model':MODEL,'messages':[{'role':'system','content':'Be conservative. Exact ranking, market-share, exclusivity and materiality qualifiers require explicit evidence.'},{'role':'user','content':prompt}],'temperature':0,'response_format':{'type':'json_object'}})
        raw=resp['choices'][0]['message']['content']
        parsed=json.loads(raw)
        reviews.append({'claim_id':item['claim_id'],'model':MODEL,'basis':'independent semantic entailment review of recorded inspected evidence','decision':parsed['decision'],'agrees_with_author':bool(parsed['agrees_with_author']),'rationale':parsed['rationale']})
    out={'schema':'semantic-independent-review-1','source_author_batch':author['batch_id'],'model':MODEL,'review_count':len(reviews),'items':reviews}
    Path(args.output).parent.mkdir(parents=True,exist_ok=True); Path(args.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    disagreements=[x for x in reviews if not x['agrees_with_author']]
    print(json.dumps({'review_count':len(reviews),'disagreements':len(disagreements)},ensure_ascii=False))
    return 0

if __name__=='__main__': raise SystemExit(main())
