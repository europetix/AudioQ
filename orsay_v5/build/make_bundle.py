import sys, os, re, json, shutil, glob, unicodedata
sys.path.insert(0, '/home/claude/orsay/v5/pipeline'); import v5_direction as V
SRC = '/home/claude/orsay/v5/tracks'
B = '/home/claude/orsay/bundle/Orsay_V5_EN'
shutil.rmtree(B, ignore_errors=True); os.makedirs(B)
SECTIONS = [  # (@section value, display, folder)
 ("Opening", "Welcome", "00_Welcome"),
 ("Academic Art", "Level 0 · Academic art", "01_L0_Academic_Art"),
 ("Realism", "Level 0 · Realism", "02_L0_Realism"),
 ("Manet and Friends", "Level 0 · Manet and friends", "03_L0_Manet_and_Friends"),
 ("Nave End", "Level 0 · End of the nave", "04_L0_End_of_the_Nave"),
 ("Impressionism", "Level 5 · Impressionism", "05_L5_Impressionism"),
 ("Van Gogh", "Level 5 · Van Gogh", "06_L5_Van_Gogh"),
 ("Post-Impressionism", "Level 5 · Post-Impressionism", "07_L5_Post_Impressionism"),
 ("Lautrec and the Nabis", "Level 2 · Lautrec and the Nabis", "08_L2_Lautrec_and_Nabis"),
 ("Art Nouveau and Sculpture", "Level 2 · Art Nouveau and sculpture", "09_L2_Art_Nouveau_and_Sculpture"),
 ("Closing", "Closing", "10_Closing"),
]
SEC = {s[0]: s for s in SECTIONS}

def slug(s, n=48):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = s.replace("'", "").replace('"', "")
    s = re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")
    return s[:n].rstrip("_")

def room_label(sec, room):
    if sec in ("Opening", "Closing"):
        return ""
    r = room.replace("–", "-")
    return slug(r.replace(" ", "-").replace("-", "~"), 24).replace("_", "-").replace("~", "-") .strip("-")

tracks = []
for f in sorted(glob.glob(SRC + '/*.perf.txt')):
    meta, clean = V.validate(f)
    n = os.path.basename(f)[:3]
    sec = meta['section']; disp, folder = SEC[sec][1], SEC[sec][2]
    title = meta['title']
    rl = room_label(sec, meta['room'])
    base = f"{n}_{rl + '_' if rl else ''}{slug(title)}"
    for d in ('scripts', 'perf'):
        os.makedirs(f"{B}/{d}/{folder}", exist_ok=True)
    open(f"{B}/scripts/{folder}/{base}.txt", "w", encoding="utf-8").write(clean + "\n")
    shutil.copy(f, f"{B}/perf/{folder}/{base}.perf.txt")
    # round-trip check: perf strips to the script exactly
    V.validate(f"{B}/perf/{folder}/{base}.perf.txt", open(f"{B}/scripts/{folder}/{base}.txt").read())
    tracks.append(dict(seq=n, section=disp, folder=folder, room=meta['room'], title=title,
        register=meta['type'], words=len(clean.split()), where=meta.get('where', ''),
        what=meta.get('what', ''), listen=meta.get('listen', ''), pace=meta['pace'],
        script=f"scripts/{folder}/{base}.txt", perf=f"perf/{folder}/{base}.perf.txt",
        mp3=f"{folder}/{base}.mp3"))
tw = sum(t['words'] for t in tracks)
plan = dict(tour_number=0, tour_slug="Musee_d_Orsay", format="V5", language="EN",
    voices={"1": "en-US-AvaMultilingualNeural (chosen voice), base rate -8%, directed per passage (render_edge.py)",
            "2": "Kokoro am_michael, base speed 0.85, directed per passage (render_kokoro.py)", "3": "en-US-AndrewMultilingualNeural (trial)", "4": "en-US-BrianMultilingualNeural (earlier test voice)"},
    wpm=125, silent_tail_seconds=V.TAIL_S, mastering="-16 LUFS / -1.5 dBTP, 64 kbps mono",
    total_tracks=len(tracks), total_words=tw, total_min=round(tw / 125),
    sections=[dict(section=d, folder=fo, tracks=sum(1 for t in tracks if t['folder'] == fo)) for _, d, fo in SECTIONS],
    tracks=tracks)
json.dump(plan, open(f"{B}/plan.json", "w"), indent=1, ensure_ascii=False)
# ES / FR / DE guides (v5/i18n/<lang>/tracks), rendered by generate_audio_ES_FR_DE.command (full guide or samples 013 + 042)
for f in sorted(glob.glob('/home/claude/orsay/v5/i18n/*/tracks/*.perf.txt')):
    lang = f.split('/')[-3]; meta, clean = V.validate(f); n = os.path.basename(f)[:3]
    folder = SEC[meta['section']][2]; rl = room_label(meta['section'], meta['room'])
    base = f"{n}_{rl + '_' if rl else ''}{slug(meta['title'])}"
    for d in ('scripts', 'perf'):
        os.makedirs(f"{B}/languages/{lang}/{d}/{folder}", exist_ok=True)
    open(f"{B}/languages/{lang}/scripts/{folder}/{base}.txt", "w", encoding="utf-8").write(clean + "\n")
    shutil.copy(f, f"{B}/languages/{lang}/perf/{folder}/{base}.perf.txt")
for p in ('v5_direction.py', 'render_kokoro.py', 'render_edge.py'):
    shutil.copy(f"/home/claude/orsay/v5/pipeline/{p}", B)
# hand-maintained bundle files (launcher, README, extended pronunciation, user-test docs)
ST = '/home/claude/orsay/build/static'
for p in ('generate_audio.command', 'README.txt', 'pronunciation.py'):  # ES/FR/DE launcher joins when Orsay is translated
    shutil.copy(f'{ST}/{p}', B)
shutil.copytree(f'{ST}/USER_TEST', f'{B}/USER_TEST')
for p in (f'{B}/generate_audio.command',):
    os.chmod(p, 0o755)
print(len(tracks), tw, round(tw/125))
for s in plan['sections']: print(s)
