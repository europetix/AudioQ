import re, json
# Orangerie V5: starts EMPTY (Ava reads French names natively); add respellings only after listen-QA.
# Phonetic respellings applied at render time (both voices). V5: +47 names for the new running order. V5.1 (5 Oct): +69 names from the traveller review; listen-QA them.
# Set APPLY_RESPELLING = False in render_kokoro.py / render_edge.py to hear native pronunciation instead.
PRONUNCIATION = json.loads(r'''{}''')

def apply_respelling(text, enable=True):
    if not enable:
        return text
    for name in sorted(PRONUNCIATION, key=len, reverse=True):
        text = re.sub(r'\b' + re.escape(name) + r'\b', PRONUNCIATION[name], text)
    return text
