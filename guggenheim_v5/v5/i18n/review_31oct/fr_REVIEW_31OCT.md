# FR review — Guggenheim Bilbao 001–029 + bridges (31 Oct 2026)

Independent native-level edit of `fr/001.json` … `fr/029.json` and `fr/bridges.txt` (bridges_001-029.txt ignored, as instructed).
Every track was read sentence by sentence against `v5/tracks/NNN.perf.txt` (read from disk on 31 Oct, after the lead's 012 change), and every bridge against `v5/bridges/*.txt`.
`assemble.py --check … fr`: all 29 OK after the edits.
Bridges: 10 lines, the same 10 keys as the English, all start with "Dans cette version courte,". Spoken word counts (punctuation not counted) are at or under the English, except 009 H>018 (see below).

## Verdict
Ready. Navigation matches the English in every track: same places, same order, same levels, landmarks, left/right/up/down, both exit variants in 021, every "if…" and every "if you're on the full tour…". Facts and hedges match. Formal "vous" throughout. One level of « » everywhere (checked by script). No symbols, no Roman numerals, years as digits.

## Points the lead asked me to judge
- **"niveau deux / niveau trois": kept. It is now the same everywhere.** Speech says "niveau deux/trois" (015, 016, 017, the bridges 009/015), @title says "Niveau 2 / Niveau 3", and @where says "niveau 2/3" (016, 017, 018, 019). The museum quote in 016 also says "niveau deux". "deuxième étage" would send a French listener one level too high. "étage" is used only as a common noun and never with a number ("entre tous les étages", "du dernier étage", "de cet étage", "l'étage inférieur", "un étage entier au-dessus du hall"). That is correct.
- **Official titles: two checked, one page at a time.** *La matière du temps*: https://www.guggenheim-bilbao.eus/fr/la-collection/oeuvres/la-matiere-du-temps (title as printed; the page says "Salle 104" and does not name a floor). *Grand arbre et l'œil*: https://www.guggenheim-bilbao.eus/fr/la-collection/oeuvres/grand-arbre-et-loeil (the heading prints "l'oeil", the body "l'œil"; "œ" is correct and safe for the voice). The translator's other FR titles (Installation pour Bilbao, Conseil à l'espace V spoken "cinq", Étreinte XI spoken "onze", Tulipes) were not re-fetched.
- **Klein (024): switched to the museum's French wording, introduced « selon le texte du musée ».** Checked word for word on https://www.guggenheim-bilbao.eus/fr/la-collection/oeuvres/fontaine-de-feu (two reads of the same page). The page has « une place publique d'une pièce d'eau sur laquelle danseraient des jets de feu au lieu de jets d'eau » (footnote 2) and « Le feu est pour moi l'avenir sans oublier le passé » (footnote 4). Neither is presented as Klein's original text.
  - P2: « Le texte anglais du musée parle d'un « projet de place publique, une étendue d'eau sur laquelle… » » → « Selon le texte du musée, son projet était « une place publique d'une pièce d'eau sur laquelle danseraient des jets de feu au lieu de jets d'eau ». »
  - P4: « En anglais, il disait : « Le feu est… » » → « Selon le texte du musée, il disait : « Le feu est pour moi l'avenir sans oublier le passé. » »
  - To stay within the word count: « L'œuvre est datée de 1961 » → « L'œuvre date de 1961 ».
  - "réalisation posthume" stays a translation of the English "posthumous realization". It is not in quotation marks as the museum's French, which says « œuvre posthume ». *For the lead:* if you want it fully French-sourced, it could become « œuvre posthume », but I did not verify that wording verbatim.
- **Bridge 009 H>018: wording tightened where possible, and kept at 51 spoken words (the English has 45).** All of the excess comes from the two gallery numbers. « deux cent quatre » and « trois cent quatre » are 6 written words where the English has 2 digits. Read aloud, the English has about 51 words ("two hundred and four", "three hundred and four"), so the French is not longer to the ear. I tried several reorderings, and none came out shorter. The only cut would remove a route element: "from the Atrium", "glass", the "if you can" condition, "niveau deux" or "balcon". So I left the line as it is. I kept "la sculpture voisine" ("voisine" means the one next to you, not the next one in a series).
- **003 (Txema Agirre): plain and respectful.** Short sentences, no embellishment. Two small fixes are listed below.
- **012:** re-read from disk after the lead's edit. The French ends Serra's quote at « Ce n'est pas linéaire. », and the English now does the same. Only P3 was changed, as listed below.

## Changes (track: before → after, why)
- 001 P1: « Ce parvis était autrefois une berge active. » → « Le sol de ce parvis était autrefois une berge industrielle. » This restores "the ground under", and "berge active" is not idiomatic. "berge industrielle" is also how 004 P5 renders the English's "working riverbank".
- 001 P2: « musées Guggenheim, avec New York et Venise » → « comme New York et Venise ». Natural phrasing.
- 002 P5: « L'autre, exposé au Rockefeller Center à New York, vit depuis 2002… » → « L'autre, d'abord au Rockefeller Center, à New York, vit depuis 2002… ». The old wording made it sound as if it was still at Rockefeller Center. The English says "stood".
- 002 P6: « l'acier percer » → « l'acier affleurer ». This is the right verb for "shows through".
- 003 P6: « Aux anniversaires » → « À chaque anniversaire ». Idiomatic.
- 003 P8: « toute la façade » → « toute la façade du musée ». As the English has it.
- 004 P3: « Ses conditions étaient franches. » → « …sans détour. » This is closer to "blunt".
- 005 P3: « l'histoire déraille souvent. On lit souvent… » → « l'histoire est d'ordinaire mal racontée. On lit souvent… ». This is the English meaning (the story is usually told wrongly), and it removes the doubled « souvent ».
- 005 P4: « Il l'a dit « en avance… » » → « Il l'a jugé « en avance… » ». Grammar.
- 008 P1: « sinon son nom » → « même sans connaître son nom ». The old phrase was unclear to the ear.
- 011 P1: « Le reste restait à venir. » → « Le reste était encore à venir. » Removes the « reste/restait » echo.
- 011 P2: « et La matière du temps complète a ouvert en juin 2005 » → « et l'œuvre complète a été inaugurée en juin 2005 ». « complète » was ambiguous after the title. The title is already given in P1.
- 012 P3: « Voici les complexes. » → « Ce sont les plus complexes. » Idiomatic.
- 013 P2: « Le guide pour les enseignants » → « Le guide du musée pour les enseignants ». As the English has it ("the museum's guide"), and consistent with 011, 012 and 016.
- 016 P6: « …la phrase de Serra, quand vous bougez… saisir ? » → « …la phrase de Serra ? Quand vous bougez… saisir. » Easier for the ear.
- 016 P7: « ce qui manque : la moindre colonne. » → « …pas une seule colonne. » Grammar and idiom.
- 017 P5: « Les savoir-faire anciens ont bâti avec le nouveau logiciel. » → « Des savoir-faire anciens l'ont bâti, aux côtés du nouveau logiciel. » The old sentence had no object for « bâti ».
- 018 P3: « Né là, dans la famille Goldberg. » → « Il était né là, chez les Goldberg. » and « Et disait que » → « Et il disait que ». Full sentences.
- 019 P4: « en vingt ans » → « en ses vingt premières années ». The English has "first twenty years".
- 019 P8: « Vous êtes parmi les bien plus nombreux qui sont venus. » → « Il en est venu bien plus, et vous en faites partie. » The old sentence was unidiomatic.
- 020 P2: « selon l'anglais de l'agence AP » → « comme l'a rapporté en anglais l'agence AP ». Clearer, and parallel to 013 « citée en anglais par l'agence AP ».
- 023 P2: « de la Japonaise Fujiko Nakaya » → « de l'artiste japonaise Fujiko Nakaya ». As the English has it.
- 023 P4: « Elle a reçu ce prix plus tard » → « Elle a plus tard reçu ce même prix ». The English has "that same prize".
- 024 P2/P4: Klein (see above).
- 025 P3: « ma mère était très intelligente » → « très habile ». In context ("Like spiders…"), "clever" means skilful.
- 025 P5: « « de douloureux souvenirs d'enfance, un père infidèle… » » → « …d'enfance : un père infidèle… ». The comma read as a list of separate things, while the English says "memories *of*" the father and mother.
- Bridge 002 H>004: « Faites une pause en passant » → « Arrêtez-vous un instant en passant ». « …du musée, la longue rue droite, la Calle Iparragirre, dans votre dos : » → « …du musée, dos à la longue rue droite, la Calle Iparragirre : ». Without "avec", the old line read as if you should find the street. Now 41 words against 42 in the English.
- Bridges 004 E>007 / H>007: « le haut cœur du bâtiment » → « le cœur élancé du bâtiment ». « haut cœur » sounds odd to the ear.
- Bridge 015 E>017: « Puis prenez un ascenseur de verre vers le niveau trois, et lancez-y Ascenseurs et passerelles… » → « Puis, dans un ascenseur de verre vers le niveau trois, lancez Ascenseurs et passerelles… ». « y » could be heard as "on level three", but the English says "start it in the lift". This is a navigation fix. Now 45 words, equal to the English (it was 46).
- Bridge 018 H>025: « …vers la promenade le long du fleuve, à l'opposé du grand pont routier. En bas, longez le bassin… » → « …vers la promenade, à l'opposé du grand pont routier. Au bord de l'eau, longez le bassin… ». « En bas » was vaguer than the English "At the water", the landmark the English gives. To stay within the length, the first mention became « la promenade », because the destination name « Promenade le long du fleuve » follows in the same line. Now 43 words against 44 (it was 45).

## Checked and left as is
- Titles: every @title starts with the same place as the English (Parvis du musée, L'escalier, ZERO, Atrium, Salle 104, Terrasse de l'atrium, Niveau 2/3, Ascenseurs et passerelles, La descente, Le hall · Extra, Dehors, Le bassin, Promenade le long du fleuve, Pont de La Salve). Extras keep "· Extra ·".
- The Extra announcements (« Si vous suivez la visite complète, un court Extra s'écoute ici… ») and « L'arrêt principal suivant est… » are the same in 013, 019, 023 and 027.
- 021: both exit variants are exact (parvis → escalier « du côté opposé au grand pont routier » / « côté fleuve, vous y êtes presque »).
- The listening glosses in 010/012 (« fermé, ouvert… », « droite, gauche… ») and 025 « en français dans le texte : Maman » translate English sub-titles and add no facts.
- 021 P1 « cette berge gagnait sa vie » is a deliberate personification of "worked for a living". It is acceptable, so I kept it.
- "LED" (008, 027): *for the lead*, check in the first audio pass that Vivienne says it naturally.
