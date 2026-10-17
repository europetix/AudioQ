# DE review, 17 Oct 2026 (all 57 tracks)

I reviewed all 57 tracks sentence by sentence against the English in /home/claude/audioq/reina_v5/v5/tracks/NNN.perf.txt, covering @title, @where and every body paragraph. I also compared the last paragraph of each track with the English and checked every @title prefix.
The original files are backed up in scratchpad/de_review/de_orig/. The edits are in scratchpad/de_review/apply_edits.py.
`assemble.py --check … de` passes for all 57 tracks (57 OK).

## 0. Sync
- 055: "LGTBIQ-plus-Rechte" became "LGBTIQ-plus-Rechte", the same form as 038 ("LGBTIQ-plus-Rechte"). LGBTIQ is the usual German form. Writing "-plus" keeps the "+" symbol out of the speech.

## B. Navigation scan, result
- Every last paragraph matches the English: the same rooms in the same order, the same floors and lifts, "um die Ecke", "Seitenflügel", "hinterer Flügel", "bleiben Sie in Saal …", the Extra announcements and "Die nächste Hauptstation ist …". Every conditional is kept, for example 001 "Wenn Sie kein Schild sehen …", 002 "Wenn Sie ihn nicht sehen …" and 055 "Falls die Dachterrasse heute geschlossen ist …". I found no navigation errors in the translation.
- Every @title starts with "Saal NNN ·". Extras have "· Extra ·" exactly where the English has it. The other prefixes are "Garten · Extra ·", "Nouvel-Dachterrasse ·" and, for 001 and 057, no room.
- One @where fix. In 045, "hinter Saal 10" became "nach Saal 10", because "hinter" means "behind" and the English says "beyond Room 10" along the route.
- 055: "fahren Sie mit dem gläsernen Aufzugsturm" became "fahren Sie im gläsernen Aufzugsturm", because you ride in a tower, not with it. 034: "mit einem davon" became "in einem davon".

## A. Other changes (track: before → after, why)
- 001: "…Sabatini, ein Architekt aus Palermo." → "…Sabatini. Der Architekt wurde in Palermo geboren." The case was wrong, and the English says "born in".
- 001: "Das Museum nennt diese Ideen ihrer Zeit voraus." → "…bezeichnet diese Ideen als ihrer Zeit voraus." The old sentence was ungrammatical. "The museum calls" is kept.
- 001: "kurz und freiwillig" → "kurz und optional". The English says "optional".
- 001: "Der Garten … hat einen kurzen Extra-Titel." → "Zum Garten … gibt es einen kurzen Extra-Titel." A garden cannot "have" a track.
- 002: "der Stahl um ihn" → "der Stahl um ihn herum". This is idiomatic German.
- 004: "sahen genau auf Armut" → "blickten genau auf Armut". This is idiomatic German.
- 005: "Das Bild war dann jahrzehntelang vergessen." → "Das Bild geriet für Jahrzehnte in Vergessenheit." This removes a second "dann".
- 005: "Man sieht, wie er sich überall bedient." → "Sie sehen, …". The English addresses the listener ("you can watch him"), so the formal address is used.
- 006: "an der Straßenwand zu sehen" → "an den Mauern der Straßen zu sehen". "Straßenwand" is not idiomatic.
- 006: "Das Museum liest sie als" → "Das Museum deutet sie als". "Liest" was an anglicism.
- 007: "Das Museum nennt es das ikonischste Bild" → "nennt das Gemälde …". "es" had no clear referent after "die Runde".
- 011: "nahe beim Land seiner Eltern" → "nahe dem Land seiner Eltern". This is idiomatic German.
- 012: "Ein kubistisches Bild, so ein Kritiker, muss man …" → "Wie ein Kritiker sagte, muss man ein kubistisches Bild …". "so ein Kritiker" can be heard as "such a critic". It is still reported speech.
- 013: "Sie lernte in Madrid" → "Sie wurde in Madrid ausgebildet". The English says "trained".
- 013: "Einer machte … Die andere …" → "Der eine machte … Die andere …". This makes the pair consistent.
- 013: "Juan Gris' Offenes Fenster." → "Juan Gris' Bild Das offene Fenster." The title now matches 014.
- 016: "wie der AIZ" → "wie der Arbeiter-Illustrierten-Zeitung". The rule is no abbreviations, and this is the magazine's real German name.
- 016: "Die Risse und Scherenschnitte" → "Die Risse und die Schnitte der Schere". "Scherenschnitt" means a paper silhouette, which is the wrong meaning.
- 017: in the body, "intel·lectuals" → "intellectuals". The middle dot was a TTS risk. The title stays recognisable, and it is followed at once by "Arbeiter, Bauern, Soldaten, Intellektuelle". The @where keeps the correct Catalan spelling "intel·lectuals" because it is display only.
- 017: "gab es so viele, von so vielen Gruppen" → "gab es so viele Plakate, …". The subject was missing.
- 021: in the body, "ALMADEN." → "Almadén.". The capitals could make the voice spell the word letter by letter. The @where keeps "ALMADEN" as it appears on the mobile.
- 021: "Es kopiert Calders Modell für die Genehmigung seiner Idee." → "Es kopiert das Modell, mit dem Calder seine Idee genehmigen ließ." The old sentence was clumsy and could be misread.
- 022: "Der Krieg ging noch weiter." → "Der Krieg dauerte noch an." This is idiomatic German.
- 024: "ganz am Anfang des Mai" → "gleich Anfang Mai". This is idiomatic German.
- 026: "Plötzlich wollten alle, dass der spanische Tanz modern war." → "Plötzlich wollten alle einen modernen spanischen Tanz." The mood of the verb was wrong.
- 027: "dieser Saal ist um ihren Anführer gebaut" → "dieser Saal kreist um ihren Anführer". "gebaut" was an anglicism.
- 028: "einen Tag mit Drachen in Form schwarzer Papiervögel" → "einen Tag, an dem man Drachen in Form schwarzer Papiervögel steigen ließ". "Drachen" alone can mean dragons. The hedge "Manche sagen" is kept.
- 030: "nicht weit von diesem Museum." → "nicht weit von diesem Museum entfernt." This is idiomatic German.
- 033: @where "Dalís Millets architektonisches Angelus" → "Dalís Bild Millets architektonischer Angelus". The body is changed the same way. "der Angelus" is masculine, and the double genitive was confusing.
- 035: "Und der Saal macht noch einen Punkt. Dieses Museum wurde auf der Rückkehr … gegründet." → "Und der Saal betont noch etwas. Dieses Museum gründet auf der Rückkehr …". "einen Punkt machen" is an anglicism.
- 037: "die Route eins" → "Route eins". This makes the term consistent with all other mentions.
- 040: "eine der kreativsten der Transición" → "… des Übergangs zur Demokratie". This applies the glossary term, as in 034, 035, 037 and 057. 036 keeps "Transición" because the sentence explains it right away.
- 042: "die Verbreitung der Spritzen war verheerend" → "die Spritzen hatten verheerende Folgen". The lead asked for a neutral rendering. It does not say whether the needles were shared or spreading. The old wording implied that the syringes themselves were spreading.
- 043: "„Ich habe deine Seele.“ So erzählte es Hervé Guibert. Das sagte sein Freund …" → "„Ich habe deine Seele.“ Das sagte, so erzählte es Hervé Guibert, sein Freund Miquel Barceló zu ihm, …". The hedge now sits where the English has it, and the order is clearer.
- 045: "Feld aus Absätzen aus Kunstharz" → "Feld aus Kunstharzabsätzen". This removes the doubled "aus".
- 047: "Eine Maschine, die Löcher macht, aus Erde gemacht." → "Eine Maschine zum Löchergraben, aus Erde gemacht." This removes the doubled "macht/gemacht".
- 048: "nur unterwegs, etwas zu werden" → "nur auf dem Weg, etwas zu werden". This is idiomatic German.
- 051: "großartigen erfundenen Gebäude" → "prächtigen …". The English "grand" means stately, not "great".
- Terminology unified across the two halves: "Bildnis" (001–028) → "Porträt", the word used in 029–057. Compounds changed with it: Kurtisanenporträts, Königsporträts, Gruppenporträt, Selbstporträt. This touches 004, 005, 007, 008, 010, 012, 013 (including the @title "Porträt Josette Gris"), 015, 022, 027 and 041.
- Checked and left alone: "Als Nächstes …" (first half) and "Weiter geht es in …" (second half) are both correct and vary the speech. "Extra-Titel" and "Hauptstation" are already the same in both halves.

## For the lead
1. **"Saal 205.03 bis" (015).** In German, "bis" means "until", so "durch Saal 205.03 und Saal 205.03 bis" can sound like a range of rooms. The brief requires "205.03 bis", so I left it. Please decide whether to add a gloss or listen-check it with Katja.
2. **Room codes with a dot.** Please listen-check one track to hear how Katja reads "Saal 205.10". It should not come out as a decimal ("Komma") or a date.
3. **Acronyms kept as in the English:** GATEPAC, AC, ARCO, HIV, LGBTIQ-plus. They are proper names or standard initialisms, but they are worth a quick listen.
4. **034, Carl Einstein, originally German.** The quote is still reported speech in Konjunktiv. The German original was not verified, which follows rule 11.
5. **English inconsistencies, translated as written:**
   - 015: the body says "Plan Macià", while @where and @what say "Pla Macià".
   - 009: "late 1800s" is rendered as "Ende des neunzehnten Jahrhunderts". The checker accepts this.
6. **Optional wording changes:**
   - 031: "Freie Bildungsanstalt" for the Institución Libre de Enseñanza is understandable, but German texts often say "Freie Lehranstalt".
   - 056: "Mediterránea" stays in Spanish with no gloss. You could add "das Mittelmeerische" if you want the meaning spoken.

## Verdict
Ready. Navigation and facts match the English in all 57 tracks, and the check passes. Items 1 and 2 above are listen checks, not text errors.
