# Caroline B. Brettell, Following Father Chiniquy: Immigration, Religious Schism, and Social Change in
# Nineteenth-Century Illinois (Carbondale, Southern Illinois University Press, 2015), epub du Drive de l'auteur
# (dossier CHINIQUY). Corpus « Recherches », préfixe BR15.
from commun import Corpus
BR = "Brettell, Caroline B. (2015), Following Father Chiniquy: Immigration, Religious Schism, and Social Change in Nineteenth-Century Illinois, Carbondale, Southern Illinois University Press"
C = Corpus('Recherches', 'BR15', BR, page_fmt='{}')
F = C.F
SA = (-87.714, 41.025)
F('01', "Sainte-Anne (Illinois) : l'église catholique du père Letellier rebâtie face aux presbytériens de Chiniquy (1871-1885)", 'religion', '1871-10/1885-06-18', SA[0]+0.003, SA[1]+0.002, 'c', ['Michel Letellier', 'Ambroise Allain', 'Antoine Allain', 'Charles Chiniquy'],
  "Après le schisme, les catholiques de Sainte-Anne doivent aller prier à Sainte-Marie (Beaverville), à dix milles. En 1871, le père Michel Letellier est envoyé reconquérir la paroisse : l'église est achevée en 1872 au point le plus haut du village, sur une terre des frères Ambroise et Antoine Allain, établis avant l'arrivée de Chiniquy. La souscription de 4 500 $ tourne mal et une dette de 7 000 $ subsiste dix ans plus tard ; Letellier note avec soin les noms des schismatiques revenus au catholicisme. En 1872-1873, la Première Église presbytérienne de Chiniquy compte pourtant 150 familles et 210 communiants. Le 18 juin 1885, la Kankakee Gazette dénombre 23 attelages devant l'église catholique contre 16 et 9 devant les deux églises presbytériennes.",
  "ch. 6", "Position approximative de l'église Sainte-Anne.")
F('02', "Sainte-Anne (Illinois) : relique de sainte Anne et pèlerinage des Canadiens du Midwest (1880-1939)", 'religion', '1881~/1939', SA[0]+0.0035, SA[1]+0.0015, 'c', ['Bourassa (abbé)', 'Matilda Cunnea', 'Lucille Walsh', 'E. L. Rivard'],
  "Calquée sur Sainte-Anne-de-Beaupré, une neuvaine attire chaque juillet les Canadiens français du Midwest ; en 1889, un train spécial de dix voitures amène de Chicago un millier de pèlerins, logés à l'académie Sainte-Anne ouverte en 1883 par les sœurs de Notre-Dame. Après la foudre de 1893, l'église est rebâtie et reçoit en 1894, à la demande de l'abbé Bourassa de Pullman, une relique (un os de la main) envoyée de Rome par le cardinal de Québec. Le 24 juillet 1904, Matilda Cunnea, paralysée depuis deux ans, se lève de son fauteuil, conservé depuis dans une chapelle latérale ; d'autres guérisons suivent jusqu'en 1912. En 1906, on compte 5 500 pèlerins. Le Viatorien E. L. Rivard y voit une réparation du schisme de Chiniquy.",
  "ch. 6", "La 105e neuvaine est célébrée en 1985.")
F('03', "Concordia (Kansas) : Mme Moïse Mercier, pèlerine guérie à Sainte-Anne (Illinois) (1910)", 'religion', '1910-07', -97.662, 39.571, 'a', ['Moïse Mercier (Mme)', 'Clément Lavoie (Mme)'],
  "Lors du pèlerinage de 1910, qui réunit deux mille personnes, Mme Moïse Mercier, de Concordia (Kansas), recouvre l'ouïe et Mme Clément Lavoie, de Sainte-Anne, jette ses béquilles : deux femmes d'ascendance canadienne-française, signe que la dévotion rayonnait jusqu'aux colonies canadiennes du Kansas.",
  "ch. 6", "Position à Concordia, foyer canadien-français du comté de Cloud.")
fiches = C.fiches
