import { defineConfig } from 'astro/config';

// Static output only: every page is pre-rendered from verified data (src/data), no server.
export default defineConfig({
  output: 'static',
  build: { format: 'directory' },
  // inline PostCSS config: stops Vite from picking up an unrelated postcss.config.js higher up the folder tree
  vite: { css: { postcss: { plugins: [] } } },
});
