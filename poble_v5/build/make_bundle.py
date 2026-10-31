import sys, os, re, json, shutil, glob, unicodedata
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT + '/v5/pipeline'); import v5_direction as V
SRC = ROOT + '/v5/tracks'
B = ROOT + '/bundle/PobleEspanyol_YoTours'
shutil.rmtree(B, ignore_errors=True); os.makedirs(B)
SECTIONS = [  # (@section value, display, folder)
 ('The gate', 'The gate', '01_The_gate'),
 ('Calle Caballeros', 'Calle Caballeros', '02_Calle_Caballeros'),
 ('The brick tower', 'The brick tower', '03_The_brick_tower'),
 ('Catalonia', 'Catalonia', '04_Catalonia'),
 ('The top of the hill', 'The top of the hill', '05_The_top_of_the_hill'),
 ('Andalusia', 'Andalusia', '06_Andalusia'),
 ('Back to the Plaza Mayor', 'Back to the Plaza Mayor', '07_Back_to_the_Plaza_Mayor'),
]
SEC = {s[0]: s for s in SECTIONS}

def slug(s, n=56):
    s = s.replace("º", "")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = s.replace("'", "").replace('"', "")
    s = re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")
    return s[:n].rstrip("_")

def short_title(title, room):
    """The title without a leading room name (Palatine titles start with the door sign; the room is already in the file name)."""
    return title   # keep the whole title ("Walkway — …", "Mirador 360º — …") so file names are consistent   # Setas titles: "<Spanish space> — <title>"; the space is kept

def room_label(sec, room, title=""):
    if True:
        return ""
    return ""   # the title already starts with the Spanish space name
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
    tracks.append(dict(seq=n, section=disp, folder=folder, room=meta['room'], title=title,
        register=meta['type'], words=len(clean.split()), where=meta.get('where', ''),
        what=meta.get('what', ''), listen=meta.get('listen', ''), pace=meta['pace'],
        script=f"scripts/{folder}/{base}.txt", perf=f"perf/{folder}/{base}.perf.txt",
        mp3=f"{folder}/{base}.mp3"))
tw = sum(t['words'] for t in tracks)
plan = dict(tour_number=0, tour_slug="Poble_Espanyol", format="V5 Yo Tours 31 Oct 2026", language="EN",
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
                .replace('@@N_MAIN@@', str(sum(1 for t in tracks if t['register'] != 'X'))).replace('@@N_X@@', str(sum(1 for t in tracks if t['register'] == 'X'))))
for p in ('generate_audio.command', 'generate_audio_ES_FR_DE.command', 'README.txt'):
    open(f'{B}/{p}', 'w', encoding='utf-8').write(fill(open(f'{ST}/{p}', encoding='utf-8').read()))
for p in ('pronunciation.py', 'tag_tracks.py', 'cover.jpg', 'make_lengths.py', 'levels.txt', 'lengths.json'):
    shutil.copy(f'{ST}/{p}', B)
# hand-written "next stop" bridges for the shorter versions: v5/bridges/*.txt (EN), v5/i18n/<lang>/bridges.txt
os.makedirs(f'{B}/bridges', exist_ok=True)
open(f'{B}/bridges/en.txt', 'w', encoding='utf-8').write(''.join(open(f, encoding='utf-8').read() for f in sorted(glob.glob(ROOT + '/v5/bridges/*.txt'))))
for f in sorted(glob.glob(ROOT + '/v5/i18n/*/bridges.txt')):
    shutil.copy(f, f"{B}/bridges/{f.split('/')[-2]}.txt")
for p in (f'{B}/generate_audio.command', f'{B}/generate_audio_ES_FR_DE.command'):
    os.chmod(p, 0o755)
print(len(tracks), tw, round(tw/125))
for s in plan['sections']: print(s)
