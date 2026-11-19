# John Francis McDermott, « The French Impress on Place Names in the Mississippi Valley », Journal of the Illinois State
# Historical Society, vol. 72, n° 3 (août 1979), p. 225-234, PDF JSTOR du Drive de l'auteur. Corpus « Recherches », préfixe MD79.
from commun import Corpus
MD = "McDermott, John Francis (1979), « The French Impress on Place Names in the Mississippi Valley », Journal of the Illinois State Historical Society, vol. 72, n° 3, p. 225-234"
C = Corpus('Recherches', 'MD79', MD, page_fmt='p. {}')
F = C.F
T = 'toponymie'
F('01', "Saint-Charles : les « Mamelles », belvédère sur le confluent du Missouri et du Mississippi", T, '1816~/1822~', -90.5500, 38.8600, 'a', ['Timothy Flint'],
  "Près de Saint-Charles, trois buttes arrondies portaient le nom de Mamelles. On y menait les visiteurs de Saint-Louis pour contempler la jonction des deux grandes rivières. En 1816, Timothy Flint notait, non sans pruderie, que les Français donnaient aux choses des noms tirés de leur ressemblance ; Beltrami parle des « Nipples ».",
  '226-227', "Position approximative des Mamelles, au nord-ouest de Saint-Charles.")
F('02', "Saint-Charles : le Marais Croche, un bras mort et non un marais", T, '1780~/1850', -90.4300, 38.8300, 'h', [],
  "McDermott relève que dans la vallée du Mississippi, « marais » ne désignait pas un marécage, mais un lac en croissant formé par un ancien méandre. Il en donne pour exemples le Grand Marais (parc d'État de l'Illinois, face à Saint-Louis) et le Marais Croche, près de Saint-Charles.",
  '227', "Point placé dans la plaine du Missouri près de Saint-Charles ; emplacement exact à vérifier.")
F('03', "Rivière Kaskaskia, dite « Okaw » : d'« Au Kas » à Okawville", T, '1703/1979', -89.6650, 38.4350, 'c', [],
  "Les Français abrégeaient volontiers : « Au Pe » pour le poste des Peorias, « Au Caho » pour Cahokia, « Au Kas » pour Kaskaskia. Les Américains ont fait de ce dernier « Okaw » : la rivière Kaskaskia fut longtemps appelée l'Okaw, et une ville de l'Illinois porte encore le nom d'Okawville. De même, « Au poste » de Vincennes devint parfois « Oposte ».",
  '230-231', "Point placé à Okawville.")
F('04', "Monts Ozarks : des Osages « aux Arcs »", T, '1750~/1979', -92.5, 36.5, 'h', [],
  "Un traiteur ou un officier écrivant du pays des Arkansas datait sa lettre « Aux Arcansas », ou simplement « Aux Arcs ». Pour les Américains, les monts du pays des Arkansas devinrent ainsi les Ozark Mountains. McDermott écarte l'hypothèse fantaisiste d'arcs taillés dans le bois d'oranger des Osages.",
  '231', "Point placé au centre du plateau des Ozarks.")
F('05', "Le Mississippi des voyageurs : la « Longue Vue des Canadiens », l'île aux Assiminiers et l'île au Plomb (vers 1822)", T, '1700~/1822', -90.2, 36.0, 'h', ['Paul-Guillaume de Wurtemberg'],
  "En 1822, le prince Paul-Guillaume de Wurtemberg s'agaçait, en remontant le Mississippi, des noms créoles donnés aux îles et aux rivières. Il citait l'île aux Assiminiers (aux asiminiers), l'île au Plomb sans plomb, et un tronçon du fleuve appelé la Longue Vue des Canadiens, souvenir de quelque aventure de voyageurs canadiens peut-être antérieure à La Nouvelle-Orléans.",
  '231-232', "Emplacements non précisés : point placé sur le Mississippi moyen.")
F('06', "Cash Creek (Illinois) : la « Cache » d'un traiteur, devenue de l'argent comptant", T, '1750~/1979', -89.1600, 37.0600, 'a', [],
  "Le ruisseau Cash, qui se jette dans l'Ohio juste au-dessus de son confluent avec le Mississippi, ne célèbre pas l'argent comptant. Son nom vient de la « cache » où un traiteur avait dû entreposer à la manière indienne des marchandises ou des pelleteries qu'il ne pouvait emporter.",
  '233')
F('07', "Rivière Wood (Illinois) : le camp d'hiver de Lewis et Clark était sur la rivière à Dubois", T, '1803-12/1804-05', -90.1030, 38.8600, 'c', ['Meriwether Lewis', 'William Clark'],
  "Pour McDermott, l'expédition de Lewis et Clark n'a pas hiverné sur une « Wood River » : les cartes du temps nomment ce petit cours d'eau, en face de l'embouchure du Missouri, la rivière à Dubois. Le « Beef Island and River » noté par Clark le 26 mai 1804 est l'île et la rivière aux Bœufs, c'est-à-dire aux bisons.",
  '233-234')
F('08', "Embouchure de la Raft River (Idaho) : le « cajeu » des voyageurs sur la piste de l'Oregon", T, '1830~/1860', -113.2, 42.6, 'h', [],
  "La Raft River, que franchissaient des milliers d'émigrants au-delà du col South Pass, portait d'abord le nom de Cajeu, mot du français de la vallée du Mississippi désignant un radeau. McDermott range dans la même série Barn Bluff (La Grange), sur le haut Mississippi, et le Grand et le Petit Gouffre, tourbillons du fleuve au-dessus de Natchez devenus Grand Gulf et Little Gulf.",
  '233', "Point placé sur la Raft River, près de son confluent avec la Snake.")
F('09', "Missouri : l'île Beausoleil et le « Cadet » Chouteau, des noms de traiteurs cachés sous l'anglais", T, '1790~/1979', -91.0, 38.6, 'h', ['Eugène Pourée dit Beausoleil', 'Pierre Chouteau', 'Pierre Berger'],
  "L'île du Missouri notée « Fair Sun Island » par Lewis et Clark, puis « Sun Island », doit son nom à Eugène Pourée dit Beausoleil, traiteur de Saint-Louis qui y avait hiverné. La ville de Cadet, au Missouri, rappelle l'un des Pierre Chouteau, père ou fils, appelés tour à tour Cadet en famille. Le « Shepherd's Creek » de Saint-Louis était la rivière à Berger, du nom de Pierre Berger, et non d'un berger.",
  '234', "Emplacement de l'île non précisé : point placé sur le bas Missouri.")
fiches = C.fiches
