#!/bin/bash
# Usage: run_analysis.sh SLUG — draft one industry analysis with Codex (read-only); skip if done.
S=C:/Users/NEOPEG~1/AppData/Local/Temp/claude/C--Users-Neo-Pegasus-Documents-ChatGPT-078-kaori-sample-artifacts-stock-coverage-audit-20261003-incoming-latest-audit-My-TW-Coverage/1bd92d0e-e36f-4ef8-b701-31d7a9c88c71/scratchpad
slug=$1
[ -s "$S/analysis/$slug.qmd" ] && grep -q '產業分析' "$S/analysis/$slug.qmd" && exit 0
mkdir "$S/analysis/$slug.lock" 2>/dev/null || exit 0
TASK=$(cygpath -w "$S/codex_analysis_task.md"); F=$(cygpath -w "$S/ind_facts/$slug.json")
codex exec --skip-git-repo-check --sandbox read-only -c 'windows.sandbox="unelevated"' -o "$S/analysis/$slug.qmd" "Read and follow the task file $TASK exactly. The industry fact file is $F . Your final message must be only the Quarto Markdown section." > "$S/analysis/$slug.log" 2>&1
echo "$slug exit=$? bytes=$(wc -c < "$S/analysis/$slug.qmd" 2>/dev/null)"
