import sys,subprocess
ids=[l.strip() for l in open(sys.argv[1]) if l.strip()]
a,b=int(sys.argv[2]),int(sys.argv[3])
open('research-site/ops/codex-review/out_sonnet/s06_tmp.txt','w').write('\n'.join(ids[a:b]))
