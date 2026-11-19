# John F. Swenson, « Chicagoua/Chicago: The Origin, Meaning, and Etymology of a Place Name », Illinois Historical
# Journal, vol. 84, n° 4 (hiver 1991), p. 235-248. PDF JSTOR du Drive de l'auteur. Corpus « Recherches », préfixe SW91.
from commun import Corpus
SW = "Swenson, John F. (1991), « Chicagoua/Chicago: The Origin, Meaning, and Etymology of a Place Name », Illinois Historical Journal, vol. 84, n° 4, p. 235-248"
C = Corpus('Recherches', 'SW91', SW, page_fmt='p. {}')
F = C.F
F('01', "Chicagou : Joutel et l'ail sauvage qui a donné son nom au lieu (25 septembre 1687)", 'toponymie', '1687-09-25', -87.8075, 41.8125, 'a', ['Henri Joutel', 'abbé Jean Cavelier', 'Anastase Douay', 'François de Boisrondel'],
  "Parti du fort Saint-Louis du Rocher le 18 septembre 1687 avec les survivants de l'expédition de La Salle (l'abbé Cavelier et son neveu, le père Douay, le pilote Tessier) et le garde-magasin Boisrondel, Joutel arrive le jeudi 25 au lieu « appelé Chicagou », qui tient son nom, d'après ce qu'il apprend, de la quantité d'ail qui pousse dans les bois. Swenson tient ce passage pour la seule véritable enquête de terrain sur l'origine du nom : en langue illinoise, chicagoua désigne l'ail sauvage (Allium tricoccum, l'ail des bois), et non l'oignon sauvage ni une « mauvaise odeur », comme on le répète depuis deux siècles.",
  '235-238', "Point au portage de Chicago ; Joutel ne précise pas l'endroit exact de son campement.")
fiches = C.fiches
