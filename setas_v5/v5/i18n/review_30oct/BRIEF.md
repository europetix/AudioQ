# Translation brief — Setas de Sevilla (Metropol Parasol) and the Antiquarium audio guide, Yo Tours 30 Oct 2026 (18 tracks incl. 2 short Extras) → ES / FR / DE

You translate English audio-guide scripts into ONE target language. The text will be read aloud by a female synthetic
voice (ES: Dalia, Mexican Spanish; FR: Vivienne, France; DE: Katja, Germany) to travellers visiting the Setas de Sevilla with
headphones: the Antiquarium (Roman and Moorish remains) at level minus one, the lifts, the walkways and the Mirador 360º on top,
the way down past an exhibition, and the Plaza Mayor above the market. Customers complained that earlier guides sent them to
wrong places, so NAVIGATION ACCURACY comes first. DO NOT EDIT ANY EXISTING FILE. Only write your own JSON files, bridge file
and notes.

## Source
/home/claude/audioq/setas_v5/v5/tracks/NNN.perf.txt — header lines (@title, @where, @what, @sources …), a line `---`, then
the spoken body with direction tags ([pause] [long pause] [warmly] [quietly] [amused] [curious] [conspiratorial] [reverent]
[wry] [lightly]) and *emphasis* marks. Paragraphs are separated by a blank line. The English is fact-checked and independently
audited: it is the single source of truth. Places are named as on the signs: Antiquarium, Plaza de la Encarnación, Mercado de
la Encarnación, Mirador 360º, Plaza Mayor, Feeling Sevilla, Aurora, the Roman houses (Casa de la Columna, Casa de Baco …),
the taquilla. Keep these names unchanged in every language (FR/DE may keep a gloss in their language once, as the English
does). "The walkway(s)" and "the lifts" are translated (glossary). There are NO numbers for places in this guide: never add
any. Levels are spoken as words ("level minus one").

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
9. NAVIGATION (the last paragraph and every direction anywhere): translate precisely every place name (unchanged), every
   landmark to look for ("with the Giralda on your left", "the steps up to the Mirador", "the lifts beside its entrance",
   "the big raised square under the parasols"), every "go down", "go up", "walk on along the walkway", "as the doors
   close", and the way out from the Plaza Mayor. Left/right, south/west and up/down exactly as the English. Never say
   "next track".
10. CONDITIONALS: translate every "if…", "if the Antiquarium is closed…", "if you're going into the film…", "if you can see…" exactly.
    A wrong condition sends a traveller to the wrong place.
11. QUOTATIONS: some quotes were originally Spanish (press quotes, the Mayor, local sayings), German (Fraunhofer, some of Mayer's words), Finnish, or other languages.
    - FR / DE: translate the English quote faithfully, introduced the same way.
    - ES: NEVER put your own back-translation of an originally Spanish quote (the Mayor, a local saying, Spanish press,
      official Spanish texts) in quotation marks — it would pass as the original. Use the original Spanish wording ONLY if
      verified verbatim from a reliable source (the original Spanish article or official page), with the URL in your
      notes; otherwise turn it into reported speech without quotation marks. Same for FR with originally French quotes, DE with originally German.
12. "The museum says / calls it": keep exactly where the English has it; never add new ones.
13. TTS SAFETY: no symbols (& % × ° º ²) in the spoken BODY or bridges. The name "Mirador 360º" stays as it is in @title
    and @where, but in the body and bridges write it as it is said: ES "Mirador trescientos sesenta", FR « Mirador trois
    cent soixante », DE „Mirador dreihundertsechzig“. Other "360º": write the words
    (ES "trescientos sesenta grados" / FR « à trois cent soixante degrés » / DE „Dreihundertsechzig-Grad-“). Amounts in words
    for the unit ("millones de euros", « millions d'euros », „Millionen Euro“), metres in words. Regnal numbers in words
    (Felipe Segundo / Philippe II written "Philippe deux" / Philipp der Zweite). No abbreviations ("St" in full; "AD" → ES
    "después de Cristo", FR « après J.-C. » written "après Jésus-Christ", DE „nach Christus“).
14. No ticket prices, opening hours or booking talk.

## Glossary
| English | ES | FR | DE |
|---|---|---|---|
| the Setas / Metropol Parasol | las Setas / el Metropol Parasol | les Setas / le Metropol Parasol | die Setas / der Metropol Parasol |
| the mushrooms (nickname) | las setas | les champignons | die Pilze |
| the parasols | los parasoles | les parasols | die Schirme |
| the walkway(s) | la pasarela / las pasarelas | la passerelle / les passerelles | der Rundweg / die Stege |
| the lifts | los ascensores | les ascenseurs | die Aufzüge |
| level minus one | la planta menos uno | le niveau moins un | die Ebene minus eins |
| the Mirador 360º / the highest point | el Mirador 360º / el punto más alto | le Mirador 360º / le point le plus haut | der Mirador 360º / der höchste Punkt |
| the Antiquarium | el Antiquarium | l'Antiquarium | das Antiquarium |
| the Plaza Mayor (raised square) | la Plaza Mayor | la Plaza Mayor | die Plaza Mayor |
| the market | el mercado | le marché | die Markthalle |
| laminated veneer lumber | madera microlaminada | bois lamellé-placage (LVL) | Furnierschichtholz |
| the Almohads / Almohad | los almohades / almohade | les Almohades / almohade | die Almohaden / almohadisch |
| on this shorter tour | en esta versión corta | dans cette version courte | in dieser Kurzfassung |
| Extra (short optional track) | un breve Extra | un court Extra | ein kurzer Extra-Titel |
| the full tour / essential / highlights | el recorrido completo / la versión esencial / los imprescindibles | la visite complète / la version essentielle / la version des temps forts | die vollständige Tour / die Kernversion / die Highlights |

## Output
For EACH assigned track write: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/set_i18n/<lang>/NNN.json
  {"title": "<translated @title>", "where": "<translated @where>", "body": "<spoken body with tags, paragraphs separated by \n\n>"}
@title keeps the English pattern: the place first ("Antiquarium — …", "Mirador 360º — …"; "Walkway" and "The way down"
are translated with the glossary); Extras keep "<place> · Extra · …". The opening title has no place. Write with Python json.dump(..., ensure_ascii=False, indent=1).

## Bridges (spoken lines for the shorter versions)
/home/claude/audioq/setas_v5/v5/bridges/*.txt holds lines "NNN E>MMM: text" (E = Essential, H = Highlights). Translate
every line whose first number NNN is one of your tracks, into
/tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/set_i18n/<lang>/bridges_<first>-<last>.txt, same
key, same format, one per line ("NNN E>MMM: <translation>"). Same navigation rules. Start with the equivalent of
"On this shorter tour," (ES "En esta versión corta,", FR "Dans cette version courte,", DE "In dieser Kurzfassung").

Self-check before finishing (fix every failure, run again until all your lines are OK):
  python3 /home/claude/audioq/setas_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/set_i18n LANG
Notes: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/set_i18n/notes/<lang>_<first>-<last>.md
(official titles you used + URL, every quotation and how you handled it, anything in the English that looked wrong).
Final report ≤ 120 words.
