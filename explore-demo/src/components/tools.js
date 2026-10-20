// 工具頁共用：摘要資料（public/data/summary.json，由 scripts/export_data.py 從已查核資料產生）、格式、觀察清單、圖表。
let _summary;
export async function summary() {
  if (!_summary) _summary = fetch('/data/summary.json').then((r) => r.json());
  return _summary;
}
export const byTicker = async () => Object.fromEntries((await summary()).map((c) => [c.t, c]));

export const fmtRev = (v) => (v == null ? '—' : v >= 100 ? `${Math.round(v).toLocaleString('en-US')} 億` : `${v.toFixed(1)} 億`);
export const fmtPct = (v, sign = false) => (v == null ? '—' : `${sign && v > 0 ? '+' : ''}${v}%`);

export function watchlist() {
  try { return JSON.parse(localStorage.getItem('watch') || '[]'); } catch (e) { return []; }
}
export function setWatchlist(v) {
  try { localStorage.setItem('watch', JSON.stringify(v)); } catch (e) {}
}

export const css = (v) => getComputedStyle(document.documentElement).getPropertyValue(v).trim();

export function el(tag, attrs = {}, ...kids) {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === 'class') e.className = v;
    else if (k === 'style') e.style.cssText = v;
    else if (k.startsWith('on')) e.addEventListener(k.slice(2), v);
    else if (v != null) e.setAttribute(k, v);
  }
  for (const k of kids.flat()) if (k != null) e.append(k.nodeType ? k : document.createTextNode(String(k)));
  return e;
}

// 一家公司的精簡卡（篩選結果、觀察清單共用）
export function miniCard(c, extra) {
  return el('div', { class: 'card', style: 'margin:12px 0;padding:14px 16px' },
    el('div', { style: 'display:flex;gap:8px;align-items:baseline;flex-wrap:wrap' },
      el('span', { class: 'kicker num', style: 'margin:0' }, c.t),
      el('a', { href: `/c/${c.t}/`, style: 'font-size:20px;font-weight:900;text-decoration:none' }, c.n),
      el('a', { class: 'chip', href: `/i/${c.i}/` }, c.in),
      c.m ? el('span', { class: 'chip' }, `證交所：${c.m}`) : null),
    el('div', { class: 'num', style: 'margin:6px 0' },
      `${c.y ?? ''} 營收 ${fmtRev(c.rev)}｜年增 ${fmtPct(c.yoy, true)}｜毛利率 ${fmtPct(c.gm)}`),
    c.h ? el('div', { class: 'muted' }, c.h) : null,
    extra || null);
}

// 公司選擇輸入框（輸入代號或名稱，datalist 自動完成）
export async function picker(onPick, placeholder = '輸入代號或公司名，例如 2330 或 台積電') {
  const all = await summary();
  const id = 'dl' + Math.random().toString(36).slice(2);
  const input = el('input', { list: id, placeholder, autocomplete: 'off',
    style: 'width:100%;font:inherit;font-size:18px;padding:10px 14px;border:2.5px solid var(--fg);border-radius:14px;background:var(--bg);color:var(--fg)' });
  const dl = el('datalist', { id }, all.map((c) => el('option', { value: `${c.t} ${c.n}` })));
  input.addEventListener('change', () => {
    const t = input.value.trim().split(/\s+/)[0];
    const hit = all.find((c) => c.t === t) || all.find((c) => c.n === input.value.trim());
    if (hit) { onPick(hit); input.value = ''; }
  });
  return el('div', {}, input, dl);
}
