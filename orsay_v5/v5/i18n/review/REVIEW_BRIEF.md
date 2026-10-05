# Review brief — Musée d'Orsay V5 audio guide, ES / FR / DE (75 tracks per language)

You are an independent native-level editor for ONE language. The translations were written in three blocks (001–025, 026–050,
051–075) by different translators. Your job: catch the errors translations typically contain, and make the whole guide read as
ONE natural voice. The English is fact-checked against the museum's own pages and is the single source of truth.

## Files
- English: /home/user/AudioQ/orsay_v5/v5/tracks/NNN.perf.txt (header, ---, spoken body). Read-only.
- Yours to edit in place: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/orsay_i18n/<lang>/NNN.json  {"title","where","body"}
- The translation rules the text must still satisfy: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/orsay_i18n/BRIEF.md — read it first, especially rules 9–14 and the glossary.
- The translators' notes: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/orsay_i18n/notes/<lang>_*.md — read them; they list
  open questions, title choices and how each quotation was handled.
- Do not edit any other file.

## Already settled (do not undo)
- 018: Bazille was killed at TWENTY-EIGHT (the English was corrected on 5 Oct from the museum's own page; your file already says 28).
- Navigation phrases: ES "Escuche su pista allí." · FR "Écoutez sa piste là-bas." · DE "Spielen Sie dort den passenden Titel ab."
  (and their plural / "in front of it" forms in BRIEF.md rule 9).

## Check EVERY track, sentence by sentence against the English
1. MEANING: any fact changed, added, dropped, softened or strengthened (dates, numbers, ages, measurements, names, who did what,
   hedges such as "probably", "allegedly", "the story goes", "the museum says", "if it is on show"). Fix to match the English.
2. MISTRANSLATIONS: false friends, wrong sense of a word, literal idioms, wrong art terms (canvas, panel, plaster, bronze,
   stoneware, still life, nude, dealer, collection, hang, wall, room, gallery), wrong gender/agreement, wrong tense.
3. NAVIGATION: level, room numbers, Seine side / rue de Lille side, left/right, up/down, which wall, near what, and the
   description of the next work (colours, size, shape, figures) must match the English precisely. Check every closing paragraph.
4. LOANS AND OPTIONS: 007, 008, 020, 021, 045, 046, 052, 053, 055, 056 and the optional 011/012 contain "if…/otherwise…"
   conditions. Check each condition word for word: a wrong one sends a traveller to the wrong room.
5. NATURALNESS FOR THE EAR: it must sound like a good live guide in that language, not like a translation. Short spoken
   sentences; vary repetitive openings; remove calques; formal address (usted / vous / Sie) everywhere.
6. CONSISTENCY across all 75 tracks: same term for the same thing (glossary), same name for each artwork and each room or space,
   same navigation phrases, same spelling of names. Pay attention to the seams between blocks (025/026, 050/051).
7. TITLES: as set in BRIEF.md rule 11. FR: the museum's exact French titles.
8. QUOTATIONS (BRIEF.md rule 12):
   - FR: every passage inside « » must be a verified original whose URL is listed in the FR notes. If a quoted passage has no
     listed source, turn it into reported speech without quotation marks. Quotes the English gives as reported speech stay so.
   - ES/DE: quotes are faithful translations of the English quote, with the same attribution. No embellishment.
9. TTS SAFETY: no abbreviations the voice may misread (Saint not St., Doktor/doctor/docteur not Dr), regnal numbers spelled out,
   years as digits, no ; or ( in the body, no symbols such as & % × °.

## Keep the automatic checks passing
After editing, every track must still pass:
  python3 /home/user/AudioQ/orsay_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/orsay_i18n <lang>
(same delivery tags in the same order and paragraph, no fewer pauses, same paragraph count, not longer than the English,
every year present as digits, no ; or ().

## Report
Write the full change list to /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/orsay_i18n/<lang>_REVIEW_LOG.md
(a short header with your global decisions, then per track: field, before → after, why).
Final report (max ~250 words): number of tracks changed, the main kinds of errors with 3–5 concrete examples (track,
before → after), anything you could not resolve, and your honest verdict on readiness for a native-speaker spot check.
