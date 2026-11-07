# MOJO4K.DE

Premium IPTV Website für Deutschland — built with Next.js 13 + Tailwind CSS.

## Features
- 🇩🇪 Vollständig auf Deutsch
- 📺 20.000+ Sender Übersicht
- 💰 Preistabelle (Starter / Premium / Jahres-Deal)
- ❓ FAQ Sektion
- 📱 Responsive Design (Mobile + Desktop)
- ⚡ Static Export für Cloudflare Pages

## Tech Stack
- Next.js 13 (Static Export)
- React 18
- Tailwind CSS 3
- TypeScript

## Deploy
Deployed via Cloudflare Pages with:
- Build command: `npx next build`
- Output directory: `out`

## Success screens
After a free-trial request (`/kostenlos-testen-de`) or a plan order (`/1-monat-1-gerat` … `/1-jahr-10-gerate`) a full-screen
checkmark overlay appears. Texts live in `CELEBRATE` in `public/celebrate.js`; after editing, bump `?v=` in the
`<script src="/celebrate.js?v=1">` tags (JS is cached for a year). Preview: `?celebrate=trial` or `?celebrate=order`.
