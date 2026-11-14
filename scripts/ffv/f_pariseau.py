from commun import *
A = "Harriet D. Munnick"
def s(p, n=None): return ff(A, p, n)
P = dict(id="pariseau", nom="Pierre Pariseau", auteur=A, pages="253-257", vie="v. 1793-1892",
 chapeau="L'engagé type : vingt ans au service de la Compagnie de la Baie d'Hudson, dont onze au fort Umpqua, puis quarante ans de vie retirée dans les vallées de la Little River, en Oregon. Son nom survit sous la forme « Parazoo ».")
E = [
("Montréal : enfance (né v. 1793)", -73.567, 45.501, 1793.0, 1810.0, "1793~", "hypothetique", "Origines",
 "Fils de Jean-Baptiste Pariseau et de Françoise Alarie, né vers 1793, peut-être en France selon la tradition familiale, et amené jeune à Montréal.",
 s(253), "Lieu de naissance incertain (France ou Bas-Canada)."),
("État de New York : à la dérive sous Jackson (1829-1832)", -75.5, 43.0, 1829.2, 1832.0, "1829/1832", "hypothetique", "Origines",
 "Il disait lui-même être « descendu » dans l'État de New York sous la présidence d'Andrew Jackson, avant de rejoindre sans doute une expédition de traite vers l'ouest.",
 s(253), "Point placé au centre de l'État."),
("Fort Vancouver : engagé de la Compagnie de la Baie d'Hudson (1832)", -122.661, 45.626, 1832.0, 1832.5, "1832", "certaine", "Fort Umpqua",
 "En 1832, il est au service de la CBH dans le pays de l'Oregon et part aussitôt vers le sud pour aider à bâtir un fort sur l'Umpqua.",
 s(253), None),
("Fort Umpqua : onze ans d'isolement (1832-1850)", -123.567, 43.633, 1832.5, 1850.0, "1832/1850", "certaine", "Fort Umpqua",
 "Trois bâtiments dans une palissade de douze pieds, deux blockhaus en diagonale : la maison du traiteur Jean-Baptiste Garnier et de sa famille, celle des engagés (dont Pariseau) et l'entrepôt. Dans l'enceinte poussent des pommiers venus de Fort Vancouver ; une enfant de pionniers se souviendra que jamais pommes n'eurent meilleur goût. On y cultive une quarantaine d'acres, on pêche le saumon aux rapides. Michel Laframboise y passe avec la brigade de Californie ; un détachement de l'expédition Wilkes s'y arrête en 1841 et le lieutenant Emmons en dresse le plan.",
 s(254, "texte de la plaque « Fort Umpqua - Douglas County History » ; Mrs. S. A. Long, « Mrs. Jesse Applegate », OHQ ix (1908), p. 181 ; plan d'Emmons, Coe Collection, Yale, reproduit dans The Umpqua Trapper, II, no 2 (1966)"),
 "Les pommiers, ou leurs rejets, marquent encore le site dans une prairie de la rive sud."),
("Champoeg : il vote « non » (2 mai 1843)", -122.874, 45.249, 1843.33, 1843.34, "1843-05-02", "certaine", "Fort Umpqua",
 "Seule mention de Pariseau dans les sources de l'époque : à l'assemblée de Champoeg, il vote contre la formation d'un gouvernement provisoire, comme la plupart des employés de la CBH mobilisés contre le projet américain. Il n'était que de passage, en route vers Fort Vancouver.",
 s(255), None),
("Prairie française : ferme et mariage avec Marie Dompierre (1850)", -122.87, 45.18, 1850.0, 1853.0, "1850/1853", "certaine", "Prairie française",
 "Le recensement de 1850 le dit « fermier, sans famille ». Il prend une demi-section à cinq milles au sud de Champoeg. Il épouse Marie Dompierre, 16 ans, fille de David Dompierre et de Marguerite Soulier, d'ascendance crie ; il en a 53 et renoue avec le catholicisme de son enfance.",
 s(255, "St. Paul Mission Record (photostat), 8 juillet 1850"), "Il ne fait pas valider sa concession (Donation Land Claim) ; citoyen américain seulement en 1864."),
("Mission Saint-Paul : baptêmes de Pierre et Louis", -122.976, 45.211, 1850.5, 1853.0, "1850/1853", "certaine", "Prairie française",
 "Ses fils Pierre et Louis sont inscrits aux registres de la mission de Saint-Paul.", s(256), None),
("Haute Little River (comté de Douglas) : quarante ans de retraite sauvage", -122.95, 43.24, 1853.0, 1892.06, "1853/1892", "approximative", "Little River",
 "Il quitte la Prairie pour les petites vallées de l'Umpqua, où d'autres Canadiens et Métis ont laissé leurs noms aux ruisseaux et aux sommets. Neuf autres enfants naissent. Il vend ses peaux au magasin du village comme jadis au magasin de la compagnie : « il n'avait jamais quitté le fort Umpqua ». Marie, devenue veuve, refusera de reparler des montagnes. Un historien dira de sa photographie qu'il a « le regard des aigles ».",
 s(256, "Elsie Pfieffer, petite-fille, à l'auteure, 1966 ; George B. Abdill, 1966"), None),
("Portland : patient rebelle à l'hôpital (années 1870-1880)", -122.676, 45.523, 1873.0, 1882.0, "1873/1882", "approximative", "Little River",
 "Octogénaire, malade, il est conduit à l'hôpital de Portland, à deux cents milles. Au bout de deux semaines, il annonce qu'il rentrera à pied si personne ne vient le chercher : il ne veut plus être « en cage ».",
 s(257), None),
("Nofog : mort et cimetière perdu (21 janvier 1892)", -123.0, 43.27, 1892.05, 1892.06, "1892-01-21", "approximative", "Little River",
 "Quelques jours avant sa mort, il fait huit milles sur une route boueuse et laisse ses pièges tendus dans les bois. Il s'endort sur sa chaise, dort trois jours et ne se réveille pas, à 96 ans environ. Inhumé au petit cimetière de Nofog, dont le site, recouvert puis coupé par l'exploitation forestière, est aujourd'hui perdu ; ses descendants écrivent « Parazoo ».",
 s(257, "nécrologie anonyme, Scrap Book no 35, p. 43, Oregon Historical Library"), "Emplacement de Nofog estimé dans le bassin de la Little River."),
]
INEDITS = [
 "St. Paul Mission Record, 8 juillet 1850 (mariage Pariseau × Dompierre) ; publié dans Catholic Church Records of the Pacific Northwest (Munnick, éd.).",
 "Recensements de 1850 (Marion County) et 1860-1880 (Douglas County, Oregon).",
 "Naturalisation de 1864 (cour du comté de Douglas).",
 "Scrap Book no 35, p. 43, Oregon Historical Society Library : nécrologie de 1892.",
 "Registres de la CBH (HBCA, Winnipeg) : contrats et comptes de Pierre Pariseau, 1832-1852 ; journaux du fort Umpqua.",
]
