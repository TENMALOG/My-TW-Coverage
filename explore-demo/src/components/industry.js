import { onVisible } from './tools.js';
// 產業頁互動：營收×毛利率散點圖、產業內往來關係力導向圖、證交所產業別篩選。

const css = (v) => getComputedStyle(document.documentElement).getPropertyValue(v).trim();

async function mount(id, makeOption, onClick) {
  const el = document.getElementById(id);
  if (!el) return;
  onVisible(el, async () => {
    if (el.dataset.chartMounted) return;
    el.dataset.chartMounted = 'true';
    const echarts = await import('./echarts.js');
    const chart = echarts.init(el, null, { renderer: 'canvas' });
    chart.setOption(makeOption());
    if (onClick) chart.on('click', onClick);
    const observer = new ResizeObserver(() => chart.resize());
    observer.observe(el);
    addEventListener('themechange', () => chart.setOption(makeOption(), true));
  }, '0px 0px -15% 0px');
}

function scatter(rows) {
  const pts = rows.filter((r) => r.rev > 0 && r.gm != null);
  return {
    textStyle: { fontFamily: 'Noto Sans TC, sans-serif', color: css('--fg') },
    grid: { left: 44, right: 16, top: 16, bottom: 36 },
    tooltip: { formatter: (p) => `${p.data.n}（${p.data.t}）<br>營收 ${p.data.value[0].toLocaleString('en-US', { maximumFractionDigits: 1 })} 億｜毛利率 ${p.data.value[1]}%` },
    xAxis: { type: 'log', name: '營收（億）', nameLocation: 'middle', nameGap: 24, axisLabel: { color: css('--muted') },
      splitLine: { lineStyle: { color: css('--line') } } },
    yAxis: { type: 'value', axisLabel: { color: css('--muted'), formatter: '{value}%' }, splitLine: { lineStyle: { color: css('--line') } } },
    dataZoom: [{ type: 'inside' }],
    animationDuration: 1100, animationEasing: 'bounceOut', animationDelay: (i) => i * 6,
    series: [{
      type: 'scatter', symbolSize: (v) => 8 + Math.min(26, Math.sqrt(v[0]) / 4),
      itemStyle: { color: '#FF573F', borderColor: css('--fg'), borderWidth: 1.5, opacity: 0.9 },
      emphasis: { label: { show: true, formatter: (p) => p.data.n, color: css('--fg'), fontWeight: 700 } },
      data: pts.map((r) => ({ value: [Math.round(r.rev * 10) / 10, r.gm], n: r.n, t: r.t })),
    }],
  };
}

function graph(d) {
  const deg = {};
  d.edges.forEach((e) => { deg[e.s] = (deg[e.s] || 0) + 1; deg[e.d] = (deg[e.d] || 0) + 1; });
  const nodes = Object.keys(deg).map((t) => ({ id: t, name: d.names[t] || t, t, symbolSize: 16 + deg[t] * 5,
    itemStyle: { color: deg[t] > 2 ? '#FF573F' : css('--card'), borderColor: css('--fg'), borderWidth: 2 } }));
  return {
    textStyle: { fontFamily: 'Noto Sans TC, sans-serif', color: css('--fg') },
    tooltip: { formatter: (p) => (p.dataType === 'edge' ? `${d.names[p.data.source]} → ${d.names[p.data.target]}` : `${p.data.name}（${p.data.t}）`) },
    series: [{
      type: 'graph', layout: 'force', roam: true, draggable: true,
      force: { repulsion: 180, edgeLength: [60, 140], gravity: 0.08 },
      label: { show: true, position: 'bottom', color: css('--fg'), fontSize: 12 },
      edgeSymbol: ['none', 'arrow'], edgeSymbolSize: 8,
      lineStyle: { color: css('--muted'), width: 1.5, curveness: 0.15 },
      data: nodes, links: d.edges.map((e) => ({ source: e.s, target: e.d })),
    }],
  };
}

function filters() {
  const bar = document.getElementById('filters');
  bar?.addEventListener('click', (ev) => {
    const b = ev.target.closest('button');
    if (!b) return;
    bar.querySelectorAll('button').forEach((x) => x.classList.toggle('on', x === b));
    document.querySelectorAll('#list > a').forEach((a) => { a.style.display = !b.dataset.m || a.dataset.m === b.dataset.m ? '' : 'none'; });
  });
}

export function initIndustry() {
  const d = JSON.parse(document.getElementById('idata').textContent);
  const go = (p) => { if (p.data?.t) location.href = `/c/${p.data.t}/`; };
  const scatterEl = document.getElementById('scatter');
  scatterEl?.setAttribute('role', 'img');
  const pts = d.rows.filter((r) => r.rev > 0 && r.gm != null).sort((a, b) => b.rev - a.rev);
  scatterEl?.setAttribute('aria-label', `公司營收與毛利率散點圖，共 ${pts.length} 家；營收最大的 ${Math.min(10, pts.length)} 家：${pts.slice(0, 10).map((r) => `${r.n}，營收 ${Math.round(r.rev).toLocaleString('en-US')} 億、毛利率 ${r.gm}%`).join('；')}`);
  mount('scatter', () => scatter(d.rows), go);
  if (d.edges.length) {
    const graphEl = document.getElementById('graph');
    graphEl?.setAttribute('role', 'img');
    graphEl?.setAttribute('aria-label', `公司往來關係圖：${d.edges.map((e) => `${d.names[e.s] || e.s} 指向 ${d.names[e.d] || e.d}`).join('；')}`);
    mount('graph', () => graph(d), (p) => p.dataType === 'node' && go(p));
  }
  filters();
}
