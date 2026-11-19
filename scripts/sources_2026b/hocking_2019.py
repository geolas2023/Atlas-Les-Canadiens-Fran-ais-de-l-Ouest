# Doug Hocking, Terror on the Santa Fe Trail: Kit Carson and the Jicarilla Apache (2019), PDF du Drive de l'auteur
# (dossier SANTA_FE_TRAIL). Corpus « Recherches », préfixe HK19 : rôle des guides francophones dans la guerre jicarilla de 1849.
# Le roman du même auteur (Massacre at Point of Rocks, 2013) est traité dans l'onglet Littérature de l'Atlas Aubry, pas ici.
from commun import Corpus
HK = "Hocking, Doug (2019), Terror on the Santa Fe Trail: Kit Carson and the Jicarilla Apache, Guilford (Conn.), TwoDot"
C = Corpus('Recherches', 'HK19', HK, page_fmt='{}')
F = C.F
LX = 'Antoine Leroux'
F('01', "Cerro de la Olla : Leroux et Autobees guident les dragons contre les Utes (printemps 1849)", 'evenement', '1849-03~', -105.73, 36.73, 'a', [LX, 'Charles Autobees', 'Bill Williams', 'Asa Estes'],
  "Au printemps 1849, le lieutenant Joseph H. Whittlesey part de Taos avec une soixantaine de dragons pour « châtier » les Utes. Ses guides sont Antoine Leroux, Charles Autobees, le vieux Bill Williams et Asa Estes ; ils trouvent le village ute sur le Cerro de la Olla, à une quinzaine de milles au nord de Río Colorado, de l'autre côté du canyon du Rio Grande, et le surprennent. Hocking pense que des Jicarillas s'y trouvaient aussi.",
  'ch. 7', "Position au Cerro de la Olla (Rio Grande del Norte, Nouveau-Mexique).")
F('02', "Breaks de la Canadian, près de Tucumcari : Leroux contre Carson (16-17 novembre 1849)", 'evenement', '1849-11-16/1849-11-17', -103.73, 35.18, 'h', [LX, 'Kit Carson', 'Robert Fisher', 'William Grier', 'Ann White'],
  "Pour retrouver Ann White, enlevée au massacre de Point of Rocks, le major Grier engage Antoine Leroux comme chef éclaireur et Robert Fisher comme guide ; Kit Carson, venu de Rayado, est placé sous les ordres de Leroux. Après plus de deux semaines sur la piste, Carson repère le camp jicarilla au débouché des Breaks de la Canadian, près de Tucumcari Butte, et propose une charge immédiate. Leroux conseille de s'arrêter pour parlementer ; Grier l'écoute. Les Jicarillas s'enfuient, Ann White est tuée en courant vers les soldats. Carson dira plus tard que, si l'on avait chargé, on l'aurait peut-être sauvée, sans blâmer ouvertement « l'autre guide ».",
  'ch. 8', "Position hypothétique du camp au sud des Breaks de la Canadian, près de Tucumcari Butte.")
F('03', "Fort Barclay : retour de Grier, Carson et « Watkin LaRoux » après le blizzard (25 novembre 1849)", 'evenement', '1849-11-25', -104.98, 35.79, 'a', ['Joaquin Leroux', LX, 'Kit Carson', 'Alexander Barclay'],
  "Au retour de l'expédition, une tempête de neige d'une violence inouïe tue un soldat et cause la mort de nombreux Jicarillas. Le journal d'Alexander Barclay note le 25 novembre 1849 l'arrivée de Grier, de Kit Carson et de « Watkin LaRoux » (Joaquin Leroux, fils d'Antoine), venus de Las Vegas.",
  'ch. 8', "Position au fort Barclay, à La Junta de los Ríos (Watrous).")
fiches = C.fiches
