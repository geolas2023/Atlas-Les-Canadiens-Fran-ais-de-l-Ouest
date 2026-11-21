# Lot « gros » (21 nov. 2026) : cinq gros PDF du Drive de l'auteur.
# Fiches tirées de Chaloult (Les « Canadiens » de l'expédition Lewis et Clark), partie lue :
# introduction à la p. 80 (début du chap. V), et de Woodger et Toropov (Encyclopedia of the
# Lewis and Clark Expedition), partie lue : p. i-xxv et 1-54 (chronologie, entrées A à « Blackfeet »).
# Pages : pagination imprimée. Préfixe GRX.
from commun import Corpus

CHA = "Chaloult, Michel, Les « Canadiens » de l'expédition Lewis et Clark : 1804-1806. La traversée du continent, Sillery, Septentrion, 2003 (PDF, Drive de l'auteur, dossier LEWIS_AND_CLARK)"
WOO = "Woodger, Elin, et Brandon Toropov, Encyclopedia of the Lewis and Clark Expedition, New York, Facts On File, 2004 (PDF, Drive de l'auteur, dossier LEWIS_AND_CLARK)"

C = Corpus('Recherches', 'GRX', CHA); F = C.F

F('01', "Villages arikaras : Tabeau et les « capitaines sans compagnies » (1803-1804)", 'personnage', '1803/1804-10', -100.5, 45.55, 'a',
  ['Pierre-Antoine Tabeau', 'Joseph Gravelines', 'Meriwether Lewis', 'William Clark', 'Régis Loisel'],
  "Pierre-Antoine Tabeau, adjoint de Régis Loisel, et Joseph Gravelines vivent chez les Arikaras quand l'expédition y séjourne cinq jours en octobre 1804 ; ils parlent la langue et servent d'interprètes. À son arrivée aux villages l'année précédente, Tabeau avait convoqué 42 de leurs chefs à un grand conseil, mais on lui avait reproché d'en avoir oublié des dizaines d'autres. Il décrit depuis la population comme des « capitaines sans compagnies ». Il tente de le faire comprendre aux capitaines et leur conseille de traiter en égaux les trois chefs de village, Crow at Rest, Hawk's Feather et Hay. Lewis et Clark font pourtant de Crow at Rest le « grand chef », ce qui offense d'abord les deux autres. Selon Chaloult, Tabeau et Gravelines déjeunent avec les capitaines le 10 octobre pour préparer le conseil, et les Statistical Views rédigées par Lewis l'hiver suivant reprennent une classification des Sioux identique à celle du récit de Tabeau.",
  'p. 32 ; Chaloult, p. 61, 64',
  "Woodger ne donne pas d'année : « the previous year » renvoie à 1803. Chaloult nomme les chefs Corbeau Éclatant, Le Foin et Plume d'Aigle, et cite LeBris sur la copie possible du manuscrit de Tabeau. L'atlas a Tabeau et Gravelines chez les Arikaras en 1804 (PA-tabeau-pierre-antoine-villages-a, DI-gravelines-joseph-villages-a), sans l'épisode des 42 chefs ni le conseil sur le grand chef. Point aux villages arikaras de la Grand River, comme les fiches existantes.",
  source=WOO)

F('02', "La Charette : Lewis et Clark rencontrent Régis Loisel (25 mai 1804)", 'exploration', '1804-05-25', -91.06, 38.62, 'a',
  ['Régis Loisel', 'Meriwether Lewis', 'William Clark', 'Pierre Dorion', 'Joseph Gravelines', 'Jean Vallée'],
  "Le 25 mai 1804, l'expédition campe à l'embouchure de la rivière Charette, où se sont établies quelques familles de chasseurs et de commerçants canadiens ; Clark note un petit village français de cinq familles seulement. Régis Loisel, né à L'Assomption, vient d'arriver à La Charette, dernier établissement blanc sur le Missouri ; il descend de l'île aux Cèdres, au pays des Sioux. Associé de marchands de Saint-Louis dans une compagnie du haut Missouri qui cherche entre autres un passage vers le Pacifique, il renseigne les capitaines sur les Indiens du haut Missouri, sur le fleuve et ses affluents. Plusieurs hommes de son équipe rendront ensuite de grands services au Corps de la Découverte, dont Pierre Dorion, Joseph Gravelines et Jean Vallée.",
  '36',
  "L'atlas a La Charette (BK16-03, HK-chartrand-joseph-la-charett) et Loisel au fort aux Cèdres (HS22-08), mais pas cette rencontre. Chaloult cite Clark : « a Small french Village called La Charatt of five families only » (Moulton, vol. 2, p. 251). Point de BK16-03.")

F('03', "Bas Missouri, en amont de la Gasconade : un radeau de peaux apporte la colère des Osages (31 mai 1804)", 'evenement', '1804-05-31', -91.85, 38.62, 'h',
  ['Auguste Chouteau', 'Pierre Chouteau', 'Meriwether Lewis', 'William Clark'],
  "Le 31 mai 1804, quelques jours après la Gasconade, les hommes de l'expédition rencontrent sur le Missouri un radeau fait de peaux, monté par un Canadien, un Indien et une Indienne. Ceux-ci rapportent que le messager envoyé par « monsieur Chouteau » de Saint-Louis chez les Osages pour leur annoncer la cession de la Louisiane aux États-Unis a été mal reçu. Ces Osages, qui habitent la vallée de l'Arkansas, n'acceptent pas que les Américains soient devenus maîtres du pays.",
  '37',
  "Chaloult ne précise ni le prénom du Chouteau ni le lieu exact de la rencontre. Point hypothétique sur le Missouri entre la Gasconade et l'embouchure de l'Osage.")

F('04', "Council Bluff : Fairfong, interprète français des Otos, au premier conseil (3 août 1804)", 'personnage', '1804-08-03', -96.03, 41.46, 'a',
  ['Fairfong', 'Meriwether Lewis', 'William Clark', 'Pierre Cruzatte'],
  "Le 3 août 1804, à la première conférence officielle de l'expédition avec les Indiens, un marchand et interprète français nommé Fairfong arrive au camp avec six chefs otos et missouris ; selon le journal, il vit chez eux et y a une famille. Après les parades, les discours et la distribution de médailles, Clark l'interroge sur les routes de commerce des Indiens. Fairfong lui apprend que Santa Fe n'est qu'à 25 jours de marche, et que l'embouchure de la Platte est centrale pour la traite : à un jour des Otos, un jour et demi des Grands Pawnees, deux jours des Omahas et deux jours et demi des Pawnees-Loups. Clark recommande d'élever un fort et un comptoir à Council Bluffs. Tout près se trouvait le poste où Pierre Cruzatte avait vécu et commercé deux ans avec les Omahas.",
  '47-48',
  "Chaloult signale, d'après Moulton (vol. 2, p. 437), l'hypothèse d'un marchand nommé Courtin, qu'il juge peu vraisemblable. Fairfong est absent de l'atlas ; le poste de Cruzatte y est (NM-cruzatte-x-fort-atkin). Le site du conseil a disparu ; point près de Fort Calhoun (Nebraska).")

F('05', "Calumet Bluff : Pierre Dorion père et fils au conseil des Yanktons (29-30 août 1804)", 'evenement', '1804-08-29/1804-08-30', -97.48, 42.86, 'a',
  ['Pierre Dorion père', 'Pierre Dorion fils', 'Jean-Baptiste Deschamps', 'Nathaniel Pryor', 'Meriwether Lewis', 'William Clark'],
  "Quelques milles au-dessus de la rivière à Jacques, la pirogue rouge du patron Deschamps et de ses engagés canadiens heurte un obstacle et doit être réparée ; l'expédition campe à Calumet Bluff. Le 29 août, le sergent Pryor revient avec cinq chefs yanktons et des dizaines de guerriers, accompagnés de Pierre Dorion fils, qui commerce avec eux ; Pierre Dorion père traduit le discours de Lewis. Le lendemain, les chefs Weucha et White Crane répondent que leur peuple est pauvre et veut un vrai commerce ; ils promettent la paix avec les Omahas, les Pawnees, les Otos et les Missouris et acceptent d'aller voir le président à Washington. Les capitaines laissent alors sur place Dorion père, le seul interprète qui parle couramment le sioux, malgré la mise en garde du chef Half Man : les Tetons, plus haut, n'écouteront pas forcément. Plus tôt dans le mois, près de l'île aux pélicans, Dorion avait renseigné les capitaines sur la Petite et la Grande Rivière des Sioux et sur la rivière à Jacques.",
  '50, 53-55',
  "L'atlas n'a Dorion père chez les Yanktons que par une fiche générale (PC-dorion-pierre-yankton-da) et ne nomme ni Calumet Bluff ni ce conseil. Chaloult juge l'abandon de Dorion « leur première erreur de taille ». Point à Calumet Bluff, près du barrage de Gavins Point (rive du Nebraska).")

F('06', "Embouchure de la Teton (Bad River) : Cruzatte, interprète faute de Dorion, devant les Tetons (25 septembre 1804)", 'evenement', '1804-09-25', -100.37, 44.36, 'a',
  ['Pierre Cruzatte', 'Pierre Dorion', 'Meriwether Lewis', 'William Clark'],
  "Le 25 septembre 1804, à l'embouchure de la rivière Teton, les capitaines tiennent conseil sous une voile tendue avec les deux principaux chefs tetons, le Bison Noir et le Partisan. Les Tetons jugent les cadeaux ridicules ; après une bouteille de whisky à bord, des guerriers saisissent le câble de la pirogue, Clark tire son sabre et les arcs se tendent, jusqu'à ce que le Bison Noir ordonne aux guerriers de lâcher le câble. Au départ, quelques carottes de tabac achètent le passage. Les capitaines regrettent l'absence de Pierre Dorion, seul interprète parlant couramment le sioux : Pierre Cruzatte, interprète ce jour-là, parle mieux la langue de sa mère omaha que celle des Tetons. Selon Chaloult, Tabeau traitait le Partisan de caméléon.",
  '59-60',
  "Aucune fiche de l'atlas sur la confrontation de la Teton (seul HS22-08 nomme le Partisan, en 1803). L'origine omaha de la mère de Cruzatte est donnée par Chaloult. Point à l'embouchure de la Bad River, en face de Pierre (Dakota du Sud).")

F('07', "Embouchure de la rivière au Boulet (Cannonball) : deux hommes de Gravelines dépouillés par les Mandans (18 octobre 1804)", 'commerce', '1804-10-18', -100.60, 46.43, 'a',
  ['Joseph Gravelines', 'Grenier'],
  "Le 18 octobre 1804, l'expédition passe l'embouchure d'une rivière aux galets ronds comme des boulets de canon, que les Canadiens ont nommée Le Boulet. Elle y trouve deux Canadiens au service de Joseph Gravelines, qui ont perdu leurs fourrures et leurs bagages aux mains des Mandans, pourtant amis des Blancs. Leurs noms ne sont pas connus ; Moulton avance pour l'un d'eux celui de Grenier, employé de Gravelines.",
  '65-66',
  "Chaloult cite Clark : « La Bullet or Cannon Ball River ». Le nom de Grenier n'est qu'une hypothèse de Moulton (vol. 3, p. 183). Point à l'embouchure de la Cannonball (Dakota du Nord).")

F('08', "Pays des Têtes-Plates : François Rivet, ancien engagé de Lewis et Clark (1809-1813)", 'personnage', '1809/1813', -114.1, 46.9, 'h',
  ['François Rivet'],
  "Né à Montréal, François Rivet devient jeune commerçant et chasseur en Louisiane ; il est l'un des engagés canadiens de la pirogue rouge en 1804. En 1809, il va vivre et se marier au pays des Têtes-Plates, au Montana. En 1813, il travaille chez eux pour la Compagnie du Nord-Ouest comme trappeur et interprète. En 1832, il commande le poste de Fort Colville pour la Compagnie de la Baie d'Hudson, et en 1838 il se retire dans la vallée de la Willamette, en Oregon.",
  '37',
  "Encadré de Chaloult d'après Moulton (vol. 2, app. A). Chaloult place Fort Colville « en Colombie britannique » : erreur, le poste était sur le Columbia, dans l'actuel État de Washington. L'atlas a Rivet aux Arrow Lakes (1815), à Spokane House et à Kettle Falls (1825-1826, CA-rivet-…) et en Oregon (MM-H7-237-1506), mais pas son établissement chez les Têtes-Plates. Point hypothétique dans le pays salish (vallée de la Bitterroot et environs de Missoula).")

fiches = C.fiches

autoch = [
  dict(id='A-GRX-01', src='GRX-01', nom="Villages arikaras : les Arikaras et le « grand chef » imposé par Lewis et Clark (1803-1804)", theme='rencontre', date='1803/1804-10', lon=-100.5, lat=45.55, cert='a',
       nations=['Arikaras'], aires=['Haut-Missouri'], francophones=['Pierre-Antoine Tabeau', 'Joseph Gravelines'],
       description="Chez les Arikaras, l'autorité est partagée entre de nombreux chefs : en 1803, quand le traitant Tabeau n'en convoque que 42 à un conseil, on lui reproche d'en avoir oublié des dizaines. En octobre 1804, les trois chefs de village, Crow at Rest, Hawk's Feather et Hay, reçoivent l'expédition, avec Tabeau et Gravelines comme interprètes. Les capitaines désignent Crow at Rest comme « grand chef », ce qui offense d'abord les deux autres, qui sont ensuite apaisés. Les Arikaras acceptent d'envoyer un représentant à Washington et de faire la paix avec les Mandans.",
       note="Woodger, p. 32. Voir GRX-01."),
  dict(id='A-GRX-03', src='GRX-03', nom="Vallée de l'Arkansas : les Osages refusent la cession de la Louisiane (mai 1804)", theme='evenement', date='1804-05', lon=-91.85, lat=38.62, cert='h',
       nations=['Osages'], aires=['Plaines'], francophones=['Chouteau'],
       description="Au printemps 1804, le messager envoyé par Chouteau, de Saint-Louis, pour annoncer aux Osages de la vallée de l'Arkansas que la Louisiane est cédée aux États-Unis est mal reçu : ils n'acceptent pas que les Américains soient devenus maîtres du pays. La nouvelle descend le Missouri sur un radeau de peaux jusqu'à l'expédition, le 31 mai.",
       note="Chaloult, p. 37. Point de la fiche GRX-03 (lieu où l'expédition reçoit la nouvelle), non du pays osage."),
  dict(id='A-GRX-04', src='GRX-04', nom="Council Bluff : Otos et Missouris au premier conseil de Lewis et Clark (3 août 1804)", theme='rencontre', date='1804-08-03', lon=-96.03, lat=41.46, cert='a',
       nations=['Otoes-Missourias'], aires=['Plaines'], francophones=['Fairfong'],
       description="Le 3 août 1804, six chefs otos et missouris viennent au camp de l'expédition avec Fairfong, marchand français qui vit chez eux avec sa famille. Ils reçoivent médailles, bracelets, vêtements, peinture, poudre et whisky, et se déclarent satisfaits. Par Fairfong, Clark apprend que l'embouchure de la Platte est à un jour de marche des Otos.",
       note="Chaloult, p. 47-48. Voir GRX-04."),
  dict(id='A-GRX-05', src='GRX-05', nom="Calumet Bluff : les Yanktons demandent un vrai commerce (29-30 août 1804)", theme='rencontre', date='1804-08-29/1804-08-30', lon=-97.48, lat=42.86, cert='a',
       nations=['Sioux (Dakotas, Lakotas, Nakotas)'], aires=['Plaines'], francophones=['Pierre Dorion père', 'Pierre Dorion fils'],
       description="Les 29 et 30 août 1804, cinq chefs yanktons rencontrent l'expédition à Calumet Bluff, avec Pierre Dorion fils, qui commerce chez eux, et Pierre Dorion père comme interprète. Weucha et White Crane répondent que leur peuple est très pauvre et veut autre chose que des médailles et des drapeaux : un véritable commerce. Ils promettent la paix avec les Omahas, les Pawnees, les Otos et les Missouris et acceptent d'aller à Washington. Le chef Half Man prévient que les Tetons, plus haut, n'écouteront pas forcément.",
       note="Chaloult, p. 54-55. Voir GRX-05."),
  dict(id='A-GRX-06', src='GRX-06', nom="Embouchure de la Teton : les Tetons du Bison Noir et du Partisan arrêtent l'expédition (25 septembre 1804)", theme='rencontre', date='1804-09-25', lon=-100.37, lat=44.36, cert='a',
       nations=['Sioux (Dakotas, Lakotas, Nakotas)'], aires=['Plaines'], francophones=['Pierre Cruzatte'],
       description="Courtiers des marchandises venues du Canada vers les nations sédentaires du haut Missouri, les Tetons entendent contrôler la navigation. Le 25 septembre 1804, ils jugent ridicules les cadeaux de l'expédition et réclament une pirogue pleine de marchandises ; des guerriers saisissent le câble d'une embarcation. Le Bison Noir apaise la crise, et le passage s'achète avec du tabac. L'interprète, Pierre Cruzatte, maîtrise mal leur langue.",
       note="Chaloult, p. 58-60. Voir GRX-06."),
  dict(id='A-GRX-07', src='GRX-07', nom="Rivière au Boulet : des Mandans dépouillent deux traitants de Gravelines (octobre 1804)", theme='commerce', date='1804-10', lon=-100.60, lat=46.43, cert='a',
       nations=['Mandans'], aires=['Haut-Missouri'], francophones=['Joseph Gravelines', 'Grenier'],
       description="À l'automne 1804, des Mandans prennent leurs fourrures et leurs bagages à deux Canadiens employés par Joseph Gravelines, que l'expédition trouve le 18 octobre à l'embouchure de la rivière au Boulet (Cannonball).",
       note="Chaloult, p. 66. Lieu de la rencontre, non du pillage. Voir GRX-07."),
  dict(id='A-GRX-08', src='GRX-08', nom="Pays des Têtes-Plates : François Rivet épouse une femme du pays (1809)", theme='famille', date='1809/1813', lon=-114.1, lat=46.9, cert='h',
       nations=['Salish (Têtes-Plates)'], aires=['Plateau'], francophones=['François Rivet'],
       description="En 1809, le Montréalais François Rivet, ancien engagé de Lewis et Clark, vient vivre et se marier chez les Têtes-Plates ; en 1813, il y est trappeur et interprète de la Compagnie du Nord-Ouest.",
       note="Chaloult, p. 37 (d'après Moulton). L'épouse n'est pas nommée. Voir GRX-08."),
]
