"""Page shell used by the generated guide and town pages."""
from site_shared import ASSET_VERSION, FOOTER, HEADER_CONTACT

BASE_URL = "https://memerrific.github.io/CA2/"


def page(*, slug, title, description, body, crumbs, schema=None, image="assets/plant-room-wide.jpg", scripts=()):
    crumb_html = '<a href="index.html">Home</a>'
    for label, href in crumbs:
        crumb_html += "<span>/</span>" + (f'<a href="{href}">{label}</a>' if href else f"<span>{label}</span>")
    schema_html = f'<script type="application/ld+json">{schema}</script>' if schema else ""
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" /><meta name="robots" content="noindex,nofollow">
    <title>{title}</title>
    <meta name="description" content="{description}" />
    <link rel="canonical" href="{BASE_URL}{slug}.html" />
    <meta property="og:type" content="article" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{description}" />
    <meta property="og:url" content="{BASE_URL}{slug}.html" />
    <meta property="og:image" content="{BASE_URL}{image}" />
    <meta name="twitter:card" content="summary_large_image" />
    {schema_html}
    <link rel="stylesheet" href="styles.css?v={ASSET_VERSION}" />
  </head>
  <body>
    <header class="topbar">
      <nav class="nav wrap">
        <a class="brand" href="index.html" aria-label="CA2 Mechanical &amp; Electrical home"><img class="brand-logo" src="assets/ca2-mechanical-electrical-logo.png" alt="CA2 Mechanical &amp; Electrical" /></a>
        <div class="links"><a href="index.html">Home</a><a href="systems.html">Services</a><a href="case-studies.html">Projects</a><a href="blog.html">Guides</a><a href="about.html">About</a><a href="contact.html">Contact</a></div>
        <button class="menu" aria-label="Open menu">☰</button>
        <div class="nav-actions">{HEADER_CONTACT}<a class="cta" href="book.html">Book a service</a></div>
      </nav>
    </header>
    <main>
      <nav class="breadcrumb wrap" aria-label="Breadcrumb">{crumb_html}</nav>
{body}
    </main>
    {FOOTER}
    <a class="mobile-cta" href="book.html">Book a service</a>
    <script src="script.js?v={ASSET_VERSION}"></script>{"".join(f'<script src="{x}?v={ASSET_VERSION}"></script>' for x in scripts)}
  </body>
</html>
"""
