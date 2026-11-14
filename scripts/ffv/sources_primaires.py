# Étapes ajoutées après consultation en ligne de sources primaires citées dans les notes du livre.
# (nom, lon, lat, debut, fin, edtf, certitude, phase, description, source, note)
FRE = "J. C. Frémont, Report of the Exploring Expedition to the Rocky Mountains in the Year 1842, and to Oregon and North California in the Years 1843-44 (1845) ; texte consulté sur Project Gutenberg, ebook no 9294"
LUT = "John C. Luttig, Journal of a Fur-Trading Expedition on the Upper Missouri, 1812-1813, éd. S. M. Drumm (1920) ; texte consulté en ligne (Mountain Men digital library, D. Rudy)"
RUX = "G. F. Ruxton, Life in the Far West (Édimbourg, 1849) ; texte consulté sur Project Gutenberg, ebook no 55093"
PARK = "F. Parkman, The Oregon Trail (éd. 1892), chap. VI et IX-X ; texte consulté sur Wikisource"
PCH = "Placer County Historical Society, notice « Jean Baptiste Charbonneau » ; comté de Placer, bulletin du patrimoine ; lewis-clark.org, « Jean Baptiste's Final Journey » (consultés en ligne)"
SP = "Source primaire consultée en ligne : "
ADD = {
 'leduc': [
  ("Fountain Creek : les bisonneaux parmi le bétail de Maurice (13 juillet 1843) — vérification", -104.69, 38.52, 1843.531, 1843.532, "1843-07-13", "certaine", "Pueblo, Hardscrabble, San Gerónimo",
   "Vérification dans le texte de Frémont : la veille de l'arrivée au Pueblo, sur la Fontaine-qui-bouille, l'expédition passe le campement d'un chasseur nommé Maurice, parti dans les plaines à la poursuite de bisonneaux ; Frémont voit des petits bisons mêlés à son bétail domestique. Le lendemain (14 juillet), il décrit le « pueblo » de l'embouchure, où des montagnards mariés à des Mexicaines cultivent la terre.",
   SP+FRE+", entrées des 12-14 juillet 1843", "Confirme la notice de Lecompte (p. 184) ; Frémont n'écrit pas le nom de famille."),
  ("Bijou Creek : « Maurice » dans le roman de Ruxton", -104.05, 39.85, 1846.8, 1849.0, "1849 (récit)", "hypothetique", "Mémoire",
   "Dans Life in the Far West, un trappeur francophone nommé Maurice, au camp de la Bijou, signale une centaine d'Indiens près de Squirrel Creek, dont un parti de guerre à pied venu voler des chevaux, et suppose des Utes dans le Bayou Salade ; il parle le patois des voyageurs. Ruxton connut LeDuc au Pueblo en 1846-1847.",
   SP+RUX+", chap. I-II", "Récit romancé ; lieu du camp fictionnel placé sur la Bijou."),
 ],
 'charbonneau': [
  ("Fort Manuel : mort de la « squaw serpent » de Charbonneau, Sacagawea (20 déc. 1812)", -100.65, 45.93, 1812.96, 1812.97, "1812-12-20", "certaine", "Saint-Louis et l'Europe",
   "Le commis Luttig note le 20 décembre 1812 la mort de fièvre putride de l'épouse serpent (shoshone) de Charbonneau, qui laisse une petite fille ; l'entrée est généralement identifiée à la mort de Sacagawea, mère de Jean-Baptiste, alors à Saint-Louis chez Clark. Le 17 septembre précédent, Toussaint Charbonneau avait donné l'alerte au fort après la mort de Lecomte, tué par des Crows.",
   SP+LUT+", entrées des 17 sept. et 20 déc. 1812", "Identification à Sacagawea débattue (thèse concurrente : mort à Wind River en 1884)."),
  ("Fort St. Vrain / île Sainte-Hélène : les chevaux égarés du camp de Chabonard (9 juillet 1842)", -103.82, 40.26, 1842.52, 1842.53, "1842-07-09", "certaine", "Trappeur",
   "Frémont apprend en route qu'une bande de chevaux s'est échappée d'un camp « à la charge de M. Chabonard », puis trouve celui-ci installé pour l'été sur l'île qu'il a nommée Sainte-Hélène.",
   SP+FRE+", entrée du 9 juillet 1842", None),
  ("Comté de Placer : guide de l'arpenteur du comté (1852)", -121.08, 38.90, 1852.0, 1852.99, "1852", "certaine", "Californie",
   "En 1852, le conseil des superviseurs du comté de Placer lui verse 48 $ pour avoir guidé l'arpenteur du comté. Il signe une pétition à Rattlesnake Bar contre l'élection d'un sénateur, adresse une pétition au conseil des superviseurs en juin 1857 et figure en mai 1865 au rôle des taxes de Rocklin.",
   SP+PCH, None),
  ("Rattlesnake Bar (American River) : la pétition", -121.10, 38.79, 1852.0, 1857.5, "185X", "approximative", "Californie",
   "Signature d'une pétition à Rattlesnake Bar contre l'élection d'un sénateur des États-Unis.", SP+PCH, "Lieu-dit minier aujourd'hui noyé par le lac Folsom."),
  ("Rocklin : au rôle des taxes (mai 1865)", -121.235, 38.79, 1865.33, 1865.42, "1865-05", "certaine", "Californie",
   "Il figure au rôle d'évaluation fiscale de Rocklin en mai 1865, un an avant son départ pour le Montana.", SP+PCH, None),
  ("Rivière Owyhee : la chute dans l'eau glacée (mai 1866)", -117.45, 42.85, 1866.35, 1866.37, "1866-05", "approximative", "Californie",
   "Selon les études récentes, il tombe dans la rivière Owyhee en la franchissant et contracte une pneumonie ; ses compagnons le portent au relais suivant, Inskip, en espérant sa guérison, à peu de distance des mines de Ruby (Silver City, Idaho).",
   SP+PCH, "Point placé au passage probable de l'Owyhee."),
  ("Old Town Auburn : la plaque commémorative (2006, révisée en 2020)", -121.077, 38.90, 1974.0, 2020.0, "1974 ; 2006 ; 2020", "certaine", "Mémoire",
   "La pierre tombale de Danner, « 1805 – 1866 », est posée par le chapitre Malheur des Filles de la Révolution américaine le 6 août 1974 ; la société historique du comté de Placer pose une plaque à Auburn le 10 décembre 2006, révisée en 2020.",
   SP+PCH, None),
 ],
 'bordeaux': [
  ("Fort Laramie : « Mr. Boudeau » reçoit Frémont (13-21 juillet 1842) — vérification", -104.553, 42.205, 1842.53, 1842.56, "1842-07-13/1842-07-21", "certaine", "Fort Laramie",
   "Frémont écrit « Boudeau » : il commande le fort avec les commis Galpin et Kellogg et une quinzaine d'hommes, presque tous mariés à des Indiennes ; il vient d'acheter une trentaine de têtes de bétail aux émigrants. Le 21 juillet, des chefs sioux et cheyennes forcent la porte de la pièce pour retenir l'expédition.",
   SP+FRE+", entrées de juillet 1842", None),
  ("Fort Laramie : la longue-vue et Marie (juin 1846) — Parkman", -104.556, 42.201, 1846.45, 1846.5, "1846-06", "certaine", "Fort Laramie",
   "Parkman loge dans la meilleure pièce du fort, celle du bourgeois Papin, en l'absence duquel commande Bordeaux ; à l'arrivée d'un camp indien, Bordeaux crie à sa femme Marie d'apporter sa longue-vue et grimpe sur le mur.",
   SP+PARK, None),
 ],
 'papin': [
  ("Sur la Platte : « Voici le vieux Papin et Frédéric ! » (juin 1846) — Parkman", -101.9, 41.13, 1846.42, 1846.44, "1846-06", "approximative", "Fort Laramie",
   "Le guide Henry Chatillon annonce l'arrivée de Papin, « bourgeois » de Fort Laramie, et de Frédéric ; la flottille, partie depuis un mois, se hâte car la rivière baisse chaque jour.",
   SP+PARK+", chap. VI", None),
 ],
 'mstvrain': [
  ("Fort St. Vrain : chevaux, mules et un Espagnol pour Frémont (10-12 juillet 1842)", -104.852, 40.285, 1842.52, 1842.53, "1842-07-10/1842-07-12", "certaine", "Fort St. Vrain",
   "Frémont est reçu par M. St. Vrain « avec beaucoup de bonté et d'hospitalité » ; grâce à lui, il obtient deux chevaux et des mules et engage un Espagnol du poste. L'année suivante (23-26 juillet 1843), l'expédition s'y regroupe avec Fitzpatrick et Kit Carson y arrive avec dix mules.",
   SP+FRE+", entrées des 10-12 juillet 1842 et 23-26 juillet 1843", "Frémont ne donne pas le prénom ; Marcellin dirigeait alors le fort."),
 ],
}
# Nouvelles traces francophones (corpus Recherches) tirées de ces sources
# (nom, lon, lat, d, f, edtf, prec, cert, pers, desc, src, note, theme)
R_ADD = [
 ("Poste de Cyprien Chouteau sur la Kansas : les Canadiens de Frémont (juin 1842)", -94.70, 39.08, 1842.42, 1842.45, "1842-06", "mois", "certaine",
  "Clément Lambert; Basile Lajeunesse; Baptiste Bernier; Honoré Ayot; François La Tulipe; Louis Ménard; Lucien Maxwell; Cyprien Chouteau",
  "Frémont organise sa première expédition au poste de Cyprien Chouteau, sur la rive droite de la Kansas, à dix milles de l'embouchure. Parmi les vingt et un hommes engagés à Saint-Louis : Lambert, L'Espérance, Lefèvre, Potra, Gouin, Dumes, Lajeunesse, Tessier, Cadotte, Clément, Benoit, Bernier, Ayot, La Tulipe, Badeau, Ménard, Ruelle, Chardonnais, Janisse, Proue. Le 14 juin, Basile Lajeunesse franchit la Kansas en crue à la nage, la corde du bateau entre les dents.",
  "Source primaire consultée en ligne : "+FRE+", juin 1842", "Lucien Maxwell, de Kaskaskia, est le chasseur de l'expédition.", "exploration"),
 ("Fort Platte : Joseph Bissonette et la lettre de L. B. Chartrain (21 juillet 1842)", -104.55, 42.215, 1842.53, 1842.58, "1842-07-21", "jour", "certaine",
  "Joseph Bissonette; L. B. Chartrain",
  "Au fort Platte de Sibille, Adams & Co., bâti en terre et inachevé, le traiteur Joseph Bissonette, qui parle couramment le sioux, adresse à Frémont une lettre écrite par L. B. Chartrain : ne pas partir avant le retour des guerriers sioux et cheyennes (chefs Otter Hat, Breaker of Arrows, Black Night, Bull's Tail). Il accompagne l'expédition jusqu'aux Red Buttes.",
  "Source primaire consultée en ligne : "+FRE+", 15-21 juillet 1842", None, "poste"),
 ("Red Buttes : « Le meilleur avis » de Bissonette (28 juillet 1842)", -106.47, 42.78, 1842.57, 1842.58, "1842-07-28", "jour", "approximative",
  "Joseph Bissonette",
  "Près des Red Buttes, Bissonette conseille à Frémont, en français, de rebrousser chemin immédiatement, puis repart avec ses Indiens ; Frémont lui confie l'invalide Dumes.",
  "Source primaire consultée en ligne : "+FRE+", 28 juillet 1842", "Position estimée des Red Buttes sur la North Platte.", "exploration"),
 ("Fort St. Vrain : les Canadiens choisis par Frémont (26 juillet 1843)", -104.858, 40.281, 1843.56, 1843.57, "1843-07-26", "jour", "certaine",
  "Basile Lajeunesse; François Badeau; Jean-Baptiste Bernier; Louis Ménard; Raphaël Proue; Jean-Baptiste Derosier; François Lajeunesse; Auguste Vasquez",
  "Pour sa propre colonne, Frémont retient Basile Lajeunesse, François Badeau, J.-B. Bernier, Louis Ménard, Raphaël Proue, Louis Zindel, J.-B. Derosier, François Lajeunesse et Auguste Vasquez. Il note aussi qu'un engagé français a été blessé par balle au fort Lupton le 4 juillet.",
  "Source primaire consultée en ligne : "+FRE+", 23-26 juillet 1843", None, "exploration"),
 ("Fort Manuel : les engagés canadiens de Lisa (1812-1813)", -100.66, 45.935, 1812.6, 1813.2, "1812/1813", "annee", "certaine",
  "Toussaint Charbonneau; Jessaume; Papin; Bijou; Lecomte; Archambeau; Cadet Chevalier; Laderoute; Pierre Chaine; Baptiste Provost",
  "Le journal de Luttig nomme au fort Manuel (baptisé solennellement un 19, avec salves) de nombreux Canadiens : Lecomte tué par des Crows (17 sept. 1812), Mercier et Carrière tués par des Sioux près du Big Bend (30 déc.), Cadet Chevalier mort de fièvre (4 janv. 1813), Latour, Machecou, Duroche et Laderoute chassés pour insubordination (21 janv.), Archambeau tué par des Sioux en charriant du foin (22 févr.).",
  "Source primaire consultée en ligne : "+LUT, "Le nom de Maurice LeDuc n'apparaît pas dans le journal (il figure au registre de compte de la compagnie).", "poste"),
]
