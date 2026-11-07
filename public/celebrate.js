/* Full-screen success screen after a free-trial request or a plan order.
   Called by the forms: mojoCelebrate("trial", email) or mojoCelebrate("order", email).
   Preview without submitting: add ?celebrate=trial or ?celebrate=order to the URL of the
   trial page (/kostenlos-testen-de) or any plan page (e.g. /1-jahr-1-gerat).
   To change the texts, edit CELEBRATE below and bump ?v= in the <script> tags (JS is cached for a year). */
(function () {
  var CELEBRATE = {
    trial: {
      title: "Ihr Gratis-Test ist unterwegs!",
      lines: [
        "Unser Mojo-Kurier sprintet gerade mit Ihren Zugangsdaten zu <b data-c-email></b>, schneller als ein Bundesliga-Konter in der Nachspielzeit. ⚽",
        "Die E-Mail ist meist in wenigen Minuten da. Schauen Sie bitte in Ihren <b>Posteingang</b> UND in Ihren <b>Spam-Ordner</b>, denn manchmal versteckt sich unsere Mail dort wie die Fernbedienung in der Sofaritze.",
        "Ihre einzige Aufgabe für die nächsten 24 Stunden: Popcorn. 🍿"
      ],
      btn: "Alles klar, zur Startseite"
    },
    order: {
      title: "Geschafft! Bestellung ist drin.",
      lines: [
        "Starke Entscheidung. Ihr Sofa wurde bereits informiert und ist mächtig stolz auf Sie. 🛋️",
        "Ihre Rechnung fliegt gerade zu <b data-c-email></b>. Bitte schauen Sie in Ihren <b>Posteingang</b> UND in Ihren <b>Spam-Ordner</b>, E-Mails spielen nämlich leidenschaftlich gern Verstecken.",
        "Rechnung bezahlen, und schon läuft Ihr Mojo-TV, pünktlicher als jede Deutsche Bahn. 🚆"
      ],
      btn: "Super, zur Startseite"
    }
  };

  var CSS =
    ".celebrating,.celebrating body{overflow:hidden}" +
    ".celebrate{position:fixed;inset:0;z-index:2147483000;display:flex;box-sizing:border-box;overflow-y:auto;overscroll-behavior:contain;-webkit-overflow-scrolling:touch;" +
      "padding:max(16px,env(safe-area-inset-top)) max(16px,env(safe-area-inset-right)) max(16px,env(safe-area-inset-bottom)) max(16px,env(safe-area-inset-left));" +
      "background:radial-gradient(circle at 50% 35%,rgba(34,197,94,.22),transparent 60%),#0d0326;backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);" +
      "animation:cel-in .3s ease both;font-family:-apple-system,'Segoe UI','Helvetica Neue',Arial,sans-serif}" +
    ".celebrate.is-out{animation:cel-out .25s ease forwards}" +
    ".celebrate-box{position:relative;margin:auto;width:min(560px,100%);box-sizing:border-box;text-align:center;padding:clamp(28px,6vw,48px) clamp(18px,5vw,40px);" +
      "background:linear-gradient(180deg,#22095c,#160540);border:1px solid rgba(34,197,94,.45);border-radius:20px;" +
      "box-shadow:0 0 0 1px rgba(34,197,94,.2),0 40px 120px -30px rgba(34,197,94,.45);animation:cel-pop .55s .05s cubic-bezier(.2,.9,.3,1.3) both}" +
    ".celebrate-mark{display:block;width:clamp(130px,38vw,180px);height:auto;margin:0 auto 22px;fill:none;stroke:#4ade80;stroke-linecap:round;stroke-linejoin:round;filter:drop-shadow(0 0 24px rgba(74,222,128,.5))}" +
    ".celebrate-mark circle{stroke-width:6;stroke-dasharray:340;stroke-dashoffset:340;animation:cel-draw .7s .2s ease forwards;fill:rgba(34,197,94,.1)}" +
    ".celebrate-mark path{stroke-width:9;stroke-dasharray:80;stroke-dashoffset:80;animation:cel-draw .45s .8s ease forwards,cel-bounce .5s 1.2s ease;transform-origin:center}" +
    ".celebrate h2{font-size:clamp(28px,6vw,40px);line-height:1.15;margin:0 0 16px;color:#4ade80;font-weight:900}" +
    ".celebrate p{color:rgba(255,255,255,.82);font-size:clamp(16px,2.2vw,18px);line-height:1.55;margin:0 auto 12px;max-width:460px}" +
    ".celebrate p b{color:#fff;word-break:break-word}" +
    ".celebrate-go{display:block;margin:18px auto 0;width:100%;max-width:360px;box-sizing:border-box;padding:15px 20px;border:0;border-radius:12px;cursor:pointer;font:inherit;font-size:17px;font-weight:800;" +
      "color:#1a0a00;background:linear-gradient(135deg,#FFD700,#FFA500);box-shadow:0 8px 28px rgba(255,206,0,.3)}" +
    ".celebrate-go:hover,.celebrate-go:focus-visible{transform:translateY(-1px);box-shadow:0 10px 32px rgba(255,206,0,.45)}" +
    ".celebrate-bits{position:fixed;inset:0;pointer-events:none;overflow:hidden}" +
    ".celebrate-bits i{position:absolute;top:-40px;left:var(--x);width:10px;height:16px;border-radius:3px;font-style:normal;font-size:22px;line-height:1;background:#FFD700;animation:cel-fall var(--t) var(--d) linear infinite}" +
    ".celebrate-bits i:nth-child(4n+1){background:#DD0000}" +
    ".celebrate-bits i:nth-child(4n+2){background:#111}" +
    ".celebrate-bits i:nth-child(4n+3){background:#4ade80}" +
    ".celebrate-bits i.e{width:auto;height:auto;background:none}" +
    "@keyframes cel-in{from{opacity:0}}@keyframes cel-out{to{opacity:0}}" +
    "@keyframes cel-pop{from{opacity:0;transform:scale(.85) translateY(20px)}}" +
    "@keyframes cel-draw{to{stroke-dashoffset:0}}" +
    "@keyframes cel-bounce{50%{transform:scale(1.15)}}" +
    "@keyframes cel-fall{from{transform:translateY(0) rotate(var(--r))}to{transform:translateY(110vh) rotate(calc(var(--r) + 540deg))}}" +
    "@media (max-width:360px){.celebrate h2{font-size:24px}.celebrate p{font-size:15px}.celebrate-mark{width:104px;margin-bottom:16px}}" +
    "@media (max-height:560px){.celebrate-box{padding:20px 24px}.celebrate-mark{width:80px;margin-bottom:10px}.celebrate h2{font-size:24px;margin-bottom:10px}.celebrate p{font-size:15px;margin-bottom:8px}.celebrate-go{margin-top:10px}}" +
    "@media (prefers-reduced-motion:reduce){.celebrate,.celebrate-box{animation:none}.celebrate-bits{display:none}.celebrate-mark circle,.celebrate-mark path{animation:none;stroke-dashoffset:0}}";

  var EMOJI = ["📺", "🍿", "⚽", "🎉"];

  function celebrate(kind, email) {
    var c = CELEBRATE[kind];
    if (!c) return false;
    if (!document.getElementById("celebrate-css")) {
      var st = document.createElement("style");
      st.id = "celebrate-css";
      st.textContent = CSS;
      document.head.appendChild(st);
    }
    var old = document.querySelector(".celebrate");
    if (old) old.parentNode.removeChild(old);
    var el = document.createElement("div");
    el.className = "celebrate";
    el.setAttribute("role", "dialog");
    el.setAttribute("aria-modal", "true");
    el.setAttribute("aria-labelledby", "celebrate-title");
    var bits = "";
    for (var i = 0; i < 28; i++) {
      var emo = i % 3 === 0;
      bits += '<i' + (emo ? ' class="e"' : "") + ' style="--x:' + ((i * 37) % 100) + "%;--d:" + ((i % 7) * 0.35) + "s;--t:" + (3.2 + (i % 5) * 0.5) + "s;--r:" + ((i * 53) % 360) + 'deg">' + (emo ? EMOJI[(i / 3) % EMOJI.length] : "") + "</i>";
    }
    el.innerHTML = '<div class="celebrate-bits" aria-hidden="true">' + bits + "</div>" +
      '<div class="celebrate-box">' +
      '<svg class="celebrate-mark" viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="54"/><path d="M36 62 53 79 86 44"/></svg>' +
      '<h2 id="celebrate-title">' + c.title + "</h2>" +
      c.lines.map(function (l) { return "<p>" + l + "</p>"; }).join("") +
      '<button class="celebrate-go" type="button">' + c.btn + "</button>" +
      "</div>";
    var slots = el.querySelectorAll("[data-c-email]");
    for (var j = 0; j < slots.length; j++) slots[j].textContent = email || "Ihre E-Mail-Adresse";
    var go = el.querySelector(".celebrate-go");
    // No way to close it: the only exit is the button, which goes to the homepage.
    document.addEventListener("keydown", function (e) {
      if (e.key === "Tab") { e.preventDefault(); go.focus(); }
      if (e.key === "Escape") e.preventDefault();
    }, true);
    go.addEventListener("click", function () { location.href = "/"; });
    document.body.appendChild(el);
    document.documentElement.classList.add("celebrating");
    try { go.focus({ preventScroll: true }); } catch (e) { go.focus(); }
    return true;
  }

  window.mojoCelebrate = celebrate;

  var q = null;
  try { q = new URLSearchParams(location.search).get("celebrate"); } catch (e) {}
  if (q) {
    var run = function () { celebrate(q === "order" ? "order" : "trial", "sie@beispiel.de"); };
    if (document.body) run(); else document.addEventListener("DOMContentLoaded", run);
  }
})();
