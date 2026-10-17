#!/bin/bash
# usage: s06_n.sh job a b W
cd "C:/Users/Neo Pegasus/Documents/ChatGPT/078-kaori sample/artifacts/stock-coverage-audit-20261003/incoming/latest-audit/My-TW-Coverage"
python -X utf8 research-site/ops/codex-review/out_sonnet/s06_slice.py research-site/ops/codex-review/jobs_sonnet/$1.txt $2 $3
python -X utf8 research-site/ops/codex-review/out_sonnet/s06_ctx.py research-site/ops/codex-review/out_sonnet/s06_tmp.txt ${4:-200}
