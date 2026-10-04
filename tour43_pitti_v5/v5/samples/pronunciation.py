import re, json
PRONUNCIATION = json.loads(r'''{"Pietro da Cortona": "Pee-ay-tro da Kor-toh-na", "Cristofano Allori": "Krees-toh-fah-no Al-loh-ree", "Andrea del Sarto": "An-dray-a del Sar-toh", "Fra Bartolomeo": "Fra Bar-toh-loh-may-oh", "Filippo Lippi": "Fee-leep-po Lip-pee", "Giambologna": "Jam-bo-loh-nya", "Macchiaioli": "Mah-kya-yoh-lee", "Volterrano": "Vol-teh-rah-no", "Ammannati": "Am-mah-nah-tee", "Giorgione": "Jor-joh-nay", "Gabbiani": "Gab-bee-ah-nee", "Pontormo": "Pon-tor-mo", "Cristofano": "Krees-toh-fah-no", "Ghirlandaio": "Gheer-lan-dye-oh", "Gentileschi": "Jen-tee-less-kee", "Buontalenti": "Bwon-ta-len-tee", "Caravaggio": "Kah-rah-vah-jo", "Masaccio": "Mah-zah-cho", "Vasari": "Vah-zah-ree", "Cortona": "Kor-toh-na", "Fattori": "Fat-toh-ree", "Cosimo": "Kaw-zee-mo", "Medici": "Med-ee-chee", "Boboli": "Boh-boh-lee", "Giotto": "Jot-toh", "Allori": "Al-loh-ree", "Lippi": "Lip-pee", "Tacca": "Tahk-ka"}''')

def apply_respelling(text, enable=True):
    if not enable:
        return text
    for name in sorted(PRONUNCIATION, key=len, reverse=True):
        text = re.sub(r'\b' + re.escape(name) + r'\b', PRONUNCIATION[name], text)
    return text
