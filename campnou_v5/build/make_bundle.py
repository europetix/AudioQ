import sys, os, re, json, shutil, glob, unicodedata
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT + '/v5/pipeline'); import v5_direction as V
SRC = ROOT + '/v5/tracks'
B = ROOT + '/bundle/SpotifyCampNou_YoTours'
shutil.rmtree(B, ignore_errors=True); os.makedirs(B)
SECTIONS = [  # (@section value, display, folder) — PLAN §1 "Sections"
 ('Outside the museum', 'Outside the museum', '01_Outside'),
 ('The entrance hall', 'The entrance hall', '02_Entrance'),
 ('The trophies', 'The trophies', '03_Trophies'),
 ("The club's history", "The club's history", '04_History'),
 ('More stories inside', 'More stories inside', '05_Stories_inside'),
 ("Messi's space", "Messi's space", '06_Messi'),
 ('The round room', 'The round room', '07_Round_room'),
 ('The models', 'The models', '08_Models'),
 ('The viewpoint', 'The viewpoint', '09_Viewpoint'),
 ('The way out', 'The way out', '10_Way_out'),
]
SEC = {s[0]: s for s in SECTIONS}

def slug(s, n=56):
    s = s.replace("º", "")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = s.replace("'", "").replace('"', "")
    s = re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")
    return s[:n].rstrip("_")

def short_title(title, room):
    """The whole title is kept: Camp Nou titles are "<place> · <title>" (Extras "<place> · Extra · <title>"; 001 plain), so file names are consistent."""
    return title

def room_label(sec, room, title=""):
    if True:
        return ""
    return ""   # the title already starts with the place name
    r = room.replace("–", "-")
    return slug(r.replace(" ", "-").replace("-", "~"), 24).replace("_", "-").replace("~", "-") .strip("-")

tracks = []
for f in sorted(glob.glob(SRC + '/*.perf.txt')):
    meta, clean = V.validate(f)
    n = os.path.basename(f)[:3]
    sec = meta['section']; disp, folder = SEC[sec][1], SEC[sec][2]
    title = meta['title']
    rl = room_label(sec, meta['room'], title)
    base = f"{n}_{rl + '_' if rl else ''}{slug(short_title(title, meta['room']))}"
    for d in ('scripts', 'perf'):
        os.makedirs(f"{B}/{d}/{folder}", exist_ok=True)
    open(f"{B}/scripts/{folder}/{base}.txt", "w", encoding="utf-8").write(clean + "\n")
    shutil.copy(f, f"{B}/perf/{folder}/{base}.perf.txt")
    # round-trip check: perf strips to the script exactly
    V.validate(f"{B}/perf/{folder}/{base}.perf.txt", open(f"{B}/scripts/{folder}/{base}.txt").read())
    tracks.append(dict(seq=n, extra=(meta['type'] == 'X' or ' · Extra · ' in title), section=disp, folder=folder, room=meta['room'], title=title,
        register=meta['type'], words=len(clean.split()), where=meta.get('where', ''),
        what=meta.get('what', ''), listen=meta.get('listen', ''), pace=meta['pace'],
        script=f"scripts/{folder}/{base}.txt", perf=f"perf/{folder}/{base}.perf.txt",
        mp3=f"{folder}/{base}.mp3"))
tw = sum(t['words'] for t in tracks)
plan = dict(tour_number=0, tour_slug="SpotifyCampNou_FC_Barcelona_Museum", guide_title="FC Barcelona Museum · Spotify Camp Nou", format="V5 Yo Tours 14 Nov 2026", language="EN",
    voices={"1": "en-US-AvaMultilingualNeural (chosen voice), base rate -8%, directed per passage (render_edge.py)",
            "2": "en-US-AndrewMultilingualNeural (trial)", "3": "en-US-BrianMultilingualNeural (earlier test voice)"},
    wpm=125, silent_tail_seconds=V.TAIL_S, mastering="-16 LUFS / -1.5 dBTP, 64 kbps mono",
    total_tracks=len(tracks), total_words=tw, total_min=round(tw / 125),
    sections=[dict(section=d, folder=fo, tracks=sum(1 for t in tracks if t['folder'] == fo)) for _, d, fo in SECTIONS],
    tracks=tracks)
json.dump(plan, open(f"{B}/plan.json", "w"), indent=1, ensure_ascii=False)
# ES / FR / DE guides (v5/i18n/<lang>/tracks), rendered by generate_audio_ES_FR_DE.command. None yet (translations come
# later): the loop then makes nothing, and that launcher says the language is not in the bundle yet.
for f in sorted(glob.glob(ROOT + '/v5/i18n/*/tracks/*.perf.txt')):
    lang = f.split('/')[-3]; meta, clean = V.validate(f); n = os.path.basename(f)[:3]
    folder = SEC[meta['section']][2]
    rl = room_label(meta['section'], meta['room'].replace("Room", {"es": "Sala", "fr": "Salle", "de": "Saal", "it": "Sala"}.get(lang, "Room")), meta['title'])
    base = f"{n}_{rl + '_' if rl else ''}{slug(short_title(meta['title'], meta['room']))}"
    for d in ('scripts', 'perf'):
        os.makedirs(f"{B}/languages/{lang}/{d}/{folder}", exist_ok=True)
    open(f"{B}/languages/{lang}/scripts/{folder}/{base}.txt", "w", encoding="utf-8").write(clean + "\n")
    shutil.copy(f, f"{B}/languages/{lang}/perf/{folder}/{base}.perf.txt")
for p in ('v5_direction.py', 'render_edge.py'):
    shutil.copy(f"{ROOT}/v5/pipeline/{p}", B)
# hand-maintained bundle files (launchers with the length lists filled in, README, pronunciation, tags, lengths, floors)
ST = ROOT + '/build/static'
LEN = json.load(open(f'{ST}/lengths.json'))
def fill(text):
    e, h = LEN['ESSENTIAL'].split(), LEN['HIGHLIGHTS'].split()
    return (text.replace('@@ESSENTIAL@@', LEN['ESSENTIAL']).replace('@@HIGHLIGHTS@@', LEN['HIGHLIGHTS'])
                .replace('@@N_FULL@@', str(len(tracks))).replace('@@N_ESS@@', str(len(e))).replace('@@N_HI@@', str(len(h)))
                .replace('@@N_MAIN@@', str(sum(1 for t in tracks if not t['extra']))).replace('@@N_X@@', str(sum(1 for t in tracks if t['extra']))))
for p in ('generate_audio.command', 'generate_audio_ES_FR_DE.command', 'README.txt'):
    open(f'{B}/{p}', 'w', encoding='utf-8').write(fill(open(f'{ST}/{p}', encoding='utf-8').read()))
for p in ('pronunciation.py', 'tag_tracks.py', 'cover.jpg', 'make_lengths.py', 'levels.txt', 'lengths.json'):
    shutil.copy(f'{ST}/{p}', B)
# hand-written "next stop" bridges for the shorter versions: v5/bridges/*.txt (EN), v5/i18n/<lang>/bridges.txt
os.makedirs(f'{B}/bridges', exist_ok=True)
_MARK = re.compile(r"\s*\[(?:O[^\]]*|ALT[^\]]*)\]")   # writers' on-site tags ([O13], [O8, ALT-K]) are never spoken: dropped from bridge lines here (the sources are not changed)
_clean = lambda t: "".join(_MARK.sub("", l) if re.match(r"^\s*\d{3}\s+[EH]>\d{3}:", l) else l for l in t.splitlines(True))
_txt = lambda f: (lambda t: t if t.endswith('\n') else t + '\n')(_clean(open(f, encoding='utf-8').read()))   # one bridge per line, even if a file lacks its last newline
# Camp Nou: the writers' files v5/bridges/{A,B,C,D}.txt are merged into one bridges/en.txt, sorted by track, version and
# destination; lines starting "#" are on-site notes (tags, conditions) and are never copied, so never voiced.
def _merge(files):
    rows = {}
    for f in files:
        for line in _txt(f).splitlines():
            m = re.match(r"^\s*(\d{3})\s+([EH])>(\d{3}):\s*(.+?)\s*$", line)
            if line.lstrip().startswith('#') or not line.strip():
                continue
            if not m:
                sys.exit(f"bridges: a line in {f} is neither a note (#) nor 'NNN E>MMM: text': {line[:60]}")
            key = (m.group(1), m.group(2), m.group(3))
            if key in rows:
                sys.exit(f"bridges: {key} is written twice")
            rows[key] = f"{key[0]} {key[1]}>{key[2]}: {m.group(4)}"
    return ''.join(rows[k] + '\n' for k in sorted(rows)), len(rows)
_en, N_BRIDGES = _merge(sorted(glob.glob(ROOT + '/v5/bridges/*.txt')))
open(f'{B}/bridges/en.txt', 'w', encoding='utf-8').write(_en)
# Check: every bridge sits where its version skips ahead, goes to the version's next stop and ends on that stop's
# @title; every skip that is not over Extras only has one (skips over Extras only are silent: levels.txt).
_T = {t['seq']: t for t in tracks}
_rows = {(m.group(1), m.group(2), m.group(3)): m.group(4) for m in re.finditer(r"^(\d{3}) ([EH])>(\d{3}): (.+)$", _en, re.M)}
_need = set()
for v, key in (('E', 'ESSENTIAL'), ('H', 'HIGHLIGHTS')):
    ns = LEN[key].split()
    for a, b in zip(ns, ns[1:]):
        between = [x for x in sorted(_T) if a < x < b]
        if between and not all(_T[x]['extra'] for x in between):
            _need.add((a, v, b))
for k in sorted(set(_rows) | _need):
    if k not in _rows: sys.exit(f"bridges: missing {k[0]} {k[1]}>{k[2]}")
    if k not in _need: sys.exit(f"bridges: {k[0]} {k[1]}>{k[2]} is not where its version skips ahead")
    if not _rows[k].rstrip('.').endswith(': ' + _T[k[2]]['title']):
        sys.exit(f"bridges: {k[0]} {k[1]}>{k[2]} does not end on the title of {k[2]} ({_T[k[2]]['title']})")
print('bridges checked:', ', '.join(f"{v} {sum(1 for k in _rows if k[1] == v)}" for v in 'EH'))
for f in sorted(glob.glob(ROOT + '/v5/i18n/*/bridges.txt')):
    open(f"{B}/bridges/{f.split('/')[-2]}.txt", 'w', encoding='utf-8').write(_merge([f])[0])
for p in (f'{B}/generate_audio.command', f'{B}/generate_audio_ES_FR_DE.command'):
    os.chmod(p, 0o755)
print(len(tracks), tw, round(tw/125), f'bridges: {N_BRIDGES}')
for s in plan['sections']: print(s)
