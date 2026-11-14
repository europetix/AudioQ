# ES review, FC Barcelona Museum, 001–034 + bridges (14 Nov 2026)

Reviewer: independent ES editor. I checked every track sentence by sentence against the current English (`v5/tracks/NNN.perf.txt`) and every bridge against `v5/bridges/*.txt`.

**Verdict: ready.** The translation was accurate and natural. I made 39 small edits in 23 tracks and changed 1 bridge. One edit fixes a real meaning error (034). Two edits put in verified original Spanish wording (021, 023). One hedge was restored (007). The rest are fluency and TTS fixes. No navigation errors were found.

## Checks run
- `assemble.py --check … es`: all 34 OK, exit 0 after the edits. The tightest tracks are 017 (199/199), 025 (209/209), 029 (277/277) and 033 (280/281).
- **Navigation scan** (by script and by eye). In all 34 last paragraphs, the places, their order and the things to look for match the English. Every spoken `<place> · <title>` matches the destination's ES @title character for character. There are 18 distinct place names, each used identically in every title, cue and bridge (see the translator's glossary). 016 and 029 each have two cues, and both are correct. 034 has no cue, as in the English.
- **Bridges:** 10 of 10 are present, with the same keys as the English. All start "En esta versión corta,", all end on the exact destination title, and none is longer than the English (001 H>008 46/46, 009 E>011 28/28, 008 H>022 31/31, 012 E>014 33/33 are equal; the rest are shorter). Both 024 bridges keep "cuando termine el espectáculo".
- **001 honesty frame and the 360° warning** (001, 024): exact, warm and not softened.
- **PLAN §4 NEVER list:** clean. There is no "Nou Camp", no "biggest stadium", no napkin "here", no "Franco ordered" (016 uses "se castellanizó"), no "regime's club", no sums of money, no anthem lyrics (032 is a paraphrase), no 2017 and no gate numbers.
- **TTS scan:** no ; ( % & + × in speech. Day numbers are written as digits ("22 de noviembre"), which reads correctly. The regnal number is in words ("Juan Pablo segundo"). The only remaining hyphens are in names (Miró-Sans, García-Barbón, Saint-Germain, foot-vall).
- The translator's build sources `cn_i18n/es_src/b1–b4.py` mirror every edit. Re-running `write.py b1 b2 b3 b4` gives the edited JSON byte for byte (checked). The pre-review state is saved in `cn_i18n/es_prereview/`.

## Points the lead asked me to settle
1. **Late English changes: both applied.** In 010 P5: "[pause] Para Xavi, fue su último partido, y su último título con estos colores." In 011 P7: "En 2026, ya fuera del club, Alexia ganó su tercero."
2. **030, sixty-eight per cent:** kept as "Algo más del sesenta y ocho por ciento", as the lead allows.
3. **004, the 1899 ad: not verified, so translated from the English.**
   - I read the club's English page (4153324) once. It gives "Our friend and colleague Mr Kans Kamper [sic], of the foot-vall [sic] section of the Sociedad de Deportes". It links no ES or CA version of the article, only the language homepages.
   - My one try at the Spanish article URL (fcbarcelona.com/es/club/noticias/4153324) was blocked because it redirects off-site. The fcbarcelona.es form of the same URL timed out on the permission check, and I did not retry it.
   - One web search found no club ES or CA copy of the article.
   - So the ES stays a faithful translation, with both misspellings exactly as printed: «Nuestro amigo y compañero míster Kans Kamper, de la sección de foot-vall».
   - **For the render test:** in Spanish, b and v sound the same, so "foot-vall" is not audibly wrong the way it is in English. Dalia may also read "ll" as /ʝ/ ("fut-bay"). The title still says "dos faltas de ortografía", and Kans Kamper carries the joke. Please listen to it.
4. **021, the napkin: original wording verified on Ara (es), and used.**
   - es.ara.cat (lucha-salvar-servilleta…_4985264, the S16 source) gives the napkin as "se compromete bajo su **única** responsabilidad y **pese a** algunas opiniones en contra a fichar al jugador Lionel Messi". This matches Ara's English (and so our English), "sole" included.
   - ES now reads "se comprometía, bajo su única responsabilidad y pese a algunas opiniones en contra, a fichar al jugador Lionel Messi". The translator had "exclusiva … a pesar de".
   - **For the lead (possible English fix):** CNN Español (cnnespanol.cnn.com/2024/02/01/messi-servilleta-subasta-barcelona-trax/) gives a different text: "se compromete bajo su responsabilidad y contra algunas opiniones discrepantes", with **no "sole"**. The two reputable sources disagree. Our English follows Ara, which is the cited source, and the passage sits under "the story goes", so the English is defensible.
   - If you want it unarguable, drop "sole" in the English ("under his own responsibility"). ES would then drop "única". I did not change it.
5. **011 title "91648": kept as is.** It is identical in the 011 title, the 010 cue and the 009 E>011 bridge (checked by script).
   - "91.648" would be read by the es-MX voice as a decimal. "91,648" is right for es-MX but reads as a decimal to readers in Spain. "91 648" risks being read as two numbers.
   - A bare "91648" is the only form every reader and the voice take as one cardinal. Writing it in words would push the 010 cue and the bridge over length.
   - Please put it on the Dalia render test. The body (011 P5) has the figure in words.

## Quotes: how each is handled
- **Verified originals:**
  - 008 "Salid y disfrutad". This is kept in every language. The DE reviewer verified it on fcbarcelona.es 643913, and I did not refetch it.
  - 020 Real Madrid. I refetched realmadrid.com …/historia/futbol/1941-1950: "Aquí nació la eterna rivalidad entre ambos clubes." and "gracias a una extraordinaria remontada". Both match the ES.
  - 021 the napkin, from Ara es (see above). It is narrated, not in quotation marks, as in the English.
  - **023 the club's statement (new).** It now reads «no se podrá formalizar debido a obstáculos económicos y estructurales». This is the club's Spanish statement of 5 Aug 2021 as reproduced by Crónica (cronica.com.ar, "A cinco años de la salida de Lionel Messi…"), and the same phrase appears across many outlets in a web search. The old text was the translator's back-translation, «no puede formalizarse por…».
- **Faithful translations of the English (unverified, as the brief allows):**
  - 004 the ad.
  - 011 Alexia ("según la traducción del club").
  - 013 Jordi Cruyff (ESPN EN) and Asensi.
  - 014 the two club lines.
  - 015 Iniesta.
  - 016 de Carreras, the 1933 bulletin and Elena Fort.
  - 018 Gamper.
  - 020 Ya (via the Guardian) and Barau (Goal).
  - 021 Rexach (ESPN EN, "Fichadlo. Ni lo penséis.").
  - 022 the club page.
  - 030 Miró-Sans.
  - 031 the club and Daučík.
- 028's treasurer stays in reported speech.

## Changes (track: before → after, why)
1. **001** P3: "un anuncio por palabras" → "un anuncio clasificado". The old phrase is Spain-only, and the new one is neutral for es-MX.
2. **001** P5: "lo repetirá en su puerta" → "lo repetirá a su entrada". This is more natural.
3. **001** cue: "lejos de la avenida" → "alejándose de la avenida". The English "away from the avenue" is a direction, not a place.
4. **002** P3: "Lamine Yamal dio el segundo … a Ferran Torres" → "dio la asistencia del segundo …". The old wording could be heard as Lamine scoring.
5. **004** P2: "los lectores leyeron esto" → "encontraron esto". This follows the English "found" and avoids the repeated verb.
6. **007** P1: "el museo exponía más de cien trofeos" → "el museo registraba más de cien trofeos de fútbol expuestos". This restores the English "listed" (the museum's own count) as a hedge.
7. **008** P2: "No eran desconocidos." → "Ya se conocían." The new wording is idiomatic for "They were no strangers".
8. **008** P4: "en su nonagésimo tercer año" → "en el año noventa y tres de su historia". The old ordinal was heavy by ear.
9. **008** cue: "las dos siguientes, París y Roma" → "las dos siguientes, las de París y Roma". This makes clear they are the cups from Paris and Rome.
10. **009** P3: "el club dio el primer equipo" → "el club confió el primer equipo". This is idiomatic.
11. **009** P4: the sentence was reordered to "La noche que salvó el año fue la semifinal contra el Chelsea, en mayo de 2009, en Stamford Bridge." The old version had a verbless fragment ("…Bridge, semifinal contra…"), and the word count stays within the limit.
12. **010** P4: "Para que hablen de mala suerte." → "Para que luego hablen de mala suerte." This completes the idiom ("So much for bad luck").
13. **011** P3: "tras cuatro derrotas previas" → "tras perder cuatro veces ante él". The English says the four defeats were against Lyon.
14. **011** cue: "busque toda una pared de camisetas" → "busque la pared de las camisetas, una junto a otra". The English instruction names "the wall of shirts", and the ES now uses the fixed display name, as the cue does.
15. **013** P1: «…por un Real Madrid-Barcelona» → «…por un Real Madrid contra Barcelona». The hyphen was a TTS risk, and the new form is natural in speech.
16. **013** P2: "fichó desde el Ajax" → "fichó procedente del Ajax". This is idiomatic.
17. **017** P1: "y salen traseros" → "y va de traseros". This is the natural phrase for "it involves backsides", at the same length.
18. **018** P4: "Ahora fue obligado a dejar" → "Entonces se vio obligado a dejar". The old wording was a calque.
19. **019** P1: "Cerca del Alto del León" → "Cerca del puerto del Alto del León". This restores "pass".
20. **019** P3: "durante casi una semana" → "durante cerca de una semana". The English says "about", not "almost".
21. **019** cue: "Quédese para una más, … de su historia" → "Quédese aquí para una más, … de la historia del club". This restores "here" and makes the "su" unambiguous.
22. **020** P3: "Pero otra parte, una amenaza en el descanso, según él nadie ha podido probarla nunca." → "…, nadie ha podido probarla nunca, según él." The new word order is easier to follow by ear.
23. **020** P6: "siguen contándolo" → "siguen contando este partido". The English says "this match", and "lo" was unclear.
24. **021** P4: "bajo su exclusiva responsabilidad y a pesar de" → "bajo su única responsabilidad y pese a". This is the verified original wording (see above).
25. **022** P4: "el récord de un año natural de Gerd Müller, de 1972" → "el récord de un año natural que Gerd Müller tenía desde 1972". The English is "the record … that Gerd Müller had set in 1972".
26. **022** cue: "Siga en el espacio de Messi: cómo acabó…, y quién…:" → "Quédese en el espacio de Messi para saber cómo acabó … y quién …:". The old version had two colons before the cue, which could blur the cue.
27. **023** P3: "la temporada 2011-2012" → "la temporada de 2011 a 2012". The voice could read the hyphen as "menos" or skip it.
28. **023** P4: the club's quote now uses the verified original Spanish (see above).
29. **023** P7: "Se traspasó" → "Pasó a otros". "Traspaso" means a player transfer and was misleading here.
30. **025** P6: "el primero de miles allí" → "el primero de miles en aquel estadio". The English says "in that bowl", and the bare "allí" was vague in the round room.
31. **026** P4: "La nueva cubierta debe proteger a todos" → "está pensada para cubrir a todos". The English "is meant to cover" is about design, not obligation.
32. **026** P7: "la piel que lo envuelve" → "la piel que envuelve el exterior". The English is "wrapped round the outside", and "lo" was unclear.
33. **028** P3: "calcula su longitud en" → "cifra su longitud en". The English "puts its length at" is not an estimate.
34. **028** P7: "las viejas abajo" → "el viejo graderío abajo". The English is "the old bowl".
35. **029** P2: the second "acogió" → "albergó". This avoids the repetition.
36. **030** P4: "según la traducción de las páginas de historia del club" → "según la versión…". The slogan was not translated into Spanish by the club, so "traducción" claimed something untrue. The hedge is kept.
37. **033** P2: "fue corta, nunca aburrida" → "fue corta y nunca aburrida". This is smoother.
38. **033** P5: "asistió en el primer gol" → "dio la asistencia del primer gol". This is idiomatic.
39. **034** P2: **meaning fix.** "Lo cerraron meses después de que su público pitara un himno" → "Lo cerraron durante meses después de…". The old ES said the closure came months later. The English means the club was shut down for months.
40. **Bridge 009 E>011:** "con sus Copas europeas" → "con las suyas propias". This keeps "their own", matches 010's "sus propias Copas de Europa", and stays at 28/28 words.

## Reviewed and left as is
- 008: the gloss "Go out and enjoy it" is dropped after «Salid y disfrutad», because it would only repeat the same words in Spanish. Both [pause] tags are kept.
- 012 title "La camiseta que pagó por llevar un nombre": a sensible rendering of the pun, and the story explains it.
- 016/021/034: the napkin title is "Una promesa en una servilleta". 021 and 034 keep "servilleta de papel".
- 021 "Fichadlo. Ni lo penséis.": the vosotros form fits a Spanish coach speaking in Spain. It is understood in es-MX.
- 027 P2 "por voto directo" without "ellos mismos": the meaning is kept, and the track is at 221/222.
- 029 P5 "marcaron dos suplentes": this keeps the English's ambiguity, and the track is at 277/277.
- 011 P7: the Alexia/Aitana pair is exactly as the English.

## For the lead
1. **021 "sole"**: the sources disagree (Ara "única", CNN Español none). Consider "his own responsibility" in the English (item 4 above).
2. **Dalia render test:** "91648" (011 title, 010 cue, 009 bridge), "foot-vall" and "Kans Kamper" (004), "Salid y disfrutad" (008), "b720" (026), "Juan Pablo segundo" (029), "Ballons d'Or" (011, 022) and "Fichadlo" (021).
3. **004 original ad:** unverified in Spanish. The club's ES or CA article URL could not be fetched here. If someone can open it in a browser, compare the ad's Spanish wording before recording, in case the printed form was "foot-ball".
4. If the English changes again, re-run `assemble.py --check` and the cue scan (`scratchpad/rev_es/nav.py`). The ES titles are the cue strings.
