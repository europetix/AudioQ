# Review brief — Orangerie V5 audio guide, ES / FR / DE (55 tracks per language)

You are an independent native-level editor for ONE language. The translations were written by three different
translators (blocks 001–018, 019–036, 037–055). Your job is to catch the errors translations typically contain
and to make the whole guide read as ONE natural voice. The English is fact-checked and is the single source of truth.

## Files
- English: /home/user/AudioQ/orangerie_v5/v5/tracks/NNN.perf.txt (header, ---, spoken body)
- Yours to edit in place: /tmp/claude-0/-home-user-AudioQ/9645e4c6-89fb-52f0-9dd4-640b4e64f64f/scratchpad/or_i18n/<lang>/NNN.json  {"title","where","body"}
- Translation rules the text must still satisfy: /tmp/claude-0/-home-user-AudioQ/9645e4c6-89fb-52f0-9dd4-640b4e64f64f/scratchpad/or_i18n/BRIEF.md (read it first, especially the rules and glossary)
- Do not edit any other file.

## Check EVERY track, sentence by sentence against the English
1. MEANING: any fact changed, added, dropped, softened or strengthened (dates, numbers, names, who did what,
   hedges such as "probably", "the story goes", "the museum says"). Fix to match the English exactly.
2. MISTRANSLATIONS: false friends, wrong sense of a word, literal idioms that make no sense, wrong art terms
   (canvas, panel, oil, still life, nude, dealer, collection, hang, wall, room), wrong gender/agreement, wrong tense.
3. NAVIGATION: directions and what to look for must match the English precisely (left/right, up/down, which wall,
   which room, colours and shapes of the next work). Travellers rely on these.
4. NATURALNESS FOR THE EAR: it must sound like a good live guide in that language, not like a translation.
   Short spoken sentences; vary repetitive openings; remove calques; formal address (usted / vous / Sie) everywhere.
5. CONSISTENCY across all 55 tracks: same terms for the same thing (glossary in BRIEF.md), same way of naming
   each artwork, same phrasing for "listen to its track there", same names for Room 1 / Room 2 / level −2.
6. TITLES: artwork titles as set in BRIEF.md rule 9. For FR, the French titles must be exactly as the English
   script gives them.
7. TTS SAFETY: no abbreviations the voice may misread (write "Saint" not "St.", spell out "numéro"),
   years as digits, no ; or ( in the body, no symbols like & or %.

## Keep the automatic checks passing
After editing, every track must still pass the self-check snippet in BRIEF.md (same delivery tags in the same
order and paragraph, no fewer pauses, same paragraph count, not longer than the English, all years present).

## Report (max ~250 words)
Number of tracks changed, the main kinds of errors you found with 3–5 concrete examples (track, before → after),
any fact or term you could not resolve, and your honest verdict on readiness for a native-speaker spot check.
Also write the full change list to /tmp/claude-0/-home-user-AudioQ/9645e4c6-89fb-52f0-9dd4-640b4e64f64f/scratchpad/or_i18n/<lang>_REVIEW_LOG.md (track, what changed, why).
