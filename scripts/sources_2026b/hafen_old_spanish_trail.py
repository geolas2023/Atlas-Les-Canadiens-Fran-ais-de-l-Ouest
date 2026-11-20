# LeRoy R. et Ann W. Hafen, Old Spanish Trail: Santa Fé to Los Angeles, Glendale, Arthur H. Clark, 1954 (The Far West and the
# Rockies Series, I). PDF du Drive de l'auteur (HISTOIRE_LIVRES/HAFEN_FAR_WEST), lu dans la visionneuse du Drive (395 p.) ;
# les Robidoux, Provost, Chalifoux, Laforet, Saint-Germain et Tabeau y étaient déjà couverts. Corpus « Recherches », préfixe OST54.
from commun import Corpus
OS = "Hafen, LeRoy R. et Ann W. Hafen (1954), Old Spanish Trail: Santa Fé to Los Angeles, Glendale, Arthur H. Clark"
C = Corpus('Recherches', 'OST54', OS, page_fmt='p. {}')
F = C.F
F('01', "Santa Fe : le créole Tiboux nargue Armijo, puis part en Californie avec Workman et Rowland (1841-1843)", 'evenement', '1841-08/1843', -105.938, 35.687, 'c', ['Tiboux', 'Manuel Armijo', 'William Workman', 'John Rowland', 'B. D. Wilson'],
  "À l'été 1841, alors que l'on attend l'expédition texane, le gouverneur Armijo harangue la foule contre les étrangers ; un « créole français américain des environs de Saint-Louis », joueur audacieux nommé Tiboux, lance d'une voix de stentor des remarques insultantes, et la foule manque de se jeter sur les Américains. Introuvable, Tiboux part à l'automne pour la Californie avec la compagnie Workman-Rowland, dont la liste nomme un « Tibeau ». En 1843, il quitte Los Angeles avec John Rowland et B. D. Wilson pour revenir à Santa Fe par les rivières Grand et Green, où son compagnon Doke se noie.", '204-218', "D'après les souvenirs de B. D. Wilson et la liste de la compagnie publiée en 1841.")
F('02', "Green River (Utah) : Auchambeau, pilote du radeau de Kit Carson, sauve Brewerton (3 juin 1848)", 'evenement', '1848-06-03', -110.160, 38.990, 'a', ['Auchambeau', 'Kit Carson', 'George D. Brewerton'],
  "Porteur des dépêches de Californie, Kit Carson fait construire un radeau pour franchir la Green River grossie par la crue ; le lieutenant Brewerton, qui fête ses vingt et un ans, prend Auchambeau (Archambeau) comme second, seul autorisé à monter sur le radeau pour le guider à la perche. Le courant rejette l'embarcation sur la rive de départ ; heurté par les billots, Brewerton coule et Auchambeau le rattrape par les cheveux. Le Santa Fe Republican du 28 juin 1848 annonce l'arrivée de Californie de « Mr. Ghambeau » avec Carson.", '320-334', "Point au passage de la vieille piste espagnole sur la Green.")
fiches = C.fiches
