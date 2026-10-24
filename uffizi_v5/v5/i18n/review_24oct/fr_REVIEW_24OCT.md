# FR review: Uffizi, 24 Oct 2026 (independent reviewer)

Scope: all 67 tracks compared sentence by sentence with the English (`v5/tracks/NNN.perf.txt`). I also checked @title, @where and both bridge files.
Check after the edits: `assemble.py --check … fr` gives 67/67 OK (exit 0).
A backup of the files as they were before the review is in `scratchpad/fr_review/fr_backup_before/`.

## Automatic checks (all 67 tracks and bridges)
- Room codes: the sequence of codes in every body and every @where matches the English. Every @title starts with the English map code. The Botticelli tracks start with « Salles Botticelli ». No A9–A12 code appears anywhere.
- Bridges: the 23 English keys (NNN E/H>MMM, NNN ≤ 067) each have exactly one French line. Every line uses the same codes and starts with « Dans cette version courte, ».
- TTS: no + & % × ° · ; ( in speech, no Roman numerals, no "St" abbreviations, at most two dashes per track.

## Changes (track: before → after, why)
- 001: « Le musée parle de l'un des premiers musées au monde conçus selon une idée moderne. » → « Pour le musée, c'est l'un des premiers musées au monde de conception moderne. » This is more natural, and 067 now uses the same wording.
- 001: « Anna Maria Luisa » → « Anne-Marie-Louise ». This unifies the name with 067. The French form also matches the other Medici names in the guide (Cosme, François, Ferdinand).
- 004 (last paragraph): « …aux quatre prophètes sous des arcades, sous le trône » → « …celui des quatre prophètes dans des arcades, sous le trône ». This removes the doubled "sous".
- 009 (navigation): « deux portes se suivent » → « deux portes côte à côte ». The English says "side by side".
- 010 (navigation): « prenez celle de la salle A7 » → « prenez celle qui mène à la salle A7 ». The English says "the one … that leads into A7".
- 012 (navigation): « l'autre porte du côté opposé au corridor » → « l'autre porte de la salle A4 du côté opposé au corridor ». The English says "on A4's far side", and the code sequence now matches the English.
- 022: « du Titien » → « de Titien », to unify with 035–067. Also « à l'étage en dessous » → « au premier étage », for floor naming.
- 022 Treaty of Vienna: kept as « le traité de Vienne la renvoya chez elle », which translates the English faithfully. It is sourced, as the lead confirms.
- 024, 025, bridge 023 E>025: « d'Urbino » → « d'Urbin ». This unifies with 052, 053 and 057. There the duchy, the duke and the established title « la Vénus d'Urbin » must sound the same, because 057 explains the name ("that is how she got her name").
- 027: « Essayez de le trouver les trois fois » → « Essayez de repérer les trois », which reads more naturally. Also « Si vous passez l'Extra » → « Si vous sautez l'Extra », because "passer" could be heard as going through it.
- 031: « en arrière à cet étage » → « plus tôt à cet étage », to match the same paragraph's « plus tôt à cet étage ». Also « passez la salle A36, fermée » → « dépassez la salle A36, fermée », because "pass" here means walk past, as in bridge 030 H>034.
- 033: « à l'étage en dessous » → « au premier étage ».
- 036: « Pierre Léopold » → « Pierre-Léopold », as in 001. Also « via dei Georgofili » → « Via dei Georgofili », to match « Via Larga ».
- 039, 042, 046, 052, 053, 057: « Prochain arrêt principal : la salle X » → « Le prochain arrêt principal est la salle X », the wording of 001–034 and 049. To stay within the word limit I made three cuts that keep all the facts: 039 « Ils symbolisaient donc » → « Ils symbolisaient », 042 « Le cardinal est là, en marbre » → « Le voici, en marbre », and 057 « et elle sait » → « et sait ».
- 042: « à l'étage » → « au deuxième étage » ("upstairs", the Goldfinch Madonna). Also « À l'ouverture de ces salles, les murs ont été peints en rose » → « Ces salles ont ouvert avec des murs roses », to save words.
- 047, 054: « à l'étage » → « au deuxième étage » (the Doni Tondo and the Tribune, both "upstairs").
- 061: « Cette salle et les trois suivantes la prolongent » → « … en poursuivent l'histoire ». The English says "carry the story", and « la » had no clear antecedent.
- 067: « créés selon une conception moderne » → « de conception moderne », which matches 001.

## Lead's points: status
- Extras: every track uses « propose un court Extra ». The next main stop is always « Le prochain arrêt principal est … » (058: « D'ici, le prochain arrêt principal est … », for the English "From here").
- Floors: « deuxième étage / premier étage / rez-de-chaussée ». "Upstairs" and "downstairs" are now named floors.
- Lanzi: 037 « descendre d'un seul étage, jusqu'au premier étage, et non jusqu'à la rue ». 037 also has « Descendez d'un seul étage », and the bridge 037 E>041 has « descendez d'un seul étage ».
- « la Vénus de Médicis » and « la Primavera » are used throughout.
- 004 Dante: I kept the faithful French rendering of the English (Longfellow), introduced as « Dans la traduction de Longfellow », and 007 echoes it with « a maintenant la faveur ». To check an established French translation, I made one WebFetch attempt on https://fr.wikisource.org/wiki/La_Divine_Comédie_(Lamennais)/Le_Purgatoire/Chant_XI. It was blocked because the permission was not answered in time, so I did not retry. No unverified Lamennais or Artaud wording was used.
- @where 038, 041, 043, 060: these already match the cleaned English, with no O19/O20/O35 or other production notes. No change was needed.
- 051 « sans fin amour dure » is still verbatim.
- Botticelli rooms: « les salles Botticelli » everywhere, with no codes.

## For the lead (no change made)
- 006 « car Santa Maria Novella était dominicaine » is acceptable but slightly elliptical. "Une église dominicaine" would put the track over the word limit.
- The French runs at 95–100 % of the English word count. Tracks 008, 013, 015, 025, 026, 045 and 065 sit exactly at the limit, so any later English cut there needs a matching French cut.
- The glosses added by the translators are name aids, not new facts: « Uffizi, les Offices » (001), « le Parmesan » (045), « de Médicis » after François premier (022, 054), and « Gian Lorenzo Bernini, le Bernin » (041). I left them in.

Verdict: ready.
