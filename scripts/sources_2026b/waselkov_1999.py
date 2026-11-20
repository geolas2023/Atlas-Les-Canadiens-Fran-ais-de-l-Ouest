# G. A. Waselkov, Old Mobile Archaeology, Mobile, Center for Archaeological Studies, University of South Alabama,
# 1999 ; rééd. University of Alabama Press (Fire Ant Books), 2005 (PDF du Drive de l'auteur, dossier MOBILE ;
# 115 000 caractères, lu en entier le 20 nov. 2026). Préfixe WA99.
from commun import Corpus
WA = "Waselkov, Gregory A. (1999), Old Mobile Archaeology, Mobile, Center for Archaeological Studies, University of South Alabama (rééd. University of Alabama Press, 2005)"
C = Corpus('Recherches', 'WA99', WA, page_fmt='p. {}')
F = C.F
OM = (-88.02, 30.92)  # Vieux Mobile, Twenty-seven Mile Bluff (site 1MB94), même point que les fiches « Fort Louis de la Mobile »
PD = (-88.11, 30.25)  # Port-Dauphin, île Dauphine (île Massacre)

F('01', "Vieux Mobile : les Canadiens d'Iberville défrichent le site du fort Louis (20 janvier 1702)", 'etablissement', '1702-01-20', *OM, 'c',
  ['Pierre Le Moyne d\'Iberville', 'Jean-Baptiste Le Moyne de Bienville', 'Charles Levasseur'],
  "Le 20 janvier 1702, les Canadiens d'Iberville commencent à défricher le Twenty-seven Mile Bluff, sur la rive droite de la rivière Mobile, juste en aval des villages des Mobiliens, qui ont recommandé l'endroit. On bâtit d'abord le fort Louis, carré de 22 toises entre les pointes des bastions, aux bastions de pièce sur pièce ; le logis de Bienville, avec un balcon sur la rivière, la chapelle, le magasin et le corps de garde forment les murs intérieurs. Un plan de la ville, probablement de Charles Levasseur, trace la même année les rues et les lots. Les Français nomment la ville d'après leurs alliés mobiliens. La poudre, stockée dans un magasin souterrain, est vite gâtée par les infiltrations ; un ouragan détruit les bastions en 1708, aussitôt rebâtis plus grands.",
  '4-7', "Point au site du Vieux Mobile (Twenty-seven Mile Bluff). Waselkov date la décision d'Iberville de janvier 1702.")
F('02', "Vieux Mobile : le dénombrement de Nicolas de La Salle (31 août 1704) et celui de 1708", 'etablissement', '1704-08-31/1708', *OM, 'c',
  ['Nicolas de La Salle', 'Madeleine Chartroux'],
  "Le commissaire Nicolas de La Salle, qui avait accompagné l'explorateur La Salle au Texas vingt ans plus tôt, compte le 31 août 1704 cent quatre-vingts hommes armés de fusils et vingt-sept familles françaises, qui n'ont que trois petites filles et sept garçons de un à dix ans. Les colons occupent quatre-vingts maisons de bois d'un étage, couvertes de palmes ou de paille ; onze Autochtones (six garçons de 12 à 18 ans et cinq jeunes femmes) sont tenus en esclavage en ville ; un jésuite et trois prêtres du Séminaire desservent la ville et les missions. Il note aussi seize canons de fer de 12 et de 8 livres au fort, et le bétail : neuf bœufs, quatorze vaches, quatre taureaux, cinq veaux, cent porcs, trois chevreaux, quatre cents poules. En 1708, il recense 339 personnes, dont 122 hommes de garnison, 24 habitants sans concession, 28 Françaises et 25 enfants, soixante Canadiens vivant « dans les villages sauvages le long du Mississippi sans permission d'aucun gouverneur » et quatre-vingts esclaves autochtones.",
  '10, 26', "Madeleine Chartroux, épouse de Nicolas de La Salle, était venue avec sa famille sur les expéditions de 1701-1702 (p. 21). Le dénombrement de 1704 est aux Archives des Colonies, C13A 1, f. 469-470.")
F('03', "Vieux Mobile : maison et jardin des prêtres du Séminaire de Québec, et le cimetière (plan de 1704-1705)", 'religion', '1704/1705', *OM, 'a',
  ['La Vente (curé)'],
  "À l'ouest de la ville, les prêtres du Séminaire de Québec ont leur logis et un grand jardin clos ; le croquis qu'en donne le plan de 1704-1705, avec cheminée centrale, toit en croupe et double porte, est, avec celui du fort, la seule vue d'époque d'un bâtiment du Vieux Mobile. En face, de l'autre côté de la rue, un terrain de 25 toises de côté est réservé au cimetière. Le curé La Vente tonne contre les colons qui gardent des esclaves autochtones comme concubines.",
  '7-9, 39')
F('04', "Vieux Mobile : la briqueterie et les briquetiers Pierre Brossard et Charles Mire (1703)", 'etablissement', '1703/1711', *OM, 'a',
  ['Pierre Brossard', 'Charles Mire', 'Jacques Le Comte'],
  "Le plan de 1704-1705 indique, au bord de la rivière, le « Terrain par La Bricqterie » ; les analyses confirment que les briques de la ville sont faites de l'argile de la berge, moulées à la main et cuites au four : c'est la première industrie de type européen de la colonie. Arrivés en 1703, les briquetiers Pierre Brossard et Charles Mire suffisent à la demande, faute de briques importées ; les tuiles, elles, viennent de France et ne coiffent, semble-t-il, que les faîtes. Le charpentier Jacques Le Comte travaille au fort et à une église paroissiale dont l'emplacement est inconnu.",
  '16-17, 24')
F('05', "Port-Dauphin : le Pélican débarque une vingtaine de jeunes Françaises, et la fièvre jaune (juillet 1704)", 'migration', '1704-07', *PD, 'c',
  [],
  "Fin juillet 1704, le Pélican débarque à Port-Dauphin, sur l'île Massacre, une vingtaine de jeunes femmes recrutées par l'évêque de Québec, surtout aux environs de Paris, pour épouser les Canadiens de la Louisiane ; presque toutes tiennent parole. Mais le navire apporte aussi la fièvre jaune, contractée à La Havane : plus de quarante colons de Mobile en meurent, et l'épidémie frappe les petites nations voisines. Port-Dauphin, où l'on transborde les marchandises sur des chaloupes et des canots pour remonter la baie jusqu'à Mobile, reste le port d'entrée de la colonie pendant vingt ans. Seuls cinq grands navires ravitaillent la Louisiane pendant l'occupation du Vieux Mobile (Renommée 1702, Loire 1703, Pélican 1704, Aigle 1706, Renommée 1708).",
  '1-2, 22-23', "Point au village de Port-Dauphin (île Dauphine).")
F('06', "Vieux Mobile : Bienville ferme le cabaret d'Étienne Burelle (1706)", 'evenement', '1706', *OM, 'c',
  ['Étienne Burelle', 'Jean-Baptiste Le Moyne de Bienville'],
  "Le seul cabaretier connu du Vieux Mobile est le Français Étienne Burelle, arrivé en 1704 sur le Pélican : Bienville ferme son cabaret six mois en 1706 pour avoir acheté des marchandises volées au magasin du roi. Les fouilles ont pourtant trouvé des débris de cabaret (verres à vin, pipes de terre surtout anglaises) sur deux autres sites de la ville et sur la seule maison fouillée du village de Port-Dauphin.",
  '28-29')
F('07', "Port-Dauphin : le fort de 1710 et l'attaque des pirates de la Jamaïque", 'evenement', '1710', *PD, 'c',
  [],
  "Pendant la guerre de Succession d'Espagne, un petit commerce de contrebande se fait avec les navires anglais et hollandais qui longent la côte, jusqu'à ce que des pirates anglais de la Jamaïque attaquent Port-Dauphin en 1710. Un fort est bâti cette année-là sur l'île, où l'on transporte peut-être une partie des canons du fort Louis. Après 1713, le commerce discret avec la Caroline du Sud reprend : la maison fouillée à Port-Dauphin (v. 1715-1725) a livré beaucoup de bouteilles anglaises et une intaille au motif d'alambic.",
  '26, 30-34')
F('08', "Vieux Mobile : la forge de la lisière nord-ouest (structure 2)", 'etablissement', '1702/1711', OM[0] - 0.003, OM[1] + 0.002, 'a',
  [],
  "Fouillée en 1990 au bord du marais qui borne la ville à l'ouest, la forge est un petit bâtiment de poteaux sur sole de 4,8 sur 6,2 mètres : 86 kilos de scories, un tas d'anthracite (peut-être les dix barriques de « charbon d'Angleterre » envoyées en 1701 avec deux enclumes, un étau et un soufflet), des bouts de verges à clous. Le forgeron fabrique des clous et répare chaudrons, gardes d'épée et armes, dont une platine de mousquet espagnol à la miquelet ; des pointes de flèche taillées tout près laissent penser qu'il avait un aide autochtone. Une quinzaine de clôtures entrecroisées entourent l'atelier, dont un poulailler.",
  '20-21', "Position décalée de quelques centaines de mètres vers le nord-ouest du point du fort, pour la lisibilité.")
F('09', "Le Vieux Mobile abandonné et brûlé (1711), puis retrouvé (1989-1993)", 'evenement', '1711/1993', *OM, 'c',
  ['Donald Harris', 'James C. Parnell', 'Jay Higginbotham', 'Gregory A. Waselkov'],
  "En 1711, les colons transportent leur établissement à la tête de la baie et, semble-t-il, incendient la vieille ville, dont ils récupèrent briques et tuiles mais pas les milliers de clous de chaque maison. Le site reste un repère, le « Vieux Fort ». Donald Harris y fait un premier sondage en 1970 ; en 1989, l'ingénieur James C. « Buddy » Parnell, inspiré par le livre de Jay Higginbotham (1977), dégage sous de légers renflements des sols d'argile, des briques et des clous. L'équipe de l'Université de South Alabama dirigée par Waselkov fouille alors la structure 1 et creuse de 1989 à 1993 15 025 sondages à la pelle, la plus vaste prospection de ce genre en Amérique : 55 bâtiments sur 70 acres, tous orientés à 40° ouest du nord, comme les rues des plans d'époque.",
  '1-2, 10-12, 16', "Le site porte le numéro 1MB94.")
F('10', "Après 1711 : le « Vieux Fort », le village Sainte-Hermine et l'habitation de M. de La Tour (carte v. 1725)", 'etablissement', '1725~', -88.03, 30.95, 'a',
  ['M. de La Tour'],
  "Sur une carte du cours de la Mobile attribuée à Valentin Devin, vers 1725, l'ancien fort et la vieille ville restent des repères le long de la rivière ; quelques familles françaises vivent au village de Sainte-Hermine ou exploitent des habitations riveraines, comme M. de La Tour au Twenty-one Mile Bluff, en aval. Deux villages mobiliens occupent toujours les escarpements de Seymour et de Chastang.",
  '55', "Point au Twenty-one Mile Bluff (même point que les autres fiches de ce lieu).")
F('11', "Vieux Mobile : Bienville accueille les Apalaches et les Chatos chassés de Floride (juillet 1704)", 'migration', '1704-07', *OM, 'c',
  ['Jean-Baptiste Le Moyne de Bienville', 'Alexandre Huvé'],
  "En juillet 1704, environ 800 habitants de San Luis de Talimali, capitale de la province d'Apalache, et de trois villages alliés, chassés par les raids des Creeks et des Anglais de James Moore, marchent près de 300 milles jusqu'à Mobile en poussant leur bétail ; ils refusent de s'établir près de Pensacola, disant que les Français les armeront mieux. Bienville leur fournit du maïs de semence et confie leur soin spirituel au père Alexandre Huvé, qui commence aussitôt à baptiser. Les Apalaches fondent deux villages en amont des Mobiliens ; environ deux cents Chatos s'établissent aux Oignonets, à l'embouchure de la rivière. Leurs potières fabriquent pour les colons des imitations de vaisselle européenne (pichets, pieds de verre).",
  '43-46', "Point au Vieux Mobile, où Bienville les reçoit ; voir les fiches de l'Atlas des Autochtones pour les villages.")
F('12', "De Mobile à Veracruz : la Précieuse, l'Espérance, l'Aventurier et la contrebande (1702-1711)", 'commerce', '1702/1711', -96.13, 19.2, 'c',
  ['Jean-Baptiste Le Moyne de Bienville'],
  "Les prêts de poudre et de vivres que Bienville consent à la garnison espagnole de Pensacola servent de prétexte à des voyages à Veracruz pour en obtenir le remboursement. Les petits bâtiments de la colonie, la Précieuse, l'Espérance et l'Aventurier, font la navette jusqu'à ce que chacun coule, rongé par les vers, dans le port de l'île Massacre ; chaque voyage emporte aussi des marchandises pour un commerce illicite. En 1710, un colon accuse Bienville et ses frères de se servir des vaisseaux du roi pour vendre leurs pelleteries à Veracruz. Les fouilles du Vieux Mobile ont livré une quantité étonnante de céramique mexicaine (majolique de Puebla, poterie de Tonalá et d'El Morro), de porcelaine chinoise et de piécettes d'argent de Mexico et de Potosí.",
  '45-50', "Point à Veracruz.")
fiches = C.fiches
