#!/usr/bin/env python3
"""Assemble translated tracks (ES / FR / DE) into perf files, with automatic checks against the English.
Input: a work folder with <lang>/NNN.json = {"title", "where", "body"} (from the translation brief, 5 Oct 2026).
Output: v5/i18n/<lang>/tracks/NNN.perf.txt — the English header with @title/@where translated, plus @lang.
Checks per track (any failure stops the run): delivery tags same order as the English, no fewer pauses, same
paragraph count, not longer than the English, every digit year of the English present, no ; or ( in speech.
Usage: python3 v5/i18n/assemble.py <workdir> [lang ...]"""
import json, os, re, sys, glob
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "v5", "pipeline")); import v5_direction as V
EN = os.path.join(ROOT, "v5", "tracks"); OUT = os.path.join(ROOT, "v5", "i18n")
dt = lambda b: [t for t in re.findall(r"\[([^\]]+)\]", b) if "pause" not in t]
pz = lambda b: len(re.findall(r"\[(?:long )?pause\]", b))
years = lambda s: set(re.findall(r"\b1[0-9]{3}\b", s))

def check(n, body, en_body):
    c, ce = V.clean(body), V.clean(en_body); e = []
    if dt(body) != dt(en_body): e.append("delivery tags differ")
    if pz(body) < pz(en_body): e.append("fewer pauses")
    if body.strip().count("\n\n") != en_body.strip().count("\n\n"): e.append("paragraph count")
    if len(c.split()) > len(ce.split()): e.append(f"too long {len(c.split())}>{len(ce.split())}")
    if years(ce) - years(c): e.append(f"missing years {sorted(years(ce) - years(c))}")
    if ";" in c or "(" in c: e.append("semicolon/parenthesis")
    return e

def main():
    work, langs = sys.argv[1], sys.argv[2:] or ["es", "fr", "de"]
    bad = 0
    for lang in langs:
        os.makedirs(os.path.join(OUT, lang, "tracks"), exist_ok=True)
        for f in sorted(glob.glob(os.path.join(work, lang, "*.json"))):
            n = os.path.basename(f)[:3]; d = json.load(open(f, encoding="utf-8"))
            en = open(os.path.join(EN, f"{n}.perf.txt"), encoding="utf-8").read()
            head, _, en_body = en.partition("\n---\n"); body = d["body"].strip()
            errs = check(n, body, en_body)
            if errs: print(lang, n, "FAIL", errs); bad += 1; continue
            head = re.sub(r"^@title: .*$", lambda m: "@title: " + d["title"].strip(), head, flags=re.M)
            head = re.sub(r"^@where: .*$", lambda m: "@where: " + d["where"].strip(), head, flags=re.M)
            head = re.sub(r"^@id: (\d+)", rf"@id: \1 · {lang.upper()}", head, flags=re.M)
            head += (f"\n@lang: {lang}\n@translation: from the fact-checked English Orangerie V5 {n} (5 Oct 2026); facts unchanged;"
                     " formal address; adapted for listening (short sentences, extra pauses)")
            p = os.path.join(OUT, lang, "tracks", f"{n}.perf.txt")
            open(p, "w", encoding="utf-8").write(head + "\n---\n" + body + "\n"); V.validate(p)
        have = sorted(os.path.basename(x)[:3] for x in glob.glob(os.path.join(OUT, lang, "tracks", "*.perf.txt")))
        missing = [f"{i:03d}" for i in range(1, 56) if f"{i:03d}" not in have]
        print(f"{lang}: {len(have)} tracks" + (f", missing {missing}" if missing else ", complete"))
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
