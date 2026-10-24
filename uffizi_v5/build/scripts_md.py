#!/usr/bin/env python3
"""Readable script book: python3 scripts_md.py <en|es|fr|de> <out.md>"""
import sys, os, glob, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT + '/v5/pipeline'); import v5_direction as V
lang, out = sys.argv[1], sys.argv[2]
src = ROOT + ('/v5/tracks' if lang == 'en' else f'/v5/i18n/{lang}/tracks')
L = [f"# Yo Tours · Uffizi Gallery · audio guide scripts ({lang.upper()}) · 24 Oct 2026 edition", ""]
sec = None
for f in sorted(glob.glob(src + '/*.perf.txt')):
    m, c = V.validate(f); n = os.path.basename(f)[:3]
    if m['section'] != sec:
        sec = m['section']; L += [f"## {sec}", ""]
    room = m['room']   # audit S25 (24 Oct 2026): the Botticelli codes A9-A12 are uncertain (map vs pages, O7): never printed
    if re.match(r"^(Room|Sala|Salle|Saal) A(9|1[0-2])$", room):
        room = {"es": "Salas de Botticelli", "fr": "Salles Botticelli", "de": "Botticelli-Säle", "it": "Sale di Botticelli"}.get(lang, "Botticelli rooms")
    L += [f"### {n} · {m['title']}", f"*{room} · {len(c.split())} words*", "", f"**Where:** {m.get('where','')}", "", f"**What:** {m.get('what','')}", "", c, ""]
open(out, 'w', encoding='utf-8').write("\n".join(L))
print(out, len(L))
