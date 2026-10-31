# Translation brief — Guggenheim Museum Bilbao: the building and its permanent works, Yo Tours 31 Oct 2026 (29 tracks incl. 4 short Extras) → ES / FR / DE

You translate English audio-guide scripts into ONE target language. The text will be read aloud by a female synthetic
voice (ES: Dalia, Mexican Spanish; FR: Vivienne, France; DE: Katja, Germany) to travellers at the Guggenheim Bilbao with
headphones: the plaza with Puppy, the plaque for Txema Agirre, the stairway down, ZERO, the Atrium, Holzer, Serra's eight
sculptures in gallery 104, the terrace, the balconies on floors 2 and 3, then outside along the river walk to the pond,
Maman, the titanium and La Salve Bridge. Customers complained that earlier guides sent them to wrong places, so NAVIGATION
ACCURACY comes first. DO NOT EDIT ANY EXISTING FILE. Only write your own JSON files, bridge file and notes.

## Source
/home/claude/audioq/guggenheim_v5/v5/tracks/NNN.perf.txt — header lines (@title, @where, @what, @sources …), a line `---`,
then the spoken body with direction tags ([pause] [long pause] [warmly] [quietly] [amused] [curious] [conspiratorial]
[reverent] [wry] [lightly]) and *emphasis* marks. Paragraphs are separated by a blank line. The English is fact-checked
and independently audited twice: it is the single source of truth. Work titles: use the official title in your language
ONLY if the museum's own Spanish/French pages use it (e.g. ES "Mamá"? NO — the museum keeps "Maman"; Puppy stays "Puppy";
"The Matter of Time" → ES "La materia del tiempo" as on guggenheim-bilbao.eus/es; DE/FR: keep the English title or the
museum's own translation if it has one). Check titles you are unsure of on the museum's own EN/ES/FR pages (WebFetch, one
page at a time, never bursts, no curl/browser, never a CAPTCHA) and list them in your notes. Basque names stay Basque
(Guggenheim Bilbao Museoa, Arku gorriak, Besarkada, Txema Agirre, Ertzaintza, Abandoibarra, Artxanda, Lehendakari).
Track 003 (Txema Agirre) is a memorial: short sentences, plain, respectful.

## Style model (read before you start)
Approved translations of earlier Yo Tours guides; match their voice:
- ES: /home/claude/audioq/setas_v5/v5/i18n/es/tracks/009.perf.txt, 014.perf.txt
- FR: /home/claude/audioq/setas_v5/v5/i18n/fr/tracks/009.perf.txt, 014.perf.txt
- DE: /home/claude/audioq/setas_v5/v5/i18n/de/tracks/009.perf.txt, 014.perf.txt
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
9. NAVIGATION (the last paragraph and every direction anywhere): translate precisely every place and gallery (gallery 104,
   the balcony opposite gallery 204/304, the Atrium, the Hall, ZERO, the terrace, the river walk, the pond, La Salve
   Bridge), every landmark to look for ("the long gallery that runs under the bridge", "the giant spider by the footbridge",
   "the tall tree of silver balls", "the red frame on the bridge"), every "go down", "go up", "glass lift", "the broad
   stairway", "back to the Atrium", and both exit variants in 021 exactly. Never say "next track". Gallery numbers as
   digits in @title/@where; in speech write them as the voice should say them in your language (ES "la sala ciento cuatro",
   FR « la salle cent quatre », DE „Saal hundertvier“ / „Galerie 104" read as „hundertvier"), consistently.
10. CONDITIONALS: translate every "if…", "if you're on the full tour…", "if he's half-dressed today…", "if the fog is running…", "if you can see the spider…" exactly.
    A wrong condition sends a traveller to the wrong place.
11. QUOTATIONS: most quotes were originally English (Gehry, Krens, Koons, Serra as printed by the museum, Holzer, Bourgeois as printed, AP). Some were originally Spanish (a museum spokeswoman to El Independiente: «No es así»; Ferrovial's works manager; the Basque painter to AP; the museum's Spanish pages), French (Klein, Bourgeois's own texts may be French) or Japanese (Nakaya).
    - FR / DE: translate the English quote faithfully, introduced the same way.
    - ES: NEVER put your own back-translation of an originally Spanish quote (Spanish press, the museum's Spanish pages,
      Ferrovial) in quotation marks — it would pass as the original. Use the original Spanish wording ONLY if
      verified verbatim from a reliable source (the original Spanish article or official page), with the URL in your
      notes; otherwise turn it into reported speech without quotation marks. Same for FR with originally French quotes, DE with originally German.
12. "The museum says / calls it": keep exactly where the English has it; never add new ones.
13. TTS SAFETY: no symbols (& % × ° º # ²) in the spoken BODY or bridges. Numbers that a voice could misread in words
    (metres, "fifty-five metres", "a third of a millimetre"). Amounts in words for the unit ("millones de dólares",
    « millions de dollars », „Millionen Dollar"). F.O.G. spoken as letters (ES "efe, o, ge" / FR « F, O, G » / DE „F, O, G");
    "Expo 70" written so the voice says the year; Chillida's titles in speech as "Consejo al espacio cinco", « Conseil à
    l'espace cinq », „Rat an den Raum fünf" etc. only if the English gives an English title — keep the English title the
    English uses, with numbers spoken in words. No abbreviations.
14. No ticket prices, opening hours or booking talk.

## Glossary
| English | ES | FR | DE |
|---|---|---|---|
| the Atrium / the Hall | el atrio / el vestíbulo (Hall) | l'atrium / le hall | das Atrium / die Eingangshalle |
| gallery 104 | la sala 104 | la salle 104 | Saal 104 |
| the balcony opposite gallery 204 | el balcón frente a la sala 204 | le balcon face à la salle 204 | der Balkon gegenüber Saal 204 |
| the terrace | la terraza | la terrasse | die Terrasse |
| the river walk | el paseo de la ría | la promenade le long de la ría / du fleuve | die Uferpromenade |
| the pond | el estanque | le bassin | das Wasserbecken |
| the plaza | la plaza | le parvis / la place | der Vorplatz |
| La Salve Bridge | el puente de La Salve | le pont de La Salve | die La-Salve-Brücke |
| weathering steel | acero corten (acero patinable) | acier Corten (acier autopatinable) | wetterfester Stahl (Cortenstahl) |
| torqued | torsionado | torsadé | verdreht / tordiert |
| on this shorter tour | en esta versión corta | dans cette version courte | in dieser Kurzfassung |
| Extra (short optional track) | un breve Extra | un court Extra | ein kurzer Extra-Titel |
| the full tour / essential / highlights | el recorrido completo / la versión esencial / los imprescindibles | la visite complète / la version essentielle / la version des temps forts | die vollständige Tour / die Kernversion / die Highlights |

## Output
For EACH assigned track write: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/gug_i18n/<lang>/NNN.json
  {"title": "<translated @title>", "where": "<translated @where>", "body": "<spoken body with tags, paragraphs separated by \n\n>"}
@title keeps the English pattern: the place first ("Gallery 104 — …" → "Sala 104 — …"); Extras keep "<place> · Extra · …".
Write with Python json.dump(..., ensure_ascii=False, indent=1).

## Bridges (spoken lines for the shorter versions)
/home/claude/audioq/guggenheim_v5/v5/bridges/*.txt holds lines "NNN E>MMM: text" (E = Essential, H = Highlights). Translate
every line into /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/gug_i18n/<lang>/bridges_001-029.txt, same key, same format, one per line. Same navigation rules. Start
with the equivalent of "On this shorter tour," (ES "En esta versión corta,", FR "Dans cette version courte,", DE "In dieser
Kurzfassung"). Not longer than the English.

Self-check before finishing (fix every failure, run again until all lines are OK):
  python3 /home/claude/audioq/guggenheim_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/gug_i18n LANG
Notes: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/gug_i18n/notes/<lang>_001-029.md (official titles you used + URL, every quotation and how you handled it,
anything in the English that looked wrong). Final report ≤ 120 words.
