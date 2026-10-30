# Audit fixes, tracks 001–018 (applied 30 Oct 2026)

Source: `research/AUDIT_V5_001-018.md` (1 MUST · 13 SHOULD · 17 NICE), plus the lead's decisions 1–9.
Finding IDs are track.number as numbered in the audit. "ALL.1" is the "Across all tracks" item, R1–R3 are the "Problems in the research files" items.
`python3 v5/lint.py` prints OK for all 18 tracks after these changes.

**Totals: 26 applied (1 MUST, 11 SHOULD, 14 NICE) · 5 not done (2 SHOULD by lead decision, 3 NICE).** Research file: R1 fixed.

Word counts after the changes: 001 357 · 002 297 · 003 258 · 004 290 · 005 258 · 006 211 · 007 278 · 008 296 · 009 291 · 010 289 · 011 242 · 012 255 · 013 285 · 014 210 · 015 196 · 016 240 (unchanged) · 017 213 (unchanged) · 018 266.

## MUST

- **005.1 (HOLD the whole track)**: **done differently, per lead decision 1.** Not held, dropped or renumbered. The track is now a position-free walk-along track, heard while walking on through the Roman houses. It names the four places as things to look for on the labels, with their glosses: the Casa de Baco (Bacchus, god of wine), the Casa de la Ninfa (nymphs), the Patio del Océano with the three-metre mural the city's tourism office lists, and the Hospitium de los Delfines (hospitium = hospitality). It never says "here", "in front of you" or where anything is. Same tags (`[lightly]`, `[pause]`, `[quietly]`), same six-paragraph shape, R, 258 words.
  - Opening: "The names in this part of the Antiquarium sound like…" → "As you walk on through the Roman houses, keep an eye on the labels. Some of the names sound like…"
  - Names: "The first is the Casa de Baco… Close by is the Casa de la Ninfa… Then comes the Patio del Océano… with a three-metre mural" → "Look for the Casa de Baco… Look, too, for the Casa de la Ninfa… Two more names are worth watching for. The Patio del Océano is the Ocean Courtyard, and the city's tourism office lists a three-metre mural there."
  - Layer line: "Then the Roman layers end. The next one you'll see belongs to Moorish Seville" → "Above the Roman layers lies Moorish Seville" (about the layers, not the route).
  - Ending: "Walk on to the Moorish house, the casa almohade, and look for its label. The next stop in the Antiquarium is The Almohad house." → "Keep reading the labels as you walk. When you reach the one for the casa almohade, the Almohad house, play the next stop in the Antiquarium: The Almohad house. If you passed it earlier, play that stop now, before you leave the Antiquarium." This works whichever comes first.
  - Header: @room → "Level −1 · Antiquarium, walking through the Roman houses". @where, @what, @listen and @brief were rewritten to say it is a walk-along track with no fixed spot. @what records the lead decision and the O4 check.
  - Knock-on (decision 9): 004's ending now matches 005's new @where (see 004).
  - `v5/ONSITE_CHECKLIST.txt` O4: added "005 BEFORE RELEASE". It says to check every name against the label photos, to fold 005 into 004 if the labels aren't there, and to check the last cue against the real order (ALT-A). Under the listening checks: added "005 never says 'here', 'in front of you' or where a house is".

## SHOULD

- **001.1 (H listener sent to a track they don't have)**: fixed (and lead decision 3). "If it's closed when you're here, go to the lifts beside its entrance and play A plaza with many lives." → "If you're on the full tour and it's closed, go to the lifts beside its entrance and play A plaza with many lives." ("when you're here" was cut to keep 001 under 360 words.)
- **001.2 ("the numbers may jump")**: fixed per lead decision 2. The idea stays, now about the track numbers on your phone. "Whichever is on your phone, play it in order: the numbers may jump, and every stop tells you where to go next." → "Whichever version you have, play the stops in order. The shorter ones skip some, so the track numbers on your phone may jump. Every stop tells you where to go next." No number is spoken. PLAN §4's "any numbering" line was not edited.
- **001.3 (durations unconfirmed)**: **not done, lead decision 3.** The durations stay. O17 is already on the checklist ("Correct 001 … if far off").
- **003.1 (contradicts 002 on who dug first)**: fixed. "The first proper look under this square was paid for by the market traders." → "Before the big digs, the very first look under this square was paid for by the market traders."
- **004.1 ("And here she is")**: fixed. "And here she is, under a Seville street." → "Someone in Roman Hispalis wanted her on their floor, here, under what is now a Seville street."
- **006.1 (30-word sentence)**: fixed and split. "In the same age, the Almohad caliph Abu Ya'qub Yusuf built the city's Great Mosque, and in 1184 work began on its minaret, the tower we now call the Giralda." → "The Almohad caliph Abu Ya'qub Yusuf built the city's Great Mosque. In 1184, work began on its minaret. Today we call it the Giralda." I dropped the audit's "In those same decades" because the sentence before it already reads "Those were great decades for Seville".
- **009.1 ("the house" assumes 006)**: fixed. "as the house found under this square" → "as a house found under this square".
- **009.2 ("Fernando III")**: fixed per lead decision 4. "When Fernando III took the city in 1248" → "When King Fernando the Third took the city in 1248". I checked every track and bridge: no other Roman-numeral regnal numbers. Added "King Fernando the Third" to the checklist's names list.
- **010.1 (fish tanks overstated)**: fixed with the audit wording.
  - Opening: "Roman tanks, still packed with fish." → "Roman tanks, filled with fish remains." ("ever" was also dropped, as the audit suggested.)
  - Find: "led to five tanks, each about three metres across. When they were dug out, the tanks were still full of compacted fish remains. Judging by what filled them…" → "led to five tanks. Four have been excavated. When the works was abandoned, they were filled with rubbish, mostly compacted fish remains. Judging by that fill…"
  - @what and @sources were updated to quote "se han excavado cuatro" and "vertidos de abandono".
- **012.1 (six figures in three sentences)**: fixed with the audit wording. "…close to 30 metres… The whole structure is about 150 metres long and 70 wide, spread over six parasols. A walkway about 250 metres long snakes across the top, and this platform crowns it." → "…close to thirty metres… Below you, six parasols spread out over a hundred and fifty metres, and the walkway snakes across their tops. This platform crowns it."
- **013.1 (8.5 million museum sentence)**: fixed per lead decision 7. The sentence is cut. "…to a final bill of about 102 million euros. The museum for the Roman remains alone added 8 and a half million." → "…to a final bill of about 102 million." @what notes that the museum figure is left out.
- **014.1 (no next step for people who skip the film)**: fixed per lead decision 6. Added after the film line: "If not, play From building site to city symbol as you walk down, past the exhibition." This matches 016's @where ("play it as you walk down").
- **ALL.1 ("Mirador 360º" for TTS)**: **not done, lead decision 5.** The English pronunciation file respells it.

## NICE

- **001.4**: fixed. "This guide takes you from one to the other." → "This guide connects the two."
- **001.5**: fixed, in a shorter form to fit the word cap. "If you came in from the north side, you'll reach the same underground level." → "From the north entrance, the way down leads to the same underground level."
- **001.6 (relax lint to allow "ticket office")**: **not done.** It would change the lint gate, which the brief tells me to pass, not edit. "The taquilla, the box office" and "its own admission" work as they are. Lead's call.
- **002.1**: fixed. "a window into two thousand years of the city." → "a window into Roman and Moorish Seville."
- **002.2 (cut "run by Seville City Council")**: **not done.** PLAN §4 prescribes exactly that wording. O4 already checks the operator on the signs, and the checklist trigger ("operator confirmed → 002 may say 'the city's culture institute'") assumes the line is there.
- **004.2 (Sigma has no gloss)**: fixed. "There is the Casa del Sigma, and the Casa de la Noria, the House of the Water Wheel." → "There is the Casa del Sigma, the House of the Sigma, the Greek letter. And there is the Casa de la Noria, the House of the Water Wheel." It makes no claim about why the house has that name.
- **007.1**: fixed. "Within ten years, traders had a wooden market here." → "Soon, traders had a wooden market here."
- **008.1**: fixed. "That's what you're walking on now." → "That's what's all around you now."
- **010.2**: fixed, as part of 010.1. "each about three metres across" was dropped to make room for "Four have been excavated".
- **011.1**: fixed. "In 2007 the engineers warned…" → "By one account, in 2007 the engineers warned…"
- **012.2 (cathedral bulk unconfirmed)**: script kept, as the audit advised. Added a fallback to O7 in the checklist: if only the Giralda is clear from the Mirador, 012 says "with the cathedral beside it".
- **013.2 (Observer unconfirmed)**: fixed with the audit's safe version. "The British critic Rowan Moore, writing in *The Observer*, was dry about it" → "The British critic Rowan Moore was dry about it". @what now says the review is relayed by Dezeen. Easy to put back if the lead accepts Observer.
- **013.3**: fixed. "and Feeling Sevilla, the film room, which you should play before you go in." → "and Feeling Sevilla, about the film room. Play that one before you go in."
- **014.2**: fixed. "and the Feria." → "and the Feria, Seville's spring fair."
- **015.1**: fixed. "The curved LED screen is 21 metres long and 3 metres high." → "The curved LED screen, three metres high, runs that whole 21 metres."
- **015.2**: fixed. "the timber makers record that its platform was built of steel and concrete, not wood." → "the timber makers record that the platform built at this height is steel and concrete, not wood."
- **017.1 ("by the operator's count")**: **not done.** The audit marks it optional. The arithmetic (1973 to Dec 2010) holds, the title already commits to 37, and putting the attribution in the hook would flatten it.

## Other audit notes

- **009.3 (MoMA "cathedral without walls")**: no change needed. The audit confirms the script's wording is accurate.
- **018 pronunciation note ("Mayer H. hoped")**: fixed in the text, so the TTS can't read "H." as the end of a sentence. "It's one of the four layers of the architect's plan. Jürgen Mayer H. hoped…" → "It's one of the four layers of the design. Its architect, Jürgen Mayer H., hoped…". The pronunciation file in `build/` was not touched (out of scope).
- **R1 (FACTS §8 cites S-HIST for Red Dot)**: fixed. In `research/FACTS_OCT2026.md`, the row now cites JMH + red-dot.org, and a dated correction note (30 Oct 2026) cites https://www.red-dot.org/project/metropol-parasol-29871. 013's @sources were corrected the same way.
- **R2 (andalucia.org Antiquarium page repeats the banned discovery claim)**: no action needed. No track cites it for the discovery history: 002 uses it only for "1st c. to 13th c." and Tiberius, 006 for the date of the Moorish house.
- **R3 (writers' 010–018 notes out of date on "euros")**: noted only. The writers' notes were not edited.

## Bridges (decision 8)

No changes needed. None of the endings that bridges hang on changed: 001's last paragraph, 008's, 012's and 013's next-stop sentence are as before. Every bridge in `v5/bridges/*.txt` still follows on from its cue.

## Endings changed (decision 9) and the next track's @where/@room

- 004 → 005: "Walk on through the Roman houses, and play the next stop in the Antiquarium as you go." This matches 005's new walk-along @where/@room.
- 005 → 006: plays at the casa almohade label. This matches 006's @where ("at the label for the casa almohade").
- 014 → 015 or 016: the film branch matches 015's @where (outside the Feeling Sevilla room). The skip branch matches 016's @where (as you walk down past the exhibition).

## Not touched

git, `build/`, `bundle/` (its perf copies are now stale until the next build), PLAN.md (its 005 row and the §4 "any numbering" line still read as before the lead's decisions), other guides.
