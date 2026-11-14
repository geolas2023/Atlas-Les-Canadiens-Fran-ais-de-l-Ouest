# Corpus « Franco-Amérique » : Louder, Dean et Éric Waddell (dir.), Franco-Amérique, Québec, Septentrion, 2008.
# (Vision et visages de la Franco-Amérique, Septentrion, 2001, n'a été fourni qu'en extrait liminaire : rien de localisable.)
from commun import Corpus
B = "Louder, Dean et Éric Waddell (dir.) (2008), Franco-Amérique, Québec, Septentrion"
C = Corpus('Franco-Amérique', 'FA', B)
def F(id, nom, theme, date, lon, lat, cert, pers, desc, page, auteur, note=''):
    C.F(id, nom, theme, date, lon, lat, cert, pers, desc, page, note, source=f"{auteur}, dans {B}")

JL = "Lamarre, Jean, « Migrants, défricheurs, fondateurs : les Canadiens français du Michigan et de l'Illinois »"
F('mi01', 'Saginaw : la famille Lavigne', 'migration', '1852/1870', -83.95, 43.42, 'c', ['Georges Lavigne'],
  "Mariés à la fin des années 1840, Georges Lavigne et son épouse passent par l'État de New York (1852) puis le Michigan (1856) ; en 1870, Georges est journalier dans le comté forestier de Saginaw. Leur parcours illustre la migration familiale vers le Midwest.", '197', JL)
F('mi02', 'Détroit : fermeture de Sainte-Anne par Mgr Borgess', 'religion', '1870/1879', -83.045, 42.331, 'c', ['Mgr Borgess'],
  "Dans les années 1870, Mgr Borgess ferme unilatéralement la paroisse Sainte-Anne (1809) et vend le terrain de l'église ; les paroissiens finissent par se soumettre. Vers 1850, le Midwest compterait près de 20 000 Canadiens français.", '200; 201', JL)
F('mi03', 'Chicago : le curé Saint-Cyr et Notre-Dame', 'religion', '1833/1884', -87.632, 41.879, 'c', ['Saint-Cyr (curé)'],
  "En 1833, les Canadiens obtiennent un prêtre résident, le curé Saint-Cyr ; Saint-Louis (années 1840, curé Lebel) connaît des troubles en 1857 ; Notre-Dame (1864) accueille les nouveaux arrivants pendant vingt ans.", '201; 202', JL)
F('mi04', 'Vallée de la Saginaw : les Tromblé', 'etablissement', '1815/1860', -83.888, 43.594, 'c', ['Louis Campau', 'Léon Tromblé', 'Benoît Tromblé', 'Joseph Marsac'],
  "Dès 1815, Louis Campau commerce dans la vallée ; Léon Tromblé, ses neveux Jos et Mader (1835) et Benoît (1836), puis le chasseur Jos Marsac (1838) s'établissent à Lower Saginaw. Les Canadiens passent de 85 (1850) à 10 000 (1900).", '205; 207', JL)
F('mi05', 'Bay City : Le Courrier et Le Patriote', 'commerce', '1878/1884', -83.888, 43.594, 'c', [],
  "Le Courrier de Bay City (1878) puis Le Patriote (1882) informent la colonie ; aux municipales d'avril 1884, quatre des 21 postes vont à des Canadiens français.", '208', JL)
F('mi06', 'Lake Linden : le Petit Canada de Joseph Grégoire', 'etablissement', '1867/1900', -88.405, 47.19, 'c', ['Joseph Grégoire', 'Louis Deschamps'],
  "Associé en 1867 à Louis Deschamps, Joseph Grégoire annonce n'employer que des compatriotes ; Lake Linden devient le « Petit Canada » de la péninsule (près de la moitié des habitants de 1870 à 1900). Enseignement en français à partir de 1881 ; académie en 1886.", '209; 211', JL)
F('mi07', 'Vincennes : poste du sieur de Vincennes', 'poste', '1732', -87.528, 38.677, 'c', ['François-Marie Bissot de Vincennes'],
  "En 1732, un petit groupe de Canadiens dirigé par François-Marie Bissot de Vincennes s'établit sur la Wabash pour protéger les intérêts français à l'ouest des Appalaches.", '206', JL)

MB = "Bouchard, Michel, « De l'Acadie à l'Alberta en passant par le Kansas : sur les traces de la famille Comeau »"
F('ka01', 'Saint-Joseph (comté de Cloud, Kansas) : les Comeau', 'famille', '1879/1899', -97.55, 39.48, 'a', ['Joseph Comeau', 'Édouard Comeau'],
  "Famille acadienne passée par le Québec, les Comeau s'installent à Saint-Joseph, paroisse francophone du comté de Cloud, où naît en 1879 le premier petit-enfant ; Joseph Comeau y meurt en 1899.", '238; 241', MB)
F('ka02', 'Sherman (comté de Washington, Kansas)', 'famille', '1880', -97.1, 39.82, 'h', ['Délima Comeau'],
  "La famille de Délima, épouse d'Édouard Comeau (1886), vit dans la communauté francophone de Sherman au recensement de 1880.", '241', MB)
F('ka03', 'Rivière-qui-Barre (Alberta) : arrivée des Comeau du Kansas', 'migration', '1888/1911', -113.82, 53.8, 'c', ['Edmond Juneau', 'Édouard Comeau'],
  "Edmond Juneau, parti du Québec pour les États-Unis en 1873, s'établit en 1888 à ce qui deviendra Rivière-qui-Barre ; les Comeau venus du Kansas y sont recensés en 1901. Les prêtres colonisateurs recrutent 620 familles dans les années 1890, dont la moitié aux États-Unis.", '239; 242', MB)
F('ka04', 'Morinville : abbé Jean-Baptiste Morin', 'etablissement', '1891~', -113.65, 53.8, 'c', ['Jean-Baptiste Morin'],
  "Au début des années 1890, l'abbé Jean-Baptiste Morin fonde Morinville, à 18 km au nord de Saint-Albert.", '241', MB)

VB = "Benoît, Virgil, « De Minomin à Wild Rice en passant par Folle Avoine : une histoire du Midwest »"
F('wr01', 'Pembina : le Vieux Folle Avoine', 'migration', '1805~', -97.243, 48.966, 'a', ['Gaytay Minomin'],
  "Vers 1805, attiré par la traite, le chef Gaytay Minomin, le « Vieux Folle Avoine », quitte la source du Mississippi pour Pembina, amorçant une longue suite de migrations vers la vallée de la rivière Rouge.", '253; 254', VB)
F('wr02', 'Mission Sainte-Croix du père Genin', 'religion', '1867', -96.8, 46.8, 'h', ['Jean-Baptiste Genin'],
  "Né en France en 1839, l'oblat Jean-Baptiste Genin part pour la rivière Rouge en 1865 et fonde en 1867 la mission permanente de Sainte-Croix, puis plusieurs paroisses le long de la voie ferrée.", '257; 258', VB)
F('wr03', 'Wild Rice : les frères Dubord', 'etablissement', '1877/1946', -96.79, 46.77, 'a', ['Eusèbe Dubord', 'Paul Dubord'],
  "En 1877, Eusèbe, Philippe et Timoléon Dubord, de Champlain, arrivent à Wild Rice (Folle Avoine) ; leurs descendants y restent. En 1977, Paul et Loretta Dubord font lire un discours en français devant l'Assemblée du Dakota du Nord.", '260; 263', VB)
F('wr04', 'Wild Rice : Filles de Sainte-Marie-de-la-Présentation', 'religion', '1903/1904', -96.79, 46.77, 'a', [],
  "Chassées de France par les lois contre les congrégations, les Filles de Sainte-Marie-de-la-Présentation (Broons, 1828) arrivent à Wild Rice en 1903 pour enseigner la religion et le français.", '264; 266', VB)
KB = "Beaulne, Kent, « Être “French” et ne pas le savoir, 1960-1975 »"
F('vm01', 'La Vieille Mine (Missouri) : les « French » des Ozarks', 'famille', '1790/1975', -90.79, 38.02, 'c', ['Kent Beaulne'],
  "Sur le flanc est des Ozarks, les familles créoles de la Vieille Mine (Old Mines), établies avant l'arrivée des Américains dans les années 1790, gardent jusqu'aux années 1970 un français, des légendes et un pique-nique paroissial d'avant la guerre de Sécession ; en 1915, l'école impose l'anglais.", '269; 271; 273', KB)
F('vm02', 'Shibboleth (comté de Washington, Missouri)', 'famille', '1900~', -90.86, 38.0, 'h', [],
  "Maison créole en rondins des Boullins à la mine de Shibboleth, habitée par la famille Boyer.", '275', KB)
MJ = "Jetté, Melinda Marie, « Un îlot oublié de la diaspora canadienne-française : la vallée de la Willamette en Orégon »"
F('wi01', 'Astoria : les Canadiens de la Pacific Fur', 'poste', '1811/1813', -123.831, 46.188, 'c', ['Gabriel Franchère'],
  "Les premiers Canadiens français de l'Oregon accompagnaient Mackenzie ; d'autres arrivent avec la Pacific Fur Company d'Astor (Gabriel Franchère dessine Astoria en 1813). Dès 1812, chasseurs et trappeurs explorent la vallée de la Willamette.", '283; 284; 285', MJ)
F('wi02', 'Michel Laframboise, chef de brigades', 'personnage', '1830/1839', -122.8, 44.5, 'h', ['Michel Laframboise'],
  "Natif de la région de Montréal, Michel Laframboise (1790-1861) dirige dans les années 1830 plusieurs expéditions de trappe de la Baie d'Hudson vers le sud de l'Oregon et la Californie.", '285', MJ)
F('wi03', 'Champoeg et Saint-Paul : Prairie française', 'etablissement', '1827/1850', -122.97, 45.21, 'c', ['François-Xavier Matthieu', 'Adolphe Jetté'],
  "Les premiers Blancs s'installent en permanence en 1827 ; vers 1830, des familles franco-amérindiennes défrichent la Prairie française, frappées par la malaria en 1831. En 1834 elles écrivent à l'évêque de Saint-Boniface et bâtissent en 1836 à Saint-Paul la première église catholique de l'Oregon. Champoeg est rasée par les crues de 1861 et 1891.", '286; 288', MJ)
F('wi04', 'Prairie française : américanisation', 'etablissement', '1848/1900', -122.97, 45.18, 'a', [],
  "Après la création du territoire de l'Oregon (1848), les Anglo-Américains dominent ; dès 1850, les familles franco-amérindiennes s'américanisent. À la fin du siècle, seuls les nés avant 1870 parlent encore français ou chinook.", '289; 290', MJ)
MBo = "Boucher, Marc T., « Les Québécois au “pays des rêves” : nouveaux enjeux, nouvelles tendances en Californie »"
F('cf01', 'French Gulch (Californie)', 'toponymie', '1848/1852', -122.637, 40.701, 'c', [],
  "Après la découverte d'or par Pierson Reading dans la gorge de la Trinité (1848), des mineurs francophones baptisent French Gulch et y fondent l'église Sainte-Rose ; en 1852-1853, plusieurs quartiers de la région sont majoritairement francophones.", '150; 152', MBo)
F('cf02', 'Los Angeles : maires Marchesseault et Beaudry', 'personnage', '1859/1876', -118.243, 34.052, 'c', ['Damien Marchesseault', 'Prudent Beaudry', 'Victor Beaudry'],
  "Damien Marchesseault est maire de Los Angeles de 1859 à 1865 ; les Montréalais Victor et Prudent Beaudry font fortune à San Francisco avant de s'établir à Los Angeles, dont Prudent devient maire dans les années 1870, alors que son frère Jean-Louis est maire de Montréal.", '153', MBo)
F('cf03', 'Los Angeles : Cercle canadien-français', 'etablissement', '1923', -118.243, 34.052, 'a', [],
  "Fondé en 1923, le Cercle canadien-français de Californie illustre la vie associative des migrants des années 1920 ; environ 175 000 Californiens déclarent une ascendance canadienne-française en 1990.", '154', MBo)
RT = "Tremblay, Rémy, « Le Floribec éphémère »"
F('fl01', 'Floribec : Surfside et Sunny Isles', 'migration', '1945/1990', -80.122, 25.88, 'c', [],
  "Après 1945, une première vague de Québécois gagne la Floride du Sud ; vers 1970, des commerçants québécois s'installent à Surfside et Sunny Isles, quartiers floribécois qui disparaissent au début des années 1990.", '140; 141', RT)
F('fl02', 'Hollywood (Floride) : Le Soleil de la Floride', 'migration', '1983/2000', -80.15, 26.011, 'c', [],
  "La communauté se déplace vers Hollywood, où paraît depuis 1983 Le Soleil de la Floride ; la population francophone de Floride passe de 195 000 (1990) à 337 000 (2000), aux deux tiers dans Dade, Broward et Palm Beach.", '139; 143; 145', RT)

fiches = C.fiches
