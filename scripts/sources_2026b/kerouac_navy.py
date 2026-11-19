# Jack Kerouac, extraits du dossier militaire officiel de l'US Navy (National Personnel Records Center, NARA), 1942-1943
# (PDF du Drive de l'auteur, dossier JACK_KEROUAC, passé à l'OCR). Préfixe KR43.
from commun import Corpus
KR = "National Archives and Records Administration, National Personnel Records Center, « Jack Kerouac. Excerpts from official military personnel file » (US Navy, 1942-1943)"
C = Corpus('Recherches', 'KR43', KR, page_fmt='PDF p. {}')
F = C.F
F('01', "Lowell : Jean-Louis (« Jack ») Kerouac, fils de Franco-Américains (né le 12 mars 1922)", 'personnage', '1922-03-12/1939', -71.3162, 42.6334, 'c', ['Jack Kerouac', 'Gabrielle Kerouac'],
  "Le dossier de la Navy de « John Louis Kerouac », signé de son nom de baptême Jean-Louis, le dit né à Lowell (Massachusetts) le 12 mars 1922, catholique, fils d'une mère née au Canada français, Gabrielle. Il y déclare avoir fait ses cinq premières années dans une école paroissiale française, avant l'école publique, puis la Horace Mann School de New York et l'université Columbia. Le français, qu'il parlait en famille, restera la langue de son enfance à Lowell.",
  '1-9', "Point au centre de Lowell ; la maison natale, au 9, Lupine Road (quartier Centralville), n'est pas citée par le dossier.")
F('02', "Newport (Rhode Island) : la brève carrière de matelot de Jack Kerouac (mars-mai 1943)", 'personnage', '1943-03-22/1943-05-18', -71.3305, 41.5088, 'c', ['Jack Kerouac'],
  "Engagé dans la réserve de la Navy à New York en décembre 1942, après trois mois dans la marine marchande jusqu'au Groenland, Kerouac se présente le 22 mars 1943 au centre d'instruction navale de Newport. Mis au repos pour de violents maux de tête, puis tenu pour inapte, il est transféré le 18 mai 1943 au centre médical naval de Bethesda (Maryland) et réformé peu après.",
  '1-9', "Point à la station navale de Newport.")
fiches = C.fiches
