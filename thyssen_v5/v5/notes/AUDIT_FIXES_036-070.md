# Audit fixes, tracks 036–070 (23 Oct 2026)

Source: research/AUDIT_V5_036-070.md. Tracks 001–035 untouched. 048 untouched (lead instruction: keep as is, fallback in v5/held/048.fallback.perf.txt). Changed: 036, 037, 039, 040, 041, 042, 043, 045, 046, 049, 050, 053, 054, 063, 066, 070. `python3 v5/lint.py 036 … 070`: all 35 OK after the changes (word counts below).

## 053: the O'Keeffe quote (re-read by me)

- Re-read https://www.museothyssen.org/en/collection/artists/okeeffe-georgia/plains-ii with WebFetch, 23 Oct 2026 (one page). It says O'Keeffe "commented on this painting in a letter to the gallery owner Edith Halpert" and quotes: "the color is just plain color out of the tube — red and orange to lemon — It shocks me so that I'm rather struck with it — I don't know what it will get to." Room 46, 1954.
- Restored. It is about this very painting, which is what the paragraph is describing, and it is verbatim. The attribution now follows the page: "dealer" → "the gallery owner Edith Halpert", and the line says she was writing about this picture.
- PLAN's "CUT 'almost shocked her'" was aimed at the old script's paraphrase. That paraphrase stays out. Only the page's own words are used.

## Line edits (before → after)

| Track | Why | Before | After |
|---|---|---|---|
| 036 | Hedge (gown colour not on page) | A young woman stands in her bedroom in a white dressing gown, in front of a tall mirror that tilts on its stand. | A young woman stands in her bedroom, half dressed, in front of a tall mirror that tilts on its stand. |
| 036 | @where, same reason | …a young woman in a white dressing gown, standing in her bedroom before… | …a half-dressed young woman standing in her bedroom before… |
| 036 | Hedge | One of its first owners was the English painter Walter Sickert. | One of its first owners was the British painter Walter Sickert. |
| 037 | Hedge (page: drops still falling) | This one is early afternoon, and it has just stopped raining. Look at the street after the rain, the carriages, … | This one is early afternoon, and the rain is only just stopping. Look at the street, the carriages, … |
| 037 | @where, same reason | …seen from high above just after rain, … | …seen from high above as the rain stops, … |
| 039 | Must-fix 4: Blue Rider anachronism | At the time, Münter was at the heart of the German avant-garde, a member of the Munich group called the Blue Rider. | At the time, Münter was at the heart of the avant-garde in Munich, and within two years she would help found the group called the Blue Rider. |
| 039 | Listening: 1961 story already told in 038 | [lightly] Now the two Kirchners in this room, and a collector's beginning. In 1961, Baron Thyssen began buying modern paintings, and these two were among the very first. They arrived together. | [lightly] Now the two Kirchners in this room. They were among the very first modern paintings the Baron bought, and they arrived together. |
| 040 | Must-fix 7: cue (no door from 37 into 56 on p-3.png) | Keep straight on into Room 37. The opening you pass into Room 56 belongs to the temporary Kenny Scharf exhibition, until 17 January 2027, and is not part of this guide. In Room 37, look for Grosz's red Metropolis. | Keep straight on into Room 37. On your right you pass the way into the Postpop rooms, 53 to 56. They hold the temporary Kenny Scharf exhibition until 17 January 2027 and are not part of this guide. In Room 37, look for Grosz's red Metropolis. |
| 041 | Must-fix 6: name change must be audible | [curious] In 1916, in the middle of a war against Britain and France, a young Berlin painter called Georg Gross changed his name to something that sounded American. He became George Grosz. | [curious] In 1916, in the middle of a war against Britain and France, a young Berlin painter called Georg Gross decided to sound American. He added an E to his first name, so that Georg became the English George. And Gross, spelled with a double S, became Grosz, with an S and a Z. |
| 042 | Must-fix 3: Hitler opened the Great German Art Exhibition (18 Jul 1937), not "Degenerate Art" (19 Jul). The museum page has the slip. | He had fled Berlin the day after Hitler opened the Nazi exhibition mocking modern art as "degenerate". | He had left Berlin that July, the week the Nazis opened their exhibition mocking modern art as "degenerate". |
| 043 | Must-fix 1: colour–shape pairs | …red to the triangle, yellow to the square, blue to the circle. | …yellow to the triangle, red to the square, blue to the circle. |
| 045 | Hedge (page: "may be" Haviland) | His Smoker is a wealthy American friend in a top hat and bow tie, … | His Smoker is probably a wealthy American friend, in a top hat and bow tie, … |
| 045 | Listening: "his" pointed to Gris | When his confiscated stock came up for sale, Kahnweiler bought this one back. | When Kahnweiler's confiscated stock came up for sale, he bought this one back. |
| 046 | Hedge | [curious] There is a good chance this painting spent years hanging the wrong way up. | [curious] This painting may once have been hung the wrong way up. |
| 046 | @listen, same reason | A picture that was probably hung the wrong way up, … | A picture that may once have been hung the wrong way up, … |
| 049 | Pronunciation-safe spelling ("clef" read as "kleff"). "Clé" is the standard modern spelling of the idiom. The official title in @what is unchanged. | In French, la clef des champs, the key of the fields, means freedom. | In French, la clé des champs, the key of the fields, means freedom. |
| 050 | Listening: keep the Watteau reveal for 056 | He turned it into a mask, the pale face of Pierrot, the same sad clown Watteau painted, upstairs in Room 24. | He turned it into a mask, the pale face of Pierrot. |
| 053 | Must-fix 7: quote restored, attribution as on the page | [lightly] To her dealer, Edith Halpert, she wrote that the colour was "just plain color out of the tube", red and orange to lemon. | [lightly] Writing about this picture to the gallery owner Edith Halpert, she said the colour was "just plain color out of the tube", red and orange to lemon. "It shocks me so that I'm rather struck with it," she added. |
| 054 | Must-fix 2: MoMA gave Pollock a one-man show in 1956–57 | …gave him a major show. It was the first time that museum had given a one-man show to a painter of the New York School. Rothko oversaw every detail. | …gave him a major show. Rothko oversaw every detail. |
| 054 | Hedge (Levin: most likely after the show) | This canvas is probably one of the first of that darker turn, though no one can be quite sure. | This canvas was most likely painted just after that show closed, though no one can be quite sure. |
| 063 | Hedge (page: "study of the female nude") | It's the most complete and ambitious nude she ever painted. | It's the most complete and ambitious study of the nude she ever painted. |
| 063 | @listen, same reason | …built her most ambitious nude the old-fashioned way. | …built her most ambitious study of the nude the old-fashioned way. |
| 066 | Hedge (page: "wrongly carries the date") | He even signed it with the wrong year. | It even carries the wrong year beside his signature. |
| 070 | Must-fix 5: Freud portrait is 1981–82 | …laid side by side in one building, from the 14th century to the 1970s. | …laid side by side in one building, from the 14th century to the 1980s. |

@sources updated to match: 039 (the page's Blue Rider slip), 042 (the page's Hitler/Degenerate Art slip, with the audit's DNB dates), 043 (where the pairing comes from: the page gives none), 053 (the verbatim letter text and the page's attribution), 054 (the page's "first one-man show" is not spoken, with the reason).

## Not applied, and why

- **048, eucalyptus hedge** (should-fix): not applied. The instruction was to keep 048 as is. "It grew out of the branches of a eucalyptus tree" still overstates the page, which says the title came later. The lead must decide: the audit's sentence is "It seems to grow out of the branches of a tree; years later Mondrian called it a eucalyptus." That sentence has a semicolon, so it would need rewording to pass lint.
- **Pronunciation lexicon** (036 psyché, Charivari, 039 Fränzi, 047 Proun, 049 Merzbild Kijkduin, 059 Cecchino Bracci, 062 Gennep/Kerssemakers/copaiva, 065 Mata Mua/Hina, 066 Ludwigskirche/Schwabing, 067 Goncharova, 068 Poiret, 070 Cánovas del Castillo and the rest): not respelled in the script. The script is also the PDF text. Per V5_AUDIO_STANDARD §4, respelling is off for ElevenLabs, and names go into the per-engine override list (build/static/pronunciation.py) after listen-QA. Note that the audit's hint "psee-ZAY" for psyché is wrong. French is psee-SHAY.
- **065 "Maori" → "Polynesian"**: optional in the audit. It is the museum's word, and it is not a misreading. Left as is.
- **070 retells 1961**: kept. That is the CLOSE recap, and only the 038/039 repeat was to be removed.
- **Not touched:** "Now find…" openings, tracks with more than 3 dates, and the Essential/Highlights cue question. These are polish or lead decisions, outside this brief.

## On-site checks still open

- 040: the Postpop corridor "on your right" going from 36 into 37. The map (p-3.png) shows it leaving the 36/37 junction to the west, which is the right side when walking south. This is PLAN E.
- 036 and 044: the gown colours. 048: NYC 3 on the wall. 056: which side the Watteau fragment is on. Also PLAN D, the B/C and D/E order, and the J exit, as listed in the audit.
- Possible misreading to listen for: "Brown and Silver I" (050, 051, 052). The voice may say "eye" instead of "one".

## Word counts after (lint)

```
036 OK (315w)   037 OK (216w)   038 OK (275w)   039 OK (324w)   040 OK (225w)
041 OK (313w)   042 OK (202w)   043 OK (291w)   044 OK (317w)   045 OK (347w)
046 OK (301w)   047 OK (327w)   048 OK (220w)   049 OK (263w)   050 OK (306w)
051 OK (223w)   052 OK (300w)   053 OK (339w)   054 OK (279w)   055 OK (346w)
056 OK (335w)   057 OK (186w)   058 OK (227w)   059 OK (338w)   060 OK (316w)
061 OK (192w)   062 OK (297w)   063 OK (303w)   064 OK (294w)   065 OK (318w)
066 OK (210w)   067 OK (298w)   068 OK (290w)   069 OK (211w)   070 OK (291w)
```
