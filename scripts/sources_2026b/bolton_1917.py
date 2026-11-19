# Herbert E. Bolton, « French Intrusions into New Mexico, 1749-1752 » (1917), tiré à part du Drive de l'auteur (dossier NEW_MEXICO),
# texte intégral sur archive.org (frenchintrusions00boltrich). Corpus « Recherches », préfixe BF17.
from commun import Corpus
BO = "Bolton, Herbert E. (1917), « French Intrusions into New Mexico, 1749-1752 », dans H. Morse Stephens et H. E. Bolton (dir.), The Pacific Ocean in History, New York, Macmillan, p. 389-407 (archive.org, frenchintrusions00boltrich)"
C = Corpus('Recherches', 'BF17', BO)
F = C.F
FE, SA, RI, CH, FU = 'Luis Febre', 'Pierre Satren', 'Joseph Miguel Riballo', 'Jean Chapuis', 'Louis Feuilli'
F('01', "Foire de Taos : trente-trois Français chez les Comanches (février 1748)", 'commerce', '1748-02-27', -105.573, 36.407, 'a', [],
  "Le 27 février 1748, sept Comanches venus d'un village de la rivière Xicarilla annoncent à Taos que trente-trois Français sont venus chez eux échanger des fusils contre des mules ; deux d'entre eux attendent pour accompagner les Comanches à la foire de Taos. Le gouverneur Codallos y voit un complot franco-comanche et propose un poste militaire sur la Xicarilla.",
  '392-393', "Point placé à Taos, lieu de la foire ; le village comanche n'est pas localisé.")
F('02', "Poste des Arkansas : départ de Febre, Satren et Riballo (automne 1748)", 'migration', '1748-09~', -91.35, 34.02, 'a', [FE, SA, RI],
  "À l'automne 1748, douze hommes partent d'un village d'Arkansas (« Zarca ») à l'ouest du poste des Arkansas pour gagner le Nouveau-Mexique par la Napestle (l'Arkansas), encouragés par le retour des Mallet et par la paix entre Jumanos et Comanches. Parmi eux, trois déserteurs : Luis Febre, 29 ans, tailleur et barbier de La Nouvelle-Orléans passé par le Canada, Michillimakinac et l'Illinois ; Pierre Satren (« Pedro Sastre »), 42 ans, charpentier et ancien soldat natif de Québec ; et Joseph Miguel Riballo, 24 ans, charpentier natif de l'Illinois.",
  '394')
F('03', "Villages jumanos (Panipiquets) de la Napestle : un drapeau français (1748-1749)", 'poste', '1748/1750', -97.04, 37.06, 'h', [FE, SA, RI, 'Felipe de Sandoval'],
  "Les Jumanos (Panipiquets, les Wichitas des Français) vivent en deux villages palissadés de huttes d'herbe sur la Napestle, cultivent maïs, haricots et courges, et arborent un drapeau français reçu du commandant de la Louisiane ; des traiteurs français y montent régulièrement en canot depuis le poste des Arkansas, à neuf jours de descente. C'est de là que les Jumanos conduisent Febre et ses compagnons chez les Comanches, puis à la foire de Taos.",
  '394-397', "Position hypothétique des villages sur l'Arkansas, vers la frontière actuelle du Kansas et de l'Oklahoma.")
F('04', "Santa Fe, palais des gouverneurs : interrogatoire de Febre, Satren et Riballo (avril 1749)", 'evenement', '1749-04-12/1750-03-05', -105.9384, 35.6877, 'c', [FE, SA, RI, 'Pedro Soutter'],
  "Ramenés de la foire de Taos par Bernardo de Bustamante y Tagle, les trois Français arrivent à Santa Fe le 12 avril 1749. Désarmés, logés au palais des gouverneurs et mis au travail selon leur métier, ils sont interrogés le lendemain par l'intermédiaire de l'interprète Pedro Soutter, puis de nouveau le 5 mars 1750. Le gouverneur Vélez Cachupín propose de les établir en Sonora ou en Nouvelle-Biscaye, sans retour possible, car ce sont de bons artisans et d'excellents tireurs ; le vice-roi l'approuve en janvier 1751. En 1752, Febre, désormais « un peu versé dans la langue espagnole », sert lui-même d'interprète.",
  '393-395, 399-401')
F('05', "Michillimakinac : le passeport de Jean Chapuis (30 juillet 1751)", 'personnage', '1751-07-30', -84.7339, 45.7867, 'c', [CH, 'Duplessis Faber'],
  "Le 30 juillet 1751, le commandant de Michillimakinac, Duplessis Faber (« Falberte »), délivre un passeport à Jean Chapuis, 48 ans, natif de France et habitant du Canada, pour retourner aux Illinois s'occuper de ses affaires et y porter des marchandises.",
  '401')
F('06', "Fort de Chartres : licence de Saint-Clair « pour faire la découverte du Nouveau-Mexique » (6 octobre 1751)", 'exploration', '1751-10-06', -90.1586, 38.0848, 'c', [CH, 'Benoît de Saint-Clair', 'Roy', 'Jeandron', 'Aubuchon', 'Calvé', 'Louis Trudeau', 'Laurent Trudeau', 'Betille', 'Du Charme'],
  "Le 6 octobre 1751, le commandant du fort de Chartres, Benoît de Saint-Clair, autorise Jean Chapuis et neuf hommes, Roy, Jeandron, Foysi, Aubuchon, Calvé, Louis et Laurent Trudeau, Betille et Du Charme, à « faire la découverte du Nouveau-Mexique » avec les marchandises qu'ils jugeront bonnes, sous pavillon et sans se séparer : une expédition à demi officielle pour ouvrir une route commerciale.",
  '401')
F('07', "Fort Cavagnial (Kansas) : l'association Chapuis-Feuilli (9 décembre 1751)", 'commerce', '1751-12-09/1752-03', -94.92, 39.33, 'a', [CH, FU, 'Pierre Trudeau', 'Laurent Trudeau'],
  "Au fort Cavagnial, chez les Kansas, Chapuis s'associe le 9 décembre 1751 à Louis Feuilli (ou Foissi), interprète du roi au poste depuis huit ans, pour « aller ensemble en Espagne » et atteindre en avril les établissements espagnols ; il lui avance 400 livres de marchandises, payables en castor. Pierre et Laurent Trudeau signent comme témoins ; Feuilli ne sait pas signer. Ils repartent vers la mi-mars 1752 ; huit hommes font demi-tour chez les Pawnees ou les Comanches.",
  '401-402', "Position approximative du fort Cavagnial, près de l'actuelle Fort Leavenworth.")
F('08', "Mission de Pecos : arrivée de Chapuis et Feuilli sous pavillon blanc (6 août 1752)", 'evenement', '1752-08-06/1752-10', -105.6866, 35.5487, 'c', [CH, FU, FE, 'Juan Joseph Toledo'],
  "Le 6 août 1752, guidés par des Apaches jicarillas et carlanes rencontrés sur la Gallinas, Chapuis et Feuilli arrivent au cimetière de la mission de Pecos avec neuf chevaux et neuf ballots d'étoffes, sous un drapeau blanc. Le père Toledo, qui écrit leurs noms « Xanxapij » et « Luis Fxuij », avertit le gouverneur. À Santa Fe, leurs marchandises sont saisies et adjugées pour 404 pesos ; vers le 1er octobre, les deux hommes partent prisonniers pour Chihuahua et Mexico, d'où l'on décide en janvier 1754 de les envoyer en Espagne.",
  '400-405')
fiches = C.fiches
