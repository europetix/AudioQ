#!/usr/bin/env python3
"""Label every MP3 of a rendered guide for phone music players (Yo Tours, 7 Oct 2026).
Writes title ("013 · Manet — Olympia"), album ("Musée d'Orsay Audio Guide · English"), track number (13/75), artist and
album artist (Yo Tours), genre, year, language and the cover image. The audio itself is copied untouched.
Safe to run again: it rewrites the labels, and it also labels MP3s rendered before this step existed.
Usage (from the bundle folder):  python3 tag_tracks.py <output folder> <script folder: . or languages/xx> <en|es|fr|de>"""
import glob, json, os, re, subprocess, sys

BRAND = "Yo Tours"
MUSEUM = "Musée d'Orsay"
LANGS = {"en": ("English", "eng"), "es": ("Español", "spa"), "fr": ("Français", "fra"), "de": ("Deutsch", "deu")}
GUIDE = {"en": "Audio Guide", "es": "Audioguía", "fr": "Audioguide", "de": "Audioguide"}
HERE = os.path.dirname(os.path.abspath(__file__))


def title_of(src, sec, base):
    perf = os.path.join(src, "perf", sec, base + ".perf.txt")
    if os.path.exists(perf):
        m = re.search(r"^@title:\s*(.+)$", open(perf, encoding="utf-8").read(), re.M)
        if m:
            return f"{base[:3]} · {m.group(1).strip()}"
    return base.replace("_", " ")


def main():
    out, src, lang = sys.argv[1], sys.argv[2], sys.argv[3].lower()
    lname, iso = LANGS.get(lang, ("English", "eng"))
    cover = os.path.join(HERE, "cover.jpg")
    try:
        total = len(json.load(open(os.path.join(HERE, "plan.json"), encoding="utf-8"))["tracks"])
    except Exception:
        total = 0
    album = f"{MUSEUM} {GUIDE.get(lang, 'Audio Guide')} · {lname}"
    files = sorted(f for f in glob.glob(os.path.join(out, "*", "*.mp3")) if ".part." not in f)
    done = bad = 0
    for f in files:
        sec, base = os.path.basename(os.path.dirname(f)), os.path.splitext(os.path.basename(f))[0]
        n = int(base[:3]) if base[:3].isdigit() else 0
        tmp = f[:-4] + ".tag.part.mp3"   # ".part.mp3" is ignored by the old-files safeguard
        cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", f]
        if os.path.exists(cover):
            cmd += ["-i", cover, "-map", "0:a", "-map", "1:v", "-c", "copy", "-disposition:v", "attached_pic",
                    "-metadata:s:v", "title=Album cover", "-metadata:s:v", "comment=Cover (front)"]
        else:
            cmd += ["-map", "0:a", "-c", "copy"]
        cmd += ["-map_metadata", "-1", "-id3v2_version", "3",
                "-metadata", f"title={title_of(src, sec, base)}",
                "-metadata", f"album={album}",
                "-metadata", f"artist={BRAND}", "-metadata", f"album_artist={BRAND}",
                "-metadata", f"track={n}/{total}" if total else f"track={n}",
                "-metadata", "genre=Audio Guide", "-metadata", "date=2026",
                "-metadata", f"language={iso}", "-metadata", f"publisher={BRAND}",
                tmp]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode == 0 and os.path.getsize(tmp) > 0:
            os.replace(tmp, f); done += 1
        else:
            bad += 1
            if os.path.exists(tmp):
                os.remove(tmp)
    print(f"  [labels] {done} track(s) labelled for phones ({album})" + (f", {bad} could not be labelled" if bad else ""))


if __name__ == "__main__":
    main()
