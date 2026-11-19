# Carolyn Hewes Toft (dir.), St. Louis: Landmarks & Historic Districts (Saint-Louis, Landmarks Association of St. Louis, 1988) ;
# PDF fourni par l'auteur de l'atlas le 19 novembre 2026. Corpus « Recherches », préfixe TFT88. Résumés rédigés par l'atlas.
from commun import Corpus
SRC = "Toft, Carolyn Hewes (dir.) (1988), St. Louis: Landmarks & Historic Districts, Saint-Louis, Landmarks Association of St. Louis"
C = Corpus('Recherches', 'TFT88', SRC, page_fmt='p. {}')
F = C.F
F('01', "Saint-Louis : Laclede's Landing, seul vestige du plan de rues du village français (arpentage de 1780)", 'toponymie', '1780', -90.1840, 38.6305, 'c', ['Pierre de Laclède Liguest', 'Auguste Chouteau'],
  "Le guide des monuments de Saint-Louis note que le quartier de Laclede's Landing, au nord de l'arche, conserve la seule portion subsistante du tracé des rues issu de l'arpentage de 1780 du village français né autour du comptoir fondé en 1764 par Laclède et Chouteau ; le reste du vieux village a été rasé pour le Jefferson National Expansion Memorial.",
  None, "Position du quartier de Laclede's Landing.")
F('02', "Saint-Louis : la vieille cathédrale de Mgr Rosati, achevée en 1834", 'religion', '1831/1834', -90.1868, 38.6245, 'c', ['Joseph Rosati', 'Morton', 'Laveille'],
  "La Old Cathedral (basilique Saint-Louis-Roi-de-France), aux murs de moellons calcaires et à la façade de grès poli, est achevée en 1834 sur les plans de Morton et Laveille ; elle se dresse sur le terrain réservé à l'église dès le village colonial et a survécu au déblaiement des berges.",
  None, "Position de la Old Cathedral.")
F('03', "Saint-Louis : la maison Chatillon-DeMenil, foyer d'Henri Chatillon et d'Odile Delor (vers 1849)", 'famille', '1849', -90.2135, 38.6005, 'c', ['Henri Chatillon', 'Odile Delor', 'Clément Delor de Treget', 'Francis Parkman'],
  "Henri Chatillon, chasseur et guide de l'expédition de Francis Parkman sur la piste de l'Oregon (1846), et sa femme Odile Delor, petite-fille de l'officier français fondateur de Carondelet en 1767, bâtissent vers 1849 le premier corps de cette maison, agrandie ensuite en villa néo-grecque par les DeMenil ; sauvée de l'autoroute dans les années 1960, elle est devenue musée.",
  None, "Position du 3352 DeMenil Place.")
F('04', "Carondelet : village fondé en 1767 et peuplé de Créoles, Français et Canadiens", 'etablissement', '1767/1870', -90.2605, 38.5560, 'a', ['Clément Delor de Treget'],
  "Fondé en 1767 et commune distincte jusqu'en 1870, Carondelet est d'abord peuplé de Créoles, de Français et de Canadiens ; le village n'est incorporé qu'en 1832, quand s'y installe déjà une petite population allemande, puis ses maisons de pierre du milieu du siècle sont surtout l'œuvre d'immigrants allemands.",
  None, "Position du vieux Carondelet.")
F('05', "Saint-Louis : la maison du Belge Emmanuel de Hodiamont, ancien trappiste de Florissant (vers 1818)", 'personnage', '1808/1818', -90.2835, 38.6625, 'a', ['Emmanuel de Hodiamont'],
  "Né en Belgique, peut-être baron déshérité, Emmanuel de Hodiamont passe ses années américaines chez les trappistes, dont une à Florissant (1808-1809), puis quitte l'ordre vers 1818 pour se marier et se lancer dans l'immobilier et l'agriculture ; il bâtit la maison de pierre qui porte son nom avant de se retirer à l'abbaye de Gethsemani, au Kentucky.",
  None, "Position approximative de la maison de Hodiamont (Maple Place).")
F('06', "Saint-Louis : la maison de René Beauvais, orfèvre d'ascendance canadienne-française (vers 1866)", 'personnage', '1866', -90.2540, 38.6155, 'a', ['René Beauvais'],
  "La maison néo-grecque de brique rouge de Shaw Place est construite vers 1866 pour René Beauvais, orfèvre et bijoutier en vue d'ascendance canadienne-française ; elle devient en 1882 une maison de retraite de la Women's Christian Association.",
  None, "Position approximative près de Shaw Place.")
fiches = C.fiches
