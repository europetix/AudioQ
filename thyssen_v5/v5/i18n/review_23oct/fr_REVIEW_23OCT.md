# FR review, all 70 tracks (23 Oct 2026)

I reviewed every track sentence by sentence against the English in /home/claude/audioq/thyssen_v5/v5/tracks/NNN.perf.txt. I checked facts, hedges and conditionals, navigation, titles, quotations, tags and TTS safety. I also scanned every last paragraph and every @title for navigation.
`assemble.py --check … fr`: **all 70 OK** (exit 0). No track is longer than the English. 19 tracks are exactly at the English count: 003, 011, 018, 021, 022, 023, 026, 031, 032, 033, 039, 046, 050, 051, 052, 054, 059, 061 and 067.
I also checked tag placement paragraph by paragraph. Every delivery tag and every pause is now in the same paragraph as the English.
A backup of the files as they were before this review is in scratchpad/frrev/bak/.

## 0. Sync (031)
- Before: « avant qu'une attaque, en 1835, n'arrête presque entièrement sa peinture à l'huile »
- After: « avant qu'une attaque, en 1835, **ne l'éloigne en grande partie** de la peinture à l'huile »
- Why: the translator had synced this, but « presque entièrement » means "almost entirely", which overstates "largely". The new wording keeps the hedge. To stay within the word limit I made two small trims in the same track: « dans les virages » became « aux virages », and « ne sont pas exposés » became « sont décrochés » (= taken off display). I also changed « cet étage » to « ce niveau » (see below).

## 1. Unifying the two halves
- **"The next main stop is …"**. The fixed form is now **« Le prochain arrêt principal est la salle X … »**, as in 001–035. The 036–070 half said « Prochaine étape principale : la salle X, avec … ». Changed in 036, 039, 041, 047, 050, 056, 057, 060 and 065, with « avec » replaced by « : » where needed.
- **Extra announcements**. Both halves already used **« La salle X propose un court Extra sur … »**. No change was needed.
- **"Next, Room X"**. This is now **« Ensuite, la salle X … »** everywhere. The rule-9 room form includes the article « la salle ». 036–070 already used it; 001–035 said « Ensuite, salle X ». Changed in 005, 012, 017, 018, 019, 022, 023, 027, 028, 029, 033, 034 and 035. These cuts pay for the extra word:
  - 022: « les deux petits cuivres » became « les deux cuivres ».
  - 029: « Un spécialiste y voyait peut-être la copie d'un membre de l'atelier » became « Un spécialiste pensait qu'il pouvait s'agir d'une copie d'atelier ». The old « peut-être » made the narrator sound unsure about what the scholar said.
  - 033: « Un des auteurs du musée » became « Un auteur du musée ».
- **"turn the corner"**. This is now « tournez l'angle » in both places:
  - 038: « Ensuite, après l'angle, la salle 35 » became « Ensuite, tournez l'angle : la salle 35 ».
  - 044: « Passez l'angle, vers la salle 41 » became « Tournez l'angle pour entrer dans la salle 41 ».
- **Level word**. "this floor" is now « ce niveau », in line with « niveau 0/1/2 » everywhere else. Changed in 030 and 031 (spoken), in 060 (« Cet étage-ci » became « Ce niveau-ci », because « étage » does not cover the ground floor) and in 059 @where. « À l'étage » for "upstairs" is kept.
- **"back in Room X"**. « en arrière, dans la salle X » is not idiomatic. Changes:
  - 043: « vue dans la salle 37 ».
  - 055: « dont vous avez vu le Berlin… dans la salle 37 », and « Le Fumeur de Gris, vous l'avez vu dans la salle 41 ».
- **Titles of works**. These are given the same way throughout: the title sits in the sentence with no quotation marks, and the same French title in every cross-reference. One mismatch is fixed. 043 had « la Madone villageoise », which is now « la Madone du village », to match the title in 044. I checked every other cross-reference (Pierrot content, Dans l'ovale clair, Le Fumeur, Femme au bain, etc.) and they match.
- **Room titles**. I compared every @where. The same room has the same French title in both halves, and spoken mentions match. I kept Room 11 « Tiziano, Tintoretto, Bassano et le Greco » because it matches the sign.
- **"not part of this guide"**. 021 « hors de ce guide » is now « qui ne fait pas partie de ce guide », as in 001, 040 and 059.

## 2. Salle I (Level 0)
- 067: « Ensuite, la salle I : » became **« Ensuite, la salle I, comme Irène : »**. This is the only spoken mention of Room I. In 068 it appears only in the title and @where, which are not spoken.
- **Audio QA needed.** If Vivienne still says "un", the fallback is « la salle portant la lettre I, comme Irène ». 067 is at 298/298, so one word would have to be cut elsewhere.

## 3. Roman numerals in speech (TTS)
The voice could read these as "i" or "premier". They are spelled out in speech only; @title and @where keep the Roman numerals.
- 044: « La tradition cubiste un ».
- 045: « La tradition cubiste deux ».
- 051: « Abstraction américaine un » and « Brown and Silver un ».
- 050: « Brown and Silver un ».
- 052: « Brown and Silver deux ».
- 053: « Abstraction américaine deux ».

## 4. Lead's specific points
- **054 Rothko**: « Sans titre (Vert sur bordeaux) » matches the English: « bordeaux » is the right French equivalent of maroon, whereas « marron » would mean brown. The parentheses are only in @title, as in the English @title. They are never in speech. In 053's spoken mention, « l'immense et sombre Sans titre, Vert sur bordeaux, de Rothko » could be heard as an adjective ("the untitled…"). It now reads « l'immense toile sombre de Rothko, Sans titre, Vert sur bordeaux ». I also fixed the agreement « trouvé » → « trouvée ».
- **069 "twenty feet"**: « à vingt pieds au fond » became **« à six mètres environ »**, because French listeners do not think in feet. 20 ft is 6.1 m, and « environ » keeps it as an approximation. « plonge loin dans la boutique » still carries the depth.
- **Henri huit**: kept as it is (007 title and @where, 012).
- **Originally French quotations**: all are reported speech without quotation marks:
  - 032 Delacroix
  - 037 Pissarro
  - 038 Derain
  - 044 and 045 Breton
  - 045 Cézanne
  - 046 Robert Delaunay
  - 048 Mondrian
  - 049 Magritte
  - 064 Monet

  I did not invent or quote any "original" French wording. I did no web lookups, because the reported speech is acceptable and nothing needed confirming. The Cézanne wording already follows the familiar French phrasing, but it stays reported speech. Non-French quotes are faithful translations inside « », which rule 11 allows for FR.

## 5. Other changes (track: before → after, why)
- 004: « Les spécialistes voient derrière lui Robert Campin » → « Les spécialistes y voient la marque de Robert Campin ». The old wording could make a listener look for a figure behind the man. The English means Campin's influence.
- 004: « que vous rencontrerez salle 10 » → « … dans la salle 10 ».
- 007: « comme si vous étiez reçu en audience » → « comme si l'on vous recevait en audience ». This avoids assuming the listener's gender.
- 007: « Assez dur pour vous arrêter net » → « Assez fort… ». "Hard enough" here means strong, not harsh.
- 009: « la fine chaîne de sa main gauche » → « dans sa main gauche ».
- 039: « Avant deux ans, elle participera à la fondation… » → « Moins de deux ans plus tard, elle aidera à fonder… ». The old wording was unidiomatic.
- 054: « Il serre les toiles » → « Il accroche les toiles serrées ». The English means hung close together.
- 054: « Cette toile est très probablement de juste après l'exposition, sans certitude » → « Cette toile fut très probablement peinte juste après l'exposition, sans certitude ». The old sentence was awkward.
- 063: [pause] moved back into paragraph 3, as in the English (it was missing there). The translator's extra pause in paragraph 2 is kept.
- 063: « Elle a fait poser le modèle nue » → « Elle a fait poser la jeune femme nue ». « le modèle nue » is an agreement error.
- 064: « artistiques, pas d'opéra » → « artistiques, pas d'opérette ». "Not operatic" here means not a cliché, and « Espagne d'opérette » is the French idiom for clichéd Spain, which fits the bullfights and castanets in the next sentence.

## Verified, no change
- **Navigation scan (B)**: all 70 last paragraphs match the English. I checked rooms and their order, levels, the lift and stairs (029, 031, 032 and 059), "next door", "stay in this room" (006, 024 and 052), the route through Room 8 to Room 9, "Rooms 7 to 10 off the long side", and 021 "back into 16, north through 18, Room 22 Extra, next main stop 23". The Carmen Thyssen access (059) and the exit (069) also match.
- **@title**: every @title starts « Salle N · » or « Salle A–J · ». Extras have « · Extra · ». 001 and 070 have no room.
- **Glossary**: le hall central, la galerie Villahermosa, prêté à, le baron Hans Heinrich Thyssen-Bornemisza, la collection Carmen Thyssen, Charles Quint, Charles deux, Henri huit and niveau 0/1/2 are all used consistently.
- **Rules 4 and 13**: no ; or ( in speech, no dashes and no symbols in speech, regnal numbers in words, formal « vous » throughout. Years are in digits (the checker confirms this).

## For the lead
1. **Salle I**: give 067 an audio check (see section 2).
2. **Roman numerals spelled out**: listen to « Brown and Silver un » and « deux » in 050–052. If the lead prefers the English title read as is, revert to « I » and « II ».
3. These points were translated as the English has them, and the translators' notes on them still stand:
   - 048: Mondrian's Composition No. XIII is said to "hang" in Room 43, but @sources says to check on site.
   - 035: Stafford House is described as "across from Buckingham Palace".
   - 021 and 028: « les salles classiques 19 à 21 » is the translators' own rendering of the English map name.
   - 001: « Début de visite recommandé » is a French map label that has not been checked.
4. 19 tracks are at 100 % of the English word count (see the top of this file). Any later addition there needs a matching cut.

Verdict: **ready**, subject to the Salle I audio check.
