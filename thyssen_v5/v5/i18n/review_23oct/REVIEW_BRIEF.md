# Review brief — Museo Nacional Thyssen-Bornemisza, Yo Tours 23 Oct 2026 (70 tracks), ONE language (ES, FR or DE)

You are an independent native-level editor. You did not write this translation. Customers complained that an earlier guide
sent them to wrong rooms, so navigation accuracy comes first, then facts, then naturalness for the ear (a synthetic voice reads it).

Files
- English (source of truth, read-only): /home/claude/audioq/thyssen_v5/v5/tracks/NNN.perf.txt
- Translation brief the translators followed: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/thy_i18n/BRIEF.md
- Yours to edit: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/thy_i18n/<lang>/NNN.json {"title","where","body"}
- Translator notes: notes/<lang>_*.md (read them; they list open points)

## 0. Sync first — the English changed after translation
- 031: "before a stroke in 1835 ended his work in oils" → "before a stroke in 1835 largely ended his work in oils".

## A. Every track, sentence by sentence against the English
Meaning and facts (incl. hedges and every "if…"), navigation (room numbers and letters exactly, floors, glass lifts, "turn the
corner", "back wing", "stay in this room", Extra announcements and "the next main stop is…"), official titles (ES: the museum's
Spanish titles of works and rooms; check doubtful ones on museothyssen.org with WebFetch, one page at a time, never in bursts,
never curl/browser), quotations handled per brief rule 11, formal address, natural spoken style, consistent terms across the
two halves (001–028 and 029–057 were done by different translators: unify terminology, room-word, glossary terms).
TTS safety: no symbols the voice may misread (+ & % ·), regnal numbers in words, no abbreviations.
Fix in place. Keep the check passing:
  python3 /home/claude/audioq/thyssen_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/thy_i18n <lang>

## B. Navigation scan (all 57)
For each track compare the LAST paragraph with the English: same rooms, same order, same floor, same things to look for.
Check every @title starts with the translated room word and number (Sala/Salle/Saal 27 · … or A–J; Extras "· Extra ·").

## Report
Write notes/<lang>_REVIEW_23OCT.md: the sync change, every other change (track, before → after, why), and anything for the lead.
Final reply ≤150 words with your verdict (ready / not ready).
