# Review brief — Palazzo Pitti audio guide, 7 Oct 2026 edition, ONE language (ES, FR or DE)

You are an independent native-level editor. You did not write this translation. Context: customers got lost because the
audio named paintings in the wrong rooms and did not match the room names written above the doors. The English was rebuilt
around the Italian door signs (Sala di Saturno, Sala di Giove …). The translations were updated to match.

## Files
- English (source of truth, read-only): /home/user/AudioQ/tour43_pitti_v5/v5/tracks/NNN.perf.txt
- Your language, assembled (read-only): /home/user/AudioQ/tour43_pitti_v5/v5/i18n/<lang>/tracks/NNN.perf.txt
- Yours to edit: /tmp/claude-0/-home-claude-audioq/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/pitti_i18n/<lang>/NNN.json {"title","where","body"} — the 24 changed tracks
  (002 004 005 006 007 010 014 015 016 017 018 019 020 023 025 027 033 034 035 036 037 038 039 040).
- What changed in English: CHANGES_7OCT.md and CHANGES_7OCT_B.md in the same folder. Translator notes: notes_<lang>.md.

## Part A — the 24 changed tracks, sentence by sentence against the English
Meaning (facts, hedges, the "if she isn't here…" fallbacks), navigation (which room, which door sign, what to look for),
naturalness for the ear, formal address, consistent phrase for "the room marked Sala di X". Track 017 is new: check it fully.
Edit the JSON in place. Keep the check passing:
  python3 /home/user/AudioQ/tour43_pitti_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude-audioq/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/pitti_i18n <lang>

## Part B — navigation consistency in ALL 61 tracks (read-only scan)
For every track of your language, compare the @where line and the LAST paragraph (the cue) with the English. Report any
place where a room name, room number, direction or "look for…" description differs from the English, and any Palatine room
named in your language instead of by its Italian door sign where the English uses the sign. If the problem is in one of the
24 JSON tracks, fix it; otherwise list it (track, sentence, fix) — do not edit the assembled files.

## Report
Write <lang>_REVIEW_7OCT.md in the same folder (changes made, Part B list). Final reply max ~150 words, with your verdict.
