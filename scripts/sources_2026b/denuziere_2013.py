# Maurice Denuzière, La dix-huitième étoile. Histoire de la Louisiane américaine, Paris, Fayard, 2013 (epub du Drive de
# l'auteur, pack « Histoire des États-Unis »). Préfixe DZ13.
from commun import Corpus
DZ = "Denuzière, Maurice (2013), La dix-huitième étoile. Histoire de la Louisiane américaine, Paris, Fayard"
C = Corpus('Recherches', 'DZ13', DZ, page_fmt='{}')
F = C.F
F('01', "La Nouvelle-Orléans coupée en trois municipalités : créoles contre Américains (1836)", 'evenement', '1836-06-15/1852', -90.0650, 29.9580, 'c', ['Denis Prieur'],
  "Au début des années 1830, la cohabitation des créoles francophones et catholiques et des Américains protestants tourne à l'affrontement. Le 15 juin 1836, un créole tue en duel un Américain qui l'avait outragé ; acquitté par un juge louisianais au nom du code de l'honneur, il provoque le siège du domicile du magistrat par la foule américaine. Le gouverneur et le maire Denis Prieur se résolvent alors à partager la ville en trois municipalités, chacune avec son conseil, sa police et ses impôts : la première, créole, du Vieux Carré entre la rue du Canal et l'avenue de l'Esplanade ; la deuxième, américaine, en amont ; la troisième, en aval. L'expérience dure jusqu'à la réunification de 1852.",
  "1re époque, ch. 4, « Créoles et Américains »", "Point au Vieux Carré. La réunification de 1852 est rappelée par l'atlas.")
F('02', "Bayou Teche (plantation Arlington) : les gens de couleur libres, une communauté francophone (vers 1830-1850)", 'personnage', '1830/1850', -91.5020, 29.7970, 'a', ['Euphrazie Carlin', 'Honoré Carlin', 'Charles Roques', 'Martin Donato'],
  "En 1840, les gens de couleur libres de La Nouvelle-Orléans forment une communauté francophone et catholique de vingt-cinq mille personnes, privée du droit de vote mais instruite et aisée : négociants, juristes, artisans, musiciens, pilotes de vapeurs. Certains sont planteurs et possèdent des esclaves (962 en 1830) : Charles Roques dans la paroisse de Natchitoches, Martin Donato dans celle de Saint-Landry (mort en 1848), ou Euphrazie Carlin, qui fait bâtir au milieu du siècle, sur les terres héritées en 1834 de son père Honoré, la maison de plantation Arlington, de style néo-grec, sur les deux rives du bayou Teche.",
  "2e époque, ch. 3, « Les gens de couleur libres »", "Point à la maison Arlington (Franklin, paroisse de Sainte-Marie), approximatif ; inscrite au Registre national des lieux historiques en 1982.")
fiches = C.fiches
