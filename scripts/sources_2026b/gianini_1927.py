# C. A. Gianini, « Manuel Lisa, One of the Earliest Traders on the Missouri River », New Mexico Historical Review 2-4 (1927),
# PDF du Drive de l'auteur (dossier MANUEL_LISA). Corpus « Recherches », préfixe GI27.
from commun import Corpus
GI = "Gianini, Charles A. (1927), « Manuel Lisa, One of the Earliest Traders on the Missouri River », New Mexico Historical Review, vol. 2, n° 4, p. 323-333"
C = Corpus('Recherches', 'GI27', GI, page_fmt='p. {}')
F = C.F
ML = 'Manuel Lisa'
F('01', "Saint-Louis : Manuel Lisa passe contrat avec « Roubidoux » (1798)", 'commerce', '1798', -90.1885, 38.6255, 'a', [ML, 'Joseph Robidoux'],
  "Né de parents espagnols à La Nouvelle-Orléans vers 1772, Manuel Lisa traite déjà sur le Mississippi à vingt ans. Il arrive à Saint-Louis en 1798 et conclut la même année un contrat avec « Roubidoux », un vieux traiteur indien, sans doute Joseph Robidoux père. Il signe aussi la pétition contre les monopoles de traite accordés par le gouverneur Trudeau.",
  '323', "Prénom de Robidoux non précisé par Gianini.")
F('02', "Les Osages des Chouteau passent sur l'Arkansas pour échapper au monopole de Lisa (1802)", 'commerce', '1802~', -95.36, 35.97, 'a', [ML, 'Pierre Chouteau', 'Auguste Chouteau'],
  "Lisa et deux associés obtiennent de l'Espagne le monopole de la traite osage, que tenaient les Chouteau. Ceux-ci persuadent une grande partie de la nation de quitter le Missouri pour l'Arkansas, où ils sont bien établis : la scission des Osages mettra longtemps à se refermer. Lisa ne garde le privilège qu'un an et, pour une lettre trop vive au gouverneur Delassus, passe quelque temps au cachot.",
  '324', "Position aux Trois-Fourches de l'Arkansas (bande de Clermont, Verdigris).")
F('03', "Embouchure de la Platte : Lisa fait rebrousser chemin à John Colter (1807)", 'exploration', '1807', -95.86, 41.05, 'a', [ML, 'John Colter', 'George Drouillard'],
  "Lors de sa première remontée du Missouri, avec une seule barge, Lisa croise près de la Platte John Colter, ancien de l'expédition Lewis et Clark qui descendait le fleuve, et le convainc de repartir vers le haut pays. L'expédition, menée avec George Drouillard, passe les Arikaras, les Mandans et les Assiniboines par la force ou la persuasion et fonde le fort Manuel au Bighorn ; c'est de là que Colter partira vers les « merveilles » de Yellowstone.",
  '325-326')
F('04', "Trois-Fourches du Missouri : le poste de Lisa au pays des Pieds-Noirs et la mort de Drouillard (1809-1810)", 'poste', '1809/1810', -111.52, 45.92, 'a', [ML, 'George Drouillard', 'Andrew Henry'],
  "En 1809, Lisa ramène à son village le chef mandan Shehaka et fait bâtir des postes chez les Gros-Ventres (Hidatsas) et aux Trois-Fourches du Missouri, en plein pays pied-noir. L'hostilité des Pieds-Noirs fait abandonner les Trois-Fourches en un an ou deux ; George Drouillard y est tué et le major Henry passe sur le versant ouest des montagnes.",
  '326-327')
F('05', "La grande course sur le Missouri : Lisa rattrape les Astoriens de Hunt (1811)", 'exploration', '1811-04/1811-06', -98.05, 42.77, 'h', [ML, 'Wilson Price Hunt'],
  "Parti deux semaines après le groupe astorien de Wilson Price Hunt, qui le soupçonnait d'avoir fait échouer Pierre Chouteau en 1807, Lisa remonte le Missouri avec une seule barge et un équipage choisi. Il rattrape Hunt juste au-delà du pays sioux après deux mois et quelque 1 200 milles, puis les deux chefs se réconcilient. Brackenridge et Bradbury en tiennent le récit, que Washington Irving reprendra dans « Astoria ».",
  '327', "Point de jonction approximatif, près de l'embouchure de la Niobrara.")
F('06', "Villages arikaras : Lisa désamorce une crise avec dix hommes (1812)", 'evenement', '1812', -100.47, 45.52, 'a', [ML],
  "En 1812, en route avec deux barges, Lisa voit les Arikaras éloigner femmes et enfants des bateaux, signe d'hostilité. Il descend à terre avec dix hommes et convoque les chefs : la querelle tient aux présents distribués aux uns et pas aux autres, et au poste de traite qu'ils réclament. L'accord rétablit la paix. Son commis Luttig, qui hiverne au fort Manuel, notera la mort de Sacagawea cet hiver-là.",
  '328-329', "Position aux villages arikaras, embouchure de la Grand (Dakota du Sud).")
F('07', "Haut Arkansas : Charles Sanguinet chez les Arapahos, à la recherche des Espagnols (1812)", 'exploration', '1812/1813', -103.2, 38.05, 'h', ['Charles Sanguinet', ML],
  "Parmi les partis envoyés par Lisa en 1812, celui de Charles Sanguinet gagne l'Arkansas pour traiter avec les Arapahos, mais surtout pour entrer en contact avec les marchands espagnols, muni d'une lettre aux autorités du Nouveau-Mexique. Il doit aussi retrouver un premier groupe expédié deux ans plus tôt, dont certains ne reviendront jamais ; d'autres hommes de Lisa seront détenus dix ans par les Espagnols.",
  '328-329', "Gianini renvoie à Bolton (1913) pour la lettre. Position hypothétique sur le haut Arkansas.")
F('08', "Île aux Cèdres ou île Américaine : Lisa dresse les Tétons contre les Santees (guerre de 1812)", 'evenement', '1813/1814', -99.33, 43.81, 'a', [ML, 'Joseph Renville', 'Tamaha', 'Robert Dickson'],
  "Sous-agent de William Clark pour les Indiens du Missouri, Lisa tient un gros poste sur l'île Américaine (Chamberlain) ou l'île aux Cèdres. Selon une lettre de Joseph Renville, interprète britannique, il retient les Tétons dans le camp américain et, chaque fois que les Santees veulent rejoindre les Anglais, fait courir le bruit que les Tétons vont attaquer leurs familles, annulant les efforts de l'agent Robert Dickson ; il paie Tamaha, le Sioux borgne, pour espionner les siens.",
  '330-331', "Position à l'île Américaine (Chamberlain, Dakota du Sud).")
F('09', "Saint-Louis : quarante-trois chefs amenés par Lisa pour les traités (1815)", 'evenement', '1815', -90.19, 38.63, 'c', [ML, 'William Clark'],
  "En 1815, Lisa conduit à Saint-Louis quarante-trois chefs et notables amis pour une visite et la signature de traités. Il démissionne de son agence en 1817, revient de son dernier voyage en avril 1820 et meurt en août. Il eut une épouse omaha, Mitain, fille d'un chef, dont la descendance s'est perpétuée ; sa dernière femme, Mary Hempstead (« Aunt Manuel »), lui survécut longtemps.",
  '331-332', "Traités de Portage des Sioux (1815), probablement.")
fiches = C.fiches
