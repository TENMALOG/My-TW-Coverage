import { defineConfig } from 'astro/config';

// Static output only: every page is pre-rendered from verified data (src/data), no server.
export default defineConfig({
  site: 'https://research.xn--g10a.tw',
  trailingSlash: 'always',
  output: 'static',
  build: { format: 'directory' },
  // inline PostCSS config: stops Vite from picking up an unrelated postcss.config.js higher up the folder tree
  vite: {
    // Keep Vite's writable cache in this checkout; node_modules is shared.
    cacheDir: './.astro/vite',
    css: { postcss: { plugins: [] } },
  },
});
