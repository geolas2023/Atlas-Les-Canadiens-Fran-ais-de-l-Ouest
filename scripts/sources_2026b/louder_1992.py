# Dean Louder (dir. et trad.), The Heart of French Canada: From Ottawa to Quebec City, New Brunswick, Rutgers University Press, 1992 (Touring North America).
# PDF du Drive de l'auteur (HISTOIRE_LIVRES/DEAN_LOUDER), lu en entier le 19 novembre 2026 par la visionneuse du Drive (192 p.).
# Guide d'excursion du 27e Congrès géographique international, centré sur la vallée laurentienne ; on ne retient que
# la migration canadienne-française hors du Québec (Est ontarien). Préfixe LO92.
from commun import Corpus
S = "Louder, Dean, dir. (1992), The Heart of French Canada: From Ottawa to Quebec City, New Brunswick, Rutgers University Press (chap. « Day Two », M. Phipps, N. Castéran et A. Gilbert)"
C = Corpus('Recherches', 'LO92', S, page_fmt='p. {}')
F = C.F
F('01', "Comtés de Prescott et Russell : la colonisation canadienne-française de l'Est ontarien conduite par l'Église (1851-1911)", 'migration', '1851/1911', -74.903, 45.390, 'a', [],
  "Pour enrayer l'exode vers les villes textiles de la Nouvelle-Angleterre, l'élite canadienne-française, surtout le clergé, prône la colonisation de terres neuves. Des paroisses entières du Québec, sous la conduite de leurs curés, viennent défricher l'Est ontarien : les Canadiens français y passent de 4 000 en 1851 à 42 000 en 1911. Le bloc francophone de Prescott et Russell s'oppose encore aux comtés anglophones de Stormont et Glengarry ; Saint-Isidore-de-Prescott y est un centre régional dynamique, le village bâti autour de l'église, du presbytère et du cimetière.",
  '39-41', "Point placé à Saint-Isidore-de-Prescott, cité par les auteurs comme exemple de village francophone.")
F('02', "Hawkesbury : les scieries attirent les Canadiens français, majoritaires dès les années 1860", 'etablissement', '1840/1869', -74.606, 45.607, 'a', [],
  "Dès 1840, les scieries ont fait de Hawkesbury, d'abord anglophone, un village cosmopolite. De nombreux Canadiens français y affluent pour travailler dans les moulins et deviennent majoritaires dans les années 1860.",
  '42', "")
F('03', "Alexandria : boîtes à fromage J. T. Schell et Carriage Works, la ville devient majoritairement française (1910)", 'etablissement', '1880/1910', -74.636, 45.309, 'a', [],
  "Le travail du bois, la fabrication des boîtes à fromage J. T. Schell et la Carriage Works rendent Alexandria (comté de Glengarry) majoritairement française vers 1910.",
  '42', "Date de début approximative ; Louder ne donne que 1910.")
F('04', "Cornwall : les Canadiens français apportent l'expérience des filatures du Québec et de la Nouvelle-Angleterre (1901)", 'etablissement', '1901', -74.730, 45.021, 'c', [],
  "L'industrialisation de Cornwall, ville loyaliste, aurait été impossible sans l'expérience acquise par les Canadiens français dans les filatures du Québec et de la Nouvelle-Angleterre. En 1901, la ville compte 6 700 habitants, dont 2 500 d'origine canadienne-française, regroupés dans des quartiers francophones autour des usines, avec leurs églises et leurs commerces.",
  '42', "")
fiches = C.fiches
