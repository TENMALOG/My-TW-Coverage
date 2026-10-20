import { use, init } from 'echarts/core';
import { BarChart, LineChart, PieChart, ScatterChart, GraphChart } from 'echarts/charts';
import { GridComponent, TooltipComponent, LegendComponent, DataZoomComponent } from 'echarts/components';
import { CanvasRenderer, SVGRenderer } from 'echarts/renderers';

use([
  BarChart, LineChart, PieChart, ScatterChart, GraphChart,
  GridComponent, TooltipComponent, LegendComponent, DataZoomComponent,
  CanvasRenderer, SVGRenderer,
]);

export { init };
