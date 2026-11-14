# Compléments au corpus « Illinois français » (l'Illinois français et l'archipel du Midwest) :
#   McQuillan, D. A. (1979), « French-Canadian Communities in the American Upper Midwest during the Nineteenth Century »,
#     Cahiers de géographie du Québec, 23 (58), p. 53-72.
#   Papen, R. A. (2006), « Les parlers français oubliés d'Amérique : le franco-minnesotain et le franco-dakotain »,
#     Revue de l'Université de Moncton, 37 (2), p. 149-171.
from commun import Corpus
MQ = "McQuillan, D. Aidan (1979), « French-Canadian Communities in the American Upper Midwest during the Nineteenth Century », Cahiers de géographie du Québec, vol. 23, no 58"
PA = "Papen, Robert A. (2006), « Les parlers français oubliés d'Amérique : le franco-minnesotain et le franco-dakotain », Revue de l'Université de Moncton, vol. 37, no 2"
C = Corpus('Illinois français', 'IF2', MQ)
F = C.F

# ---- McQuillan 1979
F('mq01', 'Michigan : villes fondées par des Canadiens après 1812', 'etablissement', '1820/1829', -85.67, 42.96, 'h', [],
  "Après la guerre de 1812, des Canadiens partis du noyau de Détroit essaiment dans le sud du Michigan et participent à la fondation de Grand Rapids, Bay City, Midland et Grand Haven dans les années 1820.", '54',
  "Point placé à Grand Rapids pour l'ensemble des quatre villes.")
F('mq02', 'Bourbonnais Grove : Noël Le Vasseur', 'etablissement', '1832', -87.879, 41.152, 'c', ['Noël Le Vasseur'],
  "Né à Yamaska en 1799, Noël Le Vasseur fait la traite dans la région du Wisconsin et des Grands Lacs avant de s'établir à Bourbonnais Grove en 1832. Il retourne au Québec en 1840 recruter des familles ; une chapelle en rondins est bâtie en 1841, et à la fin des années 1840 environ mille familles françaises vivent dans les environs.", '55')
F('mq03', 'Bourbonnais : collège Saint-Viateur et couvent', 'religion', '1858/1874', -87.879, 41.152, 'c', [],
  "Église de pierre dédiée à la Maternité de la Vierge (1858), couvent de la Congrégation de Notre-Dame (1861), puis collège classique des Clercs de Saint-Viateur venus de Joliette (1865), qui obtient une charte universitaire en 1874 et forme une élite franco-américaine.", '59')
F('mq04', "Sainte-Anne (Illinois) : schisme de Chiniquy", 'religion', '1853-09/1856', -87.714, 41.025, 'c', ['Charles Chiniquy'],
  "Soupçonné d'avoir incendié la nouvelle église de Bourbonnais en septembre 1853, Charles Chiniquy s'installe avec ses partisans au village voisin de Sainte-Anne ; l'évêque de Chicago l'excommunie en 1856.", '59')
F('mq05', 'Kankakee : Georges Létourneau, sénateur', 'personnage', '1892', -87.861, 41.12, 'c', ['Georges Létourneau', 'Joseph Legris'],
  "Revenus de Californie avec de petites fortunes, Joseph Legris et Georges Létourneau développent fermes et commerces à Kankakee ; Létourneau, républicain, est élu sénateur de l'État en 1892.", '59; 60')
F('mq06', 'Vallée de la Republican (Kansas) : colonies venues de Kankakee', 'migration', '1868/1896', -97.4, 39.59, 'a', [],
  "À partir de 1868, des Canadiens de Kankakee gagnent l'est du Kansas par le terminus ferroviaire de Waterville et prennent des homesteads dans la vallée de la Republican (Clyde, Concordia). Malgré la crise de 1893-1896, la plupart prospèrent.", '60')
F('mq07', 'Saint Paul : le marchand Fontaine', 'commerce', '1858', -93.09, 44.95, 'c', ['Fontaine'],
  "Né en 1839, Fontaine arrive à Saint Paul en 1858 et y devient un marchand prospère avant de lancer la colonie du comté de Polk.", '61')
F('mq08', 'Crookston : colonie canadienne du comté de Polk', 'etablissement', '1878/1885', -96.608, 47.774, 'c', ['Fontaine', 'Rémi Fortier'],
  "En 1878, Fontaine s'associe à Rémi Fortier à Crookston et tous deux attirent des compatriotes par lettres et par une brochure (1883) vantant la terre noire. En 1885, on compte de 5 000 à 8 000 Canadiens entre Crookston et Red Lake Falls ; des agents américains détournent à Duluth des migrants en route vers le Manitoba.", '61')
F('mq09', 'Gentilly (Minnesota)', 'etablissement', '1883', -96.45, 47.785, 'c', [],
  "Cœur de la colonie du comté de Polk, le canton et village de Gentilly est entièrement canadien-français en 1883 : église catholique, deux écoles, un magasin général et deux hôtels.", '62')
F('mq10', 'Chantiers et scieries du Wisconsin et du Michigan', 'migration', '1850/1895', -89.6, 45.6, 'h', [],
  "Des Canadiens bûcherons suivent les capitalistes canadiens vers les forêts des Grands Lacs ; selon Saint-Pierre (1895), neuf sur dix travaillent aux chantiers l'hiver et aux scieries l'été.", '62', "Point régional (nord du Wisconsin).")
F('mq11', 'Péninsule de Keweenaw : mines de cuivre', 'migration', '1840/1862', -88.45, 47.12, 'a', [],
  "La ruée vers le cuivre du Keweenaw (années 1840) et les mines de fer de la chaîne Marquette (1844) attirent des Canadiens, dont d'anciens voyageurs ; après la crise de 1857, beaucoup quittent le nord du Wisconsin (1861-1862), puis reviennent quand les prix remontent à l'été 1862.", '62; 64')
F('mq12', 'Sault-Sainte-Marie : canal de 1855', 'evenement', '1855', -84.35, 46.5, 'c', [],
  "L'ouverture du canal du Sault en 1855 favorise l'essor minier mais porte un coup fatal au transport des voyageurs et de leurs bateaux.", '62')
F('mq13', 'Détroit : paroisse de 1808 et paroisse canadienne', 'religion', '1808/1888', -83.045, 42.331, 'c', ['Maxime Laporte'],
  "La première paroisse de Détroit est organisée en 1808 par des Canadiens de la traite. L'abbé Maxime Laporte arrive de Montréal en 1874 pour les nouveaux immigrants ; après des conflits avec l'évêque Borgess, celui-ci consent des concessions à la paroisse canadienne en 1888.", '65; 66')
F('mq14', 'Grand Rapids : appel aux prêtres canadiens', 'religion', '1882', -85.67, 42.96, 'c', [],
  "À la création du diocèse de Grand Rapids (1882), l'évêque Richter fait appel à des prêtres canadiens-français pour encadrer leurs compatriotes.", '67')
F('mq15', 'Chicago : paroisse Saint-Louis, première paroisse nationale', 'religion', '1848/1857', -87.632, 41.879, 'c', [],
  "Chicago naît d'un petit poste de traite tenu par un Canadien après 1812. Les Canadiens n'ont un prêtre résident qu'en 1833 ; la paroisse Saint-Louis, à l'angle des rues Clark et Quincy, est érigée en 1848 comme première paroisse nationale des Canadiens.", '67')
F('mq16', 'Chicago : Notre-Dame (Sibley et Vernon Park)', 'religion', '1864/1887', -87.66, 41.874, 'a', ['Jacques Côté'],
  "Curé de 1864 à 1884, l'abbé Jacques Côté vend l'ancien site paroissial et rachète un terrain au sud ; école confiée à la Congrégation de Notre-Dame (1885, 400 enfants), presbytère (1886) et nouvelle église Notre-Dame (1887).", '68')
F('mq17', 'Chicago : Saint-Joseph de Brighton Park', 'religion', '1889/1893', -87.7, 41.818, 'a', [],
  "Paroisse canadienne organisée en 1889 dans la banlieue ouest ; 250 familles en 1893, souvent venues de Saint-Jean-Baptiste de Bridgeport, et un club Jacques-Cartier très actif.", '68; 69')
F('mq18', 'Minneapolis : Notre-Dame-de-Lourdes et Sainte-Anne', 'religion', '1891', -93.26, 44.99, 'a', [],
  "Environ 10 000 Canadiens français vivent à Minneapolis en 1891, regroupés en deux paroisses (Notre-Dame et Sainte-Anne) ; le Guide français réclame des écoles paroissiales de langue française.", '70')

# ---- Papen 2006
G = lambda *a, **k: F(*a, source=PA, **k)
G('pa01', 'Pembina : poste de Chaboillez', 'poste', '1797', -97.243, 48.966, 'c', ['Charles Chaboillez'],
  "En 1797, Chaboillez, employé canadien de la Compagnie du Nord-Ouest, ouvre un poste de traite à Pembina ; la frontière du 49e parallèle (1818) passe à quelques kilomètres au nord.", '152')
G('pa02', 'Saint Paul : fondation par des Canadiens et des Métis', 'etablissement', '1838', -93.09, 44.95, 'c', [],
  "En 1838, Saint Paul, future capitale du Minnesota, est fondée par des Canadiens et quelques Métis, dont plusieurs venus de la Rivière-Rouge.", '153')
G('pa03', 'Saint-Joseph (Walhalla) : poste de Norman Kittson', 'poste', '1843', -97.918, 48.923, 'c', ['Norman Kittson'],
  "En 1843, le Montréalais Norman Kittson établit un poste de traite à Saint-Joseph, aujourd'hui Walhalla (Dakota du Nord).", '153')
G('pa04', 'Gentilly et Red Lake Falls : fondation par Pierre Bottineau', 'etablissement', '1873/1876', -96.274, 47.882, 'c', ['Pierre Bottineau'],
  "De 1873 à 1876, le guide métis Pierre Bottineau fonde Gentilly et Red Lake Falls avec des familles canadiennes du Manitoba et de Saint Paul, après le traité imposé aux Ojibwés de Pembina et de Red Lake (1863).", '153')
G('pa05', 'Folle Avoine (Wild Rice, Dakota du Nord)', 'etablissement', '1869', -96.79, 46.77, 'a', ['Cossette'],
  "En 1869, un ancien trappeur nommé Cossette fonde la communauté francophone de Folle Avoine, plus tard anglicisée en Wild Rice, sur la rive ouest de la rivière Rouge.", '154')
G('pa06', 'Oakwood et Olga (Dakota du Nord)', 'migration', '1878/1881', -98.25, 48.78, 'a', [],
  "Oakwood (1878) et Olga (1881) sont fondées par des familles canadiennes-françaises venues du Massachusetts et du Rhode Island ; Willow City devient aussi un foyer important.", '154')
G('pa07', 'Réserve de Turtle Mountain et Belcourt : le mitchif', 'etablissement', '1882', -99.745, 48.84, 'c', [],
  "La réserve ojibwée de Turtle Mountain, créée en 1882 pour les bandes de Red Lake et de Pembina, accueille de nombreux Métis de la Rivière-Rouge. Le français mitchif de Belcourt y était encore parlé par des aînées enregistrées en 1985.", '154; 156')
G('pa08', 'Red Lake Falls : déclin du français', 'etablissement', '1980/1985', -96.274, 47.882, 'c', ['Virgil Benoit'],
  "En 1980, 70 % des 39 personnes interrogées à Red Lake Falls disent encore le français langue première, mais seulement les plus de 50 ans ; en 1985, il resterait moins d'une centaine de locuteurs, presque tous âgés de plus de 60 ans.", '156; 158')

fiches = C.fiches
