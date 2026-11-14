# Corpus « Atlas historique du Québec » : Frenette, Y., É. Rivard et M. St-Hilaire (dir.), La francophonie nord-américaine,
# Québec, Presses de l'Université Laval, coll. « Atlas historique du Québec », 2012. Pages imprimées (PDF - 10).
# Chapitres retenus : ceux qui portent sur les francophones hors du Québec et de l'Acadie, surtout aux États-Unis.
from commun import Corpus
B = "Frenette, Yves, Étienne Rivard et Marc St-Hilaire (dir.) (2012), La francophonie nord-américaine, Québec, PUL, coll. « Atlas historique du Québec »"
C = Corpus('Atlas historique du Québec', 'AH', B)
def F(id, nom, theme, date, lon, lat, cert, pers, desc, page, auteur, note=''):
    C.F(id, nom, theme, date, lon, lat, cert, pers, desc, page, note, source=f"{auteur}, dans {B}")

# ---- Alain Roy, « Sur la piste de Santa Fe, 1721-1880 », p. 101-106
AR = "Roy, Alain, « Sur la piste de Santa Fe, 1721-1880 »"
F('sf01', 'Fort Orléans (Bourgmont)', 'poste', '1724/1726', -93.2, 39.38, 'h', ['Étienne Véniard de Bourgmont'],
  "Chargé en 1722 de bâtir un fort pour se rapprocher des Espagnols, Bourgmont fonde le fort Orléans sur le Missouri en 1724 et fait la paix avec les Missouris, Otos, Kansas et Osages ; le fort est abandonné en 1726. Son emplacement exact est inconnu.", '101', AR)
F('sf02', 'Santa Fe : les frères Mallet', 'exploration', '1739-05/1740', -105.938, 35.687, 'c', ['Pierre Mallet', 'Paul Mallet'],
  "Partis en mai 1739 avec sept autres Français, Pierre et Paul Mallet atteignent Santa Fe pour ouvrir un commerce ; ils y restent neuf mois et deux de leurs compagnons s'y établissent. Revenus en 1750, ils sont emprisonnés et leurs biens saisis.", '101', AR)
F('sf03', 'Canadian River, la rivière des Mallet', 'toponymie', '1739', -101.0, 35.6, 'h', ['Pierre Mallet', 'Paul Mallet'],
  "La rivière empruntée par les Mallet, longue de près de 1 500 km et traversant quatre États, porte le nom de Canadian River ; une plaque la commémore.", '102', AR, "Point placé sur le cours moyen (Texas).")
F('sf04', 'Expédition de Fabry de la Bruyère', 'exploration', '1741', -97.0, 35.5, 'h', ['André Fabry de la Bruyère', 'Pierre Mallet'],
  "En 1741, Fabry de la Bruyère, guidé par les Mallet, tente sans succès d'atteindre Santa Fe pour y favoriser le commerce. En 1752, Luis Feuilli et Jean Chapuis essaient à leur tour.", '101; 102', AR)
F('sf05', 'Nouveau-Mexique : arrêt des marchands français', 'evenement', '1795', -105.938, 35.687, 'a', [],
  "En 1795, inquiet du nombre croissant de marchands canadiens-français, le gouverneur du Nouveau-Mexique ordonne leur arrestation et la confiscation de leurs biens.", '102', AR)
F('sf06', 'Santa Fe : Jean-Baptiste Lalande', 'commerce', '1804', -105.938, 35.687, 'c', ['Jean-Baptiste Lalande'],
  "Dès 1804, un marchand de Kaskaskia envoie le Canadien Jean-Baptiste Lalande commercer à Santa Fe ; il préfère s'y établir. Sa fille épousera Gervais Nolan.", '102; 104', AR)
F('sf07', 'Sangre de Cristo : Pike averti par deux trappeurs', 'evenement', '1807-02', -105.6, 37.5, 'h', ['Zebulon Pike'],
  "En février 1807, peu avant son arrestation par les Espagnols, le lieutenant Zebulon Pike est averti par deux trappeurs canadiens-français de l'avance de l'armée espagnole.", '103', AR)
F('sf08', "Île Chouteau (rivière Arkansas)", 'evenement', '1816', -100.73, 37.86, 'a', ['Auguste Pierre Chouteau', 'Étienne Provost', 'Jules de Mun'],
  "Autorisés en 1816 à trapper en territoire espagnol, notamment à Taos, Chouteau, Provost et de Mun sont attaqués au retour et se réfugient sur une île de l'Arkansas, rebaptisée île Chouteau ; arrêtés en 1817, leurs biens sont confisqués.", '103', AR)
F('sf09', 'Santa Fe : interprète canadien de Becknell', 'commerce', '1821-09', -105.938, 35.687, 'a', ['William Becknell'],
  "Parti de Franklin (Missouri) le 1er septembre 1821, William Becknell, « père de la piste de Santa Fe », engage près de Santa Fe un trappeur canadien-français comme interprète.", '104', AR)
F('sf10', 'Santa Fe : les Robidoux, maires', 'personnage', '1822/1829', -105.938, 35.687, 'c', ['Antoine Robidoux', 'Michel Robidoux', 'François Robidoux'],
  "Antoine, Michel et François Robidoux font quatre voyages à Santa Fe entre 1822 et 1825 ; devenus citoyens mexicains en 1829, deux d'entre eux sont élus maires de Santa Fe.", '104', AR)
F('sf11', 'Taos : Lavadie, LeDoux, Jeantette', 'famille', '1824/2012', -105.573, 36.407, 'c', ['Gervais Nolan', 'Charles Beaubien'],
  "Gervais Nolan et Charles Beaubien arrivent en 1824 ; plusieurs trappeurs s'installent dans les Sangre de Cristo près de Taos malgré les protestations. Des patronymes comme Lavadie, LeDoux et Jeantette en témoignent encore.", '104', AR)
F('sf12', 'Concession Beaubien-Miranda', 'etablissement', '1841', -104.92, 36.51, 'a', ['Charles Beaubien'],
  "En 1841, Charles Beaubien, marchand prospère, devient copropriétaire de la concession Beaubien-Miranda (1,7 million d'acres) ; deux ans plus tard, son fils obtient la concession Sangre de Cristo (un million d'acres).", '104', AR)
F('sf13', 'Concession de Gervais Nolan', 'etablissement', '1845', -104.6, 35.9, 'h', ['Gervais Nolan'],
  "En 1845, Gervais Nolan obtient une concession de 575 000 acres ; il y bâtit un ranch le long de la piste et irrigue les terres.", '104', AR)
F('sf14', 'Charretiers canadiens de Lewis Garrard', 'commerce', '1846/1847', -99.0, 38.2, 'h', ['Lewis Garrard'],
  "En 1846-1847, la caravane de Lewis Garrard compte de 18 à 20 charretiers canadiens-français qui ponctuent la route de jurons et de chansons. Susan Magoffin, en voyage de noces en 1846, s'offusque de leurs sacres.", '101; 104', AR, "Point placé sur la piste (Kansas).")
F('sf15', 'F.-X. Aubry : records Santa Fe-Independence', 'evenement', '1846/1848', -105.938, 35.687, 'c', ['François-Xavier Aubry'],
  "Entré à 22 ans dans le commerce Saint-Louis-Santa Fe (1846), François-Xavier Aubry relie Santa Fe au Missouri en 8 jours (1847) puis en 5 jours et 16 heures (1848).", '104', AR, "Fiche de l'univers Aubry : voir aussi l'Atlas Aubry.")
F('sf16', "Aubry's Cutoff et fort Aubrey", 'toponymie', '1851/1866', -101.98, 37.98, 'a', ['François-Xavier Aubry'],
  "En 1851, Aubry découvre un raccourci de la piste, l'Aubry's Cutoff, près duquel le fort Aubrey est établi en 1865-1866.", '101; 104', AR, "Fiche de l'univers Aubry.")
F('sf17', 'Santa Fe : magasin J. & H. Mercure', 'commerce', '1848/1863', -105.938, 35.687, 'c', ['Henri Mercure', 'Joseph Mercure', 'François-Xavier Aubry'],
  "Venus de Saint-Louis, Henri et Joseph Mercure ouvrent en 1848 le commerce J. & H. Mercure à Santa Fe, là où Aubry sera poignardé (1854). Après l'échec de prospections au Colorado, Joseph se proclame en 1863 président d'un Nouveau-Mexique indépendant ; interné, il meurt la même année sur la piste.", '104', AR)
F('sf18', 'Aubry Town (Kansas)', 'toponymie', '1857~/1880~', -94.62, 38.7, 'h', ['François-Xavier Aubry'],
  "Vers 1857, une ville du Kansas prend le nom d'Aubry ; disparue dans les années 1880, il n'en reste qu'un nom de canton.", '104', AR, "Fiche de l'univers Aubry ; emplacement approximatif (comté de Johnson).")
F('sf19', 'Aubrey Landing (Arizona)', 'toponymie', '1857~/1880~', -114.11, 34.29, 'a', ['François-Xavier Aubry'],
  "Fondée vers 1857 au bord du Colorado, Aubrey Landing porte le nom d'Aubry et disparaît dans les années 1880. Un vapeur, le F. X. Aubrey, navigue sur le Missouri de 1853 à 1860.", '104', AR, "Fiche de l'univers Aubry.")
F('sf20', 'Cimarron : Lucien B. Maxwell', 'etablissement', '1858/1864', -104.915, 36.511, 'c', ['Lucien Maxwell', 'Charles Beaubien'],
  "En 1858, Charles Beaubien cède la concession à son gendre Lucien B. Maxwell, qui quitte Rayado pour Cimarron ; son manoir accueille les voyageurs, jusqu'à 500 peones vivent sur ses terres et il fait bâtir un moulin à grain en 1864 (musée, lieu historique en 1968).", '105', AR)
F('sf21', 'Fin de la piste de Santa Fe', 'evenement', '1880', -105.0, 35.9, 'h', [],
  "Le chemin de fer réduit de moitié le trafic dès 1876 ; l'arrivée du train en 1880 scelle le sort de la piste. En 1848, 3 000 wagons et 12 000 personnes l'avaient empruntée.", '104; 105', AR, "Point placé près de Fort Union.")

# ---- Nathalie Kermoal, Pays d'en Haut, p. 37-39 ; Guillaume Teasdale, Détroit, p. 40
NK = "Kermoal, Nathalie, « Postes, missions et métissages dans les Pays d'en Haut »"
F('ph01', 'Missions jésuites des Pays d\'en Haut', 'religion', '1665/1670', -90.82, 46.67, 'a', [],
  "Les jésuites fondent plusieurs missions entre 1665 et 1670, dont Saint-Esprit à Chagouamigon (1665), près du lac Supérieur, et celle du Sault-Sainte-Marie (1668).", '38', NK)
F('ph02', 'Michillimakinac : familles métisses', 'famille', '1690/1763', -84.733, 45.787, 'c', [],
  "Après l'interdiction de la traite (1696), des communautés métisses distinctes naissent autour des Grands Lacs ; à Michillimakinac, on suit plusieurs générations de Langlade, Bertrand, Desrivières, Bourassa, Parent, Chaboyer, Blondeau…", '38', NK)
F('ph03', 'Fort La Jonquière, au pied des Rocheuses', 'poste', '1751', -114.0, 51.2, 'h', ['Jacques Le Gardeur de Saint-Pierre'],
  "Successeur de La Vérendrye, Jacques Le Gardeur de Saint-Pierre aurait atteint les Rocheuses en 1751 et y aurait construit le fort La Jonquière.", '39', NK, "Emplacement inconnu (hypothèses autour de Calgary).")
F('ph04', 'Détroit : fort Pontchartrain et côte sud', 'etablissement', '1701/1796', -83.045, 42.331, 'c', ['Antoine Laumet de La Mothe Cadillac'],
  "Fondé en 1701, le poste voit les titres de Cadillac annulés en 1716 ; les concessions reprennent en 1734 et des familles de Montréal colonisent la rive sud dès 1749. Sous les Britanniques (1763), les habitants restent ; la rive nord ne devient effectivement américaine qu'en 1796.", '40', "Teasdale, Guillaume, « Les Canadiens du détroit du lac Érié, 1701-1800 »")

# ---- Cécile Vidal, Mississippi p. 41-50 et Illinois p. 51-58
CV1 = "Vidal, Cécile, « La colonie du Mississippi »"
CV2 = "Vidal, Cécile, « Le Pays des Illinois, 1673-1818 »"
F('ms01', 'Baie de La Mobile : arrivée d\'Iberville', 'exploration', '1699-01-31', -88.05, 30.6, 'a', ["Pierre Le Moyne d'Iberville"],
  "Chargée de devancer les Anglais, l'expédition du Canadien Pierre Le Moyne d'Iberville atteint la baie de La Mobile le 31 janvier 1699 ; le chef-lieu de la colonie change cinq fois entre 1699 et 1722.", '42', CV1)
F('ms02', 'Natchitoches : fort de 1716', 'poste', '1713/1716', -93.086, 31.761, 'c', ['Louis Juchereau de Saint-Denis'],
  "Les traiteurs s'installent d'abord dans le village autochtone (1713-1714) ; en 1716, les officiers bâtissent le fort à distance, illustrant l'« intimité à distance » entre Français et Amérindiens.", '45', CV1)
F('ms03', 'La Nouvelle-Orléans : fondation', 'etablissement', '1718', -90.065, 29.958, 'c', ['Jean-Baptiste Le Moyne de Bienville'],
  "La Compagnie d'Occident de John Law décide en 1717 de fonder une ville-entrepôt ; Bienville en choisit le site en 1718, déjà occupé depuis 1708 par une dizaine de colons. Un chenal est creusé à partir de 1723 pour les navires.", '43; 44', CV1)
F('ms04', 'Côte des Allemands', 'migration', '1720/1721', -90.45, 30.0, 'a', [],
  "En 1720-1721, Law recrute quelques familles suisses et environ 4 000 Allemands de la vallée du Rhin, installés au nord de La Nouvelle-Orléans, rejoints par une centaine d'Alsaciens dans les années 1750. Sur 6 000 émigrants civils (1717-1720), environ 60 % meurent.", '46', CV1)
F('ms05', 'Natchez : massacre de 1729', 'evenement', '1729-11', -91.403, 31.56, 'c', [],
  "Le poste des Natchez, à cent lieues de La Nouvelle-Orléans, est détruit en 1729 ; après ce massacre, la Compagnie des Indes rétrocède la Louisiane à la Couronne (1731).", '42; 46', CV1)
F('ms06', 'Révolte de 1768 contre Ulloa', 'evenement', '1768-10', -90.065, 29.958, 'c', ['Antonio de Ulloa'],
  "En 1768, les élites louisianaises, soutenues par la population, se soulèvent contre le gouverneur espagnol Antonio de Ulloa, qui voulait restreindre le commerce à l'empire espagnol.", '50', CV1)
F('il01', 'Fort Crèvecœur', 'poste', '1680', -89.6, 40.65, 'a', ['René-Robert Cavelier de La Salle'],
  "La Salle bâtit le fort Crèvecœur en 1679-1680 sur la rivière des Illinois, au sud du lac Péoria ; le site est abandonné l'année suivante après une attaque.", '51', CV2)
F('il02', 'Fort Saint-Louis du Rocher', 'poste', '1682/1703', -88.993, 41.32, 'c', ['René-Robert Cavelier de La Salle', 'Henri de Tonty', 'Pierre-Charles De Liette'],
  "Au retour du Bas-Mississippi (1682), La Salle construit le fort Saint-Louis sur un promontoire près de l'actuelle Utica ; concédé à Tonty et De Liette en 1690, il est abandonné en 1703.", '51; 52', CV2)
F('il03', 'Kaskaskia : mission de l\'Immaculée-Conception', 'religion', '1703', -89.914, 37.92, 'a', ['Jacques Gravier'],
  "Fondée par le jésuite Jacques Gravier vers 1689-1690, la mission suit les Kaskaskias qui migrent au printemps 1703 vers le site de Kaskaskia ; une église de pierre y est bâtie dans les années 1740.", '51; 52; 57', CV2)
F('il04', 'Cahokia : Séminaire des Missions étrangères', 'religion', '1698/1702', -90.19, 38.57, 'c', [],
  "En 1698, Mgr de Saint-Vallier autorise le Séminaire des Missions étrangères à fonder une mission chez les Tamaroas et les Cahokias ; en 1702, ses prêtres y restent seuls. La maison Saucier y date de 1716.", '52; 57', CV2)
F('il05', 'Pays des Illinois : farine pour La Mobile', 'commerce', '1708/1715', -89.914, 37.92, 'a', [],
  "Dès 1708, La Mobile envoie chercher de la farine chez les Français des Illinois ; en 1713, on envisage un marché permanent avec Cahokia et Kaskaskia.", '52; 53', CV2)
F('il06', 'Fort de Chartres (Boisbriant)', 'poste', '1719/1752', -90.157, 38.085, 'c', ['Pierre Dugué de Boisbriant'],
  "Rattaché à la Louisiane en 1717, le Pays des Illinois reçoit au printemps 1719 la garnison de l'officier canadien Pierre Dugué de Boisbriant ; le fort de Chartres est souvent reconstruit à cause des crues.", '53; 56', CV2)
F('il07', 'Saint-Philippe (Illinois)', 'etablissement', '1721-03', -90.2, 38.13, 'a', [],
  "En mars 1721, le village de Saint-Philippe est fondé au nord de Fort de Chartres, face à la rivière Meramec et ses mines.", '53', CV2)
F('il08', 'Sainte-Geneviève : sixième village', 'etablissement', '1750~', -90.044, 37.981, 'c', ['Louis Bolduc'],
  "Sainte-Geneviève, sixième village des Illinois, naît à la fin des années 1740 sur la rive droite ; maison Bolduc (1740) et maisons en poteaux en terre. Après 1763, de nombreux habitants traversent le fleuve pour s'y établir.", '53; 56; 58', CV2)
F('il09', 'Les six villages en 1752', 'etablissement', '1752', -90.0, 38.1, 'h', [],
  "Le recensement de 1752 compte 1 385 personnes dans les six villages : 789 colons (57 %) et 596 esclaves noirs et amérindiens ; près de la moitié des feux ont des esclaves noirs.", '54; 56', CV2, "Point placé au centre du Pays des Illinois.")
F('il10', 'Saint-Louis : fondation par Laclède et Chouteau', 'etablissement', '1764', -90.19, 38.627, 'c', ['Pierre Laclède', 'Auguste Chouteau'],
  "Après les traités de 1762-1763, la plupart des habitants passent à Sainte-Geneviève ou à Saint-Louis, fondé en 1764 par Pierre Laclède et Auguste Chouteau face à Cahokia.", '58', CV2)

# ---- Kermoal et Rivard, territorialités franco-métisses, p. 95-100
KR = "Kermoal, Nathalie et Étienne Rivard, « Essors et transformations des territorialités franco-métisses »"
F('mt01', 'Réseau métis au sud des Grands Lacs', 'etablissement', '1763/1830', -87.5, 44.5, 'h', [],
  "À la fin des années 1820, près de 15 000 Métis vivent au sud et à l'ouest des lacs Supérieur et Huron dans une cinquantaine de villages, intermédiaires du « middle ground » ; quelques milliers d'autres sont liés à la traite de Saint-Louis.", '96', KR, "Point régional.")
F('mt02', 'Pembina : chasses et commerce métis', 'commerce', '1820/1849', -97.243, 48.966, 'c', [],
  "Les grandes chasses de la Rivière-Rouge (540 charrettes en 1820, 1 210 plus tard) passent par Pembina ; après avoir brisé le monopole de la Baie d'Hudson (1849), les Métis étendent leur traite vers Pembina, Saint-Joseph et Saint Paul.", '99; 100', KR)
F('mt03', 'Montagne à la Tortue : Métis du père Belcourt', 'etablissement', '1855', -100.0, 48.9, 'a', ['Georges-Antoine Belcourt'],
  "En 1855, le père Georges-Antoine Belcourt signale des groupes métis importants autour de la rivière Souris et de la Montagne à la Tortue.", '100', KR)

# ---- Roby, Nouvelle-Angleterre p. 123-132 ; Lamarre et St-Hilaire, Midwest p. 133-142
YR = "Roby, Yves, avec Yves Frenette, « L'émigration canadienne-française vers la Nouvelle-Angleterre, 1840-1930 »"
F('ne01', 'Woonsocket et Southbridge : filière de Saint-Ours', 'migration', '1815/1850', -72.033, 42.075, 'c', [],
  "Des familles de Saint-Ours s'établissent près de Woonsocket dès 1815 ; en 1850, 70 % des Canadiens de Southbridge viennent de Saint-Ours, qui fournit aussi 27 % des migrants de Woonsocket.", '125; 126', YR)
F('ne02', 'Winooski : American Woolen Mills', 'migration', '1901/1954', -73.185, 44.49, 'c', [],
  "Près de Burlington, les chutes de la Winooski actionnent les premières usines textiles du Vermont ; intégrées à l'American Woolen Company en 1901, elles ferment en 1954. En 1860, le Vermont réunissait 44 % des Canadiens de la Nouvelle-Angleterre.", '125; 129', YR)
F('ne03', 'Lewiston : régions d\'origine', 'migration', '1860/1900', -70.215, 44.1, 'c', [],
  "De 1860 à 1900, 37 % des migrants québécois de Lewiston viennent de la Beauce et des Bois-Francs. En 1900, 573 000 Canadiens français vivent en Nouvelle-Angleterre ; environ la moitié des migrants rentreraient au Québec.", '128; 129', YR)
F('ne04', 'Fall River : crises du coton', 'evenement', '1900/1904', -71.155, 41.701, 'c', [],
  "Baisses de salaires lors des surproductions de 1900-1901 et 1903-1904 à Fall River ; les patrons résistent aux hausses en 1902. La crise de 1929 met fin à l'émigration vers la Nouvelle-Angleterre.", '131; 132', YR)
JL = "Lamarre, Jean et Marc St-Hilaire, « Les Canadiens français du Midwest américain »"
F('mw01', 'Détroit : paroisse Sainte-Anne (1809)', 'religion', '1809', -83.045, 42.331, 'c', [],
  "Dès 1809 est créée à Détroit la paroisse Sainte-Anne, première paroisse canadienne-française du Midwest ; l'arrivée de catholiques irlandais crée ensuite des tensions.", '135', JL)
F('mw02', 'Green Bay : maison Grignon', 'famille', '1813', -88.07, 44.39, 'a', ['Antoine Grignon', 'Dominique Ducharme'],
  "Antoine Grignon achète en 1813 une maison au commerçant de fourrures Dominique Ducharme. En 1860, le Midwest abrite 45 000 Canadiens français, près de la moitié de ceux des États-Unis ; 190 000 au début du XXe siècle.", '133', JL, "Localisation : Kaukauna (Fox River).")
F('mw03', 'Pierre Bottineau : colonies jusqu\'à la rivière Rouge', 'etablissement', '1850/1895', -96.274, 47.882, 'c', ['Pierre Bottineau'],
  "À partir de 1850, la famille de l'ancien trappeur Pierre Bottineau fonde trois colonies entre Minneapolis et la rivière Rouge ; il meurt à Red Lake Falls en 1895, après avoir contribué à Emardville, Crookston, Huot, Terrebonne… À Gentilly, la messe est dite en français jusque dans les années 1950.", '136; 137', JL)
F('mw04', 'Bay City et Saginaw : paroisses nationales', 'religion', '1868/1874', -83.888, 43.594, 'c', [],
  "Saint-Joseph de Bay City (1868) et Sainte-Marie de Saginaw (1874) servent les bûcherons et ouvriers canadiens ; plusieurs détiennent des postes électifs à Bay City au milieu des années 1880.", '138', JL)
F('mw05', 'Lake Linden et Calumet : mineurs du cuivre', 'religion', '1871/1891', -88.405, 47.19, 'c', ['François Mailhot'],
  "Paroisses Saint-Joseph de Lake Linden (1871) et Saint-Louis de Calumet (1884) ; François Mailhot, arrivé en 1881, est chef de police en 1891, année où trois Canadiens sont élus conseillers.", '139', JL)
F('mw06', 'Saint Paul : paroisse du père Galtier et Saint-Louis-de-France', 'religion', '1840/1885', -93.09, 44.95, 'c', ['Lucien Galtier', 'Louis Labrosse'],
  "La paroisse Saint-Paul, qui donne son nom à la ville, est instituée par le père Lucien Galtier en 1840 ; les Canadiens s'en donnent une nationale, Saint-Louis-de-France, en 1868 (école en 1873), pour 4 000 personnes vers 1885. Louis Labrosse, de l'île Bizard, y émigre en 1884.", '138; 140', JL)
F('mw07', 'Chicago : paroisses canadiennes', 'religion', '1850/1882', -87.632, 41.879, 'c', [],
  "Saint-Louis (1850, devenue irlandaise dans les années 1860), Notre-Dame (1864), Saint-Jean-Baptiste (1882)… Notre-Dame abrite des écoles et institutions francophones de 1865 au milieu des années 1880.", '140', JL)

# ---- Rivard, Plaines ; Foucrier, Californie ; Weil, migrants français
F('pl01', 'Saint-Pierre-Jolys : abbé Jean-Marie Jolys', 'etablissement', '1879~', -96.98, 49.44, 'c', ['Jean-Marie Jolys'],
  "Vers la fin des années 1870, des colons guidés par l'abbé français Jean-Marie Jolys fondent Saint-Pierre, à 60 km au sud de Saint-Boniface ; la grande vague vers les Prairies déferle entre 1897 et 1920.", '155', "Rivard, Étienne, « Diversification culturelle et dispersion spatiale dans les plaines de l'Ouest »")
AF = "Foucrier, Annick, « Français et Canadiens français en Californie »"
F('ca01', 'San Francisco : Société française de bienfaisance mutuelle', 'etablissement', '1851/1869', -122.408, 37.788, 'c', [],
  "Fondée en 1851 et devenue mutuelle en 1853, la société compte en 1869 3 887 membres, dont 2 601 Français et 60 Canadiens. Une compagnie de pompiers Lafayette est organisée en 1853.", '174; 175', AF)
F('ca02', 'San Francisco : Notre-Dame-des-Victoires', 'religion', '1856', -122.404, 37.791, 'c', ['Dominique Blaive'],
  "L'église française Notre-Dame-des-Victoires est fondée en 1856 sous l'impulsion de l'abbé Dominique Blaive ; une église Jeanne-d'Arc suit en 1910.", '175', AF)
F('ca03', 'Los Angeles : Prudent Beaudry, maire', 'personnage', '1875', -118.243, 34.052, 'c', ['Prudent Beaudry'],
  "Conseiller municipal depuis 1873, le Canadien Prudent Beaudry, dont un frère fut maire de Montréal, est élu maire de Los Angeles en 1875 ; il est le grand promoteur de Bunker Hill. En 1859, Los Angeles passait pour « aussi française que La Nouvelle-Orléans ».", '175; 176; 177', AF)
F('ca04', 'Los Angeles : Jean-Louis Sainsevain et l\'aqueduc', 'commerce', '1863', -118.237, 34.05, 'a', ['Jean-Louis Sainsevain', 'Damien Marchesseault'],
  "Arrivé en 1850, le Bordelais Jean-Louis Sainsevain construit en 1863, avec le maire Damien Marchesseault, le premier réseau d'adduction d'eau ; son vignoble de la rue Aliso est célèbre.", '176; 178', AF)
F('ca05', 'Los Angeles : Union Saint-Jean-Baptiste', 'migration', '1923', -118.243, 34.052, 'c', ['Napoléon Bissonnette'],
  "Les Canadiens français arrivent nombreux dans les années 1920 ; en 1923, Napoléon Bissonnette, après 46 ans en Nouvelle-Angleterre, organise à Los Angeles un chapitre de l'Union Saint-Jean-Baptiste.", '178', AF)
F('fr01', 'New York : le quartier français', 'etablissement', '1840/1880', -74.004, 40.722, 'a', [],
  "Un quartier français existe dans le bas Manhattan dès les années 1840 (Scribner's Monthly, 1879) ; New York compte près de 10 000 natifs de France en 1880.", '171', "Weil, François, « Les migrants français et leurs communautés aux États-Unis »")

fiches = C.fiches
