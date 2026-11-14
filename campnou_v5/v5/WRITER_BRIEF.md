# WRITER BRIEF — FC Barcelona Museum at Spotify Camp Nou, Yo Tours (14 Nov 2026, 34 tracks)

You are writing part of a new English walking audio guide to the **Museum ticket** at Spotify Camp Nou, Barcelona: the club's temporary museum (the "Barça Immersive Tour") in its old ice rink beside the Palau Blaugrana, the round 360° room, the models of the finished stadium and the Construction Viewpoint over the stadium being completed. This ticket does **not** go into the stadium. The guide is built from scratch; the user's old guide was audited and is a list of topics, not a text to reuse.

**The user asked for "good facts, fun stories and their legacy … like how we did for Santiago (Real Madrid)",** and for a full tour of about 90 minutes whose extra stories are heard **inside**, standing or sitting, needing no view until their last paragraph. **The user's standing instruction: "kindly do not compromise on research and quality".** Give the stories, people, verbatim quotes and things to look at that PLAN gives you. Write in the upper half of the word range wherever the material is real. Never pad.

**The competition is weak** (research/OFFICIAL_AUDIO_COMPARISON_NOV2026.md): the club's own phone guide gives no stories beyond captions; visitors complain they never see the pitch; most guides repeat legends as fact (the napkin "in the museum", "the biggest stadium in the world", "built for Kubala", the colours "from Basel"). **Ours:** honest about what the ticket is, right places, verified facts, legends told as legends, both sides of contested history, and good to listen to.

Priorities: navigation accuracy first, accuracy of fact second, storytelling third.

Project root: /home/claude/audioq/campnou_v5 (paths below are relative to it).

## Read first, in this order
1. **v5/V5_AUDIO_STANDARD.md**: the writing and direction standard (binding; §2 and §3).
2. **Voice anchors** (spoken, warm, composed; hook → story → turn → look → payoff): our Real Madrid guide, the model the user named: /home/claude/audioq/bernabeu_v5/v5/tracks/003.perf.txt, 011.perf.txt, 013.perf.txt, 019.perf.txt and 024.perf.txt. For a hard subject told with restraint: /home/claude/audioq/guell_v5/v5/tracks/043.perf.txt. Learn the voice; never copy their facts (another club, another city).
3. **v5/PLAN.md, all of it**: binding for place, order, @section, @room, @title, content, allowed facts with row numbers and grades, quotes (Q#, RC = re-check), NOT lists, exact cues, §4 NEVER, §6 DATED, ALT cues, version-neutral sentences, safe callbacks, the bridge table and "One home per story". **Its Conventions are binding**, especially: fixed place names; displays, not rooms; the cue pattern; Extras announced only as PLAN says; the "hear it anywhere" openers (once per cluster, never alike); payoff lines only in the listed tracks; attribution variety; tense; "Watch the doubles" (two Luis Suárez, no bare "Ronaldo", two Montals, two Wembleys, two Gols, "the round room" = the 360° room only). **Its "Lead's decisions on §8" at the very end override anything above it** (Highlights 6 tracks and "about thirty-five minutes"; Essential 18 with 027; no 1 October 2017; no sums of money; no anthem lyrics at all; Sunyol's box only with a second source; Maradona's Bernabéu applause out; etc.).
4. **research/FACTS_NOV2026.md** for the rows PLAN cites (F…), incl. §18 (errors), §19 (names), §21 (quotes), §22 (legacy). **research/AUDIT_OLD_GUIDE_NOV2026.md** for the AU… rows and AU-S… sources PLAN cites, and its §3. If **research/FACTS_GAPS_NOV2026.md** exists, its "Changes proposed to FACTS rows" table overrides FACTS. Then **research/VISIT_ROUTE_AND_SPACES_NOV2026.md** §0–§2 and **research/map/OFFICIAL_ACCESS_MAP_NOTES_14NOV2026.md**.

## Accuracy rules (non-negotiable)
- **Sources.** Confirm every load-bearing fact on the source PLAN gives: the club's own pages (fcbarcelona.com, its history, museum and news pages) first, then UEFA/FIFA/the Generalitat/the Ajuntament, then the named press (Ara, 3Cat, La Vanguardia, El Periódico, Mundo Deportivo, Catalan News, BBC, Guardian, ESPN, The Athletic). WebFetch, one page at a time, never in bursts; WebSearch only to find a page. Never a browser, never curl; never complete a CAPTCHA. Wikipedia never alone; search snippets never scripted. The club's pages sometimes contradict each other (FACTS §18: "six European Cups", "22 May 1922", "80.8%"): where PLAN marks a slip, never use it. **Every FACTS/AUDIT quote is "as relayed"**: re-check the words on the page before quoting; if you can't, paraphrase without quotation marks and say so in your notes. If a page now says something different, use the page and flag it.
- **Even-handed.** 1925, Sunyol, 1943 and "Més que un club" are told as PLAN gives them: the facts first, each reading attributed to who holds it, no side taken, no comment on Catalan independence, Real Madrid named with respect. Never "the regime's club", never "Franco ordered" (lint).
- **Attribution.** Readings and legends belong to someone: "the club says", "the club's history pages", "one historian", "a Madrid paper of the time", "the story goes". Legends once, as legends, with who tells them and the honest verdict. Vary attributions (PLAN Conventions).
- **Quotes** in Catalan or Spanish: translate faithfully, introduce as such once per track ("in Catalan"), never tidy them. **Nothing in a person's mouth** that FACTS §21 or PLAN doesn't give (Messi, Guardiola, Kubala, Sunyol, Gamper beyond Q2: none). **No song lyrics**, not one line of the anthem.
- **Tense.** Past for the dead (Gamper, Sunyol, Kubala, Cruyff, Maradona, Narcís de Carreras, Samitier, Núñez…; the lint checks the main names); present for the club, its museum, living players, historians and papers.
- **Dated items** (the stadium works, capacity now, the roof, Montjuïc in 2027, trophy totals, Ballon d'Or counts, Lamine Yamal and the No 10, the women's totals, records) each in one separate sentence that can be cut.
- **Practical limits.** Only 001 carries practical lines (headphones; about an hour on the club's own count, this guide stretches it; offline; the three lengths as Lead's decision 1 words them). Never prices, hours, sums of money, ticket types, RoboKeeper, VR, the official audio guide, the shop as advice, toilets, Wi-Fi, lockers.

## Navigation rules
- @section, @room and @title exactly as PLAN. @where: where to stand and how to recognise it, 1–2 sentences, then the [O#] tags in brackets at the end.
- **The LAST paragraph of every track (except CLOSE) is the cue**, as PLAN's cue column gives it, ending with the spoken form `<place> · <title>`. Smooth the wording, never change the destination, the features, the order or the conditional fallbacks. [O#] and [RL] tags never spoken.
- **Displays, not rooms**: "when you reach…", "find…"; never "the next room", "upstairs", "turn left", compass words, distances, gate numbers, "the Masia over there".
- Never "next track", "right this way", "just over there", "as you can see on your left".
- **Topic-keyed bodies** (decision 2): only the @where, the [RL] look line and the cue may depend on the current building. Everything else must still be true if the museum moves into the stadium.

## Bridges (shorter versions)
For every row of PLAN §3 "Bridges" whose Track is one of yours (with the Lead's decision 11 change for Essential: 027 is in E), write ONE spoken bridge of 15–45 words starting "On this shorter tour," with the route to the next stop of that version, the landmarks exactly as the row says, ending `<place> · <title>` of that stop. It plays after the track's normal cue. File: v5/bridges/<first>-<last>.txt, one per line: `NNN E>MMM: text` or `NNN H>MMM: text`.

## Writing rules
- Never open with a command. Open with a hook: a surprising fact, a person, a tension. Follow PLAN's tag melody and opener guidance.
- **Length** (spoken words, tags excluded): R 180–280 · W 250–360 · ANCHOR/CLOSE 250–360 · X 150–230. Aim at PLAN §3's "Aim".
- Average sentence 11–16 words; vary; max ~30. No parentheses, no semicolons, ≤ 2 em-dashes, no exclamation marks, no asterisks.
- **One clear "you" moment per track** (find the oldest silver cup, the shirt with UNICEF's name, the six golden balls; sit on the old bench), conditional where PLAN says; Extras that need no view put theirs in the last paragraph.
- Numbers as people say them; at most ~3 dates per track; years as digits. Scores as people say them ("four–nil").
- Gloss Catalan once per track (*blaugrana*, "blue and claret"; *culers*; *socis*, "the members"; *Més que un club*, "more than a club").
- **Direction tags** only from the standard: [pause] [long pause] [warmly] [quietly] [amused] [curious] [conspiratorial] [reverent] [wry] [lightly]; about one per paragraph; [quietly] for Gamper's death, Sunyol, Cruyff's death; never [reverent].
- **Fun matters.** Football is joy: let the great nights sing (Wembley, the six, the 91,648), let the odd details land (the misspelled advert, backsides on a wall, the registrar who refused a name), with warmth, never sneering at any club or city.

## Output — one file per track: v5/tracks/NNN.perf.txt
```
@id: NNN · FC Barcelona Museum · 14 Nov 2026 edition
@section: <exactly the PLAN section name>
@room: exactly as PLAN
@type: ANCHOR | R | W | X | CLOSE
@title: exactly as PLAN (Extras keep "Extra · ")
@where: <1–2 sentences; then the [O#] tags in brackets at the end>
@what: <the story, people, dates, objects, with F/G/AU rows>
@listen: <1 sentence: what the track is about>
@brief: <one line: who is speaking, to whom, in what mood>
@pace: slow | medium-slow | medium | medium-fast
@energy: e.g. 2→4
@sources: <URLs read, with what each confirmed; OFF / SEC; one line each>
---
<spoken body, paragraphs separated by blank lines, last paragraph = cue>
```
Write v5/notes/<first>-<last>_NOTES.md (or a name your lead gives you): pages read (URL and what each confirmed); anything you couldn't confirm and what you did; wording that differs from PLAN and why; every quote re-checked or changed and every translation (original + your English).

**Check before finishing:** `python3 v5/lint.py <your track numbers>` from the project root. Every track must print OK.

**Final reply ≤ 8 lines:** tracks written, what you couldn't verify, what the lead must decide.
