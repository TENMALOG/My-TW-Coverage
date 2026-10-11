"""Generate the 1,733-company index page (index-companies.qmd) from the release-scope list.

Tiers: T2 has a research page; T1 has selected claims checked; T0 index only.
No original report content is shown — only identity, industry folder and research status.

  python research-site/scripts/build_company_index.py
"""
from __future__ import annotations

import csv
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / 'research-site'
T2 = {p.stem for p in (SITE / 'chapters/companies').glob('*.qmd')}


def main():
    rows = list(csv.DictReader(open(SITE / 'catalog/release-scope-companies.csv', encoding='utf-8-sig')))
    rows.sort(key=lambda r: r['ticker'])
    counts = {'T2': 0, 'T1': 0, 'T0': 0}
    trs = []
    for r in rows:
        tk, n = r['ticker'], int(r['claims_in_scope'])
        if tk in T2:
            tier, status = 'T2', f'<a href="chapters/companies/{tk}.html">深入研究頁</a>'
        elif n:
            tier, status = 'T1', f'已查核 {n} 條選定敘述，尚無研究頁'
        else:
            tier, status = 'T0', '尚未深入研究'
        counts[tier] += 1
        trs.append(f'<tr data-tier="{tier}"><td>{tk}</td><td>{html.escape(r["company"])}</td>'
                   f'<td>{html.escape(r["industry_folder"])}</td><td>{tier}</td><td>{status}</td></tr>')
    page = f'''---
title: "公司索引"
---

<!-- 由 research-site/scripts/build_company_index.py 產生；請勿手動修改。 -->

本索引列出原專案涵蓋的 {len(rows):,} 家上市櫃公司，並標示每家的研究深度。只有 **T2** 公司有經過查核的研究頁；**T1** 公司有部分選定敘述經過查核，但查核結果尚未整理成研究頁；**T0** 公司只列入索引。本索引不顯示原報告內容，因為原報告未經全面查核。產業分類沿用原專案的英文資料夾名稱。

| 等級 | 家數 |
|---|---:|
| T2 深入研究頁 | {counts["T2"]} |
| T1 已查核部分敘述 | {counts["T1"]} |
| T0 僅索引 | {counts["T0"]} |

```{{=html}}
<div class="company-index">
<label>篩選（代號、公司名或產業）：<input id="ci-filter" type="search" style="max-width:20em;width:100%" placeholder="例如 2645、長榮、Semiconductors"></label>
<label style="margin-left:1em"><input id="ci-t2" type="checkbox"> 只顯示有研究頁的公司</label>
<p id="ci-count" style="margin:.5em 0"></p>
<div style="overflow-x:auto"><table class="table table-sm" id="ci-table">
<thead><tr><th>代號</th><th>公司</th><th>產業（原專案分類）</th><th>等級</th><th>研究狀態</th></tr></thead>
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
