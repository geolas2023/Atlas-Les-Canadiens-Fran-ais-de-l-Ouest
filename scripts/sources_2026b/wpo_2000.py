# We Proceeded On, vol. 26, no 1 (février 2000), revue de la Lewis and Clark Trail Heritage Foundation. PDF du Drive de
# l'auteur (HISTOIRE_LIVRES/JB_CHARBONNEAU), lu en entier le 19 novembre 2026. Corpus « Recherches », préfixe WP00.
# Articles de Bob Moore (baptême de Jean-Baptiste Charbonneau), Rita Cleary (Toussaint Charbonneau), Holmberg (Seaman).
from commun import Corpus
WP = "Moore, Bob (2000), « Pompey's Baptism », We Proceeded On, vol. 26, no 1, p. 10-15"
C = Corpus('Recherches', 'WP00', WP, page_fmt='p. {}')
F = C.F
F('01', "Saint-Louis : baptême de Jean-Baptiste Charbonneau, « Pomp », par le trappiste Urbain Guillet (28 décembre 1809)", 'religion', '1809-12-28', -90.1857, 38.6243, 'c', ['Jean-Baptiste Charbonneau', 'Toussaint Charbonneau', 'Sacagawea', 'Urbain Guillet', 'Auguste Chouteau', 'Eulalie Chouteau'],
  "Le 28 décembre 1809, dans la vieille église de pieux debout de Saint-Louis, le frère Urbain Guillet, du monastère trappiste de Notre-Dame de Bon-Secours près de Cahokia, baptise l'enfant de Toussaint Charbonneau « domicilié de cette paroisse » et d'une « sauvagesse de la nation des Serpents ». Le parrain est Auguste Chouteau, cofondateur de la ville, la marraine sa fille Eulalie, douze ans ; Charbonneau signe d'une croix. Bob Moore, qui a retrouvé l'acte en 1999, note que Saint-Louis n'avait plus de curé résident depuis 1804 et que Guillet n'y passe que du 24 au 31 décembre : la famille, sans doute descendue avec l'expédition de Pierre Chouteau revenue le 16 novembre après avoir ramené le chef Sheheke, a donc saisi la première occasion. L'acte date la naissance du 11 février 1804, un an trop tôt.",
  '10-13', "Point à l'emplacement de la vieille cathédrale, au pied de l'arche.")
fiches = C.fiches
