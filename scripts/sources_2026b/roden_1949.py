# Carl B. Roden, « The Beaubien Claim », Journal of the Illinois State Historical Society, vol. 42, n° 2 (juin 1949),
# p. 147-166, PDF JSTOR du Drive de l'auteur. Corpus « Recherches », préfixe RD49.
from commun import Corpus
RD = "Roden, Carl B. (1949), « The Beaubien Claim », Journal of the Illinois State Historical Society, vol. 42, n° 2, p. 147-166"
C = Corpus('Recherches', 'RD49', RD, page_fmt='p. {}')
F = C.F
F('01', "Chicago : la réclamation Beaubien sur la réserve du fort Dearborn, de la préemption à la Cour suprême (1835-1839)", 'evenement', '1823~/1839', -87.6240, 41.8870, 'c', ['Jean-Baptiste Beaubien', 'Thomas Ford', 'Daniel Webster', 'Francis Scott Key', 'Andrew Jackson', 'Robert A. Kinzie'],
  "Établi depuis 1817 près du fort Dearborn, agent de l'American Fur Company, Jean-Baptiste Beaubien s'installe vers 1823 à l'est des bâtiments de la compagnie, sur la réserve militaire. Il y tient école, fait venir des prêtres et anime un cercle de débats. Après la loi de préemption, il dépose en 1835 une demande pour le quart sud-ouest de la section fractionnaire 10 (75,69 acres, entre la rivière et la rue Madison), qui est rejetée parce qu'il s'agit d'une réserve militaire. On raconte que le président Jackson aurait déchiré la patente prête à être signée. Le juge Thomas Ford lui donne raison sur le fond en 1836 et la Cour suprême de l'Illinois reconnaît son titre. La Cour suprême des États-Unis casse cette décision en 1839, malgré des avocats comme Daniel Webster et Francis Scott Key. Le terrain est ensuite vendu en lots de 48 pieds de façade.",
  '149-166', "Point placé à l'emplacement de la réserve, au sud de l'embouchure de la rivière Chicago.")
fiches = C.fiches
