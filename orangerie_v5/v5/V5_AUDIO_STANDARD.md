# V5 AUDIO STANDARD — "a real person telling you the story of this place"
*Pilot: Tour #43 Palazzo Pitti + Boboli. Drafted 4 Oct 2026. Replaces the V4.5 "light polish" rule for
narration (user decision, 4 Oct 2026: story-first rewrite + direction layer; paid expressive TTS = ElevenLabs).*

## 1. Why V4.5 sounded monotonous (diagnosis)
1. **Engine** — free previous-generation voices (edge-tts Brian, Kokoro am_michael) read every sentence
   with near-identical melody; flat over 3+ hours.
2. **Text** — written to be read: long sentences, em-dash asides, name/date lists, no turns or reveals.
3. **Production** — no breathing room between ideas, identical energy on intros and masterpieces,
   40 kbps mono, no loudness mastering, no signature sound.
Fixing only (1) gives a nicer-sounding monotone. All three are fixed together.

## 2. The script — written to be performed
Each track is a **told story**, not an entry. Same verified facts, different shape.

**Shape (every W-FOCUS track):** HOOK (a surprising fact, a person, a question in the listener's head —
never an instruction) → THE STORY (a person at the centre, something at stake) → THE TURN (the twist,
the doubt, the thing most people miss) → THE LOOK (what to see now, in the object itself) → THE PAYOFF
(one line that lands, then a short route cue).
**R-INTRO tracks:** orientation in one breath, one story that explains the room, one detail to find,
route cue.

**Sentence rules**
- One idea per sentence. Average 12–16 words; vary hard (a 4-word sentence after a 25-word one).
- No parentheses, no semicolons, minimal em-dashes (max 2 per track — each becomes a spoken pause).
- Numbers spoken the way people say them ("around 1512", "almost a century later"), max 3 dates a track.
- Name a person, then use "he/she" — don't repeat full names and titles.
- One clear "you" moment per track (what you can see/feel right now). Guided looking is welcome mid-track;
  never open with a command (Rule 12 stands).
- Hedge honestly in human words: "It's a wonderful story. And it may not be true."
- One warm or wry aside per track, maximum. No exclamation marks.
- Every fact in the script traces to the FACTCHECK_LOG (official source first).

**Length:** R-INTRO 180–280 words · W-FOCUS 250–360 · ANCHOR/CLOSE 250–360. Tracks over ~2,800
characters are split at a paragraph for rendering (engine limit), never mid-thought.

## 3. The direction layer (engine-neutral, applied at render time)
The clean script is the single source of truth (PDF + audio text). Performance direction lives in a
sidecar `NNN.perf.txt`; stripping its tags must reproduce the clean script **exactly** (validated).

```
@brief: one line — who is speaking, to whom, in what mood   (for humans + future engines)
@pace: slow | medium-slow | medium | medium-fast
@energy: start→peak, e.g. 2→4 (1 = hushed, 5 = animated)
---
Paragraph text with inline tags.
```
**Tag vocabulary (fixed, small):**
| Tag | Meaning | ElevenLabs v3 | Multilingual v2 | Clean script |
|---|---|---|---|---|
| `[pause]` | beat, ~0.5 s | `…` | `<break time="0.6s" />` | removed |
| `[long pause]` | ~1.2 s, before a reveal | `… …` | `<break time="1.2s" />` | removed |
| `[warmly]` `[quietly]` `[amused]` `[curious]` `[conspiratorial]` `[reverent]` `[wry]` `[lightly]` | delivery colour for the following sentence(s) | passed through as audio tag | removed | removed |
| `*word*` | stress this word | WORD (caps) | plain | plain |
Rules: at most ~1 delivery tag per paragraph; pauses only where a human would breathe or before a
payoff; never tag every sentence (over-direction sounds like acting, not talking).

## 4. Voice
- Engine: **ElevenLabs** (user's account). Model decided by blind bake-off: `eleven_v3` + direction
  layer vs `eleven_multilingual_v2` plain (v2 is steadier; v3 is more expressive but can over-act).
- One narrator voice for the whole series (brand consistency). Chosen once by blind listening on the
  3 calibration tracks; re-checked only for a new language. Long-term option on file: licensed clone
  of a hired professional narrator (consent + licence in contract).
- Pronunciation: ElevenLabs reads Italian/Egyptian names natively — the respelling layer is OFF for
  ElevenLabs by default; any name it gets wrong is added to a per-engine override list after listening.

## 5. Production (mastering)
- Render at mp3_44100_128; deliver at 96 kbps mono (spoken word; 40 kbps retired).
- Loudness normalised to −16 LUFS integrated, −1.5 dBTP (phone listening standard).
- 0.6 s between paragraphs comes from the direction layer; 2 s tail per track (was 5 s dead air).
- Optional signature: a 2–3 s licensed music sting on the opening and on each section intro only.

## 6. Quality gates (repeatable process)
1. **Verify** — real visitor route (palace + garden), current placements/closures (official source),
   coverage vs official highlights. Logged.
2. **Story script** — rewrite to §2; facts only from the log.
3. **Direction** — perf sidecars to §3; validator: tags stripped == clean script.
4. **Voice** — series voice fixed by blind bake-off (once).
5. **Render** — on the user's Mac (`render_v5_elevenlabs.py`); container cannot reach TTS.
6. **Master** — §5.
7. **Listen QA (human, mandatory)** — Claude cannot hear audio. Score every new/changed track 1–5 on:
   Naturalness · Pacing · Pronunciation · Engagement · Accuracy-as-heard. Any score <4 → fix text or
   direction → re-render that track only.
8. **Field test** — 3–5 real visitors walk it; complaints logged; then ship + snapshot source.
