from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

DONE_RE = re.compile(r"Done\. Updated:\s*(\d+)\s*\|\s*Skipped:\s*(\d+)\s*\|\s*Failed:\s*(\d+)")
ERROR_RE = re.compile(r"^\s*(\d{4,6}):\s*ERROR\b")


def run(cmd: list[str], log_path: Path | None = None) -> tuple[int, str]:
    proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, encoding="utf-8", errors="replace"
    )
    lines = []
    assert proc.stdout is not None
    for line in proc.stdout:
        print(line, end="")
        lines.append(line)
    code = proc.wait()
    text = "".join(lines)
    if log_path:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(text, encoding="utf-8")
    return code, text


def parse_done(text: str) -> dict[str, int] | None:
    matches = list(DONE_RE.finditer(text))
    if not matches:
        return None
    m = matches[-1]
    return {"updated": int(m.group(1)), "skipped": int(m.group(2)), "failed": int(m.group(3))}


def parse_errors(text: str) -> list[str]:
    return sorted(set(m.group(1) for m in map(ERROR_RE.match, text.splitlines()) if m))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--script", default="scripts/update_financials.py")
    ap.add_argument("--output", default="audit-v5/generated/financial-refresh-summary.json")
    ap.add_argument("--log", default="audit-v5/work/update-financials.log")
    ap.add_argument("--retries", type=int, default=2)
    args = ap.parse_args()

    started = datetime.now(timezone.utc).isoformat()
    code, text = run([sys.executable, "-X", "utf8", args.script], Path(args.log))
    summary = parse_done(text)
    failed_tickers = parse_errors(text)
    retry_results = {}

    for attempt in range(1, args.retries + 1):
        if not failed_tickers:
            break
        remaining = []
        for ticker in failed_tickers:
            print(f"\nRetry {attempt}/{args.retries}: {ticker}")
            rcode, rtext = run([sys.executable, "-X", "utf8", args.script, ticker])
            rsummary = parse_done(rtext)
            ok = (
                rcode == 0 and rsummary is not None
                and rsummary.get("failed", 1) == 0
                and rsummary.get("updated", 0) >= 1
            )
            retry_results.setdefault(ticker, []).append({
                "attempt": attempt, "ok": ok, "summary": rsummary
            })
            if not ok:
                remaining.append(ticker)
        failed_tickers = remaining

    payload = {
        "started_at": started,
        "finished_at": datetime.now(timezone.utc).isoformat(),
        "initial_exit_code": code,
        "initial_summary": summary,
        "retry_results": retry_results,
        "remaining_failed_tickers": failed_tickers,
        "ok": code == 0 and summary is not None and not failed_tickers,
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
