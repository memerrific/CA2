"""Pull recent Instagram posts into the site, so they display natively (no Instagram embed).

Runs daily from .github/workflows/instagram.yml. Needs the INSTAGRAM_TOKEN secret
(a long-lived Instagram API token for the CA2 professional account).

- Downloads each post's photos into assets/instagram/ (resized, re-compressed)
- Writes data/instagram.json, which projects.html and the homepage read
- Refreshes the token (valid 60 days) and prints the new one to $GITHUB_OUTPUT
- Posts whose caption contains #noweb are skipped
"""
import io
import json
import os
import pathlib
import re
import sys
import urllib.parse
import urllib.request

from PIL import Image

API = "https://graph.instagram.com"
FIELDS = "id,caption,media_type,media_url,thumbnail_url,permalink,timestamp,children{media_type,media_url,thumbnail_url}"
MAX_POSTS = 24
MAX_IMAGES_PER_POST = 8
MAX_EDGE = 1400
OUT_DIR = pathlib.Path("assets/instagram")
DATA = pathlib.Path("data/instagram.json")


def get(url, params):
    with urllib.request.urlopen(f"{url}?{urllib.parse.urlencode(params)}", timeout=60) as r:
        return json.load(r)


def save_image(url, dest):
    if dest.exists():
        return
    with urllib.request.urlopen(url, timeout=60) as r:
        img = Image.open(io.BytesIO(r.read())).convert("RGB")
    img.thumbnail((MAX_EDGE, MAX_EDGE))
    img.save(dest, "JPEG", quality=80, optimize=True, progressive=True)


def clean_caption(text):
    text = text or ""
    text = re.sub(r"(?:\s*#\w+)+\s*$", "", text)  # trailing hashtag block
    return text.strip()


def main():
    token = os.environ.get("INSTAGRAM_TOKEN")
    if not token:
        sys.exit("INSTAGRAM_TOKEN is not set")

    media = get(f"{API}/me/media", {"fields": FIELDS, "limit": 50, "access_token": token}).get("data", [])
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    posts, keep = [], set()

    for item in media:
        if len(posts) >= MAX_POSTS:
            break
        if "#noweb" in (item.get("caption") or "").lower():
            continue
        children = item.get("children", {}).get("data") or [item]
        images = []
        for n, child in enumerate(children[:MAX_IMAGES_PER_POST]):
            is_video = child.get("media_type") == "VIDEO"
            src = child.get("thumbnail_url") if is_video else child.get("media_url")
            if not src:
                continue
            name = f"{item['id']}-{n}.jpg"
            save_image(src, OUT_DIR / name)
            keep.add(name)
            images.append({"src": f"{OUT_DIR}/{name}", "video": is_video})
        if not images:
            continue
        posts.append({
            "id": item["id"],
            "date": item["timestamp"][:10],
            "caption": clean_caption(item.get("caption")),
            "images": images,
        })

    for old in OUT_DIR.glob("*.jpg"):
        if old.name not in keep:
            old.unlink()

    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(json.dumps({"source": "instagram", "posts": posts}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"saved {len(posts)} posts")

    # Keep the token alive: each refresh gives another 60 days.
    try:
        refreshed = get(f"{API}/refresh_access_token", {"grant_type": "ig_refresh_token", "access_token": token})
        new_token = refreshed.get("access_token")
        if new_token and os.environ.get("GITHUB_OUTPUT"):
            print(f"::add-mask::{new_token}")
            with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
                fh.write(f"token={new_token}\n")
    except Exception as exc:  # refresh failing shouldn't lose the posts already fetched
        print(f"token refresh skipped: {exc}")


if __name__ == "__main__":
    main()
