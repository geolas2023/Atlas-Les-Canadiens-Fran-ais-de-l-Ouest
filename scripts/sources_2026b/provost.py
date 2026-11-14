# Étienne Provost (v. 1785-1850) à Saint-Louis : fiches versées depuis l'Atlas Aubry (page « Le réseau francophone »,
# section « Aubry et Étienne Provost », et fiche L100), corpus « Recherches ». Dossier : provost.html.
# Le nom de personnage suit la graphie du corpus Hafen MM (« Etienne Provost ») pour que le filtre les regroupe.
from commun import Corpus
TY = "Tykal, Jack B. (1989), Etienne Provost: Man of the Mountains, Liberty (Utah), Eagle's View"
HA = "Havard, Gilles (2019), L'Amérique fantôme. Les aventuriers francophones du Nouveau Monde, Paris, Flammarion, ch. 8 « L'homme des montagnes : Étienne Provost »"
AA = "Atlas Aubry, page « Le réseau francophone », section « Aubry et Étienne Provost : ce qu'on sait » (geolas2023.github.io/Atlas-Aubry/reseau.html#provost)"
C = Corpus('Recherches', 'PV', TY)
F = C.F
P = 'Etienne Provost'
F('01', 'Saint-Louis : mort et inhumation d\'Étienne Provost', 'evenement', '1850-07-03/1850-07-04', -90.1857, 38.6243, 'c', [P, 'Marie-Rose Lambert'],
  "Retiré des montagnes, Étienne Provost meurt à Saint-Louis le 3 juillet 1850 ; il est inhumé le lendemain depuis la vieille cathédrale, dont le registre l'inscrit comme époux de « Maria Rose Lombard » (Marie-Rose Lambert). Le même 3 juillet, François-Xavier Aubry arrive à Independence au terme de son « retour éclair » de juin 1850 : aucune source ne montre que les deux hommes se soient connus.",
  '', "Point placé à la vieille cathédrale (basilique Saint-Louis-Roi-de-France), paroisse des Canadiens de Saint-Louis.",
  source=f"{TY} ; {HA} ; registre des sépultures de la vieille cathédrale de Saint-Louis, 4 juillet 1850, d'après {AA}")
F('02', 'Saint-Louis : taverne et épicerie de Provost', 'commerce', '1827~/1850', -90.1895, 38.618, 'h', [P],
  "Selon Jack B. Tykal, Étienne Provost tient à Saint-Louis, à partir de 1827 environ, une taverne et une épicerie (« grocery »), entre ses saisons dans les montagnes au service de l'American Fur Company.",
  '', "Adresse inconnue : point placé dans le Frenchtown de la rue Second, où Havard situe Provost. À préciser par l'annuaire de 1847 (p. 153).",
  source=f"{TY} ; {TY.split(' (')[0]}, « Provost, Etienne », Utah History Encyclopedia (uen.org), d'après {AA}")
F('03', 'Saint-Louis : Provost dans le Frenchtown de la rue Second', 'etablissement', '1845/1847', -90.189, 38.617, 'a', [P, 'Moïse Lamoureux'],
  "Gilles Havard situe Étienne Provost dans le quartier canadien-français au sud de la vieille cathédrale, encore appelé Frenchtown dans les années 1840 (rues Second et Third, entre Poplar et Lombard), d'après l'annuaire de 1847 et le recensement municipal de 1845. C'est le quartier de Moïse Lamoureux, natif de Chambly comme Provost (angle Second et Poplar en 1845), et des Blanchard, chez qui Aubry aurait logé en 1843.",
  '', "À vérifier : l'entrée de Provost dans le St. Louis Directory de 1847 (p. 153) et dans le recensement municipal de 1845 (Missouri Historical Society).",
  source=f"{HA}, notes 87, 130 et 138, d'après {AA}")
F('04', '244, South Second : « Henry N. Provost, mountain trader »', 'personnage', '1851', -90.1893, 38.6195, 'h', ['Henry N. Provost', P],
  "L'annuaire de 1851, publié après la mort d'Étienne, inscrit encore « Provost Henry N., mountain trader, 244 s Second ». Le « H. N. Provost » des annuaires de 1840-1841 et de 1845 (épicier à l'angle sud-ouest des rues Second et Lombard) est donc vraisemblablement un autre homme, peut-être un parent d'Étienne, lui aussi lié au commerce des montagnes.",
  '', "Position estimée sur la rue Second ; la numérotation de 1851 n'est pas repérée. Identification de Henry N. Provost ouverte (voir la fiche A-L100).",
  source=f"Green's St. Louis Directory for 1851, p. 281 (HathiTrust, hvd.hn4h22), d'après {AA}")
fiches = C.fiches
