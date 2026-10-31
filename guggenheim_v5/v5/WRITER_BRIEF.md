# WRITER BRIEF — Guggenheim Museum Bilbao: the building and the permanent works, Yo Tours (31 Oct 2026)

You are writing part of a new English walking audio guide to the Guggenheim Museum Bilbao. It covers the building inside and out and the permanent works: Puppy, Serra's *The Matter of Time*, Holzer, the Chillidas, Kapoor, Nakaya's fog, Klein's fire, Maman, Buren's arches and La Salve Bridge. It is built from scratch to the series standard.

**The competition is weak, but free.**
- The official guide is free with admission, scanned by QR code on your phone. Its outdoor works and Serra are web text, and its written routes give gallery numbers with no directions.
- The app tours are thin and badly rated.
- Popular claims are often wrong:
  - the crumpled-paper legend;
  - "Bilbao kept Puppy by popular demand";
  - "ETA tried to blow up Puppy";
  - Soviet-submarine titanium;
  - "the lost Snake";
  - "the Holzer columns show her Truisms";
  - "Tulips on the terrace";
  - a "50 m" Atrium.

**What ours must be:** right places, spoken directions by landmarks, verified facts, honest about the deal and its critics, and good to listen to.

**The user's complaint about the last guide was that it felt thin.** Give the stories, the people, the verbatim quotes and the things to look at that PLAN gives you. Write in the upper half of the word range wherever the material is real. Never pad.

Priorities: navigation accuracy first, accuracy of fact second, storytelling third.

Project root: /home/claude/audioq/guggenheim_v5 (all paths below are relative to it).

## Read first, in this order
1. **v5/V5_AUDIO_STANDARD.md**: the writing and direction standard (binding; §2 and §3).
2. **Voice anchors** (spoken, warm, composed; hook → story → turn → look → payoff):
   - /home/claude/audioq/cathedral_seville_v5/v5/tracks/004.perf.txt
   - /home/claude/audioq/cathedral_seville_v5/v5/tracks/014.perf.txt
   - /home/claude/audioq/alcazar_v5/v5/tracks/007.perf.txt
3. **v5/PLAN.md**: binding for place, order, @room, @title, content, the allowed facts with their source keys, what NOT to say, the exact cue (last column), DATED items, the NEVER list, ALT cues and the bridge table. Read its Conventions: directions by fixed features; gallery numbers only 101, 104, 204, 304; the two timing exceptions.
4. **research/FACTS_BUILDING_AND_PERMANENT_OCT2026.md** for the rows PLAN cites (F-A1 … F-I10). Read its §K (popular errors) and §L (unverified) whole. Then **research/VISIT_ROUTE_AND_SPACES_OCT2026.md** and **research/map/OFFICIAL_MAP_NOTES_30OCT2026.md**, with the five map screenshots.

## Accuracy rules (non-negotiable)
- **Sources.** Every load-bearing fact must be confirmed on the source PLAN gives: the museum's own pages first (guggenheim-bilbao.eus: work pages, routes, the building pages, press releases), then the institution or press source named.
  - Use WebFetch, one page at a time, never in bursts; WebSearch only to find a page.
  - Never a browser, never curl; never complete a CAPTCHA.
  - Wikipedia never alone. Anything only in a search snippet (SNIP) is not scripted.
  - If a page now says something different, use the page and flag it in your notes.
- **Wording.** Use the FACTS safe wording for conflicts ("about 33,000 sheets", "about a third of a millimetre", "about 100 million dollars to build", "on time and on budget", "early 1991", "1991" for the competition, "almost nine metres", "a sac of marble eggs" with no number).
- **Attribution.** Attribute claims:
  - "the museum's own studies" for impact figures;
  - "the builder calls it…" for the BIM claim;
  - "AP reported it in English as…" for the King's words;
  - "the story goes" for Krens jogging and Gehry's carp.
  - Legends are told as legends.
- **Quotes.** Verbatim, short, attributed by name, in English. Where PLAN marks a quote ES (Spanish) or "EN tr.", translate faithfully and attribute it plainly ("as one Spanish paper put it", "in the museum's English"). Never invent a quote or tidy one into something the person didn't say. PLAN says how to handle the coarse Gehry quote: paraphrase it.
- **Tense.** Past tense for Frank Gehry (died 5 December 2025), Richard Serra (died March 2024), Louise Bourgeois (1911–2010), Eduardo Chillida (1924–2002) and Yves Klein. The lint checks for "Gehry is", "Gehry says" and the like.
- **Views and placements.** Never describe a view or a placement the sources don't support. From the terrace, only the pond, Kapoor, the fire nozzles and the materials, plus Maman "if you can see her". Everything else is an ONSITE item, not speech.
- **Dated items.** Visitor numbers, the impact study, Puppy's replanting state and "turns thirty in 2027" each go in one separate sentence that can be cut.
- **Practical limits.** No prices, opening hours, tickets, admission, membership, the bag check or cloakroom, the official QR guide or app, the restaurants (Nerua, the Bistró, the Bar), the café, the shop, or the auditorium.
  - **The two exceptions, and only these words:** the fog runs "on the hour" (for "about eight minutes"); the fire fountains burn only "after dark". No clock times, no months, no "every fifteen minutes".
  - 001 may say once: "there's a lift for wheelchair users from the plaza, a ramp on the river side, and lifts between all the floors". It never names the Bar.
- **Temporary exhibitions do not exist in this guide.** Never name a show, an artist on show, a gallery number other than 101, 104, 204 or 304, or anything in the floor-3 Collection display. "You'll walk past other galleries" is the most you may say.

## Txema Agirre (track 003, and one clause in 020): handle with respect
- He was a person, not a plot point. Name him in full once (José María Aguirre Larraona), then as "Txema Agirre", the name on the plaza.
- State plainly:
  - his age and his newborn son;
  - what he did: he went to check the van;
  - that he was shot and died of his wounds;
  - that the planters hid grenades meant for the opening;
  - where he is remembered.
- No dramatisation:
  - no "chilling", "brave hero" in our voice (the Basque president called him a hero: attribute it), "foiled", "cowardly", "terrorists' plot" adjectives;
  - no description of the shooting or of wounds;
  - no date of death (the sources conflict);
  - no attackers' names, trials or politics.
- Do **not** say ETA tried to blow up Puppy. The target was the inauguration; the planters were placed beside Puppy. Do not dwell on the flowers.
- Direction tags: [quietly] or [reverent] only; no [amused], [wry], [lightly] or [conspiratorial]. Use one [long pause] before the cue, and no music sting on this track.
- His sister's words are **held** (headline only). Use them only if the lead gives you the confirmed text.

## Navigation rules
- @room and @title exactly as PLAN. @where: where to stand and how to recognise the place, in 1–2 sentences, with no internal notes or check codes.
- **The LAST paragraph of every track (except CLOSE) is the cue**, as in PLAN's last column. It gives the destination plus one fixed feature in 1–3 sentences and ends with the spoken form `<place> · <title>`. You may smooth the wording, but you may not change the destination, the feature or the order. Keep the [Oxx] tags out of the spoken text; list them in @where.
- **Allowed landmarks:**
  - on the plaza: Puppy, the plaque in the small square in front of Puppy, Calle Iparragirre, the broad stairway;
  - inside: the Hall, ZERO in the lobby, the Atrium and its skylight, gallery 101, gallery 104 "the long gallery under the bridge", the terrace off the Atrium on the river side, the glass lifts and walkways, the balcony opposite gallery 204 (second floor), the balcony opposite gallery 304 (third floor);
  - outside: the river walk, the pond, the tall tree of silver balls, Maman "by the footbridge" (never name it), La Salve Bridge, the tower, the red frame.
- **Forbidden until PLAN says confirmed:** left/right, "straight ahead", "turn round", compass words, "upstream/downstream", distances, "the exit is…", "out through the terrace", "under Maman", "up the tower". "Calle Iparragirre at your back" (004) is the one sourced exception.
- Floors: say "the second floor" and "the third floor". The Hall/Atrium level is "the Atrium level". Never "ground floor" or "first floor".
- Tracks heard while moving say so: 005 on the stairway, 017 in the lift, 019 going down, 021 walking round. They follow PLAN's "no visual reference for the first ≈ N words".
- Extras (014, 020, 024, 028) are announced by the track before them. That track's cue also names the next main stop.
- Never "next track", "right this way", "just over there", "as you can see on your left".

## Bridges (shorter versions)
For every row of PLAN §3 "Bridges" whose Track is one of yours, write ONE spoken bridge of 15–45 words.
- It starts "On this shorter tour," and gives the route to the next stop of that version, with the place and one landmark, exactly as the row says.
- It is played after the track's normal cue, so it must make sense after it ("On this shorter tour, skip the plaque: stay on the plaza…").
- Put the bridges in v5/bridges/<first>-<last>.txt, one per line: `NNN E>MMM: text` or `NNN H>MMM: text`.

## Version-neutral sentences
Some sentences must work in every version that contains the track:
- 007: one sentence naming Holzer's columns, because E skips 008;
- 013: one clause on Snake being the oldest, because E skips 011;
- 022: "the pond pays tribute to the Nervión", because H never hears 015;
- 029: one sentence on 400,000 needed and about 1.3 million who came, because H skips 019.

Never refer to a track the listener may not have heard ("as you heard at the plaque") unless every version containing your track also contains that one. PLAN marks the safe callbacks: 024 → 015; 026 → 017; 020 → 003; 027 → 022 is safe in E and Full but **not** in H, which has 027 without 022, so phrase it as "if you looked into Kapoor's spheres, …".

## Writing rules
- Never open with a command. Open with a hook: a surprising fact, a person, a tension. The hooks PLAN gives are suggestions; better ones from the same sources are welcome.
- **Length** (spoken words, tags excluded): R 180–280 · W 250–360 · ANCHOR/CLOSE 250–360 · X 150–230. Aim at PLAN §3's "Aim" per track (upper half where the material is real). The whole Full guide sits near 8,200 words; don't run far over.
- Average sentence 11–16 words; vary them; max ~30. No parentheses, no semicolons, ≤ 2 em-dashes, no exclamation marks: even the King's line in 020 ends with a full stop in speech.
- **One clear "you" moment per track:** what to look at now, in the object itself. Look-prompts mid-track are welcome.
- Numbers spoken as people say them ("about thirteen metres", "almost nine metres", "about a third of a millimetre"). At most ~3 dates per track. Years as digits.
- Name a person, then use "he" or "she". Give an English gloss once per track for Basque or Spanish words: *Besarkada* "embrace", *Arku gorriak* "red arches", *Ertzaintza* "the Basque police", Lehendakari "the Basque president". Pronounce *Museoa* in 001 only.
- **Direction tags** only from the standard: [pause] [long pause] [warmly] [quietly] [amused] [curious] [conspiratorial] [reverent] [wry] [lightly], and *word* for stress. About one delivery tag per paragraph.
- One warm or wry aside per track, at most (never in 003).

## Output — one file per track: v5/tracks/NNN.perf.txt
```
@id: NNN · Guggenheim Bilbao · 31 Oct 2026 edition
@section: <exactly the PLAN section name: The plaza | Going in | The Matter of Time | Up and down | The river walk>
@room: exactly as PLAN ("Gallery 104 · the first sculptures")
@type: ANCHOR | R | W | X | CLOSE
@title: exactly as PLAN (Extras keep "Extra · ")
@where: <1–2 sentences: where to stand and how to recognise it; then the [Oxx] tags this track depends on, in brackets at the end>
@what: <artist, official title, date, medium, size if useful, the credit "Guggenheim Bilbao Museoa"; plus other works covered>
@listen: <1 sentence: what the track is about>
@brief: <one line: who is speaking, to whom, in what mood>
@pace: slow | medium-slow | medium | medium-fast
@energy: e.g. 2→4  (003: 1→2)
@sources: <URLs read, with what each confirmed; OFF = read on an official page; SEC = secondary; one line each>
---
<spoken body, paragraphs separated by blank lines, last paragraph = cue>
```
Write v5/notes/<first>-<last>_NOTES.md, with this per track:
- the pages you read (URL and what each confirmed);
- anything you could not confirm (and what you did instead);
- any wording that differs from PLAN, and why;
- any quote whose exact words you changed.

**Check before finishing:** `python3 v5/lint.py <your track numbers>`. Every track must print OK; the lead adapts the lint per PLAN §1 "Lint".

**Final reply ≤ 8 lines:** the tracks written, what you could not verify, and what the lead must decide.
