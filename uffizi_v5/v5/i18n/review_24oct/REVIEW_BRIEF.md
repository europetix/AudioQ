# Review brief — Uffizi Gallery, Yo Tours 24 Oct 2026 (67 tracks), ONE language (ES, FR, DE or IT)

You are an independent native-level editor. You did not write this translation. Customers complained that earlier guides
sent them to wrong rooms, so navigation accuracy comes first, then facts, then naturalness for the ear (a synthetic voice
reads it).

Files
- English (source of truth, read-only): /home/claude/audioq/uffizi_v5/v5/tracks/NNN.perf.txt
- English bridges (read-only): /home/claude/audioq/uffizi_v5/v5/bridges/*.txt
- Translation brief the translators followed: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/uff_i18n/BRIEF.md
- Yours to edit: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/uff_i18n/<lang>/NNN.json {"title","where","body"}
  and <lang>/bridges_001-034.txt, <lang>/bridges_035-067.txt
- Translator notes: notes/<lang>_*.md (read them; they list open points)
- Map: /home/claude/audioq/uffizi_v5/source/map.txt

## A. Every track, sentence by sentence against the English
Meaning and facts (incl. hedges, "Vasari tells", every "if…" and every "if the way is closed…"), navigation (room codes
exactly, never a code for the Botticelli rooms, floors, staircase names, "down one floor only — not to the street",
"back through", "the far-side doorway", "ask a warden", the next main stop after an Extra), titles of works (IT: the
museum's Italian titles; check doubtful ones on www.uffizi.it/opere/<slug> with WebFetch, one page at a time, never in
bursts, never curl/browser, never complete a CAPTCHA), quotations per brief rule 11, formal address, natural spoken style,
consistent terms across the two halves (001–034 and 035–067 were done by different translators: unify the room word,
floor names, staircase names, Extra announcements, "the next main stop is…", glossary terms).
TTS safety: no symbols the voice may misread (+ & % · ×), regnal numbers in words, no abbreviations.
Make sure nothing was ADDED that is not in the English (e.g. treaties, dates, names).
Fix in place. Keep the check passing:
  python3 /home/claude/audioq/uffizi_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/uff_i18n <lang>

## B. Navigation scan (all 67) and bridges
For each track compare the LAST paragraph with the English: same rooms, same order, same floor, same things to look for.
Check every @title starts with the same map code as the English (Botticelli tracks: the translated "Botticelli rooms").
Check every bridge line: same key as the English (NNN E>MMM / NNN H>MMM), same route, starts with the language's
"On this shorter tour," — and every English bridge line has exactly one translated line.

## Report
Write notes/<lang>_REVIEW_24OCT.md: every change (track, before → after, why), and anything for the lead.
Final reply ≤150 words with your verdict (ready / not ready).
