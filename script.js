document.querySelector(".menu")?.addEventListener("click", () => {
  const n = document.querySelector(".links");
  n.style.display = n.style.display === "flex" ? "none" : "flex";
  n.style.position = "absolute";
  n.style.top = `${document.querySelector(".topbar")?.offsetHeight || 72}px`;
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

const pageName = location.pathname.split("/").pop() || "index.html";

const imageSlotMap = {
  "about.html": {
    selector: ".split > img",
    labels: ["About CA2 1"],
  },
  "systems.html": {
    selector: ".split > img",
    labels: ["Mechanical & Electrical 1"],
  },
  "plumbing.html": {
    selector: ".split > img",
    labels: ["Plumbing & Heating 1"],
  },
  "renovations.html": {
    selector: ".split > img",
    labels: ["Renovations & Interiors 1"],
  },
  "blog-combi-pressure.html": {
    selector: ".guide > img",
    labels: ["Guide: Combi Water Pressure"],
  },
  "blog-heat-pump-ready.html": {
    selector: ".guide > img",
    labels: ["Guide: Heat-Pump Ready"],
  },
  "blog-underfloor-heating.html": {
    selector: ".guide > img",
    labels: ["Guide: Underfloor Heating"],
  },
  "blog-heat-loss-calculations.html": {
    selector: ".guide > img",
    labels: ["Guide: Heat-Loss Calculations"],
  },
  "blog-weather-compensation.html": {
    selector: ".guide > img",
    labels: ["Guide: Weather Compensation"],
  },
  "blog-water-pressure-boosting.html": {
    selector: ".guide > img",
    labels: ["Guide: Water Pressure"],
  },
  "blog-radiator-sizing.html": {
    selector: ".guide > img",
    labels: ["Guide: Radiator Sizing"],
  },
  "blog-combi-or-cylinder.html": {
    selector: ".guide > img",
    labels: ["Guide: Combi or Cylinder"],
  },
  "blog-system-cleaning.html": {
    selector: ".guide > img",
    labels: ["Guide: System Cleaning"],
  },
};

const imageSlotConfig = imageSlotMap[pageName];
if (imageSlotConfig) {
  document.querySelectorAll(imageSlotConfig.selector).forEach((image, index) => {
    if (image.parentElement?.classList.contains("image-slot")) return;
    const slot = document.createElement("span");
    slot.className = "image-slot";
    slot.dataset.imageSlot = imageSlotConfig.labels[index] || `Image ${index + 1}`;
    image.before(slot);
    slot.append(image);
  });
}

const projectGalleries = {
  mechanical: {
    title: "Mechanical systems",
    folder: "mechanical",
    prefix: "mechanical",
    count: 14,
  },
  renovations: {
    title: "House renovations",
    folder: "renovations",
    prefix: "renovations",
    count: 5,
  },
  bathrooms: {
    title: "Bathrooms & kitchens",
    folder: "bathrooms",
    prefix: "bathrooms",
    count: 9,
  },
  "heat-pumps": {
    title: "Heat pumps",
    folder: "heat-pumps",
    prefix: "heat-pumps",
    count: 1,
  },
  controls: {
    title: "Controls & distribution",
    folder: "controls",
    prefix: "controls",
    count: 3,
  },
};

const galleryTriggers = document.querySelectorAll("[data-project-gallery]");
if (galleryTriggers.length) {
  document.body.insertAdjacentHTML(
    "beforeend",
    `<dialog class="project-gallery-dialog" aria-labelledby="project-gallery-title">
      <div class="project-gallery-shell">
        <header><div><span>CA2 project gallery</span><h2 id="project-gallery-title"></h2></div><button class="gallery-close" type="button" aria-label="Close gallery">×</button></header>
        <div class="gallery-stage">
          <button class="gallery-nav gallery-prev" type="button" aria-label="Previous photograph">←</button>
          <img class="gallery-main-image" src="" alt="" />
          <button class="gallery-nav gallery-next" type="button" aria-label="Next photograph">→</button>
        </div>
        <div class="gallery-meta"><span class="gallery-position"></span><span>Use the arrows or select a thumbnail</span></div>
        <div class="gallery-thumbnails" aria-label="Gallery thumbnails"></div>
      </div>
    </dialog>`,
  );

  const dialog = document.querySelector(".project-gallery-dialog");
  const title = dialog.querySelector("#project-gallery-title");
  const mainImage = dialog.querySelector(".gallery-main-image");
  const position = dialog.querySelector(".gallery-position");
  const thumbnails = dialog.querySelector(".gallery-thumbnails");
  const previous = dialog.querySelector(".gallery-prev");
  const next = dialog.querySelector(".gallery-next");
  let activeGallery;
  let activeIndex = 0;

  const galleryImage = (gallery, index) => {
    const number = String(index + 1).padStart(2, "0");
    return `assets/projects/${gallery.folder}/${gallery.prefix}-${number}.jpg`;
  };

  if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    const previewCards = document.querySelectorAll(".card[data-project-gallery], .project-gallery-card[data-project-gallery]");
    const visibleCards = new WeakSet();
    const cardObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) visibleCards.add(entry.target);
        else visibleCards.delete(entry.target);
      });
    }, { rootMargin: "120px" });

    previewCards.forEach((card, cardIndex) => {
      const gallery = projectGalleries[card.dataset.projectGallery];
      const firstImage = card.querySelector(":scope > img");
      if (!gallery || gallery.count < 2 || !firstImage) return;

      const matchedNumber = firstImage.getAttribute("src")?.match(/-(\d{2})\.jpg$/)?.[1];
      let currentIndex = matchedNumber ? Number(matchedNumber) - 1 : 0;
      let currentImage = firstImage;
      let incomingImage = firstImage.cloneNode();
      currentImage.classList.add("project-slide", "project-slide-base", "is-current");
      incomingImage.classList.add("project-slide", "project-slide-overlay");
      incomingImage.setAttribute("aria-hidden", "true");
      card.insertBefore(incomingImage, firstImage.nextSibling);
      cardObserver.observe(card);

      const advancePreview = async () => {
        if (!document.hidden && visibleCards.has(card)) {
          const nextIndex = (currentIndex + 1) % gallery.count;
          incomingImage.src = galleryImage(gallery, nextIndex);
          incomingImage.alt = `${gallery.title} project photograph ${nextIndex + 1}`;
          try { await incomingImage.decode(); } catch (_) {}
          incomingImage.classList.add("is-current");
          currentImage.classList.remove("is-current");
          await new Promise((resolve) => setTimeout(resolve, 1400));
          currentImage.setAttribute("aria-hidden", "true");
          incomingImage.removeAttribute("aria-hidden");
          [currentImage, incomingImage] = [incomingImage, currentImage];
          currentIndex = nextIndex;
        }
        window.setTimeout(advancePreview, 4800);
      };

      window.setTimeout(advancePreview, 4000 + cardIndex * 550);
    });
  }

  const showGalleryImage = (index) => {
    if (!activeGallery) return;
    activeIndex = (index + activeGallery.count) % activeGallery.count;
    mainImage.src = galleryImage(activeGallery, activeIndex);
    mainImage.alt = `${activeGallery.title} project photograph ${activeIndex + 1} of ${activeGallery.count}`;
    position.textContent = `${activeIndex + 1} / ${activeGallery.count}`;
    thumbnails.querySelectorAll("button").forEach((button, buttonIndex) => {
      const isCurrent = buttonIndex === activeIndex;
      button.classList.toggle("is-current", isCurrent);
      button.setAttribute("aria-current", isCurrent ? "true" : "false");
      if (isCurrent) button.scrollIntoView({ block: "nearest", inline: "center" });
    });
  };

  const openGallery = (galleryKey) => {
    activeGallery = projectGalleries[galleryKey];
    if (!activeGallery) return;
    title.textContent = activeGallery.title;
    thumbnails.innerHTML = Array.from({ length: activeGallery.count }, (_, index) =>
      `<button type="button" aria-label="View photograph ${index + 1}"><img src="${galleryImage(activeGallery, index)}" alt="" loading="lazy" /></button>`,
    ).join("");
    thumbnails.querySelectorAll("button").forEach((button, index) => button.addEventListener("click", () => showGalleryImage(index)));
    previous.hidden = activeGallery.count === 1;
    next.hidden = activeGallery.count === 1;
    showGalleryImage(0);
    dialog.showModal();
  };

  galleryTriggers.forEach((trigger) => {
    trigger.addEventListener("click", (event) => {
      event.preventDefault();
      openGallery(trigger.dataset.projectGallery);
    });
  });
  previous.addEventListener("click", () => showGalleryImage(activeIndex - 1));
  next.addEventListener("click", () => showGalleryImage(activeIndex + 1));
  dialog.querySelector(".gallery-close").addEventListener("click", () => dialog.close());
  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) dialog.close();
  });
  dialog.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft") showGalleryImage(activeIndex - 1);
    if (event.key === "ArrowRight") showGalleryImage(activeIndex + 1);
  });
}

const primaryLinks = document.querySelector(".links");
if (primaryLinks) {
  primaryLinks.innerHTML = `
    <a href="index.html">Home</a>
    <div class="nav-dropdown">
      <button type="button">Services</button>
      <div class="nav-menu">
        <a href="systems.html">Mechanical &amp; Electrical</a>
        <a href="plumbing.html">Plumbing &amp; Heating</a>
        <a href="renovations.html">Renovations &amp; Interiors</a>
      </div>
    </div>
    <a href="case-studies.html">Projects</a>
    <a href="about.html">About</a>
    <a href="blog.html">Guides</a>
    <a href="contact.html">Contact</a>
    <a href="terms.html">Terms</a>`;

  const activePage = {
    "index.html": "index.html",
    "case-studies.html": "case-studies.html",
    "about.html": "about.html",
    "blog.html": "blog.html",
    "contact.html": "contact.html",
    "terms.html": "terms.html",
  }[pageName];
  primaryLinks.querySelectorAll("[aria-current]").forEach((link) => link.removeAttribute("aria-current"));
  if (activePage) primaryLinks.querySelector(`a[href="${activePage}"]`)?.setAttribute("aria-current", "page");
  if (["systems.html", "plumbing.html", "renovations.html", "bathrooms-kitchens.html"].includes(pageName)) {
    primaryLinks.querySelector(".nav-dropdown > button")?.setAttribute("aria-current", "page");
  }
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
const pageHero = document.querySelector("main > .page-hero");
if (pageHero && !document.querySelector(".breadcrumb") && breadcrumbLabels[pageName]) {
  pageHero.insertAdjacentHTML("beforebegin", `<nav class="breadcrumb wrap" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>${breadcrumbLabels[pageName]}</span></nav>`);
}

if (!document.querySelector(".footer-services") && !document.querySelector(".status-page")) {
  document.querySelector("main")?.insertAdjacentHTML(
      "afterend",
      `<section class="footer-services" id="contact"><div class="footer-accreditations"><div class="eyebrow">Qualifications & launch direction</div><div class="footer-logos"><div><img src="assets/oftec.png" alt="OFTEC"><span>OFTEC</span></div><div><img class="logo-knockout" src="assets/mcs-certified.png" alt="MCS certification pathway"><span>Launch direction</span></div><div><img class="logo-knockout" src="assets/heat-geek.png" alt="Heat Geek"><span>Heat Geek</span></div><div><img src="assets/lcl-awards.png" alt="LCL Awards"><span>LCL Awards</span></div></div></div><div class="footer-service-columns"><div class="footer-service"><div class="eyebrow">Mechanical & electrical</div><h3>Systems</h3><ul><li>System design & specification</li><li>Heat-loss calculations</li><li>Pipe sizing & hydraulics</li><li>Heat pumps & low-temperature systems</li><li>Oil and electric boilers</li><li>Plant rooms, cylinders & thermal storage</li><li>UFH, controls & system wiring</li><li>Ventilation & air conditioning</li></ul></div><div class="footer-service"><div class="eyebrow">Plumbing & heating</div><h3>Installation & support</h3><ul><li>Full heating installations</li><li>Boiler and system conversions</li><li>Unvented hot water</li><li>Water treatment & filtration</li><li>Accumulator tanks & booster sets</li><li>System cleaning</li><li>Fault finding & maintenance</li></ul></div><div class="footer-service"><div class="eyebrow">Renovations & interiors</div><h3>Complete projects</h3><ul><li>Whole-house renovations</li><li>Bespoke bathrooms</li><li>Bespoke kitchens</li><li>Utilities and service routes</li><li>Trade coordination</li></ul></div><div class="footer-service contact-box"><div class="eyebrow">Contact CA2</div><h3>Discuss a project</h3><ul class="contact-list"><li><a href="tel:07507038346">07507 038346</a></li><li><a href="mailto:enquiries@ca2plumbing.com">Email CA2</a></li><li><a href="https://wa.me/447507038346">WhatsApp</a></li><li><span>LinkedIn — link to add</span></li><li>Sussex</li></ul></div></div></section>`,
    );
  document.querySelector("footer.footer")?.remove();
  document.body.insertAdjacentHTML(
    "beforeend",
    `<footer class="footer slim-footer"><div class="footer-bottom"><a class="brand" href="index.html" aria-label="CA2 Mechanical & Electrical Services home"><img class="brand-logo" src="assets/ca2-mechanical-electrical-logo.png" alt="CA2 Mechanical & Electrical Services"></a><p>Heating, plumbing and mechanical systems across Sussex.</p><div class="legal">© CA2 Heating & Plumbing Ltd · Company no. 12029657<br><a href="case-studies.html">Projects</a> · <a href="blog.html">Guides</a> · <a href="faq.html">FAQs</a> · <a href="terms.html">Terms</a> · <a href="privacy.html">Privacy</a> · <a href="cookies.html">Cookies</a></div></div></footer>`,
  );
}

if (document.querySelector(".status-page") && !document.querySelector("footer.footer")) {
  document.body.insertAdjacentHTML("beforeend", '<footer class="footer slim-footer"><div class="footer-bottom"><a class="brand" href="index.html" aria-label="CA2 Mechanical & Electrical Services home"><img class="brand-logo" src="assets/ca2-mechanical-electrical-logo.png" alt="CA2 Mechanical & Electrical Services"></a><p>Heating, plumbing and mechanical systems across Sussex.</p><div class="legal">© CA2 Heating & Plumbing Ltd · Company no. 12029657<br><a href="terms.html">Terms</a> · <a href="privacy.html">Privacy</a> · <a href="cookies.html">Cookies</a></div></div></footer>');
}

if (!document.querySelector(".mobile-cta")) {
  document.body.insertAdjacentHTML("beforeend", '<a class="mobile-cta" href="book.html">Book a service</a>');
}

document.querySelectorAll(".process-card").forEach((card) => {
  const setCardState = (isFlipped) => {
    card.classList.toggle("is-flipped", isFlipped);
    card.setAttribute("aria-pressed", String(isFlipped));
  };

  if (window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
    card.addEventListener("pointerenter", () => setCardState(true));
  }

  card.addEventListener("click", () => {
    setCardState(!card.classList.contains("is-flipped"));
  });
  card.addEventListener("keydown", (event) => {
    if (event.key !== "Enter" && event.key !== " ") return;
    event.preventDefault();
    setCardState(!card.classList.contains("is-flipped"));
  });
});

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
    const backControl = document.querySelector("#booking-control-back");
    if (backControl) backControl.hidden = step <= 1;
    document.querySelector(".booking-card")?.scrollIntoView({ behavior: "smooth", block: "start" });
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
  document.querySelector("#booking-control-back")?.addEventListener("click", () => {
    if (step > 1) showStep(step - 1);
  });
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
