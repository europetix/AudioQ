import sys, os, re, json, shutil, glob, unicodedata
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT + '/v5/pipeline'); import v5_direction as V
SRC = ROOT + '/v5/tracks'
B = ROOT + '/bundle/Bernabeu_YoTours'
shutil.rmtree(B, ignore_errors=True); os.makedirs(B)
SECTIONS = [  # (@section value, display, folder)
 ("Opening", "Opening", "00_Welcome"),
 ("Outside · The building and the man", "Outside · The building and the man", "01_Outside"),
 ("Panoramic view · The bowl", "Panoramic view · The bowl", "02_Panoramic_View"),
 ("Museum · Origins and the first Cups", "Museum · Origins and the first Cups", "03_Museum_Origins_and_First_Cups"),
 ("Museum · Galácticos to now", "Museum · Galácticos to now", "04_Museum_Galacticos_to_Now"),
 ("Dressing room and benches", "Dressing room and benches", "05_Dressing_Room_and_Benches"),
 ("Store and closing", "Store and closing", "06_Store"),
 ("Closing", "Closing", "07_Closing"),
]
SEC = {s[0]: s for s in SECTIONS}

def slug(s, n=48):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = s.replace("'", "").replace('"', "")
    s = re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")
    return s[:n].rstrip("_")

def short_title(title, room):
    """The title without a leading room name (Palatine titles start with the door sign; the room is already in the file name)."""
    if room and title.startswith(room):
        return title[len(room):].lstrip(" ·—-")
    if " · " in title:                                   # Bernabéu titles: "<zone> · <title>" (zone is in the file name)
        return title.split(" · ", 1)[1]
    m = re.match(r"^(Sala|Salle|Saal|Room) \d+(?:\.\d+)?(?: bis)?\s?[A-C]? · ", title)   # translated titles start with the local room word
    return title[m.end():] if m else title

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
    base = f"{n}_{rl + '_' if rl else ''}{slug(short_title(title, meta['room']))}"
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
plan = dict(tour_number=0, tour_slug="Estadio_Santiago_Bernabeu", format="V5 Yo Tours 23 Oct 2026", language="EN",
    voices={"1": "en-US-AvaMultilingualNeural (chosen voice), base rate -8%, directed per passage (render_edge.py)",
            "2": "en-US-AndrewMultilingualNeural (trial)", "3": "en-US-BrianMultilingualNeural (earlier test voice)"},
    wpm=125, silent_tail_seconds=V.TAIL_S, mastering="-16 LUFS / -1.5 dBTP, 64 kbps mono",
    total_tracks=len(tracks), total_words=tw, total_min=round(tw / 125),
    sections=[dict(section=d, folder=fo, tracks=sum(1 for t in tracks if t['folder'] == fo)) for _, d, fo in SECTIONS],
    tracks=tracks)
json.dump(plan, open(f"{B}/plan.json", "w"), indent=1, ensure_ascii=False)
# ES / FR / DE guides (v5/i18n/<lang>/tracks), rendered by generate_audio_ES_FR_DE.command
for f in sorted(glob.glob(ROOT + '/v5/i18n/*/tracks/*.perf.txt')):
    lang = f.split('/')[-3]; meta, clean = V.validate(f); n = os.path.basename(f)[:3]
    folder = SEC[meta['section']][2]
    rl = room_label(meta['section'], meta['room'].replace("Room", {"es": "Sala", "fr": "Salle", "de": "Saal"}.get(lang, "Room")))
    base = f"{n}_{rl + '_' if rl else ''}{slug(short_title(meta['title'], meta['room']))}"
    for d in ('scripts', 'perf'):
        os.makedirs(f"{B}/languages/{lang}/{d}/{folder}", exist_ok=True)
    open(f"{B}/languages/{lang}/scripts/{folder}/{base}.txt", "w", encoding="utf-8").write(clean + "\n")
    shutil.copy(f, f"{B}/languages/{lang}/perf/{folder}/{base}.perf.txt")
for p in ('v5_direction.py', 'render_edge.py'):
    shutil.copy(f"{ROOT}/v5/pipeline/{p}", B)
# hand-maintained bundle files (launcher, README, extended pronunciation, user-test docs)
ST = ROOT + '/build/static'
for p in ('generate_audio.command', 'generate_audio_ES_FR_DE.command', 'README.txt', 'pronunciation.py',
          'tag_tracks.py', 'cover.jpg', 'make_lengths.py'):
    shutil.copy(f'{ST}/{p}', B)
if os.path.isdir(f'{ST}/USER_TEST'):
    shutil.copytree(f'{ST}/USER_TEST', f'{B}/USER_TEST')
for p in (f'{B}/generate_audio.command', f'{B}/generate_audio_ES_FR_DE.command'):
    os.chmod(p, 0o755)
print(len(tracks), tw, round(tw/125))
for s in plan['sections']: print(s)
