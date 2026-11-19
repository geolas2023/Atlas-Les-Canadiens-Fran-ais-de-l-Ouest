# Récits français sur les Lakotas, pack « Histoire des États-Unis » du Drive de l'auteur :
# Drury et Clavin, Sur la terre des Sioux (Albin Michel, 2015 ; The Heart of Everything That Is, 2013), préfixe DC13 ;
# Ameur, Sitting Bull (Larousse, coll. « L'histoire comme un roman »), même module.
from commun import Corpus
DC = "Drury, Bob et Tom Clavin (2015), Sur la terre des Sioux : l'histoire inédite de Red Cloud, trad. de The Heart of Everything That Is (2013), Paris, Albin Michel"
AM = "Ameur, Farid, Sitting Bull, Paris, Larousse (epub du Drive de l'auteur)"
C = Corpus('Recherches', 'DC13', DC, page_fmt='{}')
F = C.F
F('01', "Belle Fourche (Wyoming) : Sam Deon, traiteur montréalais, au camp d'hiver de Red Cloud (hiver 1862-1863)", 'personnage', '1862-12~/1863-02~', -104.70, 44.55, 'a', ['Peter Abraham « Sam » Deon', 'Red Cloud', 'Bega (Mary Highwolf)'],
  "Petit, sec et parlant plusieurs dialectes sioux, Peter Abraham « Sam » Deon a quitté Montréal une quinzaine d'années plus tôt. Arrivé à Saint-Louis par Boston et La Nouvelle-Orléans, il devient agent de l'American Fur Company et parcourt les postes du haut Missouri. Il épouse Bega, tante maternelle de Red Cloud, plus tard appelée Mary Highwolf. Après la guerre des Dakotas du Minnesota (1862), il part de Fort Laramie avec quatre chariots et quelque 4 500 kg de marchandises vers le camp d'hiver de Red Cloud, sur la Belle Fourche. Selon Drury et Clavin, le vieux chef lui racontera plus tard sa vie au coin du feu.",
  'chap. 3-4', "Point placé sur la Belle Fourche, dans le nord-est du Wyoming ; emplacement du camp non précisé.")
F('02', "Little Bighorn : Frédéric Girard, interprète de Custer au Crow's Nest (25 juin 1876)", 'evenement', '1876-06-25', -107.3300, 45.5300, 'a', ['Frédéric Girard (Gerard)', 'George A. Custer', 'Bloody Knife', 'Mitch Bouyer'],
  "Dans le récit de Farid Ameur, Frédéric Girard, négociant de longue date au Dakota, accompagne la colonne de Custer comme interprète des éclaireurs arikaras. Le matin du 25 juin 1876, il traduit pour Custer l'avertissement de Bloody Knife, selon qui il y aurait assez de Sioux pour les occuper deux ou trois jours ; Custer répond que ce sera l'affaire d'une journée. Michel (« Mitch ») Bouyer, fils d'un trappeur français et d'une Sioux, est l'un des éclaireurs de la colonne.",
  'chap. sur la marche vers la Little Bighorn', "Point placé au Crow's Nest, dans les monts Wolf.", source=AM)
fiches = C.fiches
