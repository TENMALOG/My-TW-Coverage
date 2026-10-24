// 只加總 2025 年度營業收入，單位由仟元換為億元。
export const YEAR = '2025';
export const revenueOf = (c) => c.fin?.[YEAR]?.revenue_k ?? null;
export const revenueNote = '各公司 2025 年度合併營業收入直接相加，母子公司都上市時會重複計算，不是產業總產值；金融業與缺資料公司不列入。';
export function revenueSummary(companies) {
  const values = companies.map(revenueOf).filter((v) => v != null);
  return {
    n: values.length,
    rev: values.length ? values.reduce((s, v) => s + v, 0) / 1e5 : null,
    na: companies.filter((c) => c.fin_missing === 'format').length,
    missing: companies.filter((c) => c.fin_missing === 'absent').length,
    other: companies.filter((c) => revenueOf(c) == null && Object.keys(c.fin || {}).some((y) => y !== YEAR)).length,
    negative: values.some((v) => v < 0),
    allFormat: companies.length > 0 && companies.every((c) => c.fin_missing === 'format'),
  };
}
export const sortRevenue = (a, b) => a.rev == null ? (b.rev == null ? 0 : 1) : b.rev == null ? -1 : b.rev - a.rev;
export const exactRevenue = (v) => v == null ? undefined : `${v.toLocaleString('en-US', { maximumFractionDigits: 5 })} 億元`;
export const formatRevenue = (v) => v == null ? '無可加總資料'
  : v < 0 ? `${v.toLocaleString('en-US', { maximumFractionDigits: 2 })} 億`
  : v >= 10000 ? `${(v / 10000).toFixed(1)} 兆`
  : v > 0 && v < 1 ? '低於 1 億' : `${Math.round(v).toLocaleString('en-US')} 億`;
export const revenueLabel = (s) => s.allFormat ? '金融業報表格式不同，不加總營業收入' : formatRevenue(s.rev);
export const revenueCounts = (s) => [s.n && `${s.n} 家有 2025 年度資料`, s.na && `${s.na} 家金融業格式不適用`, s.missing && `${s.missing} 家缺資料`, s.other && `${s.other} 家僅有其他年度資料`].filter(Boolean).join('，');
