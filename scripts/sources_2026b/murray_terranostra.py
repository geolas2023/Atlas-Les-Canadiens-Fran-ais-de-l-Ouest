# Jeffrey S. Murray, Terra Nostra 1550-1950 : les cartes du Canada et leurs secrets (Sillery, Septentrion / Bibliothèque et Archives Canada) ;
# PDF fourni par l'auteur de l'atlas le 19 novembre 2026. Corpus « Recherches », préfixe TNM. Résumés rédigés par l'atlas.
from commun import Corpus
SRC = "Murray, Jeffrey S., Terra Nostra 1550-1950 : les cartes du Canada et leurs secrets, Sillery, Septentrion"
C = Corpus('Recherches', 'TNM', SRC, page_fmt='p. {}')
F = C.F
F('01', "Prairies : les cartes de La Vérendrye et la « mer de l'Ouest » chez Bellin (1730-1743)", 'exploration', '1730/1743', -98.0, 50.0, 'h', ['Pierre Gaultier de Varennes et de La Vérendrye', 'Jacques Nicolas Bellin'],
  "Murray montre comment les cartes que La Vérendrye envoie à Québec, redessinées et transmises à Paris, nourrissent les compilations françaises : Bellin, dans sa carte d'Amérique septentrionale de 1743, est l'un des premiers à les utiliser. Bien que deux fils de La Vérendrye aient traversé les Prairies en 1743 assez près des Rocheuses pour les voir, la croyance en un océan intérieur persiste, et les cartographes le relèguent derrière les montagnes.",
  30, "Point symbolique au centre des Prairies parcourues par les La Vérendrye.")
F('02', "Côte nord-ouest : la « mer de l'Ouest » de De L'Isle et Buache reliée au détroit de Juan de Fuca (1752)", 'exploration', '1752', -124.0, 48.3, 'h', ['Joseph-Nicolas De L\'Isle', 'Philippe Buache'],
  "Sur leur carte de 1752, De L'Isle et Buache font communiquer la mer de l'Ouest avec le Pacifique par le détroit de Juan de Fuca, en se fiant au récit inventé de l'amiral de Fonte ; ils placent pourtant mieux le lac des Bois et relient correctement l'Asie et l'Amérique. Après 1763, la carte pique la curiosité britannique et inspire les recherches de Hearne et de Vancouver.",
  31, "Point à l'entrée du détroit de Juan de Fuca, débouché supposé de la mer de l'Ouest.")
F('03', "Rocheuses : Édouard-Gaston Deville, arpenteur général, et la phototopographie (1885-1890)", 'exploration', '1885/1895', -115.57, 51.18, 'a', ['Édouard-Gaston Deville', 'J. J. McArthur'],
  "Né en France, Deville dirige l'arpentage des Prairies à partir de 1881 (119 équipes en 1883) et devient arpenteur général du Canada en 1885. Inspiré de la métrophotographie d'Aimé Laussedat, il fait lever les Rocheuses par photographie sur plaques de verre ; la carte de McArthur en vingt et une feuilles (début des années 1890) est la première description topographique détaillée de la chaîne.",
  153, "Point à Banff, au cœur de la zone des premiers levés phototopographiques le long du Canadien Pacifique.")
fiches = C.fiches
