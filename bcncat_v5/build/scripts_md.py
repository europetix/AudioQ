#!/usr/bin/env python3
"""Readable script book: python3 scripts_md.py <en|es|fr|de> <out.md>"""
import sys, os, glob, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT + '/v5/pipeline'); import v5_direction as V
lang, out = sys.argv[1], sys.argv[2]
src = ROOT + ('/v5/tracks' if lang == 'en' else f'/v5/i18n/{lang}/tracks')
L = [f"# Yo Tours · Barcelona Cathedral · audio guide scripts ({lang.upper()}) · 14 Nov 2026 edition", ""]


def tidy(s):
    """Writers' markers are never printed: [O5], [O-map, O2], ALT-K, and sentences that are notes for the on-site check."""
    s = re.sub(r"\s*\[[^\]]*\]", "", s)
    s = re.sub(r"\bALT-[A-Z0-9]+\b:?\s*", "", s)
    s = re.sub(r";\s*\)", ")", s).replace("()", "").replace("( ", "(")
    keep = [x for x in re.split(r"(?<=[.!?])\s+", s) if not re.search(r"\bO\d+\b|\bO-map\b|on-site check", x)]
    return re.sub(r"\s{2,}", " ", " ".join(keep)).strip()


sec = None
for f in sorted(glob.glob(src + '/*.perf.txt')):
    m, c = V.validate(f); n = os.path.basename(f)[:3]
    if m['section'] != sec:
        sec = m['section']; L += [f"## {sec}", ""]
    room = tidy(m['room'])
    L += [f"### {n} · {m['title']}", f"*{room} · {len(c.split())} words*", "", f"**Where:** {tidy(m.get('where', ''))}", "",
          f"**What:** {m.get('what', '')}", "", c, ""]
open(out, 'w', encoding='utf-8').write("\n".join(L))
print(out, len(L))
