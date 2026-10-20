import type { APIRoute } from 'astro';
import companies from '../data/companies.json';
import industries from '../data/industries.json';

export const prerender = true;

const escapeXml = (value: string) => value.replace(/[<>&"']/g, (char) => ({
  '<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;', "'": '&apos;',
})[char]!);

export const GET: APIRoute = ({ site }) => {
  if (!site) throw new Error('產生 sitemap 前，請先設定正式站台網址。');

  const paths = [
    '/', '/search/', '/compare/', '/screen/', '/watch/', '/map/',
    '/about/', '/errata/', '/license/', '/privacy/',
    ...companies.map(({ ticker }) => `/c/${encodeURIComponent(ticker)}/`),
    ...industries.map(({ slug }) => `/i/${encodeURIComponent(slug)}/`),
    '/story/semiconductors/',
  ];
  const urls = paths.map((path) => `  <url><loc>${escapeXml(new URL(path, site).href)}</loc></url>`).join('\n');

  return new Response(`<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls}\n</urlset>\n`, {
    headers: { 'Content-Type': 'application/xml; charset=utf-8' },
  });
};
