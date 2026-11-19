# « Tom Sun - Wyoming Pioneer » (notice de MarylinMae, Find a Grave, 13 septembre 2011), copiée dans le Drive de
# l'auteur (Tom_Sun.txt). Corpus « Recherches », préfixe TS11. Source secondaire de mémoire familiale, à recouper.
from commun import Corpus
TS = "MarylinMae (2011), « Tom Sun - Wyoming Pioneer », notice de Find a Grave (cimetière de Rawlins), copie Tom_Sun.txt du Drive de l'auteur"
C = Corpus('Recherches', 'TS11', TS, page_fmt='{}')
F = C.F
F('01', "Devil's Gate (Sweetwater) : le ranch Sun de Thomas de Beau Soleil, « Tom Sun » (1872-1889)", 'etablissement', '1872/1889', -107.215, 42.445, 'a', ['Thomas de Beau Soleil (Tom Sun)', 'Napoléon Bonaparte « Boney » Earnest', 'LaFevre dit Descoteaux'],
  "Né au sud de Montréal, orphelin de mère, Thomas de Beau Soleil part seul vers l'Ouest à onze ans pour retrouver un oncle trappeur ; à Saint-Louis, un trappeur canadien nommé LaFevre, que les Indiens appellent Descoteaux, l'emmène dans les Rocheuses vers 1857. Après six mois dans le 6e régiment d'infanterie du Maine (1861), il revient éclaireur civil aux forts Halleck et Steele, fournit des traverses à l'Union Pacific par flottage sur la Platte Nord (d'où le nom de French Creek, d'après ses équipes), puis guide des chasseurs anglais, ami de Buffalo Bill. En 1872, il bâtit une cabane près de Devil's Gate, siège en 1879 du ranch « Hub and Spoke ». Il prend part en 1889 au lynchage d'Ella Watson (« Cattle Kate ») et de Jim Averell. Ses descendants forment, dit-on, la plus ancienne famille non autochtone du Wyoming encore établie.",
  '', "Mémoire familiale (Mme Tom Sun fils) relayée par une notice en ligne ; dates et filiation à vérifier.")
F('02', "Devil's Gate et Atlantic City : Charles Lajeunesse, rancher et marchand, et les familles métisses du Wyoming", 'famille', '1850~/1870~', -108.73, 42.50, 'h', ['Charles Lajeunesse', 'John Richard (Reshaw)'],
  "La même notice range parmi les rares pionniers du Wyoming antérieurs au territoire qui ont une descendance sur place Charles Lajeunesse, né de parents canadiens, convoyeur, tenancier d'un relais de route à Devil's Gate puis marchand à Atlantic City, marié à une Autochtone et dont les nombreux descendants vivent sur la réserve de Wind River. Elle cite aussi le « Français » Reshaw (John Richard), marié à une Sioux parente de Red Cloud, et six ou huit trappeurs canadiens restés près des forts Bridger et Laramie avec leurs épouses autochtones.",
  '', "Position à Atlantic City (Wyoming) ; « Cimaneau » dans la notice, sans doute Seminoe, surnom des Lajeunesse.")
fiches = C.fiches
