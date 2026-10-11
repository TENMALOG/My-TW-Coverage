#!/usr/bin/env python3
"""Report Codex quota from the newest local rollout (no quota spent).

Prints one line: five_hour=<pct> (resets <local time>) weekly=<pct> (resets <local time>) state=<STATE>
STATE: OK | FIVE_HOUR_EXHAUSTED (Claude takes over until reset; do NOT use the saved reset)
       | WEEKLY_EXHAUSTED (chairman allows ONE saved reset) | UNKNOWN
Owner rule (2026-10-11): 5h exhausted + weekly left → Claude works until the 5h window resets,
then hand back to Codex; use the single saved reset only when the weekly quota is exhausted.
"""
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

SESS = Path.home() / '.codex/sessions'


def latest_limits():
    files = sorted(SESS.rglob('rollout-*.jsonl'), key=lambda p: p.stat().st_mtime, reverse=True)
    dec = json.JSONDecoder()
    for f in files[:400]:
        text = f.read_text(encoding='utf-8', errors='replace')
        for m in reversed(list(re.finditer(r'"rate_limits":', text))):
            try:
                obj, _ = dec.raw_decode(text, m.end())
            except json.JSONDecodeError:
                continue
            if isinstance(obj, dict) and obj.get('primary') and obj.get('secondary'):
                return obj, f
    return None, None


def main():
    lim, f = latest_limits()
    if not lim:
        print('state=UNKNOWN'); return
    p, s = lim['primary'], lim['secondary']
    fmt = lambda t: datetime.fromtimestamp(t).strftime('%m-%d %H:%M')
    state = 'WEEKLY_EXHAUSTED' if s['used_percent'] >= 100 else ('FIVE_HOUR_EXHAUSTED' if p['used_percent'] >= 100 else 'OK')
    print(f"five_hour={p['used_percent']}% (resets {fmt(p['resets_at'])}) weekly={s['used_percent']}% "
          f"(resets {fmt(s['resets_at'])}) state={state} source={f.name}")


if __name__ == '__main__':
    main()
