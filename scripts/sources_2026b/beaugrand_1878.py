# Honoré Beaugrand, Jeanne la fileuse : épisode de l'émigration franco-canadienne aux États-Unis (Fall River, 1878),
# epub Wikisource du Drive de l'auteur (dossier « Histoire du Canada »). Roman à thèse dont les annexes reproduisent
# des documents (presse de Fall River, statistiques de Rameau). Corpus « Recherches », préfixe BG78.
from commun import Corpus
BG = "Beaugrand, Honoré (1878), Jeanne la fileuse : épisode de l'émigration franco-canadienne aux États-Unis, Fall River (éd. Wikisource)"
C = Corpus('Recherches', 'BG78', BG, page_fmt='{}')
F = C.F
F('01', "Fall River : l'incendie de la filature Granite et ses victimes canadiennes-françaises (19 septembre 1874)", 'evenement', '1874-09-19', -71.1550, 41.7015, 'c', ['Noé Poitras', 'Victorine Beaunoyer', 'Marie Lasonde', 'A. de Montaubricq', 'Honoré Beaugrand'],
  "Beaugrand reproduit le compte rendu d'un journal de Fall River sur l'incendie de la filature Granite. La plupart des victimes sont des femmes et des enfants ; les corps sont déposés à la chapelle de la mission de la rue Pleasant. Le curé de l'église canadienne-française, l'abbé A. de Montaubricq, et les médecins canadiens se portent au secours des blessés. Trois enfants canadiens-français périssent : Noé Poitras, tué en sautant d'une fenêtre, Victorine Beaunoyer et Marie Lasonde, brûlées vives. Cinq autres sont blessés en sautant sur les draps tendus et les matelas.",
  'deuxième partie', "Beaugrand insère parmi les blessés son héroïne fictive, Jeanne Girard ; les autres noms viennent de la liste officielle publiée par la presse. Date de l'incendie d'après les sources sur la filature Granite n° 1.")
F('02', "Frontière de l'État de New York : les colonies canadiennes du lac Champlain et du Saint-Laurent (vers 1855)", 'migration', '1840~/1859', -73.4529, 44.6995, 'c', ['Mignault', 'Rameau de Saint-Père'],
  "En note, Beaugrand cite Rameau de Saint-Père : vers 1840, le commerce du bois attire les Canadiens vers Rouses Point, Burlington, Plattsburgh, Port Henry et Whitehall. D'après l'abbé Mignault, missionnaire de ces postes depuis 42 ans, on compte 800 familles canadiennes à Champlain et Corbeau, autant à Plattsburgh et Keeseville, 1 000 à 1 200 âmes à Morristown, Port Henry et Ticonderoga, et 500 familles à Ogdensburg. La population est estimée à 6 000 âmes sur la rive du Saint-Laurent, et à 800 ou 900 au cap Vincent et à Rosière, sur le lac Ontario. Mignault assure que ces Canadiens y gardent leur langue et leur foi.",
  'notes de la deuxième partie', "Point placé à Plattsburgh.")
F('03', "Fall River : Beaugrand y publie L'Écho du Canada et son roman de l'émigration (1874-1878)", 'etablissement', '1874/1878-03-15', -71.1550, 41.7015, 'c', ['Honoré Beaugrand'],
  "Beaugrand écrit Jeanne la fileuse au jour le jour, en feuilleton, à Fall River, et en signe la préface le 15 mars 1878. Il se plaint d'avoir dû confier l'impression à des typographes américains qui ne savaient pas un mot de français. Le roman veut répondre aux détracteurs des émigrés : les familles partent de Lavaltrie et de Contrecœur et arrivent en un jour, par chemin de fer, aux logements des filatures Granite. Une note reproduit l'appel du 17 mars 1874 en vue d'une grande fête nationale à Montréal, paru notamment dans L'Écho du Canada du 4 avril 1874.",
  'préface et notes')
fiches = C.fiches
