# Edward R. Kantowicz, « A Fragment of French Canada on the Illinois Prairies », Journal of the Illinois State
# Historical Society, vol. 75, n° 4 (hiver 1982), p. 263-276, PDF JSTOR du Drive de l'auteur. Corpus « Recherches », préfixe KZ82.
from commun import Corpus
KZ = "Kantowicz, Edward R. (1982), « A Fragment of French Canada on the Illinois Prairies », Journal of the Illinois State Historical Society, vol. 75, n° 4, p. 263-276"
C = Corpus('Recherches', 'KZ82', KZ, page_fmt='p. {}')
F = C.F
F('01', "Bourbonnais : le collège Saint-Viateur, pépinière du clergé de Chicago (1868-1938)", 'religion', '1868/1938', -87.8775, 41.1485, 'a', ['Ambrose Granger', 'Z. P. Bérard', 'Achille L. Bergeron'],
  "Fondé en 1868 par les Clercs de Saint-Viateur venus du Québec, le collège reproduit le modèle du collège classique québécois ; Kantowicz le présente comme le premier du genre hors du Canada. Faute de séminaire à Chicago avant 1920, il forme une part notable du clergé de l'archidiocèse : en 1916, trente-deux prêtres du diocèse y avaient étudié, dont des Irlandais devenus évêques auxiliaires. Les curés Ambrose Granger (Saint-Rose de Kankakee) et Z. P. Bérard (Sainte-Anne, quarante-quatre ans de cure), nés dans les années 1860, en sont issus. Les Viateurs ferment le collège en 1938 ; les bâtiments passent à l'Église du Nazaréen (Olivet).",
  '269-274', "L'auteur compte aussi huit paroisses françaises dans le comté de Kankakee, plus modestes mais plus généreuses par tête que les paroisses rurales du diocèse (données de 1926).")
F('02', "Saint-George (Illinois) : l'école publique tenue par les religieuses, payée par le comté (jusqu'aux années 1960)", 'etablissement', '1890~/1965~', -87.776, 41.170, 'a', [],
  "À Bourbonnais et à Saint-George, la paroisse bâtit et entretient l'unique école, confiée aux Viateurs et aux Sœurs de Notre-Dame, mais les salaires des enseignants sont payés par l'impôt du comté, à la manière des écoles confessionnelles subventionnées du Québec et de l'Ontario. Dans les années 1920, quand le comté construit de nouvelles écoles de district, il garde les religieux comme enseignants mais exige le retrait des symboles religieux et renvoie le catéchisme après les heures de classe, un compromis que l'auteur rapproche du plan de Faribault. À Bourbonnais, l'arrivée de familles protestantes après 1938 fait sortir les sœurs de l'école publique ; à Saint-George, resté homogène, elles y enseignent jusqu'aux années 1960.",
  '273-275', "Position approximative du village de Saint-George, à l'est de Bourbonnais.")
fiches = C.fiches
