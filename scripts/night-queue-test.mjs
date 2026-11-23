// Runs each Worker's invoice code (live copies downloaded from Cloudflare into <dir>/iptv-trial-<name>.js, or a repo
// worker.js) with a fake clock, a fake KV and a fake Resend: no email is ever sent. Checks that:
//  - from 05:00 to 00:59 UTC a paid order emails the client the invoice with the right link for its price;
//  - from 01:00 to 04:59 UTC the order is queued (client gets nothing yet, site inbox gets "sale queued");
//  - /invoice-flush sends nothing before 05:00 and sends each queued invoice exactly once from 05:00;
//  - a daytime order also sends what is still queued; norgesiptv.com stays manual.
// Usage: node night-queue-test.mjs <dir> [--pages <path to mojo4k.uk functions/api/invoice.js>]
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { pathToFileURL } from "node:url";

const LINKS = {
  9: "Andiamo", 18: "Allons-y", 27: "Vamonos", 29: "Deutschland", 36: "Pme", 39: "VamosLa", 45: "Idemo", 49: "osterreich", 50: "Magyarorszg", 69: "DanubeDuo", 75: "MediterraneanTrio", 89: "WesternFour", 99: "CentralEFour", 105: "SunSeaFive", 120: "TheGrandTourSix", 135: "WesternSouthernSeven", 140: "CentralEasternEight", 175: "TheGrandEuropeanNine", 180: "TheExpandedEuropeTen", 225: "TheCompleteCollection",
};
const url = (k) => `https://www.exploringnewlocationdaily.com/l/${k}?wanted=true`;
// [months, devices, price] for the USD/EUR plans, and mojo4k.uk's GBP plans with the USD price they map to.
const PLANS = [[1,1,9],[3,1,29],[6,1,39],[12,1,49],[1,2,18],[3,2,50],[6,2,69],[12,2,89],[1,3,27],[3,3,75],[6,3,105],[12,3,135],
  [1,4,36],[3,4,99],[6,4,140],[12,4,180],[1,5,45],[3,5,120],[6,5,175],[12,5,225]];
const UK = [[1,1,7,9],[1,2,12,18],[1,3,17,27],[1,4,23,36],[1,5,27,45],[6,1,29,39],[6,2,49,69],[6,3,71,105],[6,4,90,140],[6,5,117,175],
  [12,1,39,49],[12,2,62,89],[12,3,83,135],[12,4,110,180],[12,5,138,225]];
const en = (m, d, p) => `${m} Month${m > 1 ? "s" : ""} - ${d} Device${d > 1 ? "s" : ""} — $${p}`;
const de = (m, d, p) => `${m} Monat${m > 1 ? "e" : ""} / ${d} ${d > 1 ? "Geräte" : "Gerät"} / ${p} €`;
const fr = (m, d, p) => `${d} Appareil${d > 1 ? "s" : ""} — ${m} Mois — ${p}€`;
const SITES = [
  ["maplestreamtv", "maplestreamtv.ca", en], ["maple4k", "maple4k.ca", en], ["maplehd", "maplehd.ca", en],
  ["iptvmapletv", "iptvmapletv.com", en], ["iptvmojo", "iptvmojo.com", en], ["mojo4ktv", "mojo4ktv.com", en],
  ["buyiptvnorway", "buyiptvnorway.com", en], ["flimmerkanal", "flimmerkanal.de", de], ["iptvvde", "iptvv.de", de],
  ["mojo4kde", "mojo4k.de", de], ["streamdeutschland", "streamdeutschland.de", de], ["mojo4kfr", "mojo4k.fr", fr],
  ["streambleu", "streambleu.fr", fr], ["norgesiptv", "norgesiptv.com", null],
];

const RealDate = Date;
let fakeNow = 0;
class FakeDate extends RealDate {
  constructor(...a) { super(...(a.length ? a : [fakeNow])); }
  static now() { return fakeNow; }
}
globalThis.Date = FakeDate;
let sent = [];
globalThis.fetch = async (u, init) => {
  if (String(u).startsWith("https://api.resend.com/")) { sent.push(JSON.parse(init.body)); return new Response('{"id":"fake"}', { status: 200 }); }
  throw new Error("unexpected fetch " + u);
};
const fakeKV = () => {
  const m = new Map();
  return { m, get: async (k) => m.get(k) ?? null, put: async (k, v) => { m.set(k, v); }, delete: async (k) => { m.delete(k); },
    list: async ({ prefix = "" } = {}) => ({ keys: [...m.keys()].filter((k) => k.startsWith(prefix)).map((name) => ({ name })), list_complete: true }) };
};
const at = (t) => { fakeNow = RealDate.parse(`2026-11-19T${t}Z`); };

function scriptOf(file) {
  let src = fs.readFileSync(file, "utf8");
  if (src.startsWith("--")) { // Cloudflare's multipart download: keep only the script part
    const boundary = src.slice(0, src.search(/\r?\n/));
    const part = src.split(boundary)[1];
    src = part.slice(part.search(/\r?\n\r?\n/)).replace(/^\r?\n\r?\n/, "").replace(/\r?\n$/, "");
  }
  return src;
}

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "nq-"));
let fail = 0, n = 0;
const check = (ok, label, extra) => { n++; if (!ok) { fail++; console.log("  FAIL", label, extra ?? ""); } return ok; };

async function runSite(label, domain, call, plans) {
  const before = fail;
  const env = () => { const kv = fakeKV(); return { kv, e: { RESEND_KEY: "fake", RESEND_API_KEY: "fake", TRIALS: kv, TRIAL_KV: kv } }; };
  const order = async (e, plan, email) => {
    sent = [];
    const r = await call(new Request(`https://worker.example${label === "pages" ? "/api" : ""}/invoice`, { method: "POST", headers: { Origin: `https://${domain}`, "Content-Type": "application/json" }, body: JSON.stringify({ name: "Test Client", email, plan }) }), e);
    return { status: r.status, j: await r.json(), mails: sent.slice() };
  };
  const flush = async (e) => { sent = []; const r = await call(new Request(`https://worker.example${label === "pages" ? "/api" : ""}/invoice-flush`, { method: "POST" }), e); return { status: r.status, j: await r.json(), mails: sent.slice() }; };

  if (!plans) { // norgesiptv.com: always manual
    for (const t of ["00:59:00", "02:00:00", "05:00:00", "15:00:00"]) {
      at(t); const { e } = env(); const c = `c${t.replace(/:/g, "")}@example.com`;
      const r = await order(e, "12 måneder – 1 tilkobling – kr 441", c);
      check(r.mails.length === 1 && ![].concat(r.mails[0].to).includes(c) && r.mails[0].subject.startsWith(`sale / ${domain}`), `${domain} manual ${t}`, r.mails.map((m) => m.subject));
    }
    return fail === before;
  }
  // Every price, daytime (00:59 and 05:00 and 14:00): client gets the invoice with that price's link.
  for (const [plan, usd] of plans) for (const t of ["00:59:00", "05:00:00", "14:00:00"]) {
    at(t); const { e } = env(); const c = `day${usd}@example.com`;
    const r = await order(e, plan, c);
    const toC = r.mails.filter((m) => [].concat(m.to).includes(c));
    check(r.j.invoice === true && toC.length === 1 && toC[0].html.includes(url(LINKS[usd])), `${domain} ${t} ${plan} → client invoice with link ${LINKS[usd]}`, r.mails.map((m) => m.subject));
    check(r.mails.length === 2 && r.mails.some((m) => m.subject.startsWith(`invoice / ${domain} / $${usd} /`)), `${domain} ${t} ${plan} admin copy`, r.mails.map((m) => m.subject));
  }
  // Night: queued at 01:00, 02:30, 04:59; flush at 04:59 sends nothing; flush at 05:00 sends all once.
  const { kv, e } = env();
  const night = plans.filter((_, i) => i % 5 === 0).slice(0, 3);
  const times = ["01:00:00", "02:30:00", "04:59:00"];
  for (let i = 0; i < night.length; i++) {
    at(times[i]); const c = `night${i}@example.com`;
    const r = await order(e, night[i][0], c);
    check(r.j.queued === true && r.mails.length === 1 && !r.mails.some((m) => [].concat(m.to).includes(c)) && r.mails[0].subject.startsWith(`sale queued / ${domain}`), `${domain} night order ${times[i]} queued`, [r.j, r.mails.map((m) => m.subject)]);
  }
  const queued = [...kv.m.keys()].filter((k) => k.startsWith(`invoiceq:`)).length;
  check(queued === night.length, `${domain} ${night.length} orders in queue`, queued);
  at("04:59:30"); let f = await flush(e);
  check(f.mails.length === 0, `${domain} flush at 04:59 sends nothing`, f.mails.map((m) => m.subject));
  at("05:00:00"); f = await flush(e);
  for (let i = 0; i < night.length; i++) {
    const c = `night${i}@example.com`, usd = night[i][1];
    const toC = f.mails.filter((m) => [].concat(m.to).includes(c));
    check(toC.length === 1 && toC[0].html.includes(url(LINKS[usd])), `${domain} 05:00 flush emails night client ${i} ($${usd})`, f.mails.map((m) => [m.to, m.subject]));
  }
  check(f.j.sent === night.length && f.mails.filter((m) => m.subject.includes("from night queue")).length === night.length, `${domain} 05:00 flush admin copies`, f.j);
  check([...kv.m.keys()].filter((k) => k.startsWith("invoiceq:")).length === 0, `${domain} queue empty after flush`);
  f = await flush(e);
  check(f.mails.length === 0, `${domain} second flush sends nothing`, f.mails.length);
  // A night order left in the queue is also sent by the next daytime order.
  at("03:00:00"); await order(e, plans[0][0], "late@example.com");
  at("08:00:00"); const r = await order(e, plans[1][0], "morning@example.com");
  check(r.mails.some((m) => [].concat(m.to).includes("late@example.com")) && r.mails.some((m) => [].concat(m.to).includes("morning@example.com")), `${domain} daytime order also sends the queued one`, r.mails.map((m) => [m.to, m.subject]));
  return fail === before;
}

const dir = process.argv[2];
const pagesAt = process.argv.indexOf("--pages");
for (const [w, domain, fmt] of SITES) {
  const file = path.join(dir, `iptv-trial-${w}.js`);
  if (!fs.existsSync(file)) { console.log(`${domain.padEnd(22)} (no script, skipped)`); continue; }
  const copy = path.join(tmp, w + ".mjs");
  fs.writeFileSync(copy, scriptOf(file));
  const mod = await import(pathToFileURL(copy).href);
  const call = (req, env) => mod.default.fetch(req, env, { waitUntil() {} });
  const plans = fmt && PLANS.map(([m, d, p]) => [fmt(m, d, p), p]);
  const ok = await runSite("worker", domain, call, plans);
  console.log(`${domain.padEnd(22)} ${ok ? "PASS" : "FAIL"}`);
}
if (pagesAt > 0) {
  const src = fs.readFileSync(process.argv[pagesAt + 1], "utf8");
  const copy = path.join(tmp, "mojo4kuk.mjs");
  fs.writeFileSync(copy, src);
  const mod = await import(pathToFileURL(copy).href);
  const call = async (req, env) => (await mod.onRequest({ request: req, env }));
  const plans = UK.map(([m, d, gbp, usd]) => [`${m} Month${m > 1 ? "s" : ""} · ${d} Device${d > 1 ? "s" : ""} — £${gbp}`, usd]);
  const ok = await runSite("pages", "mojo4k.uk", call, plans);
  console.log(`${"mojo4k.uk".padEnd(22)} ${ok ? "PASS" : "FAIL"}`);
}
console.log(`${n - fail}/${n} checks passed`);
process.exit(fail ? 1 : 0);
