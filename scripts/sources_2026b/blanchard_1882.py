# Rufus Blanchard, History of Du Page County, Illinois, Chicago, O. L. Baskin & Co., 1882 (PDF du Drive de l'auteur, dossier
# DU_PAGE_ILLINOIS_HISTORY ; texte lu en partie, 124 000 caractères). Préfixe BL82.
from commun import Corpus
BL = "Blanchard, Rufus (1882), History of Du Page County, Illinois, Chicago, O. L. Baskin & Co."
C = Corpus('Recherches', 'BL82', BL, page_fmt='PDF p. {}')
F = C.F
F('01', "Rivière Du Page : le poste du vieux traiteur français Du Page (avant 1800)", 'toponymie', '1790~/1800', -88.21, 41.43, 'h', ['Du Page', 'Jean-Baptiste Beaubien', 'Gurdon S. Hubbard'],
  "La rivière, puis le comté de Du Page tiennent leur nom d'un traiteur français établi sur ses bords, en aval de la fourche, avant 1800. Jean-Baptiste Beaubien, de Chicago, parlait souvent du « vieux Français Du Page » dont le poste se trouvait vers l'embouchure, et précisait qu'on prononçait « Du Pâje ». Gurdon Hubbard, arrivé en 1818, rapporte que le nom était déjà connu de tous, mais que le traiteur vivait là avant son temps.",
  '14', "Emplacement du poste inconnu ; point schématique vers le confluent de la Du Page et de la Des Plaines (Channahon).")
F('02', "Naper's Settlement : le colonel Jean-Baptiste Beaubien mène les volontaires de Chicago (guerre de Black Hawk, mai 1832)", 'evenement', '1832-05', -88.147, 41.775, 'c', ['Jean-Baptiste Beaubien', 'Robert Kinzie', 'Bernardus Lawton', 'Bourassa'],
  "Au printemps 1832, quand les Sauks de Black Hawk menacent les établissements de la Du Page, le traiteur Bernardus Lawton, de la Des Plaines, vient aux nouvelles avec trois Potéouatamis et un Métis nommé « Burrasaw » (Bourassa), puis prévient les colons avec une cinquantaine de Potéouatamis restés amis. Les habitants fuient vers le fort Dearborn. Une compagnie de Chicago sous le commandement du colonel Jean-Baptiste Beaubien, agent de l'American Fur Company, retourne inspecter la colonie de Naper, avec les cinquante Indiens de Robert Kinzie ; Blanchard en raconte, d'après Richmond et Vallette, les épisodes comiques.",
  '37-42', "Point à Naperville (Illinois).")
fiches = C.fiches
