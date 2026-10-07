# Second round of English changes, 7 Oct 2026 (after an independent route audit)

IMPORTANT: tracks 039 and 040 were SWAPPED in every language. Your <lang>/039.json is now "Toward the twentieth century"
(Room 17) and <lang>/040.json is now the Rotonda di Palmieri (Room 18). Check the titles to confirm.
Update only these passages (old English → new English); keep everything else as it is. Then run the same --check.

005 body: "...so keep her track for that room and walk on to the Sala di Ulisse."
      →   "...so keep her track for that room, and walk on through a few smaller rooms to the Sala di Ulisse."
006 body: "If you're in the Sala di Prometeo, walk on to the room marked Sala di Ulisse."
      →   "If you're in the Sala di Prometeo, walk on through a few smaller rooms to the room marked Sala di Ulisse."
018 body: "around the same time as La Gravida, which you've just seen."  →  "around the same time as La Gravida, back in the Sala di Prometeo."
019 body: "the small Florentine pictures you've just met, La Gravida and the Granduca."
      →   "the small Florentine pictures, like the Granduca you've just met."
035 where: → "In the first rooms of the Gallery of Modern Art, in front of the colossal marble head of Napoleon, far bigger than life
              (not the small porcelain bust of Napoleon in Room 2). Its exact room is not published; if it isn't on view, walk on to Room 3."
036 body: "the same man who was given Napoleon's marble head in the room you've just left."
      →   "the same man who was given Napoleon's colossal marble head."
037 body: "Look too for Giovanni Dupré's sculpture of Abel, dying."  →  "Somewhere in these rooms, look too for Giovanni Dupré's sculpture of Abel, dying."
038 body, last paragraph ([warmly] ...): → "[warmly] One more of Fattori's best-loved pictures is in this gallery, a tiny panel of women under an awning
              by the sea. Its story comes a little later. When you're ready, follow the room numbers on to Room seventeen, where the last
              stretch of the loop begins."
039 (Toward the twentieth century) body, last paragraph: "That's the end of the Gallery of Modern Art. Follow the signs back ... Play its track at the entrance."
      →   "Before you go on to Room nineteen, look in Room eighteen for a tiny panel, only twelve centimetres high, of women sitting under an
              awning by the sea. That's Fattori's Rotonda di Palmieri. Play its track in front of it."
040 (Rotonda) where: → "In Room 18 of the Gallery of Modern Art, in front of Fattori's Rotonda di Palmieri, if it is on view: the Ministry of
              Culture catalogue lists it in Room 18; the museum's own site does not publish its room. It is tiny, only 12 by 35 centimetres,
              so look closely along the walls."
040 body, last paragraph: "When you're ready, follow the room numbers on. Room seventeen begins the last stretch of the loop."
      →   "Then take the last rooms at your own pace. When you've finished, follow the signs back to the landing and go along the corridor
              to the right. A staircase of two short flights takes you into the Museum of Fashion and Costume, on this same floor. Play its
              track at the entrance."
Also fix, if your notes flagged them: room names in @where lines must be the Italian door signs (e.g. "Sala del Castagnoli",
"Sala di Saturno") wherever the English @where uses them (tracks 002, 004, 016 and any other JSON you hold).
