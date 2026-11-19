# Glenn Turner, The Toronto Carrying Place: Rediscovering Toronto's Most Ancient Trail, Toronto, Dundurn, 2015.
# PDF du Drive de l'auteur, lu en partie par Drive (environ 107 000 caractères). Corpus « Recherches », préfixe TU15.
from commun import Corpus
TU = "Turner, Glenn (2015), The Toronto Carrying Place: Rediscovering Toronto's Most Ancient Trail, Toronto, Dundurn"
C = Corpus('Recherches', 'TU15', TU, page_fmt='{}')
F = C.F
F('01', "Toronto : le fort Rouillé et les deux postes qui l'ont précédé (1720-1759)", 'poste', '1720/1759', -79.4210, 43.6327, 'c', ['Jean-Baptiste Rousseau'],
  "Pour détourner vers eux les fourrures du Nord-Ouest qui filent aux Anglais, les Français élèvent trois postes successifs à Toronto. Un premier « magasin royal » est bâti en 1720 sur les ruines du village iroquois abandonné de Teiaiagon, puis délaissé ; un poste palissadé, le fort Toronto, est fondé en 1750 au départ traditionnel du portage, sur la rive est de la Humber ; trop petit, il est remplacé en 1751 par le fort Rouillé, carré à bastions de chêne équarri avec forge, boulangerie, casernes et magasin, dominant la baie. En 1757, quatre-vingt-dix guerriers mississagués menacent de le piller jusqu'à l'arrivée de deux bateaux de soldats de Niagara ; en 1759, après la chute de Niagara, la garnison l'incendie et se replie sur Montréal. Le second poste sera repris et réaménagé en maison par Jean-Baptiste Rousseau. Un obélisque marque aujourd'hui l'emplacement du fort Rouillé.",
  "chap. 1 (édition non paginée dans la copie lue)", "Point au site du fort Rouillé (terrain de l'Exposition nationale canadienne).")
fiches = C.fiches
