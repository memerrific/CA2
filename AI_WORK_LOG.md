# CA2 Website — Shared AI Work Log

This is the single canonical hand-over log for everyone working on the CA2 website, including Claude and ChatGPT/Codex. Do not create a separate assistant-specific log.

## Working agreement

Before making any change:

1. Pull or inspect the latest `main` branch.
2. Read this file from the top.
3. Check the latest commit and changed files so newer work is not overwritten.
4. Check whether a page is generated. If it is, edit its source or generator and regenerate it rather than editing generated output alone.

After making any change:

1. Test the affected desktop and mobile layouts.
2. Add a new entry directly below **Latest entries**, with the newest entry first.
3. Use the current Europe/London date and time.
4. Record the author, commit, files changed, what was completed, deployment status, and anything the next person needs to know.
5. Update this log in the same commit where practical, or in an immediate follow-up commit.
6. Never remove another contributor's work without recording the reason.

## Entry template

```text
### YYYY-MM-DD HH:MM Europe/London — Claude or ChatGPT/Codex

- Commit: full SHA or “included in this commit”
- Files changed:
- Completed:
- Generated pages/source:
- Checks performed:
- Deployment:
- Pending / hand-over:
```

## Latest entries

### 2026-10-15 21:51 Europe/London — Claude

- Commit: included in this commit
- Files changed: `book.html`, `thank-you.html`, `script.js`, `styles.css`, `faq.html`, `privacy.html`, `blog.html`, `sitemap.xml`, all pages (footer legal line, asset version), `assets/` (logo and icons resized), `tools/build_services.py` (new), `tools/build_guides.py`, `tools/build_towns.py`, `tools/site_shared.py`, new pages listed below
- Completed:
  - Booking: optional photo upload (up to 6, with previews). Because booking still uses `mailto:`, photos can't be attached; the email notes how many photos there are, and the thank-you page offers a pre-filled WhatsApp button to send them. Revisit when a form service is connected.
  - Thank-you page: personalised for bookings (`?type=booking&name=&photos=`), shows next steps.
  - New service pages: `heat-pumps.html`, `oil-boilers.html`, `underfloor-heating.html`, `water-pressure.html` (with FAQPage schema). Linked from the Services dropdown (`script.js` primaryLinks), footer and town pages.
  - New guides: `blog-how-combi-boilers-work.html`, `blog-how-heat-pumps-work.html`, `blog-oil-boiler-service.html`, `blog-pipe-sizing.html`; listed on `blog.html`.
  - FAQPage schema added to `faq.html`.
  - Footer legal line now includes "Registered in England and Wales" and the registered office address (Companies Act website disclosure).
  - Privacy policy: trading name, LinkedIn, WhatsApp photos and the on-site Instagram copies added; review date updated. Cookie policy checked: still accurate (no non-essential cookies; maps/Tradify are click-to-load).
  - Logo PNG and service icons resized (about 60% smaller). Project JPGs were already well compressed; no change.
- Generated pages/source: service pages from `tools/build_services.py`; guides from `tools/build_guides.py`; towns from `tools/build_towns.py`; `projects.html` from `tools/build_projects.py`; shared header contact and footer from `tools/site_shared.py` (re-run after any footer change). Note: `script.js` also rewrites the main nav links at runtime and injects the services/accreditations block on pages without one.
- Checks performed: internal link check (no missing files); every page loaded on desktop 1440px and mobile 390px with no JS errors or horizontal overflow; booking flow tested end to end with two photos through to the thank-you page.
- Deployment: pushed to `main` (GitHub Pages).
- Pending / hand-over: booking still `mailto:` (form service on hold at Callum's request); mock time slots kept for now; Instagram feed needs `INSTAGRAM_TOKEN` secret (see README); Google review rating to be added once 10+ reviews.

### 2026-10-15 21:45 Europe/London — ChatGPT/Codex

- Commit: included in this commit
- Files changed: `AI_WORK_LOG.md`
- Completed: Created this shared coordination log and established one hand-over process for Claude and ChatGPT/Codex.
- Checks performed: Confirmed that no `AI_WORK_LOG.md` already existed on `main`.
- Deployment: Repository-only documentation; no website deployment required.
- Pending / hand-over: Both assistants must read this file before future website work and add an entry after making changes.

### 2026-10-15 — Current website baseline (recorded by ChatGPT/Codex)

- Baseline commit: `74f740a7280a42924bc17d96b3358aa3051152c1`
- Recorded author of baseline work: Claude
- Completed: Rebranded the site to CA2 Mechanical & Electrical; added header phone and WhatsApp actions; standardised the footer; added the homepage trust strip; removed the MCS logo and described Heat Geek accurately as training; clarified that gas and LPG work is handled by Gas Safe registered partners; added four guides; added nine heating-engineer town pages; added `projects.html` and the homepage Latest Work feed; added the Instagram update workflow with existing project-photo fallbacks; added lazy loading; and updated the sitemap.
- Generated pages/source: Generator scripts are under `tools/`. Treat those scripts as the source of truth for their generated pages. The Instagram workflow is at `.github/workflows/instagram.yml`.
- Pending / hand-over: Review the current live site and repository before changing navigation, generated pages, project imagery, guides, booking, footer, or SEO files. Do not assume an older local checkout is current.

## Notes

- The live site is published from this repository with GitHub Pages.
- Never commit passwords, API keys, access tokens, private calendar credentials, customer information, or form submissions.
- Public business contact details may appear in the website, but secrets must be stored in the appropriate GitHub or hosting secret store.
