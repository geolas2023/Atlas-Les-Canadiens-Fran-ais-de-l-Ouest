# François-Antoine Larocque, Journal de Larocque de la rivière Assiniboine jusqu'à la rivière « aux Roches Jaunes », 1805,
# éd. L. J. Burpee, Publications des Archives canadiennes no 3, Ottawa, 1911 (PDF du Drive, dossier LAROCQUE ; archive.org journaldelarocq00laro).
# Corpus « Recherches », préfixe LR05 : l'itinéraire jour par jour du premier voyage de traite chez les Crows (2 juin - 18 octobre 1805).
# Masson (1889) ne donnait qu'une fiche générale pour ce voyage (MB-larocque-francois-antoine-pays-des-c).
from commun import Corpus
LJ = "Larocque, François-Antoine (1911), Journal de Larocque de la rivière Assiniboine jusqu'à la rivière « aux Roches Jaunes », 1805, éd. Lawrence J. Burpee, Ottawa, Archives canadiennes, publication no 3 (archive.org, journaldelarocq00laro)"
C = Corpus('Recherches', 'LR05', LJ)
F = C.F
FL = 'François-Antoine Larocque'
F('01', "Fort de la Montagne-à-la-Bosse : départ de Larocque pour les Rocheuses (2 juin 1805)", 'exploration', '1805-06-02', -100.95, 49.86, 'a', [FL, 'Charles McKenzie', 'Charles Chaboillez'],
  "Commis de la Compagnie du Nord-Ouest, François-Antoine Larocque part du fort de la Montagne-à-la-Bosse, sur l'Assiniboine, le 2 juin 1805, avec deux hommes et quatre chevaux, dont deux chargés de marchandises, pour un « voyage de découvertes aux Rocky Mountains » commandé par le bourgeois Chaboillez. Charles McKenzie l'accompagne jusqu'au Missouri. « J'avais le cœur gros en quittant le fort », écrit-il : on doutait qu'il en revienne.",
  '10-12', "Position approximative du fort, sur l'Assiniboine près de l'actuelle Virden (Manitoba).")
F('02', "Gué de la Souris : fuite de nuit devant les voleurs de chevaux (juin 1805)", 'exploration', '1805-06-04/1805-06-07', -100.93, 48.06, 'h', [FL],
  "Rencontrant un camp d'Assiniboines qui insistent pour les garder sous leurs tentes, Larocque et ses compagnons se font conduire à un bon gué de la Souris, la traversent et marchent toute la nuit dans la plaine pour échapper « aux plus habiles voleurs de chevaux » dont il ait entendu parler.",
  '13', "Selon Burpee, la Souris est traversée à son extrémité sud, là où elle se rapproche le plus du Missouri : position hypothétique près de l'actuelle Velva (Dakota du Nord).")
F('03', "La Grosse Butte : halte sur le coteau du Missouri (8 juin 1805)", 'exploration', '1805-06-08', -100.63, 47.80, 'h', [FL],
  "Le 8 juin 1805, Larocque gagne la Grosse Butte, mont élevé visible de très loin sur le coteau du Missouri, pour y faire sécher ses effets ; faute d'eau, ils avaient recueilli la pluie ruisselant le long d'un tronc d'arbre et dormi sous une tente d'écorce.",
  '14', "Identification hypothétique (Dog Den Butte).")
F('04', "Villages hidatsas de la Knife : chez le Borgne, en attendant les Crows (juin 1805)", 'commerce', '1805-06-10~/1805-06-29', -101.39, 47.33, 'a', [FL, 'Charles McKenzie', 'Le Borgne'],
  "Aux villages des Big Bellies (Hidatsas ou Minnetarees), où il avait déjà passé une partie de l'hiver précédent, Larocque cache ses marchandises et affronte les manœuvres des chefs, qui veulent le dissuader d'aller chez les Crows (« Rocky Mountain ») et garder la traite pour eux. Le 23 juin arrivent les premiers Crows ; Larocque fume avec eux chez le frère du Borgne et obtient de partir avec eux. Il quitte le village de Metaharta, sur la rive sud de la Knife, à la fin de juin.",
  '15-26', "Position aux villages de la rivière Knife (site historique national de Knife River Indian Villages).")
F('05', "Le Petit Missouri : en route avec le camp crow (juillet 1805)", 'exploration', '1805-07', -103.5, 46.9, 'h', [FL],
  "Avec le camp crow, Larocque traverse une région « très montagneuse » ; il gravit une hauteur pour voir le pays, y perd sa lunette, et campe sur des ruisseaux qui se jettent dans le Petit Missouri, pendant que les Crows chassent le bison en grand nombre.",
  '26-28', "Itinéraire approximatif à travers les badlands du Petit Missouri.")
F('06', "Rivière Powder : « si boueuse qu'elle n'est guère buvable » (27-28 juillet 1805)", 'exploration', '1805-07-27/1805-07-28', -105.41, 45.44, 'h', [FL],
  "Après avoir franchi une chaîne couverte de pins, le camp atteint la rivière Powder, au fort courant et aux immenses bancs de sable, qu'un vent du large (le chinook, selon Burpee) charge d'un sable fin qui salit l'eau : d'où son nom, disent les Crows. Larocque y achète trois peaux de castor et une peau d'ours.",
  '31-32', "Lieu de rencontre de la Powder non précisé ; position hypothétique.")
F('07', "Rivière Pine (Clear Creek) : première vue des Rocheuses, le massif du Bighorn (4-6 août 1805)", 'exploration', '1805-08-04/1805-08-06', -106.1, 44.6, 'a', [FL],
  "Le 4 août 1805, du haut des bluffs de la Powder, Larocque aperçoit à la lunette les « Rocky Mountains », assez nettement pour distinguer précipices, crevasses et arbres. Le 5, il quitte la Powder boueuse pour remonter la rivière Pine, eau claire et glacée venue des montagnes. Burpee précise que ce n'est pas la chaîne principale mais le Bighorn, et rappelle que La Vérendrye avait vu les montagnes soixante-deux ans plus tôt.",
  '34-35', "Position au pied du massif du Bighorn, vers l'actuelle Buffalo (Wyoming).")
F('08', "Gué de la Tongue au pied du Bighorn (15 août 1805)", 'exploration', '1805-08-14/1805-08-24', -107.0, 44.95, 'h', [FL],
  "Le camp longe le pied de la montagne vers le nord-ouest, franchit à gué la rivière Tongue le 15 août et campe sur la rive nord, face à une petite montagne que les Crows appellent Wolf Teeth. Larocque note ses achats (« 1 Knife, 2 Beavers… ») et la désertion de la femme du chef Spotted Crow, qui divise le camp sur la route à suivre.",
  '38-41', "Position hypothétique sur la haute Tongue.")
F('09', "Rivière aux Roches Jaunes : la grande île sous la fourche de Pryor (10-14 septembre 1805)", 'commerce', '1805-09-10/1805-09-14', -108.25, 45.85, 'a', [FL],
  "Le 10 septembre 1805, après la rivière Shot Stone, le camp atteint la Yellowstone, « belle et grande rivière » au courant très fort, et s'installe sur une grande île boisée de cinq milles de tour. Cinq Big Bellies (Atsinas) y apportent des paroles de paix et disent avoir traité l'hiver précédent avec John McDonald, le « Bras-Croche ». Le 14, ayant constaté la présence du castor et engagé les Crows à le chasser, Larocque réunit les chefs en conseil, leur promet de revenir avec des marchandises et reprend le chemin du retour.",
  '46-48', "Burpee situe l'arrivée sur la Yellowstone en aval de la fourche de Pryor (Pryor's Fork), vers les actuelles Billings et Huntley (Montana).")
F('10', "Confluent de la Yellowstone et du Missouri (30 septembre 1805)", 'exploration', '1805-09-30', -103.98, 47.98, 'c', [FL],
  "Après avoir descendu la Yellowstone, Larocque aperçoit le 30 septembre 1805, du haut d'une colline, le confluent de la rivière aux Roches Jaunes et du Missouri, puis suit le Missouri vers les villages mandans.",
  '54')
F('11', "Retour au fort de la Montagne-à-la-Bosse (18 octobre 1805)", 'exploration', '1805-10-18', -100.95, 49.86, 'a', [FL, 'Charles McKenzie'],
  "Le 18 octobre 1805, des Assiniboines annoncent que le fort de la Montagne-à-la-Bosse a été évacué et que M. Falcon se bâtit une maison pour l'hiver plus loin ; Larocque y retrouve Charles McKenzie et trois hommes. « Ainsi finit ce journal de mon voyage aux Rocky Mountains » (22 octobre). Selon Burpee, c'est la première description de la contrée des Crows depuis La Vérendrye (1742-1743).",
  '58-60')
fiches = C.fiches
