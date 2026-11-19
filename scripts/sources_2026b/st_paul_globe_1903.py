# « Little Canada, a Desolated Lonesome Suburb of St. Paul That Begins and Ends With a Cemetery », The St. Paul Globe,
# 6 septembre 1903, p. 26 (Chronicling America, seq-27 ; PDF du Drive de l'auteur, OCR). Corpus « Recherches », préfixe SPG03.
from commun import Corpus
SG = "« Little Canada, a Desolated Lonesome Suburb of St. Paul That Begins and Ends With a Cemetery », The St. Paul Globe, 6 septembre 1903, p. 26"
C = Corpus('Recherches', 'SPG03', SG, page_fmt='p. {}')
F = C.F
LC = (-93.087, 45.025)
F('01', "Little Canada : la tombe isolée de « Mme de Rousseau », la « grande dame » née à Paris (1792-1850)", 'personnage', '1850-06-16', LC[0]+0.002, LC[1]+0.001, 'a', ['Mme de Rousseau', 'Joseph Dellonais', 'Joseph Goiffon', 'Paul Bibeau', 'Véronique Millette'],
  "Au centre du cimetière de Little Canada, sous la grande croix de bois grise, une tombe à l'écart porte encore, presque effacée, l'inscription d'une Mme de Rousseau, née à Paris en 1792 et morte le 16 juin 1850. Le vieux pêcheur Joseph Dellonais, 82 ans, la redresse en parlant d'une « gran' lady » ; le curé Goiffon ne sait rien d'elle, sinon que sa maison a brûlé et que l'homme qui se disait son mari, un traiteur, est reparti. Tout près reposent Paul Bibeau, né à Sorel la même année qu'elle et mort en 1865, sa femme Véronique Millette (1803-1866) et deux fils morts jeunes.",
  '26', "Position au cimetière de la paroisse Saint-Jean-l'Évangéliste.")
F('02', "Little Canada : le père Goiffon, amputé après le blizzard de janvier 1860, curé depuis quarante ans", 'religion', '1860-01/1903-09-06', LC[0], LC[1], 'c', ['Joseph Goiffon'],
  "Né à Lyon, missionnaire du Nord-Ouest, le père Joseph Goiffon descend chaque année de ses deux missions de la frontière vers Saint Paul en charrette de la Rivière-Rouge. En janvier 1860, un blizzard le retient cinq jours dans la prairie ; il survit en mangeant la chair de son cheval, et des colons le trouvent endormi sous la neige. On doit l'amputer des deux pieds : en 1903, à quatre-vingts ans, il marche depuis trente-trois ans sur des moignons de bois et prédit la disparition du village, d'où les jeunes s'en vont.",
  '26')
F('03', "Little Canada : la maison du capitaine Bélanger, pilote du Mississippi (mort vers 1899)", 'personnage', '1850~/1899~', LC[0]-0.002, LC[1]-0.001, 'a', ['Bélanger (capitaine)', 'Augustin Ravoux'],
  "Plus bas dans la rue du village se dresse la maison bâtie par le capitaine Bélanger, pilote réputé du Mississippi, mort vers 1899 à 84 ans. Ses petits-enfants racontent qu'il traversa un jour le fleuve à la rame dans une terrible tempête pour mener le père Ravoux auprès d'un mourant de Mendota. Son monument est l'un des plus beaux du cimetière.",
  '26')
fiches = C.fiches
