# Wayne C. Temple, Indian Villages of the Illinois Country: Historic Tribes (Springfield, Illinois State Museum,
# Scientific Papers vol. II, part 2, 1958 ; rééd.), PDF du Drive de l'auteur (fichier de plus de 10 Mo, lu en grande partie
# par l'outil du Drive). Corpus « Recherches », préfixe TP58.
from commun import Corpus
TP = "Temple, Wayne C. (1958), Indian Villages of the Illinois Country: Historic Tribes, Springfield, Illinois State Museum, Scientific Papers, vol. II, part 2"
C = Corpus('Recherches', 'TP58', TP, page_fmt='p. {}')
F = C.F
F('01', "Starved Rock : les Iroquois assiègent le fort Saint-Louis commandé par le chevalier de Baugis (21-27 mars 1684)", 'evenement', '1684-03-21/1684-03-27', -88.9940, 41.3200, 'c', ['Chevalier de Baugis', 'Henri de Tonti', 'René-Robert Cavelier de La Salle', 'Joseph-Antoine Le Febvre de La Barre'],
  "La Salle reparti au Canada en août 1683, le gouverneur La Barre envoie le chevalier de Baugis relever Tonti au fort Saint-Louis du Rocher. Le 21 mars 1684, 200 guerriers iroquois attaquent le fort et l'assiègent six jours avant de se retirer avec des pertes, poursuivis par de petits partis illinois et alliés. Les Iroquois pillent ensuite des canots français chargés de fourrures. La Barre conclut la paix avec eux en septembre 1684, sans secourir les Illinois.",
  '27-28')
F('02', "Buffalo Rock : le fort des Miamis près du fort Saint-Louis (1683-1688)", 'etablissement', '1683/1688', -88.9330, 41.3270, 'c', ['René-Robert Cavelier de La Salle', 'Pierre Deliette'],
  "Ralliés à la confédération de La Salle en 1683, les Miamis s'installent avec les Weas et les Piankashaws autour du fort Saint-Louis : 1 300 guerriers miamis, 500 weas et 150 piankashaws selon les Illinois de retour. D'après Charlevoix, certains Miamis bâtissent leur propre fort au sommet de Buffalo Rock, à l'est du Rocher. Selon Deliette, quelques-uns y sont encore en 1687 et partent l'année suivante.",
  '58')
F('03', "Lac Pimitoui (Peoria) : les Illinois quittent le Rocher et Tonti y bâtit un fort (1691-1692)", 'poste', '1691-09/1692', -89.5890, 40.6936, 'c', ['Henri de Tonti', 'Pierre Deliette'],
  "Le Rocher étant jugé indéfendable faute de bois et d'eau en cas de siège, Deliette réunit les Illinois en septembre 1691 ; ils choisissent de s'établir au lac Pimitoui, le « lac gras », riche en gibier. Pendant l'hiver 1691-1692, Tonti y construit un fort pour protéger quelque 800 guerriers. Selon Deliette, le nouveau village compte plus de 260 cabanes et six groupes : Kaskaskias, Peorias, Moingwenas, Coiracoentanons, Maroas et Tapouaras.",
  '30-31')
F('04', "Ouiatanon : les chefs weas aux noms français, de La Peau Blanche au Comte (1746)", 'personnage', '1738/1752', -86.9800, 40.4030, 'c', ['La Peau Blanche', "L'Homme Chef", 'La Petite Jarretière', 'Le Commis', 'La Teste Blanche', 'Le Comte'],
  "Alliés des Français, les Weas mènent en 1738 quatre partis de guerre contre les Chicachas, dont ils brûlent la plupart des prisonniers dans leurs villages de la Wabash. En 1746, ils comptent encore environ 600 guerriers fidèles à la France. Leurs principaux chefs portent alors des noms français : La Peau Blanche (chef de guerre), L'Homme Chef, La Petite Jarretière, Le Commis, La Teste Blanche et Le Comte. Les traiteurs britanniques de l'Ohio et de la rivière White les attirent pourtant de plus en plus.",
  '67-68')
F('05', "Vincennes : après la mort du sieur de Vincennes, les Piankashaws quittent Chippekawkay (1736-1746)", 'etablissement', '1734/1746', -87.5285, 38.6773, 'c', ['François-Marie Bissot de Vincennes', 'Louis Groston de Saint-Ange', 'Simon Réaume', "L'Enfant"],
  "En 1734, Vincennes tente d'attirer à son poste, qu'il appelle le fort des Piankashaws, le groupe établi sur la rivière Vermilion ; en 1735, il pousse les Piankashaws à prendre la hache contre les Chicachas. Il est tué au combat en mai 1736. Les Piankashaws abandonnent aussitôt Chippekawkay, dit le Petit Ouiatanon : en 1737, il ne reste que quinze à vingt-cinq guerriers près du poste. Saint-Ange y demeure ; en 1746 on y compte une quarantaine de Blancs et cinq Noirs, tandis que les Piankashaws vivent sur la Vermilion sous le chef L'Enfant.",
  'chap. « Piankashaw »')
F('06', "Vincennes : les chefs piankashaws La Mouche Noire, Maringouin, Le Petit Castor et Grelot vendent des terres à la Wabash Land Company (18 octobre 1775)", 'evenement', '1775-10-18', -87.5285, 38.6773, 'c', ['Tobacco', 'Montour', 'La Grand Couette', 'La Mouche Noire', 'Maringouin', 'Le Petit Castor', 'Grelot'],
  "Leur chasse menacée par l'arrivée des colons, les Piankashaws cèdent une partie de leurs terres à la Wabash Land Company le 18 octobre 1775. Parmi les signataires figurent Tobacco et son fils, Montour, La Grand Couette, La Mouche Noire, Maringouin, Le Petit Castor, Grelot et Grelot fils. En 1778, après le serment des habitants français de Vincennes aux Américains (20 juillet), Tobacco signe un traité avec le capitaine Leonard Helm (7 août).",
  'chap. « Piankashaw »')
fiches = C.fiches
