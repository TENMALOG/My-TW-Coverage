import { use, init as initChart } from 'echarts/core';
import { BarChart, LineChart, PieChart, ScatterChart, GraphChart } from 'echarts/charts';
import { GridComponent, TooltipComponent, LegendComponent, DataZoomComponent, GraphicComponent } from 'echarts/components';
import { CanvasRenderer, SVGRenderer } from 'echarts/renderers';

use([
  BarChart, LineChart, PieChart, ScatterChart, GraphChart,
  GridComponent, TooltipComponent, LegendComponent, DataZoomComponent, GraphicComponent,
  CanvasRenderer, SVGRenderer,
]);

// Visual defaults only: preserve chart data, layouts, and event handling.
export function init(element, theme, options) {
  const css = (token) => getComputedStyle(document.documentElement).getPropertyValue(token).trim();
  const axis = {
    axisLabel: { color: css('--text-muted') },
    nameTextStyle: { color: css('--text-muted') },
    axisLine: { lineStyle: { color: css('--border') } },
    axisTick: { lineStyle: { color: css('--border') } },
    splitLine: { lineStyle: { color: css('--border-subtle') } },
  };
  return initChart(element, theme || {
    animation: false,
    color: [css('--chart-primary') || css('--accent'), css('--chart-second') || css('--foreground'), css('--chart-neutral'), css('--chart-neutral-light') || css('--chart-secondary')],
    textStyle: { color: css('--foreground') },
    categoryAxis: axis, valueAxis: axis, logAxis: axis,
    legend: { textStyle: { color: css('--foreground') } },
    graph: { force: { layoutAnimation: false } },
    tooltip: {
      backgroundColor: css('--surface-raised'), borderColor: css('--border'), borderWidth: 1,
      textStyle: { color: css('--foreground') }, transitionDuration: 0,
      extraCssText: 'background:var(--surface-raised);color:var(--foreground);border-color:var(--border);border-radius:var(--radius-panel);box-shadow:var(--shadow-floating)',
    },
  }, options);
}
