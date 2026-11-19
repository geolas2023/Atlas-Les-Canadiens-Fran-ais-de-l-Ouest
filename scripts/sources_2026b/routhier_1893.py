# Adolphe-Basile Routhier, De Québec à Victoria (Québec, L.-J. Demers & Frère, 1893), epub Wikisource du Drive de l'auteur
# (dossier « Histoire du Canada »). Récit de l'excursion épiscopale organisée par le père Lacombe en mai 1892.
# Corpus « Recherches », préfixe RT93.
from commun import Corpus
RT = "Routhier, Adolphe-Basile (1893), De Québec à Victoria, Québec, L.-J. Demers & Frère"
C = Corpus('Recherches', 'RT93', RT, page_fmt='{}')
F = C.F
F('01', "Calgary : le père Lacombe, « président du Pacifique canadien pendant une heure » (vers 1883)", 'personnage', '1883~', -114.0719, 51.0447, 'a', ['Albert Lacombe', 'George Stephen'],
  "Routhier ouvre son récit sur une anecdote : alors que le chemin de fer n'est pas encore en service dans la prairie, George Stephen invite le père Lacombe, missionnaire à Calgary, à dîner dans son wagon-salon. Les magnats du Canadien Pacifique le font président de la compagnie pour une heure, Stephen cédant de bonne grâce sa place. Le lendemain, ils le déposent à 40 milles de Calgary, en pleine prairie, où l'appelle son ministère. C'est à Lacombe et à la compagnie que Routhier dédie le livre de l'excursion de 1892.",
  'chap. I', "Date approximative : arrivée du chemin de fer à Calgary (1883).")
F('02', "Manitoba : les paroisses françaises et la « grande faute » des Canadiens français (1892)", 'migration', '1892', -97.1384, 49.8951, 'c', [],
  "À Winnipeg, Routhier énumère les centres peuplés de Français, de Belges, de Canadiens français et de Métis : Saint-Norbert, Saint-Léon, Saint-Alphonse, Saint-Laurent, Lourdes, Sainte-Anne, le Lac des Chênes, Saint-Malo, la Grande-Clairière. Il note que quelque 20 000 colons sont arrivés au Manitoba en 1892 et que le Canadien Pacifique y a vendu 890 000 acres, mais que les Canadiens français ne comptent presque pas dans ce flot. Il reproche aux Québécois de n'avoir pas organisé leur émigration vers l'Ouest dix ans plus tôt.",
  'chap. IX')
F('03', "Duck Lake : à la gare, les gens du pays racontent Batoche (21 mai 1892)", 'evenement', '1892-05-21', -106.2220, 52.8150, 'a', [],
  "En route vers Prince-Albert, le train des évêques s'arrête une demi-heure à Duck Lake, à 8 ou 10 milles de Batoche. Routhier interroge les habitants venus saluer les évêques sur la rébellion de 1885. Leurs récits sont si tristes qu'il préfère ne pas les reproduire : s'ils sont vrais, écrit-il, le soleil de Batoche n'a pas été celui d'Austerlitz.",
  'chap. X')
F('04', "Prince-Albert : bénédiction de la pierre angulaire de la cathédrale par Mgr Pascal et Mgr Taché (22 mai 1892)", 'religion', '1892-05-22', -105.7531, 53.2033, 'c', ['Albert Pascal', 'Alexandre-Antonin Taché', 'Albert Lacombe'],
  "Le dimanche 22 mai 1892, à Prince-Albert, l'excursion épiscopale assiste à la messe au couvent puis à la bénédiction de la pierre angulaire de la cathédrale, avec des discours de Mgr Pascal et de Mgr Taché.",
  'chap. XI')
F('05', "Calgary : l'excursion épiscopale reçue chez le juge Rouleau (25-26 mai 1892)", 'evenement', '1892-05-25/1892-05-26', -114.0719, 51.0447, 'c', ['Charles-Borromée Rouleau', 'Albert Lacombe', 'Alexandre-Antonin Taché', 'Brondel'],
  "Arrivée à Calgary à deux heures du matin la veille de l'Ascension (25 mai 1892), l'excursion y passe deux jours. Les évêques sont reçus chez le juge Rouleau ; banquet et discours réunissent le père Lacombe, Mgr Taché et les magnats du Pacifique. Le soir, Mgr Brondel, évêque d'Helena, prêche pour le mois de Marie.",
  'chap. XV')
F('06', "Hobbema, Edmonton et Saint-Albert : les Cris, les Métis et Mgr Taché (27-28 mai 1892)", 'religion', '1892-05-27/1892-05-28', -113.6250, 53.6305, 'c', ['Alexandre-Antonin Taché', 'Albert Lacombe', 'Vital-Justin Grandin'],
  "Sur la ligne d'Edmonton, l'excursion rencontre des Cris à Hobbema, qui prononcent des discours. À la gare d'Edmonton, Mgr Taché répond aux adresses et rappelle les jours d'antan à « ses chers Métis ». Le 28 mai, sous la pluie et la grêle, les excursionnistes se rendent à Saint-Albert, siège épiscopal à neuf milles au nord-ouest d'Edmonton. Routhier y recueille ensuite les récits du père Lacombe sur les Cris et les Pieds-Noirs : la petite vérole, le chef cri Wikaskokiseyin (Foin-de-Senteur), signataire des traités.",
  'chap. XVI-XX', "Point placé à Saint-Albert.")
fiches = C.fiches
