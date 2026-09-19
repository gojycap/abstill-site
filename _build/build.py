#!/usr/bin/env python3
"""Assembles the abstill.com pages from shared chrome + per-page bodies.
Run from the repo root: python3 _build/build.py
(Only the generated .html files are deployed; this script is a convenience.)"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://abstill.com"
NAME = "AB Still"
FOOTER_COPY = f"© 6one FZE trading as {NAME}. Registered as a general and legal consultancy in the SPC Free Zone, UAE."
NAV = [("what-we-do", "What we do"), ("who-we-are", "Who we are"), ("contact", "Contact"), ("terms", "Terms")]


def head(title, desc, path):
    full = NAME if path == "index.html" else f"{title} — {NAME}"
    url = SITE + ("/" if path == "index.html" else "/" + path.removesuffix(".html"))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{full}</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{url}" />
  <link rel="icon" href="favicon.svg" type="image/svg+xml" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="{NAME}" />
  <meta property="og:title" content="{full}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{SITE}/og-image.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="preload" href="fonts/Ovo-Regular.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="stylesheet" href="styles.css" />
</head>
<body>"""


def header(current):
    cur = ' aria-current="page"'
    links = "\n".join(
        f'      <a href="/{h}"{cur if h == current.removesuffix(".html") else ""}>{t}</a>' for h, t in NAV
    )
    return f"""
  <header>
    <a href="/" class="wordmark">{NAME}</a>
    <nav>
{links}
    </nav>
  </header>
"""


def footer():
    links = "\n".join(f'      <a href="/{h}">{t}</a>' for h, t in NAV)
    return f"""
  <footer>
    <p class="footer-copy">{FOOTER_COPY}</p>
    <nav class="footer-nav">
{links}
    </nav>
  </footer>
</body>
</html>
"""


def page(path, title, desc, body):
    html = head(title, desc, path) + header(path) + body + footer()
    (ROOT / path).write_text(html, encoding="utf-8")
    print("wrote", path)


for src in (ROOT / "_build" / "bodies").glob("*.html"):
    meta, _, body = src.read_text(encoding="utf-8").partition("\n---\n")
    m = dict(line.split(": ", 1) for line in meta.strip().splitlines())
    page(src.name, m["title"], m["description"], body)
