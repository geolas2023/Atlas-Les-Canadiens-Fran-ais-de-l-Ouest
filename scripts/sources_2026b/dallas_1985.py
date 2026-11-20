# Sandra Dallas, Colorado Ghost Towns and Mining Camps, Norman, University of Oklahoma Press, 1985. PDF du Drive de
# l'auteur, lu en entier via le visualiseur. Corpus « Recherches », préfixe DA85.
from commun import Corpus
DA = "Dallas, Sandra (1985), Colorado Ghost Towns and Mining Camps, Norman, University of Oklahoma Press"
C = Corpus('Recherches', 'DA85', DA, page_fmt='p. {} (PDF)')
F = C.F
F('01', "Crisman (Colorado) : la cave à vin murée du Français Pierre Ardourel (1894)", 'personne', '1880~/1894', -105.37, 40.04, 'a', ['Pierre Ardourel'],
  "Dans le camp minier de Crisman, à sept milles à l'ouest de Boulder, fondé au milieu des années 1880 autour des mines Yellow Pine et Great Logan, le principal citoyen est un Français, le propriétaire de mine Pierre Ardourel. Il s'y bâtit une belle maison avec une vaste cave à vin. En 1894, un tracé malencontreux de la voie ferrée à écartement étroit bloque l'accès de la cave ; la légende veut que les bouteilles y vieillissent encore.",
  '153-154', "Point approximatif à Crisman, dans le canyon Four Mile, à l'ouest de Boulder.")
fiches = C.fiches
