// Usage: node scheduled-sender-test.mjs <mojo4k.de worker.js or live download>
// Fake-clock test of mojo4k.de's hourly scheduled sender: it must call every site's flush outside 01-04 UTC.
import { pathToFileURL } from "node:url"; import fs from "node:fs";
const RealDate = Date; let now = 0;
globalThis.Date = class extends RealDate { constructor(...a) { super(...(a.length ? a : [now])); } static now() { return now; } };
const calls = []; let sent = [];
globalThis.fetch = async (u, init) => { u = String(u);
  if (u.startsWith("https://api.resend.com/")) { sent.push(JSON.parse(init.body)); return new Response("{}"); }
  if (u.startsWith("https://mojo4k.uk/api/invoice-flush")) { calls.push("mojo4k.uk"); return new Response('{"ok":true,"sent":0}'); }
  return new Response("[]"); };
let src = fs.readFileSync(process.argv[2], "utf8");
if (src.startsWith("--")) { const b = src.slice(0, src.search(/\r?\n/)); const part = src.split(b)[1]; src = part.slice(part.search(/\r?\n\r?\n/)).replace(/^\r?\n\r?\n/, "").replace(/\r?\n$/, ""); } const f = process.argv[2] + ".mjs"; fs.writeFileSync(f, src);
const mod = await import(pathToFileURL(f).href);
const m = new Map(); const kv = { get: async (k) => m.get(k) ?? null, put: async (k, v) => m.set(k, v), delete: async (k) => m.delete(k), list: async ({ prefix }) => ({ keys: [...m.keys()].filter((k) => k.startsWith(prefix)).map((name) => ({ name })), list_complete: true }) };
const env = { TRIALS: kv, RESEND_KEY: "x" };
for (const b of ["FLUSH_MAPLE4K","FLUSH_MAPLEHD","FLUSH_MAPLESTREAMTV","FLUSH_IPTVMAPLETV","FLUSH_IPTVMOJO","FLUSH_MOJO4KTV","FLUSH_BUYIPTVNORWAY","FLUSH_FLIMMERKANAL","FLUSH_IPTVVDE","FLUSH_STREAMDEUTSCHLAND","FLUSH_MOJO4KFR","FLUSH_STREAMBLEU"])
  env[b] = { fetch: async (u) => { calls.push(b + " " + new URL(u).pathname); return new Response('{"ok":true,"sent":0}'); } };
let fail = 0;
// queue a night order on mojo4k.de at 02:00, then run the cron at 03:00 (nothing) and 05:00 (all sites + the order).
now = RealDate.parse("2026-11-20T02:00:00Z");
await mod.default.fetch(new Request("https://w/invoice", { method: "POST", headers: { Origin: "https://mojo4k.de" }, body: JSON.stringify({ name: "A", email: "a@example.com", plan: "12 Monate / 1 Gerät / 49 €" }) }), env, {});
for (const [t, expect] of [["03:00", 0], ["05:00", 13]]) {
  now = RealDate.parse(`2026-11-20T${t}:00Z`); calls.length = 0; sent = []; const ps = [];
  await mod.default.scheduled({}, env, { waitUntil: (p) => ps.push(p) }); await Promise.allSettled(ps);
  const toClient = sent.filter((e) => [].concat(e.to).includes("a@example.com")).length;
  const ok = calls.length === expect && toClient === (t === "05:00" ? 1 : 0);
  if (!ok) fail++;
  console.log(t, "site flush calls:", calls.length, "client invoices:", toClient, ok ? "PASS" : "FAIL");
}
process.exit(fail);
