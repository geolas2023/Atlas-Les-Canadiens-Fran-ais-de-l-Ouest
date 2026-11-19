# Documents du Drive de l'auteur (dossiers CIMARRON_NM, ILLINOIS, CHARLES_BEAUBIEN, ETIENNE_PROVOST_AUDUBON, ALEXIS_GODEY, CHARLES_AUTOBEES, MOYSE_LAMOUREUX), dépouillés le 19 novembre 2026. Corpus « Recherches », préfixe DRV (DV- est pris par un livre de la Bibliothèque archive.org).
#   Murphy, « Master of the Cimarron: Lucien B. Maxwell », New Mexico Historical Review 55-1 (1980), UNM Digital Repository
#   A Walking Tour of Old Town Cimarron, New Mexico in the 1800s (dépliant, s. d.) ; Cimarron Day Trip #2 (dépliant, s. d.)
#   Four Walking Tours of Historic Bourbonnais, Illinois (Bourbonnais Grove Historical Society et Kankakee County Historic
#   Preservation Commission, 2016)
# Les positions sont tirées des adresses données par les dépliants (certitude « approximative ») sauf mention contraire.
from commun import Corpus
MU = "Murphy, Lawrence R. (1980), « Master of the Cimarron: Lucien B. Maxwell », New Mexico Historical Review, vol. 55, no 1, p. 5-23 (UNM Digital Repository, nmhr/vol55/iss1/2)"
WT = "A Walking Tour of Old Town Cimarron, New Mexico in the 1800s (dépliant, s. d., fonds Drive de l'auteur, dossier CIMARRON_NM)"
DT = "Cimarron Day Trip #2 : Cimarron Area Ranches & the Maxwell Wildlife Refuge (dépliant, s. d., fonds Drive de l'auteur)"
GU = "Gutiérrez, Priscilla Shannon, « Carlos Beaubien », Taos County, New Mexico (notice en ligne, v. 2008 ; fonds Drive de l'auteur, dossier CHARLES_BEAUBIEN)"
VA = "Vaugeois, Denis, « De Provost, Québec, à Provo, Salt Lake, Utah ? Des liens historiques et généalogiques », Le Devoir, 16-17 février 2002 (fonds Drive de l'auteur, dossier ETIENNE_PROVOST_AUDUBON)"
TY2 = "Tykal, Jack B., « Etienne Provost », Utah History Encyclopedia (fonds Drive de l'auteur)"
RB = "Robinson, John W. (2012), « Alexis Godey: Indian Friend or Indian Killer? », The Branding Iron (Los Angeles Corral of the Westerners), no 267-269, p. 8-16 (fonds Drive de l'auteur, dossier ALEXIS_GODEY)"
MR = "Murray, Robert A. (1978), Las Animas, Huerfano and Custer: Three Colorado Counties on a Cultural Frontier. A History of the Raton Basin, Bureau of Land Management, Colorado, Cultural Resources Series no 6 (fonds Drive de l'auteur, dossier CHARLES_AUTOBEES)"
WM = "Wilson, Miel et Bob Moore, St. Louis Probate Court Records: Court Ordered Slave Sales (relevé des livres C à V du tribunal des successions, 1828-1860 ; fonds Drive de l'auteur, dossier MOYSE_LAMOUREUX)"
BO = "Four Walking Tours of Historic Bourbonnais, Illinois, Bourbonnais Grove Historical Society et Kankakee County Historic Preservation Commission (2016), fonds Drive de l'auteur, dossier ILLINOIS"
C = Corpus('Recherches', 'DRV', MU)
F = C.F
MX, BB, LV = 'Lucien Maxwell', 'Charles Beaubien', 'Noël Le Vasseur'

# --- Cimarron (Nouveau-Mexique) : Maxwell, petit-fils de Pierre Ménard, et la famille Beaubien
F('01', "Cimarron : la maison de Lucien Maxwell, « bâtie comme une villa française »", 'etablissement', '1857~/1888', -104.9198, 36.5063, 'a', [MX, 'Luz Beaubien'],
  "Vers 1857-1858, Lucien Maxwell, petit-fils de Pierre Ménard de Kaskaskia et gendre de Charles Beaubien, quitte Rayado pour la rive sud du Cimarron, où il fait bâtir par John « Uncle Jack » Holland la maison qu'on appelle « Maxwell's Ranche ». Le voyageur William A. Bell la décrit « bâtie comme une villa française », avec cour intérieure et véranda ; Murphy y voit un souvenir des maisons de Kaskaskia, en particulier de celle du grand-père Ménard au-dessus du Mississippi. La partie est, réservée à la réception des visiteurs, brûle en janvier 1888 ; le reste en 1924.",
  '', "Site sur l'ancienne place d'Old Town Cimarron (arrêt 1 du parcours) ; la maison actuelle date des années 1950.", source=f"{MU}, p. 6-7 ; {WT}, arrêt 1")
F('02', "Cimarron : tombes de Pabla Beaubien et de la petite Verenisa Maxwell (1864)", 'famille', '1864-03/1864-06', -104.9205, 36.5060, 'a', ['Maria Pabla Lobato', MX, 'Luz Beaubien', BB],
  "Le parcours d'Old Town signale les tombes familiales Beaubien-Maxwell : Verenisa Maxwell (1860-1864), fille de Lucien et de Luz Beaubien, y est inhumée avec sa grand-mère Maria Pabla Lobato (1811-1864), épouse du Canadien Charles « Carlos » Beaubien, qui s'était établi à Taos en 1823 et naturalisé mexicain en 1827. Selon Priscilla Shannon Gutiérrez, Pabla s'installe chez Luz et Lucien à Cimarron à la mort de Carlos (février 1864) ; Verenisa meurt en mars et Pabla en juin. Leurs tombes sans inscription sont dans une clôture de fer forgé près de l'ancienne place, signalée par un panneau.",
  '', "Position estimée près de l'ancienne place (arrêt 2 du parcours).", source=f"{WT}, arrêt 2 ; {GU}")
F('03', "Cimarron : le moulin Aztec de Maxwell et l'agence indienne", 'commerce', '1860/1876', -104.9224, 36.5068, 'a', [MX],
  "Maxwell fait construire un grand moulin de pierre (achevé vers 1864, 48 000 $) qui moud pour les colons, Fort Union et l'agence des Utes et des Apaches Jicarillas installée au ranch en 1861 ; on y distribue les rations. C'est là que sa fille aînée Virginia épouse en secret l'agent indien A. S. B. Keyes, contre la volonté de son père. L'agence ferme en 1876. Le moulin, seul grand bâtiment de Maxwell conservé, est aujourd'hui un musée.",
  '', "Position estimée dans Old Town (arrêt 11 du parcours).", source=f"{MU}, p. 9-11 ; {WT}, arrêt 11")
F('04', "Cimarron : bureau de poste et relais de diligence chez Maxwell (1861)", 'etablissement', '1861/1868', -104.9198, 36.5063, 'a', [MX],
  "En 1861, le gouvernement ouvre un bureau de poste au ranch, désormais appelé Cimarron ; le premier maître de poste est Lucien Maxwell. La même année, le ranch devient un relais de la Missouri Stage Company entre Kansas City et Santa Fe, et un bureau du télégraphe s'y ouvre en 1868.",
  '', "Même point que la maison Maxwell.", source=f"{MU}, p. 12")
F('05', "Cimarron : église de l'Immaculée-Conception, don des Maxwell (1864)", 'religion', '1864', -104.9232, 36.5045, 'h', [MX, 'Luz Beaubien', 'Jean-Baptiste Lamy', 'Antoine Fourchegu'],
  "Lucien et Luz Maxwell offrent en 1864 l'église de l'Immaculée-Conception, en mémoire de leurs enfants Julian et Verenisa. Elle est bénie par l'évêque français Jean-Baptiste Lamy. Le père Antonio (Antoine) Fourchegu y officie jusqu'en 1875 après avoir logé chez les Abreu à Rayado.",
  '', "Position supposée dans Old Town (arrêt 12 du parcours).", source=f"{WT}, arrêt 12")
F('06', "Cimarron : l'hôtel St. James d'Henri Lambert (1872)", 'commerce', '1872/1880', -104.9207, 36.5051, 'c', ['Henri Lambert', 'Fred Lambert'],
  "Henri Lambert (1838-1913), cuisinier français qui avait servi Grant et Lincoln pendant la guerre de Sécession, gagne l'Ouest en 1864 pour l'or, ouvre d'abord un restaurant à Elizabethtown, puis bâtit en 1872 l'hôtel St. James à Cimarron (17 000 $). Ses 43 chambres et son saloon auraient vu au moins 26 meurtres ; les trous de balles du plafond de tôle sont encore visibles. Son fils Fred Lambert sera marshal de la ville.",
  '', "617 Collison Avenue (DAR : N36 30.304 W104 55.247).", source=f"{WT}, arrêts 7 et 9 ; carte postale « Cimarron, New Mexico », 1936 (fonds Drive, cimarron1936.jpg)")
F('07', "Rayado : chapelle du Sacré-Cœur de Petra Beaubien Abreu (v. 1902)", 'religion', '1902~/1904', -104.9283, 36.3707, 'a', ['Petra Beaubien', 'Jesús Abreu'],
  "Vers 1902, Petra Beaubien, fille de Charles Beaubien et veuve de Jesús Abreu, fait bâtir à Rayado la chapelle du Sacré-Cœur, dédiée deux ans plus tard. Rayado avait été le premier établissement de la concession Beaubien-Miranda, confié par Maxwell à son beau-frère Abreu vers 1858. Petra (morte en 1914, 32 petits-enfants) et Jesús reposent dans le cimetière familial derrière la maison Maxwell-Abreu, en face de la chapelle.",
  '', "Position à l'ancienne hacienda de Rayado.", source=f"{WT}, arrêts 1 et 12 ; {GU}")
F('08', "Ancien Fort Sumner : mort de Lucien Maxwell (25 juillet 1875)", 'evenement', '1875-07-25', -104.1947, 34.4033, 'a', [MX],
  "Après la vente de la concession en 1870 (1 350 000 $ à la Maxwell Land Grant and Railway Company), Maxwell achète l'ancien fort Sumner, dans la réserve abandonnée du sud-est du territoire, et s'y retire. Il y meurt le 25 juillet 1875 et y est inhumé.",
  '', "Position au site historique de Fort Sumner.", source=f"{MU}, p. 20 ; {DT}")

# --- Bourbonnais Grove (Illinois) : le cœur du corridor patrimonial canadien-français
F('09', "Bourbonnais Grove : cabane de François Bourbonnais père, puis maison Letourneau (1837)", 'etablissement', '1830~/1883', -87.8823, 41.1602, 'h', ['François Bourbonnais', 'Antoine Bourbonnais', 'George R. Letourneau'],
  "À la fin des années 1820 ou au début des années 1830, deux frères canadiens, François et Antoine Bourbonnais, s'établissent au bord de la Kankakee : le bosquet prend leur nom. La plus vieille maison du comté (1837) aurait été bâtie sur les fondations de la cabane de François ; George R. Letourneau (1831-1906), premier maire de Bourbonnais (1875-1876) puis maire de Kankakee, l'habite de 1854 à 1883. Elle a été déménagée en 1986 au 698 Stratford Drive East et sert de musée.",
  '', "Site d'origine : 261 North Main Street (stationnement du salon funéraire Clancy-Gernon) ; site probable seulement de la cabane.", source=f"{BO}, parcours 1, sites 1 et A")
F('10', "Bourbonnais Grove : maison de traite de Noël Le Vasseur (1834)", 'poste', '1834/1916', -87.8775, 41.1540, 'a', [LV, 'Henry Boucher', 'Dominique Bray', 'Mesheketeno', 'Watchekee'],
  "Noël Le Vasseur achète la terre au chef potawatomi Mesheketeno en 1834 et fait sans doute élever par ses associés de l'American Fur Company, Henry Boucher et Dominique Bray, une maison de traite de 24 pieds sur 32 où le chef tenait conseil. Elle abrite ensuite les premiers colons canadiens. Démontée, son bois est réemployé dans la maison Beique (1916) ; selon Vic Johnson, la maison démolie en 2008 contenait le poste entier.",
  '', "Site au sud-est du carrefour US 45-52 / Illinois 102.", source=f"{BO}, parcours 1, site B, et parcours 2, site C")
F('11', "Bourbonnais Grove : maison de brique de Noël Le Vasseur (1837)", 'famille', '1837/1885', -87.8768, 41.1545, 'a', [LV, 'Watchekee', 'Ruth Bull', 'Eleanor Franchère'],
  "En 1837, Thomas Durham bâtit en brique d'argile rouge la maison de Noël Le Vasseur (1799-1879), après une première cabane de rondins. Le Vasseur, d'abord marié à la Potawatomie Watchekee, y vit avec Ruth Bull (épousée en 1838) et leurs huit enfants, puis avec Eleanor « Fannie » Franchère. Sa veuve vend le domaine au collège Saint-Viateur ; la maison est démolie en 1885 et remplacée par la chapelle Roy (1889), détruite par le feu en 1906.",
  '', "Site à l'est du carrefour US 45-52 / Illinois 102, sur l'actuel campus d'Olivet Nazarene.", source=f"{BO}, parcours 2, site B")
F('12', "Bourbonnais : église de la Maternité-de-la-Bienheureuse-Vierge-Marie (chapelle de 1841)", 'religion', '1841/1858', -87.8756, 41.1571, 'c', [LV, 'Charles Chiniquy', 'Isidore-Antoine Lebel'],
  "L'église de pierre est sur le site d'une chapelle de rondins dédiée à saint Léon (1841), sur une terre cédée par Noël Le Vasseur. La paroisse est érigée en 1847 ; l'église de bois brûle en 1853, sous le père Charles Chiniquy, et le curé Isidore-Antoine Lebel fait élever l'église de calcaire achevée en 1858. Première église des Clercs de Saint-Viateur aux États-Unis et première mission de la Congrégation de Notre-Dame.",
  '', "308 East Marsile Street.", source=f"{BO}, parcours 2, site 1")
F('13', "Bourbonnais Grove : première école de rondins (1837-1848)", 'etablissement', '1837/1848', -87.8760, 41.1500, 'a', ['Thomas Durham', 'Joseph Lesage'],
  "École d'abonnement d'un étage et demi bâtie en 1837 et ouverte de 1838 à 1848 ; elle sert aussi aux prédicateurs méthodistes itinérants. En 1848, le Canadien Joseph Lesage l'achète pour en faire sa maison. Les rondins, mis au jour en 2011, ont été démontés pour être remontés près du musée Letourneau.",
  '', "493 South Main Street.", source=f"{BO}, parcours 3, site A")
F('14', "Bourbonnais Grove : Joseph Legris, revenu des mines d'or de Californie (1857)", 'migration', '1857', -87.8770, 41.1520, 'h', ['Joseph Legris', 'Gérasime Legris'],
  "Enrichi dans les mines d'or de Californie, Joseph Legris revient à Bourbonnais Grove, épouse Cléophile Sylvestre et bâtit en 1857 une cabane de rondins, cuisine de la maison actuelle. Ses fils fondent deux banques à Kankakee ; Mgr Gérasime Legris enseigne la théologie au collège Saint-Viateur et Frédéric Legris préside le conseil du village pendant 26 ans.",
  '', "Adresse non lue dans l'OCR du dépliant (parcours 3, South Main Street) : position supposée.", source=f"{BO}, parcours 3")
F('15', "Bourbonnais Grove : rive de la Kankakee, village de Mesheketeno", 'etablissement', '1830~', -87.8890, 41.1610, 'h', ['Mesheketeno', LV],
  "Le parc Riverfront marque la partie ouest du village potawatomi de Mesheketeno, fréquenté surtout à la saison des sucres, à mi-chemin du « Bourbonnais Grove », bosquet de douze milles sur un, du parc d'État de la Kankakee au parc Cobb de Kankakee. C'est à ce chef que Le Vasseur achète sa terre en 1834.",
  '', "1071-1081 Canterbury Lane ; position estimée.", source=f"{BO}, parcours 4, site 1")

# --- Charles (Carlos) Beaubien, d'après Gutiérrez ; Étienne Provost, d'après Vaugeois (Le Devoir, 2002)
F('16', "Taos : maison Beaubien sur le « Camino de Beaubien » (rue Ledoux)", 'famille', '1838~/1864', -105.5770, 36.4058, 'a', [BB, 'Maria Pabla Lobato'],
  "Vers 1838, la famille grandissante de Carlos Beaubien quitte le magasin du côté sud de la place pour une maison plus vaste au sud de l'église de Guadalupe, sur la rue appelée alors Camino de Beaubien (aujourd'hui rue Ledoux) ; les plans Sanborn portent encore la graphie « Bovien ». C'est dans une grange voisine que Narciso Beaubien est massacré le 19 janvier 1847.",
  '', "Position estimée au milieu de la rue Ledoux.", source=GU)
F('17', "Taos, place de Guadalupe : les tombes perdues de Carlos et de Narciso Beaubien", 'famille', '1847-01/1864-02-06', -105.5750, 36.4063, 'a', [BB, 'Narciso Beaubien'],
  "Carlos Beaubien meurt à Taos le 6 février 1864, à 64 ans, d'une pneumonie ; sa succession est évaluée à 63 705 $. Lui et son fils Narciso, tué en 1847, avaient été inhumés au cimetière de l'ancienne église de Guadalupe. Après l'incendie de l'église, reconstruite plus au nord-ouest, le cimetière est devenu un stationnement : les restes, aux tombes illisibles ou brûlées, n'ont pas été réinhumés et gisent sous le pavé de la place.",
  '', "Position à la place de Guadalupe (Camino de la Placita), au sud-est de l'église actuelle.", source=GU)
F('18', "Los Luceros : le juge Beaubien tient audience pendant la révolte de Taos (janvier 1847)", 'evenement', '1847-01', -106.0432, 36.1197, 'a', [BB],
  "Nommé juge par Kearny en 1846, Carlos Beaubien siège à Los Luceros (et non à Tierra Amarilla, comme on l'écrit souvent) lorsque éclate la révolte du 19 janvier 1847 ; il échappe ainsi au sort de Charles Bent. Au procès qui suit, il prononce lui-même les condamnations à mort des meurtriers de son fils : « Muerto, muerto, muerto ».",
  '', "Position au site historique de Los Luceros.", source=GU)
F('19', "San Luis et Costilla : la concession Sangre de Cristo de Beaubien (1843)", 'etablissement', '1843/1864', -105.4236, 37.2009, 'a', [BB, 'Narciso Beaubien', 'Stephen Louis Lee'],
  "En 1843, Beaubien obtient du gouverneur Armijo, au nom de son fils Narciso et de Stephen Louis Lee, la concession Sangre de Cristo, au sud de la vallée de San Luis (rivières Trinchera, Culebra et Costilla). Il y attire des familles de Taos : San Luis et Costilla en naissent. Après la mort de Narciso et de Lee en 1847, la concession passe à son nom ; William Gilpin en revendiquera ensuite près d'un million d'acres.",
  '', "Point placé à San Luis (Colorado).", source=GU)
F('20', "Fort Sumner : Pablo Beaubien, éleveur, et la maison de Peter Maxwell (1870-1881)", 'famille', '1870/1881-07-14', -104.1955, 34.4042, 'a', ['Pablo Beaubien', 'Peter Maxwell', MX, 'Luz Beaubien'],
  "En 1870, Pablo Beaubien, dernier fils de Carlos, suit les Maxwell à Fort Sumner après leur avoir vendu ses droits d'héritier sur la concession (3 500 $). Il y épouse Rebecca Abreu et devient un éleveur de moutons prospère. C'est dans la maison de son neveu Peter Maxwell, petit-fils de Beaubien, que Billy the Kid est abattu le 14 juillet 1881.",
  '', "Position estimée sur le site de l'ancien fort.", source=GU)
F('21', "Provo (Utah) : la ville porte, écourté, le nom d'Étienne Provost (1849)", 'toponymie', '1849', -111.6585, 40.2338, 'c', ['Etienne Provost'],
  "En 1849, une trentaine de familles mormones conduites par John S. Higbee s'établissent le long de la rivière que le récit de Frémont (1845) appelait « Provost Fork ». La ville garde le nom du Chamblyen Étienne Provost, premier ou l'un des premiers Blancs au Grand Lac Salé (1824), « en y laissant les deux dernières lettres », note Denis Vaugeois.",
  '', "", source=f"{VA} ; {TY2}")
F('22', "Saint-Charles : « le vieux Provost » rentre à pied à Saint-Louis (18 octobre 1843)", 'evenement', '1843-10-18', -90.4812, 38.7839, 'a', ['Etienne Provost', 'Clément Salle dit Lajoie', 'John James Audubon'],
  "Au retour de l'expédition du haut Missouri, Audubon note le 18 octobre 1843 à Saint-Charles le départ à pied de son guide, complètement ivre, pour Saint-Louis, où l'attendent sa femme, sa fille et son beau-frère Clément Salle dit Lajoie, associé de sa taverne. Pour près de cinq mois de service, Provost reçoit 214 $ d'Audubon et 78,33 $ de l'Upper Missouri Outfit. Ses chasseurs : Bonaventure Le Brun, Charles Primeau, Alexis Bombardier et le pilote Jean-Baptiste La Barge.",
  '', "À vérifier : Vaugeois nomme l'épouse « Marie Rose Salle Dupuis » et le beau-frère « Clément Salle dit Lajoie », alors que le registre de 1850 porte « Maria Rose Lombard » et l'annuaire de 1845 un « Clement Lambert, coffee-house » à l'angle des rues Second et Lombard (fiche PV-05).", source=VA)

# --- Alexis Godey (v. 1818-1889), né à Saint-Louis de parents canadiens, d'après Robinson (2012)
G = 'Alexis Godey'
F('23', "Mule Hill (San Pasqual) : Godey, Beale et Carson percent les lignes (décembre 1846)", 'evenement', '1846-12', -117.0700, 33.0870, 'a', [G, 'Kit Carson', 'Edward F. Beale'],
  "Après la défaite de Kearny à San Pasqual (6 décembre 1846), ses hommes sont cernés sur « Mule Hill ». Godey, Beale et Carson se glissent de nuit à travers les lignes californiennes pour demander secours à Stockton à San Diego. Godey est pris au retour par les lanciers d'Andrés Pico, qui le traitent avec égards et le libèrent à Frémont lors de la capitulation de Cahuenga (13 janvier 1847).",
  '', "Position au site historique de Mule Hill, près d'Escondido.", source=RB)
F('24', "Tejon : Godey interprète de la réserve Sebastian (1853)", 'personnage', '1853/1863', -118.8930, 34.8730, 'a', [G, 'Edward F. Beale'],
  "En 1853, Edward F. Beale, surintendant des Indiens de Californie, engage Godey comme interprète à la réserve Sebastian (ou de Tejon), à l'entrée du canyon de Tejon. Beale écrira que, grâce à sa connaissance du pays et à son influence sur les tribus, il put maintenir la paix dans la vallée de San Joaquin. Le contremaître José Jesús López dira de lui qu'il était « lui-même un Indien » à bien des égards.",
  '', "Position à l'entrée du canyon de Tejon.", source=RB)
F('25', "Rancho San Emigdio : Godey régisseur et « Pueblo de San Emigdio » (1855-1883)", 'etablissement', '1855/1883', -119.1750, 35.0003, 'a', [G, 'John C. Frémont', 'Edward F. Beale'],
  "Frémont achète en 1851 une demi-part du rancho San Emigdio (17 709 acres) et en confie l'exploitation à Godey, qui y vit de 1855 à 1883, fournit bœuf et mouton à Fort Tejon (1855-1861) et développe le « Pueblo de San Emigdio » : en 1872, une cinquantaine de paisanos et environ 150 Indiens, bergers et vachers. À la vente du rancho à J. F. Haggin (1883), Godey reçoit 2 000 $ en or.",
  '', "Position à l'entrée du canyon de San Emigdio.", source=RB)
F('26', "Vallée de Cuyama : l'adobe de Godey et la légende de l'empoisonnement", 'evenement', '1865~', -119.6000, 34.9300, 'h', [G],
  "Vers le milieu des années 1860, Godey fait paître un millier de bêtes au nord de la vallée de Cuyama et y bâtit un petit adobe. En 1933, Mark R. Harrington l'accuse d'y avoir empoisonné 42 Indiens ; l'enquête de Frank Latta (1939) recueille des témoignages qui réfutent l'accusation. Robinson rattache la rumeur au crime d'un vacher surnommé « El Chihuahua », qui tua une Indienne et son mari avant de fuir au Mexique.",
  '', "Position supposée au nord de la vallée.", source=RB)
F('27', "Bakersfield : Belmont Grove, le « Godey Tract » et la tombe de Godey (1883-1889)", 'famille', '1883/1889-01-19', -118.9925, 35.3713, 'a', [G],
  "Établi à Bakersfield en 1883, Godey bâtit sur la 19e Rue une grande maison, Belmont Grove, et lotit les quatre-vingts acres voisins (le « Godey Tract »). Il meurt à l'hôpital des Sœurs de Los Angeles le 19 janvier 1889, à 71 ans, et est inhumé au cimetière Union de Bakersfield près de son fils Alexis Godey fils, mort en 1877.",
  '', "Point placé au cimetière Union de Bakersfield ; la maison de la 19e Rue n'est pas localisée.", source=RB)

# --- Bassin de Raton (Colorado), d'après Murray
F('28', "Vallée de Wet Mountain : une huitaine de familles françaises (Garnier, Mercier, Albert) vers 1870", 'migration', '1870~/1874', -105.4700, 38.1300, 'h', ['Garnier', 'Mercier', 'Albert'],
  "Au moment où la colonie allemande de Carl Wulsten s'installe dans la vallée de Wet Mountain (1870-1872), environ huit familles d'origine française, dont les Garnier, Mercier et Albert, s'établissent le long de la bordure ouest de la vallée, sans organisation collective, comme quelques familles mormones venues du Lac Salé sur le ruisseau Taylor.",
  '', "Position supposée sur la bordure ouest de la vallée, au pied des Sangre de Cristo ; l'origine (France, Canada ?) reste à préciser.", source=f"{MR}, p. 47")

# --- Saint-Louis : ventes d'esclaves ordonnées par le tribunal des successions (porte du palais de justice)
F('29', "Saint-Louis, palais de justice : vente des esclaves de la succession d'Auguste Chouteau (1830)", 'evenement', '1830-09-15', -90.1892, 38.6255, 'a', ['Auguste Chouteau', 'Thérèse Cerré Chouteau', 'Pierre Chouteau'],
  "La succession du fondateur de Saint-Louis, Auguste Chouteau (mort en 1829), compte 36 esclaves ; 12 sont remis directement à sa veuve, Thérèse Cerré. Les autres (Peter, 102 ans, Ceres, Titia, Catiche, Rose, Zabette, Pélagie, Marguerite, des enfants de deux à quatorze ans...) sont vendus à la porte du palais de justice le 15 septembre 1830, pour 10 838,88 $ au total, partagés entre la veuve et les sept enfants. La même année, Patrick, esclave de la succession de Joseph Brazeau qui s'était enfui au Canada en 1829 et était revenu par vapeur de La Nouvelle-Orléans, est mis en vente parce qu'« il s'enfuira encore ».",
  '', "Point placé au palais de justice (Old Courthouse), lieu des ventes judiciaires ; le bâtiment actuel a été élevé de 1839 à 1862 sur le même îlot.", source=f"{WM}, livres C (p. 235, 282, 313-316, 356) et D (p. 1, 53-54, 112)")
F('30', "Saint-Louis, palais de justice : Moïse Lamoureux achète Thalie (1846-1847)", 'evenement', '1846-09-18/1847-06-18', -90.1892, 38.6255, 'a', ['Moïse Lamoureux', 'Didier Guyon', 'Josephine Guyon'],
  "À la vente des esclaves de la succession de Josephine Guyon, ordonnée le 18 septembre 1846, Mary (40 ans) est adjugée 190 $ à Didier Guyon et sa fille Thalie (20 ans) 475 $ à Moïse Lamoureux, Chamblyen du Frenchtown comme Étienne Provost ; la vente est approuvée le 18 juin 1847. Une enfant de trois ans figure aussi à l'inventaire.",
  '', "Point placé au palais de justice, à la porte est (« eastern door ») où se tenaient les ventes.", source=f"{WM}, livres K (p. 380, 411) et L (p. 117)")
fiches = C.fiches
