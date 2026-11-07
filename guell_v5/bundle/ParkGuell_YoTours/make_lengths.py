#!/usr/bin/env python3
"""Make a shorter version (Essential, Highlights) out of a finished full render — Yo Tours, 23 Oct 2026.
Each chosen track is copied; where the shorter version skips ahead, a short spoken bridge is added at the end of the
track ("Next stop on this shorter tour: Room 39. Wassily Kandinsky, In the Bright Oval."), in the guide's own voice and
language, so the visitor always knows where the next stop is. Tracks already made are skipped (safe to run again).
Usage (from the bundle folder):
  python3 make_lengths.py <full output folder> <script folder: . or languages/xx> <en|es|fr|de> <Name> "<001 002 …>"
Needs the same voice settings as the render (EDGE_VOICE); falls back to a plain copy if the voice service fails."""
import asyncio, glob, os, re, shutil, subprocess, sys, tempfile
import v5_direction as V

OUT, SRC, LANG, NAME, NUMS = sys.argv[1], sys.argv[2], sys.argv[3].lower(), sys.argv[4], sys.argv[5].split()
VOICE = os.environ.get("EDGE_VOICE", "en-US-AvaMultilingualNeural")
DST = f"{OUT}_{NAME}"
TXT = {
    "en": ("Next stop on this shorter tour: {place}{level}. {subject}.", "Next stop on this shorter tour: the way out.", ", on Level {n}"),
    "es": ("Próxima parada de esta versión corta: {place}{level}. {subject}.", "Próxima parada de esta versión corta: la salida.", ", en la planta {n}"),
    "fr": ("Prochaine étape de cette version courte : {place}{level}. {subject}.", "Prochaine étape de cette version courte : la sortie.", ", au niveau {n}"),
    "de": ("Nächste Station dieser Kurzfassung: {place}{level}. {subject}.", "Nächste Station dieser Kurzfassung: der Ausgang.", ", auf Ebene {n}"),
    "it": ("Prossima tappa di questa versione breve: {place}{level}. {subject}.", "Prossima tappa di questa versione breve: l'uscita.", ", al livello {n}"),
}[LANG if LANG in ("en", "es", "fr", "de", "it") else "en"]
ONE = {"en": "One", "es": "uno", "fr": "un", "de": "eins", "it": "uno"}.get(LANG, "One")
ROOMWORD = {"en": "Room", "es": "Sala", "fr": "Salle", "de": "Saal", "it": "Sala"}.get(LANG, "Room")
# Optional per-guide settings (Uffizi, 24 Oct 2026): levels.txt as JSON with floor rules and spoken floor names, and
# place aliases (rooms whose number must not be spoken). The old Thyssen marker file (not JSON) keeps the old behaviour.
CFG = {}
if os.path.exists("levels.txt"):
    try:
        import json; CFG = json.load(open("levels.txt", encoding="utf-8"))
    except Exception:
        CFG = {}
# Hand-written bridges (writers / translators): bridges/<lang>.txt, lines "NNN E>MMM: text" (E = Essential, H = Highlights).
OVERRIDE = {}
_bf = os.path.join("bridges", f"{LANG}.txt")
if os.path.exists(_bf):
    for line in open(_bf, encoding="utf-8"):
        m = re.match(r"^\s*(\d{3})\s+([EH])>(\d{3}):\s*(.+?)\s*$", line)
        if m:
            OVERRIDE[(m.group(1), m.group(2), m.group(3))] = m.group(4)


def level_of(room):
    """Museums with numbered levels (Thyssen): rooms 1–29 Level 2, 30–56 Level 1, A–J Level 0. Others: None.
    With a JSON levels.txt: the first matching rule in CFG["rules"] ([regex on @room, level]) gives the level."""
    if not os.path.exists("levels.txt"):
        return None
    if CFG.get("rules"):
        for rx, lv in CFG["rules"]:
            if re.match(rx, room):
                return lv
        return None
    m = re.match(r"^Room (\d+)$", room)
    if m:
        n = int(m.group(1)); return 2 if n <= 29 else 1 if n <= 56 else None
    return 0 if re.match(r"^Room [A-J]$", room) else None


tracks = {}
for f in sorted(glob.glob(os.path.join(SRC, "perf", "*", "*.perf.txt"))):
    head = open(f, encoding="utf-8").read().split("\n---\n", 1)[0]
    meta = dict(re.findall(r"^@(\w+):\s*(.*)$", head, re.M))
    sec, base = os.path.basename(os.path.dirname(f)), os.path.basename(f)[:-len(".perf.txt")]
    tracks[base[:3]] = dict(sec=sec, base=base, title=meta.get("title", ""), room=meta.get("room", ""), type=meta.get("type", ""))
order = sorted(tracks)


def bridge_text(cur, nxt):
    t = tracks[nxt]
    if t["type"] == "CLOSE":
        return TXT[1]
    if " · " in t["title"]:
        place, subject = t["title"].split(" · ", 1)
    elif " — " in t["title"]:                         # Seville Cathedral titles: "<Spanish space> — <title>"
        place, subject = t["title"].split(" — ", 1)
    else:
        return TXT[1]
    for rx, names in CFG.get("alias", {}).items():   # e.g. the Botticelli rooms: never speak their (uncertain) numbers
        if re.match(rx, place):
            place = names.get(LANG, names["en"]); break
    else:
        if re.match(r"^[A-Z]\d+$", place):           # Uffizi titles start with the bare code: "A4 · Giotto ..."
            place = f"{ROOMWORD} {place}"
        elif re.match(r"^(CRA )?\d+$", place) and CFG.get("place_prefix"):   # Alcázar: leaflet numbers "15 · …"
            place = f"{CFG['place_prefix'].get(LANG, CFG['place_prefix']['en'])} {place.split()[-1]}"
    subject = subject.replace("Extra · ", "").replace(" — ", ", ")
    subject = re.sub(r" \((.*?)\)", r", \1", subject)  # brackets read badly: "Untitled (Green on Maroon)" -> "Untitled, Green on Maroon"
    subject = re.sub(r" I$", " " + ONE, subject)  # "Brown and Silver I": a lone I would be read as a letter
    lc, ln = level_of(tracks[cur]["room"]), level_of(t["room"])
    if ln is not None and ln != lc:
        say = CFG.get("say", {}).get(LANG)
        level = say[str(ln)] if say else TXT[2].format(n=ln)
    else:
        level = ""
    out = TXT[0].format(place=place, level=level, subject=subject)
    return out[:-1] if out.endswith(("?.", "!.", "..")) else out


async def _say(text, mp3):
    import edge_tts
    dr, vol, pitch = V.EDGE_STYLE.get(None, (0, 0, 0)) if hasattr(V, "EDGE_STYLE") else (0, 0, 0)
    await asyncio.wait_for(edge_tts.Communicate(text, VOICE, rate=f"{-8 + dr:+d}%").save(mp3), timeout=60)


def ff(*args):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args], check=True)


made = bridged = 0
for i, n in enumerate(NUMS):
    t = tracks.get(n)
    if not t:
        continue
    src = os.path.join(OUT, t["sec"], t["base"] + ".mp3")
    if not os.path.exists(src):
        print(f"  [miss] {n}: not in the full render yet"); continue
    os.makedirs(os.path.join(DST, t["sec"]), exist_ok=True)
    dst = os.path.join(DST, t["sec"], t["base"] + ".mp3")
    if os.path.exists(dst):
        continue
    nxt = NUMS[i + 1] if i + 1 < len(NUMS) else None
    skips = nxt is not None and order.index(nxt) != order.index(n) + 1
    if skips and (n, NAME[0].upper(), nxt) not in OVERRIDE and CFG.get("skip_extras_silently"):
        between = order[order.index(n) + 1:order.index(nxt)]   # only Extras skipped: the track's own cue already names the next main stop
        if all(tracks[b]["type"] == "X" for b in between):
            skips = False
    if not skips:
        shutil.copy(src, dst); made += 1; continue
    text = OVERRIDE.get((n, NAME[0].upper(), nxt)) or bridge_text(n, nxt)
    if LANG == "en":
        try:
            from pronunciation import apply_respelling; text_tts = apply_respelling(text, True)
        except Exception:
            text_tts = text
    else:
        text_tts = text
    with tempfile.TemporaryDirectory() as tmp:
        try:
            b = os.path.join(tmp, "b.mp3")
            for attempt in range(3):
                try:
                    asyncio.run(_say(text_tts, b)); break
                except Exception:
                    if attempt == 2: raise
            ff("-i", src, "-ar", "24000", "-ac", "1", os.path.join(tmp, "t.wav"))
            ff("-i", b, "-ar", "24000", "-ac", "1", os.path.join(tmp, "b.wav"))
            ff("-f", "lavfi", "-i", "anullsrc=channel_layout=mono:sample_rate=24000", "-t", "0.6", os.path.join(tmp, "g.wav"))
            ff("-f", "lavfi", "-i", "anullsrc=channel_layout=mono:sample_rate=24000", "-t", "1.5", os.path.join(tmp, "e.wav"))
            lst = os.path.join(tmp, "l.txt")
            open(lst, "w").write("".join(f"file '{os.path.join(tmp, x)}'\n" for x in ("t.wav", "g.wav", "b.wav", "e.wav")))
            ff("-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", os.path.join(tmp, "j.wav"))
            V.master(os.path.join(tmp, "j.wav"), dst, "64k")
            bridged += 1
        except Exception as e:
            print(f"  [note] {n}: bridge not voiced ({e}); plain copy instead.")
            shutil.copy(src, dst)
    made += 1
print(f"  [length] {NAME}: {len(NUMS)} tracks ({bridged} with a spoken 'next stop' bridge) -> {DST}")
