// Runs each live Worker's invoice code (downloaded from Cloudflare into <dir>/<worker>.js) with a faked clock
// and a fake Resend: no email is sent. Used by .github/workflows/verify-night-pause.yml.
// Usage: node night-pause-test.mjs <dir>
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { pathToFileURL } from "node:url";

const dir = process.argv[2];
const SITES = [
  ["maplestreamtv.ca", "maplestreamtv.ca", "12 Months - 1 Device — $49"],
  ["maple4k-ca", "maple4k.ca", "12 Months - 1 Device — $49"],
  ["maplehd-ca", "maplehd.ca", "12 Months - 1 Device — $49"],
  ["iptvmapletv.com", "iptvmapletv.com", "12 Months - 1 Device — $49"],
  ["iptvmojo.com", "iptvmojo.com", "12 Months - 1 Device — $49"],
  ["mojo4ktv.com", "mojo4ktv.com", "12 Months - 1 Device — $49"],
  ["buyiptvnorway.com", "buyiptvnorway.com", "12 Months - 1 Device — $49"],
  ["norgesiptv.com", "norgesiptv.com", "12 måneder – 1 tilkobling – kr 441"],
  ["flimmerkanal.de", "flimmerkanal.de", "1 Jahr / 1 Verbindung / 49€"],
  ["iptvv.de", "iptvv.de", "12 Monate / 1 Gerät / 49 €"],
  ["mojo4k.de", "mojo4k.de", "12 Monate / 1 Gerät / 49 €"],
  ["streamdeutschland.de", "streamdeutschland.de", "12 Monate / 1 Gerät / 49 €"],
  ["mojo4k.fr", "mojo4k.fr", "1 Appareil — 1 Année — 49€"],
  ["streambleu-fr", "streambleu.fr", "12 mois - 1 appareil — 49 €"],
];
const WORKER = {"maplestreamtv.ca": "maplestreamtv", "maple4k-ca": "maple4k", "maplehd-ca": "maplehd", "iptvmapletv.com": "iptvmapletv", "iptvmojo.com": "iptvmojo", "mojo4ktv.com": "mojo4ktv", "buyiptvnorway.com": "buyiptvnorway", "norgesiptv.com": "norgesiptv", "flimmerkanal.de": "flimmerkanal", "iptvv.de": "iptvvde", "mojo4k.de": "mojo4kde", "streamdeutschland.de": "streamdeutschland", "mojo4k.fr": "mojo4kfr", "streambleu-fr": "streambleu"};
const TIMES = ["00:59:59", "01:00:00", "02:30:00", "04:59:59", "05:00:00", "17:00:00"];
const paused = (t) => t >= "01:00:00" && t < "05:00:00";

// Fake clock: new Date() / Date.now() return the time we set.
const RealDate = Date;
let fakeNow = 0;
class FakeDate extends RealDate {
  constructor(...a) { super(...(a.length ? a : [fakeNow])); }
  static now() { return fakeNow; }
}
globalThis.Date = FakeDate;

// Fake Resend: record every email, never send.
let sent = [];
const realFetch = globalThis.fetch;
globalThis.fetch = async (url, init) => {
  if (String(url).startsWith("https://api.resend.com/")) { sent.push(JSON.parse(init.body)); return new Response('{"id":"fake"}', { status: 200 }); }
  throw new Error("unexpected fetch " + url);
};
const kv = () => { const m = new Map(); return { get: async (k) => m.get(k) ?? null, put: async (k, v) => m.set(k, v), delete: async (k) => m.delete(k), list: async () => ({ keys: [] }) }; };

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "nt-"));
let fail = 0, n = 0;
for (const [repo, domain, plan, pages] of SITES) {
  const file = path.join(dir, `iptv-trial-${WORKER[repo]}.js`);
  const copy = path.join(tmp, repo + ".mjs");
  // Cloudflare returns the live script as multipart form data: keep only the script part.
  let code = fs.readFileSync(file, "utf8");
  if (code.startsWith("--")) {
    const boundary = code.slice(0, code.indexOf("\r\n") >= 0 ? code.indexOf("\r\n") : code.indexOf("\n"));
    const part = code.split(boundary)[1];
    code = part.slice(part.search(/\r?\n\r?\n/)).replace(/^\r?\n\r?\n/, "").replace(/\r?\n$/, "");
  }
  fs.writeFileSync(copy, code);
  const mod = await import(pathToFileURL(copy).href);
  const call = pages
    ? (req, env) => mod.onRequest({ request: req, env })
    : (req, env) => mod.default.fetch(req, env, { waitUntil() {} });
  const manual = repo === "norgesiptv.com";
  const row = [];
  for (const t of TIMES) {
    fakeNow = RealDate.parse(`2026-11-15T${t}Z`);
    sent = [];
    const env = { RESEND_KEY: "fake", RESEND_API_KEY: "fake", TRIALS: kv(), TRIAL_KV: kv() };
    const url = pages ? `https://${domain}/api/invoice` : `https://worker.example/invoice`;
    const res = await call(new Request(url, { method: "POST", headers: { Origin: `https://${domain}`, "Content-Type": "application/json" }, body: JSON.stringify({ name: "Test Client", email: `client${t.replace(/:/g, "")}@example.com`, plan }) }), env);
    const j = await res.json();
    const toClient = sent.filter((e) => [].concat(e.to).includes(`client${t.replace(/:/g, "")}@example.com`));
    const toAdmin = sent.filter((e) => !toClient.includes(e));
    const night = paused(t);
    const expectClient = !manual && !night;
    let ok = res.status === 200 && toAdmin.length === 1 && (toClient.length === (expectClient ? 1 : 0)) && j.invoice === expectClient;
    if (!expectClient) {
      const subj = toAdmin[0]?.subject || "", html = toAdmin[0]?.html || "";
      ok = ok && subj.startsWith(`sale / ${domain} /`) && (manual ? !subj.includes("night pause") && html.includes("always sent by hand")
        : subj.endsWith(" / night pause") && html.includes("paused at night (01:00 to 04:59 UTC)"));
    } else ok = ok && toAdmin[0].subject.startsWith(`invoice / ${domain} /`);
    n++; if (!ok) { fail++; console.log("FAIL", repo, t, res.status, j, sent.map((e) => [e.to, e.subject])); }
    row.push(`${t.slice(0, 5)} ${expectClient ? "invoice" : manual ? "manual" : "paused"}${ok ? "✓" : "✗"}`);
  }
  console.log(repo.padEnd(22), row.join("  "));
}
console.log(`${n - fail}/${n} cases passed`);
process.exit(fail ? 1 : 0);
