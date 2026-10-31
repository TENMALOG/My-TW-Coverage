// Shared presentation rules; the source values remain unchanged.
export const formatRevenue = (value) => value.toLocaleString('en-US', {
  minimumFractionDigits: Math.abs(value) >= 100 ? 0 : Math.abs(value) >= 1 ? 1 : 2,
  maximumFractionDigits: Math.abs(value) >= 100 ? 0 : Math.abs(value) >= 1 ? 1 : 2,
});

export function mixItems(mix) {
  const total = mix.items.reduce((sum, [, value]) => sum + Number(value), 0);
  const items = mix.items.map(([name, value]) => ({ name, value: Number(value) }));
  if (total < 99.5) items.push({ name: '其他／未列', value: +(100 - total).toFixed(2), unlisted: true });
  return { total, items };
}

export function mixSegments(mix) {
  const { items } = mixItems(mix);
  const ranked = [...items].sort((a, b) => b.value - a.value);
  const grouped = ranked.slice(0, 2);
  const components = ranked.slice(2);
  if (components.length) grouped.push({ name: '其他', value: +components.reduce((sum, item) => sum + item.value, 0).toFixed(10), components });
  return grouped;
}
