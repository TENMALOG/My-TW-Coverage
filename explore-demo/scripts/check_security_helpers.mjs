import assert from 'node:assert/strict';
import { serializeJsonForHtml, escapeHtml } from '../src/lib/html.js';

const payload = '</script><img src=x onerror=alert(1)><!--&"\'\u2028\u2029';
const data = { name: payload, nested: [payload] };
const serialized = serializeJsonForHtml(data);
assert.doesNotMatch(serialized, /[<>&\u2028\u2029]/);
assert.deepEqual(JSON.parse(serialized), data);
for (const code of ['003c', '003e', '0026', '2028', '2029']) {
  assert.ok(serialized.includes(`\\u${code}`));
}
console.log('serializeJsonForHtml:', serialized);

const escaped = escapeHtml(payload);
assert.doesNotMatch(escaped, /[<>"']/);
assert.equal(escapeHtml('&<>"\''), '&amp;&lt;&gt;&quot;&#39;');
assert.equal(escapeHtml(42), '42');
assert.equal(escapeHtml('年報 25%'), '年報 25%');
console.log('escapeHtml:', JSON.stringify(escaped));
console.log('PASS: inert HTML payload; all required characters escaped; JSON round-trip preserved.');
