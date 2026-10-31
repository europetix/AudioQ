# WRITER BRIEF — Poble Espanyol de Montjuïc (Barcelona), Yo Tours (31 Oct 2026)

You are writing part of a new English walking audio guide to the Poble Espanyol on Montjuïc: the "Spanish Village" built for the 1929 Barcelona International Exhibition, with 117 full-size buildings modelled on real ones all over Spain. The guide walks one loop from the Ávila gate up to the monastery and back to the Plaza Mayor, and tells, house by house, where the originals are and what was changed. It is built from scratch to the series standard; the user's old guide is not used.

**The competition is weak.**
- The official guide is a paid, rented tablet, available only in the daytime; visitors find it "somewhat difficult to follow" and walk round "without listening to the audio" (COMP).
- Reviewers' real complaints: "without it nobody explains which town each building represents"; the route is "a little cofusing"; the monastery and the side streets are hard to find; "more crafts in action"; "a tourist set lined with shops".
- Popular claims are often wrong:
  - "built for the 1992 Olympics";
  - "exact replicas" (the operator's own page says "exactly replicate");
  - "they visited 1,600 villages";
  - "a replica of Riaza's square";
  - "Puig i Cadafalch designed the monastery" (on the operator's own events page);
  - "the Andalusian quarter was always there";
  - "medieval frescoes";
  - "a concentration camp";
  - "it inspired Disney".

**What ours must be:** right places, spoken directions by street names, squares, house numbers and landmarks, verified facts, the politics told evenly, and good to listen to. The answer to "it's just a film set" is the story of how and why each piece was chosen.

**The user's complaint about the last guide was that it felt thin.** Give the stories, the people, the verbatim quotes and the things to look at that PLAN gives you. Write in the upper half of the word range wherever the material is real. Never pad.

Priorities: navigation accuracy first, accuracy of fact second, storytelling third.

Project root: /home/claude/audioq/poble_v5 (all paths below are relative to it).

## Read first, in this order
1. **v5/V5_AUDIO_STANDARD.md**: the writing and direction standard (binding; §2 and §3).
2. **Voice anchors** (spoken, warm, composed; hook → story → turn → look → payoff):
   - /home/claude/audioq/cathedral_seville_v5/v5/tracks/004.perf.txt
   - /home/claude/audioq/cathedral_seville_v5/v5/tracks/014.perf.txt
   - /home/claude/audioq/alcazar_v5/v5/tracks/007.perf.txt
   - for a hard subject told with restraint: /home/claude/audioq/guggenheim_v5/v5/tracks/003.perf.txt
3. **v5/PLAN.md**: binding for place, order, @room, @title, content, the allowed facts with their source keys, what NOT to say, the exact cue (last column), the **House key**, DATED items, the NEVER list, ALT cues and the bridge table. Read its Conventions first: directions by fixed features only; house numbers by confidence grade; no prices, hours, events or shop names.
4. **research/FACTS_OCT2026.md** for the rows PLAN cites (F1.1 … F8.16). Read §9 (popular errors and official-page slips) and §10 (names) whole. Then **research/VISIT_ROUTE_AND_SPACES_OCT2026.md** §3 (streets, zones, building list) and **research/map/OFFICIAL_PLAN_NOTES_31OCT2026.md** with the four plan images (look at them: every street, square and number in your cues must be on the plan).

## Accuracy rules (non-negotiable)
- **Sources.** Every load-bearing fact must be confirmed on the source PLAN gives: the operator's pages and the Ajuntament de Barcelona first (poble-espanyol.com, barcelona.cat, the Arxiu Fotogràfic, the Museu Etnològic), then the academic papers (Moliner, Santacreu, Redondo; Sirés; Rahola), then the press or reference source named.
  - Use WebFetch, one page at a time, never in bursts; WebSearch only to find a page.
  - Never a browser, never curl; never complete a CAPTCHA.
  - Wikipedia never alone. Anything only in a search snippet (SNIP) is not scripted.
  - The operator's pages are official **but promotional and sometimes wrong** (FACTS §9). Where PLAN marks an operator line as a slip, never use it; where it marks an operator line as theirs ("the Poble's own history says…"), attribute it.
  - If a page now says something different, use the page and flag it in your notes.
- **Wording.** Use the FACTS safe wording for conflicts:
  - "117 buildings, all life-size" (never 116 on air; never "miniature");
  - "they passed through almost 700 towns and stopped to study 137" on the first trip; "something like sixteen hundred places" across three trips; never "they visited 1,600 villages";
  - "about sixteen months" / "in little more than a year" (never "under a year");
  - "laid out like the square of Riaza" (never "a replica of Riaza's square" in our voice);
  - "built as a temporary set, but solidly enough that it could survive";
  - "used to hold prisoners during the war", as the Poble's own history says; no side, dates or numbers;
  - "the Andalusian quarter", never "Sevillian";
  - "the medieval walls of Ávila" (no century).
- **Attribution.** "The Poble says" for the 800,000 tiles and the casts of stones; "the Poble's own history says" for the wartime camp and Franco's use of the museum; "the house tells" / "the story goes" for Carmen Amaya dancing for the King; "a 1961 architecture journal" for the 1961 critic (never a name); "the researchers who found the notebooks argue" for "it would have disappeared long ago"; the director's words "in 2018".
- **Quotes.** Verbatim, short, attributed by name. Many quotes in PLAN are in Spanish (ES) or Catalan (CA): translate them faithfully, introduce them as such ("he wrote, in Spanish…", "a Catalan magazine wrote…"), and never invent a quote or tidy one into something the person didn't say. Where PLAN asks you to confirm a full sentence in the paper (004's Utrillo letter; 006's Reventós line), do so or quote only the part PLAN gives.
- **Tense.** Past tense for Miquel Utrillo (1862–1934), Xavier Nogués (1873–1941), Francesc Folguera (1891–1960), Ramon Reventós (1892–1976), Rafael Padilla (1878–1961), Carmen Amaya (died 1963), Alfonso XIII, Primo de Rivera, Franco. **No tense at all** for Francesc Daurella (born 1927): "the collection he founded". The lint checks for "Utrillo is", "Reventós says" and the like.
- **Spelling.** Ramon Reventós (not Raventós). Valderrobres (not the operator's "Valderrobles"). The Arco de Maia is from Amaiur, in **Navarre**.
- **Views.** From the viewpoint, only what PLAN gives from the operator's page (the Sagrada Família, the Mapfre towers, Tibidabo, "Barcelona at your feet") and only the landmarks the on-site check ticks (O9). Nothing else.
- **Dated items.** The glassblower, the crafts, the Vidre art gallery, the visitor figures, "turns a hundred in 2029" each go in one separate sentence that can be cut.
- **Practical limits.** No prices, opening hours or days, tickets, deposits, the official audio guide or tablet, the information point's hours, lockers, restaurants, bars, clubs, shops or shop names, and no events (Halloween, LA ZONA, Natalis, concerts).
  - The Tablao de Carmen is the one business named, as a house with a story. The glassblower is "the glassblower", no brand.
  - 001 may say once: "The official plan marks a step-free route; ask for it at the entrance, and this guide warns you where there are steps."
  - Crafts: name the crafts (glassblowing, pottery, stained glass), never the workshops; "if a door is open, look in" is the most you may say.

## Naming houses by number and street
The official plan numbers the buildings 1 to 116 and colours them by region (North green, Centre pink, South yellow, Mediterranean purple). PLAN's **House key** says, for each documented house, which number and street it is, the original town, and how sure we are:
- **DOC** (the number is documented: e.g. 21 the town hall from Valderrobres, 83 Can Banús from Rupit, 79–82 the Rupit fronts on Carrer Mercaders, 81 the glassblower, 69 Casa Son Berga from Palma, 61 Calle Arcos and the Tablao, 3 Casa del Sol from Cáceres, 116 the monastery): you may say "house 83, on Carrer de la Davallada". If the on-site check finds no numbers on the houses (ALT-N), PLAN's cues drop them and you name the street and the landmark only.
- **PIN+COL** (placed by the official map pin and the plan's colour, not yet confirmed on site): **never say the number.** Say "along this street, the Poble's own list includes houses from Sigüenza, Ayllón and Toro" and name the towns. The lead will add the number after the on-site photos.
- **PIN** (weak): the town name only, never placed.
- Never describe a house's architecture beyond what the sources say ("three balconies, the middle one of open wrought iron" is sourced; "a typical Castilian palace" is not).
- Say the original as "modelled on", "from", "the Poble's version of"; never "an exact copy".
- Never explain a street name (Príncipe de Viana, Alcalde de Zalamea, Alcalde de Móstoles, Bajada de Cervantes, Rincón del Triste): none is sourced.

## The dictatorship, the war and Franco (015, 020, 024): even-handed and attributed
- The village was built in 1928–29 under Primo de Rivera's dictatorship, for an Exhibition organised "by the Dictatorship's city council with the help of the state"; it was designed by four Catalanists on an idea that predates the dictatorship; and the Franco regime later used the museum set up in it. **All three are true.** Say so in that spirit.
- Give both readings with names or source types, at equal weight:
  - the national-unity reading: the historian Jordana Mendelson ("an architectural representation of a unified Spain"); the 2010 UPC study by Sirés ("accepted and ideologically swallowed" by the dictatorship; "the indissoluble unity of the Spanish nation" pleased the regime);
  - the counter-reading, from the same study: the Catalanist makers and the earlier idea "substantially complicate the simple, reductionist interpretation" that it was the dictatorship's work.
- The war and after (020): "the Poble's own history says" it held prisoners, and the published list of Francoist camps in Catalonia doesn't include it; the sources don't say who held whom. The 1942 folk-crafts museum is a fact (Museu Etnològic); "violently anti-Catalanist messages" is the Poble's own phrase: attribute it.
- No verdict in our voice. No "fascist", "propaganda", "dark chapter", "brutal regime" except inside a quote. No Franco at the 1968 festival (single source).
- Direction tags in 015 and 020: [quietly] or [curious]; no [amused], [wry] or [lightly] in the political paragraphs; no music sting on 020.

## Navigation rules
- @room and @title exactly as PLAN. @where: where to stand and how to recognise the place, in 1–2 sentences, with no internal notes; then the [O#] tags this track depends on, in brackets at the end. For 020 and 021, add the step-free note PLAN gives.
- **The LAST paragraph of every track (except CLOSE) is the cue**, as in PLAN's last column. It gives the destination plus its fixed features in 1–3 sentences and ends with the spoken form `<place> · <title>`. You may smooth the wording, but you may not change the destination, the features or the order. Keep the [O#] tags out of the spoken text.
- **Allowed landmarks:** the Ávila gate and its two towers; Plaza Castellana; the streets and squares by the names on the plan (PLAN Conventions); house numbers graded DOC; the brick tower; the church; the long grey front of the Fran Daurel Museum; the outside stair at 83; the glass furnace at 81; the fountain; the Baluard; Barcelona Panorama; the Sculpture Garden and its giant slides; the monastery and its square bell tower; the big house at 69; the Vidre art gallery; the white walls; the Gradas de Santiago; Rincón del Triste; the Plaza Mayor's steps; the town hall's arcade; the arcade at 26.
- "Uphill", "climbs", "down" are allowed: the village rises from the gate to the monastery (sourced).
- **Forbidden until PLAN says confirmed:** left/right, "straight ahead", "behind you", compass words (the plan is not drawn north-up), distances, walking times, "the exit is…" (the gate is the only way in and out we know of), "go inside" for the monastery, the patio or any workshop.
- Tracks heard while moving say so: 005 along Calle Caballeros, 007 up Calle Príncipe de Viana, 020 across the Plaza de la Iglesia. Their first ≈ 50 words need no view.
- Extras (003, 010, 016, 019) are announced by the track before them. That track's cue also names the next main stop.
- Never "next track", "right this way", "just over there", "as you can see on your left".

## Bridges (shorter versions)
For every row of PLAN §3 "Bridges" whose Track is one of yours, write ONE spoken bridge of 15–45 words.
- It starts "On this shorter tour," and gives the route to the next stop of that version, with the streets, squares and landmarks exactly as the row says.
- It is played after the track's normal cue, so it must make sense after it ("On this shorter tour, skip the stops along the way: walk on up Calle Caballeros…").
- Put the bridges in v5/bridges/<first>-<last>.txt, one per line: `NNN E>MMM: text` or `NNN H>MMM: text`.

## Version-neutral sentences
Some sentences must work in every version that contains the track:
- 002: one sentence correcting "built for the 1992 Olympics", because H and E skip 003;
- 008: one sentence on "three Aragonese buildings make one church", because E skips 009;
- 015: one sentence on the Franco years ("later used by another regime, Franco's"), because H and E skip 020;
- 022: one sentence naming the town hall (house 21, modelled on Valderrobres), because H skips 023;
- 025: a short recap of "interpretation, not copies", with nothing that depends on 024.

Never refer to a track the listener may not have heard unless every version containing your track also contains that one. **Safe callbacks** (PLAN checks them): 007 → 004 (the burnt clutch); 012 → 008 (the cast tower); 022 → 008 (Santillana let them down); 023 → 004 (the notebooks); 024 → 002 (the gate); 017 and 015 share the viewpoint. **Not safe:** anything in 003, 009, 010, 020 (Full only) from a track in H or E; anything in 005–007, 011, 013, 014, 016, 019, 021, 023, 024 from a track in H.

## Writing rules
- Never open with a command. Open with a hook: a surprising fact, a person, a tension. The hooks PLAN gives are suggestions; better ones from the same sources are welcome.
- **Length** (spoken words, tags excluded): R 180–280 · W 250–360 · ANCHOR/CLOSE 250–360 · X 150–230. Aim at PLAN §3's "Aim" per track (upper half where the material is real). The whole Full guide sits near 7,400 words; don't run far over.
- Average sentence 11–16 words; vary them; max ~30. No parentheses, no semicolons, ≤ 2 em-dashes, no exclamation marks.
- **One clear "you" moment per track:** what to look at now, in the house or the place itself (count the steps; find the three balconies; watch the tower's ceramics flash; look for a "stone" that is a cast). Look-prompts mid-track are welcome.
- Numbers spoken as people say them ("about sixteen months", "almost seven hundred towns", "about two thousand square metres"). At most ~3 dates per track. Years as digits.
- Name a person, then use "he" or "she". Give an English gloss once per track for Spanish or Catalan words: *Poble Espanyol* "Spanish Village", *Plaça Major* "main square", *caserío* "farmhouse", *Monestir* "monastery", *gradas* "steps". Say the Catalan or Spanish street names as they are signed.
- **Direction tags** only from the standard: [pause] [long pause] [warmly] [quietly] [amused] [curious] [conspiratorial] [reverent] [wry] [lightly], and *word* for stress. About one delivery tag per paragraph. The wry moments are in PLAN (the tower they liked better, *Mirador*'s gossip, the halved stair); one per track at most, and none in the political paragraphs or in 020.

## Output — one file per track: v5/tracks/NNN.perf.txt
```
@id: NNN · Poble Espanyol · 31 Oct 2026 edition
@section: <exactly the PLAN section name: The gate | Calle Caballeros | The brick tower | Catalonia | The top of the hill | Andalusia | Back to the Plaza Mayor>
@room: exactly as PLAN ("Carrer de la Davallada · house 83, facing the outside stair")
@type: ANCHOR | R | W | X | CLOSE
@title: exactly as PLAN (Extras keep "Extra · ")
@where: <1–2 sentences: where to stand and how to recognise it; step-free note where PLAN gives one; then the [O#] tags this track depends on, in brackets at the end>
@what: <the house(s) or place, with the original town and province from the House key and its grade; the dates; for 011/016 the collection and founder>
@listen: <1 sentence: what the track is about>
@brief: <one line: who is speaking, to whom, in what mood>
@pace: slow | medium-slow | medium | medium-fast
@energy: e.g. 2→4  (020: 1→2)
@sources: <URLs read, with what each confirmed; OFF / OFF-op / SEC / SEC-acad; one line each>
---
<spoken body, paragraphs separated by blank lines, last paragraph = cue>
```
Write v5/notes/<first>-<last>_NOTES.md, with this per track:
- the pages you read (URL and what each confirmed);
- anything you could not confirm (and what you did instead);
- any wording that differs from PLAN, and why;
- any quote whose exact words you changed, and every translation you made (original + your English).

**Check before finishing:** `python3 v5/lint.py <your track numbers>`. Every track must print OK; the lead adapts the lint per PLAN §1 "Lint".

**Final reply ≤ 8 lines:** the tracks written, what you could not verify, and what the lead must decide.
