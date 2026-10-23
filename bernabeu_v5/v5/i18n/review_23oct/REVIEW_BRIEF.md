# Review brief — Tour Bernabéu, Yo Tours 23 Oct 2026 (28 tracks), ONE language (ES, FR or DE)

You are an independent native-level editor. You did not write this translation. Directions come first (the tour has no
stop numbers and few signs; three cases: full tour, match day, museum first), then facts, then naturalness for the ear
(a synthetic voice reads it to football fans walking the stadium).

Files
- English (source of truth, read-only): /home/claude/audioq/bernabeu_v5/v5/tracks/NNN.perf.txt
- Translation brief: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/bern_i18n/BRIEF.md
- Yours to edit: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/bern_i18n/<lang>/NNN.json
- Translator notes: notes/<lang>.md

## A. Every track, sentence by sentence against the English
Meaning and facts (scores, minutes, dates, counts, money, hedges, "as of autumn 2026"), directions (zones, every "if…",
every "play number …" — the number must match the English), quotations per brief rule 11 (ES: originally Spanish quotes
only verbatim-verified or reported speech), formal address, natural football language for fans, consistent terms,
TTS safety (no & % € + · symbols, no abbreviations). Fix in place. Keep the check passing:
  python3 /home/claude/audioq/bernabeu_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/bern_i18n <lang>

## B. Directions scan (all 28)
Compare the LAST paragraph of each track with the English, and every case instruction in 001, 003, 007, 008, 019–022.
Check every @title: "<zone> · …" with the glossary zone word; Extras "· Extra ·".

## Report
Write notes/<lang>_REVIEW.md: every change (track, before → after, why) and anything for the lead.
Final reply ≤150 words with your verdict (ready / not ready).
