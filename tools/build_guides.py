"""Builds the long-form explainer guides. Run from the repo root: python3 tools/build_guides.py"""
import json
import sys

sys.path.insert(0, "tools")
from page_template import BASE_URL, page  # noqa: E402

GUIDES = []


def guide(slug, topic, title, description, lead, image, alt, body, cta_title, cta_text, cta_button):
    GUIDES.append(dict(slug=slug, topic=topic, title=title, description=description, lead=lead,
                       image=image, alt=alt, body=body, cta_title=cta_title, cta_text=cta_text,
                       cta_button=cta_button))


guide(
    "blog-combi-conversion",
    "Boiler conversions",
    "Converting to a combi boiler: what to expect",
    "What changes when you switch to a combi boiler: the short wait for hot water, flow rates, showers, loft tanks and what to check before deciding.",
    "A combi heats water as you use it, so there is no cylinder to keep hot and no tanks in the loft. It suits many homes very well. It also behaves differently from the system you have now, and knowing why saves surprises after the work is done.",
    "assets/plant-room-detail.jpg",
    "Copper hot-water and heating pipework installed by CA2",
    """
<h2>"Instant" hot water isn't quite instant</h2>
<p>The most common comment after a conversion is that hot water takes a little longer to arrive than it used to. There are two reasons, and neither means anything is wrong.</p>
<p>First, the boiler has to notice the tap is open, light, and bring its heat exchanger up to temperature. That usually takes a few seconds.</p>
<p>Second, the cold water already sitting in the pipe between the boiler and the tap has to run out before hot water reaches you. Ten metres of 15&nbsp;mm copper holds about 1.5 litres. At a typical kitchen-tap flow of 6 litres a minute, that alone is around 15 seconds. Combis are often fitted in the kitchen, a long way from the bathroom, so the pipe run can be longer than it was from your old cylinder.</p>
<p>Many combis have a <strong>pre-heat</strong> or <strong>comfort</strong> setting that keeps the heat exchanger warm and cuts the wait. It uses a little extra gas, so it is worth switching on only if the delay bothers you. Routing pipework sensibly and insulating it also helps.</p>

<h2>Why the wait is a trade worth making</h2>
<p>A cylinder stores 100 litres or more of hot water all day, and that water slowly loses heat whether you use it or not. The boiler then has to reheat it. A combi only heats water at the moment you draw it, so there is no stored hot water cooling down and nothing to reheat. That is where the running-cost saving comes from.</p>

<h2>How much hot water a combi can deliver</h2>
<p>A combi's hot-water output depends on its size and how much the water has to be heated. A useful rule of thumb:</p>
<p class="formula">Flow (litres per minute) ≈ boiler output (kW) × 14.3 ÷ temperature rise (°C)</p>
<p>A 30&nbsp;kW combi raising water by 35&nbsp;°C gives roughly 12 litres a minute. In winter, the incoming mains is colder, so the same boiler gives a little less hot water at the same temperature. The incoming mains also has to supply that flow. A big boiler on a weak supply will still give a weak shower, which is why we measure the incoming flow and pressure before recommending one.</p>

<h2>One outlet at a time works best</h2>
<p>A combi shares its output between every hot tap that is open. One shower is fine. A shower and a kitchen tap at once usually works, with some drop in flow. Two showers at the same time is where combis struggle. If your household regularly runs two showers together, an unvented cylinder is usually the better choice. See <a href="blog-unvented-conversion.html">upgrading to an unvented cylinder</a>.</p>

<h2>What gets removed, and what needs changing</h2>
<ul>
<li><strong>Hot water cylinder:</strong> removed, usually freeing an airing cupboard.</li>
<li><strong>Loft tanks:</strong> the cold-water storage tank and the small feed-and-expansion tank can both go. That removes the risk of tanks freezing or overflowing.</li>
<li><strong>Shower pumps:</strong> these must not be connected to the mains, so they are removed. Pumped and gravity mixer showers may need a new mains-pressure valve.</li>
<li><strong>Taps and fittings:</strong> older fittings designed for low pressure may need replacing.</li>
<li><strong>Electric showers:</strong> unaffected.</li>
</ul>

<h2>The parts people forget</h2>
<ul>
<li><strong>Gas supply:</strong> a combi needs much more gas than a typical system boiler while hot water is running, and the existing gas pipe is often too small. Gas work is carried out and certified by Gas Safe registered engineers.</li>
<li><strong>Hard water:</strong> much of Sussex has hard water, and scale builds up quickly in a combi's hot-water heat exchanger. A scale reducer on the incoming supply is required in hard-water areas, and it protects your warranty.</li>
<li><strong>System cleaning:</strong> a new boiler on dirty old pipework fails early. The system should be cleaned, filtered and dosed with inhibitor.</li>
<li><strong>Controls:</strong> a combi in England must be fitted with an extra efficiency measure, such as weather compensation or a smart thermostat with automation and optimisation. Weather compensation is the one we recommend. See <a href="blog-weather-compensation.html">heating curves explained</a>.</li>
</ul>

<h2>Think about a heat pump before removing the cylinder</h2>
<p>Heat pumps heat water into a cylinder, not on demand. If a heat pump is likely in the next ten years, removing the cylinder and its cupboard now can make that switch harder and dearer. In that case, an unvented cylinder suitable for a heat pump may be the better long-term choice. See <a href="blog-heat-pump-ready.html">is your system heat-pump ready?</a></p>

<h2>Before you decide, check</h2>
<ul>
<li>How many bathrooms you have, and whether two showers often run at once</li>
<li>Incoming flow rate and dynamic pressure, measured rather than guessed</li>
<li>Where the boiler will go, and how far it is from the bathroom</li>
<li>What type of showers you have and whether they suit mains pressure</li>
<li>Whether the gas supply needs upgrading</li>
<li>Whether a heat pump is likely in your plans</li>
</ul>""",
    "Weighing up a combi?",
    "We measure your supply, explain what will change and give you a quote with no surprises.",
    "Request a survey",
)

guide(
    "blog-unvented-conversion",
    "Hot water",
    "Upgrading from a vented to an unvented cylinder",
    "How an unvented cylinder gives mains-pressure showers, removes loft tanks and shower pumps, and what your water supply needs to make it work.",
    "Most older homes have a vented cylinder fed by a tank in the loft. Replacing it with an unvented cylinder gives strong, balanced showers throughout the house, removes the loft tanks and shower pumps, and keeps the benefit of stored hot water.",
    "assets/projects/heat-pumps/heat-pumps-01.jpg",
    "Cylinder and copper pipework installed by CA2",
    """
<h2>Vented and unvented: the difference</h2>
<p>A <strong>vented</strong> cylinder is fed by gravity from a cold-water tank in the loft. Its pressure depends on how high that tank sits: roughly 0.1&nbsp;bar for every metre. A shower one floor below the loft might get only 0.2 to 0.3&nbsp;bar, which is why so many vented systems have a shower pump.</p>
<p>An <strong>unvented</strong> cylinder is fed directly from the mains and stores hot water at mains pressure. Hot and cold both arrive at similar pressure, so showers are stronger and thermostatic mixers work properly.</p>

<h2>What you gain</h2>
<ul>
<li><strong>Stronger showers on every floor,</strong> including top-floor bathrooms that struggle on gravity.</li>
<li><strong>No shower pumps:</strong> no pump noise, and one less thing to break down and replace.</li>
<li><strong>No loft tanks:</strong> frees loft space and removes the risk of a tank freezing, leaking or overflowing.</li>
<li><strong>Several outlets at once:</strong> stored hot water copes with two showers together far better than a combi.</li>
<li><strong>Long warranties:</strong> many manufacturers offer long cover on the inner vessel, often 25 years for stainless steel. This usually depends on an annual service.</li>
<li><strong>Ready for a heat pump:</strong> a cylinder with a large enough coil works with a boiler now and a heat pump later.</li>
</ul>

<h2>Will it save space?</h2>
<p>It always saves loft space, because the tanks go. In the airing cupboard, an unvented cylinder of the same capacity is often a similar size, and it needs room for an expansion vessel and safety valves. Slimline and horizontal models help in tight spaces. We will tell you honestly what fits.</p>

<h2>Is your water supply good enough?</h2>
<p>This is the deciding question. An unvented cylinder can only deliver what the mains provides. Before recommending one, we measure:</p>
<ul>
<li><strong>Dynamic pressure:</strong> pressure while water is flowing, not just standing pressure.</li>
<li><strong>Flow rate:</strong> litres per minute at the incoming stop tap. A family home generally wants 20 litres a minute or more.</li>
<li><strong>The incoming pipe:</strong> old lead or narrow supply pipes often limit flow and may need replacing.</li>
</ul>
<p>If the supply is weak, an accumulator or a boosted cold-water set can fill the gap. See <a href="blog-water-pressure-boosting.html">improving water pressure and flow</a>.</p>

<h2>Regulations and safety</h2>
<p>An unvented cylinder stores hot water under pressure, so it is controlled by Part G3 of the Building Regulations. It must be installed by someone with an unvented hot water (G3) qualification and notified to building control, either directly or through a competent person scheme. CA2 is G3 qualified. Every installation includes:</p>
<ul>
<li>A temperature and pressure relief valve and an expansion relief valve</li>
<li>An expansion vessel or internal air gap</li>
<li>A tundish and discharge pipework to a safe, visible point outside</li>
<li>A benchmark record and handover, with annual servicing recommended</li>
</ul>

<h2>Other things to check</h2>
<ul>
<li>Cold water to the bathrooms should also come from the mains, so hot and cold pressures match.</li>
<li>Old taps, valves and showers designed for gravity pressure may need replacing.</li>
<li>Pipework sized for gravity may need upsizing to carry the extra flow.</li>
</ul>
<h2>Common questions</h2>
<h3>Is an unvented cylinder better than a combi?</h3>
<p>Neither is better everywhere. A combi suits smaller homes with one bathroom and light simultaneous use. An unvented cylinder suits homes with two or more bathrooms, busy mornings, or plans for a heat pump.</p>
<h3>Does it need servicing?</h3>
<p>Yes. An annual check of the safety valves, expansion vessel charge and controls keeps it safe, and is normally a condition of the manufacturer's warranty.</p>
<h3>How long does the work take?</h3>
<p>A straightforward swap in the same position is typically one to two days, including removing the loft tanks. Upgrading the incoming main or moving the cylinder adds time.</p>""",
    "Thinking about an unvented upgrade?",
    "We measure your incoming supply first, so you know the result before any work begins.",
    "Request a survey",
)

guide(
    "blog-dynamic-trvs",
    "Radiators & controls",
    "Self-balancing radiator valves (dynamic TRVs) explained",
    "How pre-settable and dynamic thermostatic radiator valves balance a heating system automatically, and why they matter for heat pumps and condensing boilers.",
    "If some radiators get hot quickly while others stay lukewarm, the system is unbalanced. Dynamic radiator valves fix this automatically by limiting each radiator to exactly the flow it needs.",
    "assets/projects/renovations/renovations-01.jpg",
    "Traditional column radiator installed as part of a CA2 renovation",
    """
<h2>Why radiators heat unevenly</h2>
<p>Water takes the easiest route. Radiators close to the pump get more than their share, and the furthest ones get the leftovers. The traditional fix is to adjust each radiator's lockshield valve by hand. That is slow and fiddly, and it drifts out again every time other valves open and close during the day.</p>

<h2>Three kinds of radiator valve</h2>
<ul>
<li><strong>Standard TRV:</strong> the head contains a wax or liquid sensor that closes the valve as the room warms up. It controls room temperature, not how much water the radiator receives.</li>
<li><strong>Pre-settable TRV:</strong> the valve body has a dial that caps the maximum flow. Set correctly, each radiator gets its share. The flow still changes, though, when the pressure in the system changes.</li>
<li><strong>Dynamic (pressure-independent) TRV:</strong> as well as a flow setting, the valve has a built-in regulator that holds that flow steady, whatever the rest of the system is doing. This is the self-regulating valve, and it balances the system automatically. The Danfoss Dynamic Valve is a well-known example.</li>
</ul>

<h2>How the setting is worked out</h2>
<p>Each radiator needs a flow that matches the heat it must deliver to its room. That comes from the room-by-room heat loss. The flow is calculated with a simple formula:</p>
<p class="formula">Flow (litres per hour) = heat output (W) ÷ (1.163 × temperature drop across the radiator, °C)</p>
<p>A radiator delivering 1,000&nbsp;W with a 20&nbsp;°C drop, typical of a boiler, needs about 43 litres an hour. With a 5&nbsp;°C drop, typical of a heat pump, it needs about 172 litres an hour. Each valve is set to its radiator's figure, so every room gets the heat it was designed for.</p>
<p>Because the setting is a calculated number, not a guess, the result can be checked. When a system is commissioned, flow and return temperatures at each radiator show whether it is getting its share.</p>

<h2>Why it matters for heat pumps and condensing boilers</h2>
<ul>
<li><strong>Lower return temperatures:</strong> a balanced system returns cooler water, so a condensing boiler actually condenses and runs more efficiently.</li>
<li><strong>Even heat at low temperatures:</strong> heat pumps run at low flow temperatures, so a starved radiator shows up straight away as a cold room.</li>
<li><strong>Lower pump setting:</strong> when no radiator is hogging flow, the pump can often run at a lower setting.</li>
<li><strong>Quieter running:</strong> limiting flow at each valve reduces whistling and rushing noises.</li>
</ul>

<h2>Limits worth knowing</h2>
<ul>
<li>Dynamic valves need a small minimum pump pressure to regulate, so the pump must be set to suit them.</li>
<li>They can't fix undersized pipework or radiators that are simply too small for the room.</li>
<li>Leave the room with the main thermostat without a TRV, or fully open, so the two controls don't fight each other.</li>
</ul>

<h2>When they're worth fitting</h2>
<p>They are worth considering when replacing radiators, during a heat pump installation, when converting to weather compensation, or on any system with persistent cold rooms. Because the settings come from a heat-loss calculation, we fit them as part of a designed system, not as a swap on its own. See <a href="blog-heat-loss-calculations.html">why room-by-room heat loss matters</a>.</p>
<h2>Common questions</h2>
<h3>Can I just swap the TRV heads?</h3>
<p>No. The regulating part is in the valve body, so the body has to be changed. Some existing bodies can take a pre-settable insert, which is checked on survey.</p>
<h3>Do they work with smart radiator heads?</h3>
<p>Many dynamic valve bodies accept common smart and standard heads. Check the thread type before buying heads.</p>""",
    "Cold rooms or uneven radiators?",
    "We'll calculate what each radiator needs and balance the system properly.",
    "Book a heating survey",
)

guide(
    "blog-mvhr",
    "Ventilation",
    "MVHR explained: ventilation, heat recovery and air changes",
    "How mechanical ventilation with heat recovery (MVHR) keeps an airtight home fresh while recovering heat, what air changes per hour means, and how a system is designed.",
    "As homes become better insulated and more airtight, fresh air has to be designed in rather than left to draughts. MVHR supplies fresh air continuously and recovers most of the heat from the stale air it removes.",
    "assets/projects/mechanical/mechanical-05.jpg",
    "Mechanical services installation by CA2",
    """
<h2>Why ventilation matters more than it used to</h2>
<p>A family produces several litres of water vapour a day from breathing, cooking, showers and drying clothes. In a draughty house, that moisture leaks away along with your heat. Seal the house up and it stays inside, causing condensation, mould and stale air. Good ventilation removes moisture and pollutants without throwing away the heat you have paid for.</p>

<h2>How MVHR works</h2>
<p>A central unit, usually in the loft or a cupboard, runs two fans continuously:</p>
<ul>
<li><strong>Extract:</strong> stale, moist air is drawn from the kitchen, bathrooms and utility room.</li>
<li><strong>Supply:</strong> fresh outdoor air is delivered to bedrooms and living rooms.</li>
<li><strong>Heat recovery:</strong> the two airstreams pass each other in a heat exchanger without mixing. Much of the outgoing heat warms the incoming air. Good units recover the large majority of it.</li>
</ul>
<p>A boost setting raises the airflow for cooking and showers. A summer bypass lets cool night air in without heating it.</p>

<h2>Air changes per hour, explained</h2>
<p>Air changes per hour (ACH) is how many times the whole volume of air in a home is replaced in an hour:</p>
<p class="formula">ACH = airflow (m³ per hour) ÷ volume of the home (m³)</p>
<p>A 100&nbsp;m² home with 2.4&nbsp;m ceilings holds 240&nbsp;m³ of air. A ventilation rate of 120&nbsp;m³ an hour (about 33 litres a second) replaces it roughly every two hours, which is 0.5&nbsp;ACH. For comparison, Approved Document F sets the minimum whole-dwelling rate as the higher of a figure based on the number of bedrooms or 0.3 litres a second for every square metre of floor area. For that home, the floor-area figure is 30 litres a second, about 0.45&nbsp;ACH. The design figure comes from the calculation, not a rule of thumb.</p>
<p>Don't confuse this with an <strong>airtightness test</strong> result, which is measured at an artificial 50&nbsp;pascals of pressure. That figure describes how leaky the building is, not how much fresh air it gets.</p>

<h2>What good design looks like</h2>
<ul>
<li><strong>Calculated airflows</strong> for every room, from the ventilation requirement</li>
<li><strong>Ductwork sized for low air speed,</strong> so the system is quiet; undersized ducts are the most common cause of noise</li>
<li><strong>Insulated ducts</strong> in cold spaces, so they don't form condensation</li>
<li><strong>A condensate drain</strong> and frost protection for the unit</li>
<li><strong>Commissioning:</strong> each valve balanced and airflows measured and recorded at handover</li>
</ul>

<h2>When MVHR makes sense</h2>
<p>MVHR works best in airtight homes: new builds, deep retrofits and extensive renovations where ducts can be routed. In a leaky house, much of the air bypasses the heat exchanger, so the recovery benefit drops. For partial upgrades, single-room heat recovery units or continuous extract fans may be a better fit.</p>

<h2>Maintenance</h2>
<p>Filters need cleaning or replacing roughly every six to twelve months, depending on location. Homes near busy roads or the coast may need more frequent changes. The unit and condensate drain should be checked annually. Neglected filters are the main reason systems become noisy and lose efficiency.</p>

<h2>How it links to heating design</h2>
<p>Ventilation is part of a home's heat loss. Recovering that heat reduces the size of the heat pump or boiler needed and lowers running costs. That is why we look at ventilation and heating together. See <a href="blog-heat-loss-calculations.html">why room-by-room heat loss matters</a>.</p>""",
    "Planning a renovation or new build?",
    "We can design ventilation and heating together, so the two work as one system.",
    "Discuss your project",
)


def build():
    for g in GUIDES:
        schema = json.dumps({
            "@context": "https://schema.org", "@type": "Article", "headline": g["title"],
            "description": g["description"], "image": BASE_URL + g["image"],
            "author": {"@type": "Organization", "name": "CA2 Mechanical & Electrical"},
            "publisher": {"@type": "Organization", "name": "CA2 Mechanical & Electrical"},
            "mainEntityOfPage": f"{BASE_URL}{g['slug']}.html",
        })
        body = f"""      <article class="guide">
        <div class="eyebrow">{g['topic']}</div>
        <h1>{g['title']}</h1>
        <p class="guide-lead">{g['lead']}</p>
        <img src="{g['image']}" alt="{g['alt']}" loading="lazy" decoding="async" />
{g['body']}
        <div class="guide-cta"><h2>{g['cta_title']}</h2><p>{g['cta_text']}</p><a class="btn primary" href="book.html">{g['cta_button']}</a><a href="tel:07507038346">Or call 07507 038346</a></div>
      </article>"""
        html = page(slug=g["slug"], title=f"{g['title']} | CA2 Sussex", description=g["description"],
                    body=body, crumbs=[("Guides", "blog.html"), (g["topic"], None)], schema=schema,
                    image=g["image"])
        open(f"{g['slug']}.html", "w", encoding="utf-8").write(html)
    print(f"built {len(GUIDES)} guides")


if __name__ == "__main__":
    build()
