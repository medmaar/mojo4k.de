/**
 * Mojo 4K — Kostenlos-Testen Worker
 * Sprache: Deutsch
 * - Erstellt IPTV-Testlinie (USA - All, sub=99)
 * - Sendet Willkommens-E-Mail auf Deutsch
 * - Speichert Test in KV
 * - Cron stündlich: T-4h Erinnerung + T=0 Nachfass-E-Mail
 */

const API_BASE    = "https://activationpanel.ru/api/api.php";
const API_KEY     = "35cf68cc83a3a82e1a0ac5361c7b6105";
const HOST        = "http://terry.thecontentnest.com";
const RESEND_KEY  = "re_QVAqR2F8_A9BDiVRQPjpPoFrt6fNpka2E";
const FROM_EMAIL  = "Mojo 4K <kontakt@mojo4k.de>";
const ADMIN_EMAIL = "kontakt@mojo4k.de";
const SITE_URL    = "https://mojo4k.de";
const PACK_NAME   = "USA - All";
const WA_NUMBER   = "17828026280";

// ── helpers ───────────────────────────────────────────────────────────────────

function jsonRes(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
  });
}

async function apiGet(params) {
  const qs = new URLSearchParams({ ...params, api_key: API_KEY });
  const res = await fetch(`${API_BASE}?${qs}`);
  return { status: res.status, text: await res.text() };
}

async function sendEmail(to, subject, html) {
  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${RESEND_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({ from: FROM_EMAIL, to, subject, html }),
  });
  if (!res.ok) throw new Error(`Resend (${res.status}): ${await res.text()}`);
}

// ── email layout ──────────────────────────────────────────────────────────────

function emailWrap(content) {
  return `<!DOCTYPE html>
<html lang="de">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"></head>
<body style="margin:0;padding:0;background-color:#f2f2f2;font-family:Arial,sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f2f2f2;padding:32px 16px;">
  <tr><td align="center">
    <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"
           style="max-width:600px;background:#ffffff;border-radius:8px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <tr><td style="background-color:#4a4fc0;padding:32px 40px;text-align:center;">
        <h1 style="margin:0;font-family:Arial,sans-serif;font-size:26px;font-weight:bold;color:#ffffff;">Mojo 4K</h1>
        <p style="margin:6px 0 0;font-family:Arial,sans-serif;font-size:13px;color:rgba(255,255,255,0.80);">Premium IPTV Deutschland · 4K Streaming</p>
      </td></tr>
      <tr><td style="padding:36px 40px;">${content}</td></tr>
      <tr><td style="background-color:#f8f8f8;border-top:1px solid #eeeeee;padding:18px 40px;text-align:center;">
        <p style="margin:0;font-family:Arial,sans-serif;font-size:11px;color:#aaaaaa;">
          © 2026 Mojo 4K · <a href="${SITE_URL}" style="color:#a0a4f8;text-decoration:none;">mojo4k.de</a>
        </p>
      </td></tr>
    </table>
  </td></tr>
</table>
</body></html>`;
}

function credBox(username, password, m3uUrl) {
  const server = (() => { try { return new URL(m3uUrl).origin; } catch { return HOST; } })();
  return `
  <p style="margin:0 0 8px;font-family:Arial,sans-serif;font-size:13px;font-weight:bold;color:#333333;">Xtream Codes</p>
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"
         style="background-color:#f8f9ff;border:1px solid #e0e0f0;border-radius:6px;margin-bottom:18px;">
    <tr><td style="padding:18px 22px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr><td style="padding:0 0 11px;border-bottom:1px solid #e8e8f0;">
          <p style="margin:0 0 2px;font-family:Arial,sans-serif;font-size:11px;color:#888888;text-transform:uppercase;">Server</p>
          <p style="margin:0;font-family:Arial,sans-serif;font-size:13px;color:#333333;font-weight:bold;">${server}</p>
        </td></tr>
        <tr><td style="padding:11px 0;border-bottom:1px solid #e8e8f0;">
          <p style="margin:0 0 2px;font-family:Arial,sans-serif;font-size:11px;color:#888888;text-transform:uppercase;">Benutzername</p>
          <p style="margin:0;font-family:Arial,sans-serif;font-size:13px;color:#333333;font-weight:bold;">${username}</p>
        </td></tr>
        <tr><td style="padding:11px 0 0;">
          <p style="margin:0 0 2px;font-family:Arial,sans-serif;font-size:11px;color:#888888;text-transform:uppercase;">Passwort</p>
          <p style="margin:0;font-family:Arial,sans-serif;font-size:13px;color:#333333;font-weight:bold;">${password}</p>
        </td></tr>
      </table>
    </td></tr>
  </table>
  <p style="margin:0 0 8px;font-family:Arial,sans-serif;font-size:13px;font-weight:bold;color:#333333;">M3U-Link</p>
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"
         style="background-color:#f8f9ff;border:1px solid #e0e0f0;border-radius:6px;margin-bottom:28px;">
    <tr><td style="padding:14px 20px;">
      <p style="margin:0;font-family:Arial,sans-serif;font-size:12px;color:#CC0000;word-break:break-all;">${m3uUrl}</p>
    </td></tr>
  </table>`;
}

function ctaButton(text, url) {
  return `
  <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin-bottom:28px;">
    <tr><td style="background:linear-gradient(135deg,#FFD700,#CC0000);border-radius:8px;padding:14px 32px;text-align:center;">
      <a href="${url}" style="font-family:Arial,sans-serif;font-size:15px;font-weight:bold;color:#1a0a00;text-decoration:none;">${text}</a>
    </td></tr>
  </table>`;
}

// ── email templates ───────────────────────────────────────────────────────────

function welcomeEmail(name, username, password, m3uUrl) {
  const vorname = name.split(" ")[0];
  return emailWrap(`
    <p style="margin:0 0 16px;font-family:Arial,sans-serif;font-size:15px;color:#333333;">Hallo ${vorname},</p>
    <p style="margin:0 0 14px;font-family:Arial,sans-serif;font-size:14px;line-height:1.65;color:#555555;">
      Ihr kostenloser Testzugang ist bereit! 🎉
    </p>
    <p style="margin:0 0 14px;font-family:Arial,sans-serif;font-size:14px;line-height:1.65;color:#555555;">
      Wir haben alle Länder und Sprachen freigeschaltet, damit Sie unseren Service vollständig testen können.
    </p>
    <p style="margin:0 0 24px;font-family:Arial,sans-serif;font-size:13px;line-height:1.65;color:#777777;font-style:italic;">
      Hinweis: Machen Sie sich keine Sorgen, wenn die Liste zu lang erscheint – Sie können uns jederzeit bitten, Regionen oder Kategorien auszublenden, die Sie nicht benötigen!
    </p>
    <p style="margin:0 0 18px;font-family:Arial,sans-serif;font-size:14px;line-height:1.65;color:#555555;">
      Hier sind Ihre Zugangsdaten:
    </p>
    ${credBox(username, password, m3uUrl)}
    <p style="margin:0 0 20px;font-family:Arial,sans-serif;font-size:14px;line-height:1.65;color:#555555;">
      Benötigen Sie Hilfe bei der Einrichtung? Antworten Sie auf diese E-Mail oder schreiben Sie uns direkt auf WhatsApp unter <a href="https://wa.me/${WA_NUMBER}" style="color:#CC0000;text-decoration:none;font-weight:bold;">+1 782-802-6280</a>
    </p>
    <p style="margin:0;font-family:Arial,sans-serif;font-size:14px;color:#555555;">Mit freundlichen Grüßen,<br><strong>Das Mojo 4K Team</strong></p>
  `);
}

function reminderEmail(name, username, password, m3uUrl) {
  const vorname = name.split(" ")[0];
  return emailWrap(`
    <p style="margin:0 0 16px;font-family:Arial,sans-serif;font-size:15px;color:#333333;">Hallo ${vorname},</p>
    <p style="margin:0 0 14px;font-family:Arial,sans-serif;font-size:14px;line-height:1.65;color:#555555;">
      Ihr Testzugang <strong>läuft in 4 Stunden ab</strong> ⏳
    </p>
    <p style="margin:0 0 22px;font-family:Arial,sans-serif;font-size:14px;line-height:1.65;color:#555555;">
      Nutzen Sie die verbleibende Zeit und genießen Sie Ihren vollständigen Zugang zu +50.000 Kanälen, Bundesliga, Sky Sport, DAZN und +300.000 Filmen & Serien in 4K.
    </p>
    <p style="margin:0 0 16px;font-family:Arial,sans-serif;font-size:14px;color:#555555;">Ihre aktiven Zugangsdaten:</p>
    ${credBox(username, password, m3uUrl)}
    <p style="margin:0 0 16px;font-family:Arial,sans-serif;font-size:14px;line-height:1.65;color:#555555;">
      Genießen Sie Mojo 4K ohne Unterbrechung – wählen Sie jetzt Ihr Abonnement:
    </p>
    ${ctaButton("Jetzt Abonnement wählen →", SITE_URL + "/preise/")}
    <p style="margin:0 0 20px;font-family:Arial,sans-serif;font-size:14px;line-height:1.65;color:#555555;">
      Fragen? Antworten Sie auf diese E-Mail oder kontaktieren Sie uns auf WhatsApp unter <a href="https://wa.me/${WA_NUMBER}" style="color:#CC0000;text-decoration:none;font-weight:bold;">+1 782-802-6280</a>
    </p>
    <p style="margin:0;font-family:Arial,sans-serif;font-size:14px;color:#555555;">Mit freundlichen Grüßen,<br><strong>Das Mojo 4K Team</strong></p>
  `);
}

function followupEmail(name) {
  const vorname = name.split(" ")[0];
  return emailWrap(`
    <p style="margin:0 0 16px;font-family:Arial,sans-serif;font-size:15px;color:#333333;">Hallo ${vorname},</p>
    <p style="margin:0 0 14px;font-family:Arial,sans-serif;font-size:14px;line-height:1.65;color:#555555;">
      Ihr Mojo 4K Testzugang ist nun <strong>abgelaufen</strong>.
    </p>
    <p style="margin:0 0 22px;font-family:Arial,sans-serif;font-size:14px;line-height:1.65;color:#555555;">
      Wir hoffen, Sie haben die Qualität unseres Services genossen — +50.000 Kanäle, Bundesliga, Sky Sport, DAZN und +300.000 Filme & Serien in 4K, ohne Unterbrechung.
    </p>
    <p style="margin:0 0 16px;font-family:Arial,sans-serif;font-size:14px;line-height:1.65;color:#555555;">
      Streamen Sie weiter mit Mojo 4K – wählen Sie das Paket, das zu Ihnen passt:
    </p>
    ${ctaButton("Mein Abonnement wählen →", SITE_URL + "/preise/")}
    <p style="margin:0 0 20px;font-family:Arial,sans-serif;font-size:14px;line-height:1.65;color:#555555;">
      Haben Sie Fragen? Antworten Sie auf diese E-Mail oder schreiben Sie uns auf WhatsApp unter <a href="https://wa.me/${WA_NUMBER}" style="color:#CC0000;text-decoration:none;font-weight:bold;">+1 782-802-6280</a>
    </p>
    <p style="margin:0;font-family:Arial,sans-serif;font-size:14px;color:#555555;">Mit freundlichen Grüßen,<br><strong>Das Mojo 4K Team</strong></p>
  `);
}

function adminEmail(name, email, country, device, whatsapp, notes, username, password, m3uUrl) {
  return `<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8"></head>
<body style="font-family:Arial,sans-serif;font-size:14px;color:#333;padding:20px;">
  <h2 style="color:#CC0000;margin-top:0;">Neuer Testzugang — Mojo 4K</h2>
  <table cellpadding="6" cellspacing="0" border="0">
    <tr><td style="color:#888;width:120px;">Name</td><td><strong>${name}</strong></td></tr>
    <tr><td style="color:#888;">E-Mail</td><td>${email}</td></tr>
    <tr><td style="color:#888;">Land</td><td>${country||"—"}</td></tr>
    <tr><td style="color:#888;">Gerät</td><td>${device||"—"}</td></tr>
    <tr><td style="color:#888;">WhatsApp</td><td>${whatsapp||"—"}</td></tr>
    <tr><td style="color:#888;">Nachricht</td><td>${notes||"—"}</td></tr>
    <tr><td colspan="2"><hr style="border:none;border-top:1px solid #eee;margin:8px 0;"></td></tr>
    <tr><td style="color:#888;">Benutzername</td><td><strong>${username}</strong></td></tr>
    <tr><td style="color:#888;">Passwort</td><td><strong>${password}</strong></td></tr>
    <tr><td style="color:#888;">M3U</td><td style="word-break:break-all;font-size:12px;">${m3uUrl}</td></tr>
  </table>
</body></html>`;
}

// ── fetch handler ─────────────────────────────────────────────────────────────

async function handleFetch(request, env) {
  if (request.method === "OPTIONS") {
    return new Response(null, { headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    }});
  }

  if (request.method === "GET") {
    const u = new URL(request.url);
    if (u.searchParams.has("debug")) {
      const bq = await apiGet({ action: "bouquet" });
      const ri = await apiGet({ action: "reseller_info" });
      const trials = await env.TRIALS.list();
      return jsonRes({ bouquet: bq.text.slice(0,400), reseller: ri.text.slice(0,200), kv_keys: trials.keys.length });
    }
    return new Response("Mojo 4K Trial Worker — OK", { status: 200 });
  }

  if (request.method !== "POST") return jsonRes({ success: false, error: "POST only" }, 405);

  let body;
  try { body = await request.json(); }
  catch { return jsonRes({ success: false, error: "Ungültiges JSON" }, 400); }

  const { name, email, country, device, whatsapp, notes } = body;
  if (!name || !email) return jsonRes({ success: false, error: "Name und E-Mail erforderlich" }, 400);

  let step = "bouquet";
  try {
    // 1. Paket-ID ermitteln
    const bqRes = await apiGet({ action: "bouquet" });
    let packId = "all";
    if (bqRes.text.trim().startsWith("[") || bqRes.text.trim().startsWith("{")) {
      const arr = JSON.parse(bqRes.text);
      const list = Array.isArray(arr) ? arr : Object.values(arr);
      const pkg = list.find(b => (b.name || "").trim().toLowerCase() === PACK_NAME.toLowerCase());
      if (pkg) packId = pkg.id;
    }

    // 2. Demo-Linie erstellen
    step = "create_demo";
    const crRes = await apiGet({
      action: "new", type: "m3u", sub: "99", pack: packId,
      note: `Trial / mojo4k.de / ${email} | ${whatsapp || ""}`,
    });
    if (!crRes.text.trim().startsWith("[") && !crRes.text.trim().startsWith("{")) {
      throw new Error(`Panel kein JSON: ${crRes.text.slice(0, 200)}`);
    }
    const crData = JSON.parse(crRes.text);
    const item = Array.isArray(crData) ? crData[0] : crData;
    if (!item || String(item.status) !== "true") {
      throw new Error(`Panel: ${item?.message || JSON.stringify(item)}`);
    }

    // 3. Zugangsdaten extrahieren
    step = "extract";
    const rawUrl = item.url || "";
    let username = "", password = "";
    try { const u = new URL(rawUrl); username = u.searchParams.get("username") || ""; password = u.searchParams.get("password") || ""; } catch {}
    const m3uUrl = `${HOST}/get.php?username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}&type=m3u_plus&output=ts`;

    // 4. In KV speichern ZUERST (damit Trial immer gespeichert wird, auch wenn E-Mail fehlschlägt)
    step = "kv_store";
    const expiry = Date.now() + 24 * 60 * 60 * 1000;
    await env.TRIALS.put(
      `trial:${email}`,
      JSON.stringify({ name, email, whatsapp, site: 'mojo4k.de', username, password, m3uUrl, expiry, reminder_sent: false, followup_sent: false, created_at: Date.now() }),
      { expirationTtl: 30 * 24 * 60 * 60 }
    );
    // Zentralen KV-Reader benachrichtigen
    try {
      await fetch('https://iptv-kv-reader.medmaar.workers.dev/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, whatsapp, site: 'mojo4k.de', phone: whatsapp, created_at: Date.now() })
      });
    } catch(_) {}

    // 5. Willkommens-E-Mail
    step = "email_client";
    await sendEmail(email, "Ihr Mojo 4K Testzugang ist bereit – 24h Gratis aktiviert ✓", welcomeEmail(name, username, password, m3uUrl));

    // 6. Admin-Benachrichtigung
    step = "email_admin";
    await sendEmail(ADMIN_EMAIL, `Automation / mojo4k.de / trial / ${name} / ${email}`, adminEmail(name, email, country, device, whatsapp, notes, username, password, m3uUrl));

    return jsonRes({ success: true });

  } catch (err) {
    console.error(`[step=${step}]`, err.message);
    return jsonRes({ success: false, error: `[${step}] ${err.message}` }, 500);
  }
}

// ── cron handler ──────────────────────────────────────────────────────────────

async function handleScheduled(env) {
  const now = Date.now();
  const FOUR_HOURS = 4 * 60 * 60 * 1000;
  const { keys } = await env.TRIALS.list({ prefix: "trial:" });
  console.log(`[cron] ${keys.length} Tests geprüft`);

  for (const { name: key } of keys) {
    let trial;
    try { const raw = await env.TRIALS.get(key); if (!raw) continue; trial = JSON.parse(raw); } catch { continue; }
    const { name, email, username, password, m3uUrl, expiry, reminder_sent, followup_sent } = trial;

    if (!reminder_sent && now >= expiry - FOUR_HOURS && now < expiry) {
      try {
        await sendEmail(email, "⏳ Ihr Mojo 4K Testzugang läuft in 4 Stunden ab", reminderEmail(name, username, password, m3uUrl));
        trial.reminder_sent = true;
        await env.TRIALS.put(key, JSON.stringify(trial), { expirationTtl: 30 * 24 * 60 * 60 });
        console.log(`[cron] Erinnerung → ${email}`);
      } catch (e) { console.error(`[cron] Fehler Erinnerung ${email}:`, e.message); }
    }

    if (!followup_sent && now >= expiry) {
      try {
        await sendEmail(email, "Ihr Mojo 4K Testzugang ist abgelaufen – Jetzt weiterschauen 🎬", followupEmail(name));
        trial.followup_sent = true;
        await env.TRIALS.put(key, JSON.stringify(trial), { expirationTtl: 30 * 24 * 60 * 60 });
        console.log(`[cron] Nachfass → ${email}`);
      } catch (e) { console.error(`[cron] Fehler Nachfass ${email}:`, e.message); }
    }
  }
}

export default {
  async fetch(request, env) { return handleFetch(request, env); },
  async scheduled(event, env, ctx) { ctx.waitUntil(handleScheduled(env)); },
};
