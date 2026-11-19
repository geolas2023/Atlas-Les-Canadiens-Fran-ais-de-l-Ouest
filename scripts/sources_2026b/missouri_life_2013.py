# Jim Winnerman, « Preserving Missouri's Old Mines French Dialect », Missouri Life, février 2013, p. 38-41
# (PDF du Drive de l'auteur, ML-2014-ctgy5-ArtCulFeat.pdf). Préfixe ML13.
from commun import Corpus
ML = "Winnerman, Jim (2013), « Preserving Missouri's Old Mines French Dialect », Missouri Life, février 2013"
C = Corpus('Recherches', 'ML13', ML, page_fmt='p. {}')
F = C.F
F('01', "Old Mines : le français du Missouri au bord de l'extinction (2013)", 'evenement', '1930/2013-02', -90.8457, 38.0103, 'c', ['Kent Bone', 'Natalie Villmer', 'Dennis Stroughmatt'],
  "Vers 1930, le français du Missouri est encore la langue maternelle d'environ un millier de personnes autour de la Vieille Mine, dans une zone de 150 milles qui englobe De Soto, Festus, Bonne Terre et Richwoods ; en 2013, moins de dix le parlent couramment. Isolement des villages, terres en longues bandes le long du ruisseau, messe en français à Saint-Joachim et travail manuel dans les mines de plomb puis de « tiff » (barytine) l'ont préservé ; l'école obligatoire, l'anglais imposé par les religieuses vers 1920, la mécanisation et les routes l'ont condamné. Kent Bone, Natalie Villmer, qui chante les complaintes apprises de son père, et le violoneux Dennis Stroughmatt entretiennent la mémoire de cette langue, plus proche du canadien par l'accent et du louisianais par le vocabulaire.",
  '38-41', "Point au village d'Old Mines.")
fiches = C.fiches
