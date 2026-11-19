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
RC = "ICI Radio-Canada Première (2014), Sur les traces de Kerouac, livre numérique de la série radiophonique, préfaces de Franco Nuovo et Gabriel Anctil (PDF du Drive de l'auteur, Kerouac_VF.pdf)"
F('03', "Nashua (New Hampshire) : mariage de Léo-Alcide Kerouac et de Gabrielle Lévesque (1915)", 'famille', '1915', -71.4676, 42.7654, 'c', ['Léo-Alcide Kerouac', 'Gabrielle Lévesque', 'Jack Kerouac'],
  "Le père de Jack, Léo-Alcide Kerouac (né Kirouac à Saint-Hubert-de-Rivière-du-Loup en 1889), émigre avec sa famille dès 1890 ; sa mère, Gabrielle Lévesque, née à Saint-Pacôme en 1895, cousine éloignée de René Lévesque, a elle aussi quitté le Bas-Saint-Laurent. Ils se rencontrent à Nashua et s'y marient en 1915, avant de s'établir à Lowell, dans le milieu ouvrier canadien-français des filatures.",
  '18-23', "Point au centre de Nashua.", source=RC)
F('04', "Lowell (Centralville) : Ti-Jean à l'école paroissiale bilingue Saint-Louis-de-France (1927-1933)", 'religion', '1927/1933', -71.3065, 42.6488, 'a', ['Jack Kerouac'],
  "De 1927 à 1933, « Ti-Jean » Kerouac fréquente l'école paroissiale bilingue Saint-Louis-de-France, dans le quartier de Centralville, qu'il décrira comme une communauté française étroitement unie. Toute sa vie, il écrira aussi en français : en 1952, à Mexico, il rédige en français un court roman, Sur le chemin, sur un voyage de Ti-Jean et de son père en 1935 ; d'autres manuscrits français dorment dans la Berg Collection de la New York Public Library.",
  '23-59', "Point à l'église Saint-Louis-de-France de Lowell (rue West Sixth), approximatif.", source=RC)
fiches = C.fiches
