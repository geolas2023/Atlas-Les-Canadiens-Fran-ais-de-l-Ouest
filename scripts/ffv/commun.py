# Référence commune pour le livre French Fur Traders and Voyageurs in the American West
FF = "Hafen, LeRoy R. (dir.), French Fur Traders and Voyageurs in the American West, Spokane, Arthur H. Clark, 1995 (notices tirées de The Mountain Men and the Fur Trade of the Far West, 1965-1972)"
def ff(auteur, p, note=None):
    s = f"{auteur}, dans {FF}, p. {p}"
    if note: s += f" — note de l'auteur : {note}"
    return s
# lieux fréquents (lon, lat)
STL = (-90.199, 38.627); TAOS = (-105.573, 36.407); SANTAFE = (-105.938, 35.687)
BENT = (-103.430, 38.040); PUEBLO = (-104.6115, 38.2669); MORA = (-105.330, 35.974)
FTJACKSON = (-104.790, 40.180); FTSTVRAIN = (-104.856, 40.283); FTVASQUEZ = (-104.817, 40.193); FTLUPTON = (-104.805, 40.080)
LASVEGAS = (-105.223, 35.594); SANGERONIMO = (-105.373, 35.556); TECOLOTE = (-105.278, 35.457)
HARDSCRABBLE = (-105.083, 38.262); GREENHORN = (-104.860, 37.960); FORTLEDUC = (-105.101, 38.278)
