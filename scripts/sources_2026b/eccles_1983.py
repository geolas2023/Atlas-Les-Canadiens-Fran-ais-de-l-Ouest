# W. J. Eccles, The Canadian Frontier, 1534-1760, éd. révisée, Albuquerque, University of New Mexico Press, 1983
# (PDF du Drive de l'auteur, dossier FUR_TRADE_USA). Synthèse ; seuls deux passages sur l'Ouest sont retenus. Préfixe EC83.
from commun import Corpus
EC = "Eccles, W. J. (1983), The Canadian Frontier, 1534-1760, éd. révisée, Albuquerque, University of New Mexico Press"
C = Corpus('Recherches', 'EC83', EC, page_fmt='p. {}')
F = C.F
F('01', "Lac Winnipeg : les coureurs de bois dans les plaines du Nord-Ouest avant 1688 (carte de Franquelin)", 'evenement', '1688', -97.5, 51.5, 'h', ['Jean-Baptiste-Louis Franquelin'],
  "La carte de Jean-Baptiste-Louis Franquelin (1688) figure déjà le lac des Bois (« lac de Buade ») et, sous les noms de lacs des Assinibouels et des Christinaux, les lacs Winnipeg, Manitoba et Winnipegosis, placés quelque quatre cents milles trop à l'est d'après les récits des coureurs de bois. Pour Eccles, c'est la preuve que des Français avaient atteint les plaines du Nord-Ouest avant 1688, un demi-siècle avant La Vérendrye.",
  '4', "Point schématique entre les lacs Winnipeg et Manitoba.")
F('02', "Fort La Reine et la Mer de l'Ouest : la traite des esclaves panis (années 1730-1740)", 'commerce', '1734/1749', -98.29, 49.97, 'a', ['Pierre Gaultier de Varennes et de La Vérendrye'],
  "Eccles rappelle que les explorateurs de la Mer de l'Ouest ont préféré la route de la Saskatchewan à celle du Missouri : elle évitait le pays sioux, donnait de meilleures fourrures, coupait la route de la baie d'Hudson, et le cri suffisait au commerce jusqu'aux Pieds-Noirs. Dans ces années, la traite des esclaves autochtones devient importante aux postes de l'Ouest : jusqu'à soixante par an sont expédiés à Montréal, surtout des Panis (Pawnees) du Missouri, mais aussi des Sioux capturés par les Outaouais et les Cris. On disait même que La Vérendrye, commandant de la Mer de l'Ouest, envoyait à Montréal plus d'esclaves que de ballots de fourrures.",
  '149-150', "Point au fort La Reine (Portage-la-Prairie, Manitoba), siège du poste de la Mer de l'Ouest.")
fiches = C.fiches
