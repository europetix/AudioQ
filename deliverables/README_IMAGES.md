# Orangerie V5: images for the app (one per track)

`Orangerie_V5_Image_List.csv` (opens in Excel or Numbers): one row per track, with the work to show, its official museum page, copyright status, search links and a suggested file name (`orangerie_NNN.jpg`).

## Where to get each image
1. **Paintings by Monet, Renoir, Cézanne, Rousseau, Modigliani, Soutine, Matisse and Derain (43 tracks):** use the **Wikimedia Commons** link. Commons holds faithful scans of public-domain paintings ("PD-Art"); download the largest file and check its licence box says public domain. Compare it with the museum's official page (link) to make sure it is the same work and version.
2. **Picasso (tracks 040–044):** protected by copyright until the end of 2043. A commercial app needs a licence from Picasso Administration / ADAGP (ARS in the US), or show no image (a title card only).
3. **The building, the oval rooms and the garden (001, 002, 003, 008, 014, 054, 055):** Unsplash, Pexels and Pixabay photos are free for commercial use; Flickr only with the licence filter applied in the link (CC BY / CC0 / public domain, credit the photographer for CC BY). Or take your own photos on the test visit.
4. **Track 013 (Monet in old age):** a historic photograph. Check the photographer and licence on Commons before use.

## Do not
- Copy images from musee-orangerie.fr for the app. They are © RMN-Grand Palais photographs; the museum shows them, it does not license them for reuse. Use the page to identify the work, then source the image as above, or license an HD file from RMN-GP (photo.rmn.fr).
- Use a stock photo of a painting taken in the gallery (tilted, glare, cropped frame) when a clean scan exists.

Not legal advice. The copyright statuses follow the 70-years-after-death rule in France and the EU.

## Download them automatically (on your Mac)
```bash
cd ~/Downloads && unzip -o Orangerie_App_Images_Kit.zip && cd Orangerie_App_Images_Kit
python3 download_images.py
open images/index.html
```
- Fetches the 42 public-domain paintings from Wikimedia Commons (only files licensed as public domain) into `images/orangerie_NNN.jpg`, with `images/credits.csv`.
- Optional, for the 7 building / room / garden shots: get a free key at pexels.com/api, then `export PEXELS_API_KEY=your_key` before running. The key stays in your environment and is never saved.
- Skipped on purpose: Picasso 040–044 (licence needed) and 013 (hand-pick a historic photo).
- Check every picture on the contact sheet against its official page before using it. Search can return a similar but different work.
