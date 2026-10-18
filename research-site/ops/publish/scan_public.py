"""Scan an exported public tree before it is pushed anywhere.

  python research-site/ops/publish/scan_public.py <export_dir>

Fails (exit 1) on: secrets (API keys, tokens, private keys, password assignments), local machine paths or
the local account name, e-mail addresses, natural-person names (honorifics, masked names such as 黃O明,
job title followed by a name and a speech verb), and forbidden files (annual-report slices or snapshots,
.env, audit caches). Text files only; binary assets are listed by size.
"""
import re
import sys
from pathlib import Path

SECRET = re.compile(r'(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{30,}|gho_[A-Za-z0-9]{30,}|AKIA[0-9A-Z]{16}|'
                    r'xox[bap]-[A-Za-z0-9-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|'
                    r'(?i:(password|passwd|secret|api[_-]?key|access[_-]?token)\s*[:=]\s*["\'][^"\']{6,}))')
LOCAL = re.compile(r'(?i)(C:\\Users\\|C:/Users/|/Users/[A-Za-z]|Neo Pegasus|NEOPEG~1|AppData)')
EMAIL = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
PERSON = re.compile(r'[\u4e00-\u9fff]{2,3}(先生|女士|小姐)|(?<![\u4e00-\u9fff])[\u4e00-\u9fff][OＯ○〇][\u4e00-\u9fff](?![\u4e00-\u9fff]*(公司|集團|市|縣|營造|企業))|'
                    r'(董事長|總經理|執行長|發言人|創辦人)(?![於在及與亦也則曾已將並暨兼])[\u4e00-\u9fff]{2,3}'
                    r'(?=表示|指出|說明|強調|認為|介紹|透露)')
FORBIDDEN = re.compile(r'(annual-slices|source-cache|mops-annual|audit-v5|\.env$|_semantic-review|_manual-fixes)')
TEXT = {'.md', '.qmd', '.py', '.json', '.jsonl', '.csv', '.yml', '.yaml', '.txt', '.html', '.js', '.css', '.lua', '.xml'}
ALLOWED_EMAIL = {'noreply@anthropic.com'}


def main(root: Path):
    problems = []
    big = []
    for p in root.rglob('*'):
        if '.git' in p.parts or not p.is_file():
            continue
        rel = p.relative_to(root).as_posix()
        if FORBIDDEN.search(rel):
            problems.append(('forbidden_file', rel, ''))
            continue
        if p.suffix.lower() not in TEXT:
            if p.stat().st_size > 5_000_000:
                big.append((rel, p.stat().st_size))
            continue
        t = p.read_text(encoding='utf-8', errors='replace')
        for kind, rx in (('secret', SECRET), ('local_path', LOCAL), ('person', PERSON)):
            for m in rx.finditer(t):
                problems.append((kind, rel, t[max(0, m.start() - 20):m.end() + 20].replace('\n', ' ')))
        for m in EMAIL.finditer(t):
            if m.group(0).lower() not in ALLOWED_EMAIL and not m.group(0).endswith(('.png', '.jpg', '.svg')):
                problems.append(('email', rel, m.group(0)))
    by = {}
    for k, rel, ctx in problems:
        by.setdefault(k, []).append((rel, ctx))
    for k, items in by.items():
        print(f'== {k}: {len(items)}')
        for rel, ctx in items[:15]:
            print(f'   {rel}: {ctx}')
    for rel, size in big:
        print(f'large binary {rel} {size / 1e6:.1f} MB')
    print('RESULT', 'FAIL' if problems else 'PASS')
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main(Path(sys.argv[1]).resolve())
