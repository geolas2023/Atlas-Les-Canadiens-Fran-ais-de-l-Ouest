# John Rothensteiner, History of the Archdiocese of St. Louis in its Various Stages of Development from A.D. 1673 to A.D. 1928,
# vol. II (Saint-Louis, Blackwell Wielandy, 1928) ; PDF fourni par l'auteur de l'atlas le 19 novembre 2026. Corpus « Recherches », préfixe ROT28.
# Le volume II couvre surtout l'épiscopat Kenrick (1843-1895) ; on n'en retient que ce qui touche les paroisses et missions francophones
# et les rapports avec les Autochtones. Résumés rédigés par l'atlas.
from commun import Corpus
SRC = "Rothensteiner, John (1928), History of the Archdiocese of St. Louis, vol. II, Saint-Louis, Blackwell Wielandy"
C = Corpus('Recherches', 'ROT28', SRC, page_fmt='p. {}')
F = C.F

F('01', "Kawsmouth : la « Chouteau's Church », première chapelle du site de Kansas City (1833-1839)", 'religion', '1833/1839', -94.590, 39.110, 'a', ['Benedict Roux', 'Joseph Anthony Lutz', 'Felix Van Quickenborne', 'François Chouteau'],
  "À l'établissement français de Kawsmouth, l'abbé Lutz séjourne en 1828 en allant chez les Kansas ; l'abbé Benedict Roux arrive le 14 novembre 1833 et achète un terrain où les frères Chouteau bâtissent, après son départ, une chapelle et un presbytère en rondins. Longtemps appelée simplement « Chouteau's Church », elle reçoit le 17 novembre 1839 le titre de Saint-François-Régis. Le jésuite Van Quickenborne y officie en juillet 1835 et y baptise en juillet 1836 quatorze enfants têtes-plates, kootenais et iroquois de la bande descendue des Rocheuses en 1831.",
  None, "Position de l'ancienne église Saint-François-Régis (quartier des berges de Kansas City).")
F('02', "Kansas City : l'abbé Bernard Donnelly et la paroisse française du confluent (1845-1863)", 'religion', '1845/1863', -94.585, 39.105, 'a', ['Bernard Donnelly', 'Augustus Saunier'],
  "Chargé d'Independence en 1845, Donnelly dessert aussi la paroisse de Kansas City (sauf en 1848-1849, où Augustus Saunier en est curé avant d'être muté à Little Canada) ; il y transfère sa résidence en 1857, remplace l'église Saint-François-Régis par un édifice de brique et meurt le 1er novembre 1863. La terre achetée par Roux en 1839 s'avère « une véritable mine d'or » pour la paroisse.",
  None, "Position de l'église Saint-François-Régis.")
F('03', "Saint-Joseph (Missouri) : le comptoir de Joseph Robidoux devient une ville (1830-1847)", 'etablissement', '1830/1847', -94.851, 39.768, 'a', ['Joseph Robidoux', 'Anthony Eysvogels', 'Thomas Scanlon', 'Pierre-Jean De Smet'],
  "Rothensteiner décrit le site, cent ans plus tôt, comme une ligne de collines boisées avec la cabane d'un traiteur et un débarcadère : Joseph Robidoux, troisième du nom, acquiert en 1830 la terre où s'élèvera la ville, la fait lotir et vend les lots ; la ville compte 20 000 âmes en 1864. Le jésuite Eysvogels y baptise en 1842 aux Black Snake Hills (« Robidoux's Landing »). Le premier curé résident, Thomas Scanlon, arrive le 25 octobre 1845 ; De Smet, de passage le 23 novembre 1846, compte 350 maisons et une population d'Américains, de Créoles français, d'Irlandais et d'Allemands. L'église est dédiée le 17 juin 1847.",
  99, "Position du centre historique de Saint-Joseph (rue Felix).")
F('04', "Old Mines : de la chapelle de rondins de Henri Pratte à l'église de brique de Bouillier (vers 1820-1857)", 'religion', '1820/1857', -90.770, 38.005, 'c', ['Henri Pratte', 'John Bouillier', 'Dahmen', 'James Fox'],
  "La région d'Old Mines est explorée dès 1723 par des officiers et des experts miniers français. Peu avant 1820, Henri Pratte, curé de Sainte-Geneviève, y bâtit une église de rondins ; le registre commence le 20 avril 1820. La paroisse devient autonome en 1826 avec le lazariste John Bouillier, qui élève une église de brique (pierre angulaire en 1828) consacrée par Mgr Rosati ; agrandie, elle est reconsacrée le 15 novembre 1857.",
  None, "Position de l'église Saint-Joachim d'Old Mines.")
F('05', "Little Canada (French Village) : paroisse des Canadiens du comté de Sainte-Geneviève (1848-1858)", 'religion', '1848/1858', -90.340, 37.985, 'a', ['Francis Rutkowski', 'Aloysius Rosi', 'John Anselm'],
  "French Village, appelé aussi Little Canada, reçoit des curés successifs : Francis Rutkowski de 1848 à 1856, Aloysius Rosi, noyé le 29 août 1853 dans le ruisseau Establishment en allant voir un malade, puis John Anselm, qui dessert aussi l'Establishment, les mines Vallé et Bloomsdale (1858).",
  None, "Position de French Village (comté de Sainte-Geneviève).")
F('06', "Apple Creek : église de pierre de l'abbé Loisel (1833-1834)", 'religion', '1833/1834', -89.700, 37.640, 'a', ['Loisel', 'Joseph Rosati'],
  "En février 1833, l'abbé Loisel commence une église de pierre de 30 pieds sur 40 à Apple Creek, bénite par Mgr Rosati le 30 novembre 1834 ; Loisel est promu en 1836 à la vieille paroisse de Cahokia à la mort de l'abbé Condamine.",
  None, "Position approximative d'Apple Creek (comté de Perry).")
F('07', "Potosi (Mine à Breton) : l'abbé Lewis Tucker et la pétition de Firmin Desloge (1835-1844)", 'religion', '1834/1844', -90.787, 37.936, 'a', ['Lewis Tucker', 'Firmin Desloge', 'Bouillier', 'Borgna'],
  "L'église de brique de Mine à Breton est consacrée par Rosati le 27 avril 1834 ; desservie d'Old Mines par Borgna et Bouillier, elle reçoit en 1835 l'abbé Lewis Tucker, petit-fils du premier colon catholique du comté de Perry. Les paroissiens, menés par Firmin Desloge, pétitionnent pour le garder, et il reste jusqu'en 1844.",
  None, "Position de Potosi.")
F('08', "Fredericktown : l'église Saint-Michel et les vieilles familles françaises de Mine La Motte (1845-1869)", 'religion', '1845/1869', -90.294, 37.560, 'a', ['Lewis Tucker'],
  "Curé de Saint-Michel de Fredericktown à partir de 1845, Tucker bâtit le corps principal de l'église ; ses revenus viennent surtout des ouvriers irlandais et allemands du chemin de fer (1855-1869) et des généreuses offrandes aux mariages des vieilles familles françaises du secteur, avant que l'immigration allemande n'envahisse Mine La Motte après 1840.",
  None, "Position de Fredericktown.")
F('09', "New Madrid et Little Prairie : paroisses françaises ravagées par le séisme (1811-1869)", 'religion', '1811/1869', -89.528, 36.587, 'a', ['Francis Cellini', 'Lewis Tucker', 'Julian Turmel'],
  "Avant le tremblement de terre de 1811-1812, Little Prairie compte deux cents familles, pour la plupart françaises et catholiques ; le district est ensuite dépeuplé. À New Madrid, le registre des baptêmes s'ouvre le 24 mars 1821 sous Cellini ; les curés se succèdent de façon intermittente (Tucker en 1845, Turmel en 1857-1858) jusqu'à la dédicace de l'église de 1869.",
  None, "Position de New Madrid.")
F('10', "Carondelet : église de l'abbé Saulnier et séminaire (1819-1861)", 'religion', '1819/1861', -90.260, 38.555, 'a', ['Edmond Saulnier', 'Félix De Andreis', 'Louis-Guillaume-Valentin Du Bourg'],
  "À Carondelet (Vide-Poche), la « modeste cabane de planches » posée par De Andreis en 1819 sur ordre de Du Bourg est remplacée par l'église de rondins de l'abbé Edmond Saulnier (1839), puis par son église de 1841. Le séminaire diocésain de Carondelet forme ensuite le clergé de Mgr Kenrick ; la cathédrale garde un tableau des Épousailles offert par Louis XVIII à Du Bourg en 1818.",
  None, "Position du vieux Carondelet.")
F('11', "Gravois et la Meramec : église de pierre de Van Quickenborne et catholiques français (1833-1842)", 'religion', '1833/1842', -90.410, 38.583, 'a', ['Charles Van Quickenborne', 'Peter Richard Donnelly'],
  "Le jésuite Van Quickenborne fait bâtir dès 1833 une petite église de pierre à Gravois, vingt ans avant la ville de Kirkwood, dont le nom (« forêt de l'église ») en garderait le souvenir ; en 1842, un prêtre est chargé d'organiser les catholiques irlandais et français le long de la Meramec.",
  None, "Position de Kirkwood.")
F('12', "Lagrange : le comptoir de Godfrey Le Seur à l'embouchure de la Wyaconda (1795)", 'commerce', '1795', -91.497, 40.042, 'a', ['Godfrey Le Seur', 'Peter Paul Lefevere'],
  "L'abbé Lefevere visite en 1837 Lagrange, héritière du « comptoir de Godfrey Le Seur à l'embouchure de la Wyaconda » (1795), selon l'historien des comtés de Clark et Lewis que cite Rothensteiner ; l'église bâtie en 1867 est vendue en ruine en 1893.",
  None, "Position de Lagrange (Missouri).")
F('13', "Dardenne : les Canadiens français cèdent la place aux Allemands (1830-1860)", 'migration', '1830/1860', -90.700, 38.770, 'a', [],
  "Au territoire de Dardenne (comté de Saint-Charles), l'immigration allemande venue du Hanovre arrive par petits groupes de 1830 à 1840, puis en masse jusqu'en 1860, pendant que les Canadiens français se retirent peu à peu ailleurs ; les jésuites y nomment alors des prêtres allemands.",
  None, "Position approximative de la paroisse de Dardenne.")
F('14', "Florissant : le noviciat jésuite de Saint-Stanislas et le couvent de Philippine Duchesne (1819-1846)", 'religion', '1819/1846', -90.335, 38.795, 'c', ['Philippine Duchesne', 'Charles Van Quickenborne', 'Pierre-Jean De Smet', 'John Gleizal'],
  "Les religieuses du Sacré-Cœur s'installent à Florissant en 1819 ; Mère Duchesne part le 27 mai 1826 pour Saint-Louis et le couvent est supprimé en 1846. Le noviciat Saint-Stanislas commence en 1823 dans une misérable cabane de rondins de la ferme jésuite, avec Van Quickenborne comme maître des novices et, parmi les six jeunes gens venus du Maryland, Pierre-Jean De Smet.",
  None, "Position du vieux Saint-Ferdinand de Florissant.")
F('15', "Cahokia et Kaskaskia : les Visitandines chassées par la crue de 1844", 'religion', '1833/1844', -89.917, 37.921, 'a', ['Joseph Rosati', 'John Timon'],
  "Le couvent et l'école de la Visitation, fondés à Kaskaskia en 1833 par Mgr Rosati, sont engloutis par la grande crue de 1844 ; Kenrick et Timon recueillent les religieuses à Saint-Louis. La même crue détruit l'établissement des Sœurs de Saint-Joseph à Cahokia, tandis que celui de Carondelet devient leur maison mère.",
  None, "Position de l'ancien Kaskaskia.")
F('16', "Saint-Louis : The Shepherd of the Valley, premier journal catholique à l'ouest du Mississippi, bilingue (1832-1833)", 'religion', '1832/1833', -90.1868, 38.6245, 'a', ['Joseph Rosati'],
  "Lancé sous Mgr Rosati en 1832, le Shepherd of the Valley paraît la première année en anglais et en français, puis en anglais seulement à partir du 20 septembre 1833 ; Rothensteiner signale aussi un journal français fondé à Saint-Louis en 1854.",
  None, "Position de l'ancienne cathédrale.")

fiches = C.fiches
