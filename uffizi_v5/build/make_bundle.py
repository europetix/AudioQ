import sys, os, re, json, shutil, glob, unicodedata
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT + '/v5/pipeline'); import v5_direction as V
SRC = ROOT + '/v5/tracks'
B = ROOT + '/bundle/Uffizi_YoTours'
shutil.rmtree(B, ignore_errors=True); os.makedirs(B)
SECTIONS = [  # (@section value, display, folder)
 ('Opening', 'Opening', '00_Welcome'),
 ('Second floor · The 13th and 14th centuries', 'Second floor · The 13th and 14th centuries', '01_Floor2_13th_14th_Centuries'),
 ('Second floor · Early Renaissance', 'Second floor · Early Renaissance', '02_Floor2_Early_Renaissance'),
 ('Second floor · The Botticelli rooms and the Tribune', 'Second floor · The Botticelli rooms and the Tribune', '03_Floor2_Botticelli_Tribune'),
 ('Second floor · High Renaissance', 'Second floor · High Renaissance', '04_Floor2_High_Renaissance'),
 ('Second floor · Raphael, Michelangelo and the Niobe Room', 'Second floor · Raphael, Michelangelo and the Niobe Room', '05_Floor2_Raphael_Michelangelo_Niobe'),
 ('First floor · Contini Bonacossi collection', 'First floor · Contini Bonacossi collection', '06_Floor1_Contini_Bonacossi'),
 ('First floor · Self-portraits', 'First floor · Self-portraits', '07_Floor1_Self_Portraits'),
 ('First floor · The 16th century', 'First floor · The 16th century', '08_Floor1_16th_Century'),
 ('First floor · Venice and the Verone', 'First floor · Venice and the Verone', '09_Floor1_Venice_Verone'),
 ('First floor · The 17th century', 'First floor · The 17th century', '10_Floor1_17th_Century'),
 ('Closing', 'Closing', '11_Closing'),
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
    m = re.match(r"^(?:[A-E]\d+(?:[–-][A-E]?\d+)?|[^·]*Botticelli[^·]*|(?:Sala|Salle|Saal|Room) [A-E]?\d+) · ", title)   # Uffizi titles start with the map code or "Botticelli rooms"
    return title[m.end():] if m else title

def room_label(sec, room, title=""):
    if sec in ("Opening", "Closing"):
        return ""
    if "Botticelli" in title.split(" · ")[0]:
        return "Botticelli"            # the Botticelli rooms' numbers are not certain (map vs pages): never in file names
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
plan = dict(tour_number=0, tour_slug="Galleria_degli_Uffizi", format="V5 Yo Tours 24 Oct 2026", language="EN",
    voices={"1": "en-US-AvaMultilingualNeural (chosen voice), base rate -8%, directed per passage (render_edge.py)",
            "2": "en-US-AndrewMultilingualNeural (trial)", "3": "en-US-BrianMultilingualNeural (earlier test voice)"},
    wpm=125, silent_tail_seconds=V.TAIL_S, mastering="-16 LUFS / -1.5 dBTP, 64 kbps mono",
    total_tracks=len(tracks), total_words=tw, total_min=round(tw / 125),
    sections=[dict(section=d, folder=fo, tracks=sum(1 for t in tracks if t['folder'] == fo)) for _, d, fo in SECTIONS],
    tracks=tracks)
json.dump(plan, open(f"{B}/plan.json", "w"), indent=1, ensure_ascii=False)
# ES / FR / DE / IT guides (v5/i18n/<lang>/tracks), rendered by generate_audio_ES_FR_DE_IT.command
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
for p in ('generate_audio.command', 'generate_audio_ES_FR_DE_IT.command', 'README.txt'):
    open(f'{B}/{p}', 'w', encoding='utf-8').write(fill(open(f'{ST}/{p}', encoding='utf-8').read()))
for p in ('pronunciation.py', 'tag_tracks.py', 'cover.jpg', 'make_lengths.py', 'levels.txt', 'lengths.json'):
    shutil.copy(f'{ST}/{p}', B)
# hand-written "next stop" bridges for the shorter versions: v5/bridges/*.txt (EN), v5/i18n/<lang>/bridges.txt
os.makedirs(f'{B}/bridges', exist_ok=True)
open(f'{B}/bridges/en.txt', 'w', encoding='utf-8').write(''.join(open(f, encoding='utf-8').read() for f in sorted(glob.glob(ROOT + '/v5/bridges/*.txt'))))
for f in sorted(glob.glob(ROOT + '/v5/i18n/*/bridges.txt')):
    shutil.copy(f, f"{B}/bridges/{f.split('/')[-2]}.txt")
for p in (f'{B}/generate_audio.command', f'{B}/generate_audio_ES_FR_DE_IT.command'):
    os.chmod(p, 0o755)
print(len(tracks), tw, round(tw/125))
for s in plan['sections']: print(s)
