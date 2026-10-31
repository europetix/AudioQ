# DE review, Setas de Sevilla edition 5.1 (001–021 + bridges), independent editor, 31 Oct 2026

Verdict: **READY.**

I read all 21 tracks paragraph by paragraph against the 5.1 English in `v5/tracks/`. I concentrated on what is new or changed in 5.1: the new tracks 006, 018 and 021, and the expanded tracks 002, 004, 005, 007–013, 015, 016 and 020.

**Navigation.** I compared every last paragraph and every direction in the body against the English. I found no navigation error. The following all match the English:
- place names, kept unchanged and with no numbers;
- landmarks, including the House of the Column label, the upright two-bird mosaic, the casa almohade label and the exit signs;
- the lifts beside the Antiquarium entrance, the steps up to the Mirador and the way down past the exhibition;
- the way out from the Plaza Mayor by the stairs or the escalators;
- Giralda on the left = west, Giralda at your back = north, Giralda = south;
- the Extras' "if…" conditions and "the next main stop".

**Titles.** Every @title starts with the same place as the English (Rundweg / Der Weg nach unten / Nach dem Besuch per the glossary and brief). Every spoken stop name matches its target track's DE title.

**Facts.** Hedges, attributions ("the operator says", "by one count", "the city told…", "the study…") and every year as digits all match the English. Nothing is added.

**Checks.**
- Tags are in the same order and the same paragraph as the English. No paragraph lost a pause. Each track has 3–6 pauses.
- Emphasis marks match the English.
- There are no symbols, semicolons, parentheses or dashes, and no digits in speech except years.
- `assemble.py --check … de` → all 21 tracks OK after my edits.

## Changes (track: before → after, why)
- **001** "spazieren Menschen über ein riesiges Holzdach" → "über einen riesigen Baldachin aus Holz". The English says "canopy", and the new 018 explicitly says the parasols are "kein geschlossenes Dach", so "Holzdach" would contradict a later track.
- **002** "Ein Haus aus dem maurischen Sevilla kam viel später" → "entstand viel später". "kam" is unidiomatic here.
- **004** "Weil dieser Blick auch für Sie arbeiten konnte" → "auch für einen selbst arbeiten konnte". The English "you" is generic, and the listener never owned a Roman floor.
- **006** "Aus all den Göttern und Ungeheuern … wählte" → "Von all den …". This is the idiomatic preposition.
- **006** "Es könnte dasselbe Mosaik sein. Sie stammt aus dem Hospitium…" → "Diese Tafel stammt aus…". The pronoun skipped over "Mosaik", and a "Sie" at the start of a sentence can be misheard as the formal address.
- **006** "Dort sitzen die Vögel" → "Auf dieser Tafel sitzen die Vögel". The English says "On that panel", and the change makes it clear the description is of the study's panel.
- **008** "eine richtige Markthalle" → "eine richtige, feste Markthalle". The English "permanent" had been dropped. It contrasts with the earlier wooden market.
- **010** "weniger als einen Kilometer von hier." → "… von hier entfernt." This is a grammar fix.
- **014** "Eröffnet werden sollte es 2007, es dauerte vier Jahre länger, …" → "Eröffnet werden sollte es 2007. Es dauerte aber vier Jahre länger, …". The old version was a comma splice and was hard to follow by ear.
- **017** "Das Museum … darunter öffnete am selben Abend." → "wurde am selben Abend eröffnet". This is the correct verb for an inauguration.
- **018** "folgen Sie dem Holz mit dem Blick hinunter bis zu ihm. Zwei der Stämme enthalten die Aufzüge, in Beton." → "… bis zum Stamm. In zwei der Stämme fahren die Aufzüge, umschlossen von Beton." The pronoun was unclear, and "in Beton" was a fragment. The meaning is unchanged: the lifts are inside concrete.
- **019** "Ende 2010 zog sie zurück, … bevor der Platz darüber eröffnet wurde, auf dem Sie stehen." → "Ende 2010 zog sie wieder ein, … bevor der Platz, auf dem Sie stehen, darüber eröffnet wurde." "zog sie zurück" can be heard as "withdrew", and the relative clause was misplaced. This was carried over from 5.0 but is worth fixing.
- **021** "Auf dem Weg nach oben hörten Sie von …" → "haben Sie von … gehört". Spoken German uses the Perfekt here. This now matches 019 "haben Sie gehört".

Bridges: **no changes needed.**
- All 5 English keys (001 E>008, 001 H>009, 009 H>013, 013 H>020, 014 E>017) have exactly one DE line each.
- Each line has the same route as the English and starts with "In dieser Kurzfassung".
- The lines use Rundweg, "Mirador dreihundertsechzig" and "der Weg nach unten", and the stop names match the DE titles.
- `de/bridges.txt` is still identical to `bridges_001-021.txt`.

## For the lead
- **Centuries.** In four places the English uses century-style expressions with digits, and the DE says the century in words, following rule 2. This matches the reviewed 5.0 practice.
  - 002 "the 1200s" → "dreizehnten Jahrhundert"
  - 007 "the 1100s and 1200s" → "zwölften und dreizehnten Jahrhundert"
  - 008 "the late 1500s" → "Ende des sechzehnten Jahrhunderts"
  - 010 "Early in the 1400s" → "Anfang des fünfzehnten Jahrhunderts"
  - Every actual year stays as digits. Decades stay as digits too ("1990er-", "1830er-", "1560er-", "1570er-Jahren", "2000er-Jahre").
- **Quotations.** 5.1 brings no new originally German quote. The translator's handling is correct and consistent with the 5.0 review.
  - Kruse (012) and Mayer's "new contemporary urban centre" (020) stay as reported speech.
  - The other quotes are translations of English-language originals.
  - José de la Peña (017) is a translation of the English release, which is allowed for DE.
  - Because nothing new needed checking, I did no WebFetch.
- **018 indignados.** "the outraged" is given as an appositive without quotation marks ("Sevillas Indignados, die Empörten,"). This is fine for the ear.
- **016 "LED-Leinwand".** The English also says "LED". The voice should read it as letters. Leave it unless Katja mispronounces it.
- **[O…] markers.** These are still in the @where lines of 003–011. I ignored them as instructed. Once the O4 label check is done, update the label-dependent lines in 004–007 in DE together with the English.
- **Backup.** A copy of the translator's files from before my edits is at `/tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/rv/de_backup/`.
