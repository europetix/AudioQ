# Review brief — Real Alcázar de Sevilla, Yo Tours 30 Oct 2026 (35 tracks), ONE language (ES, FR or DE)

You are an independent native-level editor. You did not write this translation. Customers complained that earlier guides
sent them to wrong rooms, so navigation accuracy comes first, then facts, then naturalness for the ear (a synthetic voice
reads it).

Files
- English (source of truth, read-only): /home/claude/audioq/alcazar_v5/v5/tracks/NNN.perf.txt
- English bridges (read-only): /home/claude/audioq/alcazar_v5/v5/bridges/*.txt
- Translation brief the translators followed: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/alc_i18n/BRIEF.md
- Yours to edit: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/alc_i18n/<lang>/NNN.json {"title","where","body"}
  and <lang>/bridges.txt
- Translator notes: notes/<lang>_*.md (read them; they list open points)
- Map legend (numbers 1–53 and Spanish names): /home/claude/audioq/alcazar_v5/research/VISIT_ROUTE_AND_SPACES_OCT2026.md

## A. Every track, sentence by sentence against the English
Meaning and facts (incl. hedges, "Vasari tells", every "if…" and every "if the way is closed…"), navigation (map numbers and
Spanish place names exactly, never "number 11", left/right exactly as the English, "follow the Salida signs", the Cuarto
Real Alto as a separate timed visit, the next main stop after an Extra), quotations per brief rule 11 (verify any
original-language wording you keep with WebFetch, one page at a time, never in bursts, never curl/browser, never complete a
CAPTCHA), formal address, natural spoken style,
consistent terms throughout (Extra announcements, "the next main stop is…", glossary terms, rulers' names).
TTS safety: no symbols the voice may misread (+ & % · ×), regnal numbers in words, no abbreviations.
Make sure nothing was ADDED that is not in the English (e.g. treaties, dates, names).
Fix in place. Keep the check passing:
  python3 /home/claude/audioq/alcazar_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/alc_i18n <lang>

## B. Navigation scan (all 35) and bridges
For each track compare the LAST paragraph with the English: same rooms, same order, same floor, same things to look for.
Check every @title starts with the same leaflet number and Spanish name as the English (CRA Extras: "CRA nn · Extra ·").
Check every bridge line: same key as the English (NNN E>MMM / NNN H>MMM), same route, starts with the language's
"On this shorter tour," — and every English bridge line has exactly one translated line.

## Report
Write notes/<lang>_REVIEW_30OCT.md: every change (track, before → after, why), and anything for the lead.
Final reply ≤150 words with your verdict (ready / not ready).
