#!/usr/bin/env python3
"""Assemble translated tracks (ES / FR / DE) into perf files, with automatic checks against the English.
Orsay version (7 Oct 2026), adapted for Pitti, then for the Prado (81 tracks: 59 main + 22 Extras, 10 Oct 2026). One addition: the Orsay English often
writes years in words ("eighteen sixty-five", "nineteen hundred and six"), so the year check also reads worded years and
requires each one as digits in the translation.
Input: a work folder with <lang>/NNN.json = {"title", "where", "body"} (from the translation brief).
Output: v5/i18n/<lang>/tracks/NNN.perf.txt — the English header with @title/@where translated, plus @lang.
Checks per track (any failure stops the run): delivery tags same order as the English, no fewer pauses, same
paragraph count, not longer than the English, every year of the English present as digits, no ; or ( in speech.
Usage: python3 v5/i18n/assemble.py <workdir> [lang ...]      Check only: python3 v5/i18n/assemble.py --check <workdir> <lang>"""
import json, os, re, sys, glob
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "v5", "pipeline")); import v5_direction as V
EN = os.path.join(ROOT, "v5", "tracks"); OUT = os.path.join(ROOT, "v5", "i18n"); N_TRACKS = 81
dt = lambda b: [t for t in re.findall(r"\[([^\]]+)\]", b) if "pause" not in t]
pz = lambda b: len(re.findall(r"\[(?:long )?pause\]", b))

_U = dict(one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9)
_T = dict(ten=10, eleven=11, twelve=12, thirteen=13, fourteen=14, fifteen=15, sixteen=16, seventeen=17, eighteen=18, nineteen=19)
_D = dict(twenty=20, thirty=30, forty=40, fifty=50, sixty=60, seventy=70, eighty=80, ninety=90)
_C = dict(sixteen=16, seventeen=17, eighteen=18, nineteen=19)
_u, _t, _d = "|".join(_U), "|".join(_T), "|".join(_D)
_TWO = rf"(?:(?:{_d})(?:-(?:{_u}))?|{_t})"                      # 10-99 in words
_YEAR = re.compile(rf"\b(?:(sixteen|seventeen|eighteen|nineteen)(?:[ -]hundred(?: and ({_TWO}|{_u}))?|[ -]oh[ -]({_u})|"
                   rf" ({_TWO}))|twenty ({_TWO}))\b(?![-\w])", re.I)

def _two(s):
    s = s.lower()
    if s in _U: return _U[s]
    if s in _T: return _T[s]
    a, _, b = s.partition("-"); return _D[a] + (_U[b] if b else 0)

def worded_years(text):
    out = set()
    for m in _YEAR.finditer(text):
        c, after_hundred, oh, two, twenty = m.groups()
        if twenty: out.add(str(2000 + _two(twenty))); continue
        base = _C[c.lower()] * 100
        out.add(str(base + (_two(after_hundred) if after_hundred else _U[oh.lower()] if oh else _two(two) if two else 0)))
    return out

digit_years = lambda s: set(re.findall(r"\b(?:1[0-9]{3}|20[0-9]{2})\b", s))
en_years = lambda s: digit_years(s) | worded_years(s)

def check(n, body, en_body):
    c, ce = V.clean(body), V.clean(en_body); e = []
    if dt(body) != dt(en_body): e.append("delivery tags differ")
    if pz(body) < pz(en_body): e.append("fewer pauses")
    if body.strip().count("\n\n") != en_body.strip().count("\n\n"): e.append("paragraph count")
    if len(c.split()) > len(ce.split()): e.append(f"too long {len(c.split())}>{len(ce.split())}")
    if en_years(ce) - digit_years(c): e.append(f"missing years as digits {sorted(en_years(ce) - digit_years(c))}")
    if ";" in c or "(" in c: e.append("semicolon/parenthesis")
    if re.findall(r"\[[^\]]*\]", V.TAG_RE.sub("", body)): e.append("unknown tag")
    return e

def en_body(n):
    return open(os.path.join(EN, f"{n}.perf.txt"), encoding="utf-8").read().partition("\n---\n")[2]

def check_dir(work, lang):
    bad = 0
    for f in sorted(glob.glob(os.path.join(work, lang, "*.json"))):
        n = os.path.basename(f)[:3]; d = json.load(open(f, encoding="utf-8"))
        errs = check(n, d["body"].strip(), en_body(n))
        if not d.get("title", "").strip() or not d.get("where", "").strip(): errs.append("empty title/where")
        wc, we = len(V.clean(d["body"]).split()), len(V.clean(en_body(n)).split())
        print(lang, n, f"{wc}/{we}w", "OK" if not errs else errs); bad += bool(errs)
    return bad

def main():
    if sys.argv[1] == "--check":
        sys.exit(1 if check_dir(sys.argv[2], sys.argv[3]) else 0)
    work, langs = sys.argv[1], sys.argv[2:] or ["es", "fr", "de"]
    bad = 0
    for lang in langs:
        os.makedirs(os.path.join(OUT, lang, "tracks"), exist_ok=True)
        for f in sorted(glob.glob(os.path.join(work, lang, "*.json"))):
            n = os.path.basename(f)[:3]; d = json.load(open(f, encoding="utf-8"))
            en = open(os.path.join(EN, f"{n}.perf.txt"), encoding="utf-8").read()
            head, _, eb = en.partition("\n---\n"); body = d["body"].strip()
            errs = check(n, body, eb)
            if errs: print(lang, n, "FAIL", errs); bad += 1; continue
            head = re.sub(r"^@title: .*$", lambda m: "@title: " + d["title"].strip(), head, flags=re.M)
            head = re.sub(r"^@where: .*$", lambda m: "@where: " + d["where"].strip(), head, flags=re.M)
            head = re.sub(r"^@id: (\d+)", rf"@id: \1 · {lang.upper()}", head, flags=re.M)
            head += (f"\n@lang: {lang}\n@translation: from the fact-checked English Prado {n} (10 Oct 2026 edition); facts unchanged;"
                     " formal address; adapted for listening (short sentences, extra pauses)")
            p = os.path.join(OUT, lang, "tracks", f"{n}.perf.txt")
            open(p, "w", encoding="utf-8").write(head + "\n---\n" + body + "\n"); V.validate(p)
        have = sorted(os.path.basename(x)[:3] for x in glob.glob(os.path.join(OUT, lang, "tracks", "*.perf.txt")))
        missing = [f"{i:03d}" for i in range(1, N_TRACKS + 1) if f"{i:03d}" not in have]
        print(f"{lang}: {len(have)} tracks" + (f", missing {missing}" if missing else ", complete"))
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
