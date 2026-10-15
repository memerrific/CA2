"""Shared header/footer snippets and site-wide fixes for the CA2 static site.

Run from the repo root:  python3 tools/site_shared.py
Safe to run repeatedly: every change checks whether it has already been made.
"""
import glob
import re

PHONE_DISPLAY = "07507 038346"
PHONE_TEL = "07507038346"
WHATSAPP = "https://wa.me/447507038346"
INSTAGRAM = "https://www.instagram.com/ca2plumbing/"
LINKEDIN = "https://www.linkedin.com/in/callum-anscombe-5901591a3/"
ASSET_VERSION = "20261015-3"

ICON_PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
ICON_CHAT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>'
ICON_INSTAGRAM = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><path d="M17.5 6.5h.01"/></svg>'
ICON_LINKEDIN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>'

HEADER_CONTACT = (
    f'<a class="nav-phone" href="tel:{PHONE_TEL}" aria-label="Call CA2 on {PHONE_DISPLAY}">'
    f'{ICON_PHONE}<span>{PHONE_DISPLAY}</span></a>'
    f'<a class="nav-icon nav-whatsapp" href="{WHATSAPP}" aria-label="Message CA2 on WhatsApp">{ICON_CHAT}</a>'
)

TOWNS = [
    ("worthing", "Worthing"),
    ("brighton-hove", "Brighton &amp; Hove"),
    ("shoreham-by-sea", "Shoreham-by-Sea"),
    ("littlehampton", "Littlehampton"),
    ("bognor-regis", "Bognor Regis"),
    ("chichester", "Chichester"),
    ("horsham", "Horsham"),
    ("crawley", "Crawley"),
    ("eastbourne", "Eastbourne"),
]

FOOTER = f"""<footer class="footer site-footer">
      <div class="wrap site-footer-grid">
        <div class="site-footer-brand">
          <a class="brand" href="index.html" aria-label="CA2 Mechanical &amp; Electrical home"><img class="brand-logo" src="assets/ca2-mechanical-electrical-logo.png" alt="CA2 Mechanical &amp; Electrical" loading="lazy" decoding="async" /></a>
          <p>Heating, renewable and mechanical systems designed and installed across Sussex.</p>
          <ul class="site-footer-contact">
            <li><a href="tel:{PHONE_TEL}">{ICON_PHONE}{PHONE_DISPLAY}</a></li>
            <li><a href="mailto:enquiries@ca2plumbing.com">enquiries@ca2plumbing.com</a></li>
            <li><a href="{WHATSAPP}">{ICON_CHAT}WhatsApp</a></li>
          </ul>
          <div class="site-footer-social">
            <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="CA2 on Instagram">{ICON_INSTAGRAM}</a>
            <a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="CA2 on LinkedIn">{ICON_LINKEDIN}</a>
          </div>
        </div>
        <div>
          <h4>Services</h4>
          <ul>
            <li><a href="heat-pumps.html">Heat pumps</a></li>
            <li><a href="oil-boilers.html">Oil boilers</a></li>
            <li><a href="underfloor-heating.html">Underfloor heating</a></li>
            <li><a href="water-pressure.html">Water pressure</a></li>
            <li><a href="systems.html">Mechanical &amp; electrical</a></li>
            <li><a href="plumbing.html">Plumbing &amp; heating</a></li>
            <li><a href="renovations.html">Renovations &amp; bathrooms</a></li>
            <li><a href="projects.html">Recent projects</a></li>
            <li><a href="book.html">Book a service</a></li>
          </ul>
        </div>
        <div>
          <h4>Areas we cover</h4>
          <ul>
{chr(10).join(f'            <li><a href="heating-engineer-{slug}.html">{name}</a></li>' for slug, name in TOWNS)}
          </ul>
        </div>
        <div>
          <h4>Guides</h4>
          <ul>
            <li><a href="blog-combi-conversion.html">Converting to a combi</a></li>
            <li><a href="blog-unvented-conversion.html">Vented to unvented</a></li>
            <li><a href="blog-dynamic-trvs.html">Self-balancing TRVs</a></li>
            <li><a href="blog-how-combi-boilers-work.html">How a combi works</a></li>
            <li><a href="blog-how-heat-pumps-work.html">How a heat pump works</a></li>
            <li><a href="blog-mvhr.html">MVHR explained</a></li>
            <li><a href="blog.html">All guides</a></li>
            <li><a href="faq.html">FAQs</a></li>
          </ul>
        </div>
      </div>
      <div class="wrap site-footer-legal">
        <p>CA2 Mechanical &amp; Electrical is a trading name of CA2 Heating &amp; Plumbing Ltd. Registered in England and Wales, company no. 12029657. Registered office: 124 City Road, London, EC1V 2NX.</p>
        <p><a href="about.html">About</a> · <a href="contact.html">Contact</a> · <a href="terms.html">Terms</a> · <a href="privacy.html">Privacy</a> · <a href="cookies.html">Cookies</a></p>
      </div>
    </footer>"""


def apply(path):
    s = open(path, encoding="utf-8").read()
    o = s

    # Brand name in page titles (the legal company name, with "Ltd", is left alone).
    s = re.sub(r"CA2 Heating (&amp;|&) Plumbing(?! Ltd)", r"CA2 Mechanical \1 Electrical", s)
    s = s.replace("CA2 Mechanical &amp; Electrical Services", "CA2 Mechanical &amp; Electrical")
    s = s.replace("CA2 Mechanical & Electrical Services", "CA2 Mechanical & Electrical")

    # Phone + WhatsApp in the header.
    if 'class="nav-phone"' not in s:
        s = s.replace('<div class="nav-actions">', '<div class="nav-actions">' + HEADER_CONTACT, 1)

    # One consistent footer on every page.
    if "site-footer" not in s:
        if re.search(r"<footer[\s\S]*?</footer>", s):
            s = re.sub(r"<footer[\s\S]*?</footer>", FOOTER, s, count=1)
        else:
            s = s.replace("</main>", "</main>\n    " + FOOTER, 1)
    else:
        s = re.sub(r'<footer class="footer site-footer">[\s\S]*?</footer>', FOOTER, s, count=1)

    # Lazy-load images (the header logo stays eager).
    def lazy(m):
        tag = m.group(0)
        if "loading=" in tag or "brand-logo" in tag and "site-footer" not in tag:
            return tag
        return tag[:4] + ' loading="lazy" decoding="async"' + tag[4:]
    head, sep, body = s.partition("</header>")
    if sep:
        s = head + sep + re.sub(r"<img\b[^>]*>", lazy, body)

    # Cache-bust shared assets.
    s = re.sub(r'(styles\.css|script\.js|feed\.js)\?v=[\w-]+', rf'\1?v={ASSET_VERSION}', s)

    if s != o:
        open(path, "w", encoding="utf-8").write(s)
        return True
    return False


if __name__ == "__main__":
    changed = [p for p in sorted(glob.glob("*.html")) if apply(p)]
    print(f"updated {len(changed)} pages")
