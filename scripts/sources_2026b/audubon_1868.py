# Jean-Jacques Audubon, Scènes de la nature dans les États-Unis et le Nord de l'Amérique, trad. Eugène Bazin, Paris, Sauton,
# 1868 (éd. Wikisource ; epub du Drive de l'auteur, pack « Histoire des États-Unis »). Préfixe AB68.
from commun import Corpus
AB = "Audubon, Jean-Jacques (1868), Scènes de la nature dans les États-Unis et le Nord de l'Amérique, trad. Eugène Bazin, Paris, Sauton (éd. Wikisource)"
C = Corpus('Recherches', 'AB68', AB, page_fmt='{}')
F = C.F
F('01', "Tawapatee Bottom : six semaines dans les glaces du Mississippi avec un équipage canadien (hiver 1810-1811)", 'evenement', '1810-12~/1811-01~', -89.45, 37.15, 'a', ['Jean-Jacques Audubon', 'Ferdinand Rozier'],
  "Remontant le Mississippi au-dessus du confluent de l'Ohio avec son associé, à destination de Sainte-Geneviève, Audubon est arrêté par les glaces ; son pilote, un « Français du Canada », choisit pour hiverner la grande courbe de Tawapatee Bottom. Le bateau à quille est protégé d'un abattis, la cargaison abritée sous les voiles ; l'équipage de douze à quatorze Canadiens français, excellents chasseurs, vit de chevreuil, de dindons, de ratons et de poissons pris sous la glace, tandis que des cygnes trompettes se posent chaque soir sur le fleuve gelé et que des Indiens viennent au camp. Après six semaines, le pilote réveille tout le monde au cri de « La débâcle ! au bateau ! » et sauve l'embarcation.",
  "« La débâcle des glaces » ; « Le Cygne trompette »", "Audubon ne date pas l'épisode ; ses biographes le placent à l'hiver 1810-1811, lors du voyage avec Ferdinand Rozier vers Sainte-Geneviève. Point approximatif au Tawapatee Bottom (comté de Scott, Missouri).")
fiches = C.fiches
