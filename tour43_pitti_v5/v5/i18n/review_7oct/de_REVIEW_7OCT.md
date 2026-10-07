# DE review — Palazzo Pitti, 7 Oct 2026 edition (independent editor, Katja voice, Sie)

Verdict: **approve after the edits below.** Meaning, hedges, the "if she isn't here…" fallbacks and every navigation cue in the
24 tracks match the current English (both rounds, including the 039/040 swap). Track 017 (new) was checked in full and is accurate.
I found one grammar error (027) and two cues that could mislead a listener (005, 010). The rest are naturalness fixes.
`assemble.py --check … de` passes for all 24 files (rc=0). The assembled files still need regenerating from the JSON.

Consistent phrase for "the room marked Sala di X": **"der Saal mit der Aufschrift Sala di X"**, now used in every
"room marked" passage, including the 002 and 004 @where lines.

## Part A — changes made (de/*.json)

| Track | Field | Change | Why |
|---|---|---|---|
| 002 | where | "die zur Sala del Castagnoli führt" → "die zum Saal mit der Aufschrift Sala del Castagnoli führt" | Uses the standard door-sign phrase, as the English does ("the room marked") |
| 002 | body | Removed the comma in "schufen diese Galerie, zwischen …" | Faulty comma |
| 002 | body | "Hier gehören die Räume zur Vorstellung." → "Hier sind die Räume selbst Teil der Inszenierung." | "Vorstellung" can also mean "imagination"; "part of the show" means staging |
| 002 | body | "Wenn Sie also einmal nicht weiterwissen" → "… die Orientierung verlieren" | Closer to "lose your place"; this is the navigation tip |
| 004 | where | "in der Mitte der Sala del Castagnoli" → "… des Saals mit der Aufschrift Sala del Castagnoli" | Matches the English "room marked" |
| 004 | body | "stammt vom späten Ende dieser langen Geschichte" → "steht ganz am Ende dieser langen Geschichte" | "spätes Ende" is not idiomatic German |
| 005 | body (cue) | "…für diesen Saal auf. Gehen Sie durch einige kleinere Räume weiter…" → "…für diesen Saal auf, und gehen Sie gleich durch einige kleinere Räume weiter…" | **Navigation.** As a separate sentence, "walk on" sounded unconditional. A listener who finds La Gravida could leave before playing 006. Now it belongs to the "if she isn't here" branch, as in the English |
| 006 | body (cue) | "Hören Sie in der Sala dell'Iliade zu, machen Sie …" → "Hören Sie diesen Titel in der Sala dell'Iliade, dann machen Sie …" | Clearer conditional for the ear |
| 007 | body (cue) | "das Badezimmer Napoleons" → "das sogenannte Badezimmer Napoleons" | Keeps the English "known as" |
| 010 | body (cue) | "die Titel mit dem Namen an seiner Tür" → "die Titel ab, die den Namen über seiner Tür tragen" | "Above the door" (the 002 tip); the wording now repeats 002's "Titel …, die diesen Namen tragen" |
| 016 | body | "Viele glauben, das Bild entstand für …" → "… das Bild sei für … entstanden" | Reported belief needs the subjunctive (Konjunktiv) |
| 017 | body | "Er ist etwa so groß …" → "Das Bild ist etwa so groß …" | "Er" (= the Raphael) sounds odd to the ear |
| 017 | body | "Er sah den Himmel sich öffnen." → "Er sah, wie sich der Himmel öffnete." | More natural |
| 017 | body | "aufgebrochen, zu einem heißen, glühenden Licht" → "aufgebrochen, in ein heißes, glühendes Licht" | Idiom |
| 017 | body | "flimmern" → "schimmern" | The English says "shimmer". "Flimmern" means flicker |
| 019 | body | "wie die Granduca" → "wie die Madonna del Granduca" | "die Granduca" is wrong (Granduca = grand duke) |
| 019 | body | "die Zutat des Prinzen, nicht Raffael" → "die Ergänzung des Prinzen, nicht Raffaels Werk" | The old line said "not Raphael" instead of "not Raphael's" |
| 019 | body | "Das Baldacchino gehörte …" → "Die Madonna del Baldacchino gehörte …" | Wrong article/referent |
| 023 | body | "Schauen Sie nun unter ihn." → "… unter die Figur." | Awkward |
| 027 | body (cue) | "…liegt vor Ihnen, durch die Tür. Sie ist der letzte Saal der heutigen Route." → "…liegt vor Ihnen, hinter der Tür. Er ist der letzte Saal des heutigen Rundgangs." | **Gender error** (Saal is masculine). "Rundgang" is the term used everywhere else |
| 033 | where | "Folgen Sie von der Treppe oder den Aufzügen aus dem Gang …" → "Von der Treppe oder den Aufzügen aus folgen Sie dem Gang und biegen links ab." | The old word order was ambiguous ("aus dem Gang") |
| 034 | body | "In Saal eins hat Amor Pietro Teneranis Psyche … verlassen" → "In Saal eins steht Pietro Teneranis Psyche aus Marmor. Amor hat sie gerade verlassen, …" | Heard aloud, "Amor Pietro Teneranis" runs together. The new version also tells the listener where to look first |
| 034, 035 | body / where | "weit größer als lebensgroß" → "weit überlebensgroß" | Idiom |
| 034 | body | "Er hat eine eigene Geschichte, auch, wie …" → "Seine Geschichte hat es in sich. Dazu gehört auch, wie …" | Clumsy sentence; the English "quite a story" is restored |
| 035 | body | "Kommen Sie aus der Galleria Palatina" → "Waren Sie schon in der Galleria Palatina" | The English says "If you've walked through" |
| 038 | body (cue) | "Ein weiteres Lieblingsbild von Fattori" → "Auch eines der beliebtesten Bilder Fattoris" | "Lieblingsbild von Fattori" means Fattori's own favourite; the English means the public's |
| 039 | body (cue) | "Bevor Sie weitergehen zu Saal neunzehn" → "Bevor Sie weiter zu Saal neunzehn gehen" | Word order |
| 040 | body | "die genau hier getragen werden" → "die hier auf dem Bild getragen werden" | The listener is in a gallery; "hier" alone is ambiguous |
| 040 | body (cue) | "Gehen Sie dann den Gang nach rechts." → "Gehen Sie dort den Gang entlang nach rechts." | Avoids a second "dann" in a row; keeps "along" |
| 023 025 027 033 034 035 036 040 | title | "–" → "—" | The English and the other DE titles use the em dash |

Checked and left unchanged: 014, 015 ("Fünf Titel": 016–020 = 5 ✓), 018, 020, 025, 036, 037. The hedges are kept
("vielleicht verliehen", "falls sie ausgestellt ist", "In welchem genau, ist nicht veröffentlicht", "Ministry catalogue lists Room 18").

## Part B — navigation scan of all 61 assembled DE tracks (@where + last paragraph)

I found no room name, room number, direction or "look for…" description that differs from the English. Wherever the
English uses a Palatine door sign, the German uses the Italian sign too. The German glosses (Jupitersaal, Marssaal,
Apollosaal, Iliassaal, Venussaal, Saturnsaal) appear only where the English itself uses a gloss ("Room of Jupiter",
"Iliad Room", "Room of Apollo", "at Venus"/"in Saturn"). Tracks 003, 008, 009, 011–013, 021, 022, 024, 026, 028–032 and 041–061 are fine.

Minor items in tracks outside the JSON set (not edited, as the brief requires):

| Track | Sentence | Suggested fix |
|---|---|---|
| 049 (cue) | "Dort reitet eine kleine, rundliche Figur auf einer Schildkröte. **Ihn** sollten Sie unbedingt kennenlernen." | Gender mismatch with "Figur" → "Dort reitet ein kleiner, rundlicher Mann auf einer Schildkröte. Ihn sollten Sie unbedingt kennenlernen." |
| 059 (@where) | "Die Tore sind wegen Restaurierung geschlossen. Betrachten Sie **sie** von außen." | "sie" seems to point to the gates → "Betrachten Sie das Gebäude von außen." |
| 022, 029–032, 043–047, 050, 051, 054, 056, 058 (titles) | Title separator "–" (en dash) | Change to "—" to match the English and the rest of the DE titles. Cosmetic only |
| 010 (JSON) / 011 (@where) | "Vorraum der Treppe del Moro" | The half-German, half-Italian name is consistent across both tracks, so I did not change it. Optional: "Vorraum der Scala del Moro" in both tracks together |

Notes for the English owner (no DE action needed):
- 008 body still says "One of them hangs in the Iliad Room" (a gloss, not the door sign). Its own track 014 now says the
  painting "may be on loan". The DE follows the English.
- 038 @where and body still name Rooms 10–13 and Rooms twelve/thirteen exactly. The translator flagged this before, and the DE follows the English.
- 002 and 004 @where in the English still add "(the Castagnoli Room)". The DE leaves this gloss out, which is harmless.
