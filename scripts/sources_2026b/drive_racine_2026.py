# Fichiers isolés à la racine du dossier Drive 1Tx_c-qfEHYTeJ1tNBsBm4TJxWiCiZWiV (dépouillement du 20 nov. 2026).
# Téléchargés en entier et lus localement (pdftotext / epub). Préfixes PM05, NMR2, KE08, MB10, FR08.
from commun import Corpus

PM = "Marchand, Philip (2008), L'Empire fantôme. De ces Français qui ont failli conquérir l'Amérique du Nord, trad. Anne-Hélène Kerbiriou, Québec, Presses de l'Université Laval (éd. orig. Ghost Empire, 2005)"
NM = "New Mexico Roots Ltd. (diligencias matrimoniales de l'archidiocèse de Santa Fe, 1678-1869), vol. 2 (noms Ba-Br), Drive de l'auteur, fichier Volume2.pdf"
KE = "Keith, LeeAnna (2008), The Colfax Massacre: The Untold Story of Black Power, White Terror, and the Death of Reconstruction, New York, Oxford University Press"
MB = "Barile, Mary Collins (2010), The Santa Fe Trail in Missouri, Columbia, University of Missouri Press (Missouri Heritage Readers)"
FR = "Fraïssé, Marie-Hélène (2008), Radisson. Indien blanc, agent double, Arles, Actes Sud"

C1 = Corpus('Recherches', 'PM05', PM, page_fmt='p. {}'); F = C1.F
F('01', "Fort Saint-Louis de La Salle (Garcitas Creek) : le canon de 1996 et la fouille du site", 'evenement', '1996/2002~', -96.73, 28.82, 'c',
  ['Robert Cavelier de La Salle', 'Henri Joutel'],
  "Sur un ranch privé dominant la rivière Garcitas, un chef d'équipe découvre en 1996 un canon enterré : c'est le site que les historiens appellent le fort Saint-Louis, plutôt un groupe de cabanes qu'un fort, établi par La Salle en 1685. Quand Philip Marchand le visite, journal de Joutel en main, la fouille entreprise par une équipe d'archéologues dure depuis près de trois ans, au lieu des six mois prévus, à cause d'une argile si dure qu'il faut la creuser à la pioche.",
  '2-3', "Même point que les fiches du fort Saint-Louis du Texas.")
F('02', "Indianola (baie de Matagorda) : la statue de La Salle de Bayside Beach (1928)", 'evenement', '1928-09', -96.49, 28.53, 'a',
  ['Robert Cavelier de La Salle', 'Nora Sweetland'],
  "Le jour de la fête du Travail 1928, on inaugure près d'Indianola, à l'emplacement présumé du débarquement de La Salle, une statue de béton de l'explorateur, œuvre de Nora Sweetland, dans un « parc du mémorial de La Salle » destiné à lancer le lotissement de Bayside Beach. La Crise met fin au projet ; dans les années 1930, un ouragan jette la statue à terre, et des vandales emportent les morceaux. Il ne reste aujourd'hui que le piédestal et les bottes.",
  '41-42', "Point approximatif à Indianola (Texas).")
F('03', "Navasota : la statue de La Salle (1930) et le buste offert par la France (1976)", 'evenement', '1930/1976', -96.09, 30.39, 'c',
  ['Robert Cavelier de La Salle'],
  "Près de l'endroit où La Salle fut tué en 1687, la ville de Navasota dresse en 1930 sur sa rue principale une statue de bronze de l'explorateur, tenant une carte du Nouveau Monde et tendant la main aux Autochtones ; l'inscription en fait un « bâtisseur d'empire ». En 1976, le Comité français pour le bicentenaire des États-Unis et l'Association France-Amérique y offrent en plus un buste de La Salle.",
  '60-61', "Point à Navasota (Texas).")
F('04', "Green Bay : les fresques de l'arrivée de Jean Nicolet (1910 et 1937)", 'evenement', '1910/1937', -88.015, 44.513, 'c',
  ['Jean Nicolet', 'Franz Rohrbeck', 'Anna Lou Matthews Bedore'],
  "Au palais de justice du comté de Brown, à Green Bay, une fresque de l'arrivée de Nicolet chez les Ho-Chunks, œuvre du peintre milwaukéen d'origine allemande Franz Rohrbeck, est inaugurée en 1910 : Nicolet y tire des coups de pistolet en l'air dans sa robe de damas chinoise. Une seconde fresque, terminée en 1937 au Neville Public Museum par l'artiste locale Anna Lou Matthews Bedore pour la Works Progress Administration, le montre assis en tailleur parmi les Winnebagos, un calumet à la main.",
  '236-237', "Point au centre de Green Bay (Wisconsin).")
F('05', "Monroe (rivière aux Raisins) : les « Mushrat French » et la fin du français au foyer (années 1930)", 'etablissement', '1930/1939', -83.40, 41.916, 'a',
  ['Dennis M. Au', 'Marcel Bénéteau'],
  "Selon Dennis M. Au, ancien directeur adjoint du musée historique du comté de Monroe, les années 1930 furent la dernière décennie où l'on parlait encore français dans les foyers du comté. Les descendants des Canadiens de la rivière aux Raisins, qui mangeaient le rat musqué le vendredi (« Dieu bénisse le rat musqué, c'est du poisson ! »), en avaient reçu le surnom de « Mushrats ». Au et l'ethnologue Marcel Bénéteau, de l'Université de Windsor, ont enregistré des centaines de leurs chansons et contes avant leur disparition.",
  '196-198', "Point à Monroe (Michigan).")
F('06', "Pittsfield (Massachusetts) : la première paroisse française (1867) et les coups de feu sur le confessionnal (1868)", 'religion', '1867/1868', -73.254, 42.45, 'c',
  ['Antoine Derbuel (abbé)'],
  "D'après un manuscrit inédit de Katherine F. Mullaney (Catholic Pittsfield, 1897), la première paroisse française de Pittsfield est fondée en 1867 pour une centaine de familles canadiennes-françaises. L'année suivante, quelqu'un tire plusieurs coups de feu par la fenêtre du confessionnal à l'heure où le curé, le père Derbuil, entend d'ordinaire les confessions ; absent ce jour-là, il en réchappe, et le tireur ne fut jamais arrêté.",
  '338-339', "Marchand écrit « Derbuil » ; l'atlas a déjà l'abbé Antoine Derbuel à Pittsfield en 1868 (Hamon 1891). Marchand date la paroisse de 1867, Hamon de 1868.")
F('07', "Richard (Louisiane) : Charlene Richard, la « petite sainte cajun » (1959)", 'religion', '1959', -92.37, 30.40, 'a',
  ['Charlene Richard', 'Joseph Brennan (père)'],
  "Charlene Richard, fillette cajun de la paroisse St. Edward de Richard, dans la prairie cajun, fête ses douze ans en janvier 1959 ; en juillet, on lui diagnostique une leucémie avancée et elle entre à l'hôpital Notre-Dame-de-Lourdes de Lafayette, où le jeune aumônier Joseph Brennan l'invite à offrir ses souffrances pour d'autres. Elle meurt la même année. Sa tombe, au cimetière de l'église St. Edward, devient un lieu de pèlerinage : on y laisse des billets dans une boîte de verre, au pied d'une statue de la Vierge.",
  '361-368', "Point au village de Richard (paroisse d'Acadie, Louisiane).")
F('08', "La Nouvelle-Orléans : la paroisse Saint-Augustin des créoles noirs francophones (1842)", 'religion', '1842', -90.069, 29.962, 'a',
  ['Jelly Roll Morton (Ferdinand Lamothe)', 'Marie-Jeanne Aliquot', 'Jérôme G. LeDoux (père)'],
  "Établie en 1842, la paroisse Saint-Augustin reste le cœur de la vie des catholiques créoles noirs francophones de La Nouvelle-Orléans. Marchand y rattache Jelly Roll Morton, né Ferdinand Lamothe, qui se vantait que « tous les gens comme lui étaient venus directement des rivages de France », et la mémoire de Marie-Jeanne Aliquot, Française arrivée en 1832 qui consacra sa vie à enseigner le catéchisme aux esclaves.",
  '395-396', "Point approximatif à l'église Saint-Augustin (Tremé).")

C2 = Corpus('Recherches', 'NMR2', NM, page_fmt='p. {}'); F = C2.F
F('01', "Taos : Enrique Blanco, « natif du Canada », épouse María Guadalupe López (16 février 1832)", 'famille', '1832-02-16', -105.573, 36.407, 'c',
  ['Enrique Blanco'],
  "Le 16 février 1832, à Taos, l'enquête prénuptiale d'Enrique Blanco, étranger et célibataire, se dit natif du « Canada aux États-Unis du Nord » et dans le pays depuis un an et six mois ; il épouse María Guadalupe López. Il obtient dispense comme vagabond et faute de pouvoir prouver son baptême.",
  '232', "Nom hispanisé : sans doute un Canadien du nom de Blanc ou Leblanc (hypothèse).")
F('02', "Socorro : Victor Bardaux, natif de France, épouse María Rafaela Gonzales de Lemitar (22 avril 1849)", 'famille', '1849-04-22', -106.891, 34.058, 'c',
  ['Victor Bardaux'],
  "Le 22 avril 1849, à Socorro, Victor Bardaux, 24 ans, cultivateur né en France et résidant aux États-Unis, fils de Pedro Bardaux et d'Angelica Gelin, épouse María Rafaela Gonzales, native de Lemitar, fille de Juan Albino Gonzales et de Balbina López.",
  '208')

C3 = Corpus('Recherches', 'KE08', KE, page_fmt='p. {}'); F = C3.F
F('01', "Colfax : la « Rigolette de Bon Dieu » et la vente de Jean-Baptiste Prudhomme (années 1830)", 'toponymie', '1832/1840~', -92.69, 31.52, 'a',
  ['Jean-Baptiste Prudhomme', 'Henry Shreve'],
  "En 1832, pendant les travaux de dégagement du Great Raft, la rivière Rouge déborde et s'empare d'un chenal circulaire que les habitants baptisent aussitôt la « Rigolette de Bon Dieu » ; la falaise ainsi créée deviendra le débarcadère de la plantation sur laquelle naîtra Colfax. La vente des 15 000 acres riverains passe par Jean-Baptiste Prudhomme, de Natchitoches, lui-même agent du propriétaire français détenteur d'un titre de la maison de Bourbon.",
  '5', "Point à Colfax (Louisiane).")
F('02', "Cane River : Narcisse Fredieu, témoin de la défense au procès de Colfax (1874)", 'personnage', '1874', -93.0, 31.6, 'h',
  ['Narcisse Fredieu'],
  "Au procès des accusés du massacre de Colfax, plusieurs témoins jurent que le cordonnier Clement Penn regardait le combat du 13 avril 1873 depuis la maison de Narcisse Fredieu, sur la Cane River. Fredieu est l'un des rares Blancs de la région à oser témoigner pour la défense ; il n'est pourtant pas ami du Ku Klux Klan, qui l'a persécuté parce qu'il refusait de renier sa femme et ses enfants métis.",
  '141', "Position hypothétique sur la Cane River (paroisse de Natchitoches) ; Keith ne situe pas la maison.")
F('03', "Ferme de Jesse McKinney (paroisse de Grant) : le créole Denis Lemoine parmi les tueurs (5 avril 1873)", 'evenement', '1873-04-05', -92.72, 31.55, 'h',
  ['Denis Lemoine', 'Prudhomme Lemoine'],
  "Le 5 avril 1873, des Blancs armés tuent le fermier noir Jesse McKinney devant sa famille, près du bac du bayou Darrow. Parmi les hommes identifiés par sa veuve figure Denis Lemoine, créole de la paroisse des Avoyelles, venu rejoindre ses cousins de la grande famille Lemoine de Natchitoches ; avec Bill Irwin, il sert ensuite d'éclaireur aux troupes blanches qui attaqueront le palais de justice de Colfax le 13 avril. Lemoine est jugé avec Prudhomme Lemoine et sept autres accusés ; les témoins l'impliquent particulièrement dans le meurtre de McKinney.",
  '88-89, 137-139', "Position hypothétique près de Colfax.")

C4 = Corpus('Recherches', 'MB10', MB, page_fmt='p. {}'); F = C4.F
F('01', "Arrow Rock : la « Pierre à Flèche » des explorateurs français", 'toponymie', '1700~/1803', -92.946, 39.069, 'a',
  [],
  "Les explorateurs français appelaient « Pierre à Flèche » les hautes falaises du Missouri où les Autochtones venaient depuis des générations tailler le silex en pointes de flèche ; le village qui s'y forma prit le nom d'Arrow Rock. Le gué et le bac de William Becknell y deviennent une étape de la piste de Santa Fe.",
  '114', "Datation large : régime français et espagnol, avant 1803.")

C5 = Corpus('Recherches', 'FR08', FR, page_fmt='{}'); F = C5.F
F('01', "Trois-Rivières : le jeune Radisson capturé par les Agniers (24 mai 1652)", 'evenement', '1652-05-24', -72.55, 46.343, 'c',
  ['Pierre-Esprit Radisson'],
  "À l'aube du 24 mai 1652, Pierre-Esprit Radisson et deux garçons de son âge quittent en cachette le bourg palissadé de Trois-Rivières pour chasser les oiseaux au bord du fleuve, en pleine « terreur iroquoise ». Radisson est pris par des Agniers (Mohawks) et adopté par une famille de ses ravisseurs ; il racontera l'épisode des années plus tard dans un récit en anglais conservé parmi les papiers de Samuel Pepys, à la Bodleian Library d'Oxford.",
  's. p. (epub)', "Point à Trois-Rivières.")
F('02', "Sainte-Marie de Gannentaha (lac Onondaga) : le festin et la fuite des Français (19-20 mars 1658)", 'evenement', '1658-03-19/1658-03-20', -76.21, 43.10, 'a',
  ['Pierre-Esprit Radisson', 'Paul Ragueneau'],
  "Recruté comme interprète par le père Paul Ragueneau, Radisson est au fort Sainte-Marie, chez les Onondagas, quand les Français, menacés, préparent leur fuite : le 19 mars 1658, ils offrent à leurs hôtes un « festin à tout manger » et, la nuit venue, s'esquivent en barques sur les rivières encore prises par les glaces. Ils sont cinquante-trois, précise Ragueneau. Radisson avoue avoir été du parti qui voulait massacrer les Onondagas endormis ; les jésuites s'y opposèrent.",
  's. p. (epub)', "Point approximatif au site de Sainte-Marie de Gannentaha (Liverpool, New York).")
F('03', "Port Nelson rebaptisé « rivière Bourbon » (1682-1684)", 'toponymie', '1682/1684', -92.4, 57.0, 'a',
  ['Pierre-Esprit Radisson', 'Médard Chouart des Groseilliers'],
  "Après leur campagne de 1682-1683 à l'embouchure des rivières Nelson et Hayes, où ils ont eu raison de deux équipages anglais sans verser de sang, Radisson et Des Groseilliers plaident leur cause à Paris. En janvier 1684, Des Groseilliers écrit au ministre Seignelay : « J'espère que l'on ne me blâmera point d'avoir changé le nom de Port Nelson pour le nommer la rivière Bourbon. » Seignelay les reçoit sans les blâmer.",
  's. p. (epub)', "Même point que les fiches de la rivière Hayes (poste de Radisson).")

fiches = C1.fiches + C2.fiches + C3.fiches + C4.fiches + C5.fiches
