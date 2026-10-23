# Translation brief — Museo Nacional Thyssen-Bornemisza audio guide, Yo Tours 23 Oct 2026 (70 tracks: 51 main stops + 19 short optional Extras) → ES / FR / DE

You translate English audio-guide scripts into ONE target language. The text will be read aloud by a female
synthetic voice (ES: Dalia, Mexican Spanish; FR: Vivienne, France; DE: Katja, Germany) to travellers walking through
the Museo Nacional Thyssen-Bornemisza in Madrid with headphones. Customers complained that the previous guide sent them to wrong rooms,
so NAVIGATION ACCURACY comes first. DO NOT EDIT ANY EXISTING FILE. Only write your own JSON files and your notes file.

## Source
/home/claude/audioq/thyssen_v5/v5/tracks/NNN.perf.txt — header lines (@title, @where, @what, @sources …), a line `---`, then
the spoken body. The body contains direction tags: [pause] [long pause] [warmly] [quietly] [amused] [curious]
[conspiratorial] [reverent] [wry] [lightly], and *emphasis* marks. Paragraphs are separated by a blank line.
The English is fact-checked against the museum's own pages: it is the single source of truth. @what and @sources give the
official title, date and URL on museothyssen.org. The museum's Spanish page is the same URL without "/en"
(…/en/collection/artists/… → …/coleccion/artistas/…). ES uses the museum's official Spanish titles of works; room titles come
from the museum's Spanish visitor map (Sala 33: Siglo XIX. El periodo impresionista, etc. — translate the English map titles
faithfully if you cannot fetch the Spanish map). Check them with
WebFetch, one page at a time (never in bursts; never browser tools or curl; if a page asks you to verify you are human, stop
using it and note the title as unchecked). FR/DE translate titles naturally, using the established title in that language
when there is one .

## Style model (read before you start)
Approved translations of earlier Yo Tours guides; match their voice:
- ES: /home/claude/audioq/orsay_v5/v5/i18n/es/tracks/013.perf.txt, 044.perf.txt
- FR: /home/claude/audioq/orsay_v5/v5/i18n/fr/tracks/013.perf.txt, 044.perf.txt
- DE: /home/claude/audioq/orsay_v5/v5/i18n/de/tracks/013.perf.txt, 044.perf.txt
Adapted FOR LISTENING, not translated line by line.

## Rules (all mandatory)
1. FACTS identical to the English: names, dates, numbers, places, sizes, attributions and hedges ("probably", "the story
   goes", "if it isn't here…", "the museum says"). Add nothing, drop no fact, don't "improve" a fact. If you think the
   English is wrong, translate it anyway and flag it in your notes.
2. YEARS AS DIGITS: every year in the English must appear as digits. Decades naturally (ES "la década de 1630",
   FR "les années 1630", DE "die 1630er-Jahre").
3. LENGTH: spoken word count ≤ the English; aim about 5% shorter.
4. FOR THE EAR: short sentences (average 9–12 words). No semicolons, no parentheses in speech. At most two dashes per track.
5. ADDRESS: formal — ES usted, FR vous, DE Sie.
6. ES vocabulary neutral for Latin America AND Spain (avoid coger, vale, vosotros, móvil, ordenador).
7. TAGS: every delivery tag in the SAME ORDER and SAME PARAGRAPH as the English. Keep every [pause]/[long pause] and add
   [pause] where a listener needs a breath (typically 3–6 per track). Only these tags.
8. PARAGRAPHS: exactly the same number, same order.
9. NAVIGATION (the last paragraph): translate precisely every room number, floor, stairs/lift, "back through", "next door",
   "stay in this room", signs to follow, and what to look for. Room numbers exactly as the English: ES "la sala 33", FR "la salle 33", DE "Saal 33"; Carmen Thyssen rooms
   ES "la sala A", FR "la salle A", DE "Saal A". Levels: ES "la planta 2 / 1 / 0", FR "le niveau 2 / 1 / 0",
   DE "Ebene 2 / 1 / 0". "the central hall" → ES "el hall central", FR "le hall central", DE "die zentrale Halle".
   "Paseo del Prado" stays. Never say "next track". In speech "Sala 7 · Extra" never appears: say "un breve Extra" etc.
10. CONDITIONALS: translate every "if…", "if it isn't here…", "if it is away on loan…", "if you can't see it, it may be on loan…" exactly. A wrong condition sends a traveller to the wrong place.
11. QUOTATIONS: many quotes were originally French (Cézanne, Degas, Matisse…), German (Kirchner, Grosz, Dix, Liebermann…), Spanish or other languages.
   - FR and DE: translate the English quote faithfully, introduced the same way.
   - ES: NEVER put your own back-translation of an originally Spanish quote in quotation marks — it would pass as the original.
     Either use the original Spanish wording ONLY if verified verbatim on museothyssen.org (WebFetch), with the URL in your
     notes, or turn it into reported speech without quotation marks. Same applies to FR for originally French quotes and DE for originally German quotes (Kirchner, Grosz, Liebermann…).
12. "The museum says / calls it": keep exactly where the English has it; never add new ones.
13. TTS SAFETY: regnal numbers in words (ES Carlos Tercero, Alfonso Trece; FR Charles trois, Alphonse treize; DE Karl der
   Dritte, Alfons der Dreizehnte). No symbols (& % × °), no abbreviations ("St" → Saint/San/Sankt in full).
14. No ticket prices, opening hours or booking talk.

## Glossary
| English | ES | FR | DE |
|---|---|---|---|
| Museo Nacional Thyssen-Bornemisza / the Thyssen | el Museo Nacional Thyssen-Bornemisza / el Thyssen | le musée national Thyssen-Bornemisza / le Thyssen | das Museo Nacional Thyssen-Bornemisza / das Thyssen |
| Baron Hans Heinrich Thyssen-Bornemisza / Carmen Thyssen | el barón Hans Heinrich Thyssen-Bornemisza / Carmen Thyssen | le baron Hans Heinrich Thyssen-Bornemisza / Carmen Thyssen | Baron Hans Heinrich Thyssen-Bornemisza / Carmen Thyssen |
| the Carmen Thyssen collection | la colección Carmen Thyssen | la collection Carmen Thyssen | die Sammlung Carmen Thyssen |
| the Villahermosa Gallery / palace | la galería Villahermosa / el palacio de Villahermosa | la galerie Villahermosa / le palais de Villahermosa | die Villahermosa-Galerie / der Palacio de Villahermosa |
| the central hall / stairs / lift | el hall central / las escaleras / el ascensor | le hall central / l'escalier / l'ascenseur | die zentrale Halle / die Treppe / der Aufzug |
| on loan to | prestado a | prêté à | ausgeliehen an |
| panel / canvas / oil on canvas | tabla / lienzo / óleo sobre lienzo | panneau / toile / huile sur toile | Tafel / Leinwand / Öl auf Leinwand |
| Extra (short optional track; in @title "Room 7 · Extra · …") | "Sala 7 · Extra · …"; en el texto "un breve Extra" | "Salle 7 · Extra · …" ; « un court Extra » | "Saal 7 · Extra · …"; „ein kurzer Extra-Titel" |
| Henry the Eighth / Charles the Fifth | Enrique Octavo / Carlos Quinto | Henri huit / Charles Quint | Heinrich der Achte / Karl der Fünfte |

## Output
For EACH assigned track write: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/thy_i18n/<lang>/NNN.json
  {"title": "<translated @title>", "where": "<translated @where>", "body": "<spoken body with tags, paragraphs separated by \n\n>"}
@title keeps the English pattern "Room 27 · Artist — Title" (Extras: "Room 7 · Extra · …") with the room word translated
(ES "Sala 27 · Rembrandt — Autorretrato con gorra y dos cadenas" with the museum's Spanish title, FR "Salle 27 · …", DE "Saal 27 · …").
Opening/closing titles have no room. Write with Python json.dump(..., ensure_ascii=False, indent=1).

Self-check before finishing (fix every failure, run again until all your lines are OK):
  python3 /home/claude/audioq/thyssen_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/thy_i18n LANG
Notes: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/thy_i18n/notes/<lang>_<first>-<last>.md
(official Spanish titles you used + URL, every quotation and how you handled it, anything in the English that looked wrong).
Final report ≤ 120 words.
