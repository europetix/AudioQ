# WRITER BRIEF — Park Güell (Barcelona), Yo Tours — EDITION 2 (≈ 45 tracks, 7 Nov 2026)

You are writing part of a new English walking audio guide to Park Güell: Eusebi Güell's failed garden-city estate on the Carmel hill (1900–1914), built by Antoni Gaudí with Josep Maria Jujol, Francesc Berenguer and the builders Pardo and Berdié, and a public park since 1926. The guide walks one loop that follows the operator's own recommended order through the one-way inner section and ends at the only exit, the Carrer d'Olot gate. It is built from scratch; there is no old guide.

**The competition is weak** (research/OFFICIAL_AUDIO_COMPARISON_NOV2026.md): a free planning app without German and with no documented audio; commercial guides with 5–6 highlights that assume one entrance, rely on GPS that fails in the park, repeat legends as fact ("the longest bench in the world", the workman in wet plaster, "Gaudí designed his own house"), leave out Jujol and the viaducts, and leave people stuck after the one-way step. **Ours:** right places, landmark directions in the park's own names, verified facts, legends told as legends, Jujol credited, and good to listen to.

**The user's standing instruction: "kindly do not compromise on research and quality".** A recent guide felt thin to them. Give the stories, the people, the verbatim quotes and the things to look at that PLAN gives you. Write in the upper half of the word range wherever the material is real. Never pad.

Priorities: navigation accuracy first, accuracy of fact second, storytelling third.

Project root: /home/claude/audioq/guell_v5 (paths below are relative to it).

## Edition 2: what changed
The user asked for ≈ 45 tracks and a 120-minute full tour: "we need to cover more stories and better quality audio, including views". PLAN_V2 gives 45 tracks. Its column "From edition 1" says for each track KEEP NNN, SPLIT FROM NNN or NEW. Edition-1 tracks are in **v5/held/ed1/tracks/** (well written; reuse their sentences where PLAN_V2 says KEEP or SPLIT, applying every audit fix it lists). The two independent audits of edition 1 are research/AUDIT_V5_FACTS.md and research/AUDIT_V5_ROUTE_LISTENING.md: their MUST and SHOULD findings are binding wherever your track reuses that text. The official route map notes are research/map/OFFICIAL_ROUTE_MAP_NOTES_7NOV2026.md (left/right allowed only where PLAN_V2 tags [O-map]). New research: research/FACTS_EXPANSION_NOV2026.md (rows E1…, corrections C1…).

**Shorter tracks need the same depth per minute.** A 200-word R track still has a hook, a real story, one thing to look at and the cue. If your material for a track is thinner than its aim, write to the material (above the type's minimum) and say so in your notes: never pad.

## Read first, in this order
1. **v5/V5_AUDIO_STANDARD.md**: the writing and direction standard (binding; §2 and §3).
2. **Voice anchors** (spoken, warm, composed; hook → story → turn → look → payoff):
   - /home/claude/audioq/poble_v5/v5/tracks/004.perf.txt and 012.perf.txt
   - /home/claude/audioq/guggenheim_v5/v5/tracks/009.perf.txt and 025.perf.txt
   - for a hard subject told with restraint: /home/claude/audioq/guggenheim_v5/v5/tracks/003.perf.txt
3. **v5/PLAN_V2.md, all of it** (edition 2; it replaces v5/PLAN.md, which stays only as background): binding for place, order, @section, @room, @title, content, the allowed facts with their row numbers and grades, quotes, what NOT to say, the exact cue (last column), the NEVER list (§4), DATED (§6), ALT cues, version-neutral sentences, safe callbacks and the bridge table (§3). **Its "Lead's decisions" section at the very end overrides anything above it.** Read its Conventions first: directions only by the fixed features listed there; no left/right, compass words, distances or walking times; [O#] tags never spoken.
4. **research/FACTS_NOV2026.md** and **research/FACTS_GAPS_NOV2026.md** for the rows PLAN cites (F… and G…). Read FACTS §15 (popular errors), §16 (names) and §17 (quotes) whole. Then **research/VISIT_ROUTE_AND_SPACES_NOV2026.md** §0–§2.

## Accuracy rules (non-negotiable)
- **Sources.** Every load-bearing fact must be confirmed on the source PLAN gives: the operator (parkguell.barcelona, B:SM) and the Ajuntament/MUHBA first, then the academic papers and Bassegoda, then the press or reference source named.
  - Use WebFetch, one page at a time, never in bursts; WebSearch only to find a page. Never a browser, never curl; never complete a CAPTCHA.
  - Wikipedia never alone. A search snippet (SNIP) is never scripted.
  - The operator's pages are official but sometimes wrong (FACTS §15: 1922 opening, 1895 purchase, 150 m bench, "Jujol designed the bench"). Where PLAN marks an operator line as a slip, never use it.
  - **Every FACTS quote is "as relayed"**: re-check the exact words on the page before you quote; if you cannot, paraphrase without quotation marks and say so in your notes.
  - If a page now says something different, use the page and flag it in your notes.
- **Safe wordings for conflicts** (FACTS): "about a hundred metres" of bench (never 102, 110 or 150 on air; never "longest"); "eighty-six columns"; "in the last years of the 1890s Güell bought up land on the hill" or "in the summer of 1899 Güell bought the top of the hill"; "in the early 1920s the city bought it from Güell's heirs"; "it opened to everyone in the spring of 1926"; "the Gaudí family bought it in 1906"; "nearly twenty years" (1906–1925); "among the first things built"; "a large tank" (no capacity unless PLAN allows the G row); "the dragon, or salamander, as the park calls it".
- **Attribution.** Readings are somebody's: "the Gaudí scholar Joan Bassegoda", "some scholars", "one researcher"; never "Gaudí meant…". "The park's own history calls it…" for the operator's opinions. Legends once, as legends, with who tells them ("tour guides like to say…", "the story goes…") and the honest verdict.
- **Nothing in Gaudí's mouth.** No verified Gaudí quotation about the park exists in our research. The famous lines ("the straight line belongs to men…") are never used. Güell's 1904 words only as PLAN's Lead's decision 5 allows.
- **Quotes** in Spanish or Catalan: translate faithfully, introduce as such ("he wrote, in Spanish…"), never tidy them.
- **Tense.** Past tense for Güell, Gaudí, Jujol, Berenguer, Bassegoda, Maragall, Rubió i Tudurí, Dalí, Alfonso XIII. The lint checks "Gaudí is", "Güell says" and the like.
- **Names.** Eusebi Güell; Josep Maria Jujol; Francesc Berenguer; the lawyer Martí Trias (never "Dr Trias"); Juli Batllevell; never Joan Rubió i Bellver as a collaborator; never "Can Coll" alone (Can Coll i Pujol, per G38, if PLAN uses it).
- **Views.** Only what PLAN allows from the operator's texts and the landmarks the on-site check ticks (O7).
- **Dated items** (restorations 2024–26, the dragon's foot back in April 2026, management of the museum, works closures, visitor numbers, the 2026 centenary, Casa Trias's expropriation) each in one separate sentence that can be cut.
- **Practical limits.** No prices, hours, time slots, ticket advice, the official app, guided tours, the shop, toilets, food, Wi-Fi, events or exhibitions. 001 alone carries the practical lines PLAN lists (headphones, no re-entry, one-way section, steep paths and the reduced-mobility route, offline). Casa Larrard is a working school and Casa Trias a private home: outside only, never "go in", never "look into the windows".

## Navigation rules
- @section, @room and @title exactly as PLAN. @where: where to stand and how to recognise the place, in 1–2 sentences, no internal notes; then the [O#] tags the track depends on, in brackets at the end.
- **The LAST paragraph of every track (except CLOSE) is the cue**, as in PLAN's last column. It gives the destination plus its fixed features in 1–3 sentences and ends with the spoken form `<place> · <title>`. You may smooth the wording, not change the destination, the features or the order. Keep [O#] tags out of the spoken text.
- Tracks heard while waiting or walking say so (007 in the queue; 023 walking down). Their first ≈ 50 words need no view.
- Extras are announced by the track before them ("There's a short Extra here…; the next main stop is…"). Extras on the full tour are framed so that a shorter-tour listener who never hears them misses nothing.
- Never "next track", "right this way", "just over there", "as you can see on your left".

## Bridges (shorter versions)
For every row of PLAN §3 "Bridges" whose Track is one of yours, write ONE spoken bridge of 15–45 words. It starts "On this shorter tour," and gives the route to the next stop of that version, with the landmarks exactly as the row says, ending with `<place> · <title>` of that next stop. It plays after the track's normal cue, so it must make sense after it. Put bridges in v5/bridges/<first>-<last>.txt, one per line: `NNN E>MMM: text` or `NNN H>MMM: text`.

## Version-neutral sentences and callbacks
Follow PLAN §3 "Version-neutral sentences" and "Safe callbacks" exactly. Never refer to a track the listener may not have heard unless every version containing your track also contains that one.

## Writing rules
- Never open with a command. Open with a hook: a surprising fact, a person, a tension.
- **Length** (spoken words, tags excluded): R 180–280 · W 250–360 · ANCHOR/CLOSE 250–360 · X 150–230. Aim at PLAN §3's "Aim" per track.
- Average sentence 11–16 words; vary; max ~30. No parentheses, no semicolons, ≤ 2 em-dashes, no exclamation marks.
- **One clear "you" moment per track:** what to look at now (find the wine-glass feet in a sun; touch the bench's backrest; look for the white broken-tile skirts at the column feet; find the red and yellow stripes under the snake).
- Numbers as people say them; at most ~3 dates per track; years as digits.
- Gloss Catalan once per track (*Sala Hipòstila*, "hall of columns"; *Pòrtic de la Bugadera*, "Portico of the Washerwoman"; *trencadís*, "broken-tile mosaic").
- **Direction tags** only from the standard: [pause] [long pause] [warmly] [quietly] [amused] [curious] [conspiratorial] [reverent] [wry] [lightly], and *word* for stress. About one per paragraph; one wry moment per track at most; [quietly]/[reverent] for Gaudí's death and the 1936 cross.

## Output — one file per track: v5/tracks/NNN.perf.txt
```
@id: NNN · Park Güell · 7 Nov 2026 edition
@section: <exactly the PLAN section name>
@room: exactly as PLAN
@type: ANCHOR | R | W | X | CLOSE
@title: exactly as PLAN (Extras keep "Extra · ")
@where: <1–2 sentences; then the [O#] tags in brackets at the end>
@what: <the place(s), dates, makers, with FACTS/G rows>
@listen: <1 sentence: what the track is about>
@brief: <one line: who is speaking, to whom, in what mood>
@pace: slow | medium-slow | medium | medium-fast
@energy: e.g. 2→4
@sources: <URLs read, with what each confirmed; OFF / OFF-op / SEC / SEC-acad; one line each>
---
<spoken body, paragraphs separated by blank lines, last paragraph = cue>
```
Write v5/notes/<first>-<last>_NOTES.md: the pages you read (URL and what each confirmed); anything you could not confirm (and what you did instead); any wording that differs from PLAN and why; every quote you re-checked or changed, every translation (original + your English).

**Check before finishing:** `python3 v5/lint.py <your track numbers>` (run from the project root as `python3 v5/lint.py 001 002 …`). Every track must print OK.

**Final reply ≤ 8 lines:** the tracks written, what you could not verify, and what the lead must decide.
