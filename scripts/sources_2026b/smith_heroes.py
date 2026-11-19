# Randy D. Smith, Heroes of the Santa Fe Trail, 1821-1900 (2010 ?), PDF du Drive de l'auteur (dossier SANTA_FE_TRAIL).
# Corpus « Recherches », préfixe RSH.
from commun import Corpus
RS = "Smith, Randy D., Heroes of the Santa Fe Trail, 1821-1900"
C = Corpus('Recherches', 'RSH', RS, page_fmt='PDF p. {}')
F = C.F
F('01', "Rayado : les troupeaux de moutons pour la Californie, avec Henry Mercure et John Bernavette (1853)", 'commerce', '1853-01/1853-03', -104.927, 36.371, 'c', ['Henry Mercure', 'John Bernavette', 'Kit Carson', 'Lucien Maxwell', 'John Hatcher'],
  "Après les profits de Dick Wootton sur les moutons vendus en Californie, Rayado s'organise : John Hatcher part avec un troupeau en janvier 1853 ; en février, Kit Carson achète 6 500 bêtes dans le sud du Nouveau-Mexique et rejoint à Rayado Henry Mercure et John Bernavette pour une deuxième conduite ; Lucien Maxwell rassemble un troisième troupeau en mars, le vend à Sacramento et revient avec Carson. Les conduites auraient rapporté de 20 000 à 50 000 dollars au ranch.",
  '72', "Henry Mercure est l'un des frères Mercure, marchands canadiens de Santa Fe liés à Aubry. Point à l'hacienda de Rayado.")
fiches = C.fiches
