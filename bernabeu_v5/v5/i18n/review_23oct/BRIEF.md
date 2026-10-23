# Translation brief — Estadio Santiago Bernabéu (Tour Bernabéu) audio guide, Yo Tours 23 Oct 2026 (28 tracks: 23 main + 5 Extras) → ES / FR / DE

You translate English audio-guide scripts into ONE target language. The text will be read aloud by a female synthetic voice
(ES: Dalia, Mexican Spanish; FR: Vivienne, France; DE: Katja, Germany) to visitors walking the Tour Bernabéu, Real Madrid's
stadium in Madrid, with headphones. Directions come first: the tour has no stop numbers and few signs, so every "where to go
next" and every "if the dressing room is closed today…" must be exact. DO NOT EDIT ANY EXISTING FILE. Only write your own
JSON files and your notes file.

## Source
/home/claude/audioq/bernabeu_v5/v5/tracks/NNN.perf.txt — header (@title, @where, @what, @sources …), a line `---`, then the
spoken body with direction tags [pause] [long pause] [warmly] [quietly] [amused] [curious] [conspiratorial] [reverent] [wry]
[lightly] and *emphasis*. Paragraphs are separated by a blank line. The English is fact-checked (sources in @sources and in
/home/claude/audioq/bernabeu_v5/research/): it is the single source of truth.

## Style model (read before you start) — approved translations of our earlier guides; match their voice
- ES: /home/claude/audioq/reina_v5/v5/i18n/es/tracks/023.perf.txt  - FR: /home/claude/audioq/reina_v5/v5/i18n/fr/tracks/023.perf.txt
- DE: /home/claude/audioq/reina_v5/v5/i18n/de/tracks/023.perf.txt
Adapted FOR LISTENING, not translated line by line. Football language natural for fans in your language.

## Rules (all mandatory)
1. FACTS identical to the English: names, dates, scores, minutes, counts, money, hedges ("the story goes", "as of autumn
   2026", "according to the club"). Add nothing, drop nothing. If the English looks wrong, translate it and flag it in notes.
2. YEARS AS DIGITS: every year in the English appears as digits ("1947", "la temporada 1931-1932" is fine as words+digits).
3. LENGTH: spoken word count ≤ the English; aim about 5% shorter.
4. FOR THE EAR: short sentences (average 9–12 words). No semicolons, no parentheses in speech, at most two dashes per track.
   Scores in words as in the English ("dos a cero", "deux buts à zéro", "zwei zu null"); never "2-0".
5. ADDRESS: formal — ES usted, FR vous, DE Sie.
6. ES vocabulary neutral for Latin America AND Spain (avoid coger, vale, vosotros, móvil, ordenador). Football terms as
   used by the club: Copa de Europa, Liga, Copa del Rey, Balón de Oro, vestuario, banquillos, palco (not on this tour).
7. TAGS: every delivery tag in the SAME ORDER and SAME PARAGRAPH as the English. Keep every [pause]/[long pause].
8. PARAGRAPHS: exactly the same number, same order.
9. DIRECTIONS (last paragraph and every "if… play number…"): translate every zone, every condition and every number exactly.
   "play number twenty-three" → ES "reproduzca el número veintitrés", FR "écoutez le numéro vingt-trois",
   DE "spielen Sie Nummer dreiundzwanzig" (numbers in words, as in the English). Never say "pista siguiente / piste suivante /
   nächster Titel".
10. CONDITIONALS: "if the dressing room and benches are closed today", "if you came into the museum before the view",
   "if it's open today" — exactly. A wrong condition sends a visitor to the wrong place.
11. QUOTATIONS: many quotes were originally Spanish (Real Madrid, Valdano, Bernabéu…).
   - ES: NEVER put your own back-translation of an originally Spanish quote in quotation marks. Use the original Spanish
     wording only if verified verbatim (WebFetch on realmadrid.com or a reputable outlet; URL in notes), otherwise reported
     speech without quotation marks. Same for FR with French originals and DE with German originals.
   - Otherwise translate the English quote faithfully, introduced the same way.
12. Spanish terms the English keeps (La Décima, La Séptima, socios, miedo escénico, Galácticos, Ye-yé, hipogeo): keep them,
    with the same quick meaning the English gives.
13. TTS SAFETY: no symbols (& % € + ·), no abbreviations; regnal numbers in words (Alfonso XIII → ES "Alfonso Trece",
    FR "Alphonse treize", DE "Alfons der Dreizehnte"). Money in words ("mil cuatrocientos millones de euros").
14. No ticket prices, opening hours or booking talk.

## Glossary
| English | ES | FR | DE |
|---|---|---|---|
| Tour Bernabéu / the stadium | el Tour Bernabéu / el estadio | le Tour Bernabéu / le stade | die Tour Bernabéu / das Stadion |
| Paseo de la Castellana / Avenida de Concha Espina | el Paseo de la Castellana / la avenida de Concha Espina | le Paseo de la Castellana / l'avenue Concha Espina | der Paseo de la Castellana / die Avenida de Concha Espina |
| the panoramic view, the top tier | la vista panorámica, la grada superior | la vue panoramique, la tribune supérieure | der Panoramablick, der oberste Rang |
| the trophy hall, the row of European Cups | la sala de trofeos, la fila de Copas de Europa | la salle des trophées, la rangée de Coupes d'Europe | der Trophäensaal, die Reihe der Europapokale |
| European Cup / Champions League | Copa de Europa / Champions League | Coupe d'Europe / Ligue des champions | Europapokal / Champions League |
| the dressing room / the benches | el vestuario / los banquillos | le vestiaire / les bancs de touche | die Kabine / die Trainerbänke |
| the press room / the store | la sala de prensa / la tienda | la salle de presse / la boutique | der Presseraum / der Store |
| the retractable pitch, the hypogeum | el césped retráctil, el hipogeo | la pelouse rétractable, l'hypogée | der versenkbare Rasen, das Hypogäum |
| the roof / the 360° screen ring | la cubierta / el videomarcador de 360 grados | le toit / l'anneau d'écrans à 360 degrés | das Dach / der 360-Grad-Bildschirmring |
| Ballon d'Or | Balón de Oro | Ballon d'or | Ballon d'Or |
| Extra (short optional track; in @title "Museum · Extra · …") | "Museo · Extra · …"; en el texto "un breve Extra" | "Musée · Extra · …"; « un court Extra » | "Museum · Extra · …"; „ein kurzer Extra-Titel" |
| @title zone words | Exterior, Panorámica, Museo, Sala de trofeos, Vestuario, Banquillos, Sala de prensa, Tienda | Extérieur, Panorama, Musée, Salle des trophées, Vestiaire, Bancs de touche, Salle de presse, Boutique | Außen, Panorama, Museum, Trophäensaal, Kabine, Trainerbänke, Presseraum, Store |

## Output
For EACH assigned track write: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/bern_i18n/<lang>/NNN.json
  {"title": "<translated @title>", "where": "<translated @where>", "body": "<spoken body with tags, paragraphs separated by \n\n>"}
@title keeps the English pattern "<zone> · <title>" (Extras "<zone> · Extra · <title>"), zone word from the glossary;
opening/closing titles have no zone. Write with Python json.dump(..., ensure_ascii=False, indent=1).

Self-check before finishing (fix every failure, run again until all your lines are OK):
  python3 /home/claude/audioq/bernabeu_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/bern_i18n LANG
Notes: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/bern_i18n/notes/<lang>.md
(official Spanish wording you used + URL, every quotation and how you handled it, anything in the English that looked wrong).
Final report ≤ 120 words.
