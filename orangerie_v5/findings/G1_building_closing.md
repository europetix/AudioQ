# G1 — Building, history, return visit, closing (tracks 01, 02, 03, 26, 27, 28, 29, 30)

Auditor: G1 · Date: 4–5 Oct 2026 · Source: /home/user/AudioQ/orangerie_v5/source/v4_tracks/NN.txt
Network note: musee-orangerie.fr blocked for WebFetch (EGRESS_BLOCKED); official pages cited from WebSearch snippets (grade OFF where the snippet came from musee-orangerie.fr).

Key sources (referred to below by short tag)
- [ORG-HIST] https://www.musee-orangerie.fr/en/node/24 ("From the orangerie to the museum") — OFF (snippets: 1852 Napoleon III; Lahalle 1960–65 two superimposed levels; Subes staircase; 146 paintings; 1966 Malraux presentation; Brochet 2000–2006, reopened May 2006; 1,000 m² created underground)
- [ORG-ARCH] https://www.musee-orangerie.fr/en/node/198900 (Archives of the genesis of the Water Lilies) — OFF (donation deed 12 April 1922; Lefèvre; eight panels two metres high, 91 m, two oval rooms "which form the infinity symbol"; mounted from 31 Jan 1927, in place by 26 Mar 1927; inaugurated 17 May 1927)
- [ORG-MC] https://www.musee-orangerie.fr/en/whats-on/exhibitions/monet-clemenceau — OFF (letter of 12 Nov 1918, full quote)
- [ORG-HOURS] https://www.musee-orangerie.fr/en/node/197817 + secretsofparis.com — OFF/SEC2 (9–18, closed Tue, last admission 17:15, rooms cleared 17:45, closed 1 May, 14 July morning, 25 Dec; first Sunday free with booking)
- [ORG-ROUSSEAU] https://www.musee-orangerie.fr/en/whats-on/exhibitions/henri-rousseau-ambition-painting + agendaculturel — OFF (25 Mar–20 Jul 2026)
- [ORG-MONET26] https://www.musee-orangerie.fr/en/whats-on/exhibitions/monet-painting-time + offi.fr + ratp.fr — OFF ("Monet, peindre le temps", 30 Sep 2026–25 Jan 2027)
- [LEVELS] sortiraparis.com 219629 + visitparisregion.com — SEC2 (levels 0 / −1 / −2; WG at −1; bookshop-shop and café, opened 2015, at −2 under a glass roof)
- [FOSSES] senat.fr questions 2005 (qSEQ050416978, qSEQ050216189) + parisupdate — SEC2 (Charles IX "Fossés jaunes" wall of 1566 found during works, visible in the basement)
- [WIKI-EN] https://en.wikipedia.org/wiki/Mus%C3%A9e_de_l%27Orangerie — WEAK (Bourgeois 1786–1853, Visconti completion, Poignant pediment with cornucopias)

---

## Track 01 — Welcome — The Orangery in the Garden
| # | Cat | Severity | Quote | Problem | Fix | Source |
|---|---|---|---|---|---|---|
| 1 | C | HIGH | "The museum is open every day except Tuesdays, nine to six." | Opening hours in speech (banned by writer brief). | Delete; hours go in PDF front matter only. | WRITER_BRIEF rule; [ORG-HOURS] OFF (hours themselves correct) |
| 2 | C | MED | "If you've already got your ticket — good." | Ticket talk in speech. | Cut; end on a hook/route cue. | WRITER_BRIEF |
| 3 | B | MED | "Today, it's a hundred and forty-eight paintings" | Official figure is 146 paintings. | "nearly a hundred and fifty paintings" or "a hundred and forty-six". | [ORG-HIST] OFF |
| 4 | B | MED | "Monet painted them as a gift to France after the First World War, a 'haven for peaceful meditation,' in his own words." | Conflation: the "asile d'une méditation paisible" phrase dates from 1909 (Roger Marx's article reporting Monet's idea, Gazette des Beaux-Arts, June 1909), nine years before the gift; most panels were painted during/after the war, not "after" it. Also "in his own words" overstates — it's Marx's reported paraphrase. | "Years before the war, Monet had dreamed of a room that would be, as a critic reported him saying, a refuge for peaceful meditation." Say it once in the tour (also in 28). | bonjourparis / paris.fr snippet (15 June 1909) WEAK; Roger Marx article SEC (not fetched) |
| 5 | B | LOW | "Two rooms upstairs, a longer route downstairs." | The lilies are on the ground (entrance) floor, not upstairs. | "Two rooms on this floor, a longer route downstairs." | [LEVELS] SEC2 |
| 6 | B | LOW | Card WHAT: "one solid wall facing you and a wall of glass on the Seine side" | At the west (Concorde) entrance you face the short west facade with columns and pediment, not the solid north wall. | "The short west end faces you; the glass side runs along the Seine, the solid side along the garden." | [WIKI-EN] WEAK; layout SEC2 |
| 7 | C | MED | whole track (435 words) | Over V5 R-INTRO length (180–280). Also a welcome, a museum summary, a route plan and practical info all in one; overlaps 02 and 03. | Keep: place + the "lilies, downstairs, lilies again" promise. Move collection summary to 13. | V5_AUDIO_STANDARD §2 |
| 8 | C | LOW | "There's\n\nno wrong day to come." | PDF page break mid-sentence in source text. | Rejoin when rebuilding the script. | source |
| 9 | B | LOW | "early-twentieth-century dealer... between 1914 and 1934... died young — at forty-two" | Correct (b. 1891, d. Oct 1934). | none | [ORG-HIST] OFF |

## Track 02 — The Glass Wall & the Stone Wall
| # | Cat | Severity | Quote | Problem | Fix | Source |
|---|---|---|---|---|---|---|
| 1 | C | MED | "Look at the building." (opening) | Commander-voice opener (Rule 12). | Open with the hook: "This building was made for orange trees, not for paintings." | WRITER_BRIEF |
| 2 | B | MED | "In 1921 ... the French state was looking for somewhere to display the Water Lilies ... Clemenceau ... pushed for them to come here ... They added skylights to the roof." + "they built two oval rooms" | Basically right but compresses: Orangerie chosen 1921 (after the Rodin-garden pavilion project was dropped); deed 12 April 1922; Lefèvre's conversion 1922–27. Duplicates 03 almost word for word. | Keep only the light/building story here; move dates to 03. | [ORG-ARCH] OFF |
| 3 | B | LOW | "the right architecture for holding eight panels of pondwater" | Eight compositions on 22 panels; "panels" contradicts 01/03. | "eight great compositions". | [ORG-ARCH] OFF |
| 4 | B | LOW | "carved decoration above the doorways ... ears of corn, cornucopias, plants" | Only the cornucopia pediment (Charles-Gallois Poignant) is sourced; "ears of corn, plants" unverified. | "the carved pediment with cornucopias, symbols of plenty". | [WIKI-EN] WEAK |
| 5 | B | LOW | "Firmin Bourgeois — he died the year after it was completed, so the entrance facades were finished by Louis Visconti" | Bourgeois d. 1853 and Visconti completed it — consistent but only wiki/blog-grade sourcing; Visconti also died Dec 1853. | Acceptable; soften to "finished by Louis Visconti, the architect of the new Louvre". | [WIKI-EN] WEAK + pariszigzag WEAK |
| 6 | C | LOW | trailing "★ ANCHOR · 4:00" in the spoken text | Header of the next track leaked into text (PDF extraction). Must not be voiced. | Strip. | source |
| 7 | E | LOW | WHERE: "Just inside the entrance, or pause again outside if you can see the south facade" | The glass south facade is only visible from the Seine-side terrace, not from inside the entrance hall; the track asks the visitor to look at both walls. | Play outside on the terrace before entering, combined with 01. | layout SEC2 |
| 8 | B | OK | 1852, Napoleon III, glass south / blind north | Confirmed. | — | [ORG-HIST] OFF, [WIKI-EN] |

## Track 03 — From Citrus Trees to Monet
| # | Cat | Severity | Quote | Problem | Fix | Source |
|---|---|---|---|---|---|---|
| 1 | B | HIGH | Card LISTEN: "a contract signed two days after the Armistice" | Wrong: 12 Nov 1918 was a LETTER, one day after the Armistice; the deed of donation was signed 12 April 1922. Contradicts the spoken text. | "a letter written the day after the Armistice". | [ORG-MC], [ORG-ARCH] OFF |
| 2 | B | MED | "The floor plan, from above, looks like the symbol for infinity. Two ovals, meeting at a single point." | The infinity reading is the museum's own description (OK), but the ovals do NOT meet at a point: they are linked by a passage/vestibule (track 09 itself calls it a "narrow corridor"). | "Seen from above, the two ovals, joined by a short passage, are often compared to the sign for infinity." | [ORG-ARCH] OFF |
| 3 | B | MED | "canvases nearly seven feet tall and, in some cases, more than fifty feet long" | Single canvases are c. 2 × 4.25 m (~6½ × 14 ft); only the assembled compositions reach ~17 m (~55 ft). | "canvases two metres high, set side by side into compositions more than fifty feet long". | [ORG-ARCH] OFF (2 m high, 91 m total) |
| 4 | B | LOW | "Monet was eighty-one years old in 1921" | Born 14 Nov 1840 — 80 for most of 1921. | "Monet was eighty". | standard biography SEC2 |
| 5 | B | LOW | "The donation contract was signed in 1922." | Correct (12 April 1922); "deed of gift" is the better term. | optional date. | [ORG-ARCH] OFF |
| 6 | B | OK | Letter quote "I'm about to finish two decorative panels which I want to sign on the day of victory, and ask you to offer to the State." | Real, accurately paraphrased. | Optional fuller ending: "...it's the only way I have of taking part in the victory." | [ORG-MC] OFF |
| 7 | B | LOW | "The museum opened to the public in May 1927" / "installed a few months later" | Correct: mounted 31 Jan–26 Mar 1927, inaugurated 17 May 1927. | Could say "the seventeenth of May, 1927". | [ORG-ARCH] OFF |
| 8 | B | LOW | "displayed permanently from 1984" | First shown 1966 (Malraux); 1984 permanent hang is plausible but not found in an official snippet. | "first shown in 1966" (verified) or cut. | [ORG-HIST] OFF (1966) / 1984 NONE |
| 9 | C | MED | 482 words, 9+ dates | Over length (ANCHOR 250–360) and over the 3-dates rule; repeats 01/02. | Pick three dates: 1852, 1918 letter, 1927 opening. | V5 standard |
| 10 | B | LOW | "A hundred and twenty years of small decisions" (card) | 1852→1927 is 75 years; 1852→1984/2006 is 130–154. Vague number. | "Seventy-five years of small decisions". | arithmetic |

## Track 26 — Coming Back Up — The Second Visit
| # | Cat | Severity | Quote | Problem | Fix | Source |
|---|---|---|---|---|---|---|
| 1 | E | MED | Structure: ground floor lilies → −1 WG → back up to lilies → exit | Feasible (open stairs/lift link 0, −1 and −2; the one public door is the west entrance on the ground floor, so returning through level 0 is on the way out). BUT the bookshop and café are on level −2, beside the temporary exhibition ("Monet, peindre le temps" runs 30 Sep 2026–25 Jan 2027); many visitors finish there. Tour never sends them to −2. | 26 WHERE: "When you've finished downstairs — and the shop and café one level further down, if you want them — take the stairs back up to the oval rooms." Remove "bookshop on the lower level" ambiguity in 30. Ask field test to confirm re-entry to the oval rooms is not blocked by one-way flow on busy days. | [LEVELS] SEC2; [ORG-MONET26] OFF |
| 2 | C | MED | "Take a breath at the top of the stairs." (opening) | Commander opener. | Open with a hook: "Nothing on these walls has changed in the last hour. Two other things have." | WRITER_BRIEF |
| 3 | C | MED | "We'll talk about what Monet actually built, architecturally, in the next track." | "next track" jargon. | "Then look up at the ceiling — that's where the next story is." | WRITER_BRIEF |
| 4 | B | LOW | "after listening to artillery from his garden for four years" | Monet and secondary sources say the guns could be heard from Giverny at times (1914, 1918 offensives); "for four years" overstated. | "while the guns of the front could sometimes be heard from his garden". | BBC clip / americanacademy WEAK–SEC2 |
| 5 | B | LOW | "The first composition you'll see again is, probably, Morning." | Depends on which room/door; Room 1 orientation not verified by me. | Defer to G2 placement audit; otherwise say "the composition straight ahead". | could not check |
| 6 | C | LOW | trailing "★ ANCHOR · 4:00" | Leaked header. | Strip. | source |
| 7 | D | LOW | Long list recap of WG painters | Redundant with 13–25; over length (406 words). | Keep 2–3 names, one image. | V5 standard |

## Track 27 — What Monet Built Here — The Oval Rooms as Architecture
| # | Cat | Severity | Quote | Problem | Fix | Source |
|---|---|---|---|---|---|---|
| 1 | B | HIGH | "The Walter-Guillaume collection — which had been on the ground floor — was moved downstairs" | Wrong: Lahalle's 1960–65 works inserted an upper level above the Water Lilies; the WG collection was shown UPSTAIRS (reached by Subes's monumental staircase), which is why the lilies lost their daylight. | "The Walter-Guillaume collection, which had been hung on the floor built above these rooms, moved to new galleries dug under the garden terrace." | [ORG-HIST] OFF |
| 2 | B | MED | "a skylight in the middle — a circle of glass and stretched fabric scrim" | The whole oval ceiling is a translucent velum under a glass roof (oval, not a central circle). | "The whole ceiling is a pale stretched-fabric velum under a glass roof." | Studio International / parisupdate / honoluluadvertiser 2006 SEC2 |
| 3 | B | MED | "It took the museum eighty years and four major renovations to get back to where it started." | "Four major renovations" unsourced (known campaigns: 1922–27 Lefèvre, 1960–65 Lahalle, 2000–06 Brochet; possibly 1978–84 works). | "It took almost eighty years to get back to where Monet started." | NONE |
| 4 | B | LOW | "a second floor was added... false ceiling blocking the skylights... gone for nearly forty years" | Substantively right (alterations 1960–65; works began Jan 2000; reopened May 2006; press said "more than four decades"). "Between roughly the 1960s and 2006" fine. | Optional: "from the mid-1960s until 2006". | [ORG-HIST] OFF; honoluluadvertiser 2006 SEC2 |
| 5 | B | LOW | "In 2000, a full renovation began. The architect Olivier Brochet ran the project." | Correct (Brochet Lajus Pueyo; closed Jan 2000, reopened 17 May 2006). | — | [ORG-HIST] OFF |
| 6 | D | MED | lower level "newly excavated basement rooms" | Missed story: the excavation uncovered Charles IX's 1566 "Fossés jaunes" city wall, now visible on the lower level — a real, checkable thing to look at and the reason the works overran. | Add one line here or in 13. | [FOSSES] SEC2 |
| 7 | B | LOW | "This is, by some accounts, the first piece of installation art" / "He insisted that nothing else be displayed" / "The floor is a quiet polished stone" | Hedged claim OK; "nothing else" and floor material not verified. | Keep hedge; drop floor detail unless confirmed on site. | NONE |
| 8 | C | MED | "One more track in here, before we walk out. The next one is just for sitting." + trailing "★★ HEAVY · 4:30" | "track" jargon; leaked header. | "Before you leave, find a place on the bench." Strip header. | WRITER_BRIEF |
| 9 | C | MED | "Look around this room." (opening), 510 words | Commander opener; over ANCHOR length. Repeats 03/04 on Lefèvre & mounting. | Cut repetition; open on the 1960s ceiling story as hook. | V5 standard |
| 10 | D | LOW | — | Possible coverage gap: 1920s–40s neglect of the rooms and the 1944 Liberation shell damage to the panels; André Masson's 1952 "Sistine Chapel of Impressionism". | Consider one line; verify first. | could not check |

## Track 28 — Sitting in the Silence — One Last Look
| # | Cat | Severity | Quote | Problem | Fix | Source |
|---|---|---|---|---|---|---|
| 1 | B | HIGH | "It's also why Monet didn't want photographs of these. He didn't want them reproduced. He said photographs killed them. He was right." | No source found for any such Monet statement; presented as a quote. Likely invented. | Delete, or rephrase as narrator's own view: "No photograph has ever quite caught them." | NONE (searched) |
| 2 | B | MED | "in his words, an asylum of peaceful meditation. He said that out loud, in 1909" | Source is Roger Marx's article (Gazette des Beaux-Arts, June 1909) reporting Monet's idea; "said that out loud" and "in his words" overstate. Same phrase also used in 01 (rendered differently: "haven"). | "In 1909 a critic reported Monet's dream of a room that would be a refuge for peaceful meditation." Use once in the tour. | paris.fr/bonjourparis snippet WEAK; Marx article not fetched |
| 3 | B | MED | "He gave them to France in 1918, the day after the war ended." | In 1918 he offered two panels by letter; the gift of the cycle was formalised 12 April 1922. | "He offered them to France the day after the Armistice." | [ORG-MC], [ORG-ARCH] OFF |
| 4 | B | OK | "The rooms opened in 1927, five months after he died" / "seventeen more years" | 5 Dec 1926 → 17 May 1927 ≈ 5½ months; 1909→1926 = 17. OK. | — | [ORG-ARCH] OFF |
| 5 | C | MED | "Sit down. Get comfortable." (opening) ; 458 words | Commander opener; "This track is mostly quiet" yet 458 words — not quiet. | Hook first; cut to ~250 words; put real silence (direction-layer long pause) in. | V5 standard |
| 6 | E | LOW | "The doors are over there — through the corridor, past the entrance, back into Paris." | Single public door is the west entrance on level 0 (OK), but visitors wanting the shop/café must go down to −2. "over there" meaningless in audio. | "The way out is back through the entrance hall, at the Concorde end." | [LEVELS] SEC2 |
| 7 | B | LOW | "You can buy postcards of these compositions in the museum shop" | Shop exists (level −2) — fine. | — | [LEVELS] SEC2 |

## Track 29 — Walking Out — The Tuileries, the Concorde, the Seine
| # | Cat | Severity | Quote | Problem | Fix | Source |
|---|---|---|---|---|---|---|
| 1 | C | MED | "One last track. Practical information you might need. Then we're done." | Track jargon / practical-info pointer. | End on the Tuileries image. | WRITER_BRIEF |
| 2 | B | LOW | "The Louvre is the biggest museum in the world." | Contested superlative. | "the most visited museum in the world" or "one of the largest". | SEC2 general |
| 3 | B | LOW | "a five-minute walk along it brings you to the Musée d'Orsay" | From the Pont de la Concorde to the Orsay entrance is ~1 km, 12–15 min. | "a fifteen-minute walk". | map arithmetic |
| 4 | B | LOW | "There's no marker." (guillotine site) | Not verified. | Drop or "there's nothing to mark the spot today". | could not check |
| 5 | B | OK | Catherine de' Medici 16th c., Le Nôtre 17th c.; Luxor obelisk >3,000 years, erected 1836; executions 1793–94 incl. Louis XVI & Marie Antoinette; Orsay–Orangerie linked since 2010 | Confirmed. | — | SEC2 |
| 6 | C | LOW | 436 words, opens "You're outside. Take a breath" | Over length; commander-ish opener; "If ... the Orsay is open" fine. | Trim to 250–300. | V5 standard |

## Track 30 — Practical Info & Goodbye
| # | Cat | Severity | Quote | Problem | Fix | Source |
|---|---|---|---|---|---|---|
| 1 | C | HIGH | Hours, last admission, Friday late nights, closures, tickets, billetterie URL, Museum Pass, under-26, first Sunday | Entire first half breaks the "no hours/prices/booking/temporary exhibitions in speech" rule. | Move to PDF front matter; delete from audio. Track becomes a short goodbye (or merge goodbye into 29). | WRITER_BRIEF |
| 2 | B | HIGH | "There's a major temporary exhibition on right now: Henri Rousseau, The Ambition of Painting. It runs through July twentieth of this year, 2026." | Expired on 20 July 2026 — false for anyone hearing it now. | Delete. Also fix 19 if it refers to the show as current (other auditor). | [ORG-ROUSSEAU] OFF |
| 3 | B | HIGH | "After July, the next major show is Monet and Time, opening in late September and running through March of next year." | Title is "Monet, peindre le temps / Monet, Painting Time"; dates 30 Sep 2026–25 Jan 2027 (not March); already open now. | Delete from audio (rule). If kept in PDF: correct dates. | [ORG-MONET26] OFF |
| 4 | B | MED | "the rooms start closing at five-thirty" | Official: rooms cleared from 17:45. | PDF only, corrected. | [ORG-HOURS] OFF |
| 5 | B | MED | "Friday late nights — open until nine, with reduced admission after six" | Not found on official page; unverified. | Drop. | NONE |
| 6 | B | LOW | "July the fourteenth in the morning only" | Correct (closed the morning of 14 July). Phrasing in speech ambiguous. | PDF only. | [ORG-HOURS] OFF |
| 7 | B | MED | "There's a bookshop at the Orangerie itself, on the lower level — ... including the giant infinity-symbol floor plan postcard." | Bookshop is on level −2 (below the WG level). The "giant infinity-symbol floor plan postcard" is unverified, probably invented. | "The bookshop and café are on the lowest level, under a glass roof." Drop the postcard. | [LEVELS] SEC2; postcard NONE |
| 8 | B | LOW | "The Orangerie is small — you can do it in an hour." | Contradicts 01 ("an hour and a half"). | Align or drop. | internal |
| 9 | B | LOW | "two of the deepest collections of modern painting anywhere in the world" | Hyperbole; Nymphéas is one work-cycle, not a "collection". | "two of the most moving rooms of modern painting in Paris". | — |
| 10 | B | LOW | "EU citizens under twenty-six get free admission" | Official wording is 18–25 residents of EU/EEA (and all under 18). Rule makes it moot. | PDF only. | [ORG-HOURS] OFF/SEC2 |
| 11 | C | LOW | 517 words; "that\n\nwasn't" page break | Over length; source artifact. | Goodbye ≤150 words. | V5 standard |

---

## Cross-track / route notes
- Circulation (E): Level 0 = entrance hall (west, Concorde side) + two oval rooms; level −1 = Walter-Guillaume; level −2 = temporary exhibitions, bookshop-shop and café (since 2015) under a glass roof [LEVELS SEC2]. The "lilies → downstairs → lilies again" plan fits (exit is via level 0), but the tour should mention −2 once (shop, café, toilets, and the current "Monet, peindre le temps" exhibition, without dates) so visitors don't miss the return or get stuck downstairs. Field test should confirm no one-way rule blocks re-entry to the oval rooms on busy days.
- Infinity (B): Museum's own text says the two ovals "form the infinity symbol" [ORG-ARCH OFF]; keep, but as a comparison, never "meeting at a single point" (03), and never as Monet's own stated intent.
- Monet quotes (B): 1918 letter = real (OFF). "Asile d'une méditation paisible" = 1909, Roger Marx reporting Monet (use once, attributed honestly). Frontispiece "l'illusion d'un tout sans fin, d'une onde sans horizon et sans rivage" = same Marx 1909 article (consistent). "Photographs killed them" (28) = no source, remove.
- Redundancy (D): 01/02/03 tell the 1921–1927 story three times; 26/27/28 give three tracks to the return visit; 30 is mostly banned content. Suggest: 01+02 merge (outside, building), 03 dates, 26+27 merge (return + ceiling story), 28 short sit, 29+30 merge (walk out + goodbye).
- Leaked headers "★ ANCHOR · 4:00" / "★★ HEAVY · 4:30" in 02, 26, 27 spoken text, and page-break splits in 01 and 30 — strip before rendering.

## Confirmed OK
- Built 1852 on the orders of Napoleon III as a winter shelter for the Tuileries citrus trees; glass south (Seine) side, nearly blind north side [ORG-HIST OFF, WIKI].
- Firmin Bourgeois architect, completed by Louis Visconti; cornucopia pediment [WEAK only].
- Tuileries Palace burned 1871; state assigned the building to the Fine Arts under-secretariat in 1921 for living artists [ORG-HIST / WIKI].
- Monet's letter to Clemenceau, 12 Nov 1918, wording [ORG-MC OFF].
- Original plan in the Hôtel Biron (Musée Rodin) garden, then the Orangerie [SEC2].
- Deed of gift 12 April 1922; architect Camille Lefèvre; eight compositions, 22 panels, 2 m high, ~91 m total, marouflaged to the walls [ORG-ARCH OFF].
- Monet died 5 Dec 1926; installation Jan–Mar 1927; inaugurated 17 May 1927 [ORG-ARCH OFF].
- Lahalle 1960–65 alterations, upper level, daylight lost; WG acquired 1959 and 1963; 1966 presentation [ORG-HIST OFF].
- Brochet renovation, closed Jan 2000, reopened May 2006; skylights restored; 1,000 m² created underground for WG [ORG-HIST OFF].
- Paul Guillaume 1891–1934, died at 42; Domenica's second husband Jean Walter (d. 1957).
- Hours as spoken in 01 (9–18, closed Tue) are correct — but banned in speech.
- Tuileries history, Luxor obelisk 1836, Concorde executions; Orsay–Orangerie public establishment since 2010.

## Could not check
- Official circulation/one-way rules for re-entering the oval rooms after the lower levels; exact exit route (no official floor plan reachable).
- Which composition faces you on re-entering Room 1 (track 26 "probably Morning") — defer to the Water Lilies placement auditor.
- WG "displayed permanently from 1984".
- Floor material of the oval rooms; "nothing else displayed" as Monet's explicit condition.
- "Friday late nights until nine" (not on official hours snippet).
- Any marker at the guillotine site, Place de la Concorde.
- 1944 Liberation damage to the panels (candidate coverage line, unverified here).
- Full text of Roger Marx, "Les Nymphéas de M. Claude Monet", Gazette des Beaux-Arts, June 1909 (attribution of the "meditation" phrase).
