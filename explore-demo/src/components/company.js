// 公司卡片頁的互動：圖表（捲到才載入 ECharts）、年報出處抽屜、觀察清單、分享。
import { inView } from 'motion';

const css = (v) => getComputedStyle(document.documentElement).getPropertyValue(v).trim();
const PALETTE = () => ['#FF573F', css('--fg'), '#FFB3A6', css('--muted'), '#E4DFD3', '#8A3324'];

// 重力落地：長條與圓餅都用 bounceOut，像重物落地後回彈兩下
const gravity = { animationDuration: 1300, animationEasing: 'bounceOut', animationDelay: (i) => i * 160 };

function base() {
  return { textStyle: { fontFamily: 'Noto Sans TC, sans-serif', color: css('--fg') }, backgroundColor: 'transparent' };
}

function mixOption(mix) {
  return {
    ...base(), ...gravity,
    tooltip: { trigger: 'item', formatter: (p) => `${p.name}：${p.value}%` },
    legend: { bottom: 0, textStyle: { color: css('--fg'), fontSize: 13 }, itemWidth: 14, itemHeight: 14 },
    color: PALETTE(),
    series: [{
      type: 'pie', radius: ['38%', '68%'], center: ['50%', '44%'], startAngle: 90,
      itemStyle: { borderColor: css('--fg'), borderWidth: 2.5 },
      label: { formatter: '{d|{c}%}', rich: { d: { fontFamily: 'Roboto Mono', fontWeight: 700, fontSize: 14, color: css('--fg') } } },
      data: mix.items.map(([n, v]) => ({ name: n, value: v })),
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
  inView(el, async () => {
    const echarts = await import('echarts');             // 圖表程式只在捲到時才下載
    const chart = echarts.init(el, null, { renderer: 'svg' });
    chart.setOption(makeOption());
    addEventListener('resize', () => chart.resize());
    addEventListener('themechange', () => chart.setOption(makeOption(), true));
  }, { margin: '0px 0px -15% 0px' });
}

function sources(data) {
  const sheet = document.getElementById('sheet');
  const body = document.getElementById('sheet-body');
  document.querySelectorAll('.src').forEach((b) => b.addEventListener('click', () => {
    const ids = (b.dataset.facts || '').split(',').filter(Boolean);
    body.replaceChildren();
    const h = document.createElement('h3');
    h.textContent = '年報出處';
    body.append(h);
    ids.forEach((id) => {
      const f = data.sources[id];
      if (!f) return;
      const q = document.createElement('blockquote');
      q.textContent = f.statement;
      const m = document.createElement('div');
      m.className = 'muted';
      m.textContent = `${data.report.fy} 年度年報 第 ${f.page} 頁｜期間：${f.period}｜編號 ${id}`;
      body.append(q, m);
    });
    const a = document.createElement('a');
    a.href = data.report.url; a.target = '_blank'; a.rel = 'noopener';
    a.textContent = `開啟年報原檔（${data.report.filename}）`;
    a.className = 'chip'; a.style.marginTop = '10px';
    body.append(a);
    sheet.showModal();
  }));
}

function watchlist(ticker) {
  const btn = document.getElementById('watch');
  if (!btn) return;
  const get = () => { try { return JSON.parse(localStorage.getItem('watch') || '[]'); } catch (e) { return []; } };
  const set = (v) => { try { localStorage.setItem('watch', JSON.stringify(v)); } catch (e) {} };
  const paint = () => { const on = get().includes(ticker); btn.textContent = on ? '★ 觀察中' : '☆ 加入觀察';
    btn.style.background = on ? '#FF573F' : ''; btn.style.color = on ? '#181715' : ''; };
  btn.addEventListener('click', () => { const w = get(); set(w.includes(ticker) ? w.filter((t) => t !== ticker) : [...w, ticker]); paint(); });
  paint();
}

function share(data) {
  document.getElementById('share')?.addEventListener('click', async () => {
    const payload = { title: `${data.name}（${data.ticker}）｜股.tw 研究室`, url: location.href };
    try {
      if (navigator.share) await navigator.share(payload);
      else { await navigator.clipboard.writeText(location.href); alert('已複製連結'); }
    } catch (e) { /* 使用者取消分享 */ }
  });
}

export function initCompany() {
  const data = JSON.parse(document.getElementById('cdata').textContent);
  if (data.mix) mount('mix', () => mixOption(data.mix));
  if (data.regions) mount('regions', () => barOption(data.regions.items.map((x) => x[0]), data.regions.items.map((x) => x[1]), '%', false));
  if (data.years.length) mount('money', () => barOption(data.years.map((y) => `${y} 營收`), data.rev.map((v) => (v >= 100 ? Math.round(v) : Math.round(v * 10) / 10)), ' 億', true));
  sources(data);
  watchlist(data.ticker);
  share(data);
}
