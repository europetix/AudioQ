# Translation brief — Museo del Prado audio guide, Yo Tours 10 Oct 2026 (81 tracks: 59 main stops + 22 short optional Extras) → ES / FR / DE

You translate English audio-guide scripts into ONE target language. The text will be read aloud by a female
synthetic voice (ES: Dalia, Mexican Spanish; FR: Vivienne, France; DE: Katja, Germany) to travellers walking through
the Museo del Prado in Madrid with headphones. Customers complained that the previous guide sent them to wrong rooms,
so NAVIGATION ACCURACY comes first. DO NOT EDIT ANY EXISTING FILE. Only write your own JSON files and your notes file.

## Source
/home/claude/audioq/prado_v5/v5/tracks/NNN.perf.txt — header lines (@title, @where, @what, @sources …), a line `---`, then
the spoken body. The body contains direction tags: [pause] [long pause] [warmly] [quietly] [amused] [curious]
[conspiratorial] [reverent] [wry] [lightly], and *emphasis* marks. Paragraphs are separated by a blank line.
The English is fact-checked against the museum's own pages: it is the single source of truth. @what and @sources give the
official title, date and URL on museodelprado.es. The museum's Spanish page is the same URL without "/en"
(…/en/the-collection/art-work/… → …/coleccion/obra-de-arte/…; or search the Spanish title) — ES uses the museum's official
Spanish title (Las meninas, La rendición de Breda, La fragua de Vulcano, El triunfo de Baco …); check them with WebFetch,
one page at a time (never in bursts; never browser tools or curl). FR/DE translate titles naturally, using the
established title in that language when there is one (FR Les Ménines, DE Las Meninas / Die Hoffräulein — keep one form).

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
   "stay in this room", signs to follow, and what to look for. Room numbers as digits with letters spaced for the voice:
   ES "la sala 55 A", FR "la salle 55 A", DE "Saal 55 A" (Room 12 → sala 12 / salle 12 / Saal 12; Room 1 → sala 1).
   Floors: ES "la planta 0 / 1 / 2", FR "le niveau 0 / 1 / 2", DE "Ebene 0 / 1 / 2". "Shown at its doorway" →
   ES "indicado en la puerta", FR "indiqué à l'entrée de la salle", DE "am Eingang angeschrieben". Never say "next track".
10. CONDITIONALS: translate every "if…", "if it isn't here…", "if the stairs stop at Floor 1…", "if the Goya rooms are being
   rehung…" exactly. A wrong condition sends a traveller to the wrong place.
11. QUOTATIONS: many quotes were originally Spanish (Palomino, Philip IV, Goya…) or other languages.
   - FR and DE: translate the English quote faithfully, introduced the same way.
   - ES: NEVER put your own back-translation of an originally Spanish quote in quotation marks — it would pass as the original.
     Either use the original Spanish wording ONLY if verified verbatim on museodelprado.es (WebFetch), with the URL in your
     notes, or turn it into reported speech without quotation marks. Same applies to FR for originally French quotes.
12. "The museum says / calls it": keep exactly where the English has it; never add new ones.
13. TTS SAFETY: regnal numbers in words (ES Felipe Cuarto, Carlos Quinto, Carlos Cuarto; FR Philippe IV → Philippe quatre,
   Charles Quint, Charles quatre; DE Philipp der Vierte / Philipps des Vierten, Karl der Fünfte, Karl der Vierte). No symbols
   (& % × °), no abbreviations ("St" → Saint/San/Sankt in full).
14. No ticket prices, opening hours or booking talk.

## Glossary
| English | ES | FR | DE |
|---|---|---|---|
| Museo del Prado / the Prado | el Museo del Prado / el Prado | le musée du Prado / le Prado | das Museo del Prado / der Prado |
| Jerónimos entrance (hall) | el vestíbulo de la entrada de los Jerónimos | le hall de l'entrée des Jerónimos | die Eingangshalle am Jerónimos-Eingang |
| Goya entrance / Murillo entrance / Velázquez entrance | la entrada de Goya / de Murillo / de Velázquez | l'entrée Goya / Murillo / Velázquez | der Goya-/Murillo-/Velázquez-Eingang |
| the Central Gallery | la Galería Central | la Galerie centrale | die Zentralgalerie |
| the Room of the Muses | la Sala de las Musas | la salle des Muses | der Saal der Musen |
| the round Room 1 / 51 | la sala redonda 1 / 51 (la rotonda) | la salle ronde 1 / 51 (la rotonde) | der runde Saal 1 / 51 (die Rotunde) |
| the Dauphin's Treasure | el Tesoro del Delfín | le Trésor du Dauphin | der Dauphin-Schatz |
| the Black Paintings | las Pinturas negras | les Peintures noires | die Schwarzen Gemälde (Pinturas negras) |
| tapestry cartoons | los cartones para tapices | les cartons de tapisserie | die Teppichkartons (Entwürfe für Wandteppiche) |
| Las Meninas | Las meninas | Les Ménines | Las Meninas |
| The Spinners | Las hilanderas | Les Fileuses | Die Spinnerinnen |
| The Feast of Bacchus / Los Borrachos | El triunfo de Baco / Los borrachos | Le Triomphe de Bacchus / Les Buveurs | Der Triumph des Bacchus / Die Trinker |
| The Surrender of Breda | La rendición de Breda / Las lanzas | La Reddition de Breda / Les Lances | Die Übergabe von Breda / Die Lanzen |
| The Garden of Earthly Delights | El jardín de las delicias | Le Jardin des délices | Der Garten der Lüste |
| The 2nd / 3rd of May 1808 | El 2 de mayo de 1808 / El 3 de mayo de 1808 (Los fusilamientos) | Le Deux Mai 1808 / Le Trois Mai 1808 | Der 2. Mai 1808 / Der 3. Mai 1808 — write "Der zweite Mai 1808" in speech |
| The Naked / Clothed Maja | La maja desnuda / La maja vestida | La Maja nue / La Maja vêtue | Die nackte Maja / Die bekleidete Maja |
| canvas / panel / altarpiece / triptych | lienzo / tabla / retablo / tríptico | toile / panneau / retable / triptyque | Leinwand / Tafel / Altarbild / Triptychon |
| buffoon / court dwarf | bufón / enano de la corte | bouffon / nain de cour | Hofnarr / Hofzwerg |
| Infanta | la infanta | l'infante | die Infantin |
| Extra (a short optional track; in @title "Room 41 · Extra · …") | Extra (título: "Sala 41 · Extra · …"); en el texto: "una pista Extra", "un breve Extra" | Extra (titre : "Salle 41 · Extra · …") ; dans le texte : "une piste Extra", "un court Extra" | Extra (Titel: "Saal 41 · Extra · …"); im Text: "ein kurzer Extra-Titel" |
| Philip IV / Charles V / Charles IV | Felipe Cuarto / Carlos Quinto / Carlos Cuarto | Philippe quatre / Charles Quint / Charles quatre | Philipp der Vierte / Karl der Fünfte / Karl der Vierte |

## Output
For EACH assigned track write: /tmp/claude-0/-home-claude-audioq/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/prado_i18n/<lang>/NNN.json
  {"title": "<translated @title>", "where": "<translated @where>", "body": "<spoken body with tags, paragraphs separated by \n\n>"}
@title keeps the English pattern "Room 12 · Artist — Title" (Extras: "Room 41 · Extra · Artist — Title") with the room word translated (ES "Sala 12 · Velázquez — Las meninas",
FR "Salle 12 · …", DE "Saal 12 · …"); opening/closing titles have no room. Write with Python json.dump(..., ensure_ascii=False, indent=1).

Self-check before finishing (fix every failure, run again until all your lines are OK):
  python3 /home/claude/audioq/prado_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude-audioq/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/prado_i18n LANG
Notes: /tmp/claude-0/-home-claude-audioq/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/prado_i18n/notes/<lang>_<first>-<last>.md
(official Spanish titles you used + URL, every quotation and how you handled it, anything in the English that looked wrong).
Final report ≤ 120 words.
