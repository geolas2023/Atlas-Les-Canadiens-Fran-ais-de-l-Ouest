# Charles E. Hanson Jr et Veronica Sue Walters, « The Early Fur Trade in Northwestern Nebraska », Nebraska History,
# vol. 57 (1976), p. 291-314. PDF du Drive de l'auteur. Corpus « Recherches », préfixe HW76.
from commun import Corpus
HW = "Hanson, Charles E. Jr et Veronica Sue Walters (1976), « The Early Fur Trade in Northwestern Nebraska », Nebraska History, vol. 57, p. 291-314"
C = Corpus('Recherches', 'HW76', HW, page_fmt='p. {}')
F = C.F
F('01', "Bordeaux Creek (Nebraska) : la « fourche de Frédéric », entre James Bordeaux et Frederick Laboue", 'toponymie', '1841~/1871~', -102.940, 42.826, 'a', ['James Bordeaux', 'Frederick Laboue', 'P. D. Papin'],
  "Second de P. D. Papin au fort John (Laramie) au milieu des années 1840, James Bordeaux devient le principal traiteur de la haute rivière Blanche, où il hiverne dès 1841 et tient pour l'American Fur Company des maisons de traite auprès des Brûlés ; le ruisseau où il trafique pendant une trentaine d'années porte aujourd'hui son nom. Les auteurs relèvent pourtant que les cartes de Bordeaux et Campbell (1857) puis de Bridger l'appellent « Frederick's Fork », et celle du lieutenant Warren (1855-1857) « F. Laboue River ». Frederick Laboue, vieil employé de l'American Fur Company, associé de l'Upper Missouri Outfit en 1848, trafiquait dès 1830 avec les Sioux et les Poncas à la tête du Niobrara ; Parkman le croise en 1846 descendant la Platte avec onze bateaux de robes.",
  '300-304', "Le rôle exact de Laboue sur la rivière Blanche reste, selon les auteurs, une énigme. Point au poste de Bordeaux, à l'est de Chadron.")
fiches = C.fiches
