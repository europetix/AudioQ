# FR review: Park Güell 001–045 (7 Nov 2026 edition), independent editor, voice Vivienne

**Verdict: ready.** There is one point for the lead (045, see below), but it needs no change to the FR.

## What I checked
- I read all 45 tracks (@title, @where and body) sentence by sentence against `guell_v5/v5/tracks/NNN.perf.txt`. That includes the 018 English as updated today ("have seen"). I also read all 21 bridges against `v5/bridges/*.txt`.
- `assemble.py --check … fr` passes for all 45. These tracks are now exactly at the English word count: 003, 004, 006, 007, 011, 015, 017, 019, 020, 023, 024, 028, 029, 035, 037, 038, 042, 043, 045. These have one word of margin: 005, 008, 010, 012, 013, 018, 031, 036, 044. Any later edit to these must be word-neutral.
- I ran a script over every track. The last paragraph of each FR track cues the same destination tracks, in the same order, as the English. Each FR cue matches the destination's FR @title exactly. The " · " count per track equals the English count.
- Bridges: there are 21, with the same keys as the English. Every one starts "Dans cette version courte,", and every one ends with the destination's FR @title. None is longer than its English line (measured in words).
- There are no ; ( + & % × anywhere in speech. Formal "vous" is used throughout. Regnal number: "Alphonse treize". The NEVER list is respected: 004 and 028 keep their denials, and no quote is put in Gaudí's mouth.
- Quotes: FR has no original-language option. All quotes are faithful translations of the English, with the attribution and the "en espagnol / en catalan" framing kept. No WebFetch was needed.

## Lead's points
| Track | Before | After | Why |
|---|---|---|---|
| 001 | "l'essentielle environ une heure et quart, celle des temps forts environ trois quarts d'heure" | "la version essentielle environ une heure et quart, les incontournables environ trois quarts d'heure" | House names for the tour lengths. "La visite complète" was already used in 001, 006, 012, 024 and 034. No other track or bridge names the essential or highlights version: the bridges say "cette version courte", as the brief asks. |
| 039 | "…le Portique de la Lavandière, même si les pages en anglais du parc l'appellent le portique de la buanderie." | "En catalan, c'est le Pòrtic de la Bugadera, le Portique de la Lavandière." | Lead's instruction: the official FR name stays, the Catalan name appears once, and the alternative-name clause is dropped. I also changed "Une construction qui emprunte…" to "C'est-à-dire une architecture qui emprunte…", because the English has "That means building that…" and the FR fragment had no verb. |
| 018 | "voient dans cette créature le Python de Delphes" | "ont vu dans cette créature…" | The English changed to "have seen" (past for the dead). |
| 045 | "Les bâtisseurs étaient un oncle et son neveu." | unchanged | **For the lead.** The current English 045 does NOT name the builders. It reads "The builders were an uncle and his nephew.", and its @what says "not named in speech (RA ed2 L9)". Pardo i Casanovas and Berdié i Pardo are named only in the held ed1 text. "Keep as the English" therefore means unnamed, so I did not add the names. Note that 028 does name "l'entrepreneur Josep Pardo i Casanovas". If you want the names spoken, change the English first: 045 FR is at 272/272 words. |

## Navigation fixes
| Track | Before | After | Why |
|---|---|---|---|
| 001 (@where, body), 002 @where, 003 @where | "juste derrière la porte (principale) de Carrer d'Olot" | "juste après la porte…" | The English says "just inside". For someone standing inside the park, "derrière la porte" can mean the street side, so it is ambiguous. "Juste après" matches the direction you have just walked in. 043, 044 and 045 already say "juste à l'intérieur", which is fine. |
| 013 | "jusqu'à l'esplanade derrière la porte de Carrer d'Olot" | "jusqu'à l'esplanade, dans l'enceinte de la porte de Carrer d'Olot" | Same problem. The listener is coming down from inside, so "derrière" would point outside. |
| 025 | "suivez le sens unique vers la sortie, en montant par le côté droit de la salle quand on arrive de l'escalier" | "suivez le sens unique hors de la salle, en montant par son côté droit en venant de l'escalier" | The English says "out" of the hall, not the park exit. "Vers la sortie" could send people to the way out. The wording now matches 024. |
| 024 | "par son côté droit quand on arrive de l'escalier" | "par son côté droit en venant de l'escalier" | This is shorter and addresses the listener. The side is unchanged ("as you came in from the stairway"). |
| 006 | "Longez l'intérieur du mur, après cette maison," | "…en dépassant cette maison," | The English says "past this house". |
| 016 | "Montez la première volée, après les lutins," | "…en passant devant les lutins," | The English says "past the goblins". "Après" could read as "beyond them". |
| 015 | "Une fois passé, arrêtez-vous…" / "après ce point, … et impossible de revenir par ici" | "Une fois le contrôle passé, arrêtez-vous…" / "au-delà, … sans retour possible par ici" | "Passé" on its own had no clear object. The second change keeps the track within its word count, with the same meaning. |
| 019 | "Montez en haut de l'escalier" | "Montez jusqu'en haut de l'escalier" | Idiomatic. |
| 020 | "à gauche quand on arrive en haut" | "à gauche quand vous arrivez en haut" | Formal address. The side is unchanged. |
| 001 | "suivez les panneaux qui descendent vers la porte principale" | "suivez les panneaux et descendez vers la porte principale" | The signs do not descend; the listener does. |
| 034, 035 | "Tenez-vous au banc et regardez la ville" | "Debout près du banc, regardez la ville" | "Se tenir au banc" means holding on to the bench. The English says "Stand at the bench". |
| 038 | "pour laisser passer le sens unique" | "pour laisser passer le flux à sens unique" | The same term as 038 @where, 039 and 040. |
| 040 | "Continuez le chemin jusqu'au bout" | "Suivez le chemin jusqu'au bout" | Idiomatic ("carry on along the path"). |

## Meaning and fidelity
| Track | Before | After | Why |
|---|---|---|---|
| 004 | "a employé le carreau brisé dès les années 1880" | "…pour la première fois dans les années 1880" | The English says "first used … in the 1880s". "Dès" added a nuance the English does not have. |
| 029 | "Son père est mort dès octobre" | "Son père est mort en octobre" | "That October". "Dès" added emphasis. The sentence already continues "quelques mois après leur arrivée". |
| 017 | "Qui montait ces marches … passait devant" | "Quiconque monterait ces marches … passerait devant" | The English uses "would pass", which is hypothetical. |
| 017 | "«un jet en forme de tête de serpent»" | "«un bec en forme de tête de serpent»" | A spout is the outlet, not the jet of water. |
| 015 | "Chaque acheteur payait une redevance" | "Chaque acheteur devait payer une redevance" | The English says "had to pay". |
| 019 | "Un photographe en a compté près de quatre cents à Barcelone" | "D'après un photographe, Barcelone compte près de quatre cents dragons" | "En" pointed back unclearly. The English says "Barcelona has nearly four hundred dragons". |
| 019 | "et dragon ou salamandre pour le parc" | "et un dragon ou une salamandre pour le parc" | Parallel with the two items before it. |
| 012 | "ses propres grottes, pas naturelles non plus" | "ses propres grottes, tout aussi artificielles" | The FR was a fragment. The new wording means the same and has the same word count. |
| 045 | "Soixante parcelles, et deux maisons seulement." | "Soixante parcelles, et seulement deux maisons bâties." | The English says "only two houses ever built". |
| 045 | "la vieille ferme en descendant" | "la vieille ferme croisée en descendant" | The English says "on the way down": a farmhouse you passed. |
| 045 | "Jetez un dernier regard en haut de l'escalier, vers les colonnes" | "…vers le haut de l'escalier, jusqu'aux colonnes" | "Look up the stairway, to the columns". The listener is at the bottom. |
| 024 | "Quatre saisons en verres à vin de quelqu'un." | "Quatre saisons, faites des verres à vin de quelqu'un." | The English says "made of". The old line was hard to parse by ear. |
| 026 | "des arbres de montagne, venus de haut" | "des arbres de haute montagne" | "Mountain trees, from high up". The new wording says the same thing more naturally. |
| 036 | "trois croix à son sommet" | "couronnée de trois croix" | "With three crosses on its top". The old phrase was a dangling apposition. |

## Ear, grammar, naturalness
- 001: "Elle ne demande aucune vue" became "Elle ne demande rien à voir" (@where). "Les visites longues" became "Les visites plus longues". "Nous finissons après la maison de Güell, à la porte…" became "Après la maison de Güell, nous finissons à la porte…".
- 002: "posé dans un mur catalan" became "serti dans un mur catalan".
- 003: "Il a étudié là-bas" became "Il a étudié à Barcelone", because "là-bas" suggests somewhere far away. "a ouvert parmi les premières cimenteries" became "a ouvert quelques-unes des premières cimenteries". "La même histoire qualifie leur lien de «pas simplement…»" was ungrammatical with the quote and became "Selon la même histoire, leur lien n'était «pas simplement…»". "Une maison que…" became "C'était une maison que…".
- 006: "Ses murs du rez-de-chaussée" became "Au rez-de-chaussée, ses murs". "dans la maison" became "à l'intérieur", to keep the word count.
- 007: "complexité compositionnelle" became "complexité de composition". "Des pièces simples, pour la vie quotidienne" became "Des pièces ordinaires, pour la vie ordinaire", which keeps the English echo ("Everyday rooms, for everyday life").
- 010: "au haut du domaine" became "jusqu'en haut du domaine". "cette pente porte la charge" became "cette inclinaison porte la charge".
- 013: "l'ont laissé pousser" became "l'ont laissé continuer à pousser" ("keep growing").
- 014: "une pièce" became "un élément" (of the water system). "pour encore une histoire" became "pour une histoire de plus".
- 016: "Si vous voyez dans les grottes" became "Si vous pouvez voir l'intérieur des grottes".
- 017: "Arrêtez-vous un instant sur ce qui est ici" became "Attardez-vous un instant sur ce qui est là". "la créature … où tout le monde s'arrête" became "la créature … qui arrête tout le monde".
- 018: "Que doit-elle représenter?" became "Qu'est-elle censée représenter?". "Un peu sous le dragon" became "Un peu en dessous du dragon".
- 020: "Comme entendu près du dragon" became "Vous l'avez entendu près du dragon:".
- 026: "Aucune maison n'est venue" became "Aucune maison n'a jamais vu le jour".
- 029: "La plupart de ces années" became "Pendant la plupart de ces années".
- 030: "Quelque part là-dessous" became "Quelque part, là en bas,".
- 032: "vous pourriez être convaincu" became "vous pourriez vous laisser convaincre".
- 034: "un court Extra s'écoute ici, sur le banc, sur les mots qu'il cache" (a double "sur") became "un court Extra, à écouter ici sur le banc, parle des mots qu'il cache".
- 036: "L'essentiel de la verdure visible est venu plus tard" became "La verdure que vous voyez est surtout venue plus tard".
- 041: "selon ses mots catalans" became "selon ses termes en catalan". "Des maisons du domaine du temps de Güell, celle qu'il a choisie pour lui" became "De toutes les maisons du domaine à l'époque de Güell, celle qu'il s'est choisie".
- 042: "Il a promu l'achat" became "Il a encouragé l'achat".
- 043: "un début de soirée de juin" became "par un début de soirée de juin".
- 044: "Quand l'entrée devint payante" became "Avec l'entrée payante". This removes a passé simple in a passé composé paragraph and saves a word.
- 045: "Un gardien gardait la porte" became "Un gardien surveillait la porte", to avoid the repetition.

## Bridges (bridges.txt)
| Key | Before | After | Why |
|---|---|---|---|
| 018 E>021 | "Montez en haut de l'escalier" | "Montez jusqu'en haut de l'escalier" | Idiomatic, and consistent with 019. |
| 018 H>022 | "montez en haut et entrez" | "montez jusqu'en haut et entrez" | Same. |
| 028 E>032 | "la grande place ouverte sur la salle aux colonnes" | "…ouverte au-dessus de la salle aux colonnes" | "Ouverte sur" means "opening onto". The English says "on top of", the same as 031. |
I left the other 18 lines unchanged. They have the same route as the English, the same left and right ("à votre droite face à la ville", "sur votre droite face à l'escalier"), and the same "before the check". 024 H>034 keeps "banc carrelé" and "s'il y a place". The fuller "banc de céramique … s'il y a de la place" would make it longer than the English line (48 words).

## Glossary update
- Tour lengths: **la visite complète / la version essentielle / les incontournables**. The shorter versions are "cette version courte" in the bridges.
- "Just inside the gate" is **juste après la porte** (001–003) or **juste à l'intérieur** (043–045, at the exit). "Derrière la porte" is no longer used for this.
- Portico: **le Portique de la Lavandière**, with the Catalan name "Pòrtic de la Bugadera" once in 039. There is no English alternative name.

## Not changed (noted)
- 035 "y sont partout": I kept the translator's deliberate ambiguity, as the English has it.
- 005 "pôle d'affaires" (English "business end"): it is acceptable spoken French, so I left it.
- There is passé simple in places (001, 012, 015, 025, 037, 038, 045). It sounds natural for narrative in French and is used consistently within each paragraph.
