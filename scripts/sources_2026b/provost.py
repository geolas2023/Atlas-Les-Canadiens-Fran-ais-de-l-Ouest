# Étienne Provost (v. 1785-1850) à Saint-Louis, corpus « Recherches ». Dossier : provost.html.
# Enquête faite d'abord pour l'Atlas Aubry (section « Aubry et Étienne Provost » et fiche L100), retirée de cet atlas
# le 14 novembre 2026 (Aubry et Provost ne se connaissaient pas) et versée ici en entier.
# Le nom de personnage suit la graphie du corpus Hafen MM (« Etienne Provost ») pour que le filtre les regroupe.
from commun import Corpus
TY = "Tykal, Jack B. (1989), Etienne Provost: Man of the Mountains, Liberty (Utah), Eagle's View"
HA = "Havard, Gilles (2019), L'Amérique fantôme. Les aventuriers francophones du Nouveau Monde, Paris, Flammarion, ch. 8 « L'homme des montagnes : Étienne Provost »"
AA = "enquête d'O. J. Caron pour l'Atlas Aubry (2026), versée dans cet atlas"
C = Corpus('Recherches', 'PV', TY)
F = C.F
P = 'Etienne Provost'
F('01', 'Saint-Louis : mort et inhumation d\'Étienne Provost', 'evenement', '1850-07-03/1850-07-04', -90.1857, 38.6243, 'c', [P, 'Marie-Rose Lambert'],
  "Retiré des montagnes, Étienne Provost meurt à Saint-Louis le 3 juillet 1850 ; il est inhumé le lendemain depuis la vieille cathédrale, dont le registre l'inscrit comme époux de « Maria Rose Lombard » (Marie-Rose Lambert).",
  '', "Point placé à la vieille cathédrale (basilique Saint-Louis-Roi-de-France), paroisse des Canadiens de Saint-Louis.",
  source=f"{TY} ; {HA} ; registre des sépultures de la vieille cathédrale de Saint-Louis, 4 juillet 1850, d'après {AA}")
F('02', 'Saint-Louis : taverne et épicerie de Provost', 'commerce', '1827~/1850', -90.1895, 38.618, 'h', [P],
  "Selon Jack B. Tykal, Étienne Provost tient à Saint-Louis, à partir de 1827 environ, une taverne et une épicerie (« grocery »), entre ses saisons dans les montagnes au service de l'American Fur Company.",
  '', "Adresse inconnue : point placé dans le Frenchtown de la rue Second, où Havard situe Provost. À préciser par l'annuaire de 1847 (p. 153).",
  source=f"{TY} ; {TY.split(' (')[0]}, « Provost, Etienne », Utah History Encyclopedia (uen.org), d'après {AA}")
F('03', 'Saint-Louis : Provost dans le Frenchtown de la rue Second', 'etablissement', '1845/1847', -90.189, 38.617, 'a', [P, 'Moïse Lamoureux'],
  "Gilles Havard situe Étienne Provost dans le quartier canadien-français au sud de la vieille cathédrale, encore appelé Frenchtown dans les années 1840 (rues Second et Third, entre Poplar et Lombard), d'après l'annuaire de 1847 et le recensement municipal de 1845. C'est aussi le quartier de Moïse Lamoureux, natif de Chambly comme Provost (angle nord-ouest des rues Second et Poplar en 1845).",
  '', "À vérifier : l'entrée de Provost dans le St. Louis Directory de 1847 (p. 153) et dans le recensement municipal de 1845 (Missouri Historical Society).",
  source=f"{HA}, notes 87, 130 et 138, d'après {AA}")
F('04', '244, South Second : « Henry N. Provost, mountain trader »', 'personnage', '1851', -90.1893, 38.6195, 'h', ['Henry N. Provost', P],
  "L'annuaire de 1851, publié après la mort d'Étienne, inscrit encore « Provost Henry N., mountain trader, 244 s Second ». Le « H. N. Provost » des annuaires de 1840-1841 et de 1845 (épicier à l'angle sud-ouest des rues Second et Lombard) est donc vraisemblablement un autre homme, peut-être un parent d'Étienne, lui aussi lié au commerce des montagnes.",
  '', "Position estimée sur la rue Second ; la numérotation de 1851 n'est pas repérée. Identification de Henry N. Provost ouverte (voir la fiche PV-05).",
  source=f"Green's St. Louis Directory for 1851, p. 281 (HathiTrust, hvd.hn4h22), d'après {AA}")
F('05', 'Saint-Louis : angle des rues Second et Lombard, les Provost et les Lambert', 'etablissement', '1840/1845', -90.189, 38.6157, 'a', ['Henry N. Provost', 'Clément Lambert', P],
  "Deux annuaires placent un Provost à ce carrefour du Frenchtown : « Provost, H. N., grocery, c Second and Lumber » (1840-1841, « Lumber » étant sans doute une coquille pour Lombard), puis « Provost HN, sw corner Second and Lombard » (Green, 1845, p. 144). À l'angle opposé, la même année : « Lambert Clement, coffee-house, ne corner Second and Lombard » (p. 103). Or Étienne Provost avait épousé Marie-Rose Lambert, et Tykal écrit qu'il tint taverne et épicerie à Saint-Louis à partir de 1827 environ. Mais l'annuaire de 1851, publié après la mort d'Étienne, inscrit encore « Provost Henry N., mountain trader » : le « H. N. Provost » du carrefour est donc vraisemblablement un autre homme, peut-être un parent. Le carrefour était hors de la zone rasée en 1939-1942 pour le parc de la Gateway Arch ; le studio Sievers a photographié en 1952 les nos 914-916 South Second, juste au sud de l'angle.",
  '', "Position estimée à quatre rues au sud de l'angle Second et Poplar ; les annuaires donnent l'angle, pas de coordonnées. Contenu de l'ancienne fiche L100 de l'Atlas Aubry.",
  source=f"The St. Louis Directory for the Years 1840-1 (St. Louis City Directories 1821-1877, Washington University Libraries) ; Green's St. Louis Directory for 1845, p. 103 et 144 (HathiTrust, hvd.hn4h26) ; Green's St. Louis Directory for 1851, p. 281 (HathiTrust, hvd.hn4h22) ; {TY} ; {HA}, notes 87, 130 et 138 ; Missouri Historical Society, studio Sievers, « Wagner's Cafe at 914 South Second Street and Wagner's Buffet at 916 South Second Street », 27 juin 1952, P0403-52375")
fiches = C.fiches
