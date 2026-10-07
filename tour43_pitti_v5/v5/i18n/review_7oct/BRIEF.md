# Update brief — Palazzo Pitti audio guide, 7 Oct 2026 edition → ES / FR / DE

The English guide was corrected after a customer complaint: "the rooms were named above the doors… the audio named
paintings that were not in the room where they were described." The English now names every Palatine room exactly as
written above its door (in Italian: Sala di Saturno, Sala di Giove …), every closing cue names the next door sign, two
paintings moved (Raphael's La Gravida is now in the Sala di Prometeo, with a fallback to the Sala dell'Iliade; Leo X is
gone, replaced by a NEW track 017 on Raphael's Ezekiel's Vision), and some Modern Art room numbers are now hedged.
Your job: bring ONE language in line with the new English. DO NOT EDIT ANY FILE except your own JSON files and notes.

## Files
- What changed, track by track (old English → new English): /tmp/claude-0/-home-claude-audioq/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/pitti_i18n/CHANGES_7OCT.md
- New English (source of truth): /home/user/AudioQ/tour43_pitti_v5/v5/tracks/NNN.perf.txt
- Your files to edit: /tmp/claude-0/-home-claude-audioq/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/pitti_i18n/<lang>/NNN.json  {"title","where","body"} — the 18 changed
  tracks, pre-filled with the current translation. Create <lang>/017.json for the new track.
- Style reference (read-only): the other translated tracks of your language in /home/user/AudioQ/tour43_pitti_v5/v5/i18n/<lang>/tracks/
  — match their voice, terms and navigation phrasing.

## Rules (all mandatory)
1. Change ONLY what the English changed (see CHANGES_7OCT.md); keep the rest of each existing translation word for word.
   Track 017 is translated in full.
2. FACTS identical to the English. Formal address: ES usted (neutral Latin-American/Spanish vocabulary), FR vous, DE Sie.
3. ROOM NAMES: always the Italian door sign exactly as in the English (Sala di Saturno, Sala dell'Iliade, Sala di Prometeo,
   Sala di Ulisse, Sala dell'Educazione di Giove, Sala della Stufa, Sala del Castagnoli, Galleria delle Statue, Sala di
   Giove, Sala di Marte, Sala di Apollo, Sala di Venere). You may add your language's gloss once, as the English sometimes
   does ("the Room of Jupiter"). "the room marked Sala di X" → ES "la sala con el letrero Sala di X" / FR "la salle marquée
   Sala di X" / DE "den Saal mit der Aufschrift Sala di X" (or an equally natural phrase, used consistently).
4. Titles: keep the "Sala di X · Artist — Title" form already in the JSON (room-intro tracks: "Sala di X — subtitle").
   Track 017: "Sala di Saturno · <Raphael in your language> — <Ezekiel's Vision in your language>".
5. Tags, pauses, paragraphs: same delivery tags in the same order and paragraph as the English; no fewer [pause]/[long pause];
   same paragraph count. Spoken length ≤ the English. Years as digits. No ; or ( in the spoken text. Never "next track".
6. Self-check until every file is OK:
   python3 /home/user/AudioQ/tour43_pitti_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude-audioq/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/pitti_i18n <lang>
7. Notes (terms you were unsure of, anything odd in the English): /tmp/claude-0/-home-claude-audioq/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/pitti_i18n/notes_<lang>.md
Final report: max ~120 words.
