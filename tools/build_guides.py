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


guide(
    "blog-how-combi-boilers-work",
    "How it works",
    "How a combi boiler works",
    "Inside a combination boiler: how it switches between heating and hot water, why it condenses, and what common faults mean.",
    "A combi does two jobs with one burner: it heats your radiators, and it heats mains water on demand for your taps and shower. Understanding how it switches between the two explains most of how it behaves day to day.",
    "assets/plant-room-detail.jpg",
    "Copper heating pipework installed by CA2",
    """
<h2>Two circuits, one burner</h2>
<p>Inside a combi are two separate water circuits that never mix:</p>
<ul>
<li><strong>The heating circuit:</strong> a sealed loop of water that flows through the boiler and your radiators.</li>
<li><strong>The hot-water circuit:</strong> fresh mains water that passes through the boiler on its way to your tap.</li>
</ul>
<p>A <strong>diverter valve</strong> decides where the boiler's heat goes. Hot water always takes priority, so the heating pauses while a tap is running. You rarely notice, because radiators hold their warmth for a few minutes.</p>

<h2>Heating mode</h2>
<p>When the thermostat calls for heat, the burner lights and warms the water in the main heat exchanger. The pump circulates it round the radiators and back. The heating circuit is sealed and runs at about 1 to 1.5&nbsp;bar when cold. An <strong>expansion vessel</strong> absorbs the water's expansion as it warms, and a <strong>pressure relief valve</strong> lets water out safely if the pressure ever climbs too high, usually at 3&nbsp;bar.</p>

<h2>Hot-water mode</h2>
<p>Open a hot tap and a <strong>flow sensor</strong> detects water moving. The diverter valve switches, and hot water from the heating side passes through a small <strong>plate heat exchanger</strong>. Mains water flows through the other side of the plates and is heated on its way to the tap. Close the tap and the boiler switches back to heating.</p>
<p>This is why there is a short wait for hot water, and why flow is limited by the boiler's size and the mains supply. See <a href="blog-combi-conversion.html">converting to a combi</a> for what that means in practice.</p>

<h2>Why modern boilers condense</h2>
<p>Burning gas produces water vapour. A condensing boiler uses an extra-large heat exchanger to cool its exhaust until that vapour turns back into water, recovering heat that older boilers sent up the flue. It only condenses when the water returning from the radiators is cool, below roughly 55&nbsp;°C. Run the radiators too hot and the boiler stops condensing and loses efficiency. That's why <a href="blog-weather-compensation.html">weather compensation</a> and lower flow temperatures matter even with a gas boiler.</p>
<p>The water it produces drains away through the <strong>condensate pipe</strong>. If that pipe runs outside and freezes in a cold snap, the boiler locks out. Correct sizing and insulation prevent it.</p>

<h2>Modulation</h2>
<p>A modern boiler can turn its burner down, as well as on and off. Combis are often sized for hot water, which needs far more power than heating a home. If the boiler can't turn down far enough, it switches on and off repeatedly on the heating side, which wastes energy and wears parts. Good setup, and choosing a boiler with a wide modulation range, keeps it running steadily.</p>

<h2>What common problems usually mean</h2>
<ul>
<li><strong>Pressure keeps dropping:</strong> a leak somewhere on the system, a failing expansion vessel or a weeping relief valve.</li>
<li><strong>Hot radiators while a tap is running:</strong> often a sticking diverter valve.</li>
<li><strong>Hot water goes hot and cold:</strong> often scale in the plate heat exchanger, common in hard-water areas, or a flow sensor fault.</li>
<li><strong>Locks out in freezing weather:</strong> very often a frozen condensate pipe.</li>
</ul>
<p>Gas appliance work is carried out by Gas Safe registered engineers.</p>""",
    "Questions about your boiler?",
    "We can look at how your system is set up and what would make it run better.",
    "Book a visit",
)

guide(
    "blog-how-heat-pumps-work",
    "How it works",
    "How a heat pump works",
    "How an air source heat pump moves heat from outdoor air into your home, what efficiency (COP) means, and why flow temperature matters so much.",
    "A heat pump doesn't burn anything. It moves heat that is already in the outdoor air into your heating and hot water, using electricity to do the moving. Done well, it delivers around three units of heat or more for every unit of electricity it uses.",
    "assets/projects/controls/controls-01.jpg",
    "Air source heat pump during CA2 controls work",
    """
<h2>The refrigeration cycle, in four steps</h2>
<p>A heat pump works like a fridge in reverse. A refrigerant circulates in a sealed loop and does four things, over and over:</p>
<ol>
<li><strong>Evaporate:</strong> outdoor air is blown across a coil containing very cold refrigerant. Even on a freezing day, the air is warmer than the refrigerant, so it absorbs heat and boils into a gas.</li>
<li><strong>Compress:</strong> the compressor squeezes that gas, which raises its temperature sharply. This is where the electricity goes.</li>
<li><strong>Condense:</strong> the hot gas passes through a heat exchanger and gives its heat to the water in your heating system, turning back into a liquid.</li>
<li><strong>Expand:</strong> an expansion valve drops the pressure, the refrigerant becomes very cold again, and the cycle repeats.</li>
</ol>

<h2>What COP means</h2>
<p>Efficiency is measured as the <strong>coefficient of performance (COP)</strong>: heat out divided by electricity in. A COP of 3 means 3&nbsp;kWh of heat for every 1&nbsp;kWh of electricity. COP changes with the weather and the water temperature, so the figure to look at is the <strong>seasonal</strong> average across a whole year, often called SCOP or SPF.</p>

<h2>Why flow temperature matters most</h2>
<p>The harder a heat pump has to lift the temperature, from outdoor air up to your radiator water, the less efficient it is. Running radiators at 35 to 45&nbsp;°C instead of 60 to 70&nbsp;°C is what makes a heat pump cheap to run. That is why the design work matters more than the brand:</p>
<ul>
<li>A <a href="blog-heat-loss-calculations.html">room-by-room heat-loss calculation</a> shows what each room needs</li>
<li><a href="blog-radiator-sizing.html">Radiators sized</a> to deliver it at a low temperature</li>
<li><a href="blog-pipe-sizing.html">Pipework sized</a> for the larger flow a heat pump needs</li>
<li><a href="blog-weather-compensation.html">Weather compensation</a> so the water is only as warm as the day requires</li>
</ul>

<h2>Things that surprise people</h2>
<ul>
<li><strong>It runs for longer, more gently.</strong> Radiators feel warm rather than hot, and the house stays at a steady temperature. That is normal and efficient.</li>
<li><strong>It defrosts itself.</strong> In cold, damp weather, ice forms on the outdoor coil. The unit briefly reverses to melt it, sometimes with a puff of steam.</li>
<li><strong>Hot water is stored.</strong> A cylinder is heated to around 50&nbsp;°C, with a regular higher-temperature cycle for hygiene.</li>
<li><strong>Placement matters.</strong> The outdoor unit needs free airflow, a sound base and sensible distance from neighbours. Planning rules on siting and noise apply, and we check them at survey.</li>
</ul>

<h2>Refrigerants</h2>
<p>Most current units use R32 or R290 (propane). R290 has a very low environmental impact and can reach higher water temperatures, which helps homes with smaller radiators. Both are sealed in the outdoor unit at the factory on monobloc models, so there is no refrigerant pipework inside your home.</p>
<h2>Common questions</h2>
<h3>Does a heat pump work in winter?</h3>
<p>Yes. Air source heat pumps extract heat from outdoor air well below freezing. Efficiency falls in very cold weather, which the design allows for.</p>
<h3>Is it noisy?</h3>
<p>Modern units are quiet, typically a low hum similar to a fridge or the fans of an air conditioner. Placement and a solid base make the biggest difference.</p>""",
    "Wondering if a heat pump would suit your home?",
    "We start with the heat loss, so the answer is based on your house rather than a guess.",
    "Request a heat pump survey",
)

guide(
    "blog-oil-boiler-service",
    "Oil heating",
    "What happens during an oil boiler service",
    "A step-by-step look at a full oil boiler service: burner strip-down, nozzle and filter replacement, cleaning, combustion testing and the checks on your tank and oil supply.",
    "An oil boiler service is more hands-on than people expect. A proper service means taking the burner apart, cleaning the boiler inside, replacing worn parts and proving it burns cleanly before we leave.",
    "assets/projects/mechanical/mechanical-06.jpg",
    "Heating plant installed by CA2",
    """
<h2>Before the boiler is opened</h2>
<ul>
<li><strong>Visual checks:</strong> the boiler casing, flue terminal, ventilation and any signs of leaks, soot or overheating.</li>
<li><strong>Oil tank:</strong> condition, base, bunding where fitted, contents gauge and any water or sludge in the tank.</li>
<li><strong>Oil supply line:</strong> pipe condition, the remote-acting fire valve and the line filter.</li>
<li><strong>Your feedback:</strong> any noises, smells, lockouts or rising oil use since the last service.</li>
</ul>

<h2>The strip-down</h2>
<ol>
<li><strong>Burner removed:</strong> the burner is taken out so the combustion chamber can be reached.</li>
<li><strong>Nozzle replaced:</strong> the nozzle sprays oil as a fine mist. It wears with use, and a worn nozzle burns poorly and causes soot, so it is replaced every service.</li>
<li><strong>Filters:</strong> the burner filter and the line filter are cleaned or replaced, so dirt doesn't reach the pump and nozzle.</li>
<li><strong>Electrodes:</strong> the ignition electrodes are cleaned, checked and set to the correct gap.</li>
<li><strong>Heat exchanger cleaned:</strong> soot and scale are brushed and vacuumed from the combustion chamber and the baffles are cleaned. A clean heat exchanger transfers heat better and uses less oil.</li>
<li><strong>Seals and gaskets:</strong> checked and replaced where needed so the boiler reassembles airtight.</li>
</ol>

<h2>Proving it works</h2>
<ul>
<li><strong>Pump pressure</strong> set to the manufacturer's figure for the nozzle fitted</li>
<li><strong>Combustion analysis:</strong> a flue gas analyser measures CO₂, carbon monoxide, flue temperature and efficiency, and a smoke test checks for unburnt fuel</li>
<li><strong>Adjustment:</strong> the burner air is tuned until combustion is clean and within the manufacturer's range</li>
<li><strong>Controls and safety:</strong> thermostats, overheat protection and the boiler's lockout function are tested</li>
</ul>
<p>You get a written service record with the readings, which manufacturers and insurers often ask for.</p>

<h2>Signs your boiler needs attention sooner</h2>
<ul>
<li>A smell of oil or fumes</li>
<li>Soot around the flue terminal or black smoke at start-up</li>
<li>Frequent lockouts, or rumbling and banging when the burner lights</li>
<li>Using noticeably more oil than usual</li>
</ul>
<p>If you smell fumes or suspect a leak, switch the boiler off and get it checked before using it again.</p>

<h2>How long does it take?</h2>
<p>A full service on a typical domestic oil boiler usually takes around one and a half to two hours, longer if parts need replacing or the boiler hasn't been serviced for a while.</p>
<h2>Looking after your tank between services</h2>
<ul>
<li>Check the tank and the ground around it for oil staining or a smell of oil.</li>
<li>Keep vegetation clear of the tank and the supply pipe.</li>
<li>Don't let the tank run very low. The last of the oil can carry water and sludge into the filter.</li>
<li>After a delivery, give the oil time to settle before relying on the boiler if it starts to struggle.</li>
</ul>
<h2>Common questions</h2>
<h3>Is an annual service really necessary?</h3>
<p>Yes. Oil burners slowly soot up and nozzles wear, so efficiency drops and the risk of breakdown rises. Most manufacturer warranties also require it.</p>
<h3>Can you service the tank too?</h3>
<p>We check the tank's condition and its supply line as part of the service, and we'll advise if anything needs repair or replacement.</p>""",
    "Due an oil boiler service?",
    "OFTEC-qualified servicing across Sussex, with a full written record.",
    "Book an oil boiler service",
)

guide(
    "blog-pipe-sizing",
    "Heating design",
    "Pipe sizing: why it matters for heat pumps",
    "Why heat pumps need more water flow than boilers, how pipe size limits the heat a system can carry, and what that means for existing pipework.",
    "Pipework is the part of a heating system nobody sees, and it is often what limits a heat pump. Heat pumps move heat with a lot of water at a small temperature difference, so pipes that were fine for a boiler can be too small.",
    "assets/plant-room-close.jpg",
    "Neatly installed copper pipework and heating equipment",
    """
<h2>Heat is flow times temperature difference</h2>
<p>The heat a pipe carries depends on two things: how much water flows through it, and how much that water cools on its way round. The relationship is simple:</p>
<p class="formula">Heat (kW) = flow (litres per second) × 4.18 × temperature drop (°C)</p>
<p>A boiler system typically runs with a 20&nbsp;°C drop between flow and return. A heat pump is designed for around 5&nbsp;°C. To carry the same heat with a quarter of the temperature drop, a heat pump needs about <strong>four times as much water</strong> moving through the pipes.</p>

<h2>Why you can't just pump harder</h2>
<p>Pushing more water through a small pipe makes it flow faster. Faster water causes noise, wears fittings and needs much more pump pressure, because resistance rises steeply with speed. Designers keep water speed modest, typically below about 1 metre per second in domestic pipework, and size the pipe to suit.</p>

<h2>What a pipe can roughly carry</h2>
<p>As a guide, at a moderate water speed of about 0.7 metres per second in copper:</p>
<table class="guide-table">
<thead><tr><th>Copper pipe</th><th>Approx. heat at 5&nbsp;°C drop (heat pump)</th><th>Approx. heat at 20&nbsp;°C drop (boiler)</th></tr></thead>
<tbody>
<tr><td>15&nbsp;mm</td><td>about 2&nbsp;kW</td><td>about 8&nbsp;kW</td></tr>
<tr><td>22&nbsp;mm</td><td>about 4.5&nbsp;kW</td><td>about 18&nbsp;kW</td></tr>
<tr><td>28&nbsp;mm</td><td>about 8&nbsp;kW</td><td>about 30&nbsp;kW</td></tr>
</tbody>
</table>
<p>These are indicative only. A real design accounts for pipe length, fittings, valves and the pump's available pressure. The point is the scale: a 22&nbsp;mm main that easily fed a whole house from a boiler may only carry enough heat for part of it at heat-pump temperatures.</p>

<h2>What this means for an existing house</h2>
<ul>
<li><strong>Primary pipework</strong> from the heat pump to the cylinder and the main heating circuit is often upsized, commonly to 28&nbsp;mm or larger.</li>
<li><strong>Branches to individual radiators</strong> carry less heat, and 15&nbsp;mm is often fine. The calculation confirms it.</li>
<li><strong>Microbore (8 and 10&nbsp;mm)</strong> can work for small radiators, but long runs to larger radiators often need replacing.</li>
<li><strong>Restrictions</strong> such as old valves, sludge and undersized fittings matter more when flow is higher. Cleaning and the right valves count.</li>
</ul>

<h2>How we size a system</h2>
<p>We start from the room-by-room heat loss, work out the flow each radiator needs, then size each section of pipe so the water speed and pressure loss stay within limits. The pump is chosen from the total, and the system is balanced so each radiator gets its share. See <a href="blog-dynamic-trvs.html">self-balancing radiator valves</a>.</p>
<h2>Common questions</h2>
<h3>Do I have to replace all my pipework for a heat pump?</h3>
<p>Usually not. The main circuits and the heat pump connections are most often upsized; many radiator branches can stay. The design shows exactly which sections need changing.</p>
<h3>Is plastic pipe a problem?</h3>
<p>No, but plastic pipe of the same nominal size has a smaller bore than copper, so it carries a little less. The design uses the actual internal size.</p>""",
    "Planning a heat pump?",
    "We'll check whether your pipework can carry the heat, and size what needs changing.",
    "Request a design survey",
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
