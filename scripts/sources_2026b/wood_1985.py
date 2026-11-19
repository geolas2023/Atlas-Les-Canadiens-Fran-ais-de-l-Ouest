# W. Raymond Wood et Thomas D. Thiessen (éd.), Early Fur Trade on the Northern Plains: Canadian Traders among the Mandan and
# Hidatsa Indians, 1738-1818 (1985), PDF du Drive de l'auteur (dossier FUR_TRADE_USA). Corpus « Recherches », préfixe WT85 :
# les Canadiens résidents (« residenters ») des villages mandans et hidatsas, d'après l'introduction des éditeurs.
from commun import Corpus
WT = "Wood, W. Raymond et Thomas D. Thiessen (éd.) (1985), Early Fur Trade on the Northern Plains: Canadian Traders among the Mandan and Hidatsa Indians, 1738-1818, Norman, University of Oklahoma Press"
C = Corpus('Recherches', 'WT85', WT)
F = C.F
J = 'René Jusseaume'
F('01', "Village awatixa (site Sakakawea) : Ménard, premier Blanc établi chez les Hidatsas (v. 1778)", 'personnage', '1778~/1804', -101.388, 47.326, 'a', ['Ménard'],
  "Le premier Euro-Américain connu à s'établir à demeure dans les villages mandans et hidatsas est un Canadien nommé Ménard, dont le prénom s'est perdu (François ou Pierre selon des éditeurs plus tardifs). Six témoins le disent arrivé entre 1778 et 1783 ; il vit dans le village aujourd'hui appelé site Sakakawea, avec une femme indienne « belle et gracieuse », et David Thompson le juge « en tout point comme un indigène ». Onze sources contemporaines (D'Église, Truteau, Collot, Thompson, Larocque, McKenzie, Tabeau, Clark, Henry…) puisent chez lui leur savoir sur le haut Missouri : il connaît la Yellowstone et les Rocheuses, et a visité plusieurs fois les Crows avec les Hidatsas. Il est tué en revenant de l'Assiniboine, au grand regret du maître de Brandon House.",
  '43-46', "Position au site Sakakawea, sur la Knife (Knife River Indian Villages).")
F('02', "Les « residenters » canadiens des villages de la Knife (années 1790-1810)", 'etablissement', '1790~/1818', -101.39, 47.33, 'a', ['Ménard', J, 'Cardin', 'Jean-Baptiste Lafrance', 'Toussaint Charbonneau', 'François La Grave', 'Joseph Garreau', 'Chayé', 'Hugh Heney'],
  "Wood et Thiessen dressent la liste des résidents libres des villages mandans et hidatsas cités dans les papiers des compagnies : Cardin, La France, Toussaint Charbonneau, La Grave, « Chayé », Ménard, Joseph Garreau, René Jusseaume, ainsi que McCracken, Colter, Heney, Morgan, Holmes et Taylor. Plusieurs sont des déserteurs de la Compagnie du Nord-Ouest ou de Prairie du Chien : John Macdonell traite de « canaille » La Grave, Garreau et Chayé. Ils vivent de la revente de chevaux, de robes et de loups aux postes de l'Assiniboine.",
  '43, 50')
F('03', "Fort Espérance (Qu'Appelle) : première mention de Jusseaume et Cardin (13 avril 1794)", 'commerce', '1794-04-13', -101.67, 50.45, 'a', [J, 'Cardin', 'John Macdonell'],
  "La plus ancienne mention de René Jusseaume est l'entrée du journal de John Macdonell du 13 avril 1794 : lui et Cardin arrivent au fort Espérance avec un parti de la Compagnie du Nord-Ouest revenant du Missouri. Thompson dit qu'il vit dans les villages depuis 1789 ou 1790 ; Alexander Henry, en 1806, « depuis plus de quinze ans ».",
  '46 et n. 98', "Position approximative du fort Espérance, sur la Qu'Appelle près de l'actuelle Rocanville (Saskatchewan).")
F('04', "Poste de Jusseaume (« fort Makay ») entre les villages mandans et hidatsas (1794-1797)", 'poste', '1794-10-27/1797-05', -101.36, 47.30, 'h', [J, 'John Evans'],
  "Parti de la rivière la Souris le 17 octobre 1794, Jusseaume conduit une expédition de la Compagnie du Nord-Ouest qui élève, peu après son arrivée au Missouri le 27 octobre, « un petit fort et une cabane » sur la rive entre les villages mandans et hidatsas : le seul bâtiment construit par les traiteurs canadiens. En septembre 1796, l'explorateur John Evans s'en empare au nom de l'Espagne et le rebaptise fort Makay ; Jusseaume tente de le tuer.",
  '28, 46-49', "Position hypothétique sur la rive du Missouri près de l'embouchure de la Knife.")
F('05', "Villages mandans : David Thompson guidé par Jusseaume (hiver 1797-1798)", 'exploration', '1797-12/1798-01-22', -101.33, 47.28, 'a', [J, 'David Thompson', 'Joseph Boisseau', 'Alexis Vivier', 'Pierre Gilbert', 'François Perrault', 'Toussaint Vaudril', 'Louis-Jean-Baptiste Houle', 'Jean-Baptiste Minie'],
  "Jusseaume sert de guide et d'interprète à l'expédition de David Thompson aux villages mandans, avec Joseph Boisseau (domestique de Thompson), Hugh McCracken, Alexis Vivier, Pierre Gilbert, François Perrault, Toussaint Vaudril, Louis-Jean-Baptiste Houle et Jean-Baptiste Minie. Le 9 janvier 1798, Thompson reçoit de Jusseaume des peaux de loup et 48 robes de bison.",
  '57, 59, 97 et n. 8')
F('06', "Rivière Grand : Jusseaume blessé par les Arikaras (1807)", 'evenement', '1807-09', -100.47, 45.55, 'a', [J, 'Shahaka', 'Nathaniel Pryor', 'Pierre Chouteau'],
  "En 1807, l'expédition de Nathaniel Pryor et de Pierre Chouteau, chargée de ramener chez lui le chef mandan Shahaka (Big White), revenu de Washington, est repoussée à coups de fusil par les Arikaras près de la rivière Grand et doit rentrer à Saint-Louis. René Jusseaume, l'interprète de Big White, est blessé.",
  '31', "Position aux villages arikaras de l'embouchure de la Grand (Dakota du Sud).")
fiches = C.fiches
