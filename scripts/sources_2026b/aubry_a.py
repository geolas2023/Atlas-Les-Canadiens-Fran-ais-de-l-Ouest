# Lot aubry_a : les 66 fichiers non-images du dossier FRANCOIS_XAVIER_AUBRY (Drive de l'auteur),
# dépouillés le 21 nov. 2026 pour vérifier ce qui manque à l'Atlas Aubry.
# Les faits manquants qui concernent Aubry lui-même vont au rapport (aubry_a.md, « Propositions pour l'Atlas Aubry ») ;
# ce module ne contient que les fiches réseau sur d'autres francophones absents de reseau.geojson.
# Préfixe FXA. Pages : pagination imprimée.
from commun import Corpus

MYERS = ("Myers, Harry C., « Massacre on the Santa Fe Trail: Mr. White's Company of Unfortunates », "
         "Wagon Tracks, vol. 6, no 2, février 1992 (PDF, Drive de l'auteur, dossier FRANCOIS_XAVIER_AUBRY)")
CHAPUT = ("Chaput, Donald, François X. Aubry: Trader, Trailmaker and Voyageur in the Southwest, 1846-1854, "
          "Glendale (Calif.), Arthur H. Clark, 1975 (PDF, Drive de l'auteur, dossier FRANCOIS_XAVIER_AUBRY/01_LIVRES)")

C = Corpus('Recherches', 'FXA', MYERS); F = C.F

F('01', "Fort Barclay (La Junta du Mora) : le capitaine Alexander Papin et ses volontaires néo-mexicains contre les Jicarillas (1849)",
  'evenement', '1849-06/1849-09', -104.98, 35.79, 'a',
  ['Alexander Papin', 'Henry Judd', 'William Miller', 'Alexander Barclay'],
  "En 1849, Alexander Papin commande une compagnie d'infanterie de volontaires du Nouveau-Mexique cantonnée au fort de Barclay, "
  "au confluent du Mora et du Sapello, là où les colons sont le plus exposés aux raids. Le 12 juin, le capitaine Henry Judd, "
  "commandant du poste de Las Vegas, l'envoie avec une partie de ses hommes fouiller les montagnes et les autres repaires des Indiens "
  "après plusieurs vols de bétail. À la fin de l'été, craignant des représailles après la charge des dragons de Burnside contre des "
  "Jicarillas, Judd envoie quarante des volontaires de Papin à Los Valles. Le 8 septembre, des Apaches pillent le rancho de Chaparito, "
  "à une dizaine de milles au sud ; Papin se lance à leur poursuite, divise sa troupe et laisse au sergent William Miller l'autre "
  "moitié, qui surprend le camp à minuit. Selon Myers, Papin (1817-1849), de la grande famille marchande des Chouteau, est le fils "
  "d'Alexandre Laforce Papin et de Julie Brazeau.",
  '20-21, 24',
  "Myers résume les rapports militaires (Judd à Dickerson, juin-septembre 1849) et le rôle de la compagnie de Papin (Territorial Archives "
  "of New Mexico, bobine 85). Le père, Alexandre Laforce Papin, figure parmi les fils de Joseph-Marie Papin et de Marie-Louise Chouteau "
  "(fiche BL88-10) ; le capitaine Alexander lui-même est absent du réseau. Point au fort de Barclay (près de l'actuelle Watrous), même "
  "position que HK19-03 ; Los Valles et Chaparito, plus au sud, ne sont pas localisés avec précision.")

F('02', "Santa Fe : Alexander Papin, capitaine des volontaires, tué par un nommé Wheeler (fin novembre 1849)",
  'personnage', '1849-11', -105.938, 35.687, 'a',
  ['Alexander Papin'],
  "Alexander Papin, né en 1817, petit-fils de Marie-Louise Chouteau et capitaine d'une compagnie de volontaires du Nouveau-Mexique "
  "pendant la guerre de 1849 contre les Jicarillas, est abattu à Santa Fe, à la fin de novembre 1849, par un certain Wheeler. "
  "Parmi les sources de sa note, Myers cite le Santa Fe New Mexican du 24 novembre 1849, le recensement de 1850 des comtés de San Miguel "
  "et de Taos et la généalogie de la famille Chouteau de Cunningham et Blythe (1977).",
  '24',
  "Fait tiré d'une note de Myers (note 22) : aucune précision sur le lieu exact ni sur les circonstances. Point au centre de Santa Fe.")

F('03', "Las Vegas – Independence : P. H. LeBlanc, Canadien de Santa Fe, sur le premier convoi du raccourci d'Aubry (sept.-oct. 1851)",
  'migration', '1851-09-19/1851-10-11', -105.218, 35.594, 'a',
  ['P. H. LeBlanc', 'François-Xavier Aubry', 'William Messervy', 'Charles Spencer', 'B. F. Mosely'],
  "En septembre 1851, Aubry réunit à Las Vegas, à l'est de Santa Fe, soixante-deux hommes, trente chariots et trois cents mules ; "
  "le convoi part le 19 septembre. Dans la Panhandle de l'Oklahoma, il quitte la piste et file de dix à quarante degrés à l'est du nord "
  "jusqu'à l'Arkansas, ouvrant une route de chariots bien pourvue d'eau et d'herbe qui évite la Jornada et la piste de la Cimarron. "
  "Parmi les passagers figurent William Messervy, Charles Spencer, B. F. Mosely et « P. H. LeBlanc, a French Canadian from Santa Fe ». "
  "Aubry quitte le convoi deux jours avant Independence et y arrive le 11 octobre sur sa jument Dolly.",
  '103-104',
  "Seule mention de LeBlanc chez Chaput (index : « LeBlanc, P.H: 104 »), qui cite Barry, Beginning of the West, p. 1015, 1042. "
  "Rien sur sa vie à Santa Fe. Point à Las Vegas (Nouveau-Mexique), lieu du départ ; le trajet suit le raccourci d'Aubry (fiches de "
  "l'Atlas Aubry L19, L81).", source=CHAPUT)

fiches = C.fiches

autoch = [dict(id='A-FXA-01', src='FXA-01',
    nom="Chaparito (comté de San Miguel) : Apaches jicarillas — le rancho pillé et le camp surpris par les volontaires de Papin (septembre 1849)",
    theme='evenement', date='1849-09-08/1849-09-10', lon=-105.0, lat=35.30, cert='h',
    nations=['Apaches'], aires=['Sud-Ouest'], francophones=['Alexander Papin'],
    description="Le 8 septembre 1849, une bande d'Apaches pille le rancho de Chaparito, à une dizaine de milles au sud de Los Valles, "
      "dans la guerre qui oppose les Jicarillas aux troupes américaines depuis l'été. Poursuivis par les volontaires néo-mexicains "
      "du capitaine Alexander Papin, ils se séparent ; à six milles de là, à minuit, le sergent William Miller surprend leur camp, "
      "tire deux salves et charge à la baïonnette. Cinq corps sont relevés, de nombreux blessés s'échappent ; le chef Vetrillo est tué, "
      "sa femme est capturée avec un troupeau de 150 bovins, distribué aux volontaires. Le capitaine Judd parle, le 10 septembre, "
      "d'une « brillante petite affaire ».",
    note="Myers, Wagon Tracks, février 1992, p. 21 (rapport de Judd du 10 septembre 1849). Myers écrit « Apaches » pour ce raid, dans "
      "un article consacré aux Jicarillas. Lieu hypothétique : Chaparito et Los Valles (comté de San Miguel) ne sont pas localisés "
      "précisément ; point approximatif au sud-est de Las Vegas.")]
