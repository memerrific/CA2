document.querySelector(".menu")?.addEventListener("click", () => {
  const n = document.querySelector(".links");
  n.style.display = n.style.display === "flex" ? "none" : "flex";
  n.style.position = "absolute";
  n.style.top = "66px";
  n.style.left = "0";
  n.style.right = "0";
  n.style.padding = "24px";
  n.style.background = "#091116";
  n.style.flexDirection = "column";
});

const siteOrigin = "https://memerrific.github.io/CA2";
const sitePath = location.pathname.replace(/^\/CA2(?=\/|$)/, "") || "/";
const robotsMeta = document.querySelector('meta[name="robots"]')?.content || "";
if (!robotsMeta.includes("noindex")) {
  if (!document.querySelector('link[rel="canonical"]')) {
    const canonical = document.createElement("link");
    canonical.rel = "canonical";
    canonical.href = `${siteOrigin}${sitePath}`;
    document.head.append(canonical);
  }
  const description = document.querySelector('meta[name="description"]')?.content || "CA2 heating, plumbing and mechanical services across Sussex.";
  const socialMeta = {
    "og:type": "website",
    "og:title": document.title,
    "og:description": description,
    "og:url": `${siteOrigin}${sitePath}`,
    "og:image": `${siteOrigin}/assets/plant-room-wide.jpg`,
    "twitter:card": "summary_large_image",
  };
  Object.entries(socialMeta).forEach(([property, content]) => {
    const selector = property.startsWith("og:") ? `meta[property="${property}"]` : `meta[name="${property}"]`;
    if (document.querySelector(selector)) return;
    const meta = document.createElement("meta");
    meta.setAttribute(property.startsWith("og:") ? "property" : "name", property);
    meta.content = content;
    document.head.append(meta);
  });
}

const primaryLinks = document.querySelector(".links");
if (primaryLinks && !primaryLinks.querySelector(".nav-dropdown")) {
  const simpleServices = [...primaryLinks.children].find(
    (item) => item.tagName === "A" && item.textContent.trim() === "Services",
  );
  if (simpleServices) {
    const dropdown = document.createElement("div");
    dropdown.className = "nav-dropdown";
    dropdown.innerHTML = '<button type="button">Services</button><div class="nav-menu"><a href="systems.html">Mechanical &amp; Electrical</a><a href="plumbing.html">Plumbing &amp; Heating</a><a href="renovations.html">Renovations &amp; Interiors</a></div>';
    simpleServices.replaceWith(dropdown);
  }
}
if (primaryLinks && !primaryLinks.querySelector('a[href="terms.html"]')) {
  const termsLink = document.createElement("a");
  termsLink.href = "terms.html";
  termsLink.textContent = "Terms";
  primaryLinks.append(termsLink);
}

const homepageAbout = document.querySelector(".split#about");
const responseStrip = document.querySelector(".seo-trust-strip");
const homepageFaq = document.querySelector(".faq-preview");
const homepageProcess = document.querySelector(".project-process");
if (homepageAbout && responseStrip && homepageFaq && homepageProcess) {
  homepageAbout.after(homepageFaq);
  homepageFaq.after(responseStrip);
  responseStrip.after(homepageProcess);
}
if (primaryLinks) {
  primaryLinks.querySelectorAll('a[href="index.html#work"]').forEach((link) => {
    link.href = "case-studies.html";
  });
  if (!primaryLinks.querySelector('a[href="blog.html"]')) {
    const guideLink = document.createElement("a");
    guideLink.href = "blog.html";
    guideLink.textContent = "Guides";
    const contactLink = primaryLinks.querySelector('a[href="contact.html"]');
    primaryLinks.insertBefore(guideLink, contactLink || null);
  }
}

const breadcrumbLabels = {
  "systems.html": "Mechanical & Electrical",
  "plumbing.html": "Plumbing & Heating",
  "renovations.html": "Renovations & Interiors",
  "bathrooms-kitchens.html": "Bathrooms & Kitchens",
  "about.html": "About",
  "contact.html": "Contact",
  "book.html": "Book a service",
  "terms.html": "Terms & Conditions",
};
const pageName = location.pathname.split("/").pop() || "index.html";
const pageHero = document.querySelector("main > .page-hero");
if (pageHero && !document.querySelector(".breadcrumb") && breadcrumbLabels[pageName]) {
  pageHero.insertAdjacentHTML("beforebegin", `<nav class="breadcrumb wrap" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>${breadcrumbLabels[pageName]}</span></nav>`);
}

if (!document.querySelector(".footer-services") && !document.querySelector(".status-page")) {
  document.querySelector("main")?.insertAdjacentHTML(
      "afterend",
      `<section class="footer-services" id="contact"><div class="footer-accreditations"><div class="eyebrow">Qualifications & launch direction</div><div class="footer-logos"><div><img src="assets/oftec.png" alt="OFTEC"><span>OFTEC</span></div><div class="mcs-mark">MCS<span>Launch direction</span></div><div><img src="assets/heat-geek.png" alt="Heat Geek"><span>Heat Geek</span></div><div><img src="assets/lcl-awards.png" alt="LCL Awards"><span>LCL Awards</span></div></div></div><div class="footer-service-columns"><div class="footer-service"><div class="eyebrow">Mechanical & electrical</div><h3>Systems</h3><ul><li>System design & specification</li><li>Heat-loss calculations</li><li>Pipe sizing & hydraulics</li><li>Heat pumps & low-temperature systems</li><li>Oil and electric boilers</li><li>Plant rooms, cylinders & thermal storage</li><li>UFH, controls & system wiring</li><li>Ventilation & air conditioning</li></ul></div><div class="footer-service"><div class="eyebrow">Plumbing & heating</div><h3>Installation & support</h3><ul><li>Full heating installations</li><li>Boiler and system conversions</li><li>Unvented hot water</li><li>Water treatment & filtration</li><li>Accumulator tanks & booster sets</li><li>System cleaning</li><li>Fault finding & maintenance</li></ul></div><div class="footer-service"><div class="eyebrow">Renovations & interiors</div><h3>Complete projects</h3><ul><li>Whole-house renovations</li><li>Bespoke bathrooms</li><li>Bespoke kitchens</li><li>Utilities and service routes</li><li>Trade coordination</li></ul></div><div class="footer-service contact-box"><div class="eyebrow">Contact CA2</div><h3>Discuss a project</h3><ul class="contact-list"><li><a href="tel:07507038346">07507 038346</a></li><li><a href="mailto:enquiries@ca2plumbing.com">Email CA2</a></li><li><a href="https://wa.me/447507038346">WhatsApp</a></li><li><span>LinkedIn — link to add</span></li><li>Sussex</li></ul></div></div></section>`,
    );
  document.querySelector("footer.footer")?.remove();
  document.body.insertAdjacentHTML(
    "beforeend",
    `<footer class="footer slim-footer"><div class="footer-bottom"><a class="brand" href="index.html" aria-label="CA2 Mechanical & Electrical Services home"><img class="brand-logo" src="assets/ca2-mechanical-electrical-logo.png" alt="CA2 Mechanical & Electrical Services"></a><p>Heating, plumbing and mechanical systems across Sussex.</p><div class="legal">© CA2 Heating & Plumbing Ltd · Company no. 12029657<br>Registered office: 124 City Road, London City Road, London, England, EC1V 2NX<br><a href="case-studies.html">Projects</a> · <a href="blog.html">Guides</a> · <a href="faq.html">FAQs</a> · <a href="terms.html">Terms</a> · <a href="privacy.html">Privacy</a> · <a href="cookies.html">Cookies</a></div></div></footer>`,
  );
}

if (document.querySelector(".status-page") && !document.querySelector("footer.footer")) {
  document.body.insertAdjacentHTML("beforeend", '<footer class="footer slim-footer"><div class="footer-bottom"><a class="brand" href="index.html" aria-label="CA2 Mechanical & Electrical Services home"><img class="brand-logo" src="assets/ca2-mechanical-electrical-logo.png" alt="CA2 Mechanical & Electrical Services"></a><p>Heating, plumbing and mechanical systems across Sussex.</p><div class="legal">© CA2 Heating & Plumbing Ltd · Company no. 12029657<br>Registered office: 124 City Road, London City Road, London, England, EC1V 2NX<br><a href="terms.html">Terms</a> · <a href="privacy.html">Privacy</a> · <a href="cookies.html">Cookies</a></div></div></footer>');
}

if (!document.querySelector(".mobile-cta")) {
  document.body.insertAdjacentHTML("beforeend", '<a class="mobile-cta" href="book.html">Book a service</a>');
}

document.querySelectorAll(".load-embed").forEach((button) => {
  button.addEventListener("click", () => {
    const container = button.closest(".third-party-embed");
    const frame = container?.querySelector("iframe[data-src]");
    if (!container || !frame) return;
    frame.src = frame.dataset.src;
    container.classList.add("loaded");
    container.querySelector(".embed-placeholder")?.remove();
  });
});

const GA4_MEASUREMENT_ID = "";
const analyticsConsentKey = "ca2_analytics_consent";
window.ca2EnableAnalytics = function () {
  if (!GA4_MEASUREMENT_ID || document.querySelector('script[data-ca2-ga4]')) return;
  const loader = document.createElement("script");
  loader.async = true;
  loader.dataset.ca2Ga4 = "true";
  loader.src = `https://www.googletagmanager.com/gtag/js?id=${GA4_MEASUREMENT_ID}`;
  document.head.append(loader);
  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  window.gtag("js", new Date());
  window.gtag("config", GA4_MEASUREMENT_ID, { anonymize_ip: true });
};

function showCookieChoice() {
  if (!GA4_MEASUREMENT_ID || document.querySelector(".cookie-banner")) return;
  document.body.insertAdjacentHTML("beforeend", '<aside class="cookie-banner" role="dialog" aria-label="Analytics cookie choices"><p>CA2 would like to use optional analytics cookies to understand how the website is used. They stay off unless you accept. <a href="cookies.html">Read the cookie policy</a>.</p><div class="cookie-actions"><button class="btn secondary" type="button" data-cookie-choice="rejected">Reject</button><button class="btn primary" type="button" data-cookie-choice="accepted">Accept</button></div></aside>');
  document.querySelectorAll("[data-cookie-choice]").forEach((button) => button.addEventListener("click", () => {
    const choice = button.dataset.cookieChoice;
    localStorage.setItem(analyticsConsentKey, choice);
    document.querySelector(".cookie-banner")?.remove();
    if (choice === "accepted") window.ca2EnableAnalytics();
  }));
}

if (GA4_MEASUREMENT_ID) {
  const analyticsConsent = localStorage.getItem(analyticsConsentKey);
  if (analyticsConsent === "accepted") window.ca2EnableAnalytics();
  else if (analyticsConsent !== "rejected") showCookieChoice();
}

const contactForm = document.querySelector("#contact-form");
contactForm?.addEventListener("submit", (event) => {
  event.preventDefault();
  if (!contactForm.reportValidity()) return;
  const data = new FormData(contactForm);
  const body = [`Name: ${data.get("name")}`, `Email: ${data.get("email")}`, `Phone: ${data.get("phone") || "Not supplied"}`, `Project: ${data.get("project")}`, "", data.get("message")].join("\n");
  window.location.href = `mailto:enquiries@ca2plumbing.com?subject=${encodeURIComponent("CA2 website enquiry")}&body=${encodeURIComponent(body)}`;
  setTimeout(() => { window.location.href = "thank-you.html"; }, 700);
});

const bookingForm = document.querySelector("#booking-form");
if (bookingForm) {
  let step = 1;
  const labels = [
    "Choose a service",
    "About you",
    "Preferred visit",
    "Your details",
  ];
  const showStep = (next) => {
    step = next;
    document
      .querySelectorAll(".booking-step")
      .forEach((el) =>
        el.classList.toggle("active", Number(el.dataset.step) === step),
      );
    const visibleStep = Math.min(step, 4);
    document.querySelector("#step-number").textContent = visibleStep;
    document.querySelector("#step-label").textContent = labels[visibleStep - 1];
    document
      .querySelectorAll(".step-dots i")
      .forEach((dot, index) =>
        dot.classList.toggle("active", index < visibleStep),
      );
    window.scrollTo({ top: 0, behavior: "smooth" });
  };
  const subchoices = {
    "boiler-service": [
      "Oil boiler service",
      "Gas boiler service",
      "LPG boiler service",
    ],
    "boiler-replacement": [
      "Oil boiler replacement",
      "Gas boiler replacement",
      "LPG boiler replacement",
      "Electric boiler replacement",
    ],
    "renewable-service": [
      "Air-source heat pump service",
      "Ground-source heat pump service",
      "Electric boiler service",
      "Thermal storage system service",
    ],
    "renewable-install": [
      "Air-source heat pump installation",
      "Ground-source heat pump installation",
      "Electric boiler installation",
      "Thermal storage system installation",
    ],
  };
  const mainChoices = document.querySelector(
    '.booking-step[data-step="1"] > .choice-grid',
  );
  const subchoice = document.querySelector("#service-subchoice");
  const subchoiceOptions = document.querySelector("#subchoice-options");
  const chooseService = (value) => {
    document.querySelector("#service-choice").value = value;
    showStep(2);
  };
  document
    .querySelectorAll('.booking-step[data-step="1"] > .choice-grid button')
    .forEach((button) =>
      button.addEventListener("click", () => {
        if (button.dataset.value) {
          chooseService(button.dataset.value);
          return;
        }
        const options = subchoices[button.dataset.group] || [];
        document.querySelector("#subchoice-label").textContent =
          button.textContent.replace("→", "").trim();
        subchoiceOptions.replaceChildren(
          ...options.map((value) => {
            const option = document.createElement("button");
            option.type = "button";
            option.dataset.value = value;
            option.innerHTML = `${value} <b>→</b>`;
            option.addEventListener("click", () => chooseService(value));
            return option;
          }),
        );
        mainChoices.hidden = true;
        subchoice.hidden = false;
      }),
    );
  document
    .querySelector('[data-action="close-subchoice"]')
    ?.addEventListener("click", () => {
      subchoice.hidden = true;
      mainChoices.hidden = false;
    });
  document
    .querySelectorAll("[data-back]")
    .forEach((button) =>
      button.addEventListener("click", () =>
        showStep(Number(button.dataset.back)),
      ),
    );
  document
    .querySelectorAll('.booking-step[data-step="2"] .choice-grid button')
    .forEach((button) =>
      button.addEventListener("click", () => {
        document.querySelector("#customer-choice").value = button.dataset.value;
        showStep(3);
      }),
    );
  const slotGrid = document.querySelector("#slot-grid");
  if (slotGrid) {
    const serviceDays = [];
    const cursor = new Date();
    cursor.setHours(12, 0, 0, 0);
    cursor.setDate(cursor.getDate() + 1);
    while (serviceDays.length < 8) {
      if (cursor.getDay() === 4 || cursor.getDay() === 5) {
        serviceDays.push(new Date(cursor));
      }
      cursor.setDate(cursor.getDate() + 1);
    }
    const dateField = bookingForm.elements.date;
    const timeField = bookingForm.elements.time;
    serviceDays.forEach((date, dayIndex) => {
      const day = document.createElement("article");
      day.className = "slot-day";
      const iso = [date.getFullYear(), String(date.getMonth() + 1).padStart(2, "0"), String(date.getDate()).padStart(2, "0")].join("-");
      day.innerHTML = `<div><span>${date.toLocaleDateString("en-GB", { weekday: "short" })}</span><strong>${date.toLocaleDateString("en-GB", { day: "numeric", month: "short" })}</strong></div><div class="slot-times"></div>`;
      ["8am–10am", "10am–12pm", "12pm–2pm", "2pm–4pm"].forEach((time, timeIndex) => {
        const button = document.createElement("button");
        button.type = "button";
        button.textContent = time;
        button.setAttribute("aria-label", `${date.toLocaleDateString("en-GB", { weekday: "long", day: "numeric", month: "long" })}, ${time}`);
        if ((dayIndex === 1 && timeIndex === 1) || (dayIndex === 4 && timeIndex === 2)) {
          button.disabled = true;
          button.textContent = "Unavailable";
        } else {
          button.addEventListener("click", () => {
            slotGrid.querySelectorAll("button").forEach((item) => item.classList.remove("selected"));
            button.classList.add("selected");
            dateField.value = iso;
            timeField.value = time;
            document.querySelector(".slot-error")?.setAttribute("hidden", "");
          });
        }
        day.querySelector(".slot-times").append(button);
      });
      slotGrid.append(day);
    });
  }
  document.querySelector(".next-step")?.addEventListener("click", () => {
    const date = bookingForm.elements.date;
    if (date.value) showStep(4);
    else document.querySelector(".slot-error")?.removeAttribute("hidden");
  });
  bookingForm.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!bookingForm.reportValidity()) return;
    const data = new FormData(bookingForm);
    const body = [
      `Service: ${data.get("service")}`,
      `Customer type: ${data.get("customer_type")}`,
      `Preferred date: ${data.get("date")}`,
      `Preferred time: ${data.get("time")}`,
      `Name: ${data.get("name")}`,
      `Phone: ${data.get("phone")}`,
      `Email: ${data.get("email")}`,
      `Postcode: ${data.get("postcode")}`,
      `Notes: ${data.get("notes") || "None"}`,
    ].join("\n");
    window.location.href = `mailto:enquiries@ca2plumbing.com?subject=${encodeURIComponent("CA2 service booking request")}&body=${encodeURIComponent(body)}`;
    setTimeout(() => { window.location.href = "thank-you.html"; }, 700);
  });
}
