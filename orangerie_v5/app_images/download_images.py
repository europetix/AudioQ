#!/usr/bin/env python3
"""Download one image per Orangerie V5 track for the app. Run on your Mac:  python3 download_images.py
Reads Orangerie_V5_Image_List.csv (same folder). Writes images/orangerie_NNN.jpg, images/credits.csv and
images/index.html (a contact sheet: open it and check every picture against the official page before use).
- Public-domain paintings: Wikimedia Commons, only files whose licence says public domain / PD.
- Building, rooms, garden: Pexels, only if PEXELS_API_KEY is set in your environment (free key at pexels.com/api).
  The key is read from the environment only and never written to any file.
- Picasso (protected until 2043) and rows needing a licensed photo are skipped and listed.
Python 3 standard library only. Existing images are kept (delete one to fetch it again)."""
import csv, json, os, re, sys, time, html, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "images")
UA = "OrangerieAudioGuideImageFetcher/1.0 (personal app research; python urllib)"
WIDTH = 2000
os.makedirs(OUT, exist_ok=True)


def get(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def french_title(subject):
    """'Claude Monet, Les Nuages (Clouds), from …' -> 'Les Nuages'"""
    parts = [p.strip() for p in subject.split(",")]
    t = parts[1] if len(parts) > 1 else parts[0]
    return re.sub(r"\s*\(.*$", "", t).strip()


def commons(title, artist):
    q = f'"{title}" {artist.split()[-1]} filetype:bitmap'
    url = ("https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6"
           f"&gsrlimit=8&gsrsearch={urllib.parse.quote(q)}&prop=imageinfo&iiprop=url|size|extmetadata&iiurlwidth={WIDTH}")
    pages = json.loads(get(url)).get("query", {}).get("pages", {})
    for p in sorted(pages.values(), key=lambda p: p.get("index", 99)):
        ii = (p.get("imageinfo") or [{}])[0]; md = ii.get("extmetadata", {})
        lic = md.get("LicenseShortName", {}).get("value", "")
        if not re.search(r"public domain|\bPD\b|PD-", lic, re.I):
            continue
        if ii.get("width", 0) < 800:
            continue
        return dict(url=ii.get("thumburl") or ii["url"], page=ii.get("descriptionurl", ""), licence=lic,
                    source="Wikimedia Commons", author=re.sub("<[^>]+>", "", md.get("Artist", {}).get("value", artist)))
    return None


def pexels(query, key):
    url = f"https://api.pexels.com/v1/search?per_page=5&query={urllib.parse.quote(query)}"
    photos = json.loads(get(url, {"Authorization": key})).get("photos", [])
    if not photos:
        return None
    p = photos[0]
    return dict(url=p["src"]["large2x"], page=p["url"], licence="Pexels licence (free, commercial use OK)",
                source="Pexels", author=p.get("photographer", ""))


STOCK = {"001": "Musee de l'Orangerie Paris", "002": "Monet water lilies Orangerie", "003": "Orangerie water lilies room",
         "008": "Orangerie Monet room", "014": "Orangerie museum interior", "054": "Orangerie water lilies",
         "055": "Tuileries garden Paris"}

rows = list(csv.DictReader(open(os.path.join(HERE, "Orangerie_V5_Image_List.csv"), encoding="utf-8-sig")))
key = os.environ.get("PEXELS_API_KEY", "")
credits, skipped = [], []
for r in rows:
    n = r["track"]; dst = os.path.join(OUT, f"orangerie_{n}.jpg")
    if os.path.exists(dst):
        print(f"  [keep] {n}"); continue
    try:
        if "PROTECTED" in r["copyright"]:
            skipped.append((n, "Picasso: licence needed (Picasso Administration / ADAGP)")); continue
        hit = None
        if n in STOCK:
            if key:
                hit = pexels(STOCK[n], key)
            else:
                skipped.append((n, "building/room/garden: set PEXELS_API_KEY, or pick one by hand from the links in the CSV")); continue
        elif r["copyright"].startswith("Public domain") and r["artist"] not in ("", "—"):
            hit = commons(french_title(r["image_subject"]), r["artist"])
        else:
            skipped.append((n, "needs a hand-picked or licensed photo (see CSV)")); continue
        if not hit:
            skipped.append((n, "no public-domain match found: use the Commons link in the CSV")); continue
        open(dst, "wb").write(get(hit["url"]))
        credits.append(dict(track=n, file=os.path.basename(dst), subject=r["image_subject"], source=hit["source"],
                            source_page=hit["page"], licence=hit["licence"], author=hit["author"],
                            official_page=r["official_page"]))
        print(f"  [ok]   {n}  {hit['source']}  {hit['page']}")
        time.sleep(1)  # be polite to the APIs
    except Exception as e:
        skipped.append((n, f"error: {e}"))

old = []
cp = os.path.join(OUT, "credits.csv")
if os.path.exists(cp):
    old = [c for c in csv.DictReader(open(cp, encoding="utf-8")) if c["track"] not in {x["track"] for x in credits}]
allc = sorted(old + credits, key=lambda c: c["track"])
if allc:
    with open(cp, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(allc[0])); w.writeheader(); w.writerows(allc)
cards = "".join(
    f'<figure><img src="{html.escape(c["file"])}"><figcaption><b>{c["track"]}</b> {html.escape(c["subject"][:110])}<br>'
    f'<a href="{html.escape(c["source_page"])}">source</a> · <a href="{html.escape(c["official_page"])}">official page</a> · '
    f'{html.escape(c["licence"])}</figcaption></figure>' for c in allc)
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(
    "<!doctype html><meta charset=utf-8><title>Orangerie images</title><style>body{font:14px system-ui;margin:16px}"
    "main{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}img{width:100%;height:200px;"
    "object-fit:contain;background:#eee}figure{margin:0}</style><h1>Orangerie V5: check every image against its "
    f"official page</h1><main>{cards}</main>")
print(f"\nDownloaded {len(credits)} new, {len(allc)} in total -> {OUT}")
print("Open images/index.html and compare each picture with its official page before using it.")
if skipped:
    print("\nNot downloaded:")
    for n, why in skipped:
        print(f"  {n}: {why}")
