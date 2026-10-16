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

### 2026-10-16 21:18 Europe/London — Claude

- Commit: included in this commit
- Files changed: `assets/ca2-mechanical-electrical-logo.png`
- Completed: Restored the full-resolution logo (900×278). On 15 Oct I had shrunk it to 486×150 to save page weight, which made it look soft on high-resolution and scaled screens. Do not downscale the logo below about 3× its displayed height (it displays at up to 70px tall).
- Note: the homepage hero image `assets/plant-room-wide.jpg` is only 1200×900 and is stretched full-width, so it looks soft on wide screens. It has not been changed by Claude. It needs a higher-resolution original (ideally 2400px or more on the long edge) from Callum.
- Deployment: pushed to `main`.

### 2026-10-15 22:13 Europe/London — Claude

- Commit: included in this commit
- Files changed: `index.html`
- Completed: Reverted the homepage section order at Callum's request. It is back to: hero → service icons → About CA2 → FAQs → orange CTA strip → process → Recent projects. Callum wants About near the top, so visitors learn who CA2 is before seeing projects. The order is static HTML; there is no JS reordering. All other sweep changes stay.
- Checks performed: homepage loads with the expected section order and no errors.
- Deployment: pushed to `main`.
- Pending / hand-over: don't move About CA2 below projects.

### 2026-10-15 22:15 Europe/London — Claude

- Commit: included in this commit
- Files changed: `index.html`, `script.js`, `styles.css`, `feed.js`, `case-studies.html`, `systems.html`, `contact.html`, `README.md`, `sitemap.xml`, `data/projects.json` (renamed from `data/instagram.json`), `.github/workflows/instagram.yml`, `tools/site_shared.py`, `tools/fetch_instagram.py`; **removed** `projects.html` and `tools/build_projects.py`; all pages regenerated
- Completed:
  - **One footer.** The services/accreditations block and the bottom bar are now a single static footer from `tools/site_shared.py`. "Renovations & interiors" column replaced by "Areas we cover"; services link to their pages. The script no longer injects a second footer block, and the homepage's static copy was removed.
  - **Homepage order** (now static HTML, the JS reordering was removed): hero → service icons → Recent projects → process → About → FAQs → orange CTA strip.
  - **Instagram strip removed** from the homepage (Callum: too many photo rows, and projects are to be curated by hand). Recent Projects is manual: `data/projects.json` feeds a hidden-until-populated "Latest jobs" section at the top of `case-studies.html`. `projects.html` deleted; "Projects" in the nav and footer goes to `case-studies.html`. The Instagram workflow is manual-only and writes `data/instagram.json`, which the site does not display.
  - **Layout:** `.wrap` is now full width with a 32px gutter (14px on mobile) everywhere, so page headings line up with the content (Callum prefers left-to-right, not centred).
  - **Fixes:** hidden leftover image placeholder labels ("MECHANICAL & ELECTRICAL 1" etc. from `imageSlotMap`); collapsed the empty grey box on the contact page before the Tradify form loads; replaced "Credentials and launch direction" note on `systems.html` with a plain qualifications line; "Ventilation & future services" card rewritten as "Ventilation & MVHR"; Instagram added to contact page.
- Checks performed: full-page screenshots of 15 pages at 1440px and 390px reviewed; all pages load with no JS errors or horizontal overflow; no broken internal links.
- Deployment: pushed to `main`.
- Pending / hand-over: booking page still says "Prototype only" and "mock calendar" by design until booking is connected (Callum said leave for now).

### 2026-10-15 22:00 Europe/London — Claude

- Commit: included in this commit
- Files changed: `index.html`, `feed.js`, `styles.css`, all pages (asset version bump to 20261015-3)
- Completed: Homepage strip heading changed to "Latest work / Fresh from Instagram." (Callum's wording). Strip now spans the full page width like the other homepage sections, with tiles filling the row. Feed tile captions now cut at a word boundary with an ellipsis, three lines maximum.
- Checks performed: homepage at 1440px and 390px.
- Deployment: pushed to `main`.
- Pending / hand-over: the strip still shows the fallback project photos until the Instagram token is added (see README).

### 2026-10-15 21:56 Europe/London — Claude

- Commit: included in this commit
- Files changed: `privacy.html`
- Completed: Privacy policy now states that enquiry and customer details are kept in CA2's job-management system (CRM) and the legal bases for that; adds a business-transfer clause (records may pass to a new owner if the business is sold, with customers told); sets retention to "normally no longer than 12 months" for enquiries that don't proceed, and "at least six years" for accounting records.
- Generated pages/source: `privacy.html` is hand-written (not generated).
- Checks performed: page loads on desktop and mobile with no errors or overflow.
- Deployment: pushed to `main`.
- Pending / hand-over: Callum to check the ICO self-assessment for the data protection fee, and to delete non-proceeding enquiries from the CRM after about 12 months so practice matches the policy.

### 2026-10-16 Europe/London — Claude

- Commit: included in this commit (branch `work-flow`, not `main`)
- Files changed: `designer/` (new), `AI_WORK_LOG.md`
- Completed: Started CA2 Designer, a browser-based heating design and handover pack app (React + TypeScript + Vite) in `designer/`. Polycam DXF / image floor plan import with room tracing; room-by-room heat loss (BS EN 12831 structure) with U-value library; radiator checks and sizing; UFH design (BS EN 1264-2); pipe sizing, pressure drop and Kv; equipment list; branded, printable handover pack. See `designer/README.md`.
- Checks performed: `npm test` (engine unit tests), `tsc`, production build; every tab driven in Chromium at 1440 px and 390 px with no console errors or horizontal overflow.
- Deployment: none. Lives on the `work-flow` branch only; the website on `main` / GitHub Pages is unchanged.
- Pending / hand-over: Test with a real Polycam DXF export; confirm external design temperatures per postcode; consider a separate repo and hosting for the app.

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
