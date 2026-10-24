# Translation brief — Uffizi Gallery audio guide, Yo Tours 24 Oct 2026 (67 tracks: 53 main stops + 14 short optional Extras) → ES / FR / DE / IT

You translate English audio-guide scripts into ONE target language. The text will be read aloud by a female synthetic
voice (ES: Dalia, Mexican Spanish; FR: Vivienne, France; DE: Katja, Germany; IT: Isabella, Italy) to travellers walking
through the Uffizi Gallery in Florence with headphones. Customers complained that earlier guides sent them to wrong rooms,
so NAVIGATION ACCURACY comes first. DO NOT EDIT ANY EXISTING FILE. Only write your own JSON files, bridge file and notes.

## Source
/home/claude/audioq/uffizi_v5/v5/tracks/NNN.perf.txt — header lines (@title, @where, @what, @sources …), a line `---`, then
the spoken body. The body contains direction tags: [pause] [long pause] [warmly] [quietly] [amused] [curious]
[conspiratorial] [reverent] [wry] [lightly], and *emphasis* marks. Paragraphs are separated by a blank line.
The English is fact-checked against the museum's own pages and independently audited: it is the single source of truth.
@what and @sources give the official title, date and uffizi.it URL. The museum's Italian page of a work is usually the same
slug under https://www.uffizi.it/opere/<slug> (English: /en/artworks/<slug>).
Map (room codes and titles, English): /home/claude/audioq/uffizi_v5/source/map.txt.

## Titles of works
- IT: use the museum's official Italian title (Italian artwork page). Check doubtful ones with WebFetch, one page at a time.
- ES / FR / DE: the established title in that language when there is one (e.g. Primavera, Maestà, la Venus de Urbino /
  la Vénus d'Urbin / die Venus von Urbino), otherwise a faithful translation. Keep Italian names as the museum gives them.
- WebFetch only, one page at a time, never in bursts; never browser tools or curl; if a page asks you to verify you are
  human, stop using it and note the title as unchecked.

## Style model (read before you start)
Approved translations of earlier Yo Tours guides (match their voice; there is no Italian model — use the Spanish and French
as the model for register: warm, spoken, formal address):
- ES: /home/claude/audioq/thyssen_v5/v5/i18n/es/tracks/029.perf.txt, 050.perf.txt
- FR: /home/claude/audioq/thyssen_v5/v5/i18n/fr/tracks/029.perf.txt, 050.perf.txt
- DE: /home/claude/audioq/thyssen_v5/v5/i18n/de/tracks/029.perf.txt, 050.perf.txt
Adapted FOR LISTENING, not translated line by line.

## Rules (all mandatory)
1. FACTS identical to the English: names, dates, numbers, places, sizes, attributions and hedges ("probably", "Vasari tells",
   "if the way is closed…", "the museum says"). Add nothing, drop no fact, don't "improve" a fact. If you think the English
   is wrong, translate it anyway and flag it in your notes.
2. YEARS AS DIGITS: every year in the English must appear as digits. Centuries naturally (IT "il Quattrocento" is fine only
   if the English says "the fifteenth century" — prefer "il XV secolo" written as words: "il quindicesimo secolo").
3. LENGTH: spoken word count ≤ the English; aim about 5% shorter.
4. FOR THE EAR: short sentences (average 9–12 words). No semicolons, no parentheses in speech. At most two dashes per track.
5. ADDRESS: formal — ES usted, FR vous, DE Sie, IT Lei.
6. ES vocabulary neutral for Latin America AND Spain (avoid coger, vale, vosotros, móvil, ordenador).
7. TAGS: every delivery tag in the SAME ORDER and SAME PARAGRAPH as the English. Keep every [pause]/[long pause] and add
   [pause] where a listener needs a breath (typically 3–6 per track). Only these tags.
8. PARAGRAPHS: exactly the same number, same order.
9. NAVIGATION (the last paragraph and every direction anywhere): translate precisely every room code, floor, staircase, lift,
   "back through", "next door", "stay in this room", signs to follow, and what to look for.
   - Room codes exactly as the English, with the room word: ES "la sala A4", FR "la salle A4", DE "Saal A4", IT "la sala A4".
     Codes are letter + number (A4, D23, E4); never change them. NEVER add a code for the Botticelli rooms (the English never
     says A9, A10, A11 or A12 — keep it that way).
   - Floors: "second floor" ES "la segunda planta", FR "le deuxième étage", DE "der zweite Stock", IT "il secondo piano";
     "first floor" ES "la primera planta", FR "le premier étage", DE "der erste Stock", IT "il primo piano";
     "ground floor" ES "la planta baja", FR "le rez-de-chaussée", DE "das Erdgeschoss", IT "il piano terra".
   - Staircases keep their names: Lanzi, Buontalenti, Magliabechi, Granducal/Lorenese (ES "la escalera Lanzi", FR "l'escalier
     Lanzi", DE "die Lanzi-Treppe", IT "lo scalone Lanzi"; same pattern for the others). The Lanzi staircase goes down ONE
     floor only, not to the street: keep that warning exactly.
   - Corridors: Eastern / Southern / Western Corridor → ES "el corredor este / sur / oeste", FR "le corridor est / sud /
     ouest", DE "der Ostkorridor / Südkorridor / Westkorridor", IT "il corridoio di Levante / il corridoio sull'Arno /
     il corridoio di Ponente" (IT: if the Italian pages name them differently, use the museum's Italian names and note it).
   - Named rooms: the Tribune (ES la Tribuna, FR la Tribune, DE die Tribuna, IT la Tribuna); the Niobe Room (ES la sala de
     Níobe, FR la salle de Niobé, DE der Niobe-Saal, IT la sala della Niobe); the Verone (keep "Verone"; IT "il Verone");
     the Vasari Corridor (ES el Corredor Vasariano, FR le corridor de Vasari, DE der Vasari-Korridor, IT il Corridoio
     Vasariano); Contini Bonacossi collection (keep the name). Never say "next track".
10. CONDITIONALS: translate every "if…", "if the way is closed…", "if it is open…", "until early 2027 … on loan" exactly.
    A wrong condition sends a traveller to the wrong place.
11. QUOTATIONS: many quotes were originally Italian (Dante, Vasari, letters, inscriptions), Latin, or other languages.
    - ES / FR / DE: translate the English quote faithfully, introduced the same way.
    - IT: NEVER put your own back-translation of an originally Italian quote in quotation marks — it would pass as the
      original. Use the original Italian wording ONLY if verified verbatim from a reliable source (the museum's Italian page,
      or for Dante a scholarly edition online), with the URL in your notes; otherwise turn it into reported speech without
      quotation marks. Same for FR with originally French quotes, DE with originally German quotes, ES with originally
      Spanish ones.
12. "The museum says / calls it": keep exactly where the English has it; never add new ones.
13. TTS SAFETY: regnal numbers in words (Cosimo the First → ES Cosme Primero / FR Cosme Ier written "Cosme premier" /
    DE Cosimo der Erste / IT Cosimo Primo; Francesco the First, Ferdinando the First, Leo the Tenth etc. the same way).
    No symbols (& % × °), no abbreviations ("St" → San/Saint/Sankt/San in full).
14. No ticket prices, opening hours or booking talk.

## Glossary
| English | ES | FR | DE | IT |
|---|---|---|---|---|
| the Uffizi / the Uffizi Gallery | los Uffizi / la Galería de los Uffizi | les Offices / la galerie des Offices | die Uffizien | gli Uffizi / la Galleria degli Uffizi |
| the Medici / Grand Duke | los Médici / el gran duque | les Médicis / le grand-duc | die Medici / der Großherzog | i Medici / il granduca |
| the Family Pact (1737) | el Pacto de Familia | le Pacte de famille | der Familienpakt | il Patto di famiglia |
| panel / canvas / tempera on panel | tabla / lienzo / temple sobre tabla | panneau / toile / tempera sur bois | Tafel / Leinwand / Tempera auf Holz | tavola / tela / tempera su tavola |
| on loan to | prestado a | prêté à | ausgeliehen an | in prestito a |
| work in progress / closed | en obras / cerrada | en travaux / fermée | wird umgebaut / geschlossen | lavori in corso / chiusa |
| Extra (short optional track; @title "A6 · Extra · …") | "A6 · Extra · …"; en el texto "un breve Extra" | « un court Extra » | „ein kurzer Extra-Titel" | "un breve Extra" |

## Output
For EACH assigned track write: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/uff_i18n/<lang>/NNN.json
  {"title": "<translated @title>", "where": "<translated @where>", "body": "<spoken body with tags, paragraphs separated by \n\n>"}
@title keeps the English pattern: the map code first, unchanged ("A4 · Giotto — Maestà di Ognissanti" in IT with the
museum's Italian title; "D23 · Tiziano — Venere di Urbino"); Botticelli tracks start with the translated "Botticelli rooms"
(ES "Salas de Botticelli · …", FR "Salles Botticelli · …", DE "Botticelli-Säle · …", IT "Sale di Botticelli · …");
Extras keep "· Extra ·". Opening/closing titles have no code. Write with Python json.dump(..., ensure_ascii=False, indent=1).

## Bridges (spoken lines for the shorter versions)
/home/claude/audioq/uffizi_v5/v5/bridges/*.txt holds lines "NNN E>MMM: text" (E = Essential, H = Highlights). Translate
every line whose first number NNN is one of your tracks, into
/tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/uff_i18n/<lang>/bridges_<first>-<last>.txt, same
key, same format, one per line ("NNN E>MMM: <translation>"). Same navigation rules. Start with the equivalent of
"On this shorter tour," (ES "En esta versión corta,", FR "Dans cette version courte,", DE "In dieser Kurzfassung",
IT "In questa versione breve,").

Self-check before finishing (fix every failure, run again until all your lines are OK):
  python3 /home/claude/audioq/uffizi_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/uff_i18n LANG
Notes: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/uff_i18n/notes/<lang>_<first>-<last>.md
(official titles you used + URL, every quotation and how you handled it, anything in the English that looked wrong).
Final report ≤ 120 words.
