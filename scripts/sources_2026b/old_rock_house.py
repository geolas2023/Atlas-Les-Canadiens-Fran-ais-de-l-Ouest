# La « Old Rock House » de Saint-Louis : N. M. Hoppe, « Whatever Happened to The Old Rock House? » (NPS, Jefferson
# National Expansion Memorial, janvier 1998) et HABS MO-31-5 (données écrites, 1933-1986). PDF du Drive de l'auteur
# (dossier MANUEL_LISA / ST_LOUIS). Corpus « Recherches », préfixe RH98.
from commun import Corpus
NPS = "Hoppe, Nancy Marie (1998), « Whatever Happened to The Old Rock House? », National Park Service, Jefferson National Expansion Memorial"
HABS = "Historic American Buildings Survey, Old Rock House, Wharf and Chestnut Streets, St. Louis, HABS MO-31-5 (données écrites de W. T. Trueblood et lettre de Marcel F. Doyle, 16 juin 1933 ; addenda Piaget-van Ravenswaay)"
C = Corpus('Recherches', 'RH98', NPS, page_fmt='p. {}')
F = C.F
X, Y = -90.1842, 38.6262
F('01', "Saint-Louis : l'entrepôt de pelleteries de Manuel Lisa, la « Old Rock House » (1818-1959)", 'commerce', '1810/1959', X, Y, 'c', ['Manuel Lisa', 'Jean-Baptiste Trudeau', 'Oliver N. Bostwick', 'Wilson Price Hunt'],
  "En 1810, Manuel Lisa achète à Jean-Baptiste Trudeau un terrain du bord de l'eau, à l'angle des rues Wharf et Chestnut, où il bâtit maison et magasin ; en 1818, il fait construire en contrebas, avec la pierre de l'ancienne carrière, son entrepôt de fourrures. Après sa mort (1820), l'entrepôt passe en 1825 au traiteur Oliver Bostwick, associé à l'American Fur Company d'Astor, puis sert de dépôt à l'expédition de Yellowstone (1819), de voilerie pour les chariots de l'Ouest et de taverne. Seul bâtiment du quai épargné avec le Vieux Palais de justice et la Vieille Cathédrale, restauré en 1943, il est démonté en 1959 pour le passage des voies ferrées devant l'Arche.",
  '1-2', "Position à l'ancien angle Wharf-Chestnut, au pied de l'Arche.")
F('02', "Saint-Louis : la tradition Marcheteau-Desnoyers et Bissonet sur le site de la Old Rock House (1767-1808)", 'famille', '1767~/1808', X+0.0004, Y+0.0003, 'h', ['Joseph Marcheteau dit Desnoyers', 'François Bissonet', 'Marie-Catherine Marcheteau Desnoyers', 'Jean-Baptiste Trudeau', 'Bernard Pratte'],
  "Selon une lettre de 1933 d'un descendant, Marcel F. Doyle, versée au dossier HABS, la maison de pierre aurait été bâtie dès 1767 par Joseph Marcheteau dit Desnoyers, venu du Canada par Cahokia, qui l'aurait cédée en 1769 par acte rédigé en français à son gendre François Bissonet, venu de Fort de Chartres, contre la promesse de le loger et nourrir jusqu'à sa mort. La veuve, Marie-Catherine Marcheteau Desnoyers, l'échange en 1798 avec Jean-Baptiste Trudeau (confirmation espagnole du 20 octobre 1799), qui la vend en 1808 à Bernard Pratte ; Lisa n'aurait fait que la louer. Le NPS date au contraire l'entrepôt de 1818.",
  '', "Tradition familiale contredite par la datation du NPS ; la cession Bissonet-Trudeau de 1798 est confirmée par les deux sources.", source=HABS)
fiches = C.fiches
