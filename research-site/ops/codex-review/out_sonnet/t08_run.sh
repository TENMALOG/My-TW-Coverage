#!/bin/bash
cd "C:/Users/Neo Pegasus/Documents/ChatGPT/078-kaori sample/artifacts/stock-coverage-audit-20261003/incoming/latest-audit/My-TW-Coverage/research-site/ops/codex-review"
../../../.venv/Scripts/python.exe -X utf8 out_sonnet/t08_compile.py "$1" ${2:-}
