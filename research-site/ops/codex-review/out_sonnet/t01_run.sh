#!/bin/bash
# usage: t01_run.sh job ticker PRE POST CAP
F=research-site/ops/codex-review
.venv/Scripts/python.exe -X utf8 $F/out_sonnet/t01_show.py $F/jobs_sonnet/$1.txt $2 ${3:-250} ${4:-150} ${5:-1500}
