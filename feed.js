// Recent projects: renders the hand-picked posts in data/projects.json on the site itself,
// with a built-in post viewer (no Instagram embeds, nothing opens Instagram).
(() => {
  const grids = document.querySelectorAll("[data-feed]");
  if (!grids.length) return;

  const esc = (text) =>
    String(text ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
  const formatDate = (iso) =>
    iso ? new Date(`${iso}T12:00:00`).toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" }) : "";
  const firstLine = (caption) => {
    const line = (caption || "").split(/\n/)[0].trim();
    if (line.length <= 80) return line;
    return `${line.slice(0, 80).replace(/[\s,.;:-]+\S*$/, "")}…`;
  };

  let posts = [];
  let viewer;
  let current = { post: 0, image: 0 };

  const buildViewer = () => {
    document.body.insertAdjacentHTML(
      "beforeend",
      `<dialog class="feed-viewer" aria-label="Project post">
        <div class="feed-viewer-shell">
          <button class="feed-close" type="button" aria-label="Close">×</button>
          <div class="feed-media">
            <img alt="" />
            <button class="feed-arrow feed-prev" type="button" aria-label="Previous photo">‹</button>
            <button class="feed-arrow feed-next" type="button" aria-label="Next photo">›</button>
            <div class="feed-dots" aria-hidden="true"></div>
          </div>
          <div class="feed-side">
            <div class="feed-author"><img src="assets/ca2-mechanical-electrical-logo.png" alt="" /><div><strong>CA2 Mechanical &amp; Electrical</strong><span>Sussex</span></div></div>
            <div class="feed-caption"></div>
            <time class="feed-date"></time>
            <div class="feed-post-nav">
              <button class="feed-post-prev" type="button">← Previous project</button>
              <button class="feed-post-next" type="button">Next project →</button>
            </div>
            <a class="btn primary feed-cta" href="book.html">Start your heating upgrade</a>
          </div>
        </div>
      </dialog>`,
    );
    viewer = document.querySelector(".feed-viewer");
    viewer.querySelector(".feed-close").addEventListener("click", () => viewer.close());
    viewer.addEventListener("click", (e) => { if (e.target === viewer) viewer.close(); });
    viewer.querySelector(".feed-prev").addEventListener("click", () => showImage(current.image - 1));
    viewer.querySelector(".feed-next").addEventListener("click", () => showImage(current.image + 1));
    viewer.querySelector(".feed-post-prev").addEventListener("click", () => open(current.post - 1));
    viewer.querySelector(".feed-post-next").addEventListener("click", () => open(current.post + 1));
    viewer.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft") showImage(current.image - 1);
      if (e.key === "ArrowRight") showImage(current.image + 1);
    });
    let startX = null;
    const media = viewer.querySelector(".feed-media");
    media.addEventListener("touchstart", (e) => { startX = e.touches[0].clientX; }, { passive: true });
    media.addEventListener("touchend", (e) => {
      if (startX === null) return;
      const dx = e.changedTouches[0].clientX - startX;
      if (Math.abs(dx) > 40) showImage(current.image + (dx < 0 ? 1 : -1));
      startX = null;
    });
    viewer.addEventListener("close", () => {
      if (location.hash.startsWith("#post-")) history.replaceState(null, "", location.pathname + location.search);
    });
  };

  const showImage = (index) => {
    const post = posts[current.post];
    const count = post.images.length;
    current.image = (index + count) % count;
    const img = viewer.querySelector(".feed-media img");
    img.src = post.images[current.image].src;
    img.alt = `${firstLine(post.caption) || "CA2 project"}, photo ${current.image + 1} of ${count}`;
    viewer.querySelector(".feed-dots").innerHTML = count > 1
      ? post.images.map((_, i) => `<i class="${i === current.image ? "on" : ""}"></i>`).join("")
      : "";
    viewer.querySelectorAll(".feed-arrow").forEach((b) => { b.hidden = count < 2; });
  };

  const open = (index) => {
    if (!viewer) buildViewer();
    current.post = (index + posts.length) % posts.length;
    const post = posts[current.post];
    viewer.querySelector(".feed-caption").innerHTML = esc(post.caption).replace(/\n/g, "<br>");
    const date = viewer.querySelector(".feed-date");
    date.textContent = formatDate(post.date);
    date.dateTime = post.date || "";
    viewer.querySelector(".feed-post-nav").hidden = posts.length < 2;
    showImage(0);
    if (!viewer.open) viewer.showModal();
    history.replaceState(null, "", `#post-${post.id}`);
  };

  const tile = (post, index) => {
    const cover = post.images[0];
    const many = post.images.length > 1;
    return `<button class="feed-tile" type="button" data-index="${index}" aria-label="Open project: ${esc(firstLine(post.caption) || "CA2 project")}">
      <img src="${esc(cover.src)}" alt="" loading="lazy" decoding="async" />
      ${many ? `<span class="feed-badge">${post.images.length} photos</span>` : cover.video ? '<span class="feed-badge">Video</span>' : ""}
      <span class="feed-tile-caption">${esc(firstLine(post.caption))}</span>
    </button>`;
  };

  fetch("data/projects.json", { cache: "no-cache" })
    .then((r) => (r.ok ? r.json() : { posts: [] }))
    .then((data) => {
      posts = (data.posts || []).filter((p) => p.images && p.images.length);
      grids.forEach((grid) => {
        const limit = Number(grid.dataset.limit) || posts.length;
        const section = grid.closest("[data-feed-section]");
        if (!posts.length) { if (section) section.hidden = true; return; }
        if (section) section.hidden = false;
        grid.innerHTML = posts.slice(0, limit).map(tile).join("");
        grid.addEventListener("click", (e) => {
          const button = e.target.closest(".feed-tile");
          if (!button) return;
          if (grid.dataset.link) location.href = `${grid.dataset.link}#post-${posts[button.dataset.index].id}`;
          else open(Number(button.dataset.index));
        });
      });
      const match = location.hash.match(/^#post-(.+)$/);
      if (match && !document.querySelector("[data-feed][data-link]")) {
        const index = posts.findIndex((p) => p.id === match[1]);
        if (index >= 0) open(index);
      }
    })
    .catch(() => {
      grids.forEach((grid) => { const s = grid.closest("[data-feed-section]"); if (s) s.hidden = true; });
    });
})();
