# abstill.com

Static site for AB Still (6one FZE trading as AB Still). Plain HTML + one stylesheet, no build step, no JavaScript, no third-party requests.

- `index.html`, `about.html`, `contact.html`, `terms.html`, `404.html` — the pages
- `styles.css` — the single stylesheet
- `fonts/` — Ovo (SIL OFL), self-hosted
- `favicon.svg`, `og-image.png` — tab icon and link-preview image
- `_build/` — optional: page bodies + a small script that stamps shared header/footer onto them. Editing the `.html` files directly is fine; the script is only a convenience for changes to the shared chrome.

Deployed on Cloudflare Pages from `main`; every push redeploys.
