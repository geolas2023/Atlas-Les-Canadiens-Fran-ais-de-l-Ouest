# Herbert E. Bolton, « New Light on Manuel Lisa and the Spanish Fur Trade », The Quarterly of the Texas State Historical
# Association (Southwestern Historical Quarterly), vol. 17, n° 1, 1913, p. 61-66 (PDF du Drive de l'auteur, dossier MANUEL_LISA). Préfixe BO13.
from commun import Corpus
BO = "Bolton, Herbert E. (1913), « New Light on Manuel Lisa and the Spanish Fur Trade », The Quarterly of the Texas State Historical Association, vol. 17, n° 1"
C = Corpus('Recherches', 'BO13', BO, page_fmt='p. {}')
F = C.F
F('01', "Fort Manuel : Lisa écrit « aux Espagnols du Nouveau-Mexique » (8 septembre 1812)", 'commerce', '1812-09-08', -100.66, 45.935, 'c', ['Manuel Lisa', 'Jean-Baptiste Champlain', 'Jean-Baptiste Lafargue', 'Charles Sanguinet'],
  "Retrouvée dans les archives de Chihuahua, une lettre écrite par Lisa au fort Manuel le 8 septembre 1812 révèle que vingt-trois de ses chasseurs fréquentaient la nation arapaho, que les Espagnols du Nouveau-Mexique venaient chaque année commercer avec elle, et qu'il avait confié des marchandises à Jean-Baptiste Champlain et Jean-Baptiste Lafargue pour traiter avec eux. Sans nouvelles, il envoie son homme de confiance Charles Sanguinet, avec deux engagés, porter la lettre où il propose, comme directeur de la Missouri Fur Company, de fournir chaque année toutes les marchandises qu'on lui commandera.",
  '61-64', "Point au fort Manuel (Dakota du Sud). Champlain serait le Baptiste Champlain de l'établissement de la Cuivre (Houck).")
F('02', "La Petite Corne : Lisa fait fonder un poste pour ses chasseurs (1812)", 'poste', '1812-09~', -107.62, 45.74, 'h', ['Manuel Lisa', 'Charles Sanguinet'],
  "Dans la même lettre, Lisa annonce qu'il envoie dix hommes, avec Sanguinet, à la « Petite Corne », affluent de la Roche Jaune (Yellowstone) à deux cent vingt-cinq lieues du fort Manuel, pour y établir un poste plus proche de ses chasseurs. Bolton y voit une tentative de poste à l'embouchure du Little Bighorn.",
  '62, 64', "Identification de Bolton ; la « Petite Corne » pourrait aussi désigner le Bighorn. Point au confluent du Little Bighorn et du Bighorn (Hardin, Montana).")
fiches = C.fiches
