"""Generate the 1,733-company index page (index-companies.qmd) from the release-scope list.

Types: T2 is hand-written aerospace research; AR is annual-report facts; T1/T0 have no page.
No original report content is shown — only identity, industry folder and research status.

  python research-site/scripts/build_company_index.py
"""
from __future__ import annotations

import csv
import html
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / 'generic'))
from industries import AERO_TICKERS, industry_names, mops_industry  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / 'research-site'
PAGES = {p.stem for p in (SITE / 'chapters/companies').glob('*.qmd')}


ZH = {k: v['name_zh'] for k, v in industry_names().items()}


def main():
    rows = list(csv.DictReader(open(SITE / 'catalog/release-scope-companies.csv', encoding='utf-8-sig')))
    rows.sort(key=lambda r: r['ticker'])
    counts = {'T2': 0, 'AR': 0, 'T1': 0, 'T0': 0}
    trs = []
    for r in rows:
        tk, n = r['ticker'], int(r['claims_in_scope'])
        if tk in PAGES and tk in AERO_TICKERS:
            tier, status = 'T2', f'<a href="chapters/companies/{tk}.html">深入研究頁</a>'
        elif tk in PAGES:
            tier, status = 'AR', f'<a href="chapters/companies/{tk}.html">年報事實頁</a>'
        elif n:
            tier, status = 'T1', f'已查核 {n} 條選定敘述，尚無研究頁'
        else:
            tier, status = 'T0', '尚未深入研究'
        counts[tier] += 1
        trs.append(f'<tr data-tier="{tier}"><td>{tk}</td><td>{html.escape(r["company"])}</td>'
                   f'<td>{html.escape(ZH[r["industry_folder"]])}</td>'
                   f'<td>{html.escape(mops_industry(tk)[0] or "不繼續公開發行")}</td><td>{tier}</td><td>{status}</td></tr>')
    page = f'''---
title: "公司索引"
---

<!-- 由 research-site/scripts/build_company_index.py 產生；請勿手動修改。 -->

本索引列出原專案涵蓋的 {len(rows):,} 家公司（依 2026-10-23 證交所與櫃買中心名單，其中上市 941 家、上櫃 683 家、興櫃 97 家，另 12 家已終止上市、上櫃或興櫃），並標示每家公司頁的內容類型。**深入研究頁**為航太與國防的人工撰寫公司頁；**年報事實頁**為其他公司的自動彙整頁，列出通過查核的年報事實與財務彙總；**T1** 公司有部分選定敘述經過查核，但查核結果尚未整理成研究頁；**T0** 公司只列入索引。本索引不顯示原報告內容，因為原報告未經全面查核。產業分類沿用原專案的英文資料夾名稱。

| 內容類型 | 家數 |
|---|---:|
| 深入研究頁 | {counts["T2"]} |
| 年報事實頁 | {counts["AR"]} |
| T1 已查核部分敘述 | {counts["T1"]} |
| T0 僅索引 | {counts["T0"]} |

```{{=html}}
<div class="company-index">
<label>篩選（代號、公司名或產業）：<input id="ci-filter" type="search" style="max-width:20em;width:100%" placeholder="例如 2645、長榮、Semiconductors"></label>
<label style="margin-left:1em"><input id="ci-t2" type="checkbox"> 只顯示深入研究頁（航太與國防）</label>
<p id="ci-count" style="margin:.5em 0"></p>
<div style="overflow-x:auto"><table class="table table-sm" id="ci-table">
<thead><tr><th>代號</th><th>公司</th><th>產業（本研究分類）</th><th>證交所產業別</th><th>類型代碼</th><th>內容類型／查核狀態</th></tr></thead>
<tbody>
{chr(10).join(trs)}
</tbody></table></div>
</div>
<script>
(function () {{
  const input = document.getElementById('ci-filter'), only = document.getElementById('ci-t2');
  const rows = Array.from(document.querySelectorAll('#ci-table tbody tr')), out = document.getElementById('ci-count');
  function apply() {{
    const q = input.value.trim().toLowerCase(); let n = 0;
    rows.forEach(tr => {{
      const ok = (!q || tr.textContent.toLowerCase().includes(q)) && (!only.checked || tr.dataset.tier === 'T2');
      tr.style.display = ok ? '' : 'none'; if (ok) n++;
    }});
    out.textContent = '顯示 ' + n + ' / ' + rows.length + ' 家';
  }}
  input.addEventListener('input', apply); only.addEventListener('change', apply); apply();
}})();
</script>
```
'''
    (SITE / 'index-companies.qmd').write_text(page, encoding='utf-8')
    print(counts)


if __name__ == '__main__':
    main()
