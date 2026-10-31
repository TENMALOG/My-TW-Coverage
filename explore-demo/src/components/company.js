// 公司卡片頁的互動：圖表、年報出處抽屜、觀察清單、分享。
import { watchlist as getWatchlist, setWatchlist } from './tools.js';
import { reportName, reportLabel } from '../lib/report.js';
import { formatRevenue, mixItems } from '../lib/chart-data.js';

const css = (v) => getComputedStyle(document.documentElement).getPropertyValue(v).trim();

// Show final chart geometry immediately, including under reduced motion.
const chartMotion = { animation: false };

function base() {
  return { textStyle: { fontFamily: css('--font-figures') || 'Roboto Mono, Noto Sans TC, monospace', color: css('--foreground') }, backgroundColor: 'transparent' };
}

function barOption(labels, values, width, { rowHeight = 0, barHeight = 30, labelSize = 14 } = {}) {
  const format = (value) => `${formatRevenue(value)} 億`;
  const labelWidth = Math.min(130, Math.max(98, Math.floor(width * .27)));
  const valueWidth = Math.max(...values.map((value) => format(value).length)) * 8.5 + 16;
  const labelGap = values.some((value) => value < 0) ? valueWidth + 8 : 8;
  const option = {
    ...base(), ...chartMotion,
    grid: { left: labelWidth + labelGap, right: valueWidth, top: 8, bottom: 8 },
    xAxis: { type: 'value', show: false, min: Math.min(0, ...values), max: values.every((value) => value === 0) ? 1 : Math.max(0, ...values) },
    yAxis: { type: 'category', data: labels, inverse: true, axisLine: { show: false }, axisTick: { show: false },
      axisLabel: { color: css('--foreground'), fontSize: 14, fontWeight: 700, width: labelWidth, margin: labelGap, overflow: 'break', lineHeight: 18, interval: 0 } },
    series: [{
      type: 'bar', data: values.map((v, i) => ({
        value: v,
        itemStyle: { color: i === values.length - 1 ? (css('--chart-primary') || css('--accent-text')) : css('--chart-neutral'),
          borderWidth: 0, borderRadius: parseFloat(css('--radius-control')) },
        label: { position: v < 0 ? 'left' : 'right' },
      })),
      barWidth: 30, barMinHeight: 4, showBackground: false,
      label: { show: true, position: 'right', distance: 8, fontFamily: css('--font-figures') || 'Roboto Mono', fontSize: 14, fontWeight: 700, color: css('--foreground'),
        formatter: (p) => format(p.value) },
    }],
  };
  if (!rowHeight) return option;
  // Editorial bars share the regions' label-above-bar layout and 8px insets.
  // Each row has the same numeric domain, so lengths remain comparable.
  return {
    ...option,
    grid: labels.map((_, i) => ({ left: values.some((v) => v < 0) ? valueWidth + 8 : 0, right: valueWidth, top: (i + 1) * rowHeight - barHeight - 8, height: barHeight })),
    xAxis: labels.map((_, i) => ({ ...option.xAxis, gridIndex: i })),
    yAxis: labels.map((label, i) => ({ type: 'category', data: [label], show: false, gridIndex: i })),
    graphic: labels.map((label, i) => ({ type: 'text', left: 0, top: i * rowHeight + 8,
      style: { text: label, fill: css('--foreground'), fontFamily: css('--font-figures') || 'Roboto Mono, Noto Sans TC, monospace', fontSize: labelSize, fontWeight: 700, lineHeight: 20 } })),
    series: values.map((_, i) => ({ ...option.series[0], barWidth: barHeight, xAxisIndex: i, yAxisIndex: i, data: [option.series[0].data[i]] })),
  };
}

async function mount(id, makeOption) {
  const el = document.getElementById(id);
  if (!el) return;
  if (el.dataset.chartMounted) return;
  el.dataset.chartMounted = 'true';
  // Mount every company chart without waiting for scrolling or a capture to reveal it.
  const echarts = await import('./echarts.js');
  const chart = echarts.init(el, null, { renderer: 'svg' });
  const paint = () => chart.setOption(makeOption(el.clientWidth, el), true);
  paint();
  const observer = new ResizeObserver(() => { chart.resize(); paint(); });
  observer.observe(el);
  addEventListener('themechange', paint);
}

function sources(data) {
  const sheet = document.getElementById('sheet');
  const body = document.getElementById('sheet-body');
  document.querySelectorAll('.src').forEach((b) => b.addEventListener('click', () => {
    const ids = (b.dataset.facts || '').split(',').filter(Boolean);
    body.replaceChildren();
    const h = document.createElement('h3');
    h.id = 'sheet-title';
    h.textContent = `${reportName(data.report)}出處`;
    sheet.setAttribute('aria-labelledby', h.id);
    body.append(h);
    ids.forEach((id) => {
      const f = data.sources[id];
      if (!f) return;
      const q = document.createElement('blockquote');
      q.textContent = f.statement;
      const m = document.createElement('div');
      m.className = 'muted';
      m.textContent = `${reportLabel(data.report)} 第 ${f.page} 頁｜期間：${f.period}｜編號 ${id}`;
      body.append(q, m);
    });
    if (data.mix?.facts?.some((id) => ids.includes(id))) {
      const breakdown = document.createElement('dl');
      breakdown.className = 'source-breakdown';
      mixItems(data.mix).items.forEach(({ name, value }) => {
        const term = document.createElement('dt');
        term.textContent = name;
        const valueEl = document.createElement('dd');
        valueEl.className = 'num';
        valueEl.textContent = `${value}%`;
        breakdown.append(term, valueEl);
      });
      body.append(breakdown);
    }
    const a = document.createElement('a');
    a.href = data.report.url; a.target = '_blank'; a.rel = 'noopener';
    a.textContent = `開啟${reportName(data.report)}原檔（${data.report.filename}）`;
    a.className = 'chip'; a.style.marginTop = '10px';
    body.append(a);
    sheet.showModal();
    h.tabIndex = -1;
    h.focus();
  }));
}

function watchlist(ticker) {
  const btn = document.getElementById('watch');
  if (!btn) return;
  const paint = () => { const on = getWatchlist().includes(ticker); btn.textContent = on ? '★ 觀察中' : '☆ 加入觀察';
    btn.setAttribute('aria-pressed', String(on));
    btn.style.background = on ? 'var(--accent-subtle)' : ''; btn.style.color = on ? 'var(--accent-text)' : ''; };
  btn.addEventListener('click', () => { const w = getWatchlist(); setWatchlist(w.includes(ticker) ? w.filter((t) => t !== ticker) : [...w, ticker]); paint(); });
  paint();
}

function share(data) {
  // 手機：連同分享卡圖片一起分享（Web Share API level 2）；不支援就只分享連結；桌面則複製連結
  document.getElementById('share')?.addEventListener('click', async () => {
    const payload = { title: `${data.name}（${data.ticker}）｜股.tw 研究室`, url: location.href };
    try {
      const res = await fetch(`/og/${data.ticker}.jpg`);
      const file = new File([await res.blob()], `${data.ticker}.jpg`, { type: 'image/jpeg' });
      if (navigator.canShare?.({ files: [file] })) await navigator.share({ ...payload, files: [file] });
      else if (navigator.share) await navigator.share(payload);
      else { await navigator.clipboard.writeText(location.href); alert('已複製連結'); }
    } catch (e) { /* 使用者取消分享 */ }
  });
}

function video() {
  // 頁面上只放封面；點封面或播放鍵，開全螢幕燈箱放大播放。
  // 只顯示 9:16 影片中間的正方形（y 280–1360，Shorts 版面的核心區）；打開燈箱才下載影片。
  const box = document.querySelector('figure.yt');
  const src = box?.dataset.video;
  if (!src) return;
  const alt = box.querySelector('img')?.alt || '公司速覽影片';
  const dlg = document.createElement('dialog');
  dlg.className = 'vbox';
  dlg.setAttribute('aria-label', alt);
  dlg.innerHTML = '<div class="vframe"><video playsinline controls preload="none" tabindex="0"></video><button class="vreplay" hidden>↻ 重播</button></div><button class="vclose" aria-label="關閉影片">✕</button>';
  document.body.append(dlg);
  const v = dlg.querySelector('video');
  const replay = dlg.querySelector('.vreplay');
  v.poster = box.querySelector('img')?.src || '';
  v.setAttribute('aria-label', alt);
  v.addEventListener('keydown', (e) => {
    if (e.code === 'Space') { e.preventDefault(); v.paused ? v.play() : v.pause(); }
  });
  v.addEventListener('ended', () => { v.currentTime = 0; replay.hidden = false; });
  v.addEventListener('play', () => { replay.hidden = true; });
  replay.addEventListener('click', () => v.play());
  dlg.querySelector('.vclose').addEventListener('click', () => dlg.close());
  dlg.addEventListener('click', (e) => { if (e.target === dlg) dlg.close(); });   // 點旁邊的暗處關閉
  dlg.addEventListener('close', () => { v.pause(); v.currentTime = 0; replay.hidden = true; });
  const open = () => {
    if (!v.src) v.src = src;
    dlg.showModal();
    v.focus();
    v.play().catch(() => {});
  };
  box.querySelector('.ytplay').addEventListener('click', open);
  box.querySelector('img')?.addEventListener('click', open);
}

export function initCompany() {
  const data = JSON.parse(document.getElementById('cdata').textContent);
  const describe = (id, label) => {
    const el = document.getElementById(id);
    if (el) { el.setAttribute('role', 'img'); el.setAttribute('aria-label', label); }
  };
  if (data.years.length) {
    describe('money', `歷年營收：${data.years.map((year, i) => `${year} 年 ${data.rev[i]} 億`).join('、')}`);
    mount('money', (width, el) => {
      const style = getComputedStyle(el);
      return barOption(data.years.map((y) => `${y} 營收`), data.rev, width, {
        rowHeight: parseFloat(style.getPropertyValue('--money-row-height')) || 0,
        barHeight: parseFloat(style.getPropertyValue('--money-bar-height')) || 30,
        labelSize: parseFloat(style.getPropertyValue('--money-label-size')) || 14,
      });
    });
  }
  sources(data);
  watchlist(data.ticker);
  share(data);
  video();
}
