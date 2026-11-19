# Documents du Drive de l'auteur (dossiers CIMARRON_NM et ILLINOIS), dépouillés le 19 novembre 2026. Corpus « Recherches », préfixe DRV (DV- est pris par un livre de la Bibliothèque archive.org).
#   Murphy, « Master of the Cimarron: Lucien B. Maxwell », New Mexico Historical Review 55-1 (1980), UNM Digital Repository
#   A Walking Tour of Old Town Cimarron, New Mexico in the 1800s (dépliant, s. d.) ; Cimarron Day Trip #2 (dépliant, s. d.)
#   Four Walking Tours of Historic Bourbonnais, Illinois (Bourbonnais Grove Historical Society et Kankakee County Historic
#   Preservation Commission, 2016)
# Les positions sont tirées des adresses données par les dépliants (certitude « approximative ») sauf mention contraire.
from commun import Corpus
MU = "Murphy, Lawrence R. (1980), « Master of the Cimarron: Lucien B. Maxwell », New Mexico Historical Review, vol. 55, no 1, p. 5-23 (UNM Digital Repository, nmhr/vol55/iss1/2)"
WT = "A Walking Tour of Old Town Cimarron, New Mexico in the 1800s (dépliant, s. d., fonds Drive de l'auteur, dossier CIMARRON_NM)"
DT = "Cimarron Day Trip #2 : Cimarron Area Ranches & the Maxwell Wildlife Refuge (dépliant, s. d., fonds Drive de l'auteur)"
BO = "Four Walking Tours of Historic Bourbonnais, Illinois, Bourbonnais Grove Historical Society et Kankakee County Historic Preservation Commission (2016), fonds Drive de l'auteur, dossier ILLINOIS"
C = Corpus('Recherches', 'DRV', MU)
F = C.F
MX, BB, LV = 'Lucien Maxwell', 'Charles Beaubien', 'Noël Le Vasseur'

# --- Cimarron (Nouveau-Mexique) : Maxwell, petit-fils de Pierre Ménard, et la famille Beaubien
F('01', "Cimarron : la maison de Lucien Maxwell, « bâtie comme une villa française »", 'etablissement', '1857~/1888', -104.9198, 36.5063, 'a', [MX, 'Luz Beaubien'],
  "Vers 1857-1858, Lucien Maxwell, petit-fils de Pierre Ménard de Kaskaskia et gendre de Charles Beaubien, quitte Rayado pour la rive sud du Cimarron, où il fait bâtir par John « Uncle Jack » Holland la maison qu'on appelle « Maxwell's Ranche ». Le voyageur William A. Bell la décrit « bâtie comme une villa française », avec cour intérieure et véranda ; Murphy y voit un souvenir des maisons de Kaskaskia, en particulier de celle du grand-père Ménard au-dessus du Mississippi. La partie est, réservée à la réception des visiteurs, brûle en janvier 1888 ; le reste en 1924.",
  '', "Site sur l'ancienne place d'Old Town Cimarron (arrêt 1 du parcours) ; la maison actuelle date des années 1950.", source=f"{MU}, p. 6-7 ; {WT}, arrêt 1")
F('02', "Cimarron : tombes de Pabla Beaubien et de la petite Verenisa Maxwell (1864)", 'famille', '1864', -104.9205, 36.5060, 'h', ['Maria Pabla Lobato', MX, 'Luz Beaubien', BB],
  "Le parcours d'Old Town signale les tombes familiales Beaubien-Maxwell : Verenisa Maxwell (1860-1864), fille de Lucien et de Luz Beaubien, y est inhumée avec sa grand-mère Maria Pabla Lobato (1811-1864), épouse du Canadien Charles « Carlos » Beaubien, qui s'était établi à Taos en 1823 et naturalisé mexicain en 1827.",
  '', "Position supposée près de la place (arrêt 2 du parcours).", source=f"{WT}, arrêt 2")
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
  "Vers 1902, Petra Beaubien, fille de Charles Beaubien et veuve de Jesús Abreu, fait bâtir à Rayado la chapelle du Sacré-Cœur, dédiée deux ans plus tard. Rayado avait été le premier établissement de la concession Beaubien-Miranda, confié par Maxwell à son beau-frère Abreu vers 1858.",
  '', "Position à l'ancienne hacienda de Rayado.", source=f"{WT}, arrêts 1 et 12")
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
fiches = C.fiches
