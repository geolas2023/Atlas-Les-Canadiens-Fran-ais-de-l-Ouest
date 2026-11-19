# Charles R. Daoust, Cent-vingt jours de service actif : récit historique très complet de la campagne du 65e au Nord-Ouest
# (Montréal, 1886), epub Project Gutenberg du Drive de l'auteur. Corpus « Recherches », préfixe DA86.
# Dates tirées du « tableau chronologique » du livre.
from commun import Corpus
DA = "Daoust, Charles R. (1886), Cent-vingt jours de service actif : récit historique très complet de la campagne du 65e au Nord-Ouest, Montréal"
C = Corpus('Recherches', 'DA86', DA, page_fmt='{}')
F = C.F
F('01', "Calgary : le 65e bataillon de Montréal au camp, entre chinook et première messe (12-20 avril 1885)", 'evenement', '1885-04-12/1885-04-23', -114.0719, 51.0447, 'c', ['Major Dugas', 'Lieutenant Starnes'],
  "Appelé en service actif le 28 mars 1885 et parti de Montréal le 2 avril, le 65e bataillon traverse en traîneau les sections inachevées du chemin de fer au nord du lac Supérieur. Il arrive à Calgary le 12 avril. Il y essuie une tempête de neige appelée « chinouck », assiste le 19 avril à sa première messe à la mission, puis se divise en deux colonnes (bataillon droit le 20 avril, bataillon gauche le 23) pour marcher sur Edmonton.",
  'tableau chronologique ; 1re partie, chap. I-II')
F('02', "Traverse du Chevreuil Rouge (Red Deer) : la compagnie du lieutenant Normandeau et le fort Normandeau (30 avril-29 juin 1885)", 'poste', '1885-04-30/1885-06-29', -113.8880, 52.2720, 'c', ['Lieutenant Normandeau'],
  "Le 30 avril 1885, la compagnie n° 8 du 65e est laissée à la Traverse du Chevreuil Rouge sous le commandement du lieutenant Normandeau. Elle y garde le passage de la piste Calgary-Edmonton dans un poste fortifié qui prend le nom de fort Normandeau. Le détachement rejoint Edmonton le 29 juin.",
  'tableau chronologique ; 3e partie, chap. V')
F('03', "Rivière Bataille et Ferme du Gouvernement : les forts Ostell et Ethier du 65e (mai-juin 1885)", 'poste', '1885-05-02/1885-06-29', -113.5800, 52.6700, 'a', ['Capitaine Ethier', 'Lieutenant Villeneuve', 'Lieutenant-colonel Ouimet'],
  "Le long de la piste d'Edmonton, le bataillon gauche laisse des détachements à la rivière Bataille et à la Ferme du Gouvernement, sous le lieutenant Villeneuve puis le capitaine Ethier. Ces postes deviennent les forts Ostell et Ethier. Le lieutenant-colonel Ouimet les inspecte en mai ; les garnisons rejoignent Edmonton les 28 et 29 juin.",
  'tableau chronologique ; 3e partie, chap. I et IV', "Point placé à la traverse de la rivière Bataille (Ponoka), site attribué au fort Ostell ; le fort Ethier était plus au nord, près de la Ferme du Gouvernement.")
F('04', "Lac aux Grenouilles : le 65e élève une croix à la mémoire des « martyrs » (25 mai 1885)", 'religion', '1885-05-25', -110.3300, 53.8800, 'c', [],
  "En marche avec la colonne du général Strange, le bataillon droit du 65e traverse l'anse du Lac aux Grenouilles (Frog Lake) le 24 mai 1885. Le lendemain, il y élève une croix à la mémoire des victimes du massacre du 2 avril, parmi lesquelles deux missionnaires oblats.",
  'tableau chronologique ; 2e partie, chap. II')
F('05', "Butte-aux-Français : le 65e au combat contre Gros-Ours ; Lemay et Marcotte blessés (28 mai 1885)", 'evenement', '1885-05-27/1885-06-03', -109.6200, 53.5800, 'c', ['Gros-Ours', 'Thomas Bland Strange', 'Lemay', 'Marcotte', 'Isidore Gauthier'],
  "Après une première rencontre la veille, la colonne Strange, dont le bataillon droit du 65e, livre le 28 mai 1885 la bataille de la Butte-aux-Français (Frenchman's Butte) contre les Cris de Gros-Ours. Les soldats Lemay et Marcotte, blessés, sont évacués le 3 juin vers l'hôpital de Battleford, accompagnés par le soldat Isidore Gauthier.",
  'tableau chronologique ; 2e partie, chap. III-V')
F('06', "Bear's Run (lac Froid) : les Montagnais se soumettent par l'entremise des pères Legoff et Prévost (8-12 juin 1885)", 'evenement', '1885-06-08/1885-06-24', -110.2000, 54.4500, 'a', ['Laurent Legoff', 'Prévost', 'Major Hughes', 'Capitaine Giroux'],
  "Poursuivant Gros-Ours vers le nord, le bataillon droit campe à Bear's Run. Le 10 juin, les pères oblats Legoff et Prévost sont délégués auprès des Montagnais (Dénés chipewyans), qui se soumettent le 12. Le bataillon reçoit le 23 juin l'ordre du retour à Montréal.",
  'tableau chronologique ; 2e partie, chap. IV', "Position approximative de Bear's Run, entre la rivière Castor et le lac Froid.")
F('07', "Fort Pitt et Battleford : la mort du sergent Valiquette (3-5 juillet 1885)", 'evenement', '1885-07-03/1885-07-05', -108.2300, 52.7300, 'c', ['Sergent Valiquette', 'Lieutenant-colonel Williams'],
  "Le 65e, réuni à Fort Pitt le 2 juillet, y perd le lendemain le sergent Valiquette, mort le même jour que le lieutenant-colonel Williams des Midlands. Leurs funérailles ont lieu le 5 juillet à Battleford. Le bataillon redescend ensuite la Saskatchewan et traverse le lac Winnipeg ; il rentre à Montréal le 20 juillet, après cent vingt jours de service.",
  'tableau chronologique ; 4e partie', "Point placé à Battleford.")
fiches = C.fiches
