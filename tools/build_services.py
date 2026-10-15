"""Builds the dedicated service pages. Run from the repo root: python3 tools/build_services.py"""
import html
import json
import sys

sys.path.insert(0, "tools")
from page_template import BASE_URL, page  # noqa: E402

SERVICES = [
    dict(
        slug="heat-pumps",
        eyebrow="Heat pumps &amp; low-temperature heating",
        title="Heat pumps designed around your home",
        meta_title="Heat Pump Design &amp; Installation in Sussex",
        description="Air source heat pumps and low-temperature heating in Sussex, designed from a room-by-room heat-loss calculation with correctly sized radiators and pipework.",
        lead="A heat pump is only as good as the system it is connected to. We start with a room-by-room heat-loss calculation, then size the heat pump, radiators, pipework and cylinder to match, so the system is comfortable and cheap to run.",
        image="assets/projects/controls/controls-01.jpg",
        image_alt="Air source heat pump during CA2 controls work",
        for_whom=[
            "Homes moving away from oil, LPG or an old gas boiler",
            "Renovations and extensions where the heating is being redesigned",
            "Existing heat-pump systems that run expensively or leave rooms cold",
        ],
        included=[
            "Room-by-room heat-loss calculation",
            "Radiator and underfloor heating sizing at a low flow temperature",
            "Pipe sizing and hydraulic design",
            "Cylinder selection for your hot-water use",
            "Weather compensation and controls set up for efficiency",
            "Commissioning, balancing and a clear handover",
        ],
        approach="We design for the lowest flow temperature the house allows, because every degree lower makes the heat pump more efficient. That usually means checking every radiator, upsizing only where needed, and balancing the system properly. We're Heat Geek trained, and that design-first approach is how we work.",
        note="CA2 is working towards MCS certification. Boiler Upgrade Scheme grants require an MCS-certified installer, so we'll explain at the outset how grant eligibility applies to your project.",
        guides=[("blog-heat-pump-ready.html", "Is your system heat-pump ready?"), ("blog-radiator-sizing.html", "Do radiators need changing for a heat pump?"), ("blog-how-heat-pumps-work.html", "How a heat pump works"), ("blog-dynamic-trvs.html", "Self-balancing radiator valves")],
        faqs=[
            ("Will a heat pump heat my house properly?", "Yes, when the system is designed for it. Most comfort problems come from undersized radiators, poor balancing or high flow temperatures, not from the heat pump itself."),
            ("Do I need to replace all my radiators?", "Rarely. The heat-loss calculation shows which rooms need more output. Often only some radiators need upsizing."),
            ("Do I need a hot water cylinder?", "Usually, yes. Heat pumps heat water into a cylinder rather than on demand, so we size one to suit your household."),
        ],
    ),
    dict(
        slug="oil-boilers",
        eyebrow="Oil boiler servicing &amp; replacement",
        title="Oil boiler servicing, repairs and replacement",
        meta_title="Oil Boiler Service, Repair &amp; Replacement in Sussex",
        description="OFTEC-qualified oil boiler servicing, fault finding and replacement across Sussex, including tanks, controls and planning a future move to a heat pump.",
        lead="Oil heating needs regular care to stay safe and efficient. We service, repair and replace oil boilers across rural Sussex, and give honest advice on whether to repair, replace or plan a move to a heat pump.",
        image="assets/projects/mechanical/mechanical-06.jpg",
        image_alt="Heating plant and pipework installed by CA2",
        for_whom=[
            "Off-gas-grid homes on heating oil",
            "Landlords needing reliable servicing records",
            "Homeowners deciding between a new oil boiler and a heat pump",
        ],
        included=[
            "Full strip-down service: burner, nozzle, filters and heat exchanger cleaned",
            "Combustion analysis and efficiency check",
            "Fault finding and repairs",
            "Boiler replacement and system upgrades",
            "Oil supply line and tank checks",
            "Service records for warranty and insurance",
        ],
        approach="An annual service keeps an oil boiler burning cleanly and catches small faults before they become breakdowns. When a boiler is near the end of its life, we'll set out the real options, including whether your home is suited to a heat pump and what that would involve.",
        note="CA2 is OFTEC qualified for oil-fired equipment.",
        guides=[("blog-oil-boiler-service.html", "What happens during an oil boiler service"), ("blog-heat-pump-ready.html", "Is your system heat-pump ready?"), ("blog-system-cleaning.html", "Does your heating system need cleaning?")],
        faqs=[
            ("How often should an oil boiler be serviced?", "Once a year. Many manufacturers require it to keep the warranty valid, and it keeps combustion clean and efficient."),
            ("What's included in a service?", "Cleaning the burner and heat exchanger, replacing the nozzle and filters, checking controls and safety devices, and testing combustion. See our guide for the full list."),
            ("Should I replace my oil boiler with a heat pump?", "It depends on the house and your plans. We can assess both options so you can compare them."),
        ],
    ),
    dict(
        slug="underfloor-heating",
        eyebrow="Underfloor heating",
        title="Underfloor heating, designed for your floor",
        meta_title="Underfloor Heating Design &amp; Installation in Sussex",
        description="Water underfloor heating for extensions, renovations and new builds in Sussex, designed for screed or timber floors and for boilers or heat pumps.",
        lead="Underfloor heating gives even, comfortable warmth and frees up wall space. It works best when it is designed from the room's heat loss and the floor construction, not laid to a standard pattern.",
        image="assets/projects/mechanical/mechanical-10.jpg",
        image_alt="Heating pipework installed by CA2",
        for_whom=[
            "Extensions and kitchen-diners",
            "Whole-house renovations and new builds",
            "Homes planning a heat pump, where UFH runs at low temperatures",
        ],
        included=[
            "Heat-loss calculation per room",
            "Pipe spacing and loop design to suit the floor finish",
            "Systems for screed, suspended timber and overlay floors",
            "Manifolds, mixing units and pump selection",
            "Zoned controls and thermostats",
            "Pressure testing, filling, balancing and commissioning",
        ],
        approach="The floor construction decides the method. Screed floors hold heat and respond slowly; timber floors need spreader plates and respond faster. We design loop lengths and spacing for each room, and set the flow temperature to suit the floor finish and the heat source.",
        note=None,
        guides=[("blog-underfloor-heating.html", "UFH in screed and timber floors"), ("blog-heat-loss-calculations.html", "Why room-by-room heat loss matters"), ("blog-weather-compensation.html", "Weather compensation explained")],
        faqs=[
            ("Can underfloor heating go upstairs?", "Yes. Timber floors use spreader plates or routed boards, designed for the joist layout and floor finish."),
            ("Will it work with my boiler?", "Yes, usually with a mixing unit to lower the water temperature. It also pairs very well with a heat pump."),
            ("What floor finishes work?", "Tile and stone work best. Engineered wood, vinyl and carpet work too, within the manufacturer's temperature and thermal-resistance limits."),
        ],
    ),
    dict(
        slug="water-pressure",
        eyebrow="Water pressure &amp; boosting",
        title="Water pressure and flow, measured and fixed",
        meta_title="Water Pressure &amp; Flow Improvements in Sussex",
        description="Low water pressure and poor flow diagnosed and fixed in Sussex homes: supply testing, mains upgrades, accumulators, booster sets and unvented cylinders.",
        lead="Weak showers usually come down to one of three things: the incoming supply, the pipework inside the house, or the hot-water system. We measure first, so you pay for the fix that actually works.",
        image="assets/plant-room-close.jpg",
        image_alt="Neatly installed copper pipework and heating equipment",
        for_whom=[
            "Weak showers, especially on upper floors",
            "Pressure that drops when another tap is opened",
            "Homes planning a combi or unvented cylinder",
        ],
        included=[
            "Static and dynamic pressure, and flow rate, measured at the supply",
            "Internal pipework checks for restrictions",
            "Mains supply pipe upgrades",
            "Accumulator tanks and pumped booster sets",
            "Unvented cylinder conversions",
            "Water treatment and filtration",
        ],
        approach="Pressure and flow are different things, and a fix for one doesn't always help the other. Once we have measured the supply, we can tell whether the answer is a new supply pipe, stored water, a pump, or simply removing a restriction.",
        note=None,
        guides=[("blog-water-pressure-boosting.html", "Improving water pressure and flow"), ("blog-unvented-conversion.html", "Upgrading to an unvented cylinder"), ("blog-combi-pressure.html", "Will a combi improve water pressure?")],
        faqs=[
            ("Will a new boiler fix low pressure?", "Not on its own. A boiler can't create more water than the supply provides. The supply has to be measured first."),
            ("Can I fit a pump on the mains?", "Not without the water company's consent. Boosting normally uses a break tank with a pump set, or an accumulator."),
            ("How long does a test take?", "Measuring pressure and flow takes minutes, and it is part of every survey for hot-water work."),
        ],
    ),
]


def build():
    for s in SERVICES:
        li = lambda items: "".join(f"<li>{i}</li>" for i in items)  # noqa: E731
        guides = "".join(f'<a href="{h}">{t} →</a>' for h, t in s["guides"])
        faqs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in s["faqs"])
        note = f'<p class="service-note">{s["note"]}</p>' if s["note"] else ""
        plain = lambda t: html.unescape(t)  # noqa: E731
        schema = json.dumps({
            "@context": "https://schema.org",
            "@graph": [
                {"@type": "Service", "name": plain(s["eyebrow"]), "description": s["description"],
                 "provider": {"@type": "Plumber", "name": "CA2 Mechanical & Electrical", "telephone": "+447507038346", "url": BASE_URL},
                 "areaServed": [{"@type": "AdministrativeArea", "name": "West Sussex"}, {"@type": "AdministrativeArea", "name": "East Sussex"}]},
                {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faqs"]]},
            ],
        })
        body = f"""      <section class="page-hero compact-hero">
        <div class="wrap">
          <div class="eyebrow">{s['eyebrow']}</div>
          <h1>{s['title']}</h1>
          <p>{s['lead']}</p>
          <div class="actions"><a class="btn primary" href="book.html">Start your heating upgrade</a><a class="btn secondary" href="tel:07507038346">Call 07507 038346</a></div>
          <ul class="hero-trust"><li>OFTEC qualified</li><li>Heat Geek trained</li><li>Established 2019</li><li>East &amp; West Sussex</li></ul>
        </div>
      </section>
      <section class="light town-section">
        <div class="wrap service-detail">
          <div>
            <div class="eyebrow">Who it's for</div>
            <ul class="tick-list">{li(s['for_whom'])}</ul>
            <div class="eyebrow">What's included</div>
            <ul class="tick-list">{li(s['included'])}</ul>
          </div>
          <div>
            <img src="{s['image']}" alt="{s['image_alt']}" loading="lazy" decoding="async" />
            <h2>How we approach it</h2>
            <p>{s['approach']}</p>
            {note}
          </div>
        </div>
      </section>
      <section class="town-section">
        <div class="wrap service-extra">
          <div>
            <div class="eyebrow">Common questions</div>
            <h2>Before you book.</h2>
            <div class="faq-list service-faq">{faqs}</div>
          </div>
          <div class="service-guides">
            <h3>Read more</h3>
            {guides}
          </div>
        </div>
      </section>
      <section class="seo-trust-strip"><div class="wrap"><strong>Ready to talk it through?</strong><span>Send the essentials today. We aim to reply within one working day.</span><a href="book.html">Book a service →</a></div></section>"""
        out = page(slug=s["slug"], title=f"{s['meta_title']} | CA2", description=s["description"], body=body,
                   crumbs=[("Services", "systems.html"), (s["eyebrow"], None)], schema=schema, image=s["image"])
        open(f"{s['slug']}.html", "w", encoding="utf-8").write(out)
    print(f"built {len(SERVICES)} service pages")


if __name__ == "__main__":
    build()
