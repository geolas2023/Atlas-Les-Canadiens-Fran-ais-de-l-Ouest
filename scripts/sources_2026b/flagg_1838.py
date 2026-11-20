# Edmund Flagg, The Far West: or, A Tour beyond the Mountains, New York, Harper, 1838, 2 vol. PDF archive.org du Drive de
# l'auteur (farwestortourbey00flag, 01 et 02), lus en entier via le visualiseur. Corpus « Recherches », préfixe FL38.
from commun import Corpus
FL = "Flagg, Edmund (1838), The Far West: or, A Tour beyond the Mountains, New York, Harper & Brothers, 2 vol."
C = Corpus('Recherches', 'FL38', FL, page_fmt='{} (PDF)')
F = C.F
F('01', "La Charbonnière : le banc de charbon du Missouri en amont de Florissant (vers 1836)", 'lieu', '1836~', -90.33, 38.86, 'h', [],
  "Sur la route de Saint-Charles, Flagg signale sur la rive droite du Missouri, un peu en amont de Florissant, « La Charbonnière », nom donné par les Français à un banc de charbon célèbre. Il affleure dans une falaise d'environ deux cents pieds de haut et deux fois plus longue ; la couche, d'une douzaine de pieds d'épaisseur, repose au bord même de l'eau et contient beaucoup de bitume. On y a aussi trouvé du minerai de fer.",
  "vol. 1, p. 257", "Point approximatif sur la rive du Missouri au nord de Florissant.")
F('02', "Rivière Meramec : la mine d'argent du sieur de Lochon et de l'Espagnol Antonio (1719-1720)", 'evenement', '1719/1720', -90.75, 38.25, 'h', ['de Lochon', 'Antonio', 'Pierre-François-Xavier de Charlevoix'],
  "Flagg reproduit le passage de Charlevoix sur la recherche d'une mine d'argent sur la Meramec. En 1719, le sieur de Lochon, envoyé comme fondeur par la Compagnie des Indes, creuse à l'endroit indiqué et tire beaucoup de minerai : une livre, fondue pendant quatre jours, aurait donné deux drachmes d'argent, mais on le soupçonne de l'avoir ajouté lui-même. La Compagnie le remplace par un Espagnol nommé Antonio, pris au siège de Pensacola, ancien galérien qui se vantait d'avoir travaillé dans une mine du Mexique. Antonio, malgré de très gros appointements, ne réussit pas mieux.",
  "vol. 1, p. 267-268", "Charlevoix situe la fouille sur la Meramec sans plus de précision ; point hypothétique sur le cours moyen de la rivière.")
F('03', "Kaskaskia : la cloche de 1741 « Pour l'église des Illinois » (vers 1836)", 'religion', '1741/1836~', -89.915, 37.92, 'a', ['Normand', 'A. Parachelle'],
  "Flagg monte au beffroi de la vieille église de Kaskaskia, si branlant qu'il oscille sous son poids et avec la cloche. Celle-ci, ornée d'un crucifix, porte l'inscription « Pour l'église des Illinois. Normand A. Parachelle, 1741 ». Du clocher, la vue embrasse le village et ses fermes dispersées sur des milles. Il ajoute en note que, depuis sa visite, tout l'angle sud-ouest de l'église s'est écroulé.",
  "vol. 2, p. 183", "L'inscription est donnée telle que la transcrit Flagg (« Leglise »). Point à l'ancien Kaskaskia.")
F('04', "Fort de Chartres : la première cour britannique et ses juges de paix français, Barbeau et Girardot (6 novembre 1768)", 'evenement', '1768-11-06', -90.157, 38.084, 'c', ['Jean-Baptiste Barbeau', 'Pierre Girardot', 'John Wilkins', 'George Morgan'],
  "En appendice, Flagg publie le procès-verbal de la cour tenue au « Chartres Village » le 6 novembre 1768. Parmi les juges de paix nommés par le gouverneur et commandant John Wilkins figurent, aux côtés de George Morgan, James Rumsey, James Campbell et James McMillan, deux habitants français, Jean-Baptiste Barbeau et Pierre Girardot. Tous prêtent le serment d'allégeance au roi George III et celui de juge de paix.",
  "vol. 2, p. 247", "")
F('05', "Kaskaskia : la maison de Jean-Baptiste Hubardeau saisie et vendue « payable en pelleterie » (décembre 1772)", 'evenement', '1772-12-19/1773-01-29', -89.915, 37.92, 'c', ['Jean-Baptiste Hubardeau', 'Andrew Hoy', 'Hugh Lord'],
  "Sous le capitaine Hugh Lord, du 18e régiment royal irlandais, le gouvernement de l'Illinois est purement militaire. Le 19 décembre 1772, le prévôt Andrew Hoy saisit la maison et le terrain de Jean-Baptiste Hubardeau, à Kaskaskia, pour une dette de 2 040 livres. L'avis de vente, affiché en français à Kaskaskia et à Cahokia, annonce la vente à la porte de l'église, « payable en pelletrie, bon argent, lettres de change, ou la bon esclaves », au mois de mai suivant. Flagg en donne le texte et la traduction.",
  "vol. 2, p. 248-249", "Point à l'ancien Kaskaskia.")
fiches = C.fiches
