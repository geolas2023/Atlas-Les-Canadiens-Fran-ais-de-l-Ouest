# Sous-dossiers du dossier Drive 1Tx_c-qfEHYTeJ1tNBsBm4TJxWiCiZWiV (42 dossiers, dépouillement du 20 nov. 2026).
# Fichiers téléchargés en entier et lus localement (pdftotext, epub, OCR tesseract pour les scans) ;
# gros fichiers (> 10 Mo) lus par l'outil du Drive, en partie seulement.
# Préfixes : WT05, MT02 (suite), DN10 (suite), TU15 (suite), FC13, KN61, NPS90, GZ63, WT09, JO03.
from commun import Corpus

WT05 = "Cook, Mary Jean (2005), « ¿Porque Monterrey? The Death and Mysterious Burial of Merchant Manuel Alvarez, Part I », Wagon Tracks, vol. 19, n° 3 (mai 2005)"
MT02 = "Montoya, María E. (2002), Translating Property: The Maxwell Land Grant and the Conflict over Land in the American West, 1840-1900, Berkeley, University of California Press"
DN10 = "Dionne, N.-E. (1910), Chouart et Radisson : odyssée de deux Canadiens-français au XVIIe siècle, Québec, Laflamme et Proulx"
TU15 = "Turner, Glenn (2015), The Toronto Carrying Place: Rediscovering Toronto's Most Ancient Trail, Toronto, Dundurn"
FC13 = "Gitlin, Jay, Barbara Berglund et Adam Arenson (dir.) (2013), Frontier Cities: Encounters at the Crossroads of Empire, Philadelphie, University of Pennsylvania Press"
KN61 = "Kane, Paul (1861), Les Indiens de la baie d'Hudson. Promenades d'un artiste parmi les Indiens de l'Amérique du Nord, imité de l'anglais par Édouard Delessert, Paris, Amyot (éd. orig. Wanderings of an Artist, 1859)"
NPS90 = "National Park Service (1990), Santa Fe National Historic Trail: Comprehensive Management and Use Plan, Denver, NPS, appendice C"
GZ63 = "Santa Fe Weekly Gazette, 27 juin 1863, « Navajo Indians » (coupure, Drive de l'auteur, dossier MERCURE_BROTHERS_SANTA_FE)"
WT09 = "Gutierrez, Priscilla Shannon (2009), « Out from the Shadow of Giants: The Life of Thomas Oliver Boggs », Wagon Tracks, vol. 23, n° 3 (mai 2009)"
JO03 = "Joly, Éric (2003), L'identité culturelle des jeunes Franco-Américains de Berlin, au New Hampshire, mémoire de maîtrise (géographie), Université d'Ottawa"

C1 = Corpus('Recherches', 'WT05', WT05); F = C1.F
F('01', "Santa Fe : Manuel Alvarez, le magasin des Mercure et l'acte d'inhumation (juin-juillet 1856)", 'personnage', '1856-06/1856-08', -105.9378, 35.6870, 'c',
  ['Manuel Alvarez', 'Henry Mercure', 'Joseph Mercure', 'Étienne Avel'],
  "Vingt jours avant sa mort, le 5 juillet 1856, le marchand espagnol Manuel Alvarez, trop faible pour traverser la place, envoie un messager au « Sr. Dn. H. Mercure », dont le magasin-cantina occupe le côté sud de la place de Santa Fe depuis les années 1840, pour obtenir 24 varas de toile de lin de bonne qualité, sans doute pour son linceul. L'établissement appartient aux frères canadiens-français Henry et Joseph Mercure ; c'est là qu'Aubry avait été tué en 1854. L'acte de sépulture rédigé par le prêtre français Étienne Avel a pour témoins Carlos [Blumner ?] et José Mercure ; il ne donne aucun lieu d'inhumation, et Alvarez ne fut pas enterré à Santa Fe. Cook voit dans Avel, Blumner et Joseph Mercure des complices informés du secret de cette sépulture.",
  '6-7', "Point sur la place de Santa Fe.")
F('02', "Ocate : Joseph Mercure témoigne pour la concession d'Alvarez (1861)", 'personnage', '1861', -105.05, 36.18, 'a',
  ['Joseph Mercure', 'Manuel Alvarez'],
  "Dans le dossier de la concession d'Ocate, Joseph Mercure déclare sous serment devant l'arpenteur général, en 1861, qu'il connaît Manuel Alvarez depuis 1848. Il rapporte que le marchand avait eu trois fils, dont un mort, d'une Autochtone « dans les montagnes Rocheuses », qu'il disait avoir épousée selon la coutume indienne, et qu'à son retour d'Europe en décembre 1855 Alvarez lui avait dit avoir vu ses deux fils en Espagne.",
  '8', "Déposition de Joseph Mercure, Ocate Land Claim, Land Grant Records, bobine 26, NMSA, d'après Cook (note 27). Point approximatif à Ocate (comté de Mora) ; le lieu de la déposition n'est pas précisé.")

C2 = Corpus('Recherches', 'MT02', MT02); F = C2.F
F('10', "San Luis : l'acte de 1863 par lequel Carlos Beaubien garantit l'usage des communs", 'etablissement', '1863/1864', -105.4236, 37.2008, 'c',
  ['Carlos Beaubien', 'William Gilpin'],
  "En 1863, avant de vendre la concession Sangre de Cristo, Carlos Beaubien met par écrit les droits d'usage qu'il accorde aux habitants de San Luis et des établissements de la Costilla, de la Culebra et de la Trinchera : accès aux communs, au bois de chauffage et de construction, à l'eau et aux pâturages. Le contrat de vente à William Gilpin, en 1864, l'oblige à confirmer ces droits. Au XXe siècle, ce document de 1863 est au cœur du procès des habitants de San Luis contre les propriétaires du ranch Taylor ; Montoya y témoigna comme experte.",
  '1-3, 212-214', "Point à San Luis (Colorado).")

C3 = Corpus('Recherches', 'DN10', DN10); F = C3.F
F('02', "Québec, août 1660 : Chouart et Radisson arrivent avec soixante canots de fourrures", 'commerce', '1660-08', -71.2080, 46.8139, 'c',
  ['Médard Chouart des Groseilliers', 'Pierre-Esprit Radisson', 'Jérôme Lalemant'],
  "Selon la Relation de 1660, le jésuite Jérôme Lalemant trouve à Québec « deux François qui ne faisoient que d'arriver de ces païs supérieurs, avec trois cents Algonquins, dans soixante canots chargez de pelleteries ». Ils avaient hiverné sur les rivages du lac Supérieur et rapportaient des nouvelles des nations de l'Ouest, dont les restes des Hurons et des Pétuns réfugiés à six journées au sud-ouest du lac. Le Journal des Jésuites note leur passage en août 1660.",
  '59', "Point à Québec. La Relation dit que les deux Français trouvèrent les Algonquins de l'Ouest à la famine et y baptisèrent des enfants : affirmation reprise par Dionne, non vérifiée.")
F('03', "Trois-Rivières, août 1661 : Chouart, Radisson et François Larivière s'évadent du fort", 'exploration', '1661-08', -72.5477, 46.3432, 'c',
  ['Médard Chouart des Groseilliers', 'Pierre-Esprit Radisson', 'François Larivière'],
  "Le gouverneur refusant son congé, Chouart, qui commande le fort de Trois-Rivières et en garde les clefs, s'entend en août 1661 avec des Autochtones du saut Sainte-Marie venus en traite : ils l'attendront sur les bords du lac Saint-Pierre, à sept lieues de la ville. Une nuit, il ouvre les portes et s'esquive avec Radisson et un nommé François Larivière. Par le Saint-Laurent, le lac Ontario, Niagara, le lac Érié et la rivière Saint-Clair, ils gagnent le lac Supérieur pour leur second voyage dans l'Ouest. Guillaume Couture, envoyé l'été 1663, les trouva partis depuis plusieurs mois.",
  '65', "Point à Trois-Rivières.")
F('04', "Percé, 11 juillet 1682 : départ de Radisson et de Chouart pour la baie d'Hudson", 'exploration', '1682-07-11', -64.2130, 48.5240, 'c',
  ['Pierre-Esprit Radisson', 'Médard Chouart des Groseilliers', 'Jean-Baptiste Chouart', 'Pierre Allemand', 'Jean-Baptiste Godefroy', 'Charles Aubert de La Chesnaye'],
  "Financés par Aubert de La Chesnaye, Radisson et Chouart obtiennent seulement un permis de pêche au loup-marin. Radisson part de Québec le 4 novembre 1681 avec trois compagnons donnés par Frontenac : Jean-Baptiste Chouart, fils de Médard et neveu de Radisson, le pilote Pierre Allemand et l'interprète Jean-Baptiste Godefroy, et hiverne à Percé. Le 11 juillet 1682, son vaisseau et la barque de trente tonneaux de Chouart, avec quinze hommes d'équipage, quittent Percé ; Radisson atteint la côte ouest de la baie le 26 août, Chouart le 7 septembre, et tous deux entrent dans la rivière que les Autochtones nomment Kakiouakina.",
  '108-109', "Point à Percé. L'établissement sur la rivière Sainte-Thérèse (Hayes) est l'objet d'autres fiches.")
F('05', "Rivière Sainte-Thérèse, 15 juillet 1685 : le capitaine Berger apprend le retour de Radisson aux Anglais", 'evenement', '1685-07-15', -92.30, 57.00, 'a',
  ['Berger', 'Pierre-Esprit Radisson', 'Jean-Baptiste Chouart', 'John Bridger'],
  "Le 15 juillet 1685, le capitaine Berger, Canadien français, quitte l'établissement français situé à quatre lieues du poste anglais de la rivière Nelson pour revenir à Québec. En chemin, il rencontre un vaisseau anglais de dix ou douze canons, commandé par le capitaine Oslar, qui porte le gouverneur Bridger ; Oslar lui apprend que Radisson et son neveu Jean-Baptiste des Groseilliers sont rendus au fort anglais.",
  '141', "Point approximatif à l'embouchure de la Hayes (rivière Sainte-Thérèse) ; Dionne ne situe pas la rencontre en mer.")

C4 = Corpus('Recherches', 'TU15', TU15, page_fmt='{}'); F = C4.F
F('02', "Embouchure de la Humber : la maison-magasin de Jean-Baptiste Rousseau, dit Saint-Jean (1792)", 'commerce', '1792/1795', -79.4720, 43.6330, 'a',
  ['Jean-Baptiste Rousseau', 'John Graves Simcoe', 'Joseph Brant'],
  "Né en 1758 dans une famille de traiteurs canadiens-français, fils d'un coureur des bois qui commerçait avec les Mississagués à l'embouchure de la Humber, Jean-Baptiste Rousseau parle l'ojibwé, le mohawk, l'anglais et le français. Il épouse la fille adoptive du chef mohawk Joseph Brant et sert d'interprète et de guide au Département des Indiens. En 1792, il bâtit avec sa femme, au pied du portage de Toronto, sur le site du deuxième poste français abandonné, une maison qui lui sert de magasin : il est le premier colon européen de Toronto et son premier boutiquier civil. Le lieutenant-gouverneur Simcoe l'y trouve installé ; la Humber s'appelle alors « rivière Saint-Jean », d'après le surnom de Rousseau, jusqu'à ce que Simcoe la fasse renommer.",
  'chap. 4 (édition numérique non paginée)', "Point près de l'embouchure de la Humber, sur le site probable du fort Toronto.")
F('03', "Ganatsekwyagon (embouchure de la Rouge) : l'hiver des sulpiciens Fénelon et d'Urfé (1669-1670)", 'religion', '1669/1670', -79.1170, 43.7946, 'a',
  ['François de Salignac de La Mothe-Fénelon', "François-Saturnin Lascaris d'Urfé"],
  "Après la destruction de la Huronie, des Tsonnontouans fondent deux villages au pied des deux branches du portage de Toronto : Ganatsekwyagon et Teiaiagon. Les Sulpiciens Fénelon et d'Urfé passent l'hiver 1669-1670 à Ganatsekwyagon, à l'embouchure de la rivière Rouge (aujourd'hui Scarborough). Le village est abandonné, comme Teiaiagon, avant 1687.",
  'édition numérique non paginée', "Point à l'embouchure de la Rouge.")
F('04', "Baby Point (Humber) : Jacques Baby achète le site de Teiaiagon (1815)", 'personnage', '1815', -79.4935, 43.6577, 'c',
  ['Jacques Baby'],
  "Issu d'une famille canadienne-française enrichie dans la traite des fourrures au Détroit, Jacques (James) Baby, membre du Conseil exécutif et de la législature du Haut-Canada, juge et surintendant adjoint du Département des Indiens, est nommé inspecteur général de la province ; il s'installe à York en 1815 et y achète un lot de 600 hectares sur la Humber, à l'emplacement de l'ancien village tsonnontouan de Teiaiagon, aujourd'hui Baby Point. Défenseur des droits des Canadiens français dans l'ouest de la colonie, il devient le francophone le plus en vue d'York.",
  'chap. 4 (édition numérique non paginée)', "Point à Baby Point (Toronto).")

C5 = Corpus('Recherches', 'FC13', FC13); F = C5.F
F('01', "Détroit, 1703 : Pierre Roy épouse Marguerite Ouabankikoué, de la famille de Pied-Froid", 'famille', '1703', -83.0458, 42.3290, 'c',
  ['Pierre Roy', 'Marguerite Ouabankikoué', 'Pied-Froid (Wisekaukautshe)', 'François Roy', 'Étienne Roy', 'Isabelle Couc (Madame Montour)'],
  "Engagé des Jésuites dans les Pays d'en haut dès l'âge de quinze ans, Pierre Roy, fils d'un notable de La Prairie, épouse au Détroit en 1703 Marguerite Ouabankikoué, sans doute sœur du chef miami Wisekaukautshe, dit Pied-Froid, de la bande de la Grue. Leurs enfants ont pour parrains et marraines des marchands et des membres des réseaux autochtones, dont Isabelle Couc, la future Madame Montour. Deux frères de Pierre, François et Étienne, passent par le Détroit : François commerce avec lui au poste miami de Kekionga, Étienne s'établit en Louisiane.",
  '74-75', "Chapitre de Karen Marrero, « On the Edge of the West ». Point au fort Pontchartrain du Détroit.")
F('02', "Kekionga (poste des Miamis), mai 1728 : mariage de Marie-Madeleine Roy et de Pierre Chesne dit LaButte", 'famille', '1728-05', -85.1394, 41.0793, 'c',
  ['Marie-Madeleine Roy', 'Pierre Chesne dit LaButte', 'Pierre Roy', 'François Roy', 'Nicolas-Joseph de Noyelles de Fleurimont'],
  "En mai 1728, au poste des Miamis de Kekionga, Marie-Madeleine, fille de Pierre Roy et de la Miamie Marguerite Ouabankikoué, épouse Pierre Chesne dit LaButte. Le commandant du poste, Nicolas-Joseph de Noyelles de Fleurimont, signe l'acte parmi de nombreux témoins, au lendemain du jour où il a passé au poste une société avec Pierre et François Roy pour y contrôler la traite. LaButte deviendra l'interprète officiel auprès des Outaouais du Détroit et jouera un rôle de premier plan pendant le siège de Pontiac en 1763.",
  '75', "Chapitre de Karen Marrero. Point à Fort Wayne (Indiana), site de Kekionga.")
F('03', "Montréal et l'île aux Tourtes, 1713 : le procès de François Lamoureux dit Saint-Germain, contrebandier d'eau-de-vie", 'commerce', '1713', -73.9900, 45.4210, 'a',
  ['François Lamoureux dit Saint-Germain', 'René-Charles de Breslay', 'Oronhoua', 'Marie-Anne Fafard dite Macouc'],
  "À l'été 1713, à la mission nipissingue de l'ouest de l'île de Montréal, le sulpicien René-Charles de Breslay est pris à la gorge par un homme ivre d'eau-de-vie de contrebande. La cour royale de Montréal poursuit François Lamoureux dit Saint-Germain, armurier et petit marchand de la rue Saint-Paul, de mère algonquine, qui approvisionne les Autochtones en eau-de-vie, en bière, en cidre et en vin ; parmi les témoins, l'Agnier Oronhoua, contrebandier du Sault-au-Récollet, et la jeune Marie-Anne Fafard dite Macouc, d'une famille métisse du Détroit. Lamoureux, déjà poursuivi pour avoir porté en 1708 des marchandises anglaises au Détroit sous couvert d'un permis de chasse, ne perd que quelques jours en prison : la cour ne donne pas suite. En août 1715, Breslay baptise son fils à Sainte-Anne-de-Bellevue et en devient le parrain.",
  '49-65', "Chapitre de Brett Rushforth, « Insinuating Empire ». « Procès contre François Lamoureux dit Saint-Germain, armurier, accusé de vente d'eau de vie des sauvages », 1713, BAnQ-M, TL4, S1. Point approximatif à l'île aux Tourtes (mission de Breslay).")

C6 = Corpus('Recherches', 'KN61', KN61, page_fmt='{}'); F = C6.F
F('01', "Rocher de Miette (Jasper), 2 novembre 1846 : le voyageur qui fumait sa pipe au-dessus de l'abîme", 'toponymie', '1846-11-02', -117.93, 53.17, 'a',
  ['Paul Kane', 'Miette', 'Colin Fraser'],
  "Passant au pied du rocher perpendiculaire de quinze cents pieds qui ferme la brèche de la vallée de l'Athabasca, Paul Kane note que le rocher de Miette doit son nom à un voyageur qui grimpa jusqu'au sommet et s'y assit, fumant sa pipe, les jambes pendantes au-dessus du vide.",
  'chap. XI', "Kane écrit « un voyageur français ». Point à la Roche Miette (parc national de Jasper).")
F('02', "Dalles des Morts (Columbia), automne 1847 : la légende du rapide", 'toponymie', '1847-10', -118.40, 51.50, 'h',
  ['Paul Kane'],
  "En remontant la Columbia à l'automne 1847, Paul Kane campe au-dessous de la « Dalle des Morts ». Le rapide tient son nom d'un drame survenu vingt-cinq ou trente ans plus tôt : un Iroquois, un Métis et un Canadien français, chargés de faire passer un bateau, le descendirent à la cordelle le long de la rive ; la corde se rompit sur les rochers et le bateau fut emporté avec toutes les provisions. Au huitième jour de marche, le Métis, craignant d'être mangé, abandonna ses compagnons ; l'Iroquois tua le Canadien et se nourrit de sa chair, puis fut démasqué par les hommes d'un canot envoyé à leur recherche.",
  'chap. XXI', "Récit rapporté par Kane, non daté avec précision (« il y a vingt-cinq ou trente ans »). Point hypothétique au rapide de Death Rapids, en amont de Revelstoke (Colombie-Britannique).")
F('03', "Edmonton, décembre 1847 : François Lucie, voyageur métis, et les voleurs de chevaux assiniboines", 'personnage', '1847-12/1848-01', -113.4909, 53.5444, 'c',
  ['François Lucie', 'Paul Kane', 'George Simpson'],
  "Quelques jours après Noël 1847, Paul Kane sort au fort d'Edmonton avec François Lucie, voyageur métis dont Sir George Simpson avait raconté l'exploit : une bande d'Assiniboines ayant enlevé vingt-quatre chevaux à Edmonton, Lucie, l'un des gardiens, rattrapa les voleurs à une petite rivière, se jeta sur un grand Assiniboine et le tua au coutelas après un corps-à-corps dans le courant. Lucie raconta lui-même l'histoire à Kane presque dans les mêmes termes.",
  'chap. XXII', "Kane cite le récit du voyage autour du monde de Simpson (1841-1842) ; la date du vol de chevaux n'est pas donnée. Point au fort Edmonton.")

C7 = Corpus('Recherches', 'NPS90', NPS90); F = C7.F
F('01', "Westport : le magasin bâti par Cyprien Chouteau (1850), plus tard magasin de Jim Bridger", 'commerce', '1850/1866', -94.5947, 39.0533, 'a',
  ['Cyprien Chouteau', 'Jim Bridger', 'Albert Wachsmann'],
  "Sur la route de Westport, juste à l'ouest du magasin Ewing-Boone, Cyprien Chouteau bâtit en 1850 un magasin qu'il vend en 1866 à Jim Bridger ; le gendre de Bridger, Albert Wachsmann, y tient boutique. Le bâtiment subsiste, très modifié.",
  'p. 93', "Site n° 43 de l'inventaire des lieux de la piste de Santa Fe. Point approximatif à Westport (Kansas City).")

C8 = Corpus('Recherches', 'GZ63', GZ63); F = C8.F
F('01', "Tierra Amarilla, mai-juin 1863 : Henry Mercure, sous-agent des Utes, rapporte les raids navajos", 'evenement', '1863-05/1863-06', -106.5497, 36.7006, 'c',
  ['Henry Mercure'],
  "De passage à Santa Fe, Henry Mercure, sous-agent pour les Utes à Tierra Amarilla, renseigne la Gazette sur les déprédations navajos du nord-ouest du territoire : le 5 mai, une quarantaine de Navajos enlèvent sept bêtes près de la maison de Juan Montaña ; le 4 juin, trois d'entre eux attaquent la bergerie de Juan Martín, blessent trois hommes et emmènent un garçon de douze ou quatorze ans ; le 12 juin, une cinquantaine volent bétail et moutons aux Cañones, près d'Abiquiu, et emmènent trois garçons, dont l'un est tué.",
  '', "Point à Tierra Amarilla (Nouveau-Mexique).")

C9 = Corpus('Recherches', 'WT09', WT09); F = C9.F
F('01', "Boggsville (Purgatoire) : Céran St. Vrain cède 2 040 acres à sa filleule Romalda Boggs (1865)", 'etablissement', '1865/1877', -103.2108, 38.0442, 'c',
  ['Céran St. Vrain', 'Romalda Luna Boggs', 'Thomas Oliver Boggs'],
  "En 1865, Thomas Boggs rompt son association avec Maxwell pour s'établir dans les basses terres de la Purgatoire. Céran St. Vrain, parrain de sa femme Romalda, nièce de Cornelio Vigil, leur cède une part de 2 040 acres de la concession Vigil-St. Vrain ; on y bâtit deux maisons d'adobe et une acequia, et l'établissement prend le nom de Boggsville. En 1877, le bureau des terres juge que Romalda ne peut prouver son titre ; le président Grant le reconnaîtra cinq mois plus tard, mais les Boggs sont déjà repartis pour le Nouveau-Mexique.",
  '', "Point au site historique de Boggsville (comté de Bent, Colorado).")

C10 = Corpus('Recherches', 'JO03', JO03); F = C10.F
F('01', "Berlin (New Hampshire) : les Canadiens français et la paroisse Sainte-Anne (années 1860-1909)", 'religion', '1860/1909', -71.1851, 44.4687, 'c',
  [],
  "L'industrie forestière de Berlin naît vers 1852 aux chutes de l'Androscoggin (Winslow & Co., puis Berlin Mills Company en 1866 et Brown Company en 1917). Les Canadiens français, venus des terres agricoles du Québec, sont parmi les premiers à s'y établir au début des années 1860. Sainte-Anne, paroisse-mère de la ville, est en 1867 une mission de la paroisse Tous-les-Saints de Lancaster, puis en 1876 de la Sainte-Famille de Gorham ; l'église Sainte-Anne est achevée en 1909. La population passe de 1 144 habitants en 1880 à 8 886 en 1900 et 20 018 en 1930.",
  '30-32', "D'après The Brown Bulletin (1927) et La paroisse Sainte-Anne de Berlin (1962), cités par Joly. Point à Berlin.")
F('02', "Berlin (New Hampshire) : les institutions franco-américaines (1905-1973)", 'etablissement', '1905/1973', -71.1820, 44.4720, 'c',
  [],
  "En 1905, l'hôpital Saint-Louis ouvre ses portes, tenu par les Sœurs de la Charité et les Sœurs grises venues du Québec. La paroisse de l'Ange-Gardien, seule à l'est de l'Androscoggin, est fondée le 15 août 1917 ; l'Académie Saint-Régis, école bilingue de la 6e à la 8e année, ouvre en 1911, l'école de l'Ange-Gardien en 1918, l'école Saint-Joseph vers 1930 et l'école secondaire Notre-Dame en 1941 ; la paroisse Saint-Joseph naît de Sainte-Anne en 1942. La caisse populaire de l'Ange-Gardien date de 1929, le quotidien Le Journal des années 1940. L'hôpital Saint-Louis et l'école Notre-Dame ferment en 1972, l'Académie Saint-Régis en 1973.",
  '32-33, 36', "Point à Berlin, à l'est de l'Androscoggin.")

fiches = C1.fiches + C2.fiches + C3.fiches + C4.fiches + C5.fiches + C6.fiches + C7.fiches + C8.fiches + C9.fiches + C10.fiches
