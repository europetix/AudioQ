# Translation brief — Catedral de Sevilla and the Giralda audio guide, Yo Tours 30 Oct 2026 (28 tracks incl. short Extras) → ES / FR / DE

You translate English audio-guide scripts into ONE target language. The text will be read aloud by a female synthetic
voice (ES: Dalia, Mexican Spanish; FR: Vivienne, France; DE: Katja, Germany) to travellers walking through Seville Cathedral
and up the Giralda with headphones. Customers complained that earlier guides sent them to wrong places, so NAVIGATION ACCURACY comes
first. DO NOT EDIT ANY EXISTING FILE. Only write your own JSON files, bridge file and notes.

## Source
/home/claude/audioq/cathedral_seville_v5/v5/tracks/NNN.perf.txt — header lines (@title, @where, @what, @sources …), a line `---`, then
the spoken body with direction tags ([pause] [long pause] [warmly] [quietly] [amused] [curious] [conspiratorial] [reverent]
[wry] [lightly]) and *emphasis* marks. Paragraphs are separated by a blank line. The English is fact-checked and independently
audited: it is the single source of truth. Every place is named by its SPANISH NAME as on
the signs (Capilla Mayor, Coro, Sacristía Mayor, Sala Capitular, Patio de los Naranjos, Puerta del Perdón …), with an English
gloss once per track in the English. Keep the Spanish names unchanged in every language (FR/DE may keep the gloss in their
language once). There are NO numbers for places in this guide: never add any. This is a working church with tombs: keep the
respectful tone.

## Style model (read before you start)
Approved translations of earlier Yo Tours guides; match their voice:
- ES: /home/claude/audioq/uffizi_v5/v5/i18n/es/tracks/017.perf.txt, 058.perf.txt
- FR: /home/claude/audioq/uffizi_v5/v5/i18n/fr/tracks/017.perf.txt, 058.perf.txt
- DE: /home/claude/audioq/uffizi_v5/v5/i18n/de/tracks/017.perf.txt, 058.perf.txt
Adapted FOR LISTENING, not translated line by line.

## Rules (all mandatory)
1. FACTS identical to the English: names, dates, numbers, places, sizes, attributions and hedges ("probably", "tradition says",
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
9. NAVIGATION (the last paragraph and every direction anywhere): translate precisely every Spanish place name (unchanged),
   every landmark to look for ("the huge gilded altarpiece behind the iron grille", "the four heralds carrying the coffin"),
   "turn round", "along the aisle", "back towards the great doors", "through the doorway into the courtyard", the Giralda's
   ramps and the one-way rule, and the exit by the Puerta del Perdón with no re-entry. Left/right exactly as the English.
   The Capilla Real is seen from its grille only: keep that exactly. Never say "next track".
10. CONDITIONALS: translate every "if…", "if the way is closed…", "if it is open…", "if the chapel is closed for worship…" exactly.
    A wrong condition sends a traveller to the wrong place.
11. QUOTATIONS: some quotes were originally Spanish (documents, inscriptions, chronicles), Arabic, or other languages.
    - FR / DE: translate the English quote faithfully, introduced the same way.
    - ES: NEVER put your own back-translation of an originally Spanish quote (inscriptions, chronicles, documents, the
      Cabildo's own texts) in quotation marks — it would pass as the original. Use the original Spanish wording ONLY if
      verified verbatim from a reliable source (catedraldesevilla.es pages/PDFs or a scholarly edition), with the URL in your
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
| Seville Cathedral / the cathedral | la Catedral de Sevilla / la catedral | la cathédrale de Séville | die Kathedrale von Sevilla |
| the Giralda / the Giraldillo | la Giralda / el Giraldillo | la Giralda / le Giraldillo | die Giralda / der Giraldillo |
| the ramps / the bell level | las rampas / el cuerpo de campanas | les rampes / l'étage des cloches | die Rampen / die Glockenstube |
| the Capilla Mayor / the Retablo Mayor | la Capilla Mayor / el Retablo Mayor | la Capilla Mayor / le Retablo Mayor (grand retable) | die Capilla Mayor / der Retablo Mayor (Hochaltar) |
| the choir (Coro) | el coro | le chœur (Coro) | der Chor (Coro) |
| Columbus's tomb | el sepulcro de Cristóbal Colón | le tombeau de Christophe Colomb | das Grabmal des Christoph Kolumbus |
| the great sacristy / chapter house | la Sacristía Mayor / la Sala Capitular | la Sacristía Mayor / la salle capitulaire | die Sacristía Mayor / der Kapitelsaal |
| on this shorter tour | en esta versión corta | dans cette version courte | in dieser Kurzfassung |
| Extra (short optional track) | un breve Extra | un court Extra | ein kurzer Extra-Titel |

## Output
For EACH assigned track write: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/cat_i18n/<lang>/NNN.json
  {"title": "<translated @title>", "where": "<translated @where>", "body": "<spoken body with tags, paragraphs separated by \n\n>"}
@title keeps the English pattern: the Spanish space name first, unchanged ("Capilla Mayor — El Retablo Mayor"); Extras keep
"<Spanish name> · Extra · …". The opening title has no space name. Write with Python json.dump(..., ensure_ascii=False, indent=1).

## Bridges (spoken lines for the shorter versions)
/home/claude/audioq/cathedral_seville_v5/v5/bridges/*.txt holds lines "NNN E>MMM: text" (E = Essential, H = Highlights). Translate
every line whose first number NNN is one of your tracks, into
/tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/cat_i18n/<lang>/bridges_<first>-<last>.txt, same
key, same format, one per line ("NNN E>MMM: <translation>"). Same navigation rules. Start with the equivalent of
"On this shorter tour," (ES "En esta versión corta,", FR "Dans cette version courte,", DE "In dieser Kurzfassung").

Self-check before finishing (fix every failure, run again until all your lines are OK):
  python3 /home/claude/audioq/cathedral_seville_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/cat_i18n LANG
Notes: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/cat_i18n/notes/<lang>_<first>-<last>.md
(official titles you used + URL, every quotation and how you handled it, anything in the English that looked wrong).
Final report ≤ 120 words.
