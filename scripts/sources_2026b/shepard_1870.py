# Elihu H. Shepard, The Early History of St. Louis and Missouri, from its First Exploration by White Men in 1673 to 1843
# (Saint-Louis, 1870), PDF du Drive de l'auteur (texte lu par l'outil du Drive jusque vers 1838 ; le reste à découper).
# Corpus « Recherches », préfixe SH70. Le reste recoupe Billon et Houck.
from commun import Corpus
SH = "Shepard, Elihu H. (1870), The Early History of St. Louis and Missouri, from its First Exploration by White Men in 1673 to 1843, Saint-Louis, Southwestern Book and Publishing Co."
C = Corpus('Recherches', 'SH70', SH, page_fmt='p. {} (éd. 1870)')
F = C.F
F('01', "Saint-Louis, près de l'étang Chouteau : un Duchouquette tué par des Delawares (Loups), vengé par son frère François (vers 1790)", 'evenement', '1788~/1793~', -90.2075, 38.6265, 'a', ['François Duchouquette', 'Tayon', 'Louis Lorimier'],
  "Shepard rapporte qu'un membre de la famille Duchouquette, surpris seul près de l'étang Chouteau par un petit groupe de Delawares (les Loups des Français), fut tué et scalpé. Son frère François, témoin de loin, donna l'alarme ; l'officier Tayon partit aussitôt à leur poursuite avec une troupe. François abattit celui qui portait la chevelure de son frère, et quatre autres furent tués. Selon Shepard, les Delawares et les Shawnees, installés par les Espagnols près du cap Girardeau grâce à Louis Lorimier pour protéger la colonie, perdirent dès lors la confiance des habitants et abandonnèrent leurs villages.",
  '31-32', "Date non donnée : l'épisode est placé entre l'installation des Delawares et des Shawnees près du cap Girardeau et l'administration de Manuel Perez (1788-1793).")
fiches = C.fiches
