"""Drop footnote-only entries from research-site/_site/search.json so it stays under Cloudflare Pages' 25 MiB file limit.

  python research-site/scripts/slim_search_index.py

Quarto indexes each page's footnote list as its own section-less entry (source titles and URLs ending in ↩︎). With the
P2 section (0.4.0) the index reached 33 MiB; those entries are about half of it. Body sections stay searchable; only
the citation text is no longer searched. Run after every full render or merge and before deploy_pages.py; re-running
is a no-op. Fails if a page would lose all of its entries.
"""
import json
from pathlib import Path

SITE = Path(__file__).resolve().parents[1] / '_site'
LIMIT = 25 * 2 ** 20


def is_footnotes(e: dict) -> bool:
    text = e.get('text') or ''
    return not e.get('section') and '↩︎' in text and not text.rsplit('↩︎', 1)[1].strip()


def main():
    path = SITE / 'search.json'
    entries = json.loads(path.read_text(encoding='utf-8'))
    keep = [e for e in entries if not is_footnotes(e)]
    pages = {e['href'].split('#')[0] for e in entries}
    lost = pages - {e['href'].split('#')[0] for e in keep}
    if lost:
        raise SystemExit(f'{len(lost)} pages would have no search entry, e.g. {sorted(lost)[:3]}')
    data = json.dumps(keep, ensure_ascii=False)
    size = len(data.encode('utf-8'))
    if size >= LIMIT:
        raise SystemExit(f'search.json still {size / 2 ** 20:.1f} MiB after removing footnotes')
    path.write_text(data, encoding='utf-8')
    print(f'search.json: {len(entries)} -> {len(keep)} entries, {size / 2 ** 20:.1f} MiB, {len(pages)} pages indexed')


if __name__ == '__main__':
    main()
