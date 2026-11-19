# Virgil Benoit, « Gentilly: A French-Canadian Community in the Minnesota Red River Valley », Minnesota History 44-8
# (hiver 1975), p. 278-289 (PDF du Drive de l'auteur). Corpus « Recherches », préfixe BN75.
from commun import Corpus
BN = "Benoit, Virgil (1975), « Gentilly: A French-Canadian Community in the Minnesota Red River Valley », Minnesota History, vol. 44, n° 8, p. 278-289"
C = Corpus('Recherches', 'BN75', BN, page_fmt='p. {}')
F = C.F
GE = (-96.455, 47.795)
F('01', "Crookston : la brochure « Description de la Colonie canadienne du comté de Polk » (1883)", 'migration', '1883', -96.608, 47.774, 'c', ['Louis Fontaine', 'Pierre Bottineau', 'Jean-Baptiste Bottineau'],
  "En 1883, un comité de Canadiens français publie à Crookston une brochure de vingt-deux pages qui donne les noms de vingt compatriotes prêts à renseigner les futurs colons. Elle couvre Crookston, Carmen, Fisher, Gentilly, Red Lake Falls, Terrebonne, Emardville, Lambert, Lafontaine, Rivière Voleuse (Thief River), Louisville, Rivière Noire et Lac aux Érables. Louis Fontaine, marchand de Saint Paul, arrive à Crookston en 1878 ; le guide métis Pierre Bottineau et son fils amènent alors de nombreuses familles des comtés de Ramsey et Hennepin et de l'Est le long de la Red Lake et de la Clearwater.",
  '279-280')
F('02', "Red Lake Falls : arrivée du père Pierre Beaugrand-Champagne, missionnaire à pied (1er novembre 1878)", 'religion', '1878-11-01/1882', -96.274, 47.882, 'c', ['Pierre Beaugrand-Champagne', 'Louis-François Laflèche'],
  "Né en 1839 à Saint-Ambroise-de-Kildare (Joliette) et ordonné en 1867 par Mgr Laflèche, ancien missionnaire de la Rivière-Rouge, le père Champagne arrive à Red Lake Falls à la Toussaint 1878. En quatre ans, il y fonde la paroisse et dessert à pied douze autres missions dans un rayon de 150 milles, de la réserve de Red Lake à Saint-Vincent, à la frontière du Manitoba ; il dit parfois la messe à l'école de Gentilly.",
  '280')
F('03', "Gentilly : 142 familles, des parents et des voisins du Québec (recensements paroissiaux de 1882 et 1889)", 'migration', '1882/1889', GE[0], GE[1], 'c', ['Alexandre Bouchard', 'Élie Theillon', 'Isaïe Normandin', 'Moïse Ricard'],
  "Le recensement paroissial de 1889, dressé par le curé Théillon, compte 142 familles canadiennes-françaises, dont au moins 125 liées à d'autres par la parenté ou le lieu d'origine : dix-huit de Saint-Isidore, douze de Joliette, dix de Saint-Urbain, sept de Longueuil, six de Saint-Hyacinthe, deux de Gentilly. Entre 1882 et 1889, au moins quarante-neuf familles sont venues puis reparties, certaines retournant au Québec avant de revenir. Isaïe Normandin, arrivé en 1882 pour racheter la terre de son beau-frère Moïse Ricard, n'avait « absolument rien ».",
  '280-283')
F('04', "Canton de Crookston : les Brunelle de Gentilly (Québec) sur la Red Lake (1880-1894)", 'famille', '1880/1894', -96.64, 47.81, 'a', ['Joseph Brunelle', 'Arthur Brunelle', 'Célina Verville'],
  "Joseph Brunelle, dont neuf des dix enfants sont nés à Gentilly (Québec), vend sa terre 4 000 $ et s'établit en 1880 au nord-ouest du Gentilly minnesotain. Son fils Arthur défriche une terre voisine sur la rive nord de la Red Lake, puis retourne à Gentilly en 1894 épouser sa cousine Célina Verville, sœur de la femme de son frère. Les dix enfants s'établiront à moins de dix milles du bien paternel, que leur petit-fils occupait encore en 1975.",
  '283', "Position approximative sur la rive nord de la Red Lake, canton de Crookston.")
F('05', "Gentilly : la fromagerie du curé Théillon (1895-1968)", 'commerce', '1895-04-29/1968-01-02', GE[0]+0.004, GE[1], 'c', ['Élie Theillon', 'H. T. Gendron', 'W. H. Verity', 'Gabriel Bernou'],
  "Arrivé en 1888, le Limousin Élie Théillon, venu par Valleyfield, pousse ses paroissiens découragés vers la polyculture. Avec le marchand H. T. Gendron, il fonde la Gentilly Dairy Association, réunie pour la première fois le 29 avril 1895 ; la fromagerie, bâtie pour 784,35 $, remporte le premier prix à la foire d'État dès 1895 et sera en 1915 la seule encore active du comté de Polk. Autorisé par Rome à diriger une entreprise commerciale, le curé vend jusqu'à Chicago et au Montana et bâtit en 1915 une église de brique de 35 000 $. Il meurt en 1935 ; la fabrication cesse en 1948 et l'association est dissoute le 2 janvier 1968.",
  '284-287', "Le roman d'Evelyn Voss Wise, The Long Tomorrow (1938), s'inspire de Théillon.")
F('06', "Gentilly : hommage à Louis Riel et visite de Tardivel (1885-1888)", 'evenement', '1885-12-19/1888-06', GE[0]-0.003, GE[1]+0.002, 'c', ['Louis Riel', 'Clément-V. Gamache', 'Élie Theillon'],
  "Le 19 décembre 1885, la communauté de Gentilly se réunit pour honorer Louis Riel, pendu le mois précédent et tenu pour un martyr de la cause canadienne-française ; après la messe, on prône un parti national et on quête pour sa famille. En février 1888, le délégué de la convention nationale franco-américaine de Nashua y est accueilli par son ancien condisciple le curé Gamache et 500 Canadiens ; Terrebonne élit le père Théillon délégué à Nashua.",
  '288-289')
fiches = C.fiches
