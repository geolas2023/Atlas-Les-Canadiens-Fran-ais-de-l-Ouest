# Lot « illinois » : dossier Drive ILLINOIS_MISSISSIPPI_KANKAKEE_JOLIET_MARQUETTE (56 fichiers non-images),
# dépouillé le 21 nov. 2026. Corpus « Recherches », préfixe ILK.
# Plusieurs sources : chaque fiche porte la sienne (argument source=). Pages : pagination imprimée, sauf mention « du PDF ».
# Voir illinois.md pour le tableau des fichiers et les extraits de preuve.
from commun import Corpus

HU = "Hulst, Cornelia Steketee (1912), Indian Sketches: Père Marquette and the Last of the Pottawatomie Chiefs, New York, Longmans, Green and Co. (PDF archive.org indiansketchesp01huls, Drive de l'auteur, dossier ILLINOIS_MISSISSIPPI_KANKAKEE_JOLIET_MARQUETTE)"
BE = "Belting, Natalia Maree (1943), « The French Villages of the Illinois Country », The Canadian Historical Review, vol. 24, n° 1, p. 14-23 (PDF Project MUSE 624508, Drive de l'auteur, dossier ILLINOIS_MISSISSIPPI_KANKAKEE_JOLIET_MARQUETTE)"
BR = "Briggs, Winstanley (1990), « Le Pays des Illinois », The William and Mary Quarterly, 3e série, vol. 47, n° 1, p. 30-56 (PDF JSTOR 2938040, Drive de l'auteur, dossier ILLINOIS_MISSISSIPPI_KANKAKEE_JOLIET_MARQUETTE)"
GU = "Gums, Bonnie (2001), « Voyage au pays des Illinois », Cap-aux-Diamants, n° 66, p. 19-25 (PDF Érudit, Drive de l'auteur, dossier ILLINOIS_MISSISSIPPI_KANKAKEE_JOLIET_MARQUETTE)"
WT = "Paul, James, Four Walking Tours of Historic Bourbonnais, Illinois, Bourbonnais Grove Historical Society et Kankakee County Historic Preservation Commission, 2016 (PDF WalkingToursWebDoc12516, Drive de l'auteur, dossier ILLINOIS_MISSISSIPPI_KANKAKEE_JOLIET_MARQUETTE/BOURBONNAIS)"
PE = "Happy 325th Birthday Peoria, brochure illustrée sur le Peoria colonial, s. a. [2016, date déduite du titre : 1691 + 325] (PDF 325th-Peoria-Birthday, Drive de l'auteur, dossier ILLINOIS_MISSISSIPPI_KANKAKEE_JOLIET_MARQUETTE)"
NO = "Nollett, Martin, Jr. (s. d.), Nollette Family History, généalogie familiale (PDF du Drive de l'auteur, dossier ILLINOIS_MISSISSIPPI_KANKAKEE_JOLIET_MARQUETTE)"
IS = "Isaacs, Marion (s. d.), The Kankakee River of History, Indiana (PDF archive.org kankakeeriverofh00isaa, Drive de l'auteur, dossier ILLINOIS_MISSISSIPPI_KANKAKEE_JOLIET_MARQUETTE/KANKAKEE)"

C = Corpus('Recherches', 'ILK', HU)
F = C.F

# --- Hulst 1912 -------------------------------------------------------------------------------------------
F('01', "Twin Lakes (comté de Marshall, Indiana) : le père Petit, la chapelle de Menominee et la déportation des Potawatomis (1837-1838)", 'religion', '1837/1838-09-04', -86.37, 41.30, 'a',
  ['Benjamin Petit', 'Menominee', 'Leopold Pokagon', 'John Tipton', 'David Wallace'],
  "Au village du chef potawatomi Menominee, à Twin Lakes, les Indiens bâtissent à la hache une chapelle de rondins de trente pieds sur quarante, avec une chambre au-dessus et une croix derrière. En 1837, le père Petit en prend la charge et vit au village ; il écrit compter de 1 000 à 1 200 chrétiens. Menominee refuse au conseil de quitter ses terres, mais la milice levée par le gouverneur Wallace convoque les Indiens à la chapelle, les y cerne et leur lit l'ordre de départ, en l'absence du prêtre. Selon le monument cité par Hulst, 859 Potawatomis sont emmenés le 4 septembre 1838 par le colonel John Tipton. Petit rejoint la colonne, obtient la libération des chefs, ligotés comme prisonniers de guerre, et note, après une halte à Danville (Illinois), « six tombes à l'ombre de la croix ». Il ne repart qu'après avoir vu les exilés installés au Kansas et meurt de la fièvre contractée avant de reprendre la route de la mission ; inhumé à Saint-Louis, il est plus tard ramené à Notre-Dame.",
  '44-47, 66-74',
  "Hulst ne donne ni le prénom ni l'origine de Petit : qu'il s'agisse de Benjamin-Marie Petit, prêtre français (H1-petit-benjamin-saint-mich), relève du contexte connu, non de la source. Ouvrage pour la jeunesse, à la manière d'Évangéline. Aucune fiche de l'atlas sur Twin Lakes ni sur cette déportation. Point approximatif au monument de Menominee, au sud-ouest de Plymouth.", source=HU)

# --- Belting 1943 -----------------------------------------------------------------------------------------
F('02', "Prairie du Rocher : de la terre de Sainte-Thérèse de Langloiserie au domaine des frères Langlois (vers 1722-1752)", 'etablissement', '1722~/1752', -90.098, 38.082, 'a',
  ['Jean Sainte-Thérèse de Langloiserie', 'Pierre Dugué de Boisbriant', 'Augustin Langlois', 'Étienne Langlois', 'Louis Langlois', 'Jacques Lalande', "Diron d'Artaguiette"],
  "Peut-être en 1722, le commandant Boisbriant concède à son neveu Jean Sainte-Thérèse de Langloiserie, officier du fort de Chartres, une terre au sud-est du fort, sur le chemin de Kaskaskia ; la carte de Broutin (1734) n'y marque que la « prairie du M. Ste. Thérèse ». Le 10 août 1737, un acte déposé à La Nouvelle-Orléans transporte « à Augustin L'Anglois mon domaine de Prairie du Rocher », les autres habitants de la prairie étant « tous seigneurs et maîtres ». Augustin et ses frères Étienne et Louis, venus de Basse-Louisiane après 1728, sont les plus grands propriétaires du lieu. Le 8 mai 1734, d'Artaguiette concède à Étienne Langlois cinq quarts de lieue dans la Grande Prairie, entre la terre de Jacques Lalande et les Kaskaskias. Le 7 mai 1743, les habitants reçoivent une commune d'une lieue de profondeur ; une chapelle funéraire dédiée à saint Joseph et douze maisons s'élèvent, et le recensement de 1752 compte 10 hommes, 9 femmes, 2 veuves et 18 jeunes gens et enfants.",
  '21-22',
  "Belting juge que les Langlois n'étaient probablement pas parents de Sainte-Thérèse, contrairement à d'autres auteurs. Les fiches TI003 et NK-barbeau-jean-b-prairie-du situent le village sans ces origines. Point au village actuel.", source=BE)

F('03', "Village de Chartres : les premières concessions près du fort (1721-1765)", 'etablissement', '1721/1765', -90.155, 38.087, 'a',
  ['Pierre Dugué de Boisbriant', 'Hébert le jeune', 'Jacques Catherine', 'François Cecire', 'Neyon de Villiers'],
  "Dès la construction du premier fort de bois, en 1721, un village naît dans la prairie à l'est du fort : le village de Fort de Chartres, appelé aussi village de la Prairie du fort de Chartres, puis Nouvelle-Chartres après 1756. Une commune est accordée aux habitants. Parmi les premiers colons, le sieur Hébert le jeune, Jacques Catherine et François Cecire reçoivent leurs terres le 2 mai 1724, à la seule condition d'y résider et de les mettre en valeur, faute de quoi elles reviennent à la Compagnie des Indes. Beaucoup d'habitants sont d'anciens soldats de la garnison devenus cultivateurs ou traiteurs. Le recensement de 1732 y compte 66 enfants légitimes et 6 illégitimes ; celui de 1752, 26 hommes, 24 femmes, 7 veuves, 93 enfants et jeunes gens et 88 Noirs. Quand les Anglais prennent le poste en 1765, la plupart des habitants ont suivi Neyon de Villiers à La Nouvelle-Orléans ou Laclède à Saint-Louis ; il reste trois familles.",
  '18-20',
  "Le chiffre « 03 » d'enfants en 1752 est lu « 93 » (coquille d'OCR probable). Le fort lui-même est déjà dans l'atlas (TI004, IL-chartres, RH-boisbriant-pierre-de-fort-de-ch) ; pas les concessions de 1724. Point approximatif à l'est du fort.", source=BE)

F('04', "Cahokia : les sept habitants français de 1735 et la maison Saucier (1735-1767)", 'etablissement', '1735/1767', -90.19, 38.57, 'a',
  ['Louis Gault', 'Blondin', 'Robillard', 'La Source', 'Rolet', 'François Mercier', 'Richard'],
  "Pendant tout le régime français, Cahokia reste surtout une mission indienne, celle de la Sainte-Famille des Tamarois, fondée par les prêtres du Séminaire de Québec. D'après une carte des archives du Séminaire, le village ne compte en 1735 que sept habitants français : Louis Gault, Blondin, Robillard, La Source, Rolet, François Mercier et Richard. Le recensement de 1752 y relève 18 hommes, 13 femmes, une veuve et 42 enfants ; en 1767, on annonce au général Gage soixante familles, et Pittman y voit quarante-cinq maisons autour de l'église. Le bâtiment dit palais de justice de Cahokia était la maison de la famille Saucier, bâtie vers la fin du régime français, l'un des rares exemples d'architecture française de l'Illinois.",
  '17-18',
  "Belting cite la carte d'après J. H. Schlarman, From Quebec to New Orleans (1929). Aucun de ces sept noms n'est dans l'atlas pour Cahokia en 1735 (RH-pretres-des-tamarois-en-1735-cahokia porte sur les prêtres). Point au centre de Cahokia.", source=BE)

# --- Briggs 1990 ------------------------------------------------------------------------------------------
F('05', "Village de Chartres : la paroisse Sainte-Anne, son syndic, son capitaine de milice et son curé choisi (vers 1720-1756)", 'religion', '1720~/1756', -90.152, 38.09, 'a',
  ['Philippe Dagnaux', 'Ignace Hébert', 'Gagnon', 'François Hennet dit Sans Chagrin', 'Robert Groston de St. Ange'],
  "Les villages de Chartres, Saint-Philippe et Prairie du Rocher forment la paroisse Sainte-Anne, qui compte 792 âmes d'après le registre et le recensement de 1752 ; Chartres s'étire sur un bon demi-mille le long du fleuve. L'assemblée des chefs de famille se tient le dimanche après la messe sur les marches de l'église, présidée par le syndic élu ; celui de Sainte-Anne fut longtemps Philippe Dagnaux, charron du village. Le capitaine de milice élu, le sieur Ignace Hébert, grand propriétaire et maître d'esclaves domestiques, était né neuvième de dix-sept enfants d'un habitant de Varennes. Les paroissiens bâtissent eux-mêmes leur église et, mécontents des prêtres du Séminaire de Cahokia, choisissent le jésuite Gagnon, ce qui suscite quarante ans de protestations du Séminaire. Le plus grand domaine, environ 750 acres, est celui d'un ancien soldat suisse, François Hennet dit Sans Chagrin.",
  '39-42, 47-48',
  "Briggs tire ces données du registre de Sainte-Anne (éd. Brown et Dean, 1977) et des manuscrits de Kaskaskia. Il cite aussi le parcours de Robert Groston, fils d'un boulanger bourguignon devenu « de St. Ange » (cf. EK15-11, EK15-28). Complète ILK-03.", source=BR)

F('06', "Kaskaskia : Louis Turpin impose le règlement des chemins du pays des Illinois (1748)", 'personnage', '1748', -89.92, 37.92, 'a',
  ['Louis Turpin'],
  "Les paroisses n'étant pas contiguës, de longues sections du chemin du Roi qui relie les villages échappent aux corvées paroissiales et relèvent du commandement, qui s'en occupe mal. Après des années de confusion, Louis Turpin, colon aisé et influent de Kaskaskia et capitaine de sa milice, obtient en 1748 d'un ingénieur du roi un règlement complet des droits et devoirs des particuliers et des communautés pour l'entretien des chemins. Il le dépose sur le bureau du notaire, subdélégué et juge, et ce texte devient aussitôt la loi des chemins des Illinois, acceptée sans un murmure par les autorités. Briggs y voit l'exemple d'un pays où l'initiative vient des habitants plutôt que des officiers.",
  '45',
  "Référence de Briggs : KAS. MSS 48/9/8/1. Belting (1943, p. 22) signale déjà une requête de Turpin du 30 décembre 1741 sur le balisage du chemin des salines, qui mentionne des mineurs de plomb établis à l'ouest du Mississippi. L'atlas n'a de Turpin qu'un jugement de 1739 (QE-turpin-louis-kaskaskia). Point au site de l'ancien Kaskaskia.", source=BR)

# --- Gums 2001 --------------------------------------------------------------------------------------------
F('07', "Prairie du Pont : la maison Martin-Boismenue, retrouvée sous les bardeaux (vers 1790)", 'etablissement', '1790~/1991~', -90.163, 38.548, 'a',
  ['Pierre Martin', 'Boismenue (famille)'],
  "Le village de Prairie du Pont, à quelques kilomètres de Cahokia, est colonisé en 1754 par les missionnaires de Cahokia, qui y bâtissent un moulin près d'une chute tombant d'une falaise de calcaire ; une petite population civile y vit en 1780. La maison Martin-Boismenue, construite vers 1790 par Pierre Martin, natif du Québec, puis confiée à la famille montréalaise Boismenue, serait la plus ancienne maison encore debout de l'Illinois. En 1981, la maison en ruine devait être brûlée lors d'un exercice de pompiers volontaires ; l'un d'eux découvrit derrière les parois modernes une structure intacte en poteaux sur sole. La Prairie du Pont Preservation Society la restaure en dix ans ; elle garde près de 80 % de ses matériaux d'origine, dont un sous-sol avec foyer de calcaire.",
  '20-22',
  "La date de fin (vers 1991) est déduite des « dix années » de restauration après 1981. L'atlas a des Boismenu à Cahokia (NL-boismenu-nicolas-cahokia) mais pas cette maison. Point approximatif à Prairie du Pont, au sud de Cahokia.", source=GU)

F('08', "Cahokia : le palais de justice, de maison coloniale à salon de thé de Chicago et retour (vers 1737-1940)", 'etablissement', '1737~/1940', -90.1903, 38.5703, 'a',
  [],
  "Le bâtiment appelé Cahokia Courthouse est construit vers 1737 et sert de palais de justice de 1793 à 1814 pour tout le territoire au nord-ouest des jeunes États-Unis. En 1904, il est démonté, expédié sur le Mississippi et rebâti en plus petit, sans son pierrotage, pour l'Exposition universelle de Saint-Louis, puis démonté de nouveau et envoyé au Jackson Park de Chicago comme salon de thé japonais. En 1939, grâce aux habitants de Cahokia, ses restes reviennent sur place ; il est reconstruit en 1940 avec des matériaux reproduits, et le Cahokia Memorial Survey de la WPA fouille alors son emplacement. Il abrite un musée de la vie coloniale française, où l'on célèbre chaque printemps une « danse de la fête ».",
  '20',
  "Belting (1943, p. 18) précise que cette maison était celle de la famille Saucier et la date de la fin du régime français (voir ILK-04). Point approximatif au palais de justice.", source=GU)

F('09', "Cahokia : Nicolas Jarrot, réfugié de la Révolution française, et son manoir de brique (1794-1810)", 'personnage', '1794/1810', -90.1885, 38.5714, 'a',
  ['Nicolas Jarrot'],
  "Tout près de l'église de la Sainte-Famille, achevée en 1799 en poteaux sur sole, se dresse le manoir Nicholas-Jarrot. Réfugié de la Révolution française, Nicolas Jarrot arrive à Cahokia en 1794 et devient un riche et célèbre entrepreneur foncier. Achevée en 1810 dans le style fédéral américain, sa maison passe pour le plus ancien bâtiment de maçonnerie de l'Illinois. Elle appartient aujourd'hui à l'État de l'Illinois.",
  '21',
  "L'atlas ne nomme Jarrot qu'en passant (FW97-02, trappistes de Cahokia). Point approximatif près de l'église de la Sainte-Famille.", source=GU)

# --- Walking Tours 2016 -----------------------------------------------------------------------------------
F('10', "Bourbonnais : l'académie Notre-Dame des sœurs de la Congrégation de Notre-Dame (1860-1972)", 'religion', '1860-10-01/1972', -87.877, 41.151, 'a',
  ['Philip Houde'],
  "Le 1er octobre 1860, trois sœurs de la Congrégation de Notre-Dame ouvrent des classes pour 50 filles dans une petite maison de pierre à l'angle des rues Roy et Marsile. En janvier 1861, elles s'installent dans un bâtiment de pierre à deux étages, construit en 1859 aux frais de Bourbonnais Grove, à l'est de l'église de la Maternité : c'est l'académie Notre-Dame. Une académie de bois à trois étages est bâtie au nord de l'église en 1862 et agrandie jusqu'en 1910 ; elle devient un pensionnat important. En 1909-1910, l'entrepreneur Philip Houde élève une académie de brique crème de quatre étages, qui accueille jusqu'à 250 élèves. L'académie ferme en 1949, le bâtiment sert de couvent, est déclaré inhabitable en 1971 et démoli en 1972.",
  '8, 10',
  "La brochure situe le bâtiment de 1859 tantôt à l'est de l'église, tantôt à l'angle Roy-Marsile ; on s'en tient aux deux extraits. L'atlas mentionne le couvent en une phrase (IF2-mq03, DRV-12). Point approximatif au nord de l'église de la Maternité.", source=WT)

# --- Peoria 325 -------------------------------------------------------------------------------------------
F('11', "Peoria : la maison à poteaux en terre du Vieux village français, fouillée en 2001 (vers 1770-1812)", 'etablissement', '1770~/1812', -89.588, 40.700, 'h',
  [],
  "La brochure situe le fort et la mission de 1691 sur la rive nord-ouest du lac Peoria, à un mille et demi au-dessus de sa décharge, près de l'actuelle marina Detweiller, à côté d'un village illinois de plus de 300 maisons longues. Le Vieux village français, habité des années 1770 à 1812, était lui aussi près de la marina ; des parties de ses terres et de ses lignes de lots furent relevées par le gouvernement américain dans les années 1820. En 2001, l'Illinois State Archaeological Survey y fouille l'empreinte d'une maison à poteaux en terre du XVIIIe siècle, près de l'angle des rues Adams et Mary, à un pied seulement sous la surface. En 2004, des vestiges du Nouveau village français (Ville de Maillet) sont découverts au centre-ville ; les sites du village illinois, de la mission et des forts restent inconnus.",
  '4, 9, 14-15 du PDF',
  "Brochure de vulgarisation sans auteur. Elle place le Vieux village près de la marina Detweiller mais la fouille de 2001 à l'angle Adams-Mary : l'emplacement de la fiche est donc hypothétique. Complète IL-vieuxpeoria, IL-maillet et IL-pimiteoui, qui ne parlent pas d'archéologie.", source=PE)

# --- Nollette Family History ------------------------------------------------------------------------------
F('12', "Valentine et la Minnechaduza (Nebraska) : Peter Robidou, charpentier du chemin de fer, et son homestead (1882-1891)", 'famille', '1882/1891', -100.69, 42.87, 'a',
  ['Peter Robidou', 'Sophia Hurteau', 'Frank Robidou', 'Peter Donoher', 'Margaret Robidou', 'Sidney Grandon'],
  "Né dans l'État de New York dans les années 1820, fils de Pierre Robidou et de Françoise Tessier, Peter Robidou épouse vers 1851 Sophia Hurteau, née au Canada ; la famille passe par Waukegan (Illinois), l'Iowa et le comté de Turner (Dakota), où Peter obtient une patente en 1882. À l'automne 1882, il arrive à Valentine avec le chemin de fer, campe tout l'hiver sous une double tente garnie de mottes et aide à construire le premier hôtel, la Valentine House. En mai 1883, la famille s'établit à sept milles à l'ouest, sur la Minnechaduza, dans une maison de rondins de 18 pieds sur 24 ; Peter est le seizième à déposer sa demande de homestead à l'ouverture du bureau des terres. Sophia lave et cuisine pour les équipes du chemin de fer ; leur fils Frank est le premier instituteur de l'école Prairie Bell, à deux milles de là. Peter fait valoir son homestead en septembre 1889 et part vers 1891 pour le secteur de Sparks et Kewanee.",
  '8-10, 14',
  "Frank enseigne à Prairie Bell en 1883 selon la p. 9, au printemps 1884 selon les registres scolaires cités p. 14. La source date l'ouverture du bureau des terres du « July 2, 1983 », coquille pour 1883. Elle fait de Peter un cousin au quatrième degré des Robidoux de Scotts Bluff (sans preuve donnée). Elle signale aussi (p. 25) que le trappeur Hubert Rouleau est inhumé au vieux cimetière Minnechaduza (Boot Hill) de Valentine (cf. HW76-18). Point approximatif à sept milles à l'ouest de Valentine.", source=NO)

F('13', "Crookston (Nebraska) : Felix Nollett et Annie Robidou, une famille qui prie en français (1887-1912)", 'famille', '1887-04-07/1912', -100.75, 42.93, 'a',
  ['Felix Nollett', 'Annie Robidou', 'Louis Nollette', 'Ellen Robidou', 'Henry Grothe', 'Ferdinand Lechleitner'],
  "Né le 22 mars 1866 dans le comté d'Iroquois et baptisé à L'Érable, Felix Nollett arrive en 1884 au comté de Cherry avec ses parents. Il dépose sa propre demande de homestead à Valentine le 7 avril 1887 et achète la même année, avec ses frères, une batteuse de douze chevaux. Le 1er mai 1889, il épouse à Crookston Annie Robidou, devant le jésuite Henry Grothe venu de St. Francis ; son frère Louis épouse Ellen Robidou le 6 octobre 1890. Le couple a treize enfants ; on parle français à la maison jusqu'à l'entrée des aînés à l'école, et l'on récite encore le chapelet en français le soir. Les prêtres de Valentine s'arrêtent chez eux au retour de Norden, où la messe est dite une fois par mois.",
  '10, 16-17',
  "La p. 10 date le mariage du 1er mai 1899, la p. 16 du 1er mai 1889 ; on retient 1889, cohérent avec la naissance d'Annie (1872) et les treize enfants. La p. 16 date aussi de « March 1990 » l'arrivée du père Lechleitner (coquille pour 1890). Point approximatif à Crookston ; le homestead de Felix n'est pas situé.", source=NO)

F('14', "French Settlement de Kewanee (comté de Cherry, Nebraska) : le cimetière Saint-Joseph (1886-1903)", 'famille', '1886-06-11/1903-10-20', -100.56, 42.96, 'h',
  ['Hilaire Nollette', 'Marie Mailloux', 'Ephrem Nollette', 'Peter Robidou', 'Sophia Hurteau', 'Ellen Robidou'],
  "Hilaire Nollette meurt le 11 juin 1886 et sa femme Marie le 4 août 1887 ; ils sont les premiers inhumés au cimetière Saint-Joseph de la French Settlement, sur le homestead de leur fils Ephrem. Ils partagent la même pierre avec Peter et Sophia Robidou, parents des épouses de Louis et de Felix Nollette. Peter meurt en février 1900 et Sophia en novembre 1901 ou 1902, tous deux enterrés au même cimetière. Ellen Robidou, femme de Louis Nollette, meurt le 20 octobre 1903 des suites d'un accouchement.",
  '4, 10, 17',
  "Contradictions internes : Peter meurt le 7 février 1900 (p. 4 et 17) ou le 16 février 1900 (p. 10) ; Sophia le 20 novembre 1902 (p. 4) ou le 20 novembre 1901 (p. 17). La p. 17 ne dit pas où Ellen est inhumée. Complète NOL-02, qui ne mentionne pas le cimetière. Point hypothétique près de NOL-02.", source=NO)

F('15', "Toledo (comté de Lewis, Washington) : l'hôtel de Hilaire Nollette fils et de Julie Courville (années 1880-1931)", 'famille', '1880~/1931-04', -122.847, 46.44, 'a',
  ['Hilaire Nollette fils', 'Julie Courville'],
  "Fils aîné de Hilaire et Marie Nollette, émigrés de Napierville en Illinois puis au Nebraska, Hilaire Nollette fils part dans les années 1880 pour Toledo, dans le comté de Lewis (Washington). Charpentier de wagons de chemin de fer, il prend sa retraite assez tôt. Avec sa femme Julie Courville, il tient un hôtel dans les premiers temps de Toledo ; on le dit sociable et aimé de tous. Il meurt en avril 1931 et Julie en novembre 1942.",
  '4',
  "Point au centre de Toledo.", source=NO)

F('16', "Élie (Manitoba) : Felix Dutour, né en Iowa, maître de poste et fermier (1901-1961)", 'migration', '1901~/1961-01-28', -97.753, 49.913, 'a',
  ['Felix Dutour', 'Jean-Baptiste Dutour', 'Josephine Nollette', 'Anna Hogue'],
  "Fils de Jean-Baptiste Dutour et de Josephine Nollette, Felix Dutour naît le 4 avril 1882 à Sheldon (Iowa), passe par le Nebraska et le Kansas et s'établit au Manitoba vers 1901. Après un an à Sainte-Anne, près de Winnipeg, il s'installe à Élie, où il cultive la terre. En 1911, il prend le bureau de poste d'Élie tout en exploitant 240 acres de grain au sud du village, et tient les agences John Deere et Westinghouse. En 1912, il épouse Anna Hogue, fille de Louis Hogue et de Julie Turcotte. Il travaille ensuite comme préposé aux pompes du Canadien National à Élie, McCreary et Russell, et meurt à Winnipeg le 28 janvier 1961 ; Anna meurt centenaire en 1986.",
  '11',
  "Exemple de remontée vers le Manitoba d'une famille canadienne-française de Bourbonnais. Point au village d'Élie.", source=NO)

F('17', "Lead et le canyon de Spearfish (Dakota du Sud) : Frank Robidou, voiturier et violoneux (1894-1914)", 'famille', '1894/1914~', -103.77, 44.35, 'a',
  ['Frank Robidou', 'Alice Paxton', 'Ed Rentz', 'Christopher Robidou'],
  "Né le 8 mars 1863, Frank Robidou, fils de Peter, épouse le 18 avril 1892, près de Valentine, Alice Paxton, devant le missionnaire Ferdinand Lechleitner. En 1894, le couple gagne Black Hawk (Dakota du Sud) en chariot, puis en 1898 le petit canyon de Spearfish, près de la station de pompage de Homestake, et en 1902 Lead, où Frank conduit des attelages pour la Homestake Mining Co. et fait partie des pompiers. Voiturier entre Pierre et Rapid City à travers la réserve, il passe des nuits à parler français avec son ami Ed Rentz. Il vend aussi des machines à coudre Singer, coupe des piquets, joue du violon et organise des bals ; la famille vit un temps à « Robidou Gulch ». Vers 1914, elle part pour Mills puis Casper (Wyoming), où Frank meurt le 11 juin 1932.",
  '14-15',
  "Récit familial de Cecelia Raycher, repris par Nollett. La p. 10 situe Frank à Deadwood ; les p. 14-15 à Lead. Point approximatif à Lead.", source=NO)

# --- Isaacs -----------------------------------------------------------------------------------------------
F('18', "Île Française (French Island) sur le Kankakee, comté de Porter (Indiana) : le traiteur LaBonta, premier colon (entre 1821 et 1847)", 'toponymie', '1821/1847', -87.08, 41.21, 'h',
  ['LaBonta', 'Lorenzo Werich'],
  "Isaacs reprend le souvenir de Lorenzo Werich, né en 1860 près de Valparaiso, qui vécut dix ans enfant sur l'île. Selon lui, les Français avaient depuis longtemps un poste de traite à Tassinong, et des chasseurs blancs arrivent dans la région du Kankakee en 1821. Le premier à s'établir sur l'île est un traiteur français nommé LaBonta ; deux ou trois autres familles françaises le suivent, d'où le nom de French Island. À l'automne 1847, Heck et John Goodridge y bâtissent la première cabane de trappeur professionnel. L'île est l'une des nombreuses îles du marais sur la rive sud du Kankakee, dans le comté de Porter.",
  '52-53',
  "Souvenir tardif et de seconde main ; aucune date pour LaBonta, sinon après 1821 et avant 1847. Isaacs (ISK-01) reconnaît la part de conjecture de son livre. Point hypothétique sur le Kankakee au sud du comté de Porter.", source=IS)

fiches = C.fiches

autoch = [dict(id='A-ILK-01', src='ILK-01', nom="Twin Lakes (Indiana) : Potawatomis — la bande de Menominee arrachée à sa chapelle (1837-1838)", theme='evenement', date='1837/1838-09-04', lon=-86.37, lat=41.30, cert='a',
   nations=['Potawatomis'], aires=['Grands Lacs'], francophones=['Benjamin Petit'],
   description="Le chef Menominee, qui prêchait lui-même à son peuple depuis des années, fait bâtir par les siens la chapelle de rondins de Twin Lakes et accueille en 1837 le père Petit. Au conseil, il refuse de vendre ou de quitter ses terres : « Je n'ai pas vendu mes terres ! Je ne les vendrai pas ! » Des squatters brûlent des wigwams de son village ; la milice convoque la bande à la chapelle, la cerne et lit l'ordre de départ. Le 4 septembre 1838, selon le monument de 1909, 859 Potawatomis sont emmenés, les chefs liés dans un chariot jusqu'à l'intervention de Petit. Le village, le plus grand du pays, est rasé ; Pokagon et quelques-uns obtiennent de rester au Michigan. On ignore où Menominee est enterré.",
   note="D'après Hulst (1912), p. 44-47, 66-74. Source pour la jeunesse, mais qui cite le rapport de Tipton et l'inscription du monument.")]
