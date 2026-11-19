# Henry Marie Brackenridge, Journal of a Voyage up the River Missouri, performed in 1811 (2e éd., Baltimore, 1816),
# rééd. Thwaites, Early Western Travels, vol. 6 (1904), PDF du Drive de l'auteur. Corpus « Recherches », préfixe BK16.
from commun import Corpus
BK = "Brackenridge, H. M. (1816), Journal of a Voyage up the River Missouri, performed in Eighteen Hundred and Eleven, 2e éd., Baltimore (rééd. Thwaites, Early Western Travels, vol. 6, 1904)"
C = Corpus('Recherches', 'BK16', BK, page_fmt='p. {} (PDF)')
F = C.F
F('01', "Saint-Charles : départ de la barge de Manuel Lisa, avec Toussaint Charbonneau et son épouse shoshone (2 avril 1811)", 'exploration', '1811-04-02', -90.4840, 38.7881, 'c', ['Manuel Lisa', 'Toussaint Charbonneau', 'Sacagawea', 'Henry Marie Brackenridge'],
  "Le 2 avril 1811, la barge de la Missouri Fur Company quitte Saint-Charles sous le commandement de Manuel Lisa, chargé de retrouver Andrew Henry et de suivre la troupe de Wilson P. Hunt. Elle porte vingt rameurs, un pierrier à la proue et des marchandises cachées dans une fausse cabine, par crainte des bandes sioux. À bord voyagent Toussaint Charbonneau et sa femme shoshone (Sacagawea), qui avaient accompagné Lewis et Clark. Brackenridge admire l'endurance des Canadiens et des Créoles de l'équipage, qui sautent dans l'eau glacée sans hésiter.",
  '17-19')
F('02', "Pointe Labadie : relâche nommée d'après un traiteur français qui y avait hiverné (1811)", 'toponymie', '1811-04', -90.8400, 38.5560, 'a', ['Labadie'],
  "Brackenridge passe la pointe Labadie, ainsi nommée d'après un traiteur français qui y avait jadis hiverné. Quarante ans plus tôt, c'était un point éloigné sur le Missouri ; en 1811, des plantations couvrent toute la vallée. Plus haut, la crique de la Femme Osage abrite l'établissement de Daniel Boone, sur une terre concédée en 1795 par le gouverneur espagnol Trudeau.",
  '22-23', "Position du village actuel de Labadie (Missouri).")
F('03', "La Charette : une trentaine de familles qui chassent et sèment un peu de maïs (avril 1811)", 'etablissement', '1811-04-08', -91.0600, 38.6200, 'a', [],
  "Le 8 avril 1811, la barge de Lisa passe en vue du petit village de La Charette, sur la rive nord-est du Missouri : une trentaine de familles y vivent de la chasse et d'un peu de maïs. Plus haut viennent l'île aux Bœufs et l'auberge de Montbrun, lieu de repos des voyageurs.",
  '24, 29', "Position approximative, près de l'actuel Marthasville.")
F('04', "Côte sans Dessein : treize familles françaises et quelques familles indiennes (1811)", 'etablissement', '1808~/1811-04-12', -91.9500, 38.6200, 'c', ['Toussaint Charbonneau', 'Manuel Lisa', 'Castor'],
  "Arrivé à pied avec l'interprète Charbonneau, Brackenridge décrit la Côte sans Dessein, sur la rive nord-est en vue de l'embouchure de l'Osage. Le nom vient d'une butte calcaire isolée au bord de l'eau. Fondé trois ans plus tôt, le village compte treize familles françaises et deux ou trois familles indiennes, qui cultivent la prairie mais passent surtout leur temps à chasser. Lisa y engage un chasseur réputé nommé Castor, un Kansa qui parlait bien le français.",
  '30-31')
F('05', "Village des Omahas : Charbonneau part à cheval rejoindre Hunt chez les Poncas (mai 1811)", 'exploration', '1811-05', -96.4900, 42.3200, 'a', ['Toussaint Charbonneau', 'Manuel Lisa', 'Wilson Price Hunt', 'Big Elk (Omaha)'],
  "Pressé de rejoindre Hunt avant le pays sioux, Lisa envoie par terre un messager métis accompagné de Charbonneau vers le village des Poncas, à trois jours de cheval. La barge repart sans saluer Big Elk, chef du village omaha. Cet oubli d'étiquette offense toujours, aussi lui laisse-t-on un présent et un message.",
  '70', "Position approximative du village omaha de l'époque.")
F('06', "Haut-Missouri : rencontre de François-Marie Benoist, traiteur né au Canada, descendant des Mandans (1811)", 'commerce', '1811-05', -96.9, 42.75, 'h', ['François-Marie Benoist', 'Manuel Lisa'],
  "La barge croise un petit bateau chargé de pelleteries, avec cinq hommes, qui descend du village mandan. D'après l'éditeur, c'est probablement François-Marie Benoist, traiteur de Saint-Louis né au Canada en 1768, arrivé en 1790, qui avait tenu un poste chez les Otos et les Pawnees. Le voyageur rapporte qu'à part les Mandans, les Arikaras et une ou deux petites tribus, toutes les nations du Missouri sont hostiles aux Blancs.",
  '74', "Lieu de la rencontre non précisé dans l'extrait : point placé entre le pays omaha et celui des Poncas.")
fiches = C.fiches
