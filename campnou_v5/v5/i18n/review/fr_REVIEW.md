# FR review, tracks 001–034 and bridges (independent reviewer)

Verdict: **ready**, once the lead has listened to the two by-ear points below.

`assemble.py --check … fr` passes for all 34 after my edits. 011, 017, 020, 025, 026, 029, 030 and 032 are now exactly at the English word count, so the next editor has no slack there.

## Things the lead asked me to confirm
- 010, paragraph 5 (the last sentence of the Xavi paragraph): "Pour Xavi, ce fut son dernier match, et son dernier trophée sous ces couleurs." It matches the current English. Confirmed.
- 011, paragraph 7: "En 2026, après avoir quitté le club, Alexia a gagné son troisième." It matches the current English. Confirmed.
- 030 "Un peu plus de soixante-huit pour cent": kept, as you allowed.

## Navigation scan (B)
- All 34 last paragraphs have the same places, the same order and the same things to look for as the English. The conditions are kept: the full-tour branches in 016 and 029, "if there's room", "if it's here", "if they are labelled".
- Every spoken `<place> · <title>` matches the destination's French @title exactly. I checked this with a script against all titles.
- The display names are identical everywhere, per the glossary. "La salle ronde" is only ever the 360° room, and "le pavillon rond" is only ever the Palau Blaugrana. "La sortie" is never used for the way out of the round room.
- The 360° warning (001, 024) is translated exactly, without softening. The honesty frame in 001 is intact.
- Bridges: 10/10, with the same keys in the same order. Each starts with "Dans cette version courte,". Each is no longer than its English line: 42/43, 46/46, 37/38, 28/28, 32/33, 30/34, 31/31, 37/37, 33/33, 31/31. Each ends on the exact French title. Both 024 bridges stay conditional ("quand le spectacle est terminé"). Bridges: no changes.

## Changes (track: before → after, why)
1. **021 (quote meaning error).** "Faites-le signer. N'y pensez même pas." → "Faites-le signer. Ne réfléchissez même pas." In French, "N'y pensez même pas" means "forget it, don't do it", which is the opposite of Rexach's meaning: sign him, no need to deliberate. The writers' notes give ESPN's English, which goes on: "And if anyone asks, tell them it's my decision."
2. **033 (typo the voice would hear as a double pause).** "Messi, dix-huit ans,, pour" → "dix-huit ans, pour".
3. **029 (TTS rule: regnal numbers in words).** "Jean-Paul II" → "Jean-Paul deux".
4. **026 (dangling modifier: it said the club, not the stadium, would be finished).** "Une fois terminé, le club prévoit…" → "Une fois le stade terminé, le club prévoit…".
5. **034 (ambiguity: it could be heard as "closed months after").** "Il fut fermé des mois après que…" → "Il fut fermé pendant des mois après que…".
6. **021.** "ne voulait garantir de le payer" → "ne voulait garantir de payer le traitement". "le payer" could be heard as paying the boy, but the English means paying for the treatment.
7. **022.** "Ce musée expose les huit." → "Ce musée les expose tous les huit." This restores "all eight of his".
8. **011.** "À Noël 1970" → "Le jour de Noël 1970", for "On Christmas Day". Also "Chacun, à l'époque, un record…" → "Chaque fois, à l'époque, un record…": "Chacun" right after a crowd figure could be heard as "each person". The last paragraph read "le mur des maillots : tout un mur, côte à côte :", with two colons and a garbled sense. It is now "le mur des maillots, tout un mur de maillots côte à côte :".
9. **013.** "pour la première fois en quatorze ans" → "depuis quatorze ans", which is correct French. "Georges, patron de la Catalogne" → "saint patron".
10. **014.** "quatre championnats d'affilée" → "quatre championnats d'Espagne d'affilée". This restores "Spanish leagues".
11. **015.** "sept des titulaires espagnols étaient du Barça" → "sept titulaires de l'Espagne jouaient au Barça". The old wording could mean "Spanish-born starters" rather than Spain's starters. Also "ce que le club défend" → "ce que le club représente", for "stands for".
12. **017.** "les supporters le portent" (the pronoun's antecedent was too far back) → "les supporters portent ce nom". "D'où qu'il vienne" → "D'où que vienne le surnom".
13. **020.** "Et même le bilan de Barcelone…" → "Et le bilan de Barcelone, lui, …". "même" (even) added an emphasis that is not in the English.
14. **023.** "un derby contre l'Espanyol" → "un derby barcelonais contre l'Espanyol". This restores "city derby".
15. **024.** "Arrêtez-le avant d'entrer" → "Arrêtez le guide avant d'entrer". "le" could be heard as the show.
16. **029.** "Et un soir, ici, appartint à deux tout autres clubs." → "Et un soir appartint ici à deux tout autres clubs.", to fix the syntax. "avec des foules records mondiales" → "avec des records mondiaux d'affluence", which is idiomatic.
17. **031.** "une chanson chantée d'abord dans cette enceinte" → "chantée pour la première fois", for "first sung".
18. **002.** "les travaux commençaient … et la pelouse elle-même partit en premier" → "les travaux étaient lancés … et la première chose à partir fut la pelouse elle-même", which is closer to the English. "Selon le compte rendu du club" → "…du club sur cette soirée", restoring "of the night".
19. **004.** "Le journal s'était trompé sur le jeu, et sur l'homme aussi." → "Le journal avait écorché le nom du jeu, et celui de l'homme aussi." The old wording read as "misjudged the game", but the point is the misspellings.
20. **006.** "Un nouveau musée s'achève dans le stade." → "On achève un nouveau musée dans le stade." "s'achève" can be heard as "is ending".
21. **012.** "Une fois à la partie consacrée à Johan Cruyff" → "Quand vous arrivez à la partie…", which is clearer for the ear.
22. **@where fields** (not word-limited):
    - 001 and 003: "le Palau Blaugrana, tout rond" → "le Palau Blaugrana, le pavillon rond", the glossary term.
    - 025: "Juste à la sortie de la salle ronde" → "Juste à l'extérieur…", to keep "sortie" away from the exit's fixed name.
    - 026 and 034: "écoutez-la" (the pronoun had no antecedent) → "écoutez cet arrêt".

## Checked and left as is
- Quotes: all are translated faithfully from the English, with their attributions. "Salid y disfrutad" is kept in Spanish with its French gloss. There are no anthem lyrics; 032 paraphrases them, as the English does. The 028 treasurer is in reported speech. Nothing needed web verification for FR.
- PLAN §4 NEVER list: it is clean. There is no "Nou Camp", no money sums, no "Franco ordered". The napkin and the museum are in separate sentences (021). 022 says six Ballons d'Or won here and eight on show. Every "the story goes" and "the club says" is present.
- Dead people are in the past tense, and living people and the club in the present.
- 033: "L'une des manches se joua au Bernabéu" drops "of that league cup final". The sentence before already names "la Coupe de la Ligue en deux manches", so the meaning survives. There was no word budget to restore it.
- Day dates are written as digits ("le 22 novembre"). Vivienne reads them correctly in French. Years are digits, as required.

## For the lead
- **By ear:** the title "D'un match de Noël à 91 648" (011, also in the cues of 010 and bridge 009 E>011). It uses a no-break space, and the voice should say "quatre-vingt-onze mille six cent quarante-huit". If it splits the number, write it as "91648" in all three places.
- **By ear:** "foot-vall" in 004.
- The translator's notes still say "Jean-Paul II". The text now says "Jean-Paul deux".
- Nothing wrong found in the English.
- I did not commit.
