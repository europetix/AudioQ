import sys, os, re, json, shutil, glob, unicodedata
sys.path.insert(0, '/home/claude/pitti/v5/pipeline'); import v5_direction as V
SRC = '/home/claude/pitti/v5/tracks'
B = '/home/claude/pitti/bundle/Palazzo_Pitti_V5_Test_EN'
shutil.rmtree(B, ignore_errors=True); os.makedirs(B)
SECTIONS = [  # (@section value, display, folder)
 ("Opening", "Opening", "00_Welcome"),
 ("Palatine", "Palatine Gallery", "01_Palatine_Gallery"),
 ("Modern Art", "Gallery of Modern Art", "02_Gallery_of_Modern_Art"),
 ("Fashion and Costume", "Museum of Fashion & Costume", "03_Museum_of_Fashion_and_Costume"),
 ("Royal Apartments", "Imperial & Royal Apartments", "04_Imperial_and_Royal_Apartments"),  # V5.1: after Fashion, on the way back down (separate ticket)
 ("Russian Icons and Chapel", "Russian Icons & Palatine Chapel", "05_Russian_Icons_and_Palatine_Chapel"),
 ("Boboli", "Boboli Gardens", "06_Boboli_Gardens"),
 ("Closing", "Closing", "07_Closing"),
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
plan = dict(tour_number=43, tour_slug="Palazzo_Pitti", format="V5-test", language="EN",
    voices={"1": "en-US-BrianMultilingualNeural, base rate -8%, directed per passage (render_edge.py)",
            "2": "Kokoro am_michael, base speed 0.85, directed per passage (render_kokoro.py)"},
    wpm=125, silent_tail_seconds=V.TAIL_S, mastering="-16 LUFS / -1.5 dBTP, 96 kbps mono",
    total_tracks=len(tracks), total_words=tw, total_min=round(tw / 125),
    sections=[dict(section=d, folder=fo, tracks=sum(1 for t in tracks if t['folder'] == fo)) for _, d, fo in SECTIONS],
    tracks=tracks)
json.dump(plan, open(f"{B}/plan.json", "w"), indent=1, ensure_ascii=False)
# ES / FR / DE voice samples (translated tracks 015 + 053), rendered by voice_samples_ES_FR_DE.command
for f in sorted(glob.glob('/home/claude/pitti/v5/i18n/*/tracks/*.perf.txt')):
    lang = f.split('/')[-3]; meta, clean = V.validate(f); n = os.path.basename(f)[:3]
    folder = SEC[meta['section']][2]; rl = room_label(meta['section'], meta['room'])
    base = f"{n}_{rl + '_' if rl else ''}{slug(meta['title'])}"
    for d in ('scripts', 'perf'):
        os.makedirs(f"{B}/voice_samples_i18n/{lang}/{d}/{folder}", exist_ok=True)
    open(f"{B}/voice_samples_i18n/{lang}/scripts/{folder}/{base}.txt", "w", encoding="utf-8").write(clean + "\n")
    shutil.copy(f, f"{B}/voice_samples_i18n/{lang}/perf/{folder}/{base}.perf.txt")
for p in ('v5_direction.py', 'render_kokoro.py', 'render_edge.py'):
    shutil.copy(f"/home/claude/pitti/v5/pipeline/{p}", B)
# hand-maintained bundle files (launcher, README, extended pronunciation, user-test docs)
ST = '/home/claude/pitti/build/static'
for p in ('generate_audio.command', 'voice_samples_ES_FR_DE.command', 'README.txt', 'pronunciation.py'):
    shutil.copy(f'{ST}/{p}', B)
shutil.copytree(f'{ST}/USER_TEST', f'{B}/USER_TEST')
for p in (f'{B}/generate_audio.command', f'{B}/voice_samples_ES_FR_DE.command', f'{B}/USER_TEST/make_listening_test.command'):
    os.chmod(p, 0o755)
print(len(tracks), tw, round(tw/125))
for s in plan['sections']: print(s)
