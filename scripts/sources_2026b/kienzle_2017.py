# Valerie Battle Kienzle, Lost St. Louis (Charleston, The History Press, 2017), epub du Drive de l'auteur.
# Corpus « Recherches », préfixe LS17.
from commun import Corpus
KZ = "Kienzle, Valerie Battle (2017), Lost St. Louis, Charleston, The History Press"
C = Corpus('Recherches', 'LS17', KZ, page_fmt='{}')
F = C.F
F('01', "Saint-Louis : l'étang Chouteau, du moulin à l'égout, comblé après le choléra (vers 1766-1853)", 'etablissement', '1766~/1853', -90.2075, 38.6265, 'c', ['Auguste Chouteau', 'Joseph Nash McDowell'],
  "Au sud de la rue Market, près de l'actuelle Union Station, un barrage et un moulin des premiers habitants avaient formé un lac d'une centaine d'acres, l'étang Chouteau (Chouteau's Pond), lieu de promenade bordé de belles maisons. La croissance de la ville en fit un cloaque d'eaux usées ; après l'épidémie de choléra de 1849, qui tua plus de 4 300 Saint-Louisiens, et le grand incendie de la même année, on décida au début des années 1850 de le drainer et de le combler. Le médecin Joseph McDowell avait milité en ce sens.",
  "« Introduction » et « Medical Science »", "Position approximative du centre de l'ancien étang, entre Market Street et la vallée du Mill Creek.")
F('02', "Saint-Louis : la grande maison d'Henri Chouteau, remplacée par le palais de justice des Four Courts (1871)", 'famille', '1840~/1871', -90.2005, 38.6262, 'a', ['Henri Chouteau'],
  "Le complexe judiciaire des Four Courts, bâti en 1871 entre Clark Avenue, Spruce et les 11e et 12e rues, occupait l'emplacement de la vaste demeure du riche homme d'affaires Henri Chouteau, près de l'ancien étang Chouteau.",
  "« Four Courts Building »", "Date de construction de la maison non précisée.")
fiches = C.fiches
