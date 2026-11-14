# L'Illinois français et l'archipel du Midwest : onze sources (FR / EN)
import json, html, re
A = '/home/claude/atlas-aubry/'
PEO = json.load(open('/home/claude/build/peoria_data.json', encoding='utf-8'))

S = {  # sources
 'louder': "Louder, D., Morissonneau, C. et Waddell, E. (1979), « Du continent perdu à l'archipel retrouvé : le Québec et l'Amérique française », Cahiers de géographie du Québec, 23 (58), p. 5-13",
 'biays': "Biays, P. (1986), compte rendu de Louder et Waddell (dir.), Du continent perdu à l'archipel retrouvé (1983), Annales de géographie, 95 (527), p. 116-118",
 'kennedy': "Kennedy, J. (1962), Why Illinois Was French, Chicago, National Society of the Colonial Dames of America in the State of Illinois",
 'east': "East, E. E. (1933), The Inhabitants of Three French Villages at Peoria, Illinois: A Directory, Peoria, Peoria Historical Press",
 'kantowicz': "Kantowicz, E. R. (1982), « A Fragment of French Canada on the Illinois Prairies », Journal of the Illinois State Historical Society, 75 (4), p. 263-276",
 'cormier': "Cormier, L.-P. (1957), « La presse française de l'Illinois », Revue d'histoire de l'Amérique française, 11 (3), p. 361-392",
 'kankakee': "Kankakee Centennial, 1853-1953: Souvenir (1953), Kankakee",
 'viator': "Thirty-Third Annual Catalogue of St. Viateur's College, Bourbonnais, Kankakee County, Illinois, 1900-1901 (1901), Bloomington",
 'ifm1': "IFMidwest Magazine, vol. 2, no 2 (été 2009), « Francophone Roots in the Midwest », Grand Forks, University of North Dakota",
 'ifm2': "IFMidwest Magazine, vol. 3, no 1 (printemps 2010), « French Living Heritage in the Midwest », Grand Forks, University of North Dakota",
 'ifm3': "IFMidwest Magazine, vol. 4, no 1 (automne 2012), « Franco-Fête », Grand Forks, University of North Dakota",
}
# lieux : id, lon, lat, catégorie, date (tri), nom fr, nom en, texte fr, texte en, source
C = {'colonial': ('#8b2e1f', "Nouvelle-France (1673-1763)", "New France (1673-1763)"),
     'peoria': ('#b0451c', "Les villages français de Peoria", "The French villages of Peoria"),
     'kankakee': ('#3e5f7a', "Le « Petit Canada » de la Kankakee", "The Kankakee “Little Canada”"),
     'presse': ('#6b7a2f', "La presse française", "The French press"),
     'midwest': ('#7a3e6b', "Patrimoine francophone du Midwest", "Francophone heritage of the Midwest")}
L = [
 ('kaskaskia', -89.915, 37.922, 'colonial', 1703, "Kaskaskia", "Kaskaskia", "Village fondé en 1703 par le jésuite Gabriel Marest auprès des Kaskaskias ; gouvernement français en place dès 1715, archives judiciaires retrouvées en 1906.", "Village founded in 1703 by the Jesuit Gabriel Marest among the Kaskaskia; French government in place by 1715, court records rediscovered in 1906.", 'kennedy'),
 ('chartres', -90.158, 38.085, 'colonial', 1723, "Fort de Chartres", "Fort de Chartres", "Premier fort bâti par Boisbriand en 1723, poste le plus occidental du domaine royal ; rattaché à la Louisiane en 1717. Ses commandants : Boisbriand, Bertet, Pierre d'Artaguiette (brûlé par les Chicachas en 1736).", "First fort built by Boisbriand in 1723, the westernmost outpost of the royal domain; attached to Louisiana in 1717. Its commanders: Boisbriand, Bertet, Pierre d'Artaguiette (burned by the Chickasaw in 1736).", 'kennedy'),
 ('crevecoeur', -89.60, 40.65, 'colonial', 1680, "Fort Crèvecœur", "Fort Crèvecœur", "Bâti par La Salle sur l'Illinois en 1680, de courte durée.", "Built by La Salle on the Illinois in 1680, short-lived.", 'kennedy'),
 ('stlouisrocher', -88.99, 41.32, 'colonial', 1682, "Fort Saint-Louis (Rocher)", "Fort St. Louis (Starved Rock)", "Fort de La Salle (1682) ; en 1683, il y concède un fief à Pierre Prudhomme, l'un des plus anciens actes de concession de l'Illinois.", "La Salle's fort (1682); in 1683 he granted a fief there to Pierre Prudhomme, one of the oldest land grants in Illinois.", 'kennedy'),
 ('pimiteoui', -89.592, 40.700, 'peoria', 1691, "Fort Pimiteoui (Saint-Louis du lac Peoria)", "Fort Pimiteoui (St. Louis on Lake Peoria)", "Fort de Tonty et La Forest (1691-1692) près d'un grand village peoria ; mission du P. Gravier (1693) ; un forgeron, Saint-Michel, y travaille en 1705.", "Fort of Tonty and La Forest (1691-1692) by a large Peoria village; Father Gravier's mission (1693); a blacksmith, St. Michel, worked there in 1705.", 'east'),
 ('vieuxpeoria', -89.590, 40.698, 'peoria', 1765, "Vieux-Peoria (1765-1796)", "Old Peoria (1765-1796)", "Antoine Saint-François y sème du maïs en 1765. Habitants chassés en 1780-1781 par les raids, revenus après 1783 ; 62 habitants connus. En 1773, Jean-Baptiste Point de Sable y achète la terre de Maillet avant de gagner la rivière Chicago.", "Antoine Saint-François sowed corn there in 1765. Inhabitants driven out in 1780-1781 by raids, back after 1783; 62 known residents. In 1773 Jean-Baptiste Point de Sable bought Maillet's land there before moving to the Chicago River.", 'east'),
 ('maillet', -89.582, 40.688, 'peoria', 1778, "La Ville de Maillet (1778-1812)", "La Ville de Maillet (1778-1812)", "Nouveau village fondé vers 1778 par Jean-Baptiste Maillet, à un mille et demi au sud, dit aussi « Au Pied du lac » (d'où « Opa », « Le Pé »). 96 habitants connus, dont Antoine Le Claire (1809-1812). Brûlé en novembre 1812 par la milice du capitaine Craig, qui expulse 42 habitants.", "New village founded about 1778 by Jean-Baptiste Maillet, a mile and a half south, also called “Au Pied du lac” (hence “Opa,” “Le Pé”). 96 known residents, including Antoine Le Claire (1809-1812). Burned in November 1812 by Captain Craig's militia, who evicted 42 inhabitants.", 'east'),
 ('traitepeoria', -89.570, 40.655, 'peoria', 1818, "Poste de traite de Peoria (après 1812)", "Peoria trading house (after 1812)", "Sur la rive est (comté de Tazewell) : agents de l'American Fur Co. (Deschamps, Buisson), la famille Bourbonne, qui y tient une auberge en 1825 avant de donner son nom à Bourbonnais. 23 habitants connus.", "On the east bank (Tazewell County): American Fur Co. agents (Deschamps, Buisson) and the Bourbonne family, who kept a tavern there in 1825 before giving their name to Bourbonnais. 23 known residents.", 'east'),
 ('bunkum', -87.582, 40.824, 'kankakee', 1832, "Bunkum (Iroquois)", "Bunkum (Iroquois)", "Poste de traite de Gurdon Hubbard pour l'American Fur Co., cédé en 1832 à son adjoint Noël Levasseur, qui épouse Watch-e-kee.", "Gurdon Hubbard's American Fur Co. post, turned over in 1832 to his assistant Noël Levasseur, who married Watch-e-kee.", 'kankakee'),
 ('tippecanoe', -86.86, 40.47, 'kankakee', 1832, "Camp Tippecanoe (traité de 1832)", "Camp Tippecanoe (1832 treaty)", "Traité avec les Potéouatamis, signé par 61 chefs ; Levasseur reçoit 1 800 $ et les Bourbonnais des terres en réserve. Après la guerre de Black Hawk, les Potéouatamis sont déplacés et leurs terres vendues.", "Treaty with the Potawatomi, signed by 61 chiefs; Levasseur received $1,800 and the Bourbonnais family reserve lands. After the Black Hawk War the Potawatomi were removed and their lands sold.", 'kankakee'),
 ('bourbonnais', -87.877, 41.150, 'kankakee', 1835, "Bourbonnais", "Bourbonnais", "François Bourbonnais et sa femme autochtone y bâtissent une cabane en 1835 ; Levasseur s'y fixe en 1837 et lance une migration en chaîne depuis le Québec. Vers 1850, village d'environ 2 000 habitants ; écarté par l'Illinois Central, il tombe à quelque 600 habitants vers 1900.", "François Bourbonnais and his Native wife built a cabin there in 1835; Levasseur settled in 1837 and set off a chain migration from Quebec. By 1850 a village of about 2,000; bypassed by the Illinois Central, it fell to some 600 by 1900.", 'kantowicz'),
 ('viator', -87.882, 41.153, 'kankakee', 1865, "Collège Saint-Viateur", "St. Viator College", "Les Clercs de Saint-Viateur arrivent de Joliette en 1865 (P. Beaudoin) ; le P. Thomas Roy ouvre le cours classique en 1868 ; charte universitaire en 1874 ; chapelle Roy (1889) en pierre bleue de la Kankakee. Premier collège classique québécois hors du Canada ; en 1916, il a formé 32 prêtres du diocèse de Chicago. En 1900-1901 : 243 élèves, dont 200 de l'Illinois.", "The Clerics of St. Viator came from Joliette in 1865 (Father Beaudoin); Father Thomas Roy opened the classical course in 1868; university charter in 1874; Roy chapel (1889) in Kankakee blue stone. The first Quebec-style classical college outside Canada; by 1916 it had trained 32 Chicago diocesan priests. In 1900-1901: 243 students, 200 from Illinois.", 'viator'),
 ('kankakee', -87.861, 41.120, 'kankakee', 1853, "Kankakee", "Kankakee", "Ville née de l'Illinois Central (« Kankakee Depot »), choisie comme chef-lieu en 1853 au détriment de Bourbonnais. Siège du Journal de l'Illinois (1857) et du Courrier de l'Ouest (1868). En 1910, environ 1 000 Canadiens français sur 13 986 habitants ; paroisse Sainte-Rose.", "Town born of the Illinois Central (“Kankakee Depot”), chosen as county seat in 1853 over Bourbonnais. Home of the Journal de l'Illinois (1857) and the Courrier de l'Ouest (1868). In 1910, about 1,000 French Canadians among 13,986 people; St. Rose parish.", 'kantowicz'),
 ('steanne', -87.715, 41.025, 'kankakee', 1851, "Sainte-Anne", "St. Anne", "Chiniquy, arrivé à Chicago le 29 octobre 1851, y attire des centaines de familles ; excommunié en 1858 sur la place du village, il passe aux presbytériens. Paroisse catholique refondée en 1871 ; relique de sainte Anne envoyée de Montréal en 1886.", "Chiniquy, who reached Chicago on October 29, 1851, drew hundreds of families there; excommunicated in 1858 in the village square, he joined the Presbyterians. Catholic parish refounded in 1871; relic of St. Anne sent from Montreal in 1886.", 'kantowicz'),
 ('momence', -87.663, 41.160, 'kankakee', 1845, "Momence", "Momence", "Bourg agricole canadien des années 1840, candidat malheureux au chef-lieu en 1853.", "Canadian farm town of the 1840s, unsuccessful candidate for county seat in 1853.", 'kantowicz'),
 ('stgeorge', -87.80, 41.08, 'kankakee', 1845, "Saint-Georges", "St. George", "Paroisse canadienne fondée dans les années 1840.", "Canadian parish founded in the 1840s.", 'kantowicz'),
 ('beaverville', -87.66, 40.95, 'kankakee', 1855, "Beaverville (Sainte-Marie)", "Beaverville (St. Mary)", "Mission de Chiniquy dans le comté d'Iroquois.", "Chiniquy mission in Iroquois County.", 'kantowicz'),
 ('lerable', -87.80, 40.90, 'kankakee', 1855, "L'Érable", "L'Erable", "Mission de Chiniquy dans le comté d'Iroquois.", "Chiniquy mission in Iroquois County.", 'kantowicz'),
 ('papineau', -87.72, 40.97, 'kankakee', 1860, "Papineau", "Papineau", "Limite sud de la colonie canadienne de la Kankakee.", "Southern edge of the Kankakee Canadian colony.", 'cormier'),
 ('manteno', -87.832, 41.250, 'kankakee', 1854, "Manteno", "Manteno", "Ville champignon créée par l'Illinois Central au début des années 1850.", "Boom town created by the Illinois Central in the early 1850s.", 'kantowicz'),
 ('shawwaw', -87.97, 41.20, 'kankakee', 1830, "Village de Shaw-waw-nas-see (Rock Creek)", "Shaw-waw-nas-see's village (Rock Creek)", "Village potéouatami à neuf milles au nord-ouest de Kankakee, sur la piste indienne qui traversait le site de la ville.", "Potawatomi village nine miles northwest of Kankakee, on the Indian trail that crossed the town site.", 'kankakee'),
 ('nauvoo', -91.385, 40.550, 'presse', 1854, "Nauvoo", "Nauvoo", "Colonie Icarienne (juillet-décembre 1854), premier journal de langue française de l'Illinois, organe de la communauté d'Étienne Cabet installée dans le village abandonné par les mormons.", "Colonie Icarienne (July-December 1854), Illinois's first French-language newspaper, organ of Étienne Cabet's community settled in the village abandoned by the Mormons.", 'cormier'),
 ('chicago', -87.632, 41.884, 'presse', 1861, "Chicago", "Chicago", "Une quinzaine de journaux français de 1861 à 1931 : L'Observateur, La Sentinelle, L'Amérique (Louis Fréchette, 1869-1870), Le Figaro illustré (1886), Le Courrier de l'Illinois (vers 1880), Le Petit Journal de Chicago (seul quotidien, 1903), Le Courrier franco-américain (1905-1931). En 1888, environ 30 000 francophones, dont 25 200 Canadiens français ; quatre paroisses.", "About fifteen French papers from 1861 to 1931: L'Observateur, La Sentinelle, L'Amérique (Louis Fréchette, 1869-1870), Le Figaro illustré (1886), Le Courrier de l'Illinois (about 1880), Le Petit Journal de Chicago (the only daily, 1903), Le Courrier franco-américain (1905-1931). In 1888, about 30,000 French speakers, 25,200 of them French Canadians; four parishes.", 'cormier'),
 ('stpaul', -93.093, 44.944, 'presse', 1877, "Saint-Paul", "St. Paul", "Le Canadien (1877-1903), fusionné par Bachand-Vertefeuille avec le Courrier de l'Ouest de Chicago.", "Le Canadien (1877-1903), merged by Bachand-Vertefeuille with Chicago's Courrier de l'Ouest.", 'cormier'),
 ('minneapolis', -93.265, 44.978, 'presse', 1900, "Minneapolis", "Minneapolis", "La Voix du Peuple (1900-1903), feuille démocrate.", "La Voix du Peuple (1900-1903), a Democratic paper.", 'cormier'),
 ('watertown', -75.91, 43.975, 'presse', 1864, "Watertown (New York)", "Watertown (New York)", "Alexandre Grandpré et Claude Petit y fondent un journal en 1864, entre les deux vies du journal de Kankakee.", "Alexandre Grandpré and Claude Petit founded a paper there in 1864, between the two lives of the Kankakee paper.", 'cormier'),
 ('baycity', -83.889, 43.594, 'presse', 1904, "Bay City (Michigan)", "Bay City (Michigan)", "Chronique régionale du Courrier-Canadien (1904), ajoutée à son en-tête.", "Regional column of the Courrier-Canadien (1904), added to its masthead.", 'cormier'),
 ('duluth', -92.104, 46.787, 'midwest', 1880, "Duluth : paroisse Saint-Jean-Baptiste", "Duluth: St. John the Baptist parish", "Présence canadienne-française ancienne et paroisse nationale ; la ville porte le nom de Daniel Greysolon, sieur du Lhut.", "Early French Canadian presence and national parish; the city bears the name of Daniel Greysolon, sieur du Lhut.", 'ifm1'),
 ('marquette', -87.395, 46.544, 'midwest', 1900, "Marquette : centre Baumier", "Marquette: Baumier center", "Centre du patrimoine franco-canadien du nord du Michigan.", "Heritage center for French Canadians in northern Michigan.", 'ifm1'),
 ('turtle', -99.99, 48.86, 'midwest', 1882, "Montagne de la Tortue (Belcourt)", "Turtle Mountain (Belcourt)", "Réserve des Chippewas de la montagne de la Tortue, foyer métis et michif ; neuvaine de sainte Anne fondée par l'abbé Jean Malo ; mémoire de Riel, de Bottineau et de Rolette. D. Delâge y voit une mémoire vivante de l'alliance franco-amérindienne.", "Turtle Mountain Chippewa reservation, a Métis and Michif hearth; St. Anne novena founded by Father Jean Malo; memory of Riel, Bottineau and Rolette. D. Delâge sees in it a living memory of the French-Indian alliance.", 'ifm2'),
 ('rolettecty', -99.84, 48.77, 'midwest', 1873, "Comté de Rolette", "Rolette County", "Nommé d'après Joseph Rolette fils, le héros de Pembina (voir Tassé, t. II).", "Named after Joseph Rolette Jr., the hero of Pembina (see Tassé, vol. II).", 'ifm1'),
 ('redlake', -96.274, 47.882, 'midwest', 1880, "Red Lake Falls, Terrebonne, Gentilly, Oklee", "Red Lake Falls, Terrebonne, Gentilly, Oklee", "Villages canadiens-français de l'ouest du Minnesota. La famille Fournier de Red Lake Falls venait de Sainte-Ursule, dans le comté de Maskinongé : le pays natal d'Aubry.", "French Canadian villages of western Minnesota. The Fournier family of Red Lake Falls came from Sainte-Ursule, Maskinongé County: Aubry's home country.", 'ifm3'),
 ('pineridge', -102.556, 43.026, 'midwest', 1870, "Pine Ridge (mission Holy Rosary)", "Pine Ridge (Holy Rosary mission)", "Les descendants des traiteurs français mariés aux Oglalas, comme John Baptiste Richard ou Pourier, forment le groupe métis le plus nombreux de la réserve ; noms français abondants (G. Gagnon, « Ikce Wasicu »).", "Descendants of French traders married to Oglala women, such as John Baptiste Richard or Pourier, form the reservation's largest mixed-blood group; many French surnames (G. Gagnon, “Ikce Wasicu”).", 'ifm2'),
 ('boniface', -97.12, 49.89, 'midwest', 1818, "Saint-Boniface", "Saint-Boniface", "Foyer franco-manitobain et métis ; Festival du Voyageur.", "Franco-Manitoban and Métis hearth; Festival du Voyageur.", 'ifm2'),
 ('fargo', -96.79, 46.877, 'midwest', 1900, "Fargo (« le Petit Fargo »)", "Fargo (“le Petit Fargo”)", "Mémoire d'une communauté canadienne-française de la vallée de la Rivière-Rouge.", "Memory of a French Canadian community of the Red River valley.", 'ifm2'),
 ('grandforks', -97.033, 47.925, 'midwest', 2008, "Grand Forks (IFMidwest)", "Grand Forks (IFMidwest)", "Siège des Initiatives en français Midwest (Université du Dakota du Nord) et de sa collection.", "Seat of Initiatives in French Midwest (University of North Dakota) and its collection.", 'ifm1'),
 ('huot', -96.43, 47.86, 'midwest', 1863, "Old Crossing (Huot)", "Old Crossing (Huot)", "Lieu du traité de 1863 sur la Red Lake ; fête française annuelle.", "Site of the 1863 treaty on the Red Lake River; annual French festival.", 'ifm1'),
 ('voyageurs', -92.85, 48.50, 'midwest', 1975, "Parc national des Voyageurs", "Voyageurs National Park", "La route des canots des voyageurs entre le lac Supérieur et le lac des Bois, devenue lieu de patrimoine.", "The voyageurs' canoe route between Lake Superior and the Lake of the Woods, now a heritage place.", 'ifm1'),
]
TL = [  # chronologie
 (1680, "La Salle bâtit le fort Crèvecœur.", "La Salle builds Fort Crèvecœur.", 'kennedy'),
 (1682, "Fort Saint-Louis du Rocher ; La Salle à l'embouchure du Mississippi.", "Fort St. Louis at Starved Rock; La Salle at the mouth of the Mississippi.", 'kennedy'),
 (1691, "Tonty et La Forest transportent le fort Saint-Louis au lac Peoria (Pimiteoui).", "Tonty and La Forest move Fort St. Louis to Lake Peoria (Pimiteoui).", 'east'),
 (1703, "Fondation de Kaskaskia par le P. Marest.", "Founding of Kaskaskia by Father Marest.", 'kennedy'),
 (1717, "Le pays des Illinois est rattaché à la Louisiane.", "The Illinois Country is attached to Louisiana.", 'kennedy'),
 (1723, "Premier fort de Chartres (Boisbriand).", "First Fort de Chartres (Boisbriand).", 'kennedy'),
 (1739, "Les frères Mallet gagnent Santa Fe par le Nebraska, le Kansas et le Colorado : le premier tracé français vers le Nouveau-Mexique, un siècle avant Aubry.", "The Mallet brothers reach Santa Fe through Nebraska, Kansas and Colorado: the first French route to New Mexico, a century before Aubry.", 'kennedy'),
 (1763, "Fin de la Nouvelle-France.", "End of New France.", 'kennedy'),
 (1765, "Antoine Saint-François sème du maïs au Vieux-Peoria.", "Antoine Saint-François sows corn at Old Peoria.", 'east'),
 (1778, "Maillet fonde la Ville de Maillet.", "Maillet founds La Ville de Maillet.", 'east'),
 (1812, "La milice de Craig brûle la Ville de Maillet.", "Craig's militia burns La Ville de Maillet.", 'east'),
 (1832, "Levasseur reprend le poste de Bunkum ; traité de Camp Tippecanoe.", "Levasseur takes over the Bunkum post; Treaty of Camp Tippecanoe.", 'kankakee'),
 (1837, "Levasseur s'établit à Bourbonnais et lance la migration québécoise.", "Levasseur settles at Bourbonnais and launches the Quebec migration.", 'kantowicz'),
 (1850, "10 699 Canadiens de naissance dans l'Illinois (recensement).", "10,699 Canadian-born in Illinois (census).", 'cormier'),
 (1851, "Chiniquy arrive à Chicago et prend Bourbonnais et Sainte-Anne.", "Chiniquy reaches Chicago and takes over Bourbonnais and St. Anne.", 'kantowicz'),
 (1852, "De 1852 à 1854, 920 familles et 4 856 célibataires quittent la rive nord du Saint-Laurent, presque tous pour l'Illinois.", "From 1852 to 1854, 920 families and 4,856 single people leave the north shore of the St. Lawrence, nearly all for Illinois.", 'kantowicz'),
 (1853, "Kankakee, ville de l'Illinois Central, devient chef-lieu.", "Kankakee, an Illinois Central town, becomes county seat.", 'kankakee'),
 (1854, "Colonie Icarienne à Nauvoo, premier journal français de l'Illinois.", "Colonie Icarienne at Nauvoo, the first French paper in Illinois.", 'cormier'),
 (1857, "Le Journal de l'Illinois à Kankakee ; enquête parlementaire du Canada-Uni sur l'émigration.", "Le Journal de l'Illinois at Kankakee; Province of Canada parliamentary inquiry into emigration.", 'cormier'),
 (1858, "Excommunication de Chiniquy à Sainte-Anne.", "Chiniquy excommunicated at St. Anne.", 'kantowicz'),
 (1868, "Collège Saint-Viateur ; Le Courrier de l'Ouest à Kankakee.", "St. Viator College; Le Courrier de l'Ouest at Kankakee.", 'viator'),
 (1878, "Tassé visite Bourbonnais et le décrit comme un vrai village canadien.", "Tassé visits Bourbonnais and describes it as a true Canadian village.", 'kantowicz'),
 (1900, "27 109 Canadiens français de première et deuxième générations dans l'Illinois, dont 12 833 à Chicago.", "27,109 first- and second-generation French Canadians in Illinois, 12,833 of them in Chicago.", 'kantowicz'),
 (1903, "Le Petit Journal de Chicago, seul quotidien français de l'Ouest (30 numéros).", "Le Petit Journal de Chicago, the only French daily in the West (30 issues).", 'cormier'),
 (1931, "Dernière mention du Courrier franco-américain.", "Last listing of the Courrier franco-américain.", 'cormier'),
]
PRESSE = [  # année, titre, ville, années, éditeur
 (1854, "Colonie Icarienne", "Nauvoo", "1854", "Étienne Cabet"),
 (1857, "Le Journal de l'Illinois", "Kankakee (et Chicago, 1857-1858)", "1857-1863 ?", "A. Grandpré et C. Petit"),
 (1861, "L'Observateur", "Chicago", "1861 ; 1866 ou 1868 ?", "S.-E. Pinta ; L. Fréchette"),
 (1867, "La Sentinelle", "Chicago", "1867", "Couillard de l'Épinay"),
 (1868, "Le Courrier de l'Ouest, puis Courrier de l'Illinois", "Kankakee, puis Chicago (vers 1880)", "1868-1896", "A. Grandpré ; J.-B.-A. Paradis"),
 (1869, "L'Amérique", "Chicago", "1869-1870", "Guéroult et Pinta ; L. Fréchette"),
 (1873, "L'Union franco-américaine", "?", "1873", "J.-B.-L. Lemoine"),
 (1885, "Le Cercle français", "Bourbonnais (collège Saint-Viateur)", "1885", ""),
 (1885, "La Trompette évangélique", "Chicago", "1885-1886", "Seguin"),
 (1886, "L'Avenir national", "Chicago", "1886", "J.-B.-L. Lemoine, J.-E. Cyr"),
 (1886, "Le Figaro illustré", "Chicago", "1886-1887", "C. Gentilé, A. Gouëre"),
 (1888, "Le Journal de Bourbonnais", "Bourbonnais", "1888", ""),
 (1889, "Le Combat", "Chicago", "1889-1893 ?", "Dr Elzéar Paquin"),
 (1894, "Le Bulletin officiel", "Chicago", "1894", "L.-J. Bachand-Vertefeuille"),
 (1896, "Le Courrier de l'Ouest", "Chicago", "1896-1903", "P. Masson ; L.-J. Bachand-Vertefeuille"),
 (1903, "Le Petit Journal de Chicago", "Chicago", "22 juin - juillet 1903", "L.-J. Bachand-Vertefeuille"),
 (1903, "Le Courrier-Canadien", "Chicago (Saint-Paul, Minneapolis, Bay City)", "1903-1904", "L.-J. Bachand-Vertefeuille"),
 (1903, "La Famille", "Chicago", "1903", "Association nationale des Canadiens-Français"),
 (1905, "Le Courrier franco-américain", "Chicago", "1905-1931 ?", "L.-J. Bachand-Vertefeuille"),
]
ETATS = [('Illinois', 200), ('New York', 7), ('Indiana', 6), ('Wisconsin', 5), ('Michigan', 5), ('Iowa', 4), ('Canada', 4), ('Missouri', 3), ('Nebraska', 3), ('Kansas', 2), ('Ohio', 1), ('Mississippi', 1), ('Tennessee', 1), ('France', 1)]

TAGS = [(r'military', "concession militaire", "military grant"), (r'petition|pet\. Cong', "pétition au Congrès", "petition to Congress"),
        (r'land grant|grant|claim', "terre", "land"), (r'American Fur', "American Fur Co.", "American Fur Co."), (r'trader|trading', "traiteur", "trader"),
        (r'blacksmith', "forgeron", "blacksmith"), (r'slain|killed', "tué", "killed"), (r'interpreter', "interprète", "interpreter"),
        (r'Pottawatomie|Indian', "Autochtone ou Métis", "Native or Métis"), (r'tavern', "aubergiste", "tavern keeper"), (r'Rev\.|priest', "prêtre", "priest"),
        (r'married|wife|widow', "famille", "family"), (r'St\. Louis|Cahokia|Kaskaskia', "lien avec le Missouri ou les Illinois", "Missouri or Illinois tie")]

def geo():
    F = [{"type": "Feature", "geometry": {"type": "Point", "coordinates": [lon, lat]},
          "properties": {"id": i, "categorie": c, "couleur": C[c][0], "annee": an, "nom": nfr, "nom_en": nen, "texte": tfr, "texte_en": ten, "source": S[s]}}
         for i, lon, lat, c, an, nfr, nen, tfr, ten, s in L]
    json.dump({"type": "FeatureCollection", "name": "illinois_francais", "features": F}, open(A + 'data/illinois_francais.geojson', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    rows = []
    for o in PEO:
        rows.append({"village": o['v'], "nom": o['nom'], "annees": o['annees'], "mentions": [t for r, t, _ in TAGS if re.search(r, o['txt'])]})
    json.dump({"source": S['east'], "habitants": rows}, open(A + 'data/peoria_habitants.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

def gabarit(fr, titre, sous, page):
    src = open(A + ('hommes.html' if fr else 'hommes-en.html'), encoding='utf-8').read()
    tete = src[:src.find('<header')]
    tete = re.sub(r'<title>.*?</title>', f'<title>{titre} · Atlas Aubry</title>', tete)
    tete = tete.replace('</head>', '<link rel="stylesheet" href="https://unpkg.com/maplibre-gl@5/dist/maplibre-gl.css">\n<script src="https://unpkg.com/maplibre-gl@5/dist/maplibre-gl.js"></script>\n</head>')
    autre = page.replace('.html', '-en.html') if fr else page
    nav = (f'<a class="lien-langue" href="{autre}" hreflang="en" lang="en">English</a><a href="index.html">← Retour à l\'atlas</a>' if fr else
           f'<a class="lien-langue" href="{autre}" hreflang="fr" lang="fr">Français</a><a href="index-en.html">← Back to the atlas</a>')
    return tete + f'<header class="barre">\n  <h1>{titre} <span>· {sous}</span></h1>\n  <span class="esp"></span>{nav}\n</header>\n'

def barres(fr):
    W, bh = 620, 20; mx = ETATS[0][1]
    o = [f'<svg viewBox="0 0 {W} {len(ETATS)*bh+10}" role="img" aria-label="%s" style="width:100%%;max-width:620px;height:auto;font-family:Georgia,serif">' % ("Élèves de Saint-Viateur par lieu d'origine, 1900-1901" if fr else "St. Viator students by home, 1900-1901")]
    for k, (e, n) in enumerate(ETATS):
        w = max(2, (W-200) * n / mx); y = k*bh + 4
        o.append(f'<text x="120" y="{y+14}" font-size="12" text-anchor="end" fill="#3b3328">{html.escape(e)}</text><rect x="128" y="{y+2}" width="{w:.0f}" height="{bh-6}" fill="#3e5f7a"/><text x="{128+w+5:.0f}" y="{y+14}" font-size="11.5" fill="#3b3328">{n}</text>')
    return ''.join(o) + '</svg>'

def page(fr):
    T = (lambda a, b: a if fr else b)
    idx = 'index.html' if fr else 'index-en.html'
    sfx = '' if fr else '-en'
    h = gabarit(fr, T("L'Illinois français", "French Illinois"), T("et l'archipel francophone du Midwest", "and the French-speaking archipelago of the Midwest"), 'illinois-francais.html')
    h += '<main>\n'
    h += T("<h2>Du continent perdu à l'archipel retrouvé</h2><p class=\"chapeau\">En 1979, les géographes Dean Louder, Christian Morissonneau et Eric Waddell proposent de lire l'Amérique française non plus comme un empire perdu en 1763, mais comme un archipel : des îlots francophones semés de la baie d'Hudson à la Louisiane par des générations de gens mobiles, coureurs de bois puis voyageurs, guides, interprètes et charretiers, dont les convois de mulets allaient du Texas à l'Assiniboine jusqu'à l'arrivée du chemin de fer. Aubry, Canadien de Maskinongé devenu convoyeur de Santa Fe, est l'une de ces trajectoires. Cette page cartographie l'un des îlots les plus denses, l'Illinois, et ceux du Midwest qui en sont les cousins.</p>",
           "<h2>From lost continent to rediscovered archipelago</h2><p class=\"chapeau\">In 1979 the geographers Dean Louder, Christian Morissonneau and Eric Waddell proposed reading French America not as an empire lost in 1763 but as an archipelago: French-speaking islands scattered from Hudson Bay to Louisiana by generations of mobile people, coureurs de bois then voyageurs, guides, interpreters and teamsters, whose mule trains ran from Texas to the Assiniboine until the railroad came. Aubry, a Canadian from Maskinongé who became a Santa Fe freighter, is one of these trajectories. This page maps one of the densest islands, Illinois, and its Midwest cousins.</p>")
    h += T(f"<p><b>Les liens avec Aubry.</b> Les frères Mallet ouvrent dès 1739 la route de Santa Fe depuis les Illinois, un siècle avant lui. Antoine Le Claire, habitant de la Ville de Maillet, est le Leclerc du tome I de Tassé. Noël Levasseur, fondateur de Bourbonnais, est dans le tome II ; Tassé lui-même visite Bourbonnais. Les familles canadiennes de Red Lake Falls venaient du comté de Maskinongé. Et à Pine Ridge, les descendants de John Baptiste Richard, traiteur de la Platte biographié par Hafen, perpétuent les noms français. Voir <a href=\"canadiens-ouest{sfx}.html\">{T('Les Canadiens de l’Ouest', 'The Canadians of the West')}</a>, <a href=\"montagnards{sfx}.html\">{T('Les hommes des montagnes', 'The Mountain Men')}</a> et <a href=\"reseau{sfx}.html\">{T('Le réseau francophone', 'The French-speaking network')}</a>.</p>",
           f"<p><b>Ties with Aubry.</b> The Mallet brothers opened the road to Santa Fe from the Illinois Country as early as 1739, a century before him. Antoine Le Claire, a resident of La Ville de Maillet, is the Leclerc of Tassé's volume I. Noël Levasseur, founder of Bourbonnais, is in volume II; Tassé himself visited Bourbonnais. The Canadian families of Red Lake Falls came from Maskinongé County. And at Pine Ridge, descendants of John Baptiste Richard, the Platte trader in Hafen's series, carry on French names. See <a href=\"canadiens-ouest{sfx}.html\">The Canadians of the West</a>, <a href=\"montagnards{sfx}.html\">The Mountain Men</a> and <a href=\"reseau{sfx}.html\">The French-speaking network</a>.</p>")
    h += T('<p class="sommaire"><a href="#carte">La carte</a> · <a href="#chrono">Chronologie</a> · <a href="#peoria">Les villages de Peoria</a> · <a href="#kankakee">Le Petit Canada de la Kankakee</a> · <a href="#presse">La presse française</a> · <a href="#viator">Saint-Viateur</a> · <a href="#midwest">L\'archipel du Midwest</a> · <a href="#sources">Sources</a></p>',
           '<p class="sommaire"><a href="#carte">The map</a> · <a href="#chrono">Timeline</a> · <a href="#peoria">The Peoria villages</a> · <a href="#kankakee">The Kankakee Little Canada</a> · <a href="#presse">The French press</a> · <a href="#viator">St. Viator</a> · <a href="#midwest">The Midwest archipelago</a> · <a href="#sources">Sources</a></p>')
    h += T('<h2 id="carte">La carte</h2>', '<h2 id="carte">The map</h2>')
    h += '<div id="carte-il" style="height:600px;border:1px solid #c9bba3;border-radius:6px"></div>\n<div id="leg-il" style="display:flex;flex-wrap:wrap;gap:.3rem 1rem;margin:.5rem 0 1rem;font-size:.88rem"></div>\n'
    h += T("<p class=\"avert\">Cliquez sur une catégorie pour l'isoler ; positions au lieu-dit ou au village (approximatives).</p>", "<p class=\"avert\">Click a category to isolate it; positions at the site or village (approximate).</p>")
    h += T('<h2 id="chrono">Chronologie</h2>', '<h2 id="chrono">Timeline</h2>') + '<table>'
    for an, tfr, ten, s in TL:
        h += f'<tr><td style="white-space:nowrap"><b>{an}</b></td><td>{html.escape(tfr if fr else ten)}</td></tr>'
    h += '</table>'
    # Peoria
    h += T('<h2 id="peoria">Les trois villages français de Peoria</h2>', '<h2 id="peoria">The three French villages of Peoria</h2>')
    h += T("<p>En 1933, le journaliste Ernest E. East a relevé dans les archives publiques (concessions de terres, pétitions au Congrès, rôles d'impôt) les noms des habitants des trois établissements français successifs du lac Peoria. Les 181 noms ci-dessous sont classés par village, avec les années de résidence connues (« -1783 » : avant 1783 ; « 1784$ » : après 1784) et la nature des mentions. L'orthographe est celle des documents.</p>",
           "<p>In 1933 the journalist Ernest E. East gathered from public records (land grants, petitions to Congress, tax rolls) the names of the residents of the three successive French settlements on Lake Peoria. The 181 names below are grouped by village, with known years of residence (“-1783”: before 1783; “1784$”: after 1784) and the kind of record. Spelling is that of the documents.</p>")
    VL = {'old': T("Vieux-Peoria (1765-1796)", "Old Peoria (1765-1796)"), 'maillet': T("La Ville de Maillet (1778-1812)", "La Ville de Maillet (1778-1812)"), 'traite': T("Le poste de traite (après 1812)", "The trading house (after 1812)")}
    for v in ('old', 'maillet', 'traite'):
        rows = [o for o in PEO if o['v'] == v]
        h += f'<details{" open" if v == "old" else ""}><summary><b>{VL[v]}</b> ({len(rows)})</summary><table style="font-size:.88rem"><tr><th>{T("Nom", "Name")}</th><th>{T("Années", "Years")}</th><th>{T("Mentions", "Records")}</th></tr>'
        for o in rows:
            tg = [(a if fr else b) for r, a, b in TAGS if re.search(r, o['txt'])]
            h += f'<tr><td>{html.escape(o["nom"])}</td><td>{html.escape(o["annees"])}</td><td>{html.escape(", ".join(tg))}</td></tr>'
        h += '</table></details>'
    h += T("<p class=\"avert\">Pour Antoine Le Claire, East donne une naissance en 1797 à Saint-Joseph (Michigan), alors que Tassé le fait naître vers 1785 ; l'écart reste à trancher.</p>",
           "<p class=\"avert\">For Antoine Le Claire, East gives a birth in 1797 at St. Joseph (Michigan), whereas Tassé has him born about 1785; the discrepancy remains open.</p>")
    # Kankakee
    h += T('<h2 id="kankakee">Le « Petit Canada » de la Kankakee</h2>', '<h2 id="kankakee">The Kankakee “Little Canada”</h2>')
    h += T("<p>Pour l'historien Edward Kantowicz (1982), c'est à la campagne et non dans les villes que le Canada français a réussi à se transplanter dans le Midwest. Après François Bourbonnais (1835), Noël Levasseur, vingt ans au service de l'American Fur Co., s'établit sur la Kankakee en 1837 ; ses récits de prairies fertiles, rapportés au Québec, déclenchent une migration en chaîne. En 1857, une enquête du Parlement du Canada-Uni constate qu'il est plus facile pour un habitant d'acquérir une terre à mille milles, en Illinois, qu'à vingt milles dans la forêt québécoise. Deux forces bouleversent la colonie dans les années 1850 : Chiniquy, l'« apôtre de la tempérance » devenu schismatique, et l'Illinois Central, qui crée Kankakee et laisse Bourbonnais à l'écart. La colonie persiste pourtant : huit paroisses dans le comté de Kankakee, cinq à Chicago, des églises en grès local copiées sur celles du Québec, et le collège Saint-Viateur comme centre.</p><p>Le souvenir du centenaire de Kankakee (1953) ajoute la préhistoire : les Potéouatamis de Shaw-waw-nas-see, le poste de Gurdon Hubbard à Bunkum cédé à Levasseur en 1832, le traité de Camp Tippecanoe, et, cent ans plus tard, les Dandurand, Papineau, Brault, Rivard et LaPlante qui jouent l'histoire de la ville dans le grand spectacle du centenaire.</p>",
           "<p>For the historian Edward Kantowicz (1982), it was in the countryside rather than the cities that French Canada managed to transplant itself in the Midwest. After François Bourbonnais (1835), Noël Levasseur, twenty years with the American Fur Co., settled on the Kankakee in 1837; his tales of fertile prairie, carried back to Quebec, set off a chain migration. In 1857 a Province of Canada parliamentary inquiry found it easier for a habitant to get land a thousand miles away in Illinois than twenty miles into the Quebec bush. Two forces shook the colony in the 1850s: Chiniquy, the “apostle of temperance” turned schismatic, and the Illinois Central, which created Kankakee and bypassed Bourbonnais. Yet the colony persisted: eight parishes in Kankakee County, five in Chicago, churches of local sandstone modelled on Quebec's, and St. Viator College at the centre.</p><p>The Kankakee centennial souvenir (1953) adds the prehistory: Shaw-waw-nas-see's Potawatomi, Gurdon Hubbard's Bunkum post turned over to Levasseur in 1832, the Treaty of Camp Tippecanoe, and, a century later, the Dandurands, Papineaus, Braults, Rivards and LaPlantes acting out the town's history in the great centennial pageant.</p>")
    # presse
    h += T('<h2 id="presse">La presse française de l\'Illinois (1854-1931)</h2>', '<h2 id="presse">The French press of Illinois (1854-1931)</h2>')
    h += T("<p>L.-P. Cormier (1957) distingue deux époques : celle d'Alexandre Grandpré, dont le journal de Kankakee, républicain et d'abord anticlérical, devient le Courrier de l'Illinois installé à Chicago (1857-1896) ; puis celle de Louis Bachand-Vertefeuille, qui fusionne les feuilles de Chicago, Saint-Paul et Minneapolis et tente en 1903 le seul quotidien français de l'Ouest. Le Courrier parle en 1876 à 40 000 électeurs de langue française de l'Illinois.</p>",
           "<p>L.-P. Cormier (1957) distinguishes two eras: that of Alexandre Grandpré, whose Kankakee paper, republican and at first anticlerical, became the Courrier de l'Illinois based in Chicago (1857-1896); then that of Louis Bachand-Vertefeuille, who merged the Chicago, St. Paul and Minneapolis papers and in 1903 attempted the only French daily in the West. In 1876 the Courrier addressed 40,000 French-speaking voters in Illinois.</p>")
    h += f'<table style="font-size:.9rem"><tr><th>{T("Titre", "Title")}</th><th>{T("Lieu", "Place")}</th><th>{T("Années", "Years")}</th><th>{T("Éditeurs, rédacteurs", "Publishers, editors")}</th></tr>'
    for an, t, v, a, e in PRESSE:
        h += f'<tr><td><i>{html.escape(t)}</i></td><td>{html.escape(v)}</td><td>{html.escape(a)}</td><td>{html.escape(e)}</td></tr>'
    h += '</table>'
    # Viator
    h += T('<h2 id="viator">Le collège Saint-Viateur en 1900-1901</h2>', '<h2 id="viator">St. Viator College in 1900-1901</h2>')
    h += T("<p>Le trente-troisième catalogue annuel du collège retrace sa fondation (les Clercs de Saint-Viateur de Joliette à Bourbonnais en 1865, le cours classique du P. Thomas Roy en 1868, la charte de 1874, la chapelle commémorative Roy de 1889) et donne la liste des élèves de l'année avec leur lieu d'origine. À la tête du collège : le P. P. Beaudoin, le P. C. Fournier, le P. L.-A. Sénécal, le P. E.-L. Rivard.</p>",
           "<p>The college's thirty-third annual catalogue recounts its founding (the Clerics of St. Viator from Joliette at Bourbonnais in 1865, Father Thomas Roy's classical course in 1868, the 1874 charter, the Roy memorial chapel of 1889) and lists the year's students with their home. At the head of the college: Fathers P. Beaudoin, C. Fournier, L.-A. Sénécal and E.-L. Rivard.</p>")
    h += barres(fr)
    # Midwest
    h += T('<h2 id="midwest">L\'archipel francophone du Midwest aujourd\'hui</h2>', '<h2 id="midwest">The French-speaking archipelago of the Midwest today</h2>')
    h += T("<p>Les trois numéros du magazine des Initiatives en français Midwest (Université du Dakota du Nord, 2009-2012) recensent les lieux de mémoire de cet archipel : la paroisse Saint-Jean-Baptiste de Duluth, le centre Baumier de Marquette, la montagne de la Tortue et ses Métis michifs, le comté de Rolette, les villages canadiens de Red Lake Falls, Terrebonne et Gentilly, les Oglalas « français » de Pine Ridge, Saint-Boniface et son Festival du Voyageur, le parc national des Voyageurs. Parmi les articles : Pierre Bottineau, Louis Riel, Joseph Rolette, l'abbé Jean Malo, le sieur du Lhut, le P. Hennepin.</p>",
           "<p>The three issues of the Initiatives in French Midwest magazine (University of North Dakota, 2009-2012) survey the memory places of this archipelago: St. John the Baptist parish in Duluth, the Baumier center in Marquette, Turtle Mountain and its Michif Métis, Rolette County, the Canadian villages of Red Lake Falls, Terrebonne and Gentilly, the “French” Oglala of Pine Ridge, Saint-Boniface and its Festival du Voyageur, Voyageurs National Park. Among the articles: Pierre Bottineau, Louis Riel, Joseph Rolette, Father Jean Malo, the sieur du Lhut, Father Hennepin.</p>")
    # sources
    h += T('<h2 id="sources">Sources et données</h2>', '<h2 id="sources">Sources and data</h2>') + '<ul>'
    for k, v in S.items():
        h += f'<li>{html.escape(v)}</li>'
    h += '</ul>'
    h += T("<p>Données : <a href=\"data/illinois_francais.geojson\" download>illinois_francais.geojson</a> (les lieux de la carte) et <a href=\"data/peoria_habitants.json\" download>peoria_habitants.json</a> (les 181 habitants de Peoria). Les textes de cette page sont des résumés rédigés pour l'atlas ; les chiffres et les dates viennent des sources citées.</p>",
           "<p>Data: <a href=\"data/illinois_francais.geojson\" download>illinois_francais.geojson</a> (the map's places) and <a href=\"data/peoria_habitants.json\" download>peoria_habitants.json</a> (the 181 Peoria residents). The texts on this page are summaries written for the atlas; figures and dates come from the sources cited.</p>")
    cats = json.dumps({k: [v[0], v[1] if fr else v[2]] for k, v in C.items()}, ensure_ascii=False)
    h += """<script>
(function(){
const FR=%s, CAT=%s;
const map=new maplibregl.Map({container:'carte-il',style:{version:8,sources:{t:{type:'raster',tiles:['https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}'],tileSize:256,attribution:'Esri, HERE, Garmin, USGS'}},layers:[{id:'t',type:'raster',source:'t',paint:{'raster-saturation':-0.5}}]},center:[-91,43.5],zoom:4.3});
map.addControl(new maplibregl.NavigationControl());
fetch('data/illinois_francais.geojson').then(r=>r.json()).then(g=>{
  const go=()=>{
    map.addSource('il',{type:'geojson',data:g});
    map.addLayer({id:'il',type:'circle',source:'il',paint:{'circle-radius':7,'circle-color':['get','couleur'],'circle-stroke-color':'#fffdf8','circle-stroke-width':1.5,'circle-opacity':0.9}});
    map.on('click','il',e=>{const p=e.features[0].properties;new maplibregl.Popup({maxWidth:'340px'}).setLngLat(e.lngLat).setHTML('<b>'+(FR?p.nom:p.nom_en)+'</b><p style="margin:.4em 0">'+(FR?p.texte:p.texte_en)+'</p><small>'+p.source+'</small>').addTo(map);});
    map.on('mouseenter','il',()=>map.getCanvas().style.cursor='pointer');map.on('mouseleave','il',()=>map.getCanvas().style.cursor='');
    const leg=document.getElementById('leg-il'); let cur=null;
    Object.entries(CAT).forEach(([k,[c,l]])=>{const a=document.createElement('a');a.href='#carte';a.style.cssText='text-decoration:none;color:inherit;cursor:pointer';
      a.innerHTML='<span style="display:inline-block;width:11px;height:11px;border-radius:50%%;background:'+c+';margin-right:5px"></span>'+l;
      a.onclick=ev=>{ev.preventDefault();cur=(cur===k)?null:k;document.querySelectorAll('#leg-il a').forEach(x=>x.style.fontWeight='normal');if(cur)a.style.fontWeight='bold';map.setFilter('il',cur?['==',['get','categorie'],cur]:null);};
      leg.appendChild(a);});
  };
  if(map.loaded()) go(); else map.on('load',go);
});
})();
</script>
""" % ('true' if fr else 'false', cats)
    h += '</main>\n</body>\n</html>\n'
    return h

geo()
for fr in (True, False):
    open(A + ('illinois-francais.html' if fr else 'illinois-francais-en.html'), 'w', encoding='utf-8').write(page(fr))
print('illinois :', len(L), 'lieux,', len(PEO), 'habitants de Peoria,', len(PRESSE), 'journaux')
