# DE review, all 70 tracks (23 Oct 2026)

I reviewed every track sentence by sentence against the English in /home/claude/audioq/thyssen_v5/v5/tracks/NNN.perf.txt, covering facts, hedges, conditionals, navigation, tags and TTS safety. I also ran a separate navigation scan of every last paragraph and every @title.
`assemble.py --check … de`: **all 70 OK** after the edits (exit 0).

## 0. Sync
- 031: already synced as the brief said. The text reads „bevor ein Schlaganfall 1835 seine Arbeit in Öl **weitgehend** beendete“, which matches the new "largely ended". No change needed.

## Changes (track: before → after, why)

### Unifying the two halves (001–035 vs 036–070)
- **Extra announcements.** The 036–070 half used „Saal X hat einen kurzen Extra-Titel zu …“. All of these now use the 001–035 form „In Saal X gibt es einen kurzen Extra-Titel über …“, with the case adjusted to the accusative:
  - 036 Pissarros verregnete Rue Saint-Honoré
  - 039 „Zuerst gibt es in Saal 36 …“
  - 041 die Gelben Blumen von Matisse
  - 047 Mondrians unvollendetes New York City 3
  - 050 das Kartenspiel von Balthus
  - 056 Frank Auerbachs pastosen Kopf von J.Y.M.
  - 057 die Telefonzellen von Richard Estes
  - 060 Bierstadts Sonnenuntergang
  - 065 Kandinskys Ludwigskirche
  - 068 Charles Bells riesigen Flipperautomaten
- **"Next, Room X".** „Als Nächstes Saal X“ became „Weiter geht es in Saal X“, the form already used in 001–035. Tracks: 038, 042, 043, 045, 046, 048, 049, 051, 054, 055, 058, 061, 062, 063, 064, 066, 067. In 038 it is now „Weiter geht es gleich um die Ecke in Saal 35“.
- **"this guide".** „diese Führung“ became „dieser Audioguide“, as in 001 and 021. Tracks: 040 („Sie ist nicht Teil dieses Audioguides“), 058, 059 and 069 (twice).
- **Dates in words.** 040 and 059 had „17. Januar“ and 049 had „24. Januar“. They now read „siebzehnten“ and „vierundzwanzigsten Januar“, as 021 and 028 already did with „zehnten Januar“. This is safer for TTS and consistent across the guide.
- **Level word.** 030 „auf diesem Stockwerk“ → „auf dieser Ebene“, to match 031.
- **Watteau title.** 025, 026 and 056 all use **„Der zufriedene Pierrot“**. For the ear, 026 now reads „Watteau malte das Bild Der zufriedene Pierrot …“ and 056 reads „Es ist Watteaus Bild Der zufriedene Pierrot“, which matches 025's „Watteaus Bild …“.
- **Room titles.** I checked all 70 @where fields. The same room carries the same title in both halves, and spoken mentions match it: Saal 33 „Die impressionistische Periode“, 41/42 „Die kubistische Tradition eins/zwei“, 46/47 „Amerikanische Abstraktion eins/zwei“, and so on. „Saal“, „Ebene“, „Erdgeschoss“ (only where the English says "ground floor"), „die zentrale Halle“ and „Die nächste Hauptstation ist …“ are already used the same way throughout.
- **J.Y.M.** 057 @where had „J. Y. M.“. It is now „J.Y.M.“, as in the title and the body.

### Saal I
- 067: „Als Nächstes Saal I:“ → „Weiter geht es in **Saal I, wie Ida**:“. This is the only spoken mention of Room I. 068's body does not name the room, and titles and @where are not spoken. **Please listen to this in audio QA.** If Katja still says "eins", fall back to „in den Saal mit dem Buchstaben I, wie Ida“ (it fits: 296/298 words leaves little room, so trim one word elsewhere).

### „entartet“ (042 and 041)
- 042 keeps „als „entartet“ verhöhnte“ in quotation marks as a historical Nazi term. No change.
- 041: „sogenannter entarteter Kunst“ → „sogenannter **„entarteter“** Kunst“. This makes the term consistent with 042. It is the standard German historiographic form.

### Mehring's second title (041)
- The museum's English page says only that Mehring "referred to this work as *Reminiscences of the Entrance to Manhattan*" (source: Lieberman). It gives no German wording, and a web search did not find a verified German original.
- So the back-translation is now flagged as a paraphrase, so that German listeners do not take it for Mehring's own wording. Before: „gab dem Bild einen zweiten Titel: Erinnerungen an …“. After: „gab dem Bild einen zweiten Titel, **sinngemäß**: Erinnerungen an die Einfahrt nach Manhattan“.
- In the same passage, „Denn viele Zeichnungen von Grosz dafür stellten sich New York vor“ was an odd personification. It is now „Denn in vielen Zeichnungen dafür stellte sich Grosz New York vor“.

### Meaning and clarity for the ear
- 001 @where: „… gehen und hinauffahren“ implied the lift only, but the English says "go up" and the stairs are also an option. It is now „… ans hintere Ende der Halle gehen und von dort nach oben“.
- 004: „Fachleute sehen Robert Campin hinter ihm“ could send a listener looking behind the figure. It is now „Fachleute sehen darin den Einfluss von Robert Campin“.
- 018: „Er malte ihn um 1630“ was ambiguous, because „ihn“ could refer to the Christ just named. It is now „Er malte das Bild um 1630“.
- 043 and 055: „zurück in Saal 37/41“ was unidiomatic. It is now „drüben in Saal 37/41“.
- 049: „Er suchte nach Träumen …“ is ambiguous between Breton and Surrealism. The English subject is Surrealism, so it is now „Der Surrealismus suchte …“.

## Verified (no change needed)
- 045, Juan Gris's Smoker: „kaufte Kahnweiler dieses Bild zurück“ is correct. The museum page says Kahnweiler repurchased it in 1921. The English "he" is ambiguous, and the DE resolves it correctly.
- Rule 11 quotes: the originally German quotes are reported speech with no quotation marks. These are Dürer (013), Münter (039) and Liebermann (050). The other quotes are faithful translations in quotation marks.
- Navigation scan (B): all 70 last paragraphs match the English. Rooms, order, floors, lift and stairs, "next door", "turn the corner", "stay in this room", the Extras and the next main stop are all correct. Every @title starts with „Saal N ·“ or „Saal A–J ·“, and every Extra has „· Extra ·“.
- No ; or ( in the spoken text, no dashes, no symbols or abbreviations, and regnal numbers are in words.

## For the lead
1. **Saal I**: give 067 an audio check (see above).
2. **041 Mehring**: if someone can find the German original, likely in Lieberman or the Mehring literature, replace the „sinngemäß“ paraphrase with it.
3. Points from the translators, still open and translated as the English has them:
   - 048: Mondrian's Composition No. XIII is said to "hang" in Room 43, but @sources says to CHECK on site.
   - 035: Stafford House is described as "across from Buckingham Palace".
   - 047: the gender of Dabrowski.
   - 058: „vierunddreißigste Straße“ is used for 34th Street.
   - 069: „zwanzig Fuß“.
4. 001–035 says „Weiter geht es in Saal …“ throughout. 036–070 now does too, so the two halves sound like one voice.

Verdict: **ready**, subject to the Saal I audio check.
