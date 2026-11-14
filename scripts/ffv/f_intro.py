from commun import *
A = "Janet Lecompte"
def s(p, n=None): return ff(A, p, n)
P = dict(id="intro", nom="Introduction : le monde français de la traite", auteur=A, pages="9-26", vie="1763-1865",
 chapeau="Lecompte rappelle que les « Français » formaient environ les quatre cinquièmes des hommes de la traite américaine, à tous les niveaux, et démonte les stéréotypes (voyageur joyeux, servile et poltron) hérités d'Irving et de Chittenden. Cet onglet localise les faits collectifs qu'elle évoque.")
E = [
("Saint-Louis : fondation par les créoles de La Nouvelle-Orléans (1764)", *STL, 1764.0, 1803.99, "1764/1803", "certaine", "Contexte",
 "Fondée en 1764 par des créoles et coloniaux venus de La Nouvelle-Orléans, dont le grand-père d'Auguste-Pierre Chouteau. Quarante ans de régime espagnol si léger qu'il ne laisse aucune trace sur la culture française ; la traite est la seule affaire de la ville. Les Chouteau, Sarpy, Papin, Robidoux, St. Vrain et Pratte s'allient par mariages et faveurs.",
 s(14, "W. E. Foley et C. D. Rice, The First Chouteaus (1983), p. 1-12 ; J. Lecompte, « Don Benito Vasquez in Early St. Louis », Bulletin MHS xxv (1970)"), None),
("Fort Union : « presque tous français » (1832)", -104.04, 47.999, 1830.0, 1832.99, "1830/1832", "certaine", "Contexte",
 "George Catlin écrit en 1832 que les hommes de Fort Union sont presque tous français. Les contrats de 1830 étudiés par William Swagerty montrent que 81 % de l'Upper Missouri Outfit sont des voyageurs, majoritairement à nom français, comme près des deux tiers des commis-traiteurs. Chittenden estimait qu'au moins quatre cinquièmes des quelque cinq mille hommes de la traite américaine étaient canadiens-français ou créoles.",
 s(11, "G. Catlin, Letters and Notes (1844), I, p. 35 ; Chittenden, The American Fur Trade (1902), I, p. 56 ; W. R. Swagerty, « A View from the Bottom Up », Montana 43/1 (1993), p. 20-25"), None),
("North Platte : la « race mêlée » des trappeurs selon Parkman (1846)", -103.5, 41.6, 1846.4, 1846.6, "1846", "approximative", "Contexte",
 "Parkman décrit les trappeurs des Rocheuses rencontrés sur la North Platte comme des hommes à demi sauvages, tous d'origine canadienne, où le sang français prédomine.",
 s(11, "Parkman, The Oregon Trail (1894), p. 64, 70"), None),
("Quais de Manhattan : le canot d'écorce des voyageurs (1811)", -74.012, 40.703, 1811.0, 1811.99, "1811", "certaine", "Stéréotypes",
 "Astor, parmi la foule, voit accoster un canot d'écorce avec huit voyageurs coiffés de plumes qui chantent ; deux d'entre eux le chargent sur l'épaule et l'emportent. Astor aurait dit que six Américains n'en feraient pas autant — à l'inverse du mot qu'Irving lui prête (un Américain vaut trois Canadiens).",
 s(21, "Alexander Ross, Adventures of the First Settlers, dans Thwaites, Early Western Travels vii, p. 42-43 ; Irving, Bonneville (1961), p. 19"), None),
("Santa Fe : la piste ouverte par le Lyonnais Pierre Vial", *SANTAFE, 1786.0, 1821.0, "1786/1821", "certaine", "Contexte",
 "La piste de Santa Fe a été ouverte par Pierre (Pedro) Vial, Français de Lyon. Après l'indépendance mexicaine (1821), les caravanes amènent muletiers, traiteurs, médecins et mineurs français qui s'établissent au Nouveau-Mexique.",
 s(15, "N. M. Loomis et A. P. Nasatir, Pedro Vial and the Roads to Santa Fe (1967), p. xv"), None),
("Nouveau-Mexique : plus de cinquante Français baptisés (1820-1850)", *TAOS, 1820.0, 1850.0, "1820/1850", "certaine", "Contexte",
 "Fray Angélico Chávez relève plus de cinquante noms français dans les registres de baptême du Nouveau-Mexique ; d'autres, en union libre, échappent aux registres mais paraissent au recensement de 1850. Des trappeurs fondent ou peuplent Taos, Mora, Tecolote et Cimarron.",
 s(25, "Chávez, « New Names in New Mexico », El Palacio 64 (1957), p. 292-318, 367-380"), None),
("Prairie française : 121 voyageurs à la retraite", -122.93, 45.18, 1830.0, 1850.0, "1830/1850", "certaine", "Contexte",
 "La plus grande colonie de Français retraités de la traite : 121 anciens, surtout de vieux voyageurs avec leurs familles indiennes, sur la Willamette entre Salem et Portland. Harriet Munnick a recensé 150 à 200 anciens de la CBH et trappeurs libres dans le Nord-Ouest.",
 s(25, "J. N. Barry, The French Canadian Pioneers of the Willamette Valley (1933), p. 1-13 ; H. Munnick, Church Records of the Pacific Northwest (1982-1987)"), None),
("Bent's Fort : les « fines girations » des Français au bal (1846)", *BENT, 1846.5, 1846.99, "1846", "certaine", "Stéréotypes",
 "Dans le mélange de pas d'un bal multiculturel, Garrard distingue la danse de guerre, le galop, le piétinement du Missourien et les « girations plus délicates » du Français. Il admire aussi les chansons « belles et piquantes » des muletiers canadiens de la piste de Santa Fe.",
 s(20, "L. H. Garrard, Wah-To-Yah and the Taos Trail (1938), p. 54, 64, 129"), None),
("Pigeon's Ranch, près de Pecos : le danseur Alexandre Vallé", -105.78, 35.58, 1850.0, 1862.0, "185X", "certaine", "Stéréotypes",
 "Le Français Alexandre Vallé, tenancier d'un relais de diligence sur la piste de Santa Fe, doit son surnom de « Pigeon » au pas d'« aile de pigeon » qu'il dansait.",
 s(21, "Marc Simmons, Following the Santa Fe Trail (1984), p. 196-197"), None),
("Hardscrabble : la lettre d'Alexander Barclay (déc. 1845)", -105.083, 38.262, 1845.9, 1846.0, "1845-12", "certaine", "Stéréotypes",
 "Barclay écrit que leurs besoins sont peu nombreux et que, sans luxe chez les voisins, nul n'éprouve d'envie ; mais il se décrit aussi en héros de Fenimore Cooper, alors que son journal de 1845-1850 respire surtout le labeur et l'ennui.",
 s(23, "Barclay à George Barclay, rivière Arkansas, déc. 1845, Barclay Papers, Bancroft Library"), None),
]
INEDITS = [
 "Contrats d'engagement et livres de salaires de l'Upper Missouri Outfit, 1830-1836, Chouteau Collection, MHS (Swagerty et Wilson : la plupart des engagés n'étaient pas endettés).",
 "Recensement territorial du Nouveau-Mexique de 1850 (manuscrit) : noms français, y compris dans le futur Colorado.",
 "Journal et lettres d'Alexander Barclay (1845-1850), Bancroft Library.",
 "H. Munnick, Catholic Church Records of the Pacific Northwest : dépouillement nominatif des familles de la Prairie française.",
]
