# WRITER BRIEF — Barcelona Cathedral, Yo Tours (14 Nov 2026, 36 tracks)

You are writing part of a new English walking audio guide to Barcelona Cathedral, the Catedral de la Santa Creu i Santa Eulàlia: the Gothic cathedral begun in 1298 over the Roman and Romanesque sees, with its 1887–1913 facade and cimbori, the choir where the Order of the Golden Fleece met in 1519, the crypt of Santa Eulàlia, the cloister with its geese, the roof by lift, and the Chapter Hall museum. It is built from scratch.

**The competition is weak** (research/OFFICIAL_AUDIO_COMPARISON_NOV2026.md): the cathedral's own phone web guide often fails to load, gives no directions and is silent on what tourists ask; no commercial product guides the interior; reviews are full of people who thought they were going to the Sagrada Família, and of legends told as fact (13 geese for 13 years, the Christ that dodged a cannonball). **Ours:** right places, landmark directions, verified facts, legends told as legends, Mass-proof alternatives, and good to listen to.

**The user's standing instruction: "kindly do not compromise on research and quality".** Give the stories, people, verbatim quotes and things to look at that PLAN gives you. Write in the upper half of the word range wherever the material is real. Never pad.

Priorities: navigation accuracy first, accuracy of fact second, storytelling third.

Project root: /home/claude/audioq/bcncat_v5 (paths below are relative to it).

## Read first, in this order
1. **v5/V5_AUDIO_STANDARD.md**: the writing and direction standard (binding; §2 and §3).
2. **Voice anchors** (spoken, warm, composed; hook → story → turn → look → payoff): /home/claude/audioq/guell_v5/v5/tracks/018.perf.txt, 022.perf.txt, 034.perf.txt and 043.perf.txt (a death told with restraint); /home/claude/audioq/poble_v5/v5/tracks/004.perf.txt.
3. **v5/PLAN.md, all of it**: binding for place, order, @section, @room, @title, content, allowed facts with row numbers and grades, quotes, NOT lists, exact cues, §4 NEVER, §6 DATED, ALT cues, version-neutral sentences, safe callbacks, the bridge table and "One home per story". **Its Conventions are binding**, especially: the cue pattern; Extras announced only as "If you're on the full tour, …"; queue tracks (012, 013) need no view before their last paragraph; doorway tracks (007, 008) never send people in; the Mass/closure fallback lines; attribution variety; payoff lines only in the tracks listed; "Watch the doubles" (two chapter houses, two Martorells, the bell vs the door vs the saint called Eulàlia, Font, Girona, Sant Sever). **Its "Lead's decisions" section at the end overrides anything above it.**
4. **research/FACTS_NOV2026.md** and **research/FACTS_GAPS_NOV2026.md** for the rows PLAN cites (F… and G…), incl. FACTS §18 (errors), §19 (names), §20 (quotes), and the GAPS "Changes proposed to FACTS rows" table (it overrides FACTS where it differs: e.g. 877 not 878; the painter Joan de Borgonya; the Eulàlia bell is not 1393). Then **research/VISIT_ROUTE_AND_SPACES_NOV2026.md** §0–§2.

## Accuracy rules (non-negotiable)
- **Sources.** Confirm every load-bearing fact on the source PLAN gives: the cathedral's own pages (catedralbcn.org), the Generalitat heritage inventory, the Ajuntament and MUHBA, MNAC, then scholarly sources, then the named press/reference source. WebFetch, one page at a time, never in bursts; WebSearch only to find a page. Never a browser, never curl; never complete a CAPTCHA. Wikipedia never alone; search snippets never scripted. Official pages are sometimes wrong or contradict each other (FACTS §18: "16th-century Christ", alabaster, chapel credits): where PLAN marks a slip, never use it. **Every FACTS/GAPS quote is "as relayed"**: re-check the words on the page before quoting; if you can't, paraphrase without quotation marks and say so in your notes. If a page now says something different, use the page and flag it.
- **Attribution.** Readings and legends belong to someone: "tradition says", "the story goes", "the cathedral says", "one historian", "the city's history museum". Legends once, as legends, with who tells them and the honest verdict. Never "the builders meant…" without a source.
- **Quotes** in Catalan, Latin or Spanish: translate faithfully, introduce as such once per track ("in Catalan"), never tidy them.
- **Tense.** Past for every medieval and 19th-century person and for Gaudí, Bermejo, Ordóñez etc. (the lint checks the main names); present for the cathedral, its chapter, MUHBA, MNAC, encyclopedias and living scholars.
- **Dated items** (works, the roof arrangements, the Lepanto Christ's Lent move, recent restorations) each in one separate sentence that can be cut.
- **Practical limits.** Only 001 carries practical lines (headphones; respect worship; the lift may have a wait; offline). Never prices, hours, Mass times, slots, ticket types, free entry, the official audio guide, AR/VR, the shop, toilets, Wi-Fi, lift capacity.

## Navigation rules
- @section, @room and @title exactly as PLAN. @where: where to stand and how to recognise it, 1–2 sentences, then the [O#] tags in brackets at the end.
- **The LAST paragraph of every track (except CLOSE) is the cue**, as PLAN's cue column gives it, ending with the spoken form `<place> · <title>`. Smooth the wording, never change the destination, the features, the order or the conditional fallbacks. [O#] tags never spoken.
- Directions only by PLAN's fixed features ("as you face the high altar", doors by name, the choir, the crypt stair, the lift chapel, the cloister door…). No compass words, distances, chapel numbers, or left/right without an [O#] tag in @where.
- Never "next track", "right this way", "just over there", "as you can see on your left".

## Bridges (shorter versions)
For every row of PLAN §3 "Bridges" whose Track is one of yours, write ONE spoken bridge of 15–45 words starting "On this shorter tour," with the route to the next stop of that version, the landmarks exactly as the row says, ending `<place> · <title>` of that stop. It plays after the track's normal cue. File: v5/bridges/<first>-<last>.txt, one per line: `NNN E>MMM: text` or `NNN H>MMM: text`.

## Writing rules
- Never open with a command. Open with a hook: a surprising fact, a person, a tension. Follow PLAN's tag melody and opener guidance.
- **Length** (spoken words, tags excluded): R 180–280 · W 250–360 · ANCHOR/CLOSE 250–360 · X 150–230. Aim at PLAN §3's "Aim".
- Average sentence 11–16 words; vary; max ~30. No parentheses, no semicolons, ≤ 2 em-dashes, no exclamation marks, no asterisks.
- **One clear "you" moment per track** (find the shield, the finger, the goose, the spectacles…), conditional where PLAN says.
- Numbers as people say them; at most ~3 dates per track; years as digits.
- Gloss Catalan once per track (*cimbori*, "the lantern tower"; *cadirat*, "the choir stalls"; *l'ou com balla*, "the dancing egg").
- **Direction tags** only from the standard: [pause] [long pause] [warmly] [quietly] [amused] [curious] [conspiratorial] [reverent] [wry] [lightly]; about one per paragraph; [reverent]/[quietly] for the martyr, 1391, 1936 and the dead.
- **This is a working church.** Tone respectful; no jokes at faith; say "worshippers" not "locals"; Mass is something to step around quietly.

## Output — one file per track: v5/tracks/NNN.perf.txt
```
@id: NNN · Barcelona Cathedral · 14 Nov 2026 edition
@section: <exactly the PLAN section name>
@room: exactly as PLAN
@type: ANCHOR | R | W | X | CLOSE
@title: exactly as PLAN (Extras keep "Extra · ")
@where: <1–2 sentences; then the [O#] tags in brackets at the end>
@what: <the place(s), dates, makers, with F/G rows>
@listen: <1 sentence: what the track is about>
@brief: <one line: who is speaking, to whom, in what mood>
@pace: slow | medium-slow | medium | medium-fast
@energy: e.g. 2→4
@sources: <URLs read, with what each confirmed; OFF / SEC; one line each>
---
<spoken body, paragraphs separated by blank lines, last paragraph = cue>
```
Write v5/notes/<first>-<last>_NOTES.md: pages read (URL and what each confirmed); anything you couldn't confirm and what you did; wording that differs from PLAN and why; every quote re-checked or changed and every translation (original + your English).

**Check before finishing:** `python3 v5/lint.py <your track numbers>` from the project root. Every track must print OK.

**Final reply ≤ 8 lines:** tracks written, what you couldn't verify, what the lead must decide.
