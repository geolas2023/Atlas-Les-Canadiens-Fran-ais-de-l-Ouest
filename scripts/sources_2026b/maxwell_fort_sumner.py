# La famille Maxwell-Beaubien à Fort Sumner (1870-1881). Fiches centrées sur les descendants de Charles (Carlos)
# Beaubien ; Billy the Kid n'y figure qu'en contexte (il a son propre atlas, dépôt Atlas-Billy-the-Kid).
# Livres du dossier BILLY_THE_KID du Drive de l'auteur. Corpus « Recherches », préfixe MFS. Renvois aux pages du PDF.
from commun import Corpus
WA = "Wallis, Michael (2007), Billy the Kid: The Endless Ride, New York, W. W. Norton"
UT = "Utley, Robert M. (2015), Wanted: The Outlaw Lives of Billy the Kid and Ned Kelly, New Haven, Yale University Press"
GA = "Garrett, Pat F. (1882), The Authentic Life of Billy, the Kid, Santa Fe, New Mexican Printing and Publishing"
C = Corpus('Recherches', 'MFS', WA, page_fmt='PDF p. {}')
F = C.F
F('01', "Fort Sumner : la maison des Maxwell dans l'ancien quartier des officiers (1870-1881)", 'etablissement', '1870~/1881', -104.1930, 34.4045, 'c', ['Lucien Maxwell', 'Pete Maxwell', 'Luz Beaubien Maxwell', 'Paulita Maxwell', 'Charlie Bowdre', 'Doc Scurlock'],
  "Quand l'armée abandonne Fort Sumner, Lucien Maxwell, après la vente de la concession Beaubien-Miranda, achète les bâtiments et s'y retire avec sa femme Luz Beaubien, fille de Charles Beaubien. À sa mort en 1875, leur fils aîné Pete (Pedro) reprend le ranch, dont le siège est l'ancien poste ; la famille habite l'ancien quartier des officiers. Pete Maxwell emploie des vachers, dont Charlie Bowdre et Doc Scurlock, établis là en 1878. Peuplé surtout de bergers hispaniques, le village devient aussi le refuge favori de Billy the Kid, ami de la famille.",
  '200', "Pete Maxwell est le petit-fils de Charles Beaubien par sa mère Luz. Utley (2015) attribue l'achat du fort à Pete ; Wallis et l'atlas (DRV-08), à Lucien. En français, l'histoire a été racontée par le Québécois Éric Veillette (Billy, 2008), qui fait intervenir Luz Beaubien Maxwell, et par Éric Vuillard (Les orphelins, roman, 2019).")
F('02', "Fort Sumner, Noël 1880 : Luz Beaubien Maxwell, Paulita et Deluvina", 'famille', '1880-12-24', -104.1925, 34.4040, 'c', ['Luz Beaubien Maxwell', 'Paulita Maxwell', 'Deluvina Maxwell', 'Pat Garrett'],
  "La veille de Noël 1880, le shérif Garrett ramène enchaînés à Fort Sumner les prisonniers de Stinking Springs, dont Billy the Kid. Deluvina Maxwell, servante navajo de la maison, capturée enfant et échangée à Lucien Maxwell, obtient de Garrett que Billy puisse dire adieu à Paulita, la plus jeune fille de Lucien et de Luz. Dans l'ancien quartier des officiers, doña Luz Beaubien Maxwell demande en vain qu'on lui ôte ses chaînes pour un moment d'intimité.",
  '217', "Utley (2015, PDF p. 102) rapporte la même scène : c'est « Mother » Maxwell, veuve de Lucien, qui implore Garrett. Voir MT02-08 pour l'arrivée de Deluvina chez les Maxwell.")
F('03', "Fort Sumner, juillet 1881 : la chambre de Pete Maxwell et le cimetière où repose Lucien", 'evenement', '1881-07-14/1881-07-15', -104.1928, 34.4042, 'c', ['Pete Maxwell', 'Deluvina Maxwell', 'Paulita Maxwell', 'Lucien Maxwell', 'Pat Garrett'],
  "Dans la nuit du 14 juillet 1881, Pat Garrett interroge Pete Maxwell dans sa chambre obscure de la maison familiale quand Billy the Kid y entre ; Garrett l'abat. Pete pose une chandelle sur le rebord de la fenêtre pour que les adjoints voient le corps. Au matin, Deluvina Maxwell frappe Garrett de ses poings, et les femmes consolent Paulita. Billy est inhumé dans le vieux cimetière militaire, où reposait déjà Lucien Maxwell depuis 1875.",
  '216, 226', "La maison Maxwell est aussi le lieu de DRV-20 (Pablo Beaubien). Le récit détaillé de la mort de Billy est dans l'Atlas Billy the Kid.")
F('04', "Près de Puerto de Luna : le ranch de Pablo Beaubien (décembre 1880)", 'evenement', '1880-12-17/1880-12-18', -104.560, 34.770, 'h', ['Pablo Beaubien', 'Pat Garrett', 'Alexander Grzelachowski'],
  "Parti du magasin de Grzelachowski à Puerto de Luna le 17 décembre 1880, le shérif Pat Garrett fait halte avec sa troupe au ranch de Pablo Beaubien, à un mille au-dessus de celui de Gayheart. Son éclaireur y revient de Fort Sumner avec la confirmation que les hommes qu'il poursuit s'y trouvent.",
  '68', "Ce Pablo Beaubien est sans doute le dernier fils de Charles Beaubien, éleveur de moutons à Fort Sumner depuis 1870 (DRV-20, WJ-beaubien-pablo) ; Garrett ne le précise pas. Position hypothétique sur le Pecos, en aval de Puerto de Luna.", source=GA)
fiches = C.fiches
