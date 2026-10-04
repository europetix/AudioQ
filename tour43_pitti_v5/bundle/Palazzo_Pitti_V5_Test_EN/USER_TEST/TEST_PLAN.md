# Palazzo Pitti V5 — user test plan

**Goal.** Find out which of three things still causes complaints, so the next fix goes to the right place:

1. **Voice**: does it still sound like a machine?
2. **Content**: are the stories interesting, clear and correct?
3. **Route**: does the audio match where people actually are?

The V5 build changes the scripts, the direction, the order and the mastering. It keeps the same free voices as the June guide. So if people still call the voice monotonous after this test, the free engines have reached their limit and paid voices are worth the cost. The ElevenLabs bake-off kit is ready for that step.

## Test 1: Desk listening (voice only), about 15 minutes per person

Run this before anyone goes on site. Use 6–10 people who haven't heard either guide.

Play the same three tracks in three versions, in shuffled order, and don't say which is which:

| Code | Version |
|---|---|
| A | June guide, am_michael (old script, no direction) |
| B | V5, am_michael |
| C | V5, Brian |

The three tracks:

| Track | Kind of track |
|---|---|
| 021 Sala di Giove | Room intro |
| 015 Madonna della Seggiola | Single work |
| 053 Amphitheatre | Garden |

The matching June tracks are 015 Throne Room, 019 Madonna della Seggiola and 081 Where the Medici Threw Their Parties. You don't need to find them yourself: once both V5 voices are rendered, run `make_listening_test.command`. It copies the nine clips to `~/Desktop/Pitti_Listening_Test/` under shuffled codes, and writes the answer key to a separate file.

For each clip, the listener answers on a 1–5 scale:
- "This sounds like a real person telling me a story."
- "I'd happily listen to 30 more tracks of this."

Then ask one open question: "What, if anything, sounded artificial?"

Read the results this way:
- **B beats A by about 1 point or more:** the writing and direction are working.
- **B and C both score 3 or below on the first statement:** the voice engine is now the bottleneck. Run the paid bake-off.

## Test 2: On-site walk (route + content), half a day per tester

Use 6–12 testers with their own phones and earphones.

**Split.** Half the testers use the June guide and half use V5, in the same voice (am_michael). This means any difference comes from the script, order and direction, not the voice.

**Brief.** Give testers the route PDF for their version (V5: Palazzo_Pitti_Audio_Guide_Route.pdf), and nothing else. Don't coach them.

**During the walk**, testers mark on the feedback form any track number where:
- **L (lost):** "I wasn't where the audio thought I was."
- **W (wrong):** "That didn't match what I was looking at."
- **R (robotic):** "The voice sounded robotic here."
- **B (bored):** "I skipped or stopped listening."

**Observers.** Shadow 2–3 testers if you can. Note each time they stop and look around, backtrack, or ask staff. That is the strongest evidence for route problems.

**Afterwards**, testers fill in the end-of-visit questions on the form. They take about 3 minutes.

## What decides the next step

| Result | Meaning | Next step |
|---|---|---|
| L flags cluster on certain track numbers | A cue or the order is wrong there | Fix those cues, and re-check the room on site |
| W flags on a track | A placement or description is wrong, or the work has moved | Re-verify on site and on uffizi.it, then fix or hold the track |
| R flags spread evenly; voice score ≤ 3 | Free voices have hit their limit | ElevenLabs bake-off (kit ready), then re-render the same scripts |
| R flags concentrated on a few tracks | Those tracks are badly directed or mispronounced | Adjust the perf tags or pronunciation.py for those tracks |
| B flags on a track | It's too long or the story is weak | Tighten or rewrite to the standard |
| V5 group needs fewer L/W flags than the June group, and the voice score improves | V5 works | Rebuild the full PDF, then release V5 |

## Timing notes (October 2026)

- **Iliad Room:** closed until 25 Oct 2026. Testers before that date take the staff detour (see the notice box in the route PDF). Track 009 tells them what to do. Note any confusion there.
- **Royal Apartments:** guided slots only. Book a slot for each tester, or mark that section "not tested".
- **Boboli:** includes restoration fences. Tracks 052, 053, 054, 056, 058 and 059 already say so.
