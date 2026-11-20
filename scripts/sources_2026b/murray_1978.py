# Robert A. Murray, Las Animas, Huerfano and Custer: Three Colorado Counties on a Cultural Frontier. A History of the Raton Basin,
# Denver, Bureau of Land Management (Cultural Resources Series, 6), 1978. PDF du Drive de l'auteur (HISTOIRE_LIVRES/CHARLES_AUTOBEES),
# lu en entier le 19 novembre 2026. Synthèse sans recherche originale : Fort LeDuc, Kinkead, Milk Fort, Autobees Plaza, familles
# Garnier, Mercier et Albert de la Wet Mountain sont déjà dans l'atlas. Une seule information nouvelle. Préfixe MU78.
from commun import Corpus
S = "Murray, Robert A. (1978), Las Animas, Huerfano and Custer: Three Colorado Counties on a Cultural Frontier. A History of the Raton Basin, Denver, Bureau of Land Management, Cultural Resources Series no 6"
C = Corpus('Recherches', 'MU78', S, page_fmt='p. {}')
F = C.F
F('01', "Autobees Plaza : premier chef-lieu du comté de Huerfano, transféré à Badito (1861-1866)", 'lieu', '1861/1866', -104.372, 38.207, 'a', ['Charles Autobees'],
  "Fondée en 1853 à l'embouchure de la Huerfano par Charles Autobees et quelques vieux montagnards, Autobees Plaza fut le premier siège du comté de Huerfano. En 1866, quand la législature du Colorado retrancha la plus grande partie du comté primitif pour former des parties des comtés de Las Animas, de Fremont et de Bent, le chef-lieu fut déplacé à Badito, village né autour d'un gué très fréquenté par les troupeaux.",
  '45, 49', "Murray s'appuie sur une lettre au Colorado Chieftain du 13 mai 1874. Point légèrement décalé de la fiche C010 (plaza).")
fiches = C.fiches
