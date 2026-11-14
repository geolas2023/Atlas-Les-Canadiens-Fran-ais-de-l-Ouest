# Outils communs aux dépouillements de novembre 2026 (deuxième lot).
# Chaque fiche : F(id, nom, theme, date_edtf, lon, lat, certitude, personnages, description, page, note='')
# certitude : 'c' certaine, 'a' approximative, 'h' hypothétique (de la localisation)
import re
CERT = {'c': 'certaine', 'a': 'approximative', 'h': 'hypothetique'}

def bornes(edtf):
    """Années décimales (début, fin) et précision à partir d'une date EDTF simple."""
    s = edtf.strip()
    parts = s.split('/') if '/' in s else [s, s]
    def un(x, fin=False):
        x = x.strip()
        m = re.match(r'^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?([~?%]*)$', x)
        if not m: raise ValueError(edtf)
        a = int(m.group(1)); mo = m.group(2); j = m.group(3)
        if mo:
            v = a + (int(mo) - 1) / 12 + ((int(j) - 1) / 365 if j else 0)
            return round(v, 3)
        return float(a) + (0.999 if fin else 0.0)
    d, f = un(parts[0]), un(parts[1], fin=True)
    p0 = parts[0]
    prec = 'circa' if ('~' in s or '?' in s) else ('jour' if re.match(r'^\d{4}-\d{2}-\d{2}$', p0) else ('mois' if re.match(r'^\d{4}-\d{2}$', p0) else 'annee'))
    return round(d, 3), round(min(f, float(int(f)) + 0.999), 3), prec

class Corpus:
    def __init__(self, nom, prefixe, source, page_fmt='p. {}'):
        self.nom, self.prefixe, self.source, self.page_fmt = nom, prefixe, source, page_fmt
        self.fiches = []
    def F(self, id, nom, theme, date, lon, lat, cert, pers, desc, page='', note='', source=None):
        d, f, prec = bornes(date)
        src = source or self.source
        if page: src = f"{src}, {self.page_fmt.format(page) if str(page)[0].isdigit() else page}"
        self.fiches.append({"type": "Feature", "geometry": {"type": "Point", "coordinates": [round(lon, 4), round(lat, 4)]},
            "properties": {"id": f"{self.prefixe}-{id}", "nom": nom, "corpus": self.nom, "theme": theme,
                "debut": d, "fin": f, "date_edtf": date, "precision": prec, "certitude": CERT[cert],
                "personnages": pers, "description": desc, "sources": src + '.', "note": note}})
