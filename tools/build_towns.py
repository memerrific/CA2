"""Builds the 'Heating engineer in <town>' pages. Run from the repo root: python3 tools/build_towns.py

Each page should gain real local projects (photo + one line) as they happen;
that is what makes a town page genuinely useful rather than a template.
"""
import json
import sys

sys.path.insert(0, "tools")
from page_template import BASE_URL, page  # noqa: E402
from site_shared import TOWNS  # noqa: E402

LOCAL = {
    "worthing": dict(
        county="West Sussex",
        image="assets/projects/mechanical/mechanical-02.jpg",
        intro="Worthing's homes range from Victorian and Edwardian terraces near the town centre to 1930s semis and the bungalows found across Goring, Durrington and Findon Valley. Each comes with its own heating layout, and many still run on systems designed decades ago.",
        notes=[
            ("Hard water", "Worthing's water is hard, so scale builds up in combi heat exchangers and cylinder coils. We fit scale protection and clean the system as standard."),
            ("Bungalows", "Single-storey homes with long pipe runs suit careful pipe sizing and balanced radiators, and are often good candidates for heat pumps."),
            ("Weak showers", "Older gravity systems are common. An unvented cylinder or a boosted supply can transform upstairs showers."),
        ],
        nearby=["Goring-by-Sea", "Durrington", "Findon Valley", "High Salvington", "Ferring", "Lancing"],
    ),
    "brighton-hove": dict(
        county="East Sussex",
        image="assets/projects/renovations/renovations-01.jpg",
        intro="Brighton &amp; Hove is full of Regency and Victorian houses, many converted into flats, alongside interwar suburbs in Patcham and Hangleton. Space is often tight and access can be awkward, so neat planning matters as much as the equipment.",
        notes=[
            ("Converted flats", "Compact homes often suit a well-specified combi or a slimline cylinder. We check flow and pressure first, as top-floor flats can be limited by the supply."),
            ("Period properties", "Listed buildings and conservation areas may need consent for external equipment such as heat pumps or new flues, so we flag this early."),
            ("Hard water", "Brighton's water is hard. Scale protection and proper system cleaning protect new boilers and cylinders."),
        ],
        nearby=["Hove", "Portslade", "Patcham", "Rottingdean", "Saltdean", "Kemp Town"],
    ),
    "shoreham-by-sea": dict(
        county="West Sussex",
        image="assets/projects/heat-pumps/heat-pumps-01.jpg",
        intro="Shoreham-by-Sea mixes older cottages and terraces near the high street with post-war family homes and newer riverside flats. We carry out heating conversions, cylinder upgrades and complete plumbing for homes and contractors across the town.",
        notes=[
            ("System conversions", "Converting older open-vented systems to sealed systems or mains-pressure hot water is common work here."),
            ("Coastal exposure", "Outdoor equipment near the sea needs corrosion-resistant specification and sensible placement."),
            ("Contractor work", "We work alongside builders on renovations and conversions, coordinating plumbing and heating with the other trades."),
        ],
        nearby=["Lancing", "Southwick", "Sompting", "Steyning", "Upper Beeding"],
    ),
    "littlehampton": dict(
        county="West Sussex",
        image="assets/projects/mechanical/mechanical-04.jpg",
        intro="Littlehampton and its neighbouring villages have a high share of bungalows and post-war homes, with oil-heated properties in the surrounding countryside. Both are well suited to carefully designed heating upgrades.",
        notes=[
            ("Oil heating", "We are OFTEC qualified for oil boiler servicing and replacement in the villages around Littlehampton and Arundel."),
            ("Heat pumps on the coast", "Coastal homes need heat pumps with corrosion protection and placement that keeps salt spray and noise in mind."),
            ("Off-gas grants", "Homes switching from oil can currently get a larger Boiler Upgrade Scheme grant towards a heat pump. We explain how this works."),
        ],
        nearby=["Rustington", "Angmering", "East Preston", "Arundel", "Wick"],
    ),
    "bognor-regis": dict(
        county="West Sussex",
        image="assets/projects/controls/controls-02.jpg",
        intro="Bognor Regis and its neighbouring villages combine seaside bungalows and family homes with oil-heated properties further inland. Many systems are older and have been extended over the years without being redesigned.",
        notes=[
            ("Rebalancing older systems", "Extended systems often have cold radiators. A proper balance, or self-balancing valves, can fix this without replacing the boiler."),
            ("Oil boilers", "OFTEC-qualified servicing, fault finding and replacement for oil-heated homes."),
            ("Low-temperature upgrades", "Bungalows with good loft space are often straightforward to prepare for a heat pump."),
        ],
        nearby=["Felpham", "Middleton-on-Sea", "Aldwick", "Pagham", "Barnham"],
    ),
    "chichester": dict(
        county="West Sussex",
        image="assets/projects/mechanical/mechanical-07.jpg",
        intro="Chichester's historic centre sits within a wide rural district, from the Manhood Peninsula to the South Downs. Many village homes are off the gas grid and heated by oil, and period properties need care with every pipe route.",
        notes=[
            ("Off-gas-grid homes", "We service and replace oil boilers, and plan heat-pump conversions for homes ready to move away from oil."),
            ("Listed and period buildings", "External equipment and new pipe routes in listed buildings or conservation areas may need consent, which we account for at survey."),
            ("Larger homes", "Bigger rural properties often benefit from plant-room design: zoning, thermal storage and properly sized pumps."),
        ],
        nearby=["Bosham", "Fishbourne", "Selsey", "East Wittering", "Midhurst"],
    ),
    "horsham": dict(
        county="West Sussex",
        image="assets/projects/mechanical/mechanical-09.jpg",
        intro="Horsham's market-town homes are surrounded by Weald villages, where period cottages and larger detached houses are often heated by oil. Both benefit from heating designed around how the building actually loses heat.",
        notes=[
            ("Oil to heat pump", "We help oil-heated homes plan a heat pump properly, starting with room-by-room heat loss rather than guesswork."),
            ("Underfloor heating", "Extensions and renovations are a good time to fit underfloor heating, designed for screed or timber floors."),
            ("Hot water upgrades", "Unvented cylinders sized for larger households, with the incoming supply measured first."),
        ],
        nearby=["Southwater", "Billingshurst", "Storrington", "Henfield", "Cowfold"],
    ),
    "crawley": dict(
        county="West Sussex",
        image="assets/projects/controls/controls-03.jpg",
        intro="Much of Crawley was built as a post-war new town, so many homes share similar layouts and heating systems that are now due for an upgrade. We also support commercial and light-industrial sites around the town.",
        notes=[
            ("Post-war systems", "Original pipework and undersized radiators are common. A heat-loss survey shows exactly what needs changing and what can stay."),
            ("Controls upgrades", "Weather compensation and zoning can cut running costs on an existing boiler without replacing it."),
            ("Commercial work", "Plant rooms, pumps, cylinders and maintenance for smaller commercial properties."),
        ],
        nearby=["Three Bridges", "Pound Hill", "Ifield", "Copthorne", "Crawley Down"],
    ),
    "eastbourne": dict(
        county="East Sussex",
        image="assets/projects/renovations/renovations-03.jpg",
        intro="Eastbourne's large Victorian and Edwardian houses, many now flats, sit alongside suburbs of bungalows and family homes. We take on heating upgrades, cylinder work and complete renovation plumbing across the town.",
        notes=[
            ("Large period houses", "Tall buildings with long pipe runs need correctly sized pumps and balanced systems to heat every floor evenly."),
            ("Bungalows", "Simple layouts that suit low-temperature heating and future heat pumps."),
            ("Hard water", "Scale protection and water treatment keep new equipment efficient."),
        ],
        nearby=["Willingdon", "Polegate", "Hampden Park", "Pevensey", "Seaford"],
    ),
}

SERVICES = [
    ("Heat pumps &amp; low-temperature heating", "Designed from a room-by-room heat-loss calculation.", "heat-pumps.html"),
    ("Oil boiler servicing &amp; replacement", "OFTEC-qualified service, repair and replacement.", "oil-boilers.html"),
    ("Boiler and cylinder conversions", "Combi, system or unvented, chosen to suit how you use hot water.", "blog-combi-conversion.html"),
    ("Underfloor heating", "Designed for screed or suspended timber floors.", "underfloor-heating.html"),
    ("Water pressure &amp; boosting", "Measured supply, then the right fix.", "water-pressure.html"),
    ("Bathrooms, kitchens &amp; renovations", "First-fix to final connections, coordinated with other trades.", "renovations.html"),
]


def build():
    for slug, name in TOWNS:
        d = LOCAL[slug]
        plain = name.replace("&amp;", "&")
        page_slug = f"heating-engineer-{slug}"
        notes = "".join(f"<article><h3>{t}</h3><p>{p}</p></article>" for t, p in d["notes"])
        services = "".join(f'<a class="town-service" href="{h}"><strong>{t}</strong><span>{p}</span></a>' for t, p, h in SERVICES)
        nearby = ", ".join(d["nearby"])
        schema = json.dumps({
            "@context": "https://schema.org", "@type": "Service",
            "name": f"Heating and plumbing in {plain}",
            "serviceType": "Heating engineer",
            "provider": {"@type": "Plumber", "name": "CA2 Mechanical & Electrical", "telephone": "+447507038346", "url": BASE_URL},
            "areaServed": [{"@type": "City", "name": plain}] + [{"@type": "Place", "name": n} for n in d["nearby"]],
        })
        body = f"""      <section class="page-hero compact-hero town-hero">
        <div class="wrap">
          <div class="eyebrow">{d['county']}</div>
          <h1>Heating engineer in {name}</h1>
          <p>{d['intro']}</p>
          <div class="actions"><a class="btn primary" href="book.html">Start your heating upgrade</a><a class="btn secondary" href="tel:07507038346">Call 07507 038346</a></div>
          <ul class="hero-trust"><li>OFTEC qualified</li><li>Heat Geek trained</li><li>Established 2019</li><li>Reply within one working day</li></ul>
        </div>
      </section>
      <section class="light town-section">
        <div class="wrap">
          <div class="eyebrow">What we do in {name}</div>
          <h2>Heating, hot water and plumbing, designed properly.</h2>
          <div class="town-services">{services}</div>
        </div>
      </section>
      <section class="town-section town-local">
        <div class="wrap town-local-grid">
          <div>
            <div class="eyebrow">Local knowledge</div>
            <h2>What we see in {name} homes.</h2>
            <img src="{d['image']}" alt="Heating and plumbing work by CA2" loading="lazy" decoding="async" />
          </div>
          <div class="town-notes">{notes}</div>
        </div>
      </section>
      <section class="light town-section">
        <div class="wrap town-process">
          <div>
            <div class="eyebrow">How it works</div>
            <h2>From first conversation to handover.</h2>
            <p>We start by understanding the property and how you use it. Where the job calls for it, we measure the water supply and calculate heat loss before recommending equipment. You get a written scope that says what is included, then a tidy installation, commissioning and a clear handover.</p>
            <p>Gas and LPG appliance work is carried out and certified by Gas Safe registered engineers we work with.</p>
          </div>
          <div class="town-areas">
            <h3>Also covering</h3>
            <p>{nearby} and the surrounding area.</p>
            <h3>Useful guides</h3>
            <p><a href="blog-heat-pump-ready.html">Is your system heat-pump ready?</a><br><a href="blog-combi-conversion.html">Converting to a combi</a><br><a href="blog-unvented-conversion.html">Upgrading to an unvented cylinder</a></p>
          </div>
        </div>
      </section>
      <section class="seo-trust-strip"><div class="wrap"><strong>Work in {name}?</strong><span>Send the essentials today. We aim to reply within one working day.</span><a href="book.html">Book a service →</a></div></section>"""
        html = page(slug=page_slug, title=f"Heating Engineer in {name} | CA2 Mechanical &amp; Electrical",
                    description=f"Heating, heat pumps, oil boilers, hot water and plumbing in {plain} and nearby. Designed and installed by CA2. Call 07507 038346.",
                    body=body, crumbs=[("Areas", None), (name, None)], schema=schema, image=d["image"])
        open(f"{page_slug}.html", "w", encoding="utf-8").write(html)
    print(f"built {len(TOWNS)} town pages")


if __name__ == "__main__":
    build()
