# Real Alcázar de Sevilla: official vs third-party audio guides (as of 30 Oct 2026)

Prepared for Yo Tours (Alcázar V5 audio guide). Research was done with WebSearch and WebFetch only. Official sites were fetched one page at a time. No curl, no browser, no CAPTCHA.

**Grades**
- **OFF**: an official Real Alcázar / Patronato source (alcazarsevilla.org, its PDFs, the BOP ordinance).
- **SEC**: a secondary page that was fetched and read (operator, OTA, app store, EU portal, OCU, press, review sites).
- **SNIP**: seen only in a search-result title or snippet. It was not fetched, or the fetch was blocked.

All "read" dates are **2026-10-30**. WebFetch returns summaries from a helper model, so treat exact figures marked SEC as "as displayed on that page that day". Many OTA prices are shown in the viewer's currency, and they vary.

---

## 0. Pages blocked or unavailable (we moved on)

| URL | Result |
|---|---|
| https://www.alcazarsevilla.org/en/ | Site returned a client error, so the English homepage was not retrieved. The Spanish homepage worked. |
| https://app.museummate.net/museums/NzctUEFUUk9OQVRPIFJFQUwgQUxDQVpBUiBERSBTRVZJTExB/ (the official free audio guide itself) | Blocked: permission request not answered. **Its languages, stop list and coverage could NOT be verified.** |
| https://alcazardesevilla.infoticketing.com/es (official ticket shop) | Blocked: permission request not answered. Whether an audio guide add-on is sold there in 2026 is unverified. |
| https://apps.apple.com/es/app/artymax/id1457958938 | Blocked: permission request not answered. The US and TH store pages were read instead. |
| https://www.getyourguide.com/alcazar-of-seville-l4542/audio-guides-tc144/ and https://www.getyourguide.com/alcazar-of-seville-l4542/ | Site returned a client error. **No GetYourGuide data was read directly.** GYG-type bundles are covered through Tiqets, Tripadvisor, Musement and GuruWalk mirrors. |
| https://www.tripadvisor.com/Attraction_Review-...-or10-... (page 2 of Alcázar reviews) | Blocked: permission request not answered. |
| https://listen.hubhopper.com/podcast/rick-steves-spain-portugal-audio-tours/153431 | Blocked. Used ricksteves.com instead. |
| https://api.panchotours.com/audioguide-alcazar-seville | Live, but showed only "Página en mantenimiento". |

---

## 1. The official audio guide

### 1a. What the official site offers today: a free QR web audio guide

- The homepage shows "ACCESO AUDIOGUÍA – Directamente en tu móvil" but no link. Hours: Oct–Mar 09:30–17:00, Apr–Sep 09:30–19:00. [OFF] https://www.alcazarsevilla.org/ (read 2026-10-30)
- The "Prepara la visita" page says: "Escanea este código QR con tu móvil y podrás disfrutar ya de la Audioguía". It links to a **MuseumMate web app**: `app.museummate.net/museums/NzctUEFUUk9OQVRPIFJFQUwgQUxDQVpBUiBERSBTRVZJTExB/`. The base64 slug decodes to "77-PATRONATO REAL ALCAZAR DE SEVILLA". The page gives **no price, languages, provider or accessibility details**. [OFF] https://alcazarsevilla.org/prepara-la-visita/ (read 2026-10-30)
  - Price: the page states no price, but QR access is open to anyone with a phone, so it is **effectively free**. This is an inference. Tripadvisor reviewers in 2022 already described a free "QR / MuseumMate" guide. [SEC] https://www.tripadvisor.com/ShowTopic-g187443-i284-k13925357-How_to_get_audioguide_for_Alcazar-Seville_Province_of_Seville_Andalucia.html (read 2026-10-30; posts dated "4 years ago")
  - Format: web app in the phone browser, so it needs a connection. Not an installed app.
  - Languages, number of stops, length: **unknown, because the MuseumMate page was blocked.**
  - Gardens, Cuarto Real Alto, Casa de la Contratación coverage: **unknown, for the same reason.**
- Ticketing context [OFF] https://alcazarsevilla.org/prepara-la-visita/ (read 2026-10-30):
  - General entry is €15.50 and covers the ground floor of the palaces plus the gardens.
  - Cuarto Real Alto is €5.50.
  - Reduced entry is €8.00.
  - The site warns that "occasional closures of some spaces or gardens" give no discount or refund.
- Tariff confirmation [OFF] BOP Sevilla nº 247, 23 Dec 2024, https://alcazarsevilla.org/wp-content/uploads/2025/02/BOP-ORDENANZA-PATRONATO-2025.pdf (read 2026-10-30):
  - General €15.50, which "incluye la visita a la planta baja de los Palacios y Jardines".
  - Cuarto Real Alto €5.50, described as a "visita parcial organizada".
  - **The ordinance lists no audio guide tariff.**

**What visitors say about the official QR guide (Tripadvisor, all 2026)** [SEC] https://www.tripadvisor.com/Attraction_Review-g187443-d191139-Reviews-Real_Alcazar_de_Sevilla-Seville_Province_of_Seville_Andalucia.html (read 2026-10-30; attraction rated 4.7 from 36,960 reviews):
- "The audioguide (from QR codes on site) was complicated and limited." Sarah00056, 21 Oct 2026. She also says many English info signs were too faded to read.
- "The online audio guide connection was patchy at best (and doesn't match with numbers on the printed map)." JamesE2002, 12 Oct 2026. He adds that "notice/info boards were sun faded so as to be unreadable".
- "Don't count on the digital guide." Art P, 13 Jun 2026. He also wrote: "The system tells you to stand, turn, walk into, stop, and observe." Route-style instructions are hard to follow in crowds, and he thinks the guide should be part of the ticket.
- TheShirtSpeaks, Oct 2026: "signage issues that certainly could be improved".

### 1b. The official concession: "Official Audioguide" (UTE Viajes Alsa + Pancho Tours, Artymax app)

- **Who runs it.** The Patronato awarded the audio-guide, radio-guide and devices concession to a temporary union of companies (UTE): Viajes Alsa + Pancho Tours.
  - Pancho Tours: "The Real Alcazar granted us the concession of audio guide services, radio guides and other devices". It runs on the **Artymax** app (iOS/Android, "also available on the website") with "HD videos of the 30 rooms". [SEC] https://www.panchotours.com/information-about-real-alcazar-of-seville-audioguide (read 2026-10-30; article headed "22 DIC", year not shown)
  - EU Accessible portal: developer is "UTE Viajes Alsa + Pancho Tours" for the Patronato. Launched **2 April 2023**, with more than 14,000 users in its first two months. [SEC] https://accessible-eu-centre.ec.europa.eu/royal-alcazar-sevilla-inclusive-audioguide-app-spain_en (read 2026-10-30)
- **Languages.** Sources disagree:
  - "5 languages: Spanish, English, French, Italian, Chinese" [SEC] Pancho Tours page above.
  - 6 languages (ES, EN, FR, IT, DE, ZH) without ticket; German missing for the with-ticket version [SEC] https://tickets.realalcazarsevilla.com/en/official-audioguide-alcazar-of-seville (read 2026-10-30).
  - "10 spoken-language tracks" [SEC] EU portal.
  - The Artymax version note says "Implementación de cinco nuevos idiomas para la audioguía Real Alcázar de Sevilla" (no date shown). [SEC] https://apps.apple.com/th/app/artymax/id1457958938 (read 2026-10-30)
- **Stops and length.** 30 rooms, "every stop along the 30-room itinerary has synchronized AD and LSE video" [SEC] EU portal. Visit about 2 h with ticket, 2 h 30 for the Upper Room bundle [SEC] tickets.realalcazarsevilla.com.
- **Accessibility (the strongest feature in the market).** Audio description, Spanish Sign Language (LSE) video, 3-D reconstructions, adjustable font and contrast, tactile buttons, rentable adapted handsets. About 38% of users used their own phones. [SEC] EU portal.
- **Price.**
  - In-app purchase "Alcázar de Sevilla" is **US$7.99** on the US App Store and ฿299 on the TH store [SEC] https://apps.apple.com/us/app/artymax/id1457958938 and the TH page (read 2026-10-30). One reviewer says they paid €6.
  - In Nov 2023 OCU reported the official-site audioguide as an optional **€9.50** add-on [SEC] https://www.ocu.org/organizacion/prensa/notas-de-prensa/2023/alcazarsevilla201123 (read 2026-10-30; note dated 20 Nov 2023). The 2025 ordinance does not list it, and the 2026 official ticket shop was blocked, so **current on-site pricing is unverified.**
  - Bundles on tickets.realalcazarsevilla.com run by Feel The City: "From 39,90 €" (ticket + audioguide) and "From 50,90 €" (+ Upper Room). That site states: "This site is not the website of the Real Alcázar of Seville." [SEC] (read 2026-10-30)
  - Pancho Tours sells the same bundle at €39.90 adult, €25.50 child, €20.50 infant [SEC] https://www.panchotours.com/ticket-and-audioguide-alcazar-seville (read 2026-10-30).
- **Coverage.**
  - Gardens: not stated on the concession pages. Pancho's bundle page only mentions "Alcázar Gardens" in passing [SEC].
  - Cuarto Real Alto: sold as a separate "Upper Room" add-on with "access to the Royal High Quarters" [SEC] tickets.realalcazarsevilla.com. It is unclear whether audio content exists inside, because the Cuarto Real Alto is an "organised partial visit" [OFF BOP].
  - An affiliate site says "No audio guide access is available there". [SEC] https://alcazar-seville.co/tickets/audio-guide/ (read 2026-10-30; page updated 15 Oct 2026)
  - Casa de la Contratación: **not mentioned** on any concession page.
- **Recent reviews of the app.** Overwhelmingly negative, and the complaints are technical:
  - Audio does not play through Bluetooth or AirPods. Audio stops when the screen locks or when switching apps.
  - No rewind or fast-forward, so you must restart a section.
  - Needs fast 4G, but Wi-Fi exists only at the counter.
  - The map back-arrow can't be tapped on iPhone X and newer.
  - "Waste of money … lost €12."
  - Sources: [SEC] https://apps.apple.com/us/app/artymax/id1457958938 and https://apps.apple.com/th/app/artymax/id1457958938 (read 2026-10-30; reviews undated except one referencing 2023).
  - Rick Steves forum, 25 Aug 2023: "Avoid Alcazar app (Artymax)", hard to navigate, "you have to restart each section from the beginning". On 13 Jan 2024 the vendor's reply was paraphrased as "too bad. we have your money". [SEC] https://community.ricksteves.com/travel-forum/spain/sevilla-warning-avoid-alcazar-app-artymax (read 2026-10-30)
- **Legacy app.** "Royal Alcazar of Seville" (Soviews / Miguel Pérez Cabezas): $0.99, EN/ES, last updated **16 Dec 2016**, rated 1.2 from 9 ratings. A 30 Dec 2022 review says "Audio Doesn't Work". [SEC] https://apps.apple.com/us/app/id938105969 (read 2026-10-30)

> **Bottom line on "official":** in 2026 the Alcázar's own site points visitors to a **free MuseumMate QR web guide**, which reviewers call limited, patchy and mis-numbered. Separately, a **paid concession product** (Artymax, UTE Alsa–Pancho Tours) is marketed as "official". It has excellent accessibility on paper and poor app reviews. Neither source verifiably covers the Cuarto Real Alto or the Casa de la Contratación.

---

## 2. Third-party audio tours

| # | Product (operator) | Price | Languages | Length / stops | Last update | Evidence |
|---|---|---|---|---|---|---|
| A | **Rick Steves Audio Europe** | Free | EN | **No Alcázar tour exists.** Spain list is Barcelona City Walk, Eixample Walk, Madrid City Walk and **Sevilla City Walk** only | Not shown (© 2026) | [SEC] https://www.ricksteves.com/watch-read-listen/audio/audio-tours/spain-portugal-audio-tours (read 2026-10-30) |
| B | **izi.TRAVEL "Royal Alcázar of Seville"** (WendyCrawfordWrites.com) | Free | EN only | One narrated track naming about 11 spaces (Puerta del León … Cuarto del Admirante, Salones de Carlos V) | Not shown. **Content is stale:** it quotes admission as €9.50 when the real price is €15.50 | [SEC] https://izi.travel/en/7792-royal-alcazar-de-sevilla/en (read 2026-10-30) |
| C | **Clio Muse Tours** self-guided audio tour (sold via Musement, Magpie and others) | No-ticket version shown as "from AED 9.99" on Magpie. With ticket: **€28** | EN, ES, FR, DE, IT (+PT on Musement) | 2 h to 2 h 30. Stop count not given. Names Lion's Gate, Hall of Justice, House of Trade of Indies, Patio de las Muñecas, gardens. Offline text, audio and maps | Ticket listing updated **12 Aug 2025** | [SEC] https://magpie.travel/things-to-do/en/reseller-view/entrance-ticket-with-audio-tour-to-royal-alcazares-of-seville/4a3c9134-67dd-4524-8db6-142d713f2fda ; https://magpie.travel/things-to-do/royal-alcazares-of-seville-self-guided-audio-tour-no-ticket/78388286-e765-4acb-9732-353d7967be7c ; https://www.musement.com/us/seville/royal-alcazar-of-seville-self-guided-audio-tour-268418/ (all read 2026-10-30) |
| D | **Naturanda** ticket + downloadable audio app (Tripadvisor, Musement, TUI) | From £25 (Musement) | EN, IT, FR, ES, DE | 1 to 1.5 h. Covers Patio de las Doncellas, Baths of María de Padilla, **Admiral's Hall**, gardens. **Excludes Upper Royal Chamber** | Reviews up to Oct 2026 | [SEC] https://www.tripadvisor.com/AttractionProductReview-g187443-d33237495-or20-Royal_Alcazar_of_Seville_Entry_Ticket_with_Audio_Guide-Seville_Province_of_Se.html ; https://www.musement.com/uk/sevilla/entrada-al-alcazar-real-de-sevilla-con-audioguia-descargable-489241/ (read 2026-10-30) |
| E | **My Top Tour** "Fast Track Ticket + Audio Guide App" (Tiqets; own site mytoptour.org) | €29.99 on own site. Tiqets price not shown | EN, FR, DE, ES (Tiqets). Own site adds IT, PT | About 2 h. Stops not listed. Offline not stated | Reviews to Sep 2026 | [SEC] https://www.tiqets.com/en/seville-attractions-c65870/tickets-for-royal-alcazar-of-seville-fast-track-entry-audio-guide-app-p1116517/ ; https://www.mytoptour.org/en/all-reviews-tour/real-alcazar-audioguide (read 2026-10-30) |
| F | **Alhambra Valparaíso Ocio y Cultura** "Entry Ticket + Audio Guide" (Tiqets product, GuruWalk mirror) | From €28 | **7: DE, EN, ES, FR, IT, NL, ZH** | Not stated | Not shown | [SEC] https://www.guruwalk.com/walks/p40048-royal-alcazar-of-seville-entry-ticket-audio-guide-cGFub3B0ZXM (read 2026-10-30) |
| G | **TouringBee** "Audio Guide App: Seville Alcásar (No ticket)" | From €10 | EN, FR, ES, DE, IT | 1 h 30, 9 landmarks incl. Mercury pond, Patio del Yeso, Apeadero, Puerta de Marchena, gardens. **Also lists "Business School Chamber of Commerce of Seville"**, a red flag for auto-generated content. Offline GPS map | No reviews | [SEC] https://www.freetour.com/seville/audio-guide-app-seville-alcasar (read 2026-10-30) |

**Other products checked:**
- **Smartify:** no Alcázar tour found in search. [SNIP] search "smartify.org Seville Alcázar" (2026-10-30)
- **VoiceMap:** 7 Seville tours, none covers the Alcázar interior. [SEC] https://voicemap.me/tour/seville (read 2026-10-30)
- **Headout** audio guide: $13.41, rated **2.5 from 11**, needs a 100–150 MB download. [SEC] https://www.headout.com/seville-alcazar-tickets/audio-guide-to-the-royal-alcazares-of-seville-e-24059 (read 2026-10-30)
- **Clicatour** "9 languages": browser-based, 19 listening points, printable A4 map, no ticket. [SEC] https://clicatour.com/en/excursion/espagne/seville/seville-audioguide-real-alcazar-en-9-langues (read 2026-10-30)
- **WeGoTrip** Alcázar ticket + city walk (EN only, €28.14, 4.5 from 2,165): the page contradicts itself on whether the Alcázar interior is covered. [SEC] https://wegotrip.com/sevilla-2510911-d2510911/seville-walking-tour-with-royal-alczar-of-seville-ticket-p12546/ (read 2026-10-30)
- **Tiqets "Seville City Audio Guide"** + live-guided Alcázar tour: EN/ES, 100+ city POIs, offline, rated 3.8 from 4. [SEC] https://www.tiqets.com/en/alcazar-of-seville-tour-seville-city-audio-guide-b38443/ (read 2026-10-30)
- **Bingetours** reserved ticket + audio (EN only, 3.0 from 2, currently unavailable). [SEC] https://www.tripadvisor.com/AttractionProductReview-g187443-d33005763-Royal_Alcazar_Seville_Reserved_Entrance_Tickets_with_Audio_Guide-Seville_Province_.html (read 2026-10-30)

### Recent review praise and complaints (2024–2026)

| Product | Praise | Complaints | Source |
|---|---|---|---|
| Official QR (MuseumMate) | (none quoted) | "complicated and limited" (21 Oct 2026). Connection "patchy", "doesn't match with numbers on the printed map" (12 Oct 2026). "Don't count on the digital guide", and step instructions are hard to follow in crowds (13 Jun 2026) | [SEC] Tripadvisor attraction page (above) |
| Official concession (Artymax) | Accessibility suite (AD, LSE, 3-D) [SEC EU portal] | No Bluetooth. Stops on screen lock. No scrubbing. Needs 4G. Restarts sections. Poor value | [SEC] App Store US and TH; Rick Steves forum 2023–Jan 2024 |
| Naturanda (D) | "informative audio guide" (Jörg S, Oct 2026) | "the stations are not always entirely clear" (Oct 2026). Long in-person ticket pick-up, required "to download the audio guides" (Oct 2025). Booking not found (Oct 2026). Rated 3.8 from 71 | [SEC] Tripadvisor d33237495 |
| My Top Tour (E) | 4.6 from 188 on its own site | "signage and directions during the tour could be far better … difficult to follow in such a busy place" (22 Dec 2025). Rated **3.0 from 184 on Tiqets** | [SEC] mytoptour.org; Tiqets p1116517 |
| Alhambra Valparaíso (F) | 7 languages | Rated 3.40 from 141. Official tickets emailed ≥24 h later. Non-refundable | [SEC] GuruWalk p40048 |
| Headout | (none) | Rated 2.5 from 11 | [SEC] Headout e-24059 |

**Closed areas and restoration context:**
- The Mercury pond restoration page is framed as complete ("El Estanque de Mercurio recupera su esplendor"), page modified 20 Mar 2025. It gives no works dates. It also mentions a reopened "pasillo olvidado" corridor between the Patio de las Muñecas and the Jardín del Príncipe, **which no competitor mentions**. [OFF] https://alcazarsevilla.org/restauracion-estanque-mercurio/ (read 2026-10-30)
- Current homepage notices: temporary shop closure, Sala de la Justicia closed for a press conference, conservation works on the access doors between Plaza del Triunfo and Patio de Banderas. [OFF] homepage (read 2026-10-30)
- Storm precedent: after cyclone Bernard the gardens closed for more than a week and reopened 1 Nov 2023. The Jardín de la Danza and Jardín de los Poetas stayed roped off. [SEC] https://vivirediciones.es/?p=439883 (read 2026-10-30)
- Naturanda's conditions say parts of the palace may close in rain or strong wind. [SEC] Tripadvisor d33237495
- No 2024–2026 review found complaining specifically about the Mercury pond works inside a guide.

**Third-party price context:** OCU (20 Nov 2023) found "official-looking" sites bundling the audioguide to push ticket prices up to 2×. [SEC] OCU note (above)

---

## 3. Comparison table

Legend: ✔ = covered or stated · ✖ = stated not covered · ? = not stated or unverifiable · ~ = partial or passing mention.

| Feature | Official QR (MuseumMate) | Official concession (Artymax, UTE Alsa–Pancho) | izi.TRAVEL (B) | Clio Muse (C) | Naturanda (D) | My Top Tour / Tiqets (E) | Alhambra Valparaíso (F) | TouringBee (G) | **Yo Tours V5 (planned)** |
|---|---|---|---|---|---|---|---|---|---|
| Price | Free (inferred) [OFF] | $7.99 IAP. €39.90 bundle. €9.50 add-on in 2023 | Free | No-ticket from about €10 equiv.; €28 with ticket | From £25 with ticket | €29.99 with ticket | From €28 with ticket | €10 | to fill |
| Ticket included | ✖ | Bundles only | ✖ | Optional | ✔ | ✔ | ✔ | ✖ | to fill |
| Languages | ? (blocked) | 5 / 6 / 10 (sources conflict) | 1 (EN) | 5–6 | 5 | 4–6 | 7 | 5 | to fill |
| Stops / length | ? | 30 rooms, about 2 h | 1 track, about 11 spaces | 2–2.5 h | 1–1.5 h | about 2 h | ? | 9 POIs, 1.5 h | to fill |
| Format | Web app (online) | Native app + web | App/web | App, offline | App (download) | App | App | App, offline + GPS | to fill |
| Works offline | ✖ (patchy online, per reviews) | ✖ ("needs fast 4G", per reviews) | ? | ✔ | ? | ? | ? | ✔ | to fill |
| Bluetooth / background play | ? | ✖ (per reviews) | ? | ? | ? | ? | ? | ? | to fill |
| Gardens | ? | ~ | ~ (passing) | ~ | ✔ | ? | ~ | ✔ (incl. Mercury pond, Puerta de Marchena) | to fill |
| Cuarto Real Alto | ? | ~ (sold as add-on; audio inside unclear) | ✖ | ✖ ("No admission for the Royal Bedroom") | ✖ (excluded) | ? | ? | ✖ | to fill |
| Casa de la Contratación / Admiral's Hall | ? | ? | ✔ (Cuarto del Admirante) | ~ (House of Trade of Indies) | ✔ (Admiral's Hall) | ? | ? | ✖ | to fill |
| Stop numbers match on-site / printed map | ✖ (12 Oct 2026 review) | ? | ? | ? | ~ ("stations not always clear") | ✖ (signage complaint) | ? | ? | to fill |
| Accessibility (AD / sign language) | ? | ✔ AD + LSE + 3-D | ✖ | ✖ | ✖ | Wheelchair route only | ✖ | ✖ | to fill |
| Closure / live-status notes | ✖ | ✖ | ✖ | ✖ | Weather caveat only | ✖ | ✖ | ✖ | to fill |
| Content freshness | ? | Version dates not shown | ✖ (quotes €9.50 entry) | Listing updated Aug 2025 | ? | ? | ? | ✖ (odd POI) | to fill |
| Rating (latest seen) | n/a (complaints in 2026 reviews) | US App Store reviews all negative | none | 4.3 / 3 | 3.8 / 71 | 3.0 / 184 (Tiqets) | 3.40 / 141 | none | to fill |

---

## 4. What each one does well

- **Official QR guide:** free, zero install, signposted on the official site and on site. It is the default that every visitor can compare against. [OFF]
- **Official concession (Artymax):** the best accessibility in the market. Audio description, Spanish Sign Language video on every stop, 3-D reconstructions, font and contrast settings, rentable adapted devices. It also has the widest claimed spoken-language range (up to 10) and a full 30-room spine. [SEC EU portal]
- **izi.TRAVEL:** free, and it names the Cuarto del Admirante / Casa de Contratación link explicitly. [SEC]
- **Clio Muse:** genuine offline package (text, audio, maps), multiple languages, and a ticket option. It is honest that it excludes the Royal Bedroom and Upper Quarters. [SEC]
- **Naturanda:** names concrete highlights (Baths of María de Padilla, Admiral's Hall, gardens). Reviewers call the content "informative". [SEC]
- **Alhambra Valparaíso:** the broadest third-party language set (7, including Dutch and Mandarin). [SEC]
- **TouringBee:** cheap (€10). Offline with GPS map. Explicitly covers garden points (Mercury pond, Puerta de Marchena, Apeadero). [SEC]
- **Clicatour (also seen):** 9 languages, browser-only, printable A4 map. [SEC]

---

## 5. The bar to beat

### Must match (table stakes)

- [ ] **Free-tier parity.** The official QR guide is free, so a paid V5 must be visibly better (see the gaps below), or offer a free taster.
- [ ] **At least 7 languages at launch, with a roadmap to 10.** Alhambra Valparaíso has 7, Clicatour claims 9, the concession claims 10. Include ZH and NL.
- [ ] **Full spine of about 30 spaces plus gardens**, matching the concession's "30 rooms". Plan 2 h at the core, with 1 h and 3 h variants.
- [ ] **True offline**: one pre-download over Wi-Fi with audio, images and map. Clio Muse and TouringBee already do this. Visitors report palace Wi-Fi and 4G are unreliable.
- [ ] **Bluetooth / AirPods output, background and lock-screen playback, 10 s rewind and scrub, resume where left off.** These are the exact failures reported for Artymax.
- [ ] **Accessibility baseline**: transcripts for every track, adjustable text size and contrast, a step-free route. Aim for audio description; LSE is the concession's unique strength.
- [ ] **Named coverage** of Patio de las Doncellas, Embajadores, Muñecas, Baños de Doña María de Padilla, Cuarto del Almirante / Casa de la Contratación, Gothic Palace (Salones de Carlos V), Mercury pond, Puerta de Marchena and the main gardens.
- [ ] **No ticket hassle.** Competitors require passport forms, in-person pick-up at Alemanes 31, or tickets emailed up to 24 h later. Keep the guide usable with any official ticket.

### Must exceed (where everyone is weak)

- [ ] **Stop numbering that matches the physical site and our own map.** This was a 12 Oct 2026 complaint, and Naturanda and My Top Tour reviewers say the same. Use photo-anchored "you are here" cues, because the info boards are sun-faded.
- [ ] **Crowd-proof navigation.** Use landmark and photo cues, not "stand, turn, walk into". Offer "skip ahead / come back later" when a room is packed.
- [ ] **Live closures panel**, editable without an app release. Cover rooms closed for events (Sala de la Justicia), works (Triunfo–Banderas doors), storm or wind garden closures, and seasonal hours. Auto-reroute around them. **Nobody offers this.**
- [ ] **Cuarto Real Alto chapter.** No audio product verifiably covers it: it is an organised partial visit at €5.50, and one affiliate says there is no audio access there. Ship a "before / after your Upper Rooms visit" track plus an optional at-home listen.
- [ ] **Casa de la Contratación depth.** Only izi.TRAVEL and Naturanda name it. Make it a flagship story (the House of Trade, the Admiral's Hall and its altarpiece; these story points are from our own notes, not from this research, so verify before scripting), because it is under-served.
- [ ] **Newly reopened and lesser-known spaces**, for example the reopened corridor between Patio de las Muñecas and Jardín del Príncipe (official site), the Mercury pond after restoration, and the outer gardens. No competitor mentions them.
- [ ] **Verifiable freshness.** Show a "content checked on <date>" stamp and current prices. izi.TRAVEL still quotes €9.50.
- [ ] **Layered depth**: a 2–3 min core track per stop plus optional deep-dives. The affiliate benchmark is 3–5 min per stop across 20–25 stops.
- [ ] **QA hygiene**: no off-site or erroneous POIs (TouringBee lists a business school), no broken audio links (the 2016 Soviews app).

### Gaps none of them cover well (summary)

1. Live closure and reroute information.
2. On-site numbering that matches the map.
3. A Cuarto Real Alto audio companion.
4. Rich Casa de la Contratación content.
5. Reliable offline plus Bluetooth playback in one product.
6. Crowd-aware navigation.
7. Dated, visible content freshness.
8. Accessibility (AD / LSE) outside the official concession.

---

### Caveats
- The MuseumMate guide's own content (languages, stops) and the 2026 official ticket shop could not be read. Re-check both from a normal browser by hand before finalising V5 claims.
- No GetYourGuide data was read directly (site errors).
- Concession language counts conflict (5 / 6 / 10). Treat 10 as the ceiling claimed by the EU portal.
