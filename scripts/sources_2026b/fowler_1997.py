# Melvin L. Fowler, The Cahokia Atlas: A Historical Atlas of Cahokia Archaeology, Studies in Illinois Archaeology n° 6,
# Springfield, Illinois Historic Preservation Agency, 1989, éd. révisée 1997 (PDF du Drive de l'auteur, dossier CAHOKIA ;
# texte lu en partie, environ 150 000 caractères). Préfixe FW97.
from commun import Corpus
FW = "Fowler, Melvin L. (1997), The Cahokia Atlas: A Historical Atlas of Cahokia Archaeology, éd. révisée, Studies in Illinois Archaeology n° 6, Springfield, Illinois Historic Preservation Agency"
C = Corpus('Recherches', 'FW97', FW, page_fmt='{}')
F = C.F
F('01', "Monticule des Moines (Cahokia) : la chapelle française et le « mont de l'Abbé »", 'religion', '1690~/1752~', -90.0623, 38.6604, 'h', [],
  "Les premiers explorateurs français, Marquette et Jolliet compris, ne signalent pas les tertres de Cahokia, à l'écart des routes du fleuve et du chemin de Cahokia à Kaskaskia. Mais des colons français élèvent plus tard une chapelle à l'angle sud-ouest du grand tertre et un poste de traite à proximité : le monticule porte pour cette raison le nom de « L'Abbé » bien avant l'arrivée des trappistes. L'étude des collections des musées a permis d'établir pour la première fois la présence d'une mission française sur le site dès la fin du XVIIe siècle.",
  "ch. 1-2 et fig. 5.12", "Dates approximatives : Fowler parle d'une mission du XVIIe siècle et d'une chapelle du XVIIIe (Walthall et Benchley 1987). Point au monticule des Moines (Monks Mound).")
F('02', "Monticule des Moines : le monastère des trappistes de Cahokia (1809-1813)", 'religion', '1809-04/1813', -90.0640, 38.6595, 'c', ['Nicolas Jarrot', 'Henry Marie Brackenridge'],
  "En avril 1809, une petite communauté de trappistes français s'établit sur quelque 400 acres cédés par le major Nicolas Jarrot, de Cahokia, dont la terre englobe le grand tertre. Ils bâtissent des cabanes de rondins sur un tertre voisin, font un potager sur la terrasse du grand monticule et sèment du blé à son sommet ; Brackenridge, qui les visite en 1811, s'offusque de leur silence. Le climat paludéen et d'autres causes font échouer l'entreprise ; selon Snyder, les survivants vendent la terre et rentrent en France. Le grand tertre garde depuis le nom de monticule des Moines, et les archéologues ont appelé « Trappist » la couche d'occupation la plus récente du site.",
  "ch. 2", "Snyder (1917), cité par Fowler, date la vente de mars 1819 ; la plupart des historiens placent le départ des trappistes vers 1813. Point au tertre voisin du grand monticule.")
fiches = C.fiches
