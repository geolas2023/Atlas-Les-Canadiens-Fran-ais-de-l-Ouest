# Harold P. Howard, Sacajawea, Norman, University of Oklahoma Press, 1971.
# PDF du Drive de l'auteur (HISTOIRE_LIVRES/AUTOCHTONES), relu en entier le 19 novembre 2026. Préfixe HO71.
# L'expédition, le fort Manuel, Toussaint et Jean-Baptiste Charbonneau sont déjà largement couverts (F-charbonneau, R012, OT76) ;
# seules les informations absentes sont retenues.
from commun import Corpus
S = "Howard, Harold P. (1971), Sacajawea, Norman, University of Oklahoma Press"
C = Corpus('Recherches', 'HO71', S, page_fmt='p. {}')
F = C.F
F('01', "Saint-Louis : Luttig puis Clark tuteurs de Lizette et de « Toussaint » Charbonneau (août 1813)", 'personne', '1813-06/1813-08', -90.19, 38.627, 'c', ['John C. Luttig', 'William Clark', 'Lizette Charbonneau', 'Jean-Baptiste Charbonneau'],
  "À l'abandon du fort Manuel, au printemps 1813, le commis John Luttig emmène la petite fille que Sacagawea a laissée en mourant, Lizette. Arrivé à Saint-Louis en juin, il demande en août au tribunal la tutelle de Lizette et d'un garçon d'environ dix ans appelé « Toussaint » ; dans le registre, son nom est ensuite rayé et remplacé par celui de William Clark. Howard pense que ce « Toussaint » est en fait Jean-Baptiste. Luttig meurt en 1815.",
  '161, 170', "")
F('02', "Westport (Missouri) : baptême de Victoire, fille de Joseph Vertifeuille et d'Elizabeth Carboneau, peut-être Lizette (23 avril 1843)", 'personne', '1843-04-23', -94.59, 39.05, 'h', ['Joseph Vertifeuille', 'Elizabeth Carboneau', 'Lizette Charbonneau'],
  "On ne sait ce qu'est devenue Lizette, la fille de Sacagawea et de Toussaint Charbonneau. Le 23 avril 1843, une fillette nommée Victoire, fille de Joseph Vertifeuille et d'Elizabeth Carboneau, est baptisée à Westport ; Howard juge « au moins possible » que la mère soit Lizette.",
  '162', "Identification conjecturale.")
F('03', "Fort Lupton : un engagé français tué le 4 juillet, sa veuve shoshone part avec Frémont (juillet 1843)", 'evenement', '1843-07-04/1843-07-18', -104.81, 40.08, 'a', ['John Charles Frémont'],
  "Frémont rapporte qu'un engagé français du fort Lupton a été tué d'une balle dans le dos le 4 juillet 1843. Sa veuve, une Indienne de la nation des Serpents, demande à suivre l'expédition jusqu'à la rivière aux Ours pour rejoindre les siens ; elle part avec ses deux enfants métis, cinq ou six chevaux de bât et une petite tente que Frémont lui donne, et quitte la troupe le 18 juillet près de la Ham's Fork, espérant trouver des Shoshones au nouveau fort Bridger. Grace Raymond Hebard voyait en elle Sacagawea revenant chez son peuple.",
  '177', "Le nom de l'engagé n'est pas donné. L'identification à Sacagawea relève de la tradition rapportée par Hebard.")
F('04', "Réserve de Wind River (Fort Washakie) : la tradition shoshone d'une Sacagawea morte en 1884", 'personne', '1884', -108.88, 43.0, 'h', ['Sacagawea', 'Toussaint Charbonneau', 'John Roberts', 'Grace Raymond Hebard', 'Charles A. Eastman'],
  "Selon la tradition recueillie par Grace Raymond Hebard et Charles A. Eastman, Sacagawea, battue par Charbonneau qui avait pris une jeune épouse ute, l'aurait quitté, aurait vécu chez les Comanches, puis serait revenue chez les Shoshones, retrouvant son fils Baptiste et son fils adoptif Bazil. Le révérend John Roberts présida en 1884 aux funérailles d'une vieille femme qu'il croyait être Sacagawea. Howard oppose à ce récit le journal de Luttig, qui note sa mort au fort Manuel en décembre 1812.",
  '162, 175-178', "Tradition orale contestée.")
fiches = C.fiches
