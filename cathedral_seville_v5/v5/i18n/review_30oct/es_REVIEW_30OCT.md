# ES review: Catedral de Sevilla 001–028 and bridges (30 Oct 2026)

This is an independent review of es/*.json and es/bridges.txt. I compared them with v5/tracks/*.perf.txt (020 as of 11:59:37) and v5/bridges/*.txt.

**Result after my edits:** `assemble.py --check … es` reports all 28 OK, exit 0. I did not run assemble without --check. I edited only es/001, 017, 020 and 028. The bridges needed no change.

## A. Changes (track: before → after, and why)

### 001, Opening
- **Version names**, changed to match the Alcázar ES 001 (recorrido completo / versión esencial / imprescindibles):
  - Before: "Esta guía es un recorrido en tres duraciones. La completa dura… La esencial… La de imprescindibles… Tenga la que tenga en su teléfono"
  - After: "Esta guía es un solo recorrido en tres duraciones. El recorrido completo dura… La versión esencial… La de imprescindibles… Sea cual sea la versión de su teléfono"
  - In paragraph 4, "casi al final de la versión completa" became "casi al final del recorrido completo".
  - "La versión de imprescindibles" (paragraph 6) was already consistent with the Alcázar.
- **Extras on the shorter tours:**
  - Before: "En una versión corta, los números saltan. Si se anuncia un Extra, no está en su teléfono: siga…"
  - After: "En una versión corta, los números saltan, y los Extras que se anuncien no están en su teléfono. Siga…"
  - Why: as two separate sentences, someone on the full tour could hear "an announced Extra is not on your phone" as applying to them. The English ties it to the shorter tour.
- **Signs:**
  - Before: "nombra el siguiente lugar en español, como en los carteles"
  - After: "nombra el siguiente lugar como aparece en los carteles"
  - Why: for a Spanish listener, the point is that the names match the signs. The place names themselves are unchanged.
- **Capilla Real:**
  - Before: "solo se ve tras su reja"
  - After: "solo se ve a través de su reja"
  - Why: the English says "seen only through its grille". "tras su reja" reads as "behind its grille".

### 017, Sala del Pabellón Extra
- Before: "la lista de pinturas de la catedral". After: "la propia lista de pinturas de la catedral".
- Why: the English says "the Cathedral's own list". The track is now at 173/173 words.

### 020, last paragraph (the English changed at 11:59, after translation)
- Before: "Primero hay un breve Extra sobre la propia Sala Capitular. Después, la siguiente parada principal, en la misma sala, es la Inmaculada de Murillo. [pause] Pase por el Antecabildo, la antesala, y siga el pasillo curvo hasta la Sala Capitular. Es la sala ovalada, con la Virgen de Murillo…"
- After: "En la Sala Capitular hay primero un breve Extra sobre la propia sala. La siguiente parada principal, en esa misma sala, es la Inmaculada de Murillo. [pause] Pase por el Antecabildo, la antesala, y siga el pasillo curvo hasta la Sala Capitular: la sala ovalada del cabildo, con la Virgen de Murillo presidiendo un anillo de cuadros redondos."
- Why: it now follows the new English cue in the same order: where the Extra is, then the next main stop in the same room, then the route. It also uses the standard "La siguiente parada principal" formula, without the added "Después".

### 028, Puerta del Perdón
- Before: "Una elección intencionada". After: "Una elección con toda la intención".
- Why: this keeps the wry "pointed choice".

## B. Checked, no change needed

- **003 "Treinta y cuatro rampas"** is kept, as the lead confirmed (Turris Fortissima congress 2025: 34 ramps, 7 chambers). The translator's open note on 003 is closed.
- **Navigation.** I compared the last paragraph of all 28 tracks with the English. Rooms, order and landmarks match, and so do these points:
  - "vaya por su derecha" on the ramps (002–006, and the @where lines).
  - Capilla Real seen from the grille only (001, 022, 023).
  - Exit by the Puerta del Perdón with no re-entry (001, 028).
  - The next main stop after every Extra (004, 008, 016, 018, 020, 021).
  - "lado por donde bajó de la torre" / "lado opuesto a la torre" exactly as the English (010, 011, 012, 013, 014, 023, 024, 026).
  - There is no left/right in the English, and none was added.
- **Conditionals present:**
  - Lagarto / Príncipe entrances.
  - "¿No va a subir?"
  - "Si hay misa, escuche desde fuera de la reja."
  - "si se detuvo allí" (026).
  - "si su recorrido pasó por allí" (028).
  - "si puede verla" (028).
  - "Si es así" (025).
  - "si no compartieron la gloria" (014).
- **Titles.** Every @title starts with the same Spanish space name as the English. The Extra pattern "· Extra ·" is kept.
  - 007 "La nave" and 012 "Los pies de la iglesia" stand for English titles that have no Spanish space name.
  - The opening title has no space name.
- **Bridges.**
  - There are 7 lines, matching the 7 English lines, with the same keys: 006 H>008, 008 H>014, 011 E>013, 014 H>025, 022 E>025, 025 E>028, 025 H>028.
  - Each follows the same route and starts with "En esta versión corta,".
- **Quotations (rule 11).** No originally Spanish wording appears in quotation marks.
  - 006 ("mad" canon and the 1401 decision), 014 Mélida, 015 Faro a Colón and Hernando's bequest, 018 Murillo/Ponz and 027 Ortiz de Zúñiga are all reported speech.
  - The quotes kept in marks are the Arabic chronicler in 002 (the English rendering, translated) and The Nation in 011 (originally English).
  - None needed verification, so I fetched no pages.
- **Facts.** Dates, numbers, hedges ("se decía", "según cuentan", "la tradición", "se dice", "al parecer", "unos restos", "la catedral dice") and "the Cathedral says/calls" match the English. I found nothing added.
- **TTS and style.**
  - No symbols, abbreviations or Roman numerals.
  - Regnal names are in words (Fernando Tercero, Carlos Tercero, Pedro Primero), and years are in digits.
  - No semicolons, parentheses or dashes in speech.
  - Usted is used throughout. There is no vosotros, coger, vale, móvil or ordenador.

## For the lead
1. **007 stop label.** In 001, ES «al pie de la Giralda» renders the English stop name "at the foot of the Giralda". That name exists only in the English @room/@id of 007; the title is "The nave — A hollow mountain" / "La nave — Una montaña hueca". If the Spanish app shows the title, or keeps the English @room, a non-climber will not see "al pie de la Giralda" anywhere. The English has the same mismatch. Consider matching the 001 wording to whatever label the app actually shows.
2. **Translator notes.** The notes on 011, 014 and 019 are superseded by the revised English, and the Spanish already follows it. The 003 ramp-count flag is closed.
3. **Minor wording.** These were left as is and are acceptable:
   - 007 "El Guinness la registra".
   - 011 "el pintor de la propia Sevilla" ("Seville's own painter").
   - 023 "La catedral la considera de origen francés" ("The Cathedral calls her of French origin").

**Verdict: ready.**
