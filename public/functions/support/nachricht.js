// Cloudflare Pages Function
// Route: /support/nachricht
//
// Keeps the real WhatsApp number out of this site's HTML source.
// Buttons link here instead of directly to wa.me/<number> or
// api.whatsapp.com/send; this function 302-redirects the visitor
// straight to WhatsApp.
//
// To change the number later, edit WHATSAPP_NUMBER below and push.

const WHATSAPP_NUMBER = '4917600000000'; // digits only, no +, spaces or dashes

export async function onRequestGet(context) {
  const url = new URL(context.request.url);
  const msg = url.searchParams.get('msg');

  const target = msg
    ? `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`
    : `https://wa.me/${WHATSAPP_NUMBER}`;

  return Response.redirect(target, 302);
}
