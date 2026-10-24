// 不同引用事實的期間與分母不交叉拼接。
export function hookScope(c) {
  const scopes = (c.hook?.facts || []).flatMap((id) => {
    const source = c.sources?.[id];
    if (!source) return [];
    const groups = [c.mix, c.regions].filter((g) => g?.facts?.includes(id) && g.basis);
    if (groups.length) return groups.map((g) => {
      const period = source.period || (g.year ? `${g.year} 年度` : '');
      const year = g.year && !period.includes(String(g.year)) ? `${g.year} 年度；` : '';
      return [year + period, `占比口徑：${g.basis}`].filter(Boolean).join('｜');
    });
    const basis = source.statement?.match(/[占佔][^，。；、%\d]{1,60}?(?:合計|比重)/)?.[0];
    return [source.period, basis && `占比口徑：${basis}`].filter(Boolean).join('｜');
  });
  return [...new Set(scopes.filter(Boolean))].join('；');
}
export function scopedHook(c) {
  const text = c.hook?.text || '';
  const scope = hookScope(c);
  return text && scope ? `${text}（${scope}）` : text;
}
