# DE review: Park Güell 001–045 (7 Nov 2026 edition), independent editor

**Verdict: ready.**

## What I checked
- I read all 45 tracks (@title, @where and body) sentence by sentence against `guell_v5/v5/tracks/NNN.perf.txt`, and all 21 bridges against `v5/bridges/*.txt`.
- `assemble.py --check … de` passes for all 45. Headroom: 045 is 272/272 words, and 038, 040, 007 and 023 are within 2 words. Any later edit there must be word-neutral.
- I wrote a script that checks every in-body cue and every bridge cue. Each one matches a DE @title exactly (with " — " read as " · "). Each one also points to the same destination track as the English cue.
- All 21 bridges have the same key as the English, start with "In dieser Kurzfassung", and are no longer than the English line.
- Navigation: every last paragraph names the same places, in the same order, with the same things to look for. Left and right, "the one without the tower", "on your right as you face the stairway/the city" and "before the check" all match the English. Nothing is added and nothing is dropped.
- Formal "Sie" is used throughout. There are no TTS-unsafe symbols, years are given as digits, and no quotes are attributed to Gaudí. The NEVER list is respected.
- Quotes: DE has no original-language option, so all quotes are faithful translations of the English, with attribution and "auf Spanisch/Katalanisch" framing kept. The only original-language words are the ones the English itself keeps: "barrio de la salud", "molt tensa", "Capelya" and "Garden Party". I did no WebFetch verification because none was needed.

## Lead's points
| Track | Before | After | Why |
|---|---|---|---|
| 001 | "Die ganze Tour … das Wesentliche etwa eineinviertel Stunden, die Highlights …" | "Die vollständige Tour … die Kernversion etwa eineinviertel Stunden, die Highlights …" | House names for the tour lengths |
| 006, 012, 024, 034 | "Wenn Sie die ganze Tour machen" | "Wenn Sie die vollständige Tour machen" | Same |
| 005 | "hyperbolisches Paraboloid" | unchanged | Lead confirmed |
| 039 | "auch wenn die englischen Seiten des Parks ihn Laundry Room Portico nennen" | "auch wenn die Seiten des Parks ihn Laundry Room Portico nennen" | "englischen" is not in the English. The rest of the line matches the English. I also changed "Auf Katalanisch ist es der Pòrtic …" to "Auf Katalanisch heißt er Pòrtic …", because Portikus is masculine. |
| 002 | "Nicht das katalanische „Parc“, sondern die englische Schreibweise." | "Nicht das katalanische „Parc“ mit c, sondern die englische Schreibweise." | Katja says "Parc" and "Park" the same way, so without the letter the contrast cannot be heard. This stays within the rule-4 explanation the lead allowed. |

## Other changes (meaning, ear, grammar)
| Track | Before | After | Why |
|---|---|---|---|
| 001 @where | "Sie brauchen dafür keinen Blick auf etwas." / "Eingangsvorplatz am Tor an der Carrer d'Olot" | "Sie müssen dafür nichts sehen." / "Eingangsvorplatz innerhalb des Tors an der Carrer d'Olot" | Unidiomatic; the English says "inside the … gate" |
| 001 | "Die längeren Touren steigen dann hinauf" | "… führen dann hinauf" | Tours do not "climb" in German |
| 002, 043; @where 003, 044, 045 | "aus dem Weg der Hinausgehenden" | "abseits der Hinausgehenden" | Natural German, and now the same as bridge 043 E>045 |
| 004 | "…seine Tür sehen, aus dem Weg:" | "…seine Tür sehen, ohne im Weg zu stehen:" | "out of the way" = not blocking anyone |
| 030 | "…stehen, aus dem Weg:" | "…stehen, wo Sie niemandem im Weg sind:" | Same |
| 006 | "als Bauhütte" | "als Baubaracke" | "Bauhütte" suggests a medieval masons' lodge; the English means a builders' hut |
| 007 | "So klein es ist, dieses Haus wurde…" | "So klein es auch ist, dieses Haus wurde…" | Grammar (concessive) |
| 008 | "Die Führungen des Museums hier" | "Die eigenen Führungen des Museums hier" | The English says "the museum's own visits" |
| 010 | "Vor jedem Haus baute Gaudí die Straßen." | "Noch vor dem ersten Haus baute Gaudí die Straßen." | The old wording could be heard as "in front of every house" |
| 010 | "die Grundstücke" | "die Parzellen" | Glossary: plot = Parzelle |
| 012 | "bei Fackellicht" / "Gaudí kleidete seine Brücken als Höhlen" | "im Fackelschein" / "Gaudí verkleidete seine Brücken als Höhlen" | Idiom |
| 013 | "von der Plage der Reblaus getroffen" | "von der Reblausplage befallen" | Idiom |
| 019 | "an seinen Gebäuden, Brunnen und Parks" | "an Gebäuden, Brunnen und in Parks" | Preposition: "an Parks" is wrong |
| 019 | "auf ihn hinunter" | "auf das Wesen hinunter" | Unclear pronoun (the previous sentence uses "es") |
| 019, 020 | "der aus (drei) Schlangen gemacht scheint" | "der aus (drei) Schlangen zu bestehen scheint" | Grammar ("scheint" needs "zu …") |
| 020 | "sehen manche Autoren über den Park das antike Griechenland" | "sehen manche, die über den Park schreiben, darin das antike Griechenland" | The old wording could be heard as "see Greece above the park" |
| 021 | "gebaut vor seiner Kundschaft" | "gebaut, bevor seine Kundschaft kam" | Clearer to the ear |
| 022 | "Die Bank sitzt auf der Kolonnade" | "Die Bank ruht auf der Kolonnade" | Idiom |
| 023 | "beeinflusste beim Bauen Gaudí Jujol" | "habe beim Bauen Gaudí Jujol beeinflusst" | Reported speech (Duch quoting the son) |
| 024 | "die Medaillons der vier Sonnen, eine für jede Jahreszeit" | "… eines für jede Jahreszeit" | Agreement with "Medaillon" (neuter) |
| 025 | "aus Minen im Hügel" | "aus Stollen im Hügel" | In German, "Minen" means explosive or ore mines. These are water galleries (Catalan "mines d'aigua"). |
| 038 | "einer alten Wassermine, eines schmalen Tunnels" | "eines alten Wasserstollens, eines schmalen Tunnels" | Same. The following "er ist sehr eng" now agrees. |
| 038 | "Er führt weiter zu Güells eigenem Zuhause." | "Er führt weiter auf Güells eigenes Zuhause zu." | The English says "leads on toward", not "to" |
| 027 | "Heute, mit den Worten des Parks, „ist …" | "Heute, so der Park, „ist …" | Smoother |
| 027 | "den Zwangskauf eingeleitet" | "ein Enteignungsverfahren eingeleitet" | Standard German for compulsory purchase |
| 028 | "Kein Käufer kam dafür." | "Es fand sich kein Käufer." | Idiom |
| 028 | "Später machte ein Ehepaar, das ihn bewunderte, das Ehepaar Chiappo, es als Casa Gaudí bekannt." | "Später machte es ein Ehepaar, das ihn bewunderte, die Chiappos, als Casa Gaudí bekannt." | Clumsy repetition |
| 028 | "die rosa verputzten Wände und der spitze Turm" | "… und den spitzen Turm" | Case (accusative after "Suchen Sie es") |
| 028 | "Bleiben Sie mit dem rosa Haus im Blick:" | "Behalten Sie das rosa Haus im Blick:" | Idiom |
| 029 | "So lebten drei im Haus" | "So lebten drei Menschen im Haus" | Idiom |
| 030 | "hat es zusammengesetzt" / "sie haben „gute Aussichten“" | "hat es rekonstruiert" / "sie hätten „gute Ausblicke“" | Idiom. "gute Aussichten" also means "good prospects" |
| 033 | "Warum ein Fest auf einer Siedlung" | "… in einer Siedlung" | Preposition |
| 033 | "hundert Jahre nachdem er ein öffentlicher Park wurde, waren die Nachbarn …" | "hundert Jahre nachdem der Park öffentlich wurde, waren die Anwohner …" | "er" was unclear after the race sentence. "Anwohner" fits a community dinner. |
| 036 | "an Barcelona angeschlossen worden" | "nach Barcelona eingemeindet worden" | Correct German term for a municipal merger |
| 037 | "etwa hundertachtzig Meter hoch" | "auf etwa hundertachtzig Metern Höhe" | The English gives the elevation ("metres up"), not the hill's height |
| 039 | "Der Stein … hält einen Hang" / "die einen Hügel hält" / "Das heißt Bauen, das …" | "stützt einen Hang" / "die einen Hügel stützt" / "Gemeint ist ein Bauen, das …" | Idiom |
| 041 | "auf seine eigene Siedlung" / "Heute ist es eine Schule in Betrieb" | "in seine eigene Siedlung" / "Heute ist dort eine Schule in Betrieb" | Preposition; idiom |
| 044 | "Wer in der Stadt lebt, und vor allem die Nachbarn, kann weiterhin kostenlos hinein." | "Wer in der Stadt lebt, und vor allem wer in der Nachbarschaft wohnt, kommt weiterhin kostenlos hinein." | Broken syntax |
| Bridge 016 E>018 | "ein Stück über den roten und gelben Streifen" | "knapp über den roten und gelben Streifen" | Now the same as 015 H>018 |

None of these changes affects a place name, a direction or a cue. `bridges_001-045.txt` is left as the translator's original; `bridges.txt` is the edited file.

## Glossary deltas (on top of the translator's)
- full tour / the essential / the highlights → **die vollständige Tour / die Kernversion / die Highlights**
- water mine / mines in the hill → **Wasserstollen / Stollen**
- builders' hut → Baubaracke

## For the lead (no action needed unless you disagree)
1. **023, "original tile-shard mosaics"** (park quote). If the park's Spanish says "originales mosaicos", the sense is "inventive", which would be "originellen" in German. I kept the literal "originalen". The cue is not affected.
2. **017 "Eine Forscherin"** (García Ávila) and **040 "Ein Forscher"** (Rius Santamaria). The gender comes from the sources; no name is added. I accept both.
3. **008 "promoter" = "Förderer"**. This works as patron or sponsor and fits the artist and patron line. "Bauträger" would only be right if Freixa meant "property developer".
4. In the bridges, "In dieser Kurzfassung" covers both the Kernversion and the Highlights. This is required by the brief and is fine to the ear.
