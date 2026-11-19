# Charles E. Peterson, Colonial St. Louis: Building a Creole Capital (Saint-Louis, Missouri Historical Society, 1949), PDF du Drive de l'auteur.
# Corpus « Recherches », préfixe PT49. Les bâtisseurs et artisans du Saint-Louis colonial.
from commun import Corpus
PT = "Peterson, Charles E. (1949), Colonial St. Louis: Building a Creole Capital, Saint-Louis, Missouri Historical Society"
C = Corpus('Recherches', 'PT49', PT, page_fmt='p. {}')
F = C.F
SL = (-90.1866, 38.6268)
F('01', "Saint-Louis : Amable Guyon, premier maçon, né au fort de Chartres, tué lors de l'attaque de 1780", 'personnage', '1764-06/1780-05-26', *SL, 'c', ['Amable Guyon', 'Pierre Laclède'],
  "Premier tailleur de pierre connu de Saint-Louis, Amable Guyon était né en 1718 au vieux fort de Chartres, dont il a peut-être bâti la grande enceinte de maçonnerie. Venu de Cahokia avec sa famille au début de juin 1764, il travailla sans doute au quartier général en pierre de la compagnie de Laclède, puis se bâtit une maison de pierre de 2 500 livres sur la Grande Rue Royale. Il fut tué le 26 mai 1780 dans les champs derrière le village, lors de l'attaque britannique et amérindienne.",
  '62')
F('02', "Saint-Louis : le maçon Jean-Marie Pepin dit Lachance et la société des « sans-culottes » (1795)", 'evenement', '1795', *SL, 'c', ['Jean-Marie Pepin dit Lachance', 'Francisco Luis Héctor de Carondelet', 'Charles Gratiot', 'Joseph Labrosse'],
  "Né au Canada vers 1740, maître maçon à Saint-Louis dès 1767, Pepin (ou Papin) dit Lachance avait été chassé de Cahokia pour trouble à l'ordre public. Exclu du monopole espagnol de la traite, il aurait aidé à fonder à Saint-Louis une société de « sans-culottes » qui inquiéta les autorités. En 1795, le gouverneur Carondelet ordonna secrètement son arrestation, le qualifiant d'ennemi du gouvernement. Pepin se réfugia quelques mois à Vincennes, puis vendit l'année suivante une grande maison de pierre à Charles Gratiot.",
  '62-63')
F('03', "Saint-Louis : Antoine Roussel dit Sansouci, maçon venu de Lachine, bâtisseur de la prison provinciale (1774)", 'personnage', '1768/1799', *SL, 'c', ['Antoine Roussel dit Sansouci', 'Paul Sigle dit Maltais'],
  "Né vers 1740 dans la paroisse de Lachine, Roussel dit Sansouci figure comme maître maçon à Saint-Louis en 1768 et s'y marie l'année suivante. Il taille une grande meule pour le tanneur Paul Sigle dit Maltais (1769), construit les maisons Sale et Rivière (1770, 1773) et monte la maçonnerie de la prison provinciale en 1774. Milicien et souvent agent de police, il meurt en 1799.",
  '63')
F('04', "Saint-Louis et Florissant : Hyacinthe Saint-Cyr, maçon né près de Québec, ruiné par les fortifications", 'personnage', '1780/1826', -90.3226, 38.7892, 'c', ['Hyacinthe Saint-Cyr'],
  "Né près de Québec vers 1746, Hyacinthe Saint-Cyr arrive à Saint-Louis par Cahokia en 1780 ; il bâtit plusieurs maisons de pierre et un moulin. Il perd de l'argent sur un contrat des fortifications de la ville dans les années 1790 et, en 1801, une grande partie de ses biens (terres à Saint-Louis, Florissant et Creve Coeur, moulin à chevaux, deux fours à chaux, forges) est vendue pour ses créanciers. Il se retire à Florissant, où il meurt en 1826, père de quinze enfants.",
  '63', "Point placé à Florissant, lieu de sa retraite.")
F('05', "Saint-Louis : maison de rondins commandée par Joseph Robidoux, cordonnier arrivé de Montréal (1771)", 'famille', '1771', *SL, 'c', ['Joseph Robidoux', 'Jean-Baptiste Ortès'],
  "En 1771, le menuisier béarnais Jean-Baptiste Ortès s'engage à bâtir pour Joseph Robidoux, cordonnier récemment arrivé de Montréal, une maison de trois pièces en pièce sur pièce (cotonnier, frêne ou noyer). Le prix : cinq cents livres en castors ou en chevreuils, plus trois paires de souliers.",
  '65')
F('06', "Saint-Louis : la boulangerie de pierre et le moulin à huit chevaux de Joseph Robidoux (1802-1809)", 'commerce', '1802/1809', *SL, 'c', ['Joseph Robidoux'],
  "À la fin de la période coloniale, Joseph Robidoux bâtit une boulangerie de pierre à deux étages derrière sa grande maison de la Grande Rue Royale. Il semble avoir eu des contrats de pain et de biscuits, faits avec la farine de son moulin. Ce moulin, mû par huit chevaux en 1802, était sans doute l'un des plus grands de son genre. L'inventaire de 1809, à sa mort, détaille le matériel de boulanger : pétrins, pelles de bois, corbeilles à pain.",
  '38, 40')
F('07', "Saint-Louis : le moulin de Joseph Taillon, premier meunier (1766-1799)", 'commerce', '1766-08-11/1799', *SL, 'c', ['Joseph Taillon'],
  "Joseph Taillon bâtit le premier moulin de Saint-Louis, établi le 11 août 1766. Premier meunier de la ville, il avait 82 ans à la fin du siècle et ne pouvait plus gérer ses affaires. Il possédait encore un moulin à chevaux à deux meules, estimé à quatre cents dollars, quand ses biens furent vendus en 1799.",
  '37-38')
F('08', "Rivière Maline : la scierie du capitaine Jean-Baptiste Montigny et d'André Roy (1770-1774)", 'commerce', '1770/1774', -90.2150, 38.7450, 'a', ['Jean-Baptiste Montigny', 'André Roy', 'Joachim Roy', 'François Mandeville', 'Charles Bizet'],
  "Sur une concession de quatre arpents obtenue en 1770 sur la rivière Maline, à deux lieues en amont de Saint-Louis, Montigny et André Roy montent un moulin à scie avec une petite maison de chaume. L'association est dissoute deux ans plus tard. Le moulin est loué à Joachim Roy et François Mandeville contre 2 000 planches, endommagé par une crue, vendu en 1774 à Charles Bizet, puis réuni au domaine royal.",
  '38', "Position approximative sur le cours inférieur du ruisseau Maline.")
F('09', "Saint-Louis : la tannerie du Canadien Jean-Baptiste Lorraine, achetée par Manuel Lisa (1780-1799)", 'commerce', '1780/1799', *SL, 'c', ['Jean-Baptiste Lorraine', 'Manuel Lisa', 'Jean Valdy'],
  "Corroyeur et tanneur canadien, Jean-Baptiste Lorraine est à Saint-Louis dès 1780. Sa maison et sa tannerie de la rue de l'Église sont achetées en 1799 par Manuel Lisa, jeune traiteur arrivé de La Nouvelle-Orléans. Peterson nomme aussi les tanneurs Paul Sigle dit le Maltais (mort en 1769) et Jean Valdy.",
  '40')
F('10', "Saint-Louis : la poterie de Joseph Eberlein, « artiste » (vers 1795-1797)", 'commerce', '1795~/1797', *SL, 'c', ['Joseph Eberlein', 'Louis Boissy', 'François Drouin'],
  "Seule poterie connue du Saint-Louis colonial : Joseph Eberlein, dit artiste, a vers 1796 un four à cuire la terre sur la rue de l'Église. Il le vend 2 000 livres à Louis Boissy, qui ne peut payer. La propriété est revendue aux enchères en 1797 à François Drouin (ou Derouen), jeune marchand ambulant de Montréal.",
  '40')
F('11', "Carondelet : les noms de Prairie à Catalan, Vide-Poche, Louisbourg et Pain de Sucre (1771)", 'toponymie', '1771', -90.2627, 38.5612, 'c', ['Clément Delor de Tréget', 'Claude Tinon', 'Joseph Boisvert'],
  "En 1771 ou plus tôt, les terres du nouveau faubourg de la Prairie à Catalan furent détachées de la Commune de Saint-Louis. Le lieu fut aussi appelé Vide-Poche, Louisbourg, Pain de Sucre, puis Carondelet. Clément Delor de Tréget reçut les premières concessions le 20 août 1771, suivi de Claude Tinon, des Thabault, de Joseph Boisvert et des Ménard en 1773-1774.",
  '24')
F('12', "Chez les Grands Osages : mort du menuisier Jean Cambas (1784)", 'personnage', '1784', -94.18, 38.05, 'h', ['Jean Cambas', 'Jean-Baptiste Ortès'],
  "Né en France vers 1736, associé d'Ortès dès 1767, Jean Cambas acheva l'église du village en 1776. Milicien de Saint-Louis, il mourut en 1784 chez les Grands Osages. Son inventaire mentionne deux grands dictionnaires de l'Académie française et trente-cinq rabots.",
  '66', "Point placé dans la région des villages osages de la rivière Osage ; lieu exact inconnu.")
fiches = C.fiches
