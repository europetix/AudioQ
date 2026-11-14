# Review brief — Barcelona Cathedral, Yo Tours 14 Nov 2026 (36 tracks), ONE language (ES, FR or DE)

You are an independent native-level editor. You did not write this translation. Customers complained that earlier guides sent them to wrong places, so navigation accuracy comes first, then facts, then naturalness for the ear (a synthetic voice reads it).

Files
- English (source of truth, read-only): /home/claude/audioq/bcncat_v5/v5/tracks/NNN.perf.txt
- English bridges (read-only): /home/claude/audioq/bcncat_v5/v5/bridges/*.txt
- Translation brief the translator followed: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/bcn_i18n/BRIEF.md
- Yours to edit: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/bcn_i18n/<lang>/NNN.json and <lang>/bridges.txt
- Translator notes: notes/<lang>_001-036.md (read them; they list open points)
- Context: bcncat_v5/v5/PLAN_V2.md, bcncat_v5/research/FACTS_*.md, research/map/

## A. Every track, sentence by sentence against the English
Meaning and facts (every hedge and attribution, every "if you're on the full tour…"), navigation (place names identical across titles, cues and bridges; left/right, "before the check", "the one without the tower" exactly as the English; nothing added or dropped), quotations per brief rule 11 (verify any original-language wording kept, with WebFetch one page at a time, never bursts, never curl/browser, never a CAPTCHA; if unverifiable make it a faithful translation or reported speech), formal address, natural spoken style, consistent terms, TTS safety (no symbols the voice may misread, regnal numbers in words, no abbreviations). Nothing ADDED that is not in the English. Fix in place. Keep the check passing:
  python3 /home/claude/audioq/bcncat_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/bcn_i18n <lang>

## B. Navigation scan (all 36) and bridges
For each track compare the LAST paragraph with the English: same places, same order, same things to look for; the spoken `<place> · <title>` matches the destination's translated @title. Every bridge: same key as the English, same route, starts with the language's opener (ES "En esta versión corta," FR "Dans cette version courte," DE "In dieser Kurzfassung"), not longer than the English, and every English bridge has exactly one translated line.

## Report
Write notes/<lang>_REVIEW_14NOV.md: every change (track, before → after, why), and anything for the lead. Final reply ≤150 words with your verdict (ready / not ready).
