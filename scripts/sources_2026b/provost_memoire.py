# Étienne Provost dans la mémoire québécoise : article de Denis Vaugeois (Le Devoir, 2008) et roman de Louis Hamelin (2020),
# documents du dossier ETIENNE_PROVOST_AUDUBON du Drive de l'auteur. Corpus « Recherches », préfixe PVM.
from commun import Corpus
VG = "Vaugeois, Denis (2008), « Provost, Québec - Provo, Salt Lake, Utah ? », Le Devoir, 16-17 février 2008 (coupure du Drive de l'auteur)"
C = Corpus('Recherches', 'PVM', VG, page_fmt='{}')
F = C.F
F('01', "Provo (Utah) : Denis Vaugeois relie le trappeur québécois Étienne Provost à la ville mormone (Le Devoir, 2008)", 'toponymie', '2008-02', -111.6585, 40.2338, 'c', ['Étienne Provost', 'Denis Vaugeois', 'John James Audubon', 'Bad Gocha'],
  "L'historien et éditeur Denis Vaugeois raconte aux lecteurs du Devoir la vie d'Étienne Provost : parti avant ses vingt ans pour la traite avec Saint-Louis pour base, emprisonné par les Espagnols en 1817, de retour à Taos en 1821. En 1824, il est l'un des premiers Blancs à atteindre le Grand Lac Salé ; le chef shoshone Bad Gocha l'attire à un calumet de paix sans armes, et l'embuscade décime sa troupe. Vaugeois évoque aussi Provost guide d'Audubon en 1843, saisi par Alfred Jacob Miller dans la toile Catching Up (1837). Il rappelle que la rivière, puis la ville de Provo, où une trentaine de familles mormones conduites par John S. Higbee s'installent en 1849, portent son nom.",
  'non paginé')
F('02', "Fort Union : Les Crépuscules de la Yellowstone, roman de Louis Hamelin sur Audubon et son guide Provost (2020)", 'evenement', '2020', -104.0405, 47.9994, 'c', ['Louis Hamelin', 'Étienne Provost', 'John James Audubon', 'Alexander Culbertson', 'Alexis La Bombarde'],
  "Le romancier québécois Louis Hamelin fait de la remontée du Missouri par Audubon en 1843 un roman-fleuve, avec Étienne Provost en guide et contrepoint. On y croise, à bord du vapeur et aux forts de l'American Fur Company, Alexander Culbertson, le Métis Alexis La Bombarde et les nations du Haut-Missouri (Pieds-Noirs, Assiniboines, Arikaras, Mandans). Le livre s'ouvre sur une phrase de Ramsay Crooks, président de la compagnie, sur la docilité « utile à nos affaires » des engagés canadiens.",
  'roman', "Œuvre de fiction : la fiche situe le roman à Fort Union, terme du voyage d'Audubon en 1843.",
  source="Hamelin, Louis (2020), Les Crépuscules de la Yellowstone, roman, Montréal, Boréal (PDF du Drive de l'auteur)")
fiches = C.fiches
