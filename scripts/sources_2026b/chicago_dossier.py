# Dossier HISTOIRE_LIVRES/CHICAGO du Drive de l'auteur, relu le 19 nov. 2026 (soir) : dépliant « Chicago, une ville où le
# français se parle depuis 1673 », Diamond et Ndiaye, Histoire de Chicago (lu, sans autre apport), et 30 images
# (cartes de 1830 et 1833, fiche scolaire sur DuSable, carte de l'incendie de 1871, etc.). Préfixe CHF.
from commun import Corpus
SD = "« Chicago, une ville où le français se parle depuis 1673 », dépliant (PDF du Drive de l'auteur, dossier CHICAGO)"
SN = "Diamond, Andrew, et Pap Ndiaye (2013), Histoire de Chicago, Paris, Fayard"
SI = "« Jean Baptiste Pointe DuSable c.1745-1818 », fiche pédagogique illustrée (image du dossier CHICAGO, Drive de l'auteur)"
SC = "Carte « The Town of Chicago, population 350 » (1833), reproduction (images du dossier CHICAGO, Drive de l'auteur) ; carte de l'embouchure de la rivière Chicago par F. Harrison Jr. et William Howard (24 février 1830)"
C = Corpus('Recherches', 'CHF', SD, page_fmt='p. {}')
F = C.F
F('01', "Chicago : Pierre You de La Découverte épouse une Miami nommée Élisabeth (avril 1693)", 'famille', '1693-04', -87.635, 41.885, 'a', ['Pierre You de La Découverte'],
  "Selon le dépliant, qui s'appuie sur le Dictionnaire biographique du Canada, le militaire Pierre You, sieur de La Découverte, épouse en avril 1693, sur le territoire de Chicago, une Miami surnommée Élisabeth : le premier mariage célébré à Chicago.",
  '4', "Point placé à l'embouchure de la rivière Chicago ; le lieu exact n'est pas précisé.")
F('02', "Chicago : le « French Battalion » parmi les compagnies levées par nationalité au début de la guerre de Sécession (1861)", 'evenement', '1861', -87.630, 41.880, 'a', [],
  "Au début de la guerre de Sécession, des compagnies sont levées à Chicago selon les affiliations nationales : les Lincoln Rifles (Europe centrale et orientale), les German Turner Union Cadets, la Scottish Highland Guard et un « French Battalion ».",
  '', "Mention brève ; le livre ne donne ni effectifs ni chefs.", source=SN)
F('03', "Saint-Charles (Missouri) : Jean-Baptiste Pointe DuSable, qui a vendu ses biens de Chicago 1 200 $ le 7 mai 1800, meurt pauvre le 28 août 1818", 'personne', '1800-05-07/1818-08-28', -90.482, 38.784, 'c', ['Jean-Baptiste Pointe DuSable'],
  "Selon cette fiche, DuSable, né en Haïti vers 1745, vend soudain ses terres et ses biens de Chicago pour 1 200 $ le 7 mai 1800 et quitte la région ; il meurt presque sans le sou le 28 août 1818 et est enterré dans un cimetière catholique de Saint-Charles (Missouri). Sa petite-fille, née en 1796, serait le premier enfant né à Chicago ; l'État de l'Illinois et la ville le reconnaissent comme fondateur le 25 octobre 1968.",
  '', "Fiche de vulgarisation sans références ; les circonstances de son départ y sont présentées comme incertaines.", source=SI)
F('04', "Chicago en 1833 : la cabane et le magasin La Framboise, Ouilmette, Billy Caldwell et la maison Portier sur la carte de la ville", 'etablissement', '1830/1833', -87.640, 41.889, 'a', ['La Framboise', 'Antoine Ouilmette', 'Billy Caldwell (Sauganash)', 'Joseph Porthier', 'Jean-Baptiste Beaubien'],
  "La carte de la « ville de Chicago, 350 habitants » (1833) situe, outre le second fort Dearborn (1816), la maison Kinzie, la taverne Sauganash et le premier pont-levis (1834), la cabane et le magasin La Framboise, la maison d'Antoine Ouilmette sur la route de Green Bay, celle de Billy Caldwell (Sauganash) et la maison Portier. La carte de l'embouchure dressée par F. Harrison Jr. et William Howard le 24 février 1830 montre le magasin de J.-B. Beaubien au sud du fort et la maison Kinzie occupée par Jonathan Bailey.",
  '', "Cartes reproduites sans indication d'éditeur ; points approximatifs.", source=SC)
fiches = C.fiches
