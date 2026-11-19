# Gilles Havard, L'Amérique fantôme. Les aventuriers francophones du Nouveau Monde, Paris, Flammarion, 2019 (PDF et epub du
# dossier GILLES_HAVARD du Drive de l'auteur). Préfixe HV19. Seuls l'introduction et les ch. 1 à 3 (début) sont lisibles par
# l'outil du Drive (fichiers de 30 et 13,8 Mo) ; les ch. 4 à 10 (Perrot, Lalondette et Amiotte, Truteau, Charbonneau,
# Provost, Beauchamp) restent à dépouiller.
from commun import Corpus
HV = "Havard, Gilles (2019), L'Amérique fantôme. Les aventuriers francophones du Nouveau Monde, Paris, Flammarion"
C = Corpus('Recherches', 'HV19', HV, page_fmt='{}')
F = C.F
F('01', "Île d'Edelano (lac George, fleuve Saint-Johns, Floride) : le truchement Pierre Gambie, gendre d'un chef timucua (1564-1565)", 'personnage', '1564-10/1565-04', -81.6200, 29.3500, 'a', ['Pierre Gambie', 'René Goulaine de Laudonnière', 'Jacques Le Moyne de Morgues'],
  "Jeune Normand, sans doute huguenot, formé dans la maison du cardinal de Châtillon, Pierre Gambie a déjà vécu en Floride pour apprendre les langues et commercer avant l'expédition de Laudonnière de 1564 : c'est un « truchement », interprète placé chez les Indiens. À l'automne 1564, il quitte seul le fort Caroline, chargé de marchandises, s'établit au village d'Adelano, sur une île du fleuve Saint-Johns, épouse la fille du chef timucua et gouverne en son absence, au point de se faire haïr. Vers avril 1565, rentrant vers le fort Caroline dans une pirogue chargée de ses biens, il est tué à coups de hache par l'un de ses deux piroguiers. Laudonnière tente en vain de surprendre le chef d'Adelano en représailles. La scène, d'après une aquarelle perdue de Le Moyne de Morgues, est la dernière planche de la série floridienne de Théodore de Bry (1591), placée à part pour ne pas troubler l'image de la concorde franco-timucua. Havard doute des motifs de cupidité ou de vengeance avancés par les témoins, et suggère la jalousie ou un manquement aux devoirs de redistribution d'un parent.",
  "Ch. 1, « Une ombre en Floride : le meurtre de Pierre Gambie »", "Adelano est généralement identifié à l'île Drayton, dans le lac George ; point à cette île (la carte de Havard situe l'île d'Adelano près du lac George).")
fiches = C.fiches
