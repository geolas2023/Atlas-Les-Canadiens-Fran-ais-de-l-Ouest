# Corpus « Nouvelle-France » : explorations et postes de l'Empire français (XVIe-XVIIIe s.), trois ouvrages :
#   Margry, Pierre (éd.), Découvertes et établissements des Français dans l'ouest et dans le sud de l'Amérique septentrionale,
#     t. I : Voyages des Français sur les Grands Lacs et découverte de l'Ohio et du Mississippi (1614-1684), Paris, Jouaust, 1876.
#     Pages : début du chapitre (table des matières) ; l'OCR du microfilm étant fautif, les dates sont celles des documents.
#   Johnson, William Henry (1905), French Pathfinders in North America, Boston, Little, Brown.
#   Marchand, Philip (2005), Ghost Empire: How the French Almost Conquered North America, Toronto, McClelland & Stewart.
#     (L'auteur suit l'itinéraire de La Salle et visite les lieux aujourd'hui ; pages imprimées.)
from commun import Corpus
MA = "Margry, Pierre (éd.) (1876), Découvertes et établissements des Français dans l'ouest et dans le sud de l'Amérique septentrionale, t. I (1614-1684), Paris, D. Jouaust"
JO = "Johnson, William Henry (1905), French Pathfinders in North America, Boston, Little, Brown and Co."
GE = "Marchand, Philip (2005), Ghost Empire: How the French Almost Conquered North America, Toronto, McClelland & Stewart"
C = Corpus('Nouvelle-France', 'NF', MA)
F = C.F
NOTE_M = "Document d'archives édité par Margry ; date et lieu d'après le document, localisation de l'atlas."

# ---- Margry, t. I
F('m01', 'Baie des Puans : premier voyage des Français', 'exploration', '1634~', -88.02, 44.52, 'a', ['Jean Nicolet'],
  "Premiers voyages des Français au sault Sainte-Marie, au lac Michigan et à la baie des Puans (Green Bay), à la recherche d'une mer menant à l'Asie ; on y rattache Jean Nicolet.", 'chap. III, p. 35 et suiv.', NOTE_M)
F('m02', 'Sault-Sainte-Marie : Raymbault et Jogues', 'religion', '1641', -84.35, 46.5, 'c', ['Charles Raymbault', 'Isaac Jogues'],
  "Les jésuites Raymbault et Jogues poussent jusqu'au sault Sainte-Marie, porte du lac Supérieur (rappelé aussi par Belisle, 1907).", 'chap. III', NOTE_M)
F('m03', 'Chagouamigon : mission du père Allouez', 'religion', '1665/1669', -90.82, 46.67, 'a', ['Claude Allouez'],
  "Notice sur Claude Allouez, missionnaire des nations outaouaises : mission du Saint-Esprit à Chagouamigon, sur le lac Supérieur, puis mission Saint-François-Xavier de la baie des Puans.", 'chap. IV', NOTE_M)
F('m04', 'Lac Supérieur : cuivre de la Nantaouagan', 'commerce', '1670-11-10', -89.3, 46.9, 'a', ['Jean Talon'],
  "Dans son mémoire au roi du 10 novembre 1670, l'intendant Talon envoie du cuivre très pur tiré du lac Supérieur et de la rivière Nantaouagan (Ontonagon) ; plus de vingt Français auraient vu dans le lac un bloc d'environ huit cents livres.", 'chap. V, p. 95', NOTE_M)
F('m05', 'Départ de Dollier, Galinée et La Salle vers l\'Ohio', 'exploration', '1669-07', -73.57, 45.5, 'c', ['François Dollier de Casson', 'René de Bréhant de Galinée', 'René-Robert Cavelier de La Salle'],
  "À la fin de juin 1669, La Salle (5 canots, 14 hommes) et les sulpiciens Dollier et Barthélemy (3 canots, 7 hommes) préparent à Montréal le voyage vers la rivière que les Iroquois appellent Ohio, qu'on espère mener à la mer Vermeille.", 'chap. VI, p. 114-115', NOTE_M)
F('m06', 'Lac Érié : prise de possession par Dollier et Galinée', 'exploration', '1670-03-23', -80.2, 42.78, 'a', ['François Dollier de Casson', 'René de Bréhant de Galinée'],
  "Après avoir hiverné sur la rive nord du lac Érié, les sulpiciens Dollier de Casson et Galinée prennent possession des terres voisines au nom du roi (mars 1670), avant de gagner le sault Sainte-Marie.", 'chap. VI', NOTE_M)
F('m07', 'Sault-Sainte-Marie : prise de possession de Saint-Lusson', 'evenement', '1671-06-14', -84.35, 46.5, 'c', ['Simon-François Daumont de Saint-Lusson', 'Jean Talon'],
  "Envoyé par Talon, Saint-Lusson plante la croix et les armes du roi au sault en présence de dix-sept nations, qui se soumettent selon le récit des jésuites présents ; Talon joint l'acte de prise de possession à son rapport.", 'chap. V, p. 93', NOTE_M)
F('m08', 'Lac Ontario : voyage du gouverneur Courcelles', 'exploration', '1671', -76.5, 44.2, 'a', ['Daniel de Rémy de Courcelles'],
  "Voyage du gouverneur Daniel de Rémy de Courcelles jusqu'au lac Ontario pour impressionner les Iroquois.", 'chap. VII, p. 167', NOTE_M)
F('m09', 'Cataracoui : fort Frontenac', 'poste', '1673/1677', -76.48, 44.23, 'c', ['Louis de Buade de Frontenac', 'René-Robert Cavelier de La Salle'],
  "Voyage de Frontenac au lac Ontario (1673) et fondation du fort ; La Salle en obtient le gouvernement et la seigneurie (1675) et y investit lourdement, ce qui lui vaut l'hostilité des marchands.", 'chap. VIII ; XII-XIV, p. 271-299', NOTE_M)
F('m10', 'Jolliet et Marquette jusqu\'au 33e degré', 'exploration', '1673-07', -91.2, 33.8, 'a', ['Louis Jolliet', 'Jacques Marquette'],
  "Le père Marquette et Louis Jolliet descendent le Mississippi jusqu'au 33e degré de latitude et concluent qu'il se jette dans le golfe du Mexique ; Marquette veut ouvrir une mission chez les Illinois.", 'chap. XI, p. 253-270', NOTE_M)
F('m11', 'Niagara : poste et construction de la barque', 'poste', '1678-12/1679-08', -79.06, 43.26, 'a', ['René-Robert Cavelier de La Salle', 'Henri de Tonty'],
  "Autorisé à découvrir l'ouest (lettres de 1678), La Salle fait établir un poste à Niagara et construire une barque au-dessus des chutes.", 'chap. XV ; XIX, p. 327 ; 433', NOTE_M)
F('m12', 'Fort des Miamis (rivière Saint-Joseph)', 'poste', '1679-11', -86.48, 42.1, 'a', ['René-Robert Cavelier de La Salle', 'Henri de Tonty'],
  "Relation officielle de l'entreprise de La Salle (1678-1681) : fort élevé à l'embouchure de la rivière des Miamis (Saint-Joseph) avant le portage vers les Illinois.", 'chap. XIX, p. 433', NOTE_M)
F('m13', 'Fort Crèvecœur', 'poste', '1680-01/1680-04', -89.6, 40.65, 'a', ['René-Robert Cavelier de La Salle', 'Henri de Tonty'],
  "Fort construit chez les Illinois, près du lac Péoria, et abandonné par sa garnison en l'absence de La Salle (relation officielle et relation de Tonty).", 'chap. XIX ; XXI', NOTE_M)
F('m14', 'Embouchure du Mississippi : prise de possession', 'exploration', '1682-04-09', -89.25, 29.15, 'a', ['René-Robert Cavelier de La Salle', 'Henri de Tonty', 'Nicolas de La Salle'],
  "La Salle arrive à l'embouchure du Mississippi et prend possession de la Louisiane, puis remonte au Canada ; récit de Nicolas de La Salle.", 'chap. XX, p. 545', NOTE_M)
F('m15', 'Fort Saint-Louis du Rocher (Tonty)', 'poste', '1682/1684', -88.993, 41.32, 'c', ['Henri de Tonty', 'René-Robert Cavelier de La Salle'],
  "Voyages et établissements des Français sur les lacs et le Mississippi sous La Salle et Tonty, 1678-1684 : relation de Henri de Tonty, qui commande le fort Saint-Louis des Illinois.", 'chap. XXI', NOTE_M)

# ---- Johnson 1905
G = lambda *a, **k: F(*a, source=JO, **k)
G('j01', 'Port-Royal (Caroline du Sud) : Jean Ribault', 'etablissement', '1562', -80.68, 32.38, 'a', ['Jean Ribault'],
  "En 1562, le huguenot Jean Ribault fonde Charlesfort à Port Royal ; la petite garnison abandonne le poste l'année suivante.", '67')
G('j02', 'Fort Caroline : René de Laudonnière', 'etablissement', '1564/1565', -81.5, 30.39, 'a', ['René de Laudonnière', 'Jean Ribault'],
  "En 1564, René de Laudonnière établit une colonie huguenote au fort Caroline, sur la rivière Saint-Jean (Floride) ; les Espagnols la détruisent en 1565.", '77')
G('j03', 'Lac Supérieur : Radisson et Des Groseilliers', 'exploration', '1659/1660', -90.8, 46.6, 'a', ['Pierre-Esprit Radisson', 'Médard Chouart Des Groseilliers'],
  "Pierre-Esprit Radisson et Médard Chouart Des Groseilliers explorent le lac Supérieur et le pays des Sioux ; le récit, abrégé d'après Thwaites, vaut à Radisson une place parmi les découvreurs.", '187')
G('j04', 'Chutes Saint-Antoine : Hennepin', 'exploration', '1680', -93.255, 44.982, 'c', ['Louis Hennepin'],
  "Le récollet Louis Hennepin, envoyé par La Salle vers le haut Mississippi et capturé par les Sioux, nomme les chutes Saint-Antoine (Minneapolis).", '289')
G('j05', 'Assassinat de La Salle', 'evenement', '1687-03-19', -95.9, 30.6, 'h', ['René-Robert Cavelier de La Salle'],
  "Après l'échec de la colonie du Texas, La Salle est assassiné par ses compagnons en cherchant à rejoindre le Mississippi.", '261; 278', "Lieu exact inconnu (vallée de la Brazos ou de la Trinity).")
G('j06', 'Bienville et la fondation de la Louisiane', 'etablissement', '1699/1718', -88.04, 30.69, 'a', ['Pierre Le Moyne d\'Iberville', 'Jean-Baptiste Le Moyne de Bienville'],
  "Supplément sur l'exécution du plan de La Salle par les frères Le Moyne : Biloxi, La Mobile, puis La Nouvelle-Orléans.", '278; 284')
G('j07', 'Les La Vérendrye vers les Rocheuses', 'exploration', '1742/1743', -100.35, 44.37, 'a', ['Louis-Joseph Gaultier de La Vérendrye', 'François Gaultier Du Tremblay'],
  "Les fils La Vérendrye atteignent des montagnes à l'ouest du Missouri (1742-1743) ; une plaque de plomb enfouie à Pierre (Dakota du Sud), retrouvée en 1913, atteste leur passage.", '313', "La plaque de 1913 est postérieure au livre ; ajout de l'atlas pour situer le point.")

# ---- Marchand 2005
H = lambda *a, **k: F(*a, source=GE, **k)
H('g01', 'Garcitas Creek : fort Saint-Louis du Texas', 'poste', '1685/1689-04', -96.73, 28.82, 'c', ['René-Robert Cavelier de La Salle'],
  "En avril 1689, l'expédition espagnole d'Alonso de León trouve, sur la Garcitas, près de la baie de Matagorda, les ruines saccagées de la colonie de La Salle ; l'auteur visite les fouilles et rencontre ses historiens.", '1-2')
H('g02', 'Matagorda : La Salle dans les prairies', 'exploration', '1685/1687', -96.4, 28.7, 'a', ['René-Robert Cavelier de La Salle'],
  "Récit des errances de La Salle dans les prairies du Texas et de sa fin pathétique ; l'auteur cherche un monument dans la campagne.", '44')
H('g03', 'Lachine : le domaine de La Salle', 'etablissement', '1667/1669', -73.67, 45.43, 'c', ['René-Robert Cavelier de La Salle'],
  "Le jeune La Salle obtient une seigneurie à l'ouest de Montréal, surnommée « la Chine » ; une maison d'un de ses censitaires subsiste.", '89')
H('g04', 'Teiaiagon (Baby Point, Toronto) : le Passage de Toronto', 'exploration', '1678', -79.5, 43.66, 'a', ['Louis Hennepin', 'Jacques Baby'],
  "Le Passage de Toronto (Carrying Place) remontait la Humber jusqu'au village sénéca de Teiaiagon, aujourd'hui Baby Point, du nom du colon francophone Jacques Baby (XIXe s.).", '138')
H('g05', 'Détroit : la barque Le Griffon', 'exploration', '1679-08', -83.045, 42.331, 'a', ['René-Robert Cavelier de La Salle', 'Louis Hennepin'],
  "Au quatrième jour, Le Griffon de La Salle entre dans le détroit ; il faudra quatre-vingts ans avant qu'un autre voilier y passe.", '177')
H('g06', 'Saint-Ignace et Michillimakinac', 'poste', '1679/1781', -84.73, 45.87, 'c', ['Jacques Marquette'],
  "Le Griffon fait escale à la mission de Saint-Ignace, où repose Marquette ; le fort Michillimakinac, bâti par les Français sur la rive sud du détroit, est pris par les Britanniques puis déplacé sur l'île de Mackinac après la révolte de Pontiac.", '218; 230')
H('g07', 'Green Bay : Charles Langlade', 'etablissement', '1765~', -88.02, 44.52, 'c', ['Charles de Langlade'],
  "Né à Michillimakinac d'un traiteur français et d'une Outaouaise, Charles Langlade s'installe à Green Bay et en fait un établissement permanent dominé par quelques familles de traiteurs.", '246; 256')
H('g08', 'Beaverville (Illinois)', 'etablissement', '1860~/2005', -87.66, 40.95, 'c', [],
  "Sur la route de La Salle vers le pays des Illinois, l'auteur traverse Beaverville, village d'origine canadienne-française du comté d'Iroquois, dont l'église domine les champs de maïs et de soja.", '262; 264')
H('g09', 'Sainte-Geneviève : la vieille ville française', 'etablissement', '1750~/2005', -90.044, 37.981, 'c', [],
  "Premier établissement permanent du Missouri, aux terres en longues bandes comme au Détroit et sur le Saint-Laurent ; l'auteur évoque l'esclavage en Haute-Louisiane et les légendes locales.", '310; 311')
H('g10', 'Fort Prud\'homme (Chickasaw Bluffs)', 'poste', '1682-02', -89.98, 35.2, 'a', ['René-Robert Cavelier de La Salle', 'Pierre Prud\'homme'],
  "Sur les bluffs du Mississippi, l'armurier Pierre Prud'homme se perd en chassant ; La Salle fait élever une palissade, le fort Prud'homme, pendant les recherches. Le chapitre visite Memphis (fort de l'Assomption).", '332; 333')
H('g11', 'Arkansas Post : les Quapaws', 'poste', '1682-03/1686', -91.35, 34.02, 'c', ['René-Robert Cavelier de La Salle', 'Henri de Tonty'],
  "La Salle est bien accueilli par les Quapaws près du confluent de l'Arkansas ; le poste d'Arkansas, plus ancien établissement européen de la vallée, en découle. L'auteur évoque les Français de l'Arkansas.", '351')
H('g12', 'Pittsfield (Massachusetts) : les Canadiens', 'religion', '1850~/1900~', -73.245, 42.45, 'a', [],
  "Digression sur les Canadiens français de Pittsfield, dont un prêtre fut victime d'une tentative de meurtre, sur fond d'hostilité aux catholiques.", '351; 357')
H('g13', 'Tensas : la capitale des Taensas', 'exploration', '1682-03', -91.33, 31.95, 'a', ['René-Robert Cavelier de La Salle', 'Henri de Tonty'],
  "Dans l'actuelle paroisse de Tensas, l'expédition découvre la capitale des Taensas ; l'auteur poursuit chez les Cadiens (Longfellow, Évangéline).", '375')
H('g14', 'La Nouvelle-Orléans : l\'empire du diable', 'exploration', '1682-04-09', -90.065, 29.958, 'c', ['René-Robert Cavelier de La Salle', 'Jacques de La Métairie'],
  "Le notaire La Métairie dresse l'acte de prise de possession à l'embouchure ; dernier chapitre à La Nouvelle-Orléans, entre tombeaux et mémoire de l'empire.", '404')

fiches = C.fiches
