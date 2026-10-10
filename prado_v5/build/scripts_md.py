#!/usr/bin/env python3
"""Readable script book: python3 scripts_md.py <en|es|fr|de> <out.md>"""
import sys, os, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT + '/v5/pipeline'); import v5_direction as V
lang, out = sys.argv[1], sys.argv[2]
src = ROOT + ('/v5/tracks' if lang == 'en' else f'/v5/i18n/{lang}/tracks')
L = [f"# Yo Tours · Museo del Prado · audio guide scripts ({lang.upper()}) · 10 Oct 2026 edition", ""]
sec = None
for f in sorted(glob.glob(src + '/*.perf.txt')):
    m, c = V.validate(f); n = os.path.basename(f)[:3]
    if m['section'] != sec:
        sec = m['section']; L += [f"## {sec}", ""]
    L += [f"### {n} · {m['title']}", f"*{m['room']} · {len(c.split())} words*", "", f"**Where:** {m.get('where','')}", "", f"**What:** {m.get('what','')}", "", c, ""]
open(out, 'w', encoding='utf-8').write("\n".join(L))
print(out, len(L))
