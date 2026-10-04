# AUDIT BRIEF — Tour #43 Palazzo Pitti + Boboli Gardens (V4.5 audio guide), 4 Oct 2026

You are one of several reviewers auditing a shipped, 92-track English walking audio guide.
Today is **Sunday 4 October 2026**. Work read-only: DO NOT edit any file except your own findings file.

## Material
- `/home/claude/pitti/tracks/NNN.txt` — one file per track (NNN = play order 001–092). Each holds the
  printed PDF page (header with internal ID + ROOM/STOP label, WHERE/WHAT/LISTEN card, prose) AND the
  exact spoken audio script. The spoken script is what visitors hear.
- `/home/claude/pitti/tracks/INDEX.txt` — all 92 tracks: play order, internal ID, room/stop, title.
  Use it to avoid proposing "missing" works that are already covered elsewhere in the tour.
- Room numbering used by the guide = the official Gallerie degli Uffizi room numbers for Palazzo Pitti
  (e.g. Palatine: Sala di Venere 28, Apollo 27, Marte 26, Giove 25, Saturno 24, Iliade 23 …).

## Authority (strict)
- **Tier 1 = official**: uffizi.it (Gallerie degli Uffizi — artwork pages usually carry a location /
  "sala" line; museum pages; itineraries; **notices/avvisi** for closures), the Gallerie's official
  floor plans/maps, official press releases. Record the URL and the page's date if shown.
- **Tier 2 = corroborated**: ≥2 independent recent (2025–2026) sources that agree, no contrary signal.
- Otherwise **UNVERIFIED** — say so plainly. Never upgrade a guess. Never invent or reconstruct a URL;
  cite only pages you actually fetched/saw in search results.
- Beware stale sources (old floor-plan PDFs, pre-2020 guidebooks, pre-reopening Royal Apartments info).
- Known context (re-verify, don't assume): Sala di Saturno (Room 24) reported temporarily CLOSED and
  Sala di Giove (25) OPEN as of 8 Jun 2026; Treasury of the Grand Dukes was closed for maintenance
  from Feb 2026; Royal Apartments reopened Jan 2025 with timed reservation; Buontalenti Grotto opens at
  set times only. Doni portraits (Raphael) are at the UFFIZI since 2018 — never propose them for Pitti.
- Add-on #25 (house rule): spoken prose must not contain ticket prices, opening hours or temporary-
  exhibition content; closures only where needed for navigation. Flag violations.

## Output
Write your findings to the file path given in your task, in Markdown, with these sections (omit a
section only if your task says so):
A. PLACEMENT — table: play# | work/room | guide says | current (official) | verdict (CORRECT / WRONG /
   MOVED / CLOSED / ON LOAN / UNVERIFIED) | tier | source URL + date
B. ACCURACY — only problems: play# | exact quote from the SPOKEN script | problem (WRONG / NEEDS HEDGE /
   OUTDATED / SCRIPT≠PDF) | proposed correction (one sentence, same voice) | source URL
   Then one line: "N claims checked, M problems".
C. STALE / OPERATIONAL LINES — time-sensitive wording that will date badly or breaks Add-on #25.
D. COVERAGE GAPS — official highlights for your section not covered anywhere in INDEX.txt:
   work | artist | current official room | source | where in the route it would sit | priority (H/M/L)
E. ROUTE CUES — every "next / ahead / turn / through the door / back to" instruction in your tracks:
   play# | cue (quote) | consistent with the real layout? | fix
F. COULD NOT VERIFY — list honestly, with what you tried.

Be thorough but economical: check every work and every load-bearing claim (dates, attributions,
provenance, measurements, anecdotes, "the first/only/largest" claims). Report OKs as counts, details
only for problems. Your final reply: 5–8 line summary + the findings file path.
