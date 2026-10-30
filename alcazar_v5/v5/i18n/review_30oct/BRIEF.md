# Translation brief — Real Alcázar de Sevilla audio guide, Yo Tours 30 Oct 2026 (35 tracks: 33 in the walking order incl. Extras, plus 2 optional Cuarto Real Alto Extras) → ES / FR / DE

You translate English audio-guide scripts into ONE target language. The text will be read aloud by a female synthetic
voice (ES: Dalia, Mexican Spanish; FR: Vivienne, France; DE: Katja, Germany) to travellers walking through the Real Alcázar
de Sevilla with headphones. Customers complained that earlier guides sent them to wrong places, so NAVIGATION ACCURACY comes
first. DO NOT EDIT ANY EXISTING FILE. Only write your own JSON files, bridge file and notes.

## Source
/home/claude/audioq/alcazar_v5/v5/tracks/NNN.perf.txt — header lines (@title, @where, @what, @sources …), a line `---`, then
the spoken body with direction tags ([pause] [long pause] [warmly] [quietly] [amused] [curious] [conspiratorial] [reverent]
[wry] [lightly]) and *emphasis* marks. Paragraphs are separated by a blank line. The English is fact-checked and independently
audited: it is the single source of truth. Every place is named by its NUMBER on the Alcázar's own map (the official leaflet,
1–53) and its SPANISH NAME, exactly as printed on the leaflet: /home/claude/audioq/alcazar_v5/research/VISIT_ROUTE_AND_SPACES_OCT2026.md
(legend table). Keep the numbers and the Spanish names unchanged in every language (they are what visitors read on site).

## Style model (read before you start)
Approved translations of earlier Yo Tours guides; match their voice:
- ES: /home/claude/audioq/uffizi_v5/v5/i18n/es/tracks/017.perf.txt, 058.perf.txt
- FR: /home/claude/audioq/uffizi_v5/v5/i18n/fr/tracks/017.perf.txt, 058.perf.txt
- DE: /home/claude/audioq/uffizi_v5/v5/i18n/de/tracks/017.perf.txt, 058.perf.txt
Adapted FOR LISTENING, not translated line by line.

## Rules (all mandatory)
1. FACTS identical to the English: names, dates, numbers, places, sizes, attributions and hedges ("probably", "Vasari tells",
   "if the way is closed…", "the museum says"). Add nothing, drop no fact, don't "improve" a fact. If you think the English
   is wrong, translate it anyway and flag it in your notes.
2. YEARS AS DIGITS: every year in the English must appear as digits. Centuries in words (ES "el siglo catorce",
   FR « le quatorzième siècle », DE „das vierzehnte Jahrhundert") — no Roman numerals in speech.
3. LENGTH: spoken word count ≤ the English; aim about 5% shorter.
4. FOR THE EAR: short sentences (average 9–12 words). No semicolons, no parentheses in speech. At most two dashes per track.
5. ADDRESS: formal — ES usted, FR vous, DE Sie.
6. ES vocabulary neutral for Latin America AND Spain (avoid coger, vale, vosotros, móvil, ordenador).
7. TAGS: every delivery tag in the SAME ORDER and SAME PARAGRAPH as the English. Keep every [pause]/[long pause] and add
   [pause] where a listener needs a breath (typically 3–6 per track). Only these tags.
8. PARAGRAPHS: exactly the same number, same order.
9. NAVIGATION (the last paragraph and every direction anywhere): translate precisely every map number, Spanish place name,
   "through the triple arch", "keep the palace front on your right", "back the way you came", "follow the Salida signs", and
   what to look for. Numbers: ES "el número 15 del mapa del Alcázar, el Salón de los Embajadores", FR « le numéro 15 du plan de
   l'Alcázar, le Salón de los Embajadores », DE „Nummer 15 auf dem Alcázar-Plan, der Salón de los Embajadores" (first mention;
   afterwards "el número 15", « le numéro 15 », „Nummer 15"). Never change a number; never say "number 11". The Cuarto Real Alto
   is a separate timed visit: keep that wording exactly. Never say "next track".
10. CONDITIONALS: translate every "if…", "if the way is closed…", "if it is open…", "if the pavilion is still behind screens…" exactly.
    A wrong condition sends a traveller to the wrong place.
11. QUOTATIONS: some quotes were originally Spanish (documents, inscriptions, chronicles), Arabic, or other languages.
    - FR / DE: translate the English quote faithfully, introduced the same way.
    - ES: NEVER put your own back-translation of an originally Spanish quote (inscriptions, chronicles, documents, the
      Alcázar's own texts) in quotation marks — it would pass as the original. Use the original Spanish wording ONLY if
      verified verbatim from a reliable source (alcazarsevilla.org pages/PDFs or a scholarly edition), with the URL in your
      notes; otherwise turn it into reported speech without quotation marks. Arabic inscriptions: keep the English rendering
      translated faithfully, introduced the same way. Same for FR with originally French quotes, DE with originally German.
12. "The museum says / calls it": keep exactly where the English has it; never add new ones.
13. TTS SAFETY: regnal numbers in words (Charles the Fifth → ES Carlos Quinto / FR Charles Quint / DE Karl der Fünfte;
    Pedro the First → ES Pedro Primero / FR Pierre Ier written "Pierre premier" / DE Peter der Erste; Felipe Segundo etc.;
    in Spanish space names keep the name as spoken: "Salón del Techo de Carlos Quinto").
    No symbols (& % × °), no abbreviations ("St" → San/Saint/Sankt/San in full).
14. No ticket prices, opening hours or booking talk.

## Glossary
| English | ES | FR | DE |
|---|---|---|---|
| the Real Alcázar / the Alcázar | el Real Alcázar / el Alcázar | le Real Alcázar / l'Alcázar | der Real Alcázar / der Alcázar |
| the Alcázar map (official leaflet) | el mapa del Alcázar | le plan de l'Alcázar | der Alcázar-Plan |
| King Pedro / Pedro the First | el rey don Pedro / Pedro Primero | le roi Pierre Ier ("Pierre premier") | König Peter der Erste / König Pedro |
| Almohad / Mudéjar / Gothic palace | almohade / mudéjar / Palacio Gótico | almohade / mudéjar / palais gothique | almohadisch / Mudéjar- / Gotischer Palast |
| the Cuarto Real Alto (separate timed visit) | el Cuarto Real Alto (visita aparte con horario) | le Cuarto Real Alto (visite séparée à horaire fixe) | der Cuarto Real Alto (eigene Besichtigung mit Zeitfenster) |
| on this shorter tour | en esta versión corta | dans cette version courte | in dieser Kurzfassung |
| Extra (short optional track) | un breve Extra | un court Extra | ein kurzer Extra-Titel |

## Output
For EACH assigned track write: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/alc_i18n/<lang>/NNN.json
  {"title": "<translated @title>", "where": "<translated @where>", "body": "<spoken body with tags, paragraphs separated by \n\n>"}
@title keeps the English pattern: the leaflet number and the Spanish space name first, unchanged ("15 · Salón de los
Embajadores — La cúpula de 1427"); Extras keep "· Extra ·"; Cuarto Real Alto Extras keep "CRA 20 · Extra · …". The opening
title has no number. Write with Python json.dump(..., ensure_ascii=False, indent=1).

## Bridges (spoken lines for the shorter versions)
/home/claude/audioq/alcazar_v5/v5/bridges/*.txt holds lines "NNN E>MMM: text" (E = Essential, H = Highlights). Translate
every line whose first number NNN is one of your tracks, into
/tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/alc_i18n/<lang>/bridges_<first>-<last>.txt, same
key, same format, one per line ("NNN E>MMM: <translation>"). Same navigation rules. Start with the equivalent of
"On this shorter tour," (ES "En esta versión corta,", FR "Dans cette version courte,", DE "In dieser Kurzfassung").

Self-check before finishing (fix every failure, run again until all your lines are OK):
  python3 /home/claude/audioq/alcazar_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/alc_i18n LANG
Notes: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/alc_i18n/notes/<lang>_<first>-<last>.md
(official titles you used + URL, every quotation and how you handled it, anything in the English that looked wrong).
Final report ≤ 120 words.
