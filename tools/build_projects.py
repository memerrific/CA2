"""Builds projects.html, the on-site Recent Projects feed. Run: python3 tools/build_projects.py"""
import sys

sys.path.insert(0, "tools")
from page_template import page  # noqa: E402
from site_shared import ICON_INSTAGRAM, INSTAGRAM  # noqa: E402

BODY = f"""      <section class="page-hero compact-hero">
        <div class="wrap">
          <div class="eyebrow">Recent projects</div>
          <h1>Work from the last few weeks.</h1>
          <p>Plant rooms, heat pumps, cylinders, underfloor heating and bathroom pipework from jobs across Sussex. Select a project to see every photo.</p>
        </div>
      </section>
      <section class="light feed-section" data-feed-section>
        <div class="wrap">
          <div class="feed-grid" data-feed></div>
          <div class="feed-follow">
            <p>Browse projects by type in our <a href="case-studies.html">project galleries</a>, or follow new work as it happens.</p>
            <a class="feed-follow-link" href="{INSTAGRAM}" target="_blank" rel="noopener">{ICON_INSTAGRAM}Follow CA2</a>
          </div>
        </div>
      </section>"""

open("projects.html", "w", encoding="utf-8").write(page(
    slug="projects",
    title="Recent Projects | CA2 Mechanical &amp; Electrical",
    description="Recent heating, heat pump, plant room and plumbing projects by CA2 across Sussex.",
    body=BODY,
    crumbs=[("Recent projects", None)],
    scripts=("feed.js",),
))
print("built projects.html")
