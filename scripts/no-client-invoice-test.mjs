// Runs each live Worker's invoice code (downloaded from Cloudflare into <dir>/iptv-trial-<name>.js) with a fake
// clock and a fake Resend (no email is ever sent). Checks that a paid order NEVER emails the client, at any hour,
// for any price, and that the site inbox still gets one "sale / ..." notice. Used by verify-no-client-invoice.yml.
// Usage: node no-client-invoice-test.mjs <dir>
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { pathToFileURL } from "node:url";

const dir = process.argv[2];
const SITES = [
  ["maplestreamtv", "maplestreamtv.ca", ["12 Months - 1 Device — $49", "1 Month - 1 Device — $9", "3 Months - 1 Device — $29", "1 Month - 7 Devices — $63"]],
  ["maple4k", "maple4k.ca", ["12 Months - 1 Device — $49", "1 Month - 1 Device — $9", "3 Months - 2 Devices — $50"]],
  ["maplehd", "maplehd.ca", ["12 Months - 1 Device — $49", "1 Month - 1 Device — $9"]],
  ["iptvmapletv", "iptvmapletv.com", ["12 Months - 1 Device — $49", "6 Months - 1 Device — $39"]],
  ["iptvmojo", "iptvmojo.com", ["12 Months - 1 Device — $49", "1 Month - 1 Device — $9"]],
  ["mojo4ktv", "mojo4ktv.com", ["12 Months - 1 Device — $49", "1 Month - 1 Device — $9"]],
  ["buyiptvnorway", "buyiptvnorway.com", ["12 Months - 1 Device — $49", "3 Months - 1 Device — $29"]],
  ["norgesiptv", "norgesiptv.com", ["12 måneder – 1 tilkobling – kr 441"]],
  ["flimmerkanal", "flimmerkanal.de", ["1 Jahr / 1 Verbindung / 49€", "1 Monat / 1 Verbindung / 9€"]],
  ["iptvvde", "iptvv.de", ["12 Monate / 1 Gerät / 49 €", "1 Monat / 1 Gerät / 9 €"]],
  ["mojo4kde", "mojo4k.de", ["12 Monate / 1 Gerät / 49 €", "1 Monat / 1 Gerät / 9 €"]],
  ["streamdeutschland", "streamdeutschland.de", ["12 Monate / 1 Gerät / 49 €"]],
  ["mojo4kfr", "mojo4k.fr", ["1 Appareil — 1 Année — 49€", "1 Appareil — 1 Mois — 9€"]],
  ["streambleu", "streambleu.fr", ["12 mois - 1 appareil — 49 €", "1 mois - 1 appareil — 9 €"]],
];
const TIMES = ["00:30:00", "02:30:00", "05:00:00", "09:00:00", "12:00:00", "17:00:00", "21:00:00", "23:59:00"];

const RealDate = Date;
let fakeNow = 0;
class FakeDate extends RealDate {
  constructor(...a) { super(...(a.length ? a : [fakeNow])); }
  static now() { return fakeNow; }
}
globalThis.Date = FakeDate;
let sent = [];
globalThis.fetch = async (url, init) => {
  if (String(url).startsWith("https://api.resend.com/")) { sent.push(JSON.parse(init.body)); return new Response('{"id":"fake"}', { status: 200 }); }
  throw new Error("unexpected fetch " + url);
};
const kv = () => { const m = new Map(); return { get: async (k) => m.get(k) ?? null, put: async (k, v) => m.set(k, v), delete: async (k) => m.delete(k), list: async () => ({ keys: [] }) }; };

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "nc-"));
let fail = 0, n = 0;
for (const [w, domain, plans] of SITES) {
  const src = fs.readFileSync(path.join(dir, `iptv-trial-${w}.js`), "utf8");
  const staticOk = !src.includes("T().subject, invoiceEmail(") && src.includes('const INVOICE_MODE = "notify_owner"');
  const copy = path.join(tmp, w + ".mjs");
  fs.writeFileSync(copy, src);
  const mod = await import(pathToFileURL(copy).href);
  let ok = staticOk, cases = 0;
  for (const plan of plans) for (const t of TIMES) {
    fakeNow = RealDate.parse(`2026-11-16T${t}Z`);
    sent = [];
    const client = `client${t.replace(/:/g, "")}@example.com`;
    const env = { RESEND_KEY: "fake", RESEND_API_KEY: "fake", TRIALS: kv(), TRIAL_KV: kv() };
    const res = await mod.default.fetch(new Request("https://worker.example/invoice", { method: "POST", headers: { Origin: `https://${domain}`, "Content-Type": "application/json" }, body: JSON.stringify({ name: "Test Client", email: client, plan }) }), env, { waitUntil() {} });
    const j = await res.json();
    const toClient = sent.filter((e) => [].concat(e.to).includes(client));
    const toAdmin = sent.filter((e) => !toClient.includes(e));
    const c = res.status === 200 && j.invoice === false && toClient.length === 0 && toAdmin.length === 1 && toAdmin[0].subject.startsWith(`sale / ${domain} /`);
    n++; cases++;
    if (!c) { ok = false; fail++; console.log("FAIL", w, plan, t, res.status, j, sent.map((e) => [e.to, e.subject])); }
  }
  console.log(`${domain.padEnd(22)} live code: client send removed=${staticOk}  ${cases} orders → client emails: 0 expected  ${ok ? "PASS" : "FAIL"}`);
}
console.log(`${n - fail}/${n} orders passed`);
process.exit(fail ? 1 : 0);
