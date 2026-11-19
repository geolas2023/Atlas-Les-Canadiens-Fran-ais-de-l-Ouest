# John Francis McDermott (dir.), Frenchmen and French Ways in the Mississippi Valley (Urbana, University of Illinois Press, 1969),
# actes du second colloque de Saint-Louis ; PDF fourni par l'auteur de l'atlas le 19 novembre 2026. Corpus « Recherches », préfixe FFW69.
# Résumés rédigés par l'atlas ; chaque fiche nomme l'article (auteur, titre) dont elle est tirée.
from commun import Corpus
FW = "McDermott, John Francis (dir.) (1969), Frenchmen and French Ways in the Mississippi Valley, Urbana, University of Illinois Press"
def A(auteur, titre): return f"{auteur}, « {titre} », dans {FW}"
CHO = A("McDermott, John Francis", "Auguste Chouteau: First Citizen of Upper Louisiana")
BOU = A("Boulle, Pierre H.", "Some Eighteenth-Century French Views on Louisiana")
NIC = A("Bray, Martha Coleman", "Joseph Nicolas Nicollet, Geographer")
DUB = A("Faherty, William Barnaby", "The Personality and Influence of Louis William Valentine Du Bourg")
MAS = A("Fortier, John B.", "New Light on Fort Massac")
PIT = A("Le Gardeur, René J., Jr. et Pitot, Henry C.", "An Unpublished Memoir of Spanish Louisiana, 1796-1802")
SUP = A("Hardy, James D., Jr.", "The Superior Council in Colonial Louisiana")
DAU = A("Holmes, Jack D. L.", "Dauphin Island in the Franco-Spanish War, 1719-22")
BIR = A("McWilliams, Richebourg Gaillard", "Iberville at the Birdfoot Subdelta: Final Discovery of the Mississippi River")
STG = A("Porterfield, Neil H.", "Ste. Genevieve, Missouri")
PON = A("Rule, John C.", "Jérôme Phélypeaux, Comte de Pontchartrain, and the Establishment of Louisiana, 1696-1715")
SAU = A("Saucier, Walter J. et Seineke, Kathrine Wagner", "François Saucier, Engineer of Fort de Chartres, Illinois")
BRO = A("Wilson, Samuel, Jr.", "Ignace François Broutin")
C = Corpus('Recherches', 'FFW69', FW, page_fmt='p. {}')
F = C.F
SL = (-90.1885, 38.6275)
NO = (-90.0630, 29.9580)
MOB = (-88.0430, 30.6900)
CH = (-90.1580, 38.0860)   # fort de Chartres (le fort de pierre)
SG = (-90.0430, 37.9790)   # Sainte-Geneviève (nouvelle ville)

# --- Auguste Chouteau (McDermott)
F('01', "Saint-Louis : Auguste Chouteau dirige le défrichement du site (15 février 1764)", 'etablissement', '1764-02-15', *SL, 'a', ['Auguste Chouteau', 'Pierre de Laclède Liguest'],
  "McDermott ouvre son portrait sur le jeune Auguste Chouteau, à peine quatorze ans, qui conduit le 15 février 1764 l'équipe chargée de dégager le site choisi par Laclède. Né à La Nouvelle-Orléans de René Chouteau, originaire de L'Hermenault en Vendée, et de Marie-Thérèse Bourgeois, il est élevé sans son père ; en septembre 1764, il fait venir de Cahokia sa mère et ses quatre cadets.",
  None, "Position au site de la place du marché coloniale.", source=CHO)
F('02', "Saint-Louis : Chouteau rebâtit la maison de pierre de Laclède (1789) et obtient le monopole de la traite osage (1794-1800)", 'commerce', '1789/1800', -90.1880, 38.6265, 'a', ['Auguste Chouteau', 'Pierre Chouteau', 'François-Louis Hector de Carondelet'],
  "Après la mort de Laclède en 1778, Chouteau hérite de la conduite des affaires. En 1789, il reconstruit en grande résidence la maison de pierre du fondateur, qu'il habitera quarante ans et que la lithographie de J. C. Wild (1841) montre peu avant sa démolition. Son plus beau succès de la fin du régime espagnol est le monopole de la traite avec les Osages, accordé par Carondelet pour six ans (1794-1800) ; en 1797, il reçoit aussi 2 160 arpents sur le Missouri, voisins de ceux de son frère Pierre.",
  None, "Position du bloc de la maison Laclède-Chouteau.", source=CHO)
F('03', "Saint-Louis : Chouteau, commissaire aux traités avec les nations du Nord après 1815", 'evenement', '1815/1816', *SL, 'a', ['Auguste Chouteau', 'William Clark', 'Ninian Edwards'],
  "En 1804, Chouteau préside le comité de cinq notables chargé des rapports avec Washington ; après la guerre de 1812, il siège comme commissaire des États-Unis avec les gouverneurs William Clark et Ninian Edwards pour conclure les traités avec les nations du Nord, et rédige le 21 février 1816 un mémoire précieux sur l'emplacement des différentes nations.",
  None, "Position à Saint-Louis.", source=CHO)
F('04', "Saint-Louis : la bibliothèque de Chouteau et la visite de La Fayette (1778-1825)", 'personnage', '1778/1825', -90.1880, 38.6268, 'a', ['Auguste Chouteau', 'La Fayette', 'Henry Marie Brackenridge'],
  "Dès 1778, à la vente des biens de Laclède, Chouteau achète des livres (dont La Nouvelle Héloïse et les Essais de Bacon) et dix-sept volumes d'histoire ecclésiastique à la vente Hubert. Brackenridge le décrit en 1810 comme un homme vénérable à la belle tête intellectuelle. En 1825, il accueille La Fayette, qui lève son verre au « patriarche » fondateur de la ville.",
  None, "Position de la maison Chouteau.", source=CHO)

# --- Boulle : opinion française sur la Louisiane
F('05', "La Louisiane vue de France : mémoires de 1758-1762 sur la transmigration des Canadiens", 'migration', '1758/1762', -90.06, 29.96, 'h', ['Rivoire', 'Henri Pouillard', 'Choiseul'],
  "Boulle dépouille les mémoires adressés aux ministres pendant la guerre de Sept Ans : plusieurs projets de 1761 proposent de faire passer les habitants du Canada en Louisiane (« Moyen de peupler la Louisianne »), d'autres, comme celui de Pouillard, d'y développer population et commerce. Contrairement à l'image d'une Louisiane méprisée, l'auteur montre que sa valeur était tenue pour acquise dans les années 1750, avant la cession de Fontainebleau (novembre 1762).",
  None, "Point symbolique à La Nouvelle-Orléans : l'objet est un débat métropolitain.", source=BOU)

# --- Nicollet (Bray)
F('06', "Fort Snelling : Joseph Nicolas Nicollet hiverne et cartographie les sources du Mississippi (1836-1837)", 'exploration', '1836/1837', -93.181, 44.893, 'c', ['Joseph Nicolas Nicollet'],
  "Né en Savoie en 1786, savant ruiné par la crise de 1830, Nicollet arrive aux États-Unis en 1832. À l'été 1836, après quatre ans de voyages, il est au fort Snelling ; il y passe l'hiver 1836-1837 pour mettre au net ses relevés des sources du Mississippi, et son journal témoigne de relations sympathiques avec les Autochtones.",
  None, "Position du fort Snelling.", source=NIC)
F('07', "Coteau des Prairies : l'expédition Nicollet-Frémont vers le Missouri (1838-1839)", 'exploration', '1838/1839', -97.0, 44.5, 'h', ['Joseph Nicolas Nicollet', 'John Charles Frémont'],
  "En avril 1838, le Bureau des ingénieurs topographes achète la carte de Nicollet et le charge de couvrir le pays jusqu'au Missouri ; le jeune lieutenant Frémont devient son assistant. La carte qui en résulte (publiée en 1843, rééditée en 1845) est d'une exactitude remarquable : un arpenteur ferroviaire de 1882 n'y trouve que dix à quinze pieds d'écart sur les altitudes, notamment au fort Pierre.",
  None, "Point au cœur de la région cartographiée (Coteau des Prairies).", source=NIC)

# --- Du Bourg (Faherty)
F('08', "Saint-Louis : l'évêque Du Bourg fonde l'académie qui deviendra le collège Saint-Louis (1818-1820)", 'religion', '1818/1820', -90.1868, 38.6245, 'a', ['Louis-Guillaume-Valentin Du Bourg'],
  "Né à Saint-Domingue le 14 février 1766, sulpicien ordonné en 1788, réfugié au Maryland en 1794, Du Bourg est sacré à Rome, à Saint-Louis-des-Français, le 24 septembre 1815. Installé à Saint-Louis, il ouvre à l'automne 1818 une académie de garçons près de l'église, qui prend en 1820 le nom de collège Saint-Louis, l'année où il bénit la nouvelle église.",
  None, "Position de l'ancienne église (actuelle Old Cathedral).", source=DUB)
F('09', "Perryville : le séminaire Sainte-Marie des Barrens incorporé (1822)", 'religion', '1822-11-28', -89.858, 37.722, 'a', ['Louis-Guillaume-Valentin Du Bourg', 'Joseph Rosati'],
  "La législature du Missouri incorpore à la fin de 1822 le séminaire Sainte-Marie des Barrens, fondé sous Du Bourg, qui accueille aussi des élèves laïcs. En 1823, Du Bourg présente à Washington un projet d'école autochtone jointe à un centre de formation missionnaire près du confluent du Missouri et du Mississippi.",
  None, "Position du séminaire à Perryville.", source=DUB)

# --- Fort Massac (Fortier)
F('10', "Fort Massiac (Massac) sur l'Ohio : construction et garnison françaises (1757-1764)", 'poste', '1757/1764', -88.705, 37.147, 'c', ['Macarty', 'Philippe-François de Rastel de Rocheblave', 'Kerlerec'],
  "Fortier reconstitue l'histoire du fort élevé au printemps 1757 sur l'Ohio, aussi près que possible du Tennessee, sur ordre du commandant des Illinois ; il est attaqué par des Autochtones dès 1757. Bâti en pièce sur pièce, il reçoit en mai 1760 une expédition de deux bateaux et cinquante soldats et habitants menée par Rocheblave. En décembre 1763, la garnison est réduite à un officier et quinze hommes et cinq des huit canons passent à Sainte-Geneviève ; les Britanniques ne l'atteignent qu'en 1765, abandonné. L'auteur écarte toute dérivation du nom à partir de « massacre ».",
  None, "Position du site du fort Massac (Metropolis, Illinois).", source=MAS)
F('11', "Ohio inférieur : le poste de Juchereau de Saint-Denys près de Mound City (1702)", 'poste', '1702', -89.16, 37.08, 'h', ['Charles Juchereau de Saint-Denys'],
  "Avec au moins vingt-cinq hommes, Juchereau de Saint-Denys atteint le pays des Illinois à la fin de 1702 et établit un poste près de l'embouchure de l'Ohio, que l'on situe aux environs de Mound City ; Fortier le rappelle comme antécédent français du fort Massac.",
  None, "Position hypothétique (Mound City, Illinois).", source=MAS)

# --- Pitot (Le Gardeur & Pitot)
F('12', "La Nouvelle-Orléans : James Pitot et ses « Observations sur la colonie de la Louisiane de 1796 à 1802 »", 'personnage', '1796/1802', *NO, 'a', ['James Pitot', 'Pierre Derbigny', 'Carondelet'],
  "Né à Villedieu-les-Poêles (Normandie) en 1761, Jacques-François (James) Pitot passe par Saint-Domingue, gagne les États-Unis en 1793 et arrive à La Nouvelle-Orléans en août 1796. Négociant (Lanthois & Pitot), il rédige un mémoire inédit de 76 pages, conservé au Havre, qui juge l'administration espagnole de Carondelet à Salcedo et l'économie coloniale (indigo, sucre établi en 1796, plomb des Illinois, pelleteries). Il sera maire de La Nouvelle-Orléans en 1804-1805.",
  None, "Position au Vieux Carré.", source=PIT)

# --- Conseil supérieur (Hardy)
F('13', "La Nouvelle-Orléans : le Conseil supérieur, cour et greffe de la colonie (1712-1747)", 'evenement', '1712/1747', -90.0640, 29.9575, 'a', ['Antoine Crozat', 'Fleuriau', 'Jean-Baptiste Raguet', 'Louis Robineau de Portneuf'],
  "Créé en 1712, rendu permanent en 1716 et remanié en 1719 pour la Compagnie des Indes, le Conseil supérieur réunit gouverneur, commissaire, procureur général et conseillers. Hardy montre qu'en 1744 il consacre plus de la moitié de son temps aux actes notariés et aux successions : procurations (le commandant des Natchitoches, de Blanc, à sa femme en 1746), contrats de mariage (Voisin et Denis de Bonaventure, 1745), successions disputées (d'Ausseville, Roquigny) et procédures criminelles réglées sur l'ordonnance de 1670.",
  None, "Position de la place d'Armes.", source=SUP)

# --- Île Dauphine (Holmes)
F('14', "Île Dauphine : port de la Louisiane, raids et guerre franco-espagnole (1699-1722)", 'poste', '1699/1722', -88.110, 30.250, 'c', ["Pierre Le Moyne d'Iberville", 'Jean-Baptiste Le Moyne de Bienville', 'Antoine de La Mothe Cadillac', 'Andrés de Pez'],
  "Iberville mouille devant l'île le 31 janvier 1699 ; nommée île Massacre puis Dauphine (1701), elle devient le port de la colonie après le transfert depuis Biloxi en 1702. Un corsaire jamaïcain la pille en septembre 1710 ; l'ouragan de 1717 bouche le port et coupe l'île en deux. Pendant la guerre de la Quadruple-Alliance, elle sert de base contre Pensacola, prise en 1719, puis rendue et détruite le 26 novembre 1722.",
  None, "Position de l'île Dauphine (Alabama).", source=DAU)

# --- Iberville au delta (McWilliams)
F('15', "Passe de l'Est du Mississippi : Iberville entre dans le fleuve par la « palissade » (2 mars 1699)", 'exploration', '1699-03-02', -89.20, 29.15, 'a', ["Pierre Le Moyne d'Iberville", 'Carlos de Sigüenza y Góngora'],
  "McWilliams étudie la « palissade » de troncs à l'embouchure qui donna aux Espagnols le nom de Río de la Palizada : les expéditions espagnoles de 1686 à 1693 voient les passes sans y entrer. Le 2 mars 1699, par gros temps, Iberville pénètre par la passe de l'Est et remonte le fleuve découvert par La Salle en 1682 ; les datations au carbone 14 donnent à ce delta d'oiseau environ 240 ans d'âge à l'époque.",
  None, "Position approximative de l'ancienne passe de l'Est.", source=BIR)

# --- Sainte-Geneviève (Porterfield)
F('16', "Sainte-Geneviève : maisons coloniales Bequette-Ribault, Janis, Amoureux, Vallé et Huberdeau (1780-1811)", 'etablissement', '1780/1811', *SG, 'c', ['Jean-Baptiste Bequette', 'Nicolas Janis', 'François Janis', 'Mathurin Michel Amoureux', 'François Vallé II', 'Jean-Baptiste Vallé', 'Jean-Baptiste Huberdeau', 'Jean-Baptiste Moreau'],
  "L'inventaire de Porterfield décrit les maisons françaises du village : la maison Bequette-Ribault en poteaux en terre (avant 1780), la maison Janis sur sole (vers 1790, concession confirmée à Nicolas Janis en 1771), la maison Amoureux, celle du commandant François Vallé II (mort en 1804), la maison de pierre de Huberdeau (vers 1800) et la maison Vallé achetée par Jean-Baptiste Vallé après 1811.",
  None, "Position du centre historique de Sainte-Geneviève.", source=STG)
F('17', "Sainte-Geneviève : les Français de la rive gauche passent le fleuve (1763 et 1799)", 'migration', '1763/1799', SG[0]+0.005, SG[1]+0.004, 'a', ['André de Guire dit La Rose', 'Moses Austin'],
  "Après le traité de 1763, beaucoup de Français des Illinois traversent vers Sainte-Geneviève, croyant la rive ouest restée française ; un second mouvement suit l'arrivée de l'autorité américaine. Le plus ancien acte connu du registre est le mariage d'André de Guire dit La Rose en 1759. Moses Austin y possède une maison de 1799 à 1811.",
  None, "Position à Sainte-Geneviève.", source=STG)
F('18', "Mine La Motte : première permission de mines de plomb accordée à Renault (1723)", 'commerce', '1723', -90.39, 37.55, 'a', ['Philippe-François Renault'],
  "Porterfield rappelle que les officiers du fort de Chartres accordent en 1723 à Philippe-François Renault la première permission d'exploiter les mines de plomb du futur Missouri, base de la vie économique de Sainte-Geneviève.",
  None, "Position de Mine La Motte (Missouri).", source=STG)

# --- Pontchartrain (Rule)
F('19', "Versailles et le golfe : Jérôme de Pontchartrain prépare l'expédition d'Iberville (1696-1699)", 'exploration', '1698/1699', -88.86, 30.39, 'h', ['Jérôme Phélypeaux de Pontchartrain', "Pierre Le Moyne d'Iberville", 'Henri Joutel', 'Henri de Tonti'],
  "Rule montre que Jérôme Phélypeaux dirige en fait la Marine dès 1696 et crée un Dépôt des cartes et plans. Alarmé par les avertissements de l'abbé Cavelier et de Tonti sur une avancée anglaise, il fait chercher la relation de Joutel à Rouen, choisit Iberville, vainqueur de la baie d'Hudson (1697), et lui fournit cartes et mémoires. Iberville mouille à Pensacola le 26 janvier 1699 avant de longer la côte vers le Mississippi.",
  None, "Point sur la côte de Biloxi, premier établissement issu de l'expédition.", source=PON)
F('20', "Mobile : Crozat reçoit la Louisiane, Cadillac gouverneur (1712-1717)", 'commerce', '1712/1717', *MOB, 'a', ['Antoine Crozat', 'Antoine de La Mothe Cadillac', 'Jean-Baptiste Le Moyne de Bienville'],
  "Après les difficultés de la guerre de Succession d'Espagne, Pontchartrain confie l'administration financière de la Louisiane au banquier Antoine Crozat, qui l'exploite comme une affaire jusqu'en 1717, et nomme Cadillac gouverneur pour contrebalancer l'influence des Canadiens autour de Bienville.",
  None, "Position du fort Louis de Mobile.", source=PON)

# --- Saucier (Saucier & Seineke)
F('21', "Mobile : famille Saucier, d'origine québécoise (vers 1700-1743)", 'famille', '1700/1743', *MOB, 'a', ['François Saucier', 'Jean Saucier', 'Gabrielle Savary', 'Marie Jeanne Fontaille', 'Louis Saucier'],
  "Les auteurs, descendants de l'ingénieur, retracent la famille : Louis Saucier, de la garnison de Québec (1666), épouse la veuve Prévost ; son fils Jean, marchand du fort Louis de Mobile, témoigne pour Bienville en 1708 et épouse Gabrielle Savary. Leur fils François, né vers 1712 à Mobile, dessine à seize ans un plan de La Nouvelle-Orléans (12 mai 1728), étudie à Paris et épouse Marie-Jeanne Fontaille à Mobile en 1743. Son frère utérin Vifvarenne et Henry Saucier s'établissent aux Illinois.",
  None, "Position du fort Condé de Mobile.", source=SAU)
F('22', "Campagnes chicachas : Saucier relève les routes vers les villages chicachas (1737-1740)", 'exploration', '1737/1740', -89.52, 34.36, 'h', ['François Saucier', 'Bernard Deverges', 'Ignace François Broutin', 'Jean-Baptiste Le Moyne de Bienville'],
  "Dessinateur auprès des ingénieurs Deverges et Broutin, Saucier part en 1738 avec Coustilhas, puis explore avec 200 Autochtones la route vers les forts chicachas. La Carte particulière signée à La Nouvelle-Orléans le 27 juin 1740 par Broutin, Deverges et Saucier trace ses routes jusqu'au Tallahatchie, au nord de l'actuelle Oxford.",
  None, "Point au Tallahatchie au nord d'Oxford (Mississippi), d'après la description de la carte.", source=SAU)
F('23', "Fort Toulouse des Alibamons : Saucier y travaille et y voit naître sa fille (1749-1750)", 'poste', '1749/1750', -86.255, 32.507, 'c', ['François Saucier', 'Marie Jeanne Fontaille'],
  "Une fille, Marie-Jeanne, naît « aux Alibamons » le 19 février 1749 à François Saucier, sous-ingénieur du roi, preuve que la famille hivernait avec lui au fort Toulouse ; en janvier 1750, Vaudreuil note encore qu'il y est. En 1742, il avait aussi inspecté le poste de Tombecbé.",
  None, "Position du fort Toulouse (Wetumpka, Alabama).", source=SAU)
F('24', "Fort de Chartres : François Saucier, ingénieur du nouveau fort de pierre (1751-1757)", 'poste', '1751/1757', *CH, 'c', ['François Saucier', 'Macarty', 'Vaudreuil'],
  "Envoyé aux Illinois en 1751 avec Macarty, Saucier fait le choix du site, près de Prairie du Rocher, et dresse les plans du nouveau fort de Chartres ; ses lettres de 1752 à Vaudreuil sont conservées à la Huntington Library. Il meurt le 26 février 1757. Le Britannique Pittman jugera le fort « le plus commode et le mieux bâti d'Amérique du Nord » ; il est cédé au capitaine Stirling le 10 octobre 1765 par Louis Saint-Ange.",
  None, "Position du fort de Chartres (État de l'Illinois).", source=SAU)
F('25', "Cahokia : les fils et filles de Saucier après la cession (1774-1782)", 'famille', '1774/1782', -90.190, 38.571, 'a', ['François Saucier (fils)', 'Marguerite Cadron', 'Félicité Saucier', 'Antoine Damour de Louvière', 'Mathieu Saucier'],
  "Les registres de Sainte-Anne et de Cahokia montrent la famille restée au pays : Félicité Saucier épouse Antoine Damour de Louvière en 1775 ; François fils, officier réformé, épouse Marguerite Cadron, fille d'un capitaine de milice, en 1774 ; Mathieu fait baptiser une fille en 1782. Trois fils serviront à la cour de Cahokia sous le régime américain.",
  None, "Position du village de Cahokia.", source=SAU)

# --- Broutin (Wilson)
F('26', "Biloxi : Ignace François Broutin arrive avec la concession Le Blanc (22 septembre 1720)", 'etablissement', '1720-09-22', -88.885, 30.395, 'a', ['Ignace François Broutin', 'Claude Le Blanc', 'La Tour'],
  "Cartographe de l'Alsace, nommé capitaine, Broutin recrute deux compagnies pour la concession de Le Blanc, Belle-Isle et d'Asfeld et arrive à Biloxi sur l'Alexandre le 22 septembre 1720, premier architecte-ingénieur important à gagner la colonie, avant Pauger.",
  None, "Position du Nouveau-Biloxi.", source=BRO)
F('27', "Natchez : Broutin commande la concession de la Terre Blanche (1722-1729)", 'etablissement', '1722/1729', -91.37, 31.50, 'h', ['Ignace François Broutin', 'Gonichon', 'Charles-Henri Desliettes de Tonti'],
  "Envoyé aux Natchez en 1722 pour cartographier la concession de la Terre Blanche, Broutin s'y méfie des Natchez et conseille une action ferme ; en 1729, il y conduit sept esclaves et laisse Gonichon, l'un des rares rescapés du soulèvement du 28 novembre 1729. Il dresse ensuite un plan du siège des deux forts natchez de février 1730.",
  None, "Position hypothétique de la concession de la Terre Blanche, au sud de Natchez.", source=BRO)
F('28', "La Nouvelle-Orléans : Broutin, ingénieur du roi, et le couvent des Ursulines (1731-1751)", 'religion', '1731/1751', -90.0605, 29.9610, 'c', ['Ignace François Broutin', 'Pierre Baron', 'Bienville', 'Vaudreuil', 'Micaela Almonester de Pontalba'],
  "Ingénieur du roi après le départ de Baron (1731), Broutin dessine les casernes de la place d'Armes (1732-1738), le mur de la poudrière, le chai de l'intendance et, le 10 novembre 1745, le second couvent des Ursulines, seul édifice du régime français encore debout en Louisiane. Il meurt le 9 août 1751 ; son arrière-petite-fille, la baronne de Pontalba, bâtira en 1849-1850 les immeubles Pontalba à l'emplacement de ses casernes.",
  None, "Position du couvent des Ursulines (rue Chartres).", source=BRO)
F('29', "Natchitoches : plan d'un fort de pieux par Broutin (1733-1734)", 'poste', '1733/1734', -93.087, 31.758, 'a', ['Ignace François Broutin', 'Louis Juchereau de Saint-Denis'],
  "Broutin dessine le 15 janvier 1733 le poste de Saint-Jean-Baptiste des Natchitoches et rédige le 1er mars 1734 le devis d'un nouveau fort de pieux confié au constructeur Le Brun ; Saint-Denis, Canadien fondateur du poste, en est alors le commandant.",
  None, "Position du fort Saint-Jean-Baptiste (Natchitoches).", source=BRO)
F('30', "Mobile : réparations du fort Condé sur devis de Broutin (1741-1752)", 'poste', '1741/1752', -88.040, 30.689, 'c', ['Ignace François Broutin', 'Dubreuil', 'De Batz'],
  "Venu à Mobile en 1741, Broutin propose une caserne à deux niveaux et l'épaississement du parapet ; le contrat de réparations de Dubreuil (23 décembre 1742) suit son devis, et De Batz relève les bâtiments achevés en 1752.",
  None, "Position du fort Condé.", source=BRO)

fiches = C.fiches
