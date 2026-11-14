# Corpus « Nouvelle-Angleterre » : l'émigration canadienne-française vers les villes de filatures.
#   Vermette, David (2018), A Distinct Alien Race: The Untold Story of Franco-Americans, Montréal, Baraka Books.
#   MacDonald, William (1898), « The French Canadians in New England », Quarterly Journal of Economics, 12 (3), p. 245-279.
#   Belisle, Alexander (1907), The French Canadians in the Development of the United States, Worcester Society of Antiquity, vol. XXIII.
from commun import Corpus
VE = "Vermette, David (2018), A Distinct Alien Race: The Untold Story of Franco-Americans. Industrialization, Immigration, Religious Strife, Montréal, Baraka Books"
MD = "MacDonald, William (1898), « The French Canadians in New England », The Quarterly Journal of Economics, vol. 12, no 3, p. 245-279"
BE = "Belisle, Alexander (1907), « The French Canadians in the Development of the United States », Proceedings of the Worcester Society of Antiquity, vol. XXIII"
C = Corpus('Nouvelle-Angleterre', 'NA', VE)
F = C.F

# ---- Vermette 2018
F('v01', 'Burlington : Le Patriote canadien de Ludger Duvernay', 'commerce', '1839', -73.212, 44.476, 'c', ['Ludger Duvernay'],
  "Des réfugiés des Rébellions de 1837-1838 forment de petits noyaux canadiens au Vermont et dans l'État de New York ; à Burlington, Ludger Duvernay fonde en 1839 le premier journal canadien de langue française aux États-Unis.", '92')
F('v02', 'Chicopee : recrutement de la Dwight Manufacturing', 'migration', '1859', -72.608, 42.149, 'c', ['J. M. Boynton'],
  "Dès 1859, avant la guerre de Sécession, la Dwight Manufacturing Company de Chicopee charge un agent de recruter de la main-d'œuvre au Québec, payé quatre dollars par tête.", '104')
F('v03', 'Lowell : recrutement de Samuel Marin', 'migration', '1865', -71.316, 42.633, 'c', ['Samuel Marin'],
  "Peu de Franco-Américains à Lowell avant 1865 ; au lendemain de la guerre, les manufacturiers engagent le Canadien Samuel Marin pour recruter au Québec. La part des immigrants à la filature Hamilton était passée de moins de 4 % (1836) à plus de 60 % (1860).", '98; 105')
F('v04', 'Grand Tronc : de Montréal à Lewiston et Portland', 'migration', '1853/1890~', -70.214, 44.1, 'a', [],
  "L'extension du Grand Tronc à partir de 1853 accélère l'exode : les trains transportent directement des familles de Montréal, Saint-Hyacinthe ou Sherbrooke vers Lewiston et Portland. Les Franco-Américains, 37 420 en Nouvelle-Angleterre en 1860, sont parmi les rares immigrants arrivés par le rail.", '97; 106')
F('v05', 'Manchester : Philippe Lemay, ouvrier du textile', 'migration', '1864', -71.463, 42.995, 'c', ['Philippe Lemay'],
  "Arrivé du Québec avec sa famille en 1864, Philippe Lemay raconte son parcours d'ouvrier du textile au Federal Writers' Project dans les années 1930.", '105')
F('v06', 'Brunswick (Maine) : premières familles et filature Cabot', 'migration', '1844/1860', -69.965, 43.917, 'c', [],
  "Aucun Canadien à Brunswick au recensement de 1840 ; un premier, entré par Derby Line en 1838, dirait y être arrivé en 1844. En 1860, une quinzaine de familles venues surtout de la vallée du Richelieu travaillent à la filature Cabot, en comptant retourner sur leurs terres.", '118; 120')
F('v07', 'Brunswick : le quartier français', 'etablissement', '1870/1900', -69.963, 43.914, 'c', [],
  "Plus de 65 familles en 1870 (près d'un habitant sur dix), 1 199 personnes en 1880 et 2 556 en 1900 ; dans les années 1920, la ville est à moitié franco-américaine. En 1880, 96 % des actifs travaillent à la filature ou comme journaliers.", '122; 124; 127')
F('v08', "L'Islet, foyer d'origine des ouvriers de Brunswick", 'migration', '1866/1880', -70.367, 47.11, 'c', ['Pierre Morin'],
  "Après l'agrandissement de la filature Cabot (1866), des mariés de L'Islet déclarent Brunswick comme résidence (1867). Le comté de L'Islet et trois comtés voisins de la Côte-du-Sud deviennent la principale source des familles. Né à L'Islet en 1847, Pierre Morin préside la société de naturalisation de Brunswick (1884).", '123; 183')
F('v09', "L'Islet en 1852-1861 : moulins et salaires", 'commerce', '1852/1861', -70.367, 47.11, 'c', ['Eugène Casgrain', 'Leonard Ennis'],
  "Selon les recensements canadiens, L'Islet compte des moulins du seigneur Eugène Casgrain et de l'ingénieur Leonard Ennis ; une cardeuse y gagne 4 $ par mois en 1861, alors que la filature Cabot offrait 4 à 4,50 $ par semaine dès 1853.", '186; 190')
F('v10', 'Brunswick : grèves à la filature Cabot', 'evenement', '1881-08/1898', -69.965, 43.917, 'c', [],
  "Au moins quatre grèves entre 1881 et 1887 ; en août 1881, quinze garçons de 8 à 14 ans débraient en apprenant que Lisbon et Lewiston paient mieux. En 1898, Brunswick se joint à la grande grève régionale, qui dure plus de deux mois.", '113; 115')
F('v11', 'Suncook : grève de 1881', 'evenement', '1881', -71.453, 43.13, 'c', [],
  "À Suncook (New Hampshire), des Franco-Américains font grève contre trois filatures en 1881 ; mal organisée, la grève pousse des employés à quitter la ville.", '114')
F('v12', 'Biddeford-Saco : grève et crise de 1898', 'evenement', '1898', -70.453, 43.492, 'c', [],
  "Pendant la crise cotonnière de 1898, les grèves frappent New Bedford, Biddeford et Saco ; la presse décrit la misère des familles ouvrières de Biddeford.", '115; 158')
F('v13', 'Brunswick : épidémie de diphtérie', 'evenement', '1886', -69.963, 43.914, 'c', [],
  "À l'été 1886, une diphtérie meurtrière ravage le quartier français ; le curé de Saint-Jean dit avoir enterré plus d'enfants qu'il n'en a baptisé depuis janvier. Le Conseil d'hygiène du Maine blâme la gestion des logements par la compagnie Cabot.", '131; 135; 143')
F('v14', 'Brunswick : paroisse Saint-Jean', 'religion', '1877/1927', -69.966, 43.913, 'a', [],
  "Sans être officiellement nationale, la paroisse Saint-Jean reste massivement franco-américaine jusqu'au milieu du XXe siècle ; son livre du cinquantenaire (1927) honore ses soldats de la Grande Guerre.", '125; 279')
F('v15', 'Lowell : le Petit Canada', 'etablissement', '1882', -71.31, 42.645, 'a', [],
  "En 1882, le Bureau des statistiques du travail du Massachusetts décrit le Petit Canada de Lowell, bâti sur des remblais insalubres.", '145')
F('v16', 'Massachusetts : le rapport Wright (« Chinois de l\'Est »)', 'evenement', '1881', -71.06, 42.358, 'c', ['Carroll D. Wright', 'Ferdinand Gagnon'],
  "Dans son rapport de 1881, Carroll D. Wright, directeur du Bureau des statistiques du travail, qualifie les Canadiens français de « Chinois des États de l'Est ». Les chefs franco-américains, dont Ferdinand Gagnon, obtiennent une audience publique pour le réfuter.", '205; 206')
F('v17', 'Worcester : Ferdinand Gagnon et la convention de 1870', 'personnage', '1870-09', -71.802, 42.263, 'c', ['Ferdinand Gagnon'],
  "Né à Saint-Hyacinthe en 1849, le journaliste Ferdinand Gagnon s'installe à Worcester. En septembre 1870, la convention générale des Canadiens des États-Unis s'y tient ; un recensement paroissial de 1871 n'y trouve que 57 propriétaires au Québec sur 562 familles.", '173; 201; 236')
F('v18', 'Nashua : convention générale de 1888', 'evenement', '1888', -71.468, 42.765, 'c', ['Edmond Mallet'],
  "À la convention générale de Nashua (1888), le major Edmond Mallet, héros de la guerre de Sécession, défend une Amérique formée de toutes les nationalités immigrées.", '203')
F('v19', 'Waterville : baptistes franco-américains', 'religion', '1893', -69.632, 44.552, 'a', [],
  "En 1893, de petites congrégations baptistes franco-américaines existent notamment à Worcester et à Waterville ; le séminaire de Newton ouvre un département français pour former des missionnaires.", '227')
F('v20', 'Brunswick : contre la loi « Corporation Sole »', 'religion', '1909-10-04/1909-10-05', -69.965, 43.917, 'c', [],
  "La loi de 1887 fait de l'évêque de Portland le seul propriétaire des biens d'Église au Maine. Les 4 et 5 octobre 1909, des Franco-Américains de tout l'État se réunissent à Brunswick et nomment un comité pour la combattre.", '232')
F('v21', 'Portland : quartier général du Ku Klux Klan', 'evenement', '1924', -70.255, 43.661, 'c', [],
  "En 1924, le Klan inaugure à Portland un quartier général avec auditorium de 4 000 places ; une modification de la charte municipale soutenue par le Klan réduit le poids politique des quartiers catholiques et juifs.", '274; 283')
F('v22', 'Greenville (Maine) : bûcherons IWW contre le Klan', 'evenement', '1924-02', -69.59, 45.46, 'c', [],
  "En février 1924, par grand froid, des bûcherons franco-américains membres des IWW refoulent quarante Klansmen cagoulés à Greenville.", '280')
F('v23', 'Biddeford : défense du pont contre le Klan', 'evenement', '1924-09', -70.444, 43.497, 'c', [],
  "En septembre 1924, des Franco-Américains défendent Biddeford contre le Klan qui s'élance sur le pont depuis Saco.", '281')
F('v24', 'Lewiston : bombe du Klan', 'evenement', '1924', -70.215, 44.1, 'c', [],
  "En 1924, le Klan fait exploser une bombe dans la ville très franco-américaine de Lewiston pour célébrer sa victoire présumée aux primaires républicaines.", '281')
F('v25', 'Woonsocket : Lucien Sansouci et La Tribune', 'evenement', '1924', -71.515, 42.003, 'c', ['Lucien Sansouci'],
  "Lucien Sansouci, reporter de La Tribune de Woonsocket, affirme avoir été marqué au fer par des Klansmen qui l'avaient surpris à observer un rassemblement (1924).", '281')
F('v26', 'Brunswick : réunion du Klan à l\'hôtel de ville', 'evenement', '1923-12-19', -69.965, 43.917, 'c', [],
  "Le 19 décembre 1923, le Klan tient une réunion à l'hôtel de ville de Brunswick (7 261 habitants en 1920) ; en 1930, la Saint-Jean-Baptiste y est de nouveau fêtée en grande pompe.", '286; 290')
F('v27', 'Woonsocket : grève générale du textile', 'evenement', '1934', -71.515, 42.003, 'c', [],
  "Lors de la grève générale de 1934, 10 000 ouvriers affrontent la Garde nationale à Woonsocket ; au moins un mort.", '296')
F('v28', 'Lewiston : déclin et exode', 'migration', '1927/1929', -70.215, 44.1, 'c', [],
  "Avec le départ des filatures vers le Sud, la population franco-américaine de Lewiston baisse de 8,6 % entre 1927 et 1929.", '297')
F('v29', 'Fall River : fermetures des années 1950', 'evenement', '1954', -71.155, 41.701, 'c', [],
  "Au début des années 1950, la moitié des emplois du textile de la Nouvelle-Angleterre disparaissent (1954) ; Fall River, qu'on disait troisième ville francophone, est durement touchée.", '298')
F('v30', 'Brunswick : fermeture de la filature Verney', 'evenement', '1955-06', -69.965, 43.917, 'c', ['Gilbert Verney'],
  "Vendue en 1942 à Gilbert Verney de Manchester, l'ancienne filature Cabot ferme définitivement en juin 1955.", '305; 307')
F('v31', 'Lewiston : Camille Lessard-Bissonnette', 'personnage', '1904', -70.215, 44.1, 'c', ['Camille Lessard-Bissonnette'],
  "En 1904, la journaliste et romancière Camille Lessard-Bissonnette vient du Québec à Lewiston avec sa famille.", '145')

# ---- MacDonald 1898
G = lambda *a, **k: F(*a, source=MD, **k)
G('m01', 'Burlington et Swanton : premières paroisses françaises', 'religion', '1850/1856', -73.212, 44.476, 'c', [],
  "Les paroisses de Burlington (1850) et de Swanton (1856), au Vermont, comptent parmi les premières paroisses canadiennes-françaises de la Nouvelle-Angleterre.", '248')
G('m02', 'Connecticut : première paroisse canadienne', 'religion', '1880', -71.88, 41.92, 'h', [],
  "Le Connecticut est atteint en dernier : sa première paroisse canadienne-française n'est organisée qu'en 1880, alors que trente-six existent déjà ailleurs en Nouvelle-Angleterre.", '249',
  "Point régional (nord-est du Connecticut).")
G('m03', 'Nouvelle-Angleterre : 331 804 Canadiens français en 1890', 'migration', '1890', -71.5, 42.6, 'h', [],
  "Le recensement de 1890, premier à les distinguer, compte 331 804 Canadiens français en Nouvelle-Angleterre, dont 93 459 nés aux États-Unis ; 58 % des actifs travaillent dans les manufactures. L'immigration, à son sommet de 1875 à 1890, ralentit en 1897.", '257; 262')
G('m04', 'Manchester : seule grande ville où les Canadiens dépassent les Irlandais', 'etablissement', '1890', -71.463, 42.995, 'c', [],
  "Parmi les villes de plus de 25 000 habitants, Manchester est en 1890 la seule où les Canadiens français sont plus nombreux que les Irlandais ; à Fall River et New Bedford, les deux groupes s'équilibrent.", '266')
G('m05', 'Grosvenordale (Connecticut)', 'etablissement', '1881', -71.9, 41.98, 'a', ['Ferdinand Gagnon'],
  "Cité par Gagnon devant le Bureau du travail en 1881 : Grosvenordale et Mechanicsville comptent 2 400 Canadiens, dont douze propriétaires seulement.", '269')

# ---- Belisle 1907
H = lambda *a, **k: F(*a, source=BE, **k)
H('b01', 'Milwaukee : Salomon Juneau', 'etablissement', '1818', -87.906, 43.039, 'c', ['Salomon Juneau'],
  "Parti de chez lui à 18 ans en 1815, Salomon Juneau s'établit en 1818 au bord de la rivière Milwaukee ; fondateur de Milwaukee, longtemps appelée Juneau City.", '5')
H('b02', 'Prairie du Chien et Dubuque : Julien Dubuque', 'poste', '1785/1810', -90.664, 42.5, 'a', ['Julien Dubuque'],
  "Établi à 23 ans à Prairie du Chien (1785), Julien Dubuque obtient des Mesquakies des terres minières confirmées en 1806 ; mort en 1810, les Autochtones entretiennent longtemps une lampe sur sa tombe.", '6')
H('b03', 'Mendota : Joseph Renville et Jean-Baptiste Faribault', 'personnage', '1812/1846', -93.165, 44.884, 'a', ['Joseph Renville', 'Jean-Baptiste Faribault'],
  "Joseph Renville commande des Sioux en 1812 et protège les voyageurs (Frémont, 1837) ; mort en 1846. Né en 1774, J.-B. Faribault refuse de combattre sous le drapeau anglais et est fait prisonnier à Prairie du Chien.", '7')
H('b04', 'Chicago : la famille Beaubien', 'famille', '1812/1833', -87.624, 41.885, 'a', ['Jean-Baptiste Beaubien', 'Médard Beaubien'],
  "Né à Détroit en 1785, le colonel Jean-Baptiste Beaubien s'établit à Chicago ; il y fonde un club littéraire (hiver 1831-1832). Son frère Médard préside le premier conseil municipal en 1833.", '12; 13')
H('b05', 'Kaskaskia : mort de Pierre Ménard', 'religion', '1844', -89.914, 37.92, 'a', ['Pierre Ménard'],
  "Né au Québec en 1767, Pierre Ménard, associé (1808) d'une grande firme de traite et premier lieutenant-gouverneur de l'Illinois (1818), meurt à Kaskaskia en 1844.", '11; 12')
H('b06', 'Kansas City : Jacques Fournier, centenaire', 'personnage', '1871', -94.627, 39.114, 'a', ['Jacques Fournier'],
  "Mort à Kansas City en 1871, Jacques Fournier aurait vu la bataille des plaines d'Abraham (1759), servi Lewis et Clark et combattu pour les États-Unis en 1812.", '15; 16', "Récit traditionnel non vérifié par l'auteur.")
H('b07', 'Galveston : Michel Brindamour Ménard', 'etablissement', '1836~', -94.797, 29.301, 'c', ['Michel Brindamour Ménard'],
  "Signataire de la déclaration d'indépendance du Texas, Michel B. Ménard achète pour 30 000 $ un vaste terrain à la jeune république et fonde Galveston.", '16', "Belisle date la déclaration de 1846 ; elle est de 1836.")
H('b08', 'Los Angeles : Prudent Beaudry', 'personnage', '1852', -118.243, 34.052, 'c', ['Prudent Beaudry'],
  "Établi à Los Angeles en 1852, Prudent Beaudry contribue plus que quiconque au développement de la ville.", '17')

fiches = C.fiches
