// 公司卡片頁的互動：圖表（捲到才載入 ECharts）、年報出處抽屜、觀察清單、分享。
import { watchlist as getWatchlist, setWatchlist, onVisible } from './tools.js';
import { reportName, reportLabel } from '../lib/report.js';
import { escapeHtml } from '../lib/html.js';

const css = (v) => getComputedStyle(document.documentElement).getPropertyValue(v).trim();
const PALETTE = () => ['#FF573F', css('--fg'), '#FFB3A6', css('--muted'), '#E4DFD3', '#8A3324'];

// 重力落地：長條與圓餅都用 bounceOut，像重物落地後回彈兩下
const gravity = { animationDuration: 1300, animationEasing: 'bounceOut', animationDelay: (i) => i * 160 };

function base() {
  return { textStyle: { fontFamily: 'Noto Sans TC, sans-serif', color: css('--fg') }, backgroundColor: 'transparent' };
}

function mixOption(mix, sourceName) {
  const total = mix.items.reduce((sum, [, value]) => sum + Number(value), 0);
  const items = mix.items.map(([name, value]) => ({ name, value }));
  if (total < 99.5) items.push({ name: '其他／未列', value: +(100 - total).toFixed(2), itemStyle: { color: css('--muted') } });
  const note = total > 100.5 ? `各項加總 ${+total.toFixed(2)}%，可能有重疊` : '';
  return {
    ...base(), ...gravity,
    tooltip: { trigger: 'item', formatter: (p) => `${escapeHtml(p.name)}：${escapeHtml(p.value)}%${p.name === '其他／未列' ? `<br>${escapeHtml(sourceName)}未逐項列出的部分` : ''}${note ? `<br>${escapeHtml(note)}` : ''}` },
    legend: { bottom: 0, textStyle: { color: css('--fg'), fontSize: 13 }, itemWidth: 14, itemHeight: 14 },
    color: PALETTE(),
    series: [{
      type: 'pie', radius: ['38%', '68%'], center: ['50%', '44%'], startAngle: 90,
      itemStyle: { borderColor: css('--fg'), borderWidth: 2.5 },
      label: { formatter: '{d|{c}%}', rich: { d: { fontFamily: 'Roboto Mono', fontWeight: 700, fontSize: 14, color: css('--fg') } } },
      data: items,
      animationType: 'expansion',
    }],
  };
}

function barOption(labels, values, unit, highlightLast) {
  return {
    ...base(), ...gravity,
    grid: { left: 8, right: 56, top: 8, bottom: 8, containLabel: true },
    xAxis: { type: 'value', show: false },
    yAxis: { type: 'category', data: labels, inverse: true, axisLine: { show: false }, axisTick: { show: false },
      axisLabel: { color: css('--fg'), fontSize: 14, fontWeight: 700 } },
    series: [{
      type: 'bar', data: values.map((v, i) => ({
        value: v,
        itemStyle: { color: (highlightLast ? i === values.length - 1 : i === 0) ? '#FF573F' : css('--card'),
          borderColor: css('--fg'), borderWidth: 2.5, borderRadius: 12 },
      })),
      barWidth: 30,
      label: { show: true, position: 'right', fontFamily: 'Roboto Mono', fontWeight: 700, color: css('--fg'),
        formatter: (p) => `${p.value.toLocaleString('en-US', { maximumFractionDigits: 2 })}${unit}` },
    }],
  };
}

async function mount(id, makeOption) {
  const el = document.getElementById(id);
  if (!el) return;
  onVisible(el, async () => {
    if (el.dataset.chartMounted) return;
    el.dataset.chartMounted = 'true';
    const echarts = await import('./echarts.js');       // 圖表程式只在捲到時才下載
    const chart = echarts.init(el, null, { renderer: 'svg' });
    chart.setOption(makeOption());
    const observer = new ResizeObserver(() => chart.resize());
    observer.observe(el);
    addEventListener('themechange', () => chart.setOption(makeOption(), true));
  }, '0px 0px -15% 0px');
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
    btn.style.background = on ? '#FF573F' : ''; btn.style.color = on ? '#181715' : ''; };
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
  if (data.mix) {
    const option = mixOption(data.mix, reportName(data.report));
    describe('mix', `營收結構：${option.series[0].data.map(({ name, value }) => `${name} ${value}%`).join('、')}${data.mix.items.reduce((sum, [, v]) => sum + Number(v), 0) > 100.5 ? '；各項可能有重疊' : ''}`);
    mount('mix', () => mixOption(data.mix, reportName(data.report)));
  }
  if (data.regions) {
    describe('regions', `地區營收結構：${data.regions.items.map(([name, value]) => `${name} ${value}%`).join('、')}`);
    mount('regions', () => barOption(data.regions.items.map((x) => x[0]), data.regions.items.map((x) => x[1]), '%', false));
  }
  if (data.years.length) {
    describe('money', `歷年營收：${data.years.map((year, i) => `${year} 年 ${data.rev[i]} 億`).join('、')}`);
    mount('money', () => barOption(data.years.map((y) => `${y} 營收`), data.rev.map((v) => (v >= 100 ? Math.round(v) : Math.round(v * 10) / 10)), ' 億', true));
  }
  sources(data);
  watchlist(data.ticker);
  share(data);
  video();
}
