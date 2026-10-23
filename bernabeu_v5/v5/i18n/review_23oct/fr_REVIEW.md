# FR review: Bernabéu 001–028

Reviewer: independent editor. I compared all 28 tracks sentence by sentence against the English (`v5/tracks/NNN.perf.txt`). After my edits, `assemble.py --check … fr` passes on all 28 tracks.

## Verdict: READY

Directions are correct in all 28 tracks. Every closing paragraph matches the English, and so does every case instruction in 001, 003, 007, 008 and 019–022. Every "écoutez le numéro …" number matches the English: neuf, vingt-trois, vingt-sept, vingt-deux, vingt et un, quatre and vingt-six. Each conditional carries the same condition and the same "or" structure as the English. All @titles use the glossary zone word: Extérieur, Panorama, Musée, Salle des trophées, Vestiaire, Bancs de touche, Salle de presse and Boutique. The Extras use "· Extra ·", and 001 and 028 have no zone. Facts, scores, minutes, money, years and hedges ("à l'automne 2026", "selon le club", "dit-on") are all checked. I found no TTS-unsafe symbols, parentheses or semicolons, and every score is in words.

## Changes (track: before → after, why)

**Requested by the lead: English 008 changed after translation**
- 008: "En décembre 1985, le Real Madrid avait perdu cinq buts à un…" → "À l'automne 1985, le Real Madrid avait perdu cinq buts à un…". Also "Au retour, ici, Valdano a marqué" → "Au retour, ici, en décembre, Valdano a marqué". This syncs with the updated English: the 5–1 loss was in late November and the 4–0 return leg was on 11 December 1985.

**Meaning and clarity**
- 008: "qui l'employait pour la peur du public" → "qui l'employait pour la peur d'affronter le public". The old wording was ambiguous, since it could mean the audience's fear. The English says "the dread of facing an audience".
- 008: "C'était tout le propos de Valdano." → "Voilà le propos de Valdano." This keeps the word count within the limit after the change above.
- 019: "le Real Madrid a annoncé que toute sa délégation n'irait pas" → "… que toute sa délégation resterait à l'écart". In French, "toute… n'irait pas" can be heard as "not all of it would go". The English says the whole delegation stayed away.
- 019: "En 2024, on attendait largement la victoire de Vinícius Júnior." → "En 2024, Vinícius Júnior était le grand favori." This is more natural for fans, means the same as "widely expected to win", and frees words for the change above.
- 019: "Une source au club" → "Une source du club". This is the idiomatic press wording, and the attribution still matches the English ("a source at the club"). The AFP quote is kept as the translator wrote it: « Le Real Madrid ne va pas là où on ne le respecte pas. ». It is a faithful French rendering of a quote that was originally Spanish, in guillemets and introduced as in the English. That is acceptable under rule 11.
- 021: "Le premier titre de champion, lors de la saison 1931-1932, sans la moindre défaite." → "Le premier titre de champion est arrivé lors de la saison 1931-1932, sans la moindre défaite." The sentence had no verb and sounded unfinished when read aloud.
- 021: "[pause] Et puis il y a l'intrus." → "[pause] Puis vient l'intrus." This saves words for the change above, and the meaning is unchanged.
- 023: "S'ils sont en place aujourd'hui" → "Si c'est le cas aujourd'hui". The "ils" was ambiguous between the players and the name markers. The English "if they're up today" refers to the markers.
- 016: "Puis, en 2014, il atteint la finale" → "… il a atteint la finale". This fixes a stray present tense in a passage told in the passé composé.
- 016: "chacun savait très bien" → "chacun savait exactement". This is closer to "knew exactly" and keeps the word count within the limit.
- 027: "en a rapporté trois cent soixante-trois millions." → "… trois cent soixante-trois millions d'euros." I restored the currency stated in the English.

**Natural French ("ce tour" / "le tour se termine" is an anglicism; "la visite" sounds natural)**
- 001: "Vous entrez par l'entrée du tour, avenue Concha Espina," → "L'entrée du Tour Bernabéu se trouve avenue Concha Espina,". This removes the "entrez par l'entrée" repetition and uses the glossary name.
- 003: "vers l'entrée du tour" → "vers l'entrée du Tour Bernabéu".
- 001, 025, 026: "où le tour se termine" → "où la visite se termine".
- 015: "bien des choses sur ce tour" → "bien des choses que vous voyez ici".
- 022: "deux portes de ce tour" → "deux portes de cette visite". 023: "De toutes les salles de ce tour" → "… de cette visite".
- 027 (@where): "à la fin du tour" → "à la fin de la visite".

**Checked and kept as written**
- 007, 008 and 020: "si le vestiaire est fermé aujourd'hui", where the English says "if it's closed today". In all three, "it" is the dressing room, so the French matches the English meaning. Kept.
- 019: "si votre visite a commencé par le musée, avant la vue" is the correct condition ("came into the museum before the view"). 020 "si vous n'avez pas encore vu le panorama", 021 "si vous n'avez pas encore visité la tribune supérieure" and 022 "Si vous n'avez pas encore vu la tribune supérieure" all match their English conditions.
- 007: "la réserve" for the underground "store" correctly avoids confusion with "la boutique".

## For the lead
- 008 now runs 202 words against an English limit of 204, and passes the check.
- Several tracks sit at or within 1–2 words of the length limit: 019, 021, 025, 027 and 005, among others. Any future edit to the English needs a word budget check in French.
- 019 opens "Un seul footballeur a jamais reçu…". This is acceptable but slightly literary, and I left it because of the word budget (349/350).
- 028: "S10" is left as printed on the bus. Please confirm that the Vivienne voice reads it as "S dix".
- 021: "la saison 1931-1932" follows the brief. Please confirm that the TTS does not read the hyphen aloud.
