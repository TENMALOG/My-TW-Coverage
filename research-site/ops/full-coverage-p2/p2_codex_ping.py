"""Refresh both Codex accounts' rate_limits with a tiny exec, so the quota guard reads current numbers."""
import os
import subprocess
from pathlib import Path

codex = str(Path(os.environ['APPDATA']) / 'npm' / 'codex.cmd')
for h in ('.codex', '.codex-b'):
    r = subprocess.run([codex, 'exec', '--skip-git-repo-check', '--sandbox', 'read-only', '-c', 'model_reasoning_effort="low"',
                        'Reply with the single word OK.'], env={**os.environ, 'CODEX_HOME': str(Path.home() / h)},
                       capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=150)
    print(h, r.returncode)
