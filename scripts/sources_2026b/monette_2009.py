# Pierre Monette, St. John de Crèvecœur et les Lettres d'un fermier américain (Québec, Presses de l'Université Laval, 2009) ;
# epub/PDF fourni par l'auteur de l'atlas le 19 novembre 2026. Corpus « Recherches », préfixe MON09. Résumés rédigés par l'atlas.
# L'étude porte surtout sur le séjour de Crèvecœur en Nouvelle-France (lac Champlain, Québec, 1757-1759), hors du champ de l'atlas de l'Ouest ;
# on ne retient que ses liens avec la vallée de l'Ohio et du Mississippi.
from commun import Corpus
SRC = "Monette, Pierre (2009), St. John de Crèvecœur et les Lettres d'un fermier américain, Québec, Presses de l'Université Laval"
C = Corpus('Recherches', 'MON09', SRC, page_fmt='p. {}')
F = C.F
F('01', "Vallée de l'Ohio : séjour attribué à Michel-Guillaume Saint-Jean de Crèvecœur (1767)", 'exploration', '1767', -80.0, 40.44, 'h', ['Michel-Guillaume Saint-Jean de Crèvecœur'],
  "Dans sa chronologie, Monette retient qu'après avoir servi comme officier et cartographe dans les troupes de la Nouvelle-France (il dresse un plan du fort William-Henry en 1757), Crèvecœur aurait séjourné en 1767 dans la vallée de l'Ohio, la même année qu'un voyage possible en Jamaïque et aux Bermudes. Ses Lettres d'un fermier américain (1782) évoquent l'Ohio, la Monongahela et la Redstone Creek comme terres d'établissement.",
  None, "Point hypothétique au confluent de l'Ohio (Pittsburgh) : le séjour n'est pas localisé.")
F('02', "Du delta du Mississippi au Canada : le voyage de dessinateur que la rumeur prête à Crèvecœur", 'exploration', '1755/1767', -90.06, 29.96, 'h', ['Michel-Guillaume Saint-Jean de Crèvecœur', 'Peter Dubois'],
  "Un rapport de l'assistant juge de paix Peter Dubois, enquêtant sur Crèvecœur pendant la Révolution, rapporte qu'on le disait venu une première fois en Amérique comme dessinateur d'un noble français, sur un trajet intérieur de l'embouchure du Mississippi jusqu'au Canada ; Crèvecœur lui-même laissait entendre avoir remonté le fleuve. Monette traite ce récit avec prudence, le séjour documenté étant celui du lac Champlain et de Québec.",
  None, "Point symbolique à l'embouchure du Mississippi ; itinéraire non attesté.")
fiches = C.fiches
