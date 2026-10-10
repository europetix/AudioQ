# Review brief — Museo del Prado, Yo Tours 10 Oct 2026 (81 tracks), ONE language (ES, FR or DE)

You are an independent native-level editor. You did not write this translation. Customers complained that the previous
guide sent them to wrong rooms, so navigation accuracy comes first, then facts, then naturalness for the ear.

Files
- English (source of truth, read-only): /home/claude/audioq/prado_v5/v5/tracks/NNN.perf.txt
- Translation brief the translators followed: /tmp/claude-0/-home-claude-audioq/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/prado_i18n/BRIEF.md
- Yours to edit: /tmp/claude-0/-home-claude-audioq/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/prado_i18n/<lang>/NNN.json {"title","where","body"}
- Translator notes: notes/<lang>_*.md

## 0. Sync first — the English changed after translation (update these JSON files to match exactly)
- 030: Christ Carrying the Cross was cut (not reliably on display). Now Salome only: new @title, @where, and paragraphs 3–4 rewritten.
- 060: "Rubens came back to Madrid" → "Rubens came to Madrid himself".
- 003: the queen is now "Isabel Farnese" (as in 034) — use one consistent form in 003 and 034.
- 013: @where now "the Virgin with the Christ Child, the infant John the Baptist and an older woman".
- 069: "the ones you came up" removed from the stairs sentence.
- 044: @what says "Gift of Francesc Cambó" (header only — nothing to do unless your body says "bequeathed").

## A. Every track, sentence by sentence against the English
Meaning and facts (incl. hedges and every "if…"), navigation (room numbers, floors, stairs/lift, "back through", "next door",
"stay in this room", Extra announcements and the "if you're skipping the Extras" directions), official titles (ES: the
museum's Spanish titles), quotations handled per brief rule 11, formal address, natural spoken style, consistent terms.
Fix in place. Keep the check passing:
  python3 /home/claude/audioq/prado_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude-audioq/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/prado_i18n <lang>

## B. Navigation scan (all 81)
For each track compare the LAST paragraph with the English: same rooms, same order, same floor, same things to look for.
Also check every @title starts with the translated room word and number (Sala/Salle/Saal NN · …; Extras "· Extra ·").

## Report
Write notes/<lang>_REVIEW_10OCT.md: the sync changes, every other change (track, before → after, why), and anything for
the lead. Final reply ≤150 words with your verdict (ready / not ready).
