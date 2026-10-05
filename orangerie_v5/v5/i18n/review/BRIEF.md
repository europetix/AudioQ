# Translation brief — Musée de l'Orangerie audio guide, V5 (55 tracks) → ES / FR / DE

You translate English audio-guide scripts into ONE target language. The text will be read aloud by a female
synthetic voice (ES: Dalia, Mexican Spanish; FR: Vivienne, France; DE: Katja, Germany) to travellers standing
in the museum. DO NOT EDIT ANY EXISTING FILE. Only write your output JSON files.

## Source
/home/user/AudioQ/orangerie_v5/v5/tracks/NNN.perf.txt — header lines (@title, @where, …), a line `---`, then
the spoken body. The body contains direction tags in square brackets: [pause] [long pause] [warmly] [quietly]
[amused] [curious] [conspiratorial] [reverent] [wry] [lightly]. Paragraphs are separated by a blank line.
The English is fact-checked: it is the single source of truth.

## Approved model (read it first)
/home/user/AudioQ/tour43_pitti_v5/v5/i18n/es/tracks/015.perf.txt and 053.perf.txt — the Spanish style the
client approved: adapted FOR LISTENING, not translated line by line.

## Rules (all mandatory)
1. FACTS: identical to the English. Same names, dates, numbers, places, attributions, hedges ("probably",
   "usually hangs here", "the story goes"). Add nothing, drop no fact. Every 4-digit year in the English must
   appear in your text, written as digits (e.g. 1512, 1790). Other numbers may be words or digits. When the English writes a year in words ("fifteen twelve", "sixteen ninety-seven"), write it as digits (1512, 1697): the voices read years correctly in your language.
2. LENGTH: spoken word count ≤ the English word count; aim about 5% shorter.
3. STYLE FOR THE EAR: short sentences, one idea each (average 9–12 words). Split long English sentences.
   Natural storytelling in the target language; a light rhetorical question or "look at…" is welcome.
   No semicolons, no parentheses in the spoken text. Avoid more than two dashes.
4. ADDRESS: formal — ES usted (never vosotros/tú), FR vous, DE Sie.
5. ES vocabulary must work for Latin America AND Spain (neutral): avoid coger, vale, ordenador, móvil, vosotros,
   zumo, coche→use auto only if needed. Prefer neutral words.
6. TAGS: keep every delivery tag ([warmly], [quietly], [amused], [curious], [conspiratorial], [reverent], [wry],
   [lightly]) in the SAME ORDER and in the SAME PARAGRAPH as the English. A delivery tag colours the rest of its
   paragraph. Keep every [pause]/[long pause] of the English, and ADD [pause] where a listener needs a breath
   (after a reveal, before "look at…"): typically 3–6 pauses per track. Use only these tags.
7. PARAGRAPHS: exactly the same number of paragraphs as the English, in the same order.
8. NAVIGATION: the last paragraph usually tells the visitor where to go next and what to look for. Translate it
   precisely: directions (left/right/up/down), room names, what the next work looks like. Never say "next track";
   phrases like "play its track there" → ES "reproduzca su pista allí", FR "écoutez sa piste là-bas", DE "spielen
   Sie dort den passenden Titel ab" (or similar natural wording, consistent across your tracks).
9. ARTWORK TITLES: the museum is French; its official titles are French. Where the English gives the French title and an English gloss (e.g. "Le Modèle blond, The Blond Model"): ES/DE keep the French title and translate the gloss ("Le Modèle blond, La modelo rubia"); FR uses the French title once (no gloss). Where the English gives only an English title, translate it naturally. Water Lilies compositions keep their French names where the English uses them (Les Nuages, Matin, Soleil couchant, Reflets verts, Le Matin clair aux saules, Les Deux Saules…).
10. NO ticket prices, opening hours or booking talk beyond what the English says. Do not name a specific exit door (the English deliberately does not).

## Glossary (use consistently)
| English | ES | FR | DE |
|---|---|---|---|
| Musée de l'Orangerie | el Museo de l'Orangerie | le musée de l'Orangerie | das Musée de l'Orangerie |
| the Water Lilies (Monet's cycle) | los Nenúfares (Les Nymphéas) on first mention, then los Nenúfares | les Nymphéas | die Seerosen (Les Nymphéas) on first mention, then die Seerosen |
| water lily (the plant) | nenúfar | nymphéa / nénuphar | Seerose |
| orangery | invernadero de naranjos (explain once: "eso es una orangerie") | orangerie | Orangerie |
| Tuileries garden | el Jardín de las Tullerías | le jardin des Tuileries | der Tuileriengarten |
| Room 1 / Room 2 (oval rooms) | la Sala 1 / la Sala 2 | la salle 1 / la salle 2 | Saal 1 / Saal 2 |
| lower level / level minus two | el nivel inferior / nivel menos dos | le niveau inférieur / niveau moins deux | das Untergeschoss / Ebene minus zwei |
| Walter-Guillaume collection | la colección Walter-Guillaume | la collection Walter-Guillaume | die Sammlung Walter-Guillaume |
| art dealer | marchante de arte | marchand d'art | Kunsthändler |
| Napoleon III | Napoleón III | Napoléon III | Napoleon III. |
| Catherine de' Medici | Catalina de Médici | Catherine de Médicis | Katharina von Medici |
| Victory Day / Armistice | el día de la Victoria / el Armisticio | le jour de la Victoire / l'Armistice | der Tag des Sieges / der Waffenstillstand |
| the State (French) | el Estado francés / el Estado | l'État | der französische Staat / der Staat |
| Paul Guillaume, Domenica, Jean Walter, Clemenceau, Giverny, Le Nôtre | unchanged | unchanged | unchanged |
| Renoir, Cézanne, Matisse, Picasso, Modigliani, Soutine, Derain, Henri Rousseau | unchanged (Rousseau "el Aduanero" only if the English says "Douanier") | unchanged ("le Douanier") | unchanged ("der Zöllner" only if the English says it) |

## Output
For EACH assigned track write one file: /tmp/claude-0/-home-user-AudioQ/9645e4c6-89fb-52f0-9dd4-640b4e64f64f/scratchpad/or_i18n/<lang>/NNN.json
  {"title": "<translated @title>", "where": "<translated @where, may use normal punctuation>", "body": "<spoken body with tags, paragraphs separated by \n\n>"}
Write valid JSON (use Python json.dump with ensure_ascii=False to be safe).
Before finishing, self-check every file with this snippet (fix and rewrite any failure):
  python3 - <<'PY'
  import json,re,sys,glob; sys.path.insert(0,'/home/user/AudioQ/orangerie_v5/v5/pipeline'); import v5_direction as V
  for f in sorted(glob.glob('/tmp/claude-0/-home-user-AudioQ/9645e4c6-89fb-52f0-9dd4-640b4e64f64f/scratchpad/or_i18n/LANG/*.json')):
      n=f[-8:-5]; d=json.load(open(f)); en=V.parse(f'/home/user/AudioQ/orangerie_v5/v5/tracks/{n}.perf.txt')[1]
      dt=lambda b:[t for t in re.findall(r'\[([^\]]+)\]',b) if 'pause' not in t]
      pz=lambda b:len(re.findall(r'\[(?:long )?pause\]',b)); c=V.clean(d['body']); ce=V.clean(en)
      errs=[]
      if dt(d['body'])!=dt(en): errs.append('delivery tags differ')
      if pz(d['body'])<pz(en): errs.append('fewer pauses')
      if d['body'].strip().count('\n\n')!=en.strip().count('\n\n'): errs.append('paragraph count')
      if len(c.split())>len(ce.split()): errs.append(f'too long {len(c.split())}>{len(ce.split())}')
      if set(re.findall(r'\b1[0-9]{3}\b',ce))-set(re.findall(r'\b1[0-9]{3}\b',c)): errs.append('missing years '+str(set(re.findall(r'\b1[0-9]{3}\b',ce))-set(re.findall(r'\b1[0-9]{3}\b',c))))
      if ';' in c or '(' in c: errs.append('semicolon/parenthesis')
      if re.findall(r'\[[^\]]*\]',V.TAG_RE.sub('',d['body'])): errs.append('unknown tag')
      print(n, 'OK' if not errs else errs)
  PY
(replace LANG with your language code). Report: the list of tracks written, any track where you were unsure of a
fact or a term, max ~150 words.
