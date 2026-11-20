# J. Lorenzo Werich, Pioneer Hunters of the Kankakee, 1920. PDF du Drive de l'auteur (pioneerhunters_Kankakee), lu en
# entier via le visualiseur. Corpus « Recherches », préfixe WE20.
from commun import Corpus
WE = "Werich, J. Lorenzo (1920), Pioneer Hunters of the Kankakee, s.l., l'auteur"
C = Corpus('Recherches', 'WE20', WE, page_fmt='p. {} (PDF)')
F = C.F
F('01', "Coude de la Saint-Joseph (South Bend) : Charlevoix recrute chez les Loups pour descendre le Kankakee (1721)", 'evenement', '1721', -86.25, 41.676, 'a', ['Pierre-François-Xavier de Charlevoix'],
  "Selon Werich, une bande de Mohicans qui se disaient « Loups », chassés de chez eux par les Iroquois, s'était réfugiée près des sources du Théakiki (Kankakee). Charlevoix, en 1721, parle de ces Loups lors de sa descente du Kankakee ; c'est dans leur village, à quelques milles du coude de la rivière Saint-Joseph, là où s'élève South Bend, qu'il recrute les hommes de son expédition vers l'Illinois et le Mississippi.",
  '20', "Source tardive et de seconde main. Point à South Bend.")
fiches = C.fiches
