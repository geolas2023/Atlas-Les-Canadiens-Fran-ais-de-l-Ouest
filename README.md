# Les Canadiens français de l'Ouest — Atlas historique des francophones d'Amérique du Nord

Atlas Web interactif (MapLibre GL JS) des francophones (Canadiens français, Créoles du Missouri et de l'Illinois, Français, Suisses romands) et des événements qui les concernent en Amérique du Nord. La première version porte sur l'Ouest américain ; le deuxième lot de novembre 2026 l'étend au Midwest, à la Nouvelle-Angleterre, à la Louisiane et à la Nouvelle-France. La chronologie couvre 1560-2010. Le site est publié avec GitHub Pages : `https://geolas2023.github.io/Atlas-Les-Canadiens-Fran-ais-de-l-Ouest/`.

Projet parent : l'**Atlas Aubry** (François-Xavier Aubry, 1824-1854), dont les fiches ponctuelles sont intégrées ici.

## Corpus de cette version

| Corpus | Fiches | Contenu |
|---|---|---|
| **Cragin** | 183 | Dépouillement complet des *Early Far West Notebooks* de Francis W. Cragin (entrevues de pionniers, 1902-1923 ; transcription de Mrs. Shaw, PDF consultable de 333 pages). Toutes les mentions de francophones ont été géolocalisées : trappeurs et voyageurs (Lesperance, Ledoux, LeDuc, Levanway, Chalifoux, Lalande, Robidoux, Leroux, Janis, Provost…), familles (St. Vrain, Beaubien, Vasquez, Autobees, Lefebvre, Nolan, Gillette…), postes (fort St. Vrain, fort Vasquez, fort Uintah, fort Leche, Hardscrabble, El Pueblo), colonies (Butte Valley, La Porte, San Gerónimo), événements (révolte de Taos et de Mora en 1847, massacre du Pueblo, combats) et toponymes (Fontaine-qui-Bouille, Cache-la-Poudre, Duchesne). |
| **Recherches** | 7 | Traces francophones repérées dans la littérature et sur le Web au fil des recherches (Rio Colorado/Questa, Hardscrabble, Las Vegas, forts Robidoux…), sources citées dans chaque fiche. Corpus appelé à grandir. |
| **Hafen** | 419 | (1) 396 étapes géolocalisées tirées des 22 notices et de l'introduction de *French Fur Traders and Voyageurs in the American West* (Hafen dir., 1995), lues intégralement : chaque fiche cite la page du livre et la source primaire donnée en note par l'auteur de la notice (identifiants `F-<personnage>-NN`). (2) 23 points provisoires (`H…`) pour les autres francophones ayant une notice dans *The Mountain Men and the Fur Trade of the Far West* (1965-1972), résumés d'après des sources générales, à vérifier. |
| **Hafen MM** | 2 129 | Dépouillement des vol. 2, 4-9 de *The Mountain Men* : lieux datés des biographies de 68 francophones (repérage automatique, page citée ; à vérifier). Remplace 21 points provisoires `H…`. Script : `scripts/ajouts_2026_11.py`, données sources : `scripts/sources_2026/`. |
| **Tassé** | 174 | Joseph Tassé, *Les Canadiens de l'Ouest* (1878), t. I et II : 35 vies, 158 étapes et 16 établissements, page citée. |
| **Illinois français** | 38 | Nouvelle-France, villages de Peoria (181 habitants, East 1933), Petit Canada de la Kankakee, presse française de l'Illinois (Cormier 1957), collège Saint-Viateur, archipel du Midwest (IFMidwest). |
| **Atlas historique du Québec** | 62 | Frenette, Rivard et St-Hilaire (dir.), *La francophonie nord-américaine* (PUL, 2012) : piste de Santa Fe, Pays d'en Haut, Détroit, Louisiane, Pays des Illinois, Métis, Nouvelle-Angleterre, Midwest, Plaines, Californie (identifiants `AH-…`). |
| **Franco-Amérique** | 26 | Louder et Waddell (dir.), *Franco-Amérique* (Septentrion, 2008) (`FA-…`). |
| **Nouvelle-France** | 36 | Margry, t. I (1876) ; Johnson, *French Pathfinders* (1905) ; Marchand, *Ghost Empire* (2005) (`NF-…`). |
| **Nouvelle-Angleterre** | 44 | Vermette, *A Distinct Alien Race* (2018) ; MacDonald (1898) ; Belisle (1907) (`NA-…`). |
| **Piste de l'Oregon** | 23 | Bergeron, *La légende de l'Oregon était vraie* (`OR-…`). |
| *compléments* | 41 | Illinois français : McQuillan (1979), Papen (2006) (`IF2-…`) ; Recherches : allocution de Worcester, *Le Progrès du Golfe* (1940) (`R2-…`) ; Étienne Provost à Saint-Louis, versé depuis l'Atlas Aubry (`PV-…`, 5 fiches, dont l'ancienne L100 ; dossier `provost.html` / `provost-en.html` généré par `scripts/page_provost.py`). Script : `scripts/ajouts_2026_11b.py` (à lancer après `ajouts_2026_11.py`), données : `scripts/sources_2026b/`. |
| *Drive de l'auteur (nov. 2026)* | 989 | Corpus « Recherches » : documents du Drive dépouillés les 19 et 20 novembre 2026 (`DRV-…`, 35 fiches : Cimarron et Maxwell, Bourbonnais Grove, Carlos Beaubien, Provost, Godey, ventes d'esclaves à Saint-Louis, pionniers de Los Angeles) ; Lecompte, *Pueblo, Hardscrabble, Greenhorn* (1978) (`LC78-…`, 16) ; Bolton, *French Intrusions into New Mexico* (1917) (`BF17-…`, 8) ; *Journal de Larocque*, 1805 (éd. Burpee, 1911) (`LR05-…`, 11, voyage chez les Crows) ; Wood et Thiessen, *Early Fur Trade on the Northern Plains* (1985) (`WT85-…`, 13, Ménard, Jusseaume et les résidents des villages mandans, fort des Trembles, Pine Fort, Larocque et Macdonell) ; Hocking, *Terror on the Santa Fe Trail* (2019) (`HK19-…`, 3, Leroux et la guerre jicarilla) ; Gianini, « Manuel Lisa » (1927) (`GI27-…`, 9) ; Ebright, *Land Grants and Lawsuits* (1994) (`EB94-…`, 3) ; Montoya, *Translating Property* (2002) (`MT02-…`, 9, la concession Beaubien-Maxwell) ; Benoit, « Gentilly » (1975) (`BN75-…`, 6) ; lettre de Chiniquy à Brassard (1857) (`CQ57-…`, 2) ; Old Rock House de Saint-Louis (NPS 1998, HABS) (`RH98-…`, 2) ; certificat de décès de Mary Rose Pillsbury, « fille d'Étienne Provo » (1913) (`PV13-…`, 1) ; Kienzle, *Lost St. Louis* (2017) (`LS17-…`, 2, l'étang Chouteau) ; Brettell, *Following Father Chiniquy* (2015) (`BR15-…`, 15, la colonie de la Kankakee, le schisme et le pèlerinage de Sainte-Anne) ; Hyde, *Life of George Bent* (1968) (`GB68-…`, 4, Edmond Guerrier) ; Antoine, *Remnants of French Prairie du Chien* (2019) (`MA19-…`, 8, maisons pièce sur pièce) ; Hafen, « When Was Bent's Fort Built? » (1954) (`HF54-…`, 2) ; notice « Tom Sun - Wyoming Pioneer » (2011) (`TS11-…`, 2, Thomas de Beau Soleil, Charles Lajeunesse) ; Meir, « Wagons West to Kansas » (*Le Journal du Village*, 2011) (`LJ11-…`, 6, de la Kankakee au Kansas) ; *The St. Paul Globe*, « Little Canada » (1903) (`SPG03-…`, 3) ; Peterson, *Colonial St. Louis* (1949), les bâtisseurs et artisans (`PT49-…`, 12) ; Brackenridge, *Journal of a Voyage up the River Missouri* (1811) (`BK16-…`, 6) ; coupures de presse sur la mémoire des pionniers (1939, 1956) (`PRM-…`, 2) ; Cormier, « La presse française de l'Illinois » (1957) (`CO57-…`, 8) ; Gitlin, *The Bourgeois Frontier* (2010), passe complète (`GT10-…`, 4) ; Provost dans la mémoire québécoise (Vaugeois 2008, Hamelin 2020) (`PVM-…`, 2) ; McDermott, *A Glossary of Mississippi Valley French* (1941), sobriquets de lieux (`MD41-…`, 5) ; Shepard, *Early History of St. Louis* (1870), lecture partielle (`SH70-…`, 1) ; Billon, *Annals of St. Louis in its Territorial Days* (1888), lu en entier : tour à plomb de Maclot, académie Pescay, Guibord, Chenié, René Paul, Perdreauville, fils Papin, forge Beauvais (`BL88-…`, 11) ; Paquin, *La colonie canadienne-française de Chicago* (1893) (`PQ93-…`, 12) ; Drury et Clavin, *Sur la terre des Sioux* ; Ameur, *Sitting Bull* (`DC13-…`, 2) ; Houzeau, *La terreur blanche au Texas* (1862) (`HZ62-…`, 2) ; Routhier, *De Québec à Victoria* (1893) (`RT93-…`, 6) ; Beaugrand, *Jeanne la fileuse* (1878) (`BG78-…`, 3) ; Beaugrand, *Six mois dans les Montagnes-Rocheuses* (1890) (`BG90-…`, 5) ; Daoust, *Cent-vingt jours de service actif* (1886), le 65e en Alberta (`DA86-…`, 7) ; McDermott, « The French Impress on Place Names » (1979) (`MD79-…`, 9) ; Roden, « The Beaubien Claim » (1949) (`RD49-…`, 5) ; *Nollette Family History* (Kankakee et Nebraska) (`NOL-…`, 3) ; Hamy, *Au Mississipi* (1903) (`HM03-…`, 1) ; Temple, *Indian Villages of the Illinois Country* (1958), lu en entier (`TP58-…`, 10) ; Trépanier, « Un Montréalais du siècle dernier : l'immigrant juif Louis Marchand » (1965) (`TR65-…`, 1) ; Isaacs, *The Kankakee River of History* (s.d.), tradition d'un fort français (`ISK-…`, 1) ; Amsbary, *Ballads of Bourbonnais* (1904) (`AM04-…`, 1) ; Kantowicz, « A Fragment of French Canada on the Illinois Prairies » (1982) (`KZ82-…`, 2) ; Pease et Werner, *The French Foundations, 1680-1693* (1934), lu en entier : concessions du fort Saint-Louis, lettre de La Salle (1683), engagés de Montréal, mémoire De Gannes (`PE34-…`, 5) ; Chaloult, *Les « Canadiens » de l'expédition Lewis et Clark* (2003), lu en entier (`CH03-…`, 4) ; Dionne, *Chouart et Radisson* (1910), le fort de Chagouamigon (`DN10-…`, 1) ; Snyder, « Antoine LeClaire, the First Proprietor of Davenport » (*Annals of Iowa*) (`SNL-…`, 2) ; Hanson et Walters, « The Early Fur Trade in Northwestern Nebraska » (1976) (`HW76-…`, 18 : fort Lucien, Chadron Creek, fort Platte, Crow Butte, district de Bordeaux, Francis C. Boucher) ; Swenson, « Chicagoua/Chicago » (1991), Joutel et l'ail sauvage (`SW91-…`, 1) ; Ancelet, « Québec, Acadie et Louisiane : l'influence des retrouvailles » (`ANC-…`, 1, CODOFIL) (`ANC-…`, 1) ; Podruchny, *Making the Voyageur World* (2006) (`PD06-…`, 13 : Jean Mongle, recruteurs, grèves, dérouine, affaire Connolly) ; Turner, *The Toronto Carrying Place* (2015), le fort Rouillé (`TU15-…`, 1) ; Foxcurran, Bouchard et Malette, *Songs Upon the Rivers* (2016), Ecorse, Marie Rouensa, Madame Laframboise, Frenchtown, élection de 1825 (`FX16-…`, 11) ; Audubon, « The Missouri River Journals » (*Audubon and his Journals*, 1897), Étienne Provost chasseur au fort Union en 1843 (`AU43-…`, 2) ; Adair, *The History of the American Indians* (éd. Braund 2005), relu : Pierre Chartier, Priber à Tellico, la révolte de Soulier Rouge, le fort Toulouse (1740, 1749-1750, 1763), Tombecbé, le siège des Natchez de 1731, la cession de Mobile (`AD05-…`, 17) ; Smith, *Heroes of the Santa Fe Trail* : les convois de moutons de Rayado avec Henry Mercure (1853) (`RSH-…`, 1) ; Les Maxwell-Beaubien à Fort Sumner, 1870-1881 : la maison de Pete Maxwell, Luz Beaubien, Paulita et Deluvina, le ranch de Pablo Beaubien (Wallis 2007, Utley 2015, Garrett 1882) (`MFS-…`, 4) ; Radisson, récit du « quatrième voyage » (éd. Scull, Prince Society, 1885), lu par OCR : village huron-outaouais, famine de 1659-1660, fête des Morts avec les Sioux, camp des Cris (`RD85-…`, 4) ; Freiberger, *Lucien Maxwell: Villain or Visionary* (1999) : l'or du mont Baldy, Elizabethtown, la First National Bank de Santa Fe, la communauté de Fort Sumner (`FB99-…`, 4) ; LeMoine, *Le massacre au fort George* (1864) : le missionnaire des Abénaquis en 1757, la querelle McClellan-Montcalm de 1864 (`LM64-…`, 2) ; Buies, *Chroniques*, t. II (1875) : le voyage en Californie de juin 1874 (Chicago, Omaha, San Francisco) (`BU75-…`, 3) ; Eccles 1983, The Canadian Frontier : 2 fiches (EC83) (`EC83-…`, 2) ; Forrest 2020, The Death of the French Atlantic : 1 fiche (FO20) (`FO20-…`, 1) ; News from Old Mines 2016 (Austin 1804) : 3 fiches (OM16) (`OM16-…`, 3) ; Missouri Life 2013, le français d'Old Mines : 1 fiche (ML13) (`ML13-…`, 1) ; Bolton 1913, New Light on Manuel Lisa : 2 fiches (BO13) (`BO13-…`, 2) ; Weber, *The Taos Trappers* (1971), d'après les archives espagnoles et mexicaines (SANM, MANM) : Charvet, Durocher, La Lande, Lacroix et Terien, Champlain et Lafargue, Philibert, les convois Robidoux et Pratte, les trappeurs français de Taos (1827), les naturalisations de 1829-1830 (`WB71-…`, 54) ; Cleland, *This Reckless Breed of Men* (1950) : le massacre de l'Umpqua (1828), Laframboise et Josette Legacé en Californie (`CL50-…`, 3) ; *Proceedings of the 2015 Fur Trade Symposium* : Fort Platte, Fort John, Fort Jackson, le « rendez-vous de Robidoux », le poste de Reed et Julien (`FT15-…`, 10) ; Yealy 1935, Sainte Genevieve (`YE35-…`, 7) ; Fowler 1997, The Cahokia Atlas : 2 fiches (FW97) (`FW97-…`, 2) ; Trudeau, Journal du haut Missouri 1794-1796 (éd. Grenier et Saint-Gelais 2006) : 14 fiches (GS06) (`GS06-…`, 14) ; Nicollet 1841, Report (haut Mississippi), relu en entier : Fort Pierre, lac du Diable, Traverse des Sioux, les Renville au Lac qui Parle, Laframboise à la Grande Lisière de Bois, carrière de pierre à calumet, rivière aux Canots, côtes brûlées, Talle de Chênes, Louison Frenière, lac des Chicots, Francis Brunet au lac Sangsue, Itasca (`NI41-…`, 14) ; Kent 1976 et Tremblay 1915, Étienne Brûlé : 6 fiches (KE76, TB15 : Toanché, Otouacha, Carhagouha, Québec 1633, Ihonatiria) (`KE76-…`, 6) ; Blanchard 1882, History of Du Page County : 2 fiches (BL82) (`BL82-…`, 2) ; Dossier militaire de Jack Kerouac (NARA) et Sur les traces de Kerouac (Radio-Canada 2014) : 4 fiches (KR43) (`KR43-…`, 4) ; Volney 1803, Tableau du climat et du sol des États-Unis (voyage de 1796) : 8 fiches (VO03) (`VO03-…`, 8) ; Audubon, Scènes de la nature (trad. Bazin 1868) : 1 fiche (AB68) (`AB68-…`, 1) ; McDermott (dir.), *The French in the Mississippi Valley* (1965, `FMV65-…`, 28 fiches : maisons de Saint-Louis et de Kaskaskia, familles de Saint-Domingue, Regnier, Gibault, ingénieurs de la Louisiane espagnole) et *Frenchmen and French Ways in the Mississippi Valley* (1969, `FFW69-…`, 30 fiches : Auguste Chouteau, Nicollet, Du Bourg, fort Massac, mémoire Pitot, Conseil supérieur, île Dauphine, Iberville au delta, Sainte-Geneviève, Pontchartrain, François Saucier, Broutin) ; Rothensteiner, *History of the Archdiocese of St. Louis*, vol. II (1928, `ROT28-…`, 16 fiches : Chouteau's Church de Kawsmouth, Saint-Joseph de Robidoux, Old Mines, Little Canada, Florissant) ; Toft, *St. Louis: Landmarks & Historic Districts* (1988, `TFT88-…`, 6) ; Murray, *Terra Nostra* (`TNM-…`, 3 : mer de l'Ouest, phototopographie de Deville) ; Monette, *St. John de Crèvecœur* (2009, `MON09-…`, 2) ; Denuzière 2013, La dix-huitième étoile (Louisiane) : 2 fiches (DZ13) (`DZ13-…`, 2) ; Dziembowski 2015, La guerre de Sept Ans : forts Marin (Presqu'île, Le Bœuf, Machault), Chouaguen, William Henry, Carillon, fort de Chartres 1763 (`DZ15-…`, 7) ; Marienstras 2014, La résistance indienne aux États-Unis : Neolin 1762, conseil de Pontiac 1763 (`MR14-…`, 2) ; Bouchard et Lévesque 2011, Elles ont fait l'Amérique : Esther Wheelwright, Madame Montour, Susan La Flesche Picotte, Émilie Tremblay (`EF11-…`, 11) ; Balesi 2016, The Legacy of the French Canals : canal Illinois-Michigan et vision de Jolliet, L'Enfant à Washington (`BA16-…`, 2) ; Havard 2019, L'Amérique fantôme, lu en entier : Gambie en Floride, Pierre Beauchamp au fort Berthold, Junior Morsette, Lalande et Amiot (plaque de 1743), Toussaint Charbonneau (Awatichai, Saint-Ferdinand, guignolée de 1819, lac Traverse, fort Clark), mines de Perrot, « Maître Trudeau » (`HV19-…`, 11) ; McDermott, The Early Histories of St. Louis (1952) (`MD52-…`, 18) ; Ekberg et Person, St. Louis Rising (2015) (`EK15-…`, 89) ; Hämäläinen, L'Amérique des Sioux (2022) (`HS22-…`, 11) ; Sanborn, The Grand Tetons (1978) : Antoine Clément, chasseur de Stewart, de l'Ouest au château de Murthly ; duel Carson-Shunar (`SB78-…`, 4) ; Dary, The Santa Fe Trail (2000) : Pratte tué en 1833 sur la Canadienne ; deux Françaises à Chihuahua (Gregg) (`DY00-…`, 2) ; Flagg, The Far West (1838) : Charbonnière, mine Lochon, cloche de Kaskaskia, cour de 1768, saisie Hubardeau (`FL38-…`, 5) ; Werich, Pioneer Hunters of the Kankakee (1920) : Charlevoix chez les Loups (`WE20-…`, 1) ; Audubon, Journals vol. 1 (1843) : Omega, Chouteau, Bellevue, Rivière à Jacques, Fort Pierre (`AJ43-…`, 5) ; Dallas, Colorado Ghost Towns (1985) : Pierre Ardourel à Crisman (`DA85-…`, 1) ; Morrison, Superior Rendezvous-Place (2007) : Landriaux, Rototte, mission de la Kaministiquia (`JM07-…`, 3) ; Ottoson, « Toussaint Charbonneau, A Most Durable Man » (South Dakota History, 1976) (`OT76-…`, 13) ; We Proceeded On 26-1 (2000) : baptême de Pomp par Urbain Guillet (`WP00-…`, 1) ; Lecompte, « Charles Autobees » (*Colorado Magazine*, 1957-1958), chap. I-II et IX : Pierre Ortubise, Picking Bones Woman, mariage de 1842, concession de La Lama, procès Ortubise-Lucero, acte Craig, fort Reynolds, fandango de French Joe (`LA57-…`, 16) ; Murray, *Las Animas, Huerfano and Custer* (BLM, 1978) : Autobees Plaza premier chef-lieu (`MU78-…`, 1) ; Gutiérrez, « Carlos Beaubien » (notice, v. 2007) : la guía de Chihuahua (1826) (`PSG-…`, 1) ; Howard, *Sacajawea* (1971) : la tutelle de Lizette, Victoire Vertifeuille à Westport, la veuve shoshone du fort Lupton, la tradition de Wind River (`HO71-…`, 4) ; Bernand, *Histoire des peuples d'Amérique* (2019) : Cartier à Stadaconé, Le Jeune et Carigonan, les hiéroglyphes de Maillard, La Pérouse à la baie Lituya (`BE19-…`, 4) ; Sagard, *Le Grand Voyage du pays des Hurons* (1632, éd. Warwick 1998) : de Gaspé à la Huronie et retour (1623-1624), Quieunonascaran, Toenchain, la Chaudière, la noyade de Viel (`SG32-…`, 14) ; Viau, *Amerindia* : Hochelaga, Roberval à Lachine, Fénelon à Gentilly, l'île Perrot, l'Île-aux-Tourtes, Nicollet chez les Népissingues (`VIA-…`, 6) ; Skarsten, *George Drouillard, Hunter and Interpreter for Lewis and Clark* (1964) (`SK64-…`, 15) ; Chaput, *Virgil Earp, Western Peace Officer* (1994-1996) (`CP94-…`, 2) ; Louder (dir.), *The Heart of French Canada* (1992), Est ontarien (`LO92-…`, 4) ; Louder, *Rencontres et voyages en Franco-Amérique* (2013) (`LO13-…`, 21) ; Louder et Waddell (dir.), *French America* (1993) (`FR93-…`, 26) ; Société d'histoire de Cournoyer, Blanchard et Loiselle de Saint-Marc (2018) (`BSM-…`, 3) ; Cragin, *Early Far West Notebooks*, compléments (`CRG-…`, 3) ; Dossier Chicago du Drive : dépliant, Diamond et Ndiaye, cartes de 1830-1833 (`CHF-…`, 4) ; x (`WT85-…`, 7) ; Compléments du lot FRENCH_CANADIAN_USA / FUR_TRADE_USA / GERVAIS_NOLAN : Mackie (1997), Vermette (2018), Luttig (1920), Kennedy (1962) et une chronologie de la concession Nolan (`LUS-…`, 6) ; x (`LC78-…`, 2) ; Carter, « Tom Tobin », The American West (1965) : le demi-frère de Charles Autobees, « Tom Autobees » jusqu'en 1853 (`CT65-…`, 4) ; Hafen (dir.), The Mountain Men and the Fur Trade of the Far West, vol. I (1965) : Chardon, Chatillon, La Barge (`MM1-…`, 6) ; Hafen et Hafen, Old Spanish Trail (1954) : Tiboux, Auchambeau (`OST54-…`, 2) ; Deschênes, Un pays rebelle (Côte-du-Sud et guerre de l'Indépendance) : Gosselin, Ayotte, réfugiés canadiens du lac Champlain (`DS23-…`, 11) ; Waselkov, *Old Mobile Archaeology* (1999), lu en entier : fondation du fort Louis, dénombrements de 1704 et 1708, Séminaire de Québec, briqueterie, le Pélican à Port-Dauphin, cabaret Burelle, pirates de 1710, forge, redécouverte de 1989, arrivée des Apalaches, contrebande avec Veracruz (`WA99-…`, 12) ; Dubois, Leumas et Richardson, *Speaking French in Louisiana, 1720-1955* (2018), lecture partielle : Avoyelles 1835, séminaire de l'Assomption 1841, Notre-Dame-de-Bon-Secours 1854, Carrollton 1859 (`DU18-…`, 4) ; fichiers isolés du Drive (`drive_racine_2026.py`) : Marchand, *L'Empire fantôme* (2008) — fouille du fort Saint-Louis du Texas, statues de La Salle à Indianola et Navasota, fresques de Nicolet à Green Bay, « Mushrat French » de Monroe, Pittsfield 1867-1868, Charlene Richard, paroisse Saint-Augustin (`PM05-…`, 8) ; New Mexico Roots, vol. 2 : Enrique Blanco, « natif du Canada », à Taos en 1832, Victor Bardaux à Socorro en 1849 (`NMR2-…`, 2) ; Keith, *The Colfax Massacre* (2008) : Rigolette de Bon Dieu, Narcisse Fredieu, Denis Lemoine (`KE08-…`, 3) ; Barile 2010 : Pierre à Flèche (Arrow Rock) (`MB10-…`, 1) ; Fraïssé, *Radisson* (2008) : Trois-Rivières 1652, Gannentaha 1658, rivière Bourbon (`FR08-…`, 3) ; sous-dossiers du Drive (`drive_dossiers_2026.py`) : Cook, « ¿Porque Monterrey? » (*Wagon Tracks* 19-3, 2005), Manuel Alvarez et les frères Mercure (`WT05-…`, 2) ; Montoya (2002), l'acte de 1863 de Beaubien pour San Luis (`MT02-10`) ; Dionne (1910), Québec 1660, évasion de Trois-Rivières 1661, Percé 1682, le capitaine Berger 1685 (`DN10-02` à `05`) ; Turner (2015), Jean-Baptiste Rousseau, Ganatsekwyagon, Jacques Baby (`TU15-02` à `04`) ; Gitlin, Berglund et Arenson (dir.), *Frontier Cities* (2013), Pierre Roy et Marguerite Ouabankikoué, Kekionga 1728, le procès Lamoureux de 1713 (`FC13-…`, 3) ; Kane, *Les Indiens de la baie d'Hudson* (1861), rocher de Miette, Dalles des Morts, François Lucie (`KN61-…`, 3) ; NPS, *Comprehensive Management and Use Plan* (1990), magasin de Cyprien Chouteau à Westport (`NPS90-01`) ; *Santa Fe Weekly Gazette* (1863), Henry Mercure à Tierra Amarilla (`GZ63-01`) ; Gutierrez, « Thomas Oliver Boggs » (*Wagon Tracks* 23-3, 2009), Boggsville (`WT09-01`) ; Joly, mémoire sur Berlin (New Hampshire) (2003) (`JO03-…`, 2). Modules dans `scripts/sources_2026b/`. |
| **Atlas Aubry** | 100 | Renvois courts vers les fiches de l'Atlas Aubry (identifiants `A-Lxx` inchangés) : nom, date, lieu, une phrase et un bouton vers la fiche complète, qui garde ses sources et ses images. |

Chaque fiche Cragin renvoie aux **pages du PDF** (`pages_pdf`) où se trouve le témoignage.

## Salle de lecture : les traiteurs et voyageurs français

`salle.html` offre **un onglet par personnage** du livre *French Fur Traders and Voyageurs in the American West* (22 notices + introduction), chacun avec sa couleur propre, son récit chronologique par phases, sa carte de parcours (trait pointillé, puis trait plein « déjà parcouru »), son **échelle de temps** cliquable, une liste de **pistes d'archives inédites** (sources primaires citées en note par les auteurs, ou proposées par l'atlas) et sa bibliographie. Données : `data/personnages/index.json` et `data/personnages/<id>.geojson`. Adresses directes : `salle.html#chouteau`, `salle.html#vasquez-14`.

Maurice LeDuc (onglet `leduc`, bleu ciel `#00a8e8`, couleur réservée dans tout l'atlas) réunit les 30 étapes de la première salle et 33 étapes tirées de la notice de Janet Lecompte (p. 176-189) : Fort Manuel (1812), mariage de Taos (1823), Pegleg Smith, Gila, Ashley, Frémont (1843), mariage de San Miguel (1848), recensement de 1850, etc. L'ancienne adresse `maurice-leduc.html` redirige vers cet onglet.

**Traduction et droit d'auteur.** Les passages du livre sont résumés et traduits librement en français ; les citations sont très brèves et signalées. Les sources primaires (lettres, registres, journaux) sont décrites et localisées, non reproduites.

## Pages de lecture (novembre 2026)

`canadiens-ouest.html` (Tassé, t. I et II : carte, schémas des liens, 35 vies), `montagnards.html` (Hafen, vol. 2 et 4-9 : 229 biographies, 7 708 lieux datés, carte filtrable), `illinois-francais.html` (onze sources sur l'Illinois français et le Midwest, habitants de Peoria, presse). Chaque page a sa version anglaise (`-en.html`). Ces pages viennent de l'Atlas Aubry, qui ne garde que ce qui touche Aubry et son entourage ; elles sont générées par les scripts de l'Atlas Aubry (`vers_cf.py`). Données : `data/tasse*.geojson`, `data/hafen.geojson`, `data/hafen_personnes.json`, `data/illinois_francais.geojson`, `data/peoria_habitants.json`.

## Structure

```
index.html            page principale (carte, filtres, chronologie, fiches)
css/style.css         mise en page
js/atlas.js           carte, filtres, chronologie, fiches, recherche, index des personnages
js/fonds.js           fonds de carte d'époque (repris de l'Atlas Aubry)
data/lieux.geojson    points (EPSG:4326)
data/themes.json      libellés des thèmes
data/piste.geojson    contexte : relevé de la piste de Santa Fe (Atlas Aubry)
images/aubry/         documents de l'Atlas Aubry
scripts/              scripts de construction (Cragin, recherches, Hafen, ffv/ = un module par personnage du livre)
salle.html, js/salle.js, css/salle.css   salle de lecture multi-personnages
data/personnages/     un GeoJSON par personnage + index.json
```

## Modèle d'attributs (`data/lieux.geojson`)

| Champ | Exemple | Rôle |
|---|---|---|
| `id` | `C042`, `A-L01` | identifiant stable (C = Cragin, A- = Atlas Aubry) |
| `nom` | `Fort Vasquez (Platteville)` | libellé |
| `corpus` | `Cragin` / `Atlas Aubry` | source principale |
| `theme` | `poste`, `etablissement`, `famille`, `personnage`, `evenement`, `commerce`, `migration`, `exploration`, `religion`, `toponymie` | catégorie (couleur) |
| `debut`, `fin` | `1835.0`, `1860.5` | années décimales (filtrage chronologique) |
| `date_edtf` | `1847-01-19`, `1820~` | date documentée ([EDTF](https://www.loc.gov/standards/datetime/)) |
| `precision` | `jour` / `mois` / `annee` / `circa` | précision de la date |
| `certitude` | `certaine` / `approximative` / `hypothetique` | certitude de la **localisation** |
| `personnages` | `["Céran St. Vrain", "Felix St. Vrain"]` | personnes liées (index des personnages) |
| `description` | | résumé rédigé pour l'atlas |
| `sources` | | référence complète |
| `pages_pdf` | `63; 64` | pages du PDF des carnets Cragin |
| `note` | | note critique : divergences entre témoins, identification incertaine |
| `images` | `[{"src": "images/…", "legende": "…"}]` | documents (fiches Aubry) |

Les fiches qui partagent exactement le même point (Taos, Mora…) sont légèrement décalées à l'affichage ; un clic sur un groupe affiche la liste.

## Ajouter un corpus

Ajouter des entités dans `data/lieux.geojson` avec une nouvelle valeur de `corpus`, puis déclarer ce corpus dans l'objet `CORPUS` de `js/atlas.js` (libellé et couleur du contour).

## Tester en local

```
python -m http.server 8000
```

puis ouvrir http://localhost:8000.

## Publier

*Settings → Pages → Source : Deploy from a branch → `main` / `(root)`*.

## Avertissement

Les carnets de Cragin rapportent des souvenirs recueillis des décennies après les faits ; les informateurs se contredisent parfois (lieu et date de la mort de Maurice LeDuc ou de Joseph Levanway, par exemple). Ces divergences sont signalées dans les notes. Les récits d'O. P. Wiggins, réputé pour ses exagérations, sont marqués comme tels.

## Hub entre les atlas : Atlas de l'Amérique française

Cet atlas est l'**accueil du réseau** « Atlas de l'Amérique française » : le panneau d'accueil présente les atlas du réseau d'après le registre `data/atlas.json` (une entrée par atlas : titre, description, adresse, couleur, pages ; `ici: true` pour cet atlas), et le bouton « ⚜ Les atlas » de l'en-tête y ramène. Les atlas de personnages et de familles (Aubry, Iberville, Jolliet, Robidoux) apparaissent sur la carte sous forme de renvois courts (`A-Lxx`, `I-Lxx`, `J-Lxx`, `R-Lxx`). L'ancienne adresse du portail (Atlas-de-l-Am-rique-fran-aise) redirige ici.

Chaque fiche vit dans un seul atlas ; les autres y renvoient par un lien profond, sans recopier le contenu. Les adresses des pages et les identifiants des fiches ne changent pas.

- Champ commun `voir_aussi` : liste de `{"url": …, "texte": …}`, affichée en boutons dans la fiche (les deux atlas).
- Liens profonds : `Atlas-Aubry/index.html#lieu=L78` ; `Atlas-Les-Canadiens-Fran-ais-de-l-Ouest/index.html#AH-sf08` ; `montagnards.html#p=H6-371` ; `salle.html#vasquez`.
- `scripts/hub.py` réduit le corpus Atlas Aubry à des renvois, crée les renvois des Atlas Iberville, Jolliet et Robidoux depuis leurs clones locaux (variables `IBERVILLE`, `JOLLIET`, `ROBIDOUX`) et pose les renvois des autres fiches (`VOIR_AUSSI`).
- Chaîne de production : `build.py` → `ajouts_2026_11.py` → `ajouts_2026_11b.py` → `hub.py` → `page_provost.py`.
- Pour un nouvel atlas de personnage : lui donner le même champ `voir_aussi` et un lien d'en-tête vers les autres atlas, puis ajouter ses renvois dans `hub.py`.

## Publier une nouvelle version

GitHub Pages laisse les navigateurs garder les fichiers en cache une dizaine de minutes. À chaque publication, changer le numéro `?v=` de `index.html` (scripts et feuille de style) : `js/atlas.js` le reprend pour charger les données (`lieux.geojson`, `themes.json`, `atlas.json`).

## Bibliothèque archive.org (en cours, par lots)

Dépouillement des livres du **domaine public** d'archive.org sur les francophones d'Amérique du Nord hors Québec : chaque livre forme un corpus `archive.org · <livre>` (groupe « Bibliothèque archive.org » du filtre Corpus).

- Méthode : lecture du texte intégral (OCR) par tranches ; une ligne par personne dans `scripts/sources_archive/<livre>.txt` (`NOM, Prénoms | naissance | lieu, année {contexte}; … | référence`) ; lieux résolus par `scripts/sources_archive/lieux_ouest.py` ; une fiche par lieu daté, avec le contexte de la présence (rôle, événement) paraphrasé du livre. Script : `scripts/ajouts_archive.py` (après `ajouts_2026_11b.py`, avant `hub.py`).
- Chaque fiche cite le livre (entrée ou page) et renvoie au livre sur archive.org (recherche du nom dans le texte). Repérage à vérifier ; localisation attribuée par l'atlas.
- Livres sous droit d'auteur (Hafen, *The Mountain Men* ; Lecompte) : prêt seulement sur archive.org, non lisibles ici ; à fournir en PDF.

| Livre | Identifiant archive.org | Fiches |
|---|---|---|
| Morice, *Dictionnaire historique des Canadiens et des Métis français de l'Ouest* (1908) | `dictionnairehist00mori` | 715 (dont 457 avec contexte, `morice_1908_contextes.txt`) |
| Larpenteur, *Forty Years a Fur Trader on the Upper Missouri*, éd. Coues (1898), 2 vol. | `fortyyearsfurtra01larpiala`, `fortyyearsfurtra02larpiala` | 129 |
| Tassé, *Les Canadiens de l'Ouest* (1878), 2 tomes | `cihm_33778`, `cihm_33779` | 555 |
| Billon, *Annals of St. Louis in its Early Days under the French and Spanish Dominations* (1886) | `cihm_00427` | 430 |
| Hamon, *Les Canadiens-français de la Nouvelle-Angleterre* (1891) | `cihm_39098` | 183 |
| Dugas, *L'Ouest canadien* (1896) | `cihm_30150` | 102 |
| Dugas, *Histoire de l'Ouest canadien de 1822 à 1869* (1906) | `histoiredelouest00dugauoft` | 56 |
| Dugas, *Un voyageur des pays d'en haut* (1890) | `unvoyageurdespay00duga` | 23 |
| Dugas, *La première Canadienne du Nord-Ouest* (1883) | `lapremirecanadi00duga` | 38 |
| Dugas, *Monseigneur Provencher et les missions de la Rivière-Rouge* (1889) | `monseigneurprove00duga` | 86 |
| Houck, *A History of Missouri* (1908), vol. 1 | `historyofmissour01houc` | 265 |
| Houck, *A History of Missouri* (1908), vol. 2 | `historyofmissour02houc` | 338 |
| Houck, *A History of Missouri* (1908), vol. 3 | `historyofmissour03houc` | 125 |
| Houck, *The Spanish Regime in Missouri* (1909), vol. 1 | `spanishregimeinm01houc` | 325 |
| Houck, *The Spanish Regime in Missouri* (1909), vol. 2 | `spanishregimeinm02houc` | 177 |
| Chittenden, *The American Fur Trade of the Far West* (1902), vol. 1 | `americanfurtrade01chit` | 98 |
| Chittenden, *The American Fur Trade of the Far West* (1902), vol. 2-3 | `americanfurtrade00chit_0` | 52 |
| Franchère, *Narrative of a Voyage to the Northwest Coast of America* (trad. 1854) | `cihm_35175` | 42 |
| Masson, *Les Bourgeois de la Compagnie du Nord-Ouest* (1889), vol. 1 : liste des engagés de 1804, un point par département | `cihm_30414` | 656 |
| Masson (1889), vol. 1 : journaux de Malhiot (lac du Flambeau, 1804-1805), McDonnell (1793-1795), Larocque et Charles McKenzie (Mandanes, 1804-1806) | `cihm_30414` | 60 |
| Masson, *Les Bourgeois de la Compagnie du Nord-Ouest* (1890), vol. 2 : McDonald of Garth, Keith, Johnston, Wilcocke (mort de Frobisher), Cameron (Nipigon), James McKenzie (fort Chipewyan) | `cihm_30415` | 59 |
| Coues (dir.), *New Light on the Early History of the Greater Northwest* (1897), vol. 1 : journal d'Alexander Henry le jeune à la rivière Rouge (1799-1808) | `newlightonearlyh01henr` | 155 |
| Coues (dir.), *New Light* (1897), vol. 2 : Henry en Saskatchewan (1808-1811) et au fort George/Astoria (1813-1814), notes tirées de Thompson | `newlightonearlyh02henr` | 164 |
| Perrault, « Narrative of the Travels and Adventures of a Merchant Voyageur » (1783-1820), *Michigan Pioneer and Historical Collections*, vol. 37 (1910) | `michiganhistoric37michuoft` | 82 |
| Cox, *Adventures on the Columbia River* (1832) | `adventuresoncolu00coxr` | 48 |
| Ross, *The Fur Hunters of the Far West* (1855), 2 vol. | `cihm_40228`, `cihm_40229` | 12 |
| Burton, *Cadillac's Village, or Detroit under Cadillac* (1896) : lots du village et répertoire des habitants, 1701-1710 | `cadillacsvillage00burt` | 151 |
| Hamlin, *Legends of le Détroit* (1884) : légendes situées et notice des anciennes familles françaises | `legendsofledtr00haml` | 58 |
| « Cadillac Papers », *Michigan Pioneer and Historical Collections*, vol. 33 (1904) | `michiganhistoric33michuoft` | 62 |
| « Cadillac Papers » (suite) et « Detroit Rulers », *Michigan Pioneer and Historical Collections*, vol. 34 (1905) | `michiganhistoric34michuoft` | 49 |
| Ross et Catlin, *Landmarks of Detroit* (1898), partie historique jusqu'en 1832 | `landmarksofdetr00ross` | 44 |
| Andreas, *History of Chicago*, vol. 1 (1884) : Chicago français et métis jusqu'en 1832 | `historyofchicago01andr` | 40 |
| *Portrait and Biographical Record of Kankakee County* (1892) : Canadiens de Bourbonnais, Sainte-Anne et Kankakee | `portraitbiographica00lake` | 38 |
| `cu31924092232747` | 22 |
| `transactionsrepo00nebr` | 9 |
| `bwb_P8-BLU-581` | 9 |
| `cu31924028874141` | 7 |
| `collectionofnebr00daug` | 11 |
| Andreas (1882), transcription kancoll.org | 29 |
| `idahochronologyn00reesrich` | 12 |
| `historyofstateof00bros` | 14 |
| `illustratedhisto00slwe` | 15 |
| `driggs` | 13 |
| `historyofidahoge01hawl` | 11 |
| `OregonMissionsAndTravels` | 9 |
| `historyidaho1884` | 23 |
| `adventuresofcap00irvi` | 22 |
| `historyofwashing31banc` | 6 |
| `historyofwashing31banc` (Montana) | 46 |
| `IndianAndWhiteInTheNW` | 35 |
| `contributionstohvol1hist1876rich` | 22 |
| `contributionstohvol2hist1896rich` | 32 |
| `contributionstohvol3hist1900rich` | 17 |
| `contributionstohvol7hist1910rich` | 4 |
| `contributionstoh08mont` | 5 |
| `contributionstohvol9hist1923rich` | 6 |
| `illustratedhisto00mill` | 22 |
| `historyofmontana11sand`, `historyofmontanab02sand`, `historyofmontana03insand` | 26 |
| `historyofwyoming00cout` | 65 |
| `historyofwyoming01bart` | 11 |
| `bozemantrailhist01heba`, `bozemantrailhist02heba` | 7 |
| `historyofwyoming02bart` | 5 |
| Progressive Men of Wyoming (1903), transcription rootsweb | 3 |
| `annalsofwyom114192324wyom` à `annalsofwyom514192728wyom` | 43 |
| `nevcolandwyom00bancroft` (partie Wyoming) | 19 |
| `annalsofwyom614192930wyom`, `annalsofwyom714193031wyom` | 20 |
| `historyofutah00bancrich` | 11 |
| `ashleysmithexplo00daleuoft` | 15 |
| `reportoftheexplor1845eng` (partie Utah) | 11 |
| `explorationsurve001853stan` | 12 |
| `ajourneytogreat01brengoog`, `ajourneytogreat00remygoog` | 8 |
| `romanceofcolorad00dell` | 3 |
| `utah-historical-quarterly_1929-10_2_4` à `_1930-07_3_3` | 6 |
| `historyofutahcom01whit` | 8 |
| `historyofsaltlak00tull` | 1 |
| `catholicchurchin0000harr_k0t3` | 9 |
| `pioneersprominen00esshrich`, `pioneersprominen02essh` | 36 |
| `cityofsaintsacro00burtuoft` | 15 |
| `historyofutahcom04whit` | 3 |
| `tullidgeshistori02tull` | 3 |
| `compendiumhistor00chic` | 34 |
| `ndcollections01nortuoft` | 224 |
| `collectionsofsta02stat_0` | 15 |
| `collectionsofsta03stat` | 25 |
| `collectionsofsta04stat_0` | 9 |
| `collectionsofsta05stat` | 7 |
| `collectionsofsta06stat_0` | 3 |
| `collectionsofsta07stat` | 17 |
| `earlyhistoryofno01loun` | 40 |
| `northdakotahisto02loun` | 7 |
| `northdakotahisto03loun` | 7 |
| `illustratedalbum00alde_0` | 30 |
| `historyofredrive01chicuoft` | 64 |
| `outwherewestbeg00tringoog` | 15 |
| `northdakotahisto01loun` | 43 |
| `historyofdakotaterr01king` | 29 |
| `historyofdakotat02king` | 4 |
| `historyofdakotat04king` | 13 |
| `historyofdakotat05king` | 12 |
| `fortyyearsinnort00arno` | 2 |
| `empirebuildersof00arms` | 4 |
| `historyofdakotat03king` | 2 |
| `narrativeofcanad01hind` | 5 |
| `historyofutahcom02whitrich`, `historyofutahcom03whit` | 5 |
| `nevcolandwyom00bancroft` (partie Nevada) | 12 |
| `reportoftheexplor1845eng` (partie Nevada) | 4 |
| `historyofnevada00ange` | 29 |
| `historyofstateof00wren` | 16 |
| `historyofnevada01davirich`, `historyofnevada02davirich` | 17 |
| `sim_nevada-historical-society-papers_1913-1916` à `_1925-1926` | 6 |
| `historyofbigbona00dequ` | 5 |
| `arizonanewmex00bancroft` (partie Arizona) | 10 |
| `soldiersofcrossn00salp` | 22 |
| `portraitbioarizo00chaprich` | 17 |
| `arizonaprehistor01mcclrich` | 17 |
| `arizonaprehistor02mcclrich` | 8 |
| `arizonaprehistor03mcclrich` | 20 |
| `historyofarizona01faririch`, `historyofarizona02faririch` | 7 |
| `reportanexpidit00sitggoog` | 5 |
| `conquestofnewmex00cookrich` | 6 |
| `arizonahistorica03univ` (n° 1-3, 1930) | 2 |
| `historyofarizona03faririch` à `historyofarizona08faririch` | 12 |
| `thenorthmexivol115bancmiss`, `northmexicanst02bancrich` (Texas) | 47 |
| `historyoftexasfr01yoak`, `historyoftexasfr02yoak` | 50 |
| `reminiscencesoft00pari` | 46 |
| `missionaryadvent00dome` | 27 |
| `napoleonicexiles00reev` | 15 |
| `athanasedemzi01mz`, `athanasedemzi02mzuoft` | 62 |
| `pictorialhistory01thra` | 17 |
| `memorialbiograph00lew` | 38 |
| `earlysettlersind00sowe` | 28 |
| `journeythroughte01olms` | 8 |
| `ahistorytexasan01winkgoog`, `historyoftexaste04john` | 50 |
| `TexasInTheMiddle18thC` | 23 |
| `historyoftexasfr01brow`, `historyoftexasfr02brow` | 11 |
| `indianwarspionee00brow` | 21 |
| `journeysrnrober06coxgoog` | 15 |
| `menwhomadetexasf00dixo` | 5 |
| `southwesternhist10bark`, `17bark`, `19bark`, `20bark` | 20 |
| `spanishfrenchriv01dunn` | 10 |
| `texastexansoradv01foot`, `texastexansoradv02foot` | 1 |
| `beginningsoftexa00clar` | 11 |
| `sanantoniodebexa00corn` | 5 |
| `texasriseprogre01kenngoog` | 4 |
| `louisianacompris01fort` (Louisiane) | 133 |
| `louisianacompris02fort` | 106 |
| `louisianacompris03fort` | 156 |
| `southwestlouisia00perr` | 403 |
| `historyoflouisia01gayaiala` | 166 |
| `historyoflouisia02gayaiala` | 102 |
| `cihm_45094` | 54 |
| `cihm_45095` | 93 |
| `historicalmemoi00latogoog` | 70 |
| `creolesoflouisia00cabluoft` | 63 |
| `historyoflouisia01fortuoft` | 126 |
| `historyoflouisia02fortuoft` | 86 |
| `historyoflouisia03fortuoft` | 124 |
| `historyoflouisia04fortuoft` | 75 |
| `nouveauxvoyagesa00boss_0` | 79 |
| `cihm_36229` | 121 |
| `cihm_36231` | 88 |
| `historicalcollec00fren_1` | 80 |
| `creolefamiliesof00king` | 103 |
| `histoiredecomit00bard` | 92 |
| `louisianastudie00fortgoog` | 46 |
| `neworleansplacep00king` | 61 |
| `historyoflouisia0002unse` | 119 |
| `historyoflouisia0003unse` | 130 |
| `presentstateofeu00pitt` | 20 |
| `per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1917-01-08_1_1` | 176 |
| `per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1919-01_2_1` | 163 |
| `per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1920-01_3_1` | 202 |
| `per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1921-01_4_1` | 147 |
| `per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1922-01_5_1` | 165 |
| `per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1923-01_6_1` | 170 |
| `per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1924-01_7_1` | 167 |
| `per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1925-01_8_1` | 160 |
| `per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1926-01_9_1` | 148 |
| `per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1927-01_10_1` | 109 |
| `per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1928-01_11_1` | 143 |
| `per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1929-01_12_1` | 285 |
| `per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1930-01_13_1` | 358 |
| `louisianahistori01loui` | 94 |
| `publicationslou01socigoog` | 29 |
| `publicationslou04socigoog` | 40 |
| `publicationslou03socigoog` | 18 |
| `louisianahistori08loui` | 42 |
| `publicationslou06socigoog` | 34 |
| `louisianahistori10loui` | 18 |
| `historyoflouisia00lepa` | 52 |
| `mmoireshistori01dumo` | 85 |
| `earlyvoyagesupdo00shea` | 34 |
| `mmoiresetdocum04marg` | 44 |
| `mmoiresetdocum05marg` | 97 |
| `cihm_09946` | 95 |
| `dcouverteett01marg` | 56 |
| `dcouverteett02marg` | 38 |
| `dcouverteett03marg` | 44 |
| `inacadiaacadians00john` | 9 |
| `stbernardparishl00stbe` | 8 |
| `CatholicHistoryOfAlabamaAndTheFloridasV1` | 56 |
| `AHistoryOfTheCatholicChurchV1` | 113 |
| `ahistorycatholi00sheagoog` | 129 |
| `historychurchusa03sheauoft` | 137 |
| `historychurchusa04sheauoft` | 132 |
| `publicationsofmi3190unse` | 6 |
| `publicationsmis05rilegoog` | 4 |
| `publicationsmis09socigoog` | 6 |
| `publicationsmis07socigoog` | 17 |
| `publicationsmis05socigoog` | 17 |
| `publicationsmis00rilegoog` | 26 |
| `publicationsmis00socigoog` | 2 |
| `publicationsmis01socigoog` | 11 |
| `publicationsofmi12rowl` | 14 |
| `publicationsofmi04rowl` | 2 |
| `publicationsofmi0005vari` | 29 |
| `colonialmobilehi01hami` | 278 |
| `mississippicompr01rowl` | 87 |
| `mississippicompr02rowl` | 88 |
| `SketchOfTheCatholicChurchInTheCity` | 40 |
| `oldbiloxifirstse00rowl` | 4 |
| `cu31924073559761` | 34 |
| `cu31924028795405` | 105 |
| `ahistorymississ00mccagoog` | 44 |
| `biographicalhist11good` | 83 |
| `biographicalhist21good` | 38 |
| `cihm_38028` | 38 |
| `cihm_38029` | 3 |
| `mississippiprovi01missuoft` | 20 |
| `mississippiterri01missuoft` | 8 |
| `reportonagricult00miss` | 42 |
| `mississippicompr03rowl` | 7 |
| `publications01arka` | 4 |
| `publications02arka` | 30 |
| `publications03arka_0` | 7 |
| `publications04arka` | 7 |
| `pictorialhistory00hemp` | 54 |
| `centennialhistor0001dall` | 46 |
| `biographicalhistpjlf00good` | 28 |
| `biographicalhist00good_0` | 18 |
| `biographicalhist02good_0` | 7 |
| `biographicalhist00sout_0` | 12 |
| `makersofarkansas01reyn` | 4 |
| `biographicalpict01hall` | 2 |
| `journaloftravels00nutt` | 12 |
| `biographicalhist02good` | 9 |
| `centennialhistor00hern` | 6 |
| `pioneersandmake00shingoog` | 45 |
| `travelsthroughth01boss` | 2 |
| `historicalreview03hemp` | 1 |
| Andreas et Cutler (1883), transcription kancoll.org | 96 |
| `collectionsofkan08kans_0` | 9 |
| `collectionsofkan09kans` | 37 |
| `collectionsofkan10kans_0` | 8 |
| `collectionsofkan13kans` | 6 |
| `collectionsofkan1619kans` | 62 |
| `collectionsofkan1719kans` | 8 |
| `collectionsofkan12kans_0` | 2 |
| Blackmar (1912), transcription ksgenweb.org | 48 |
| `standardhistoryo01conn` | 32 |
| Hollibaugh (1903), transcription ksgenweb.org | 49 |
| Ramsey (1853), transcription ldsgenealogy.com | 6 |
| Albright (1909), transcription ahgp.org | 2 |
| Goodspeed, Shelby (1887), transcription usgwarchives.us | 7 |
| `historymiddlete00putngoog` | 6 |
| `historyofdavidso00clay` | 12 |
| `standardhistoryo00youn` | 19 |
| `tennesseehistori02tennuoft` | 8 |
| `tennesseehistori04tennuoft` | 4 |
| `tennesseehistori05tennuoft` | 1 |
| `civilpoliticalhi00hayw` | 5 |
| `historyofalabama01pick` | 72 |
| `historyofalabama04pick` | 19 |
| `cu31924028794042` | 28 |
| `mobileoffiveflag00hami` | 42 |
| `historyofalabama01owen` | 23 |
| `historyofalabama02owen` | 38 |
| `historyalabamaa02owengoog` | 10 |
| `historyalabamaa03owengoog` | 7 |
| `transactionsofal04alab` | 320 |
| `transactionsofal02alab` | 2 |
| `transactionsofal03alab` | 10 |
| `memorialrecordof00tayl` | 9 |
| `memorialrecordof21tayl` | 7 |
| `memorialrecordof22tayl` | 7 |
| `soldiersofcrossn00salp` (Nouveau-Mexique) | 66 |
| `arizonanewmex00bancroft` (Nouveau-Mexique) | 22 |
| `historyofmilitar00twit` | 8 |
| `lifeofrightrever00howl` | 35 |
| `cu31924105349660` | 20 |
| `illustratedhisto00readrich` | 50 |
| `aconcisehistory00pringoog` | 24 |
| `histnewmexico00prin` | 17 |
| `oldsantaftrailst00inma` | 9 |
| `commerceofprairi01greg` | 1 |
| `spanisharchiveso01twituoft` | 22 |
| `spanisharchiveso02twituoft` | 17 |
| `oldsantafemagazi01unse_1` | 25 |
| `oldsantafemagazi02unse` | 4 |
| `oldsantafemagazi03unse` | 17 |
| `newmexicohistori01univrich` | 15 |
| `newmexicohistori02univrich` | 11 |
| `newmexicohistori04univrich` | 5 |
| `historyofnewmexi01paci` | 22 |
| `nevcolandwyom00bancroft` (partie Colorado) | 12 |
| `historyofstateof01hall` | 14 |
| `historyofstateof02hall` | 5 |
| `historyofstateof03hall` | 11 |
| `historyofstateof04hall` | 39 |
| `semicentennialhi01smil` | 20 |
| `historyofclearcr00olba` | 9 |
| `historycolorad01stat` | 17 |
| `historycolorad02stat` | 9 |
| `historycolorad03stat` | 4 |
| `historycolorad04stat` | 4 |
| `historycolorad05stat` | 2 |
| `sketchesofearlyc00spal` | 9 |
| `centenaryofcatho00webb` | 96 |
| `SketchesOfTheLifeTimes` | 18 |
| `centenaryoflouis00durr` | 22 |
| `collinshistorica01coll` | 9 |
| `collinshistorica02coll` | 5 |
| `historicaltribut00howl` | 8 |
| `memorialhistoryo02john` | 1 |
| `lesfranaisenca00levy` | 240 |
| `worksofhuberthow19bancrich` | 30 |
| `worksofhuberthow20bancrich` | 9 |
| `worksofhuberthow21bancrich` | 41 |
| `worksofhuberthow22bancrich` | 19 |
| `explorationterri01duflrich` | 27 |
| `voyageautourdumo02duha` | 4 |
| `voyagesencalifor00sain` | 7 |
| `worksofhuberthow24bancrich` | 12 |
| `voyageencaliforn00auge` | 30 |
| `historyoflosange00wils` | 28 |
| `illustratedhistoflacty00lewi` | 39 |
| `historyoftuolumn00lang` | 20 |
| `historyofsantacl00munr` | 19 |
| `historyofalamed00munr` | 7 |
| `historyofmontere00elli` | 3 |
| `historyofplacerc00ange` | 8 |
| `historyofnevadac00well` | 13 |
| `historyofyubacou00cham` | 14 |
| `historyofsiskiyo00well` | 17 |
| `historyofmendoci00palm` | 1 |
| `historyofmarinco00munr` | 6 |
| `historyofcontrco00munrrich` | 2 |
| `historyofsanmate00sanf` | 2 |
| `historyofhumbold00wwel` | 3 |
| `historyoftularec00wwel` | 1 |
| `historyofdelnort00bled` | 2 |
| `historyofsantacr00will` | 2 |
| `historyofsantacr00harr` | 1 |
| `historyofmercedc00park` | 1 |
| `historyofamadorc00maso` | 4 |
| `historyofsanluis00ange` | 13 |
| `historyofsantaba00maso` | 5 |
| `illustratedhisto00chic` | 4 |
| `historyofsolanoc00munr` | 3 |
| `historyofnapalak00palm` | 7 |
| `illustratedhisto00davi` | 7 |
| `cu31924051210965` | 6 |
| `historyofstockto00tink` | 3 |
| `historyofyubasut00dela` | 8 |
| `annalsofsanfranc00soul` | 5 |
| `historyofsolan00greg` | 9 |
| `historyofsanjoaq00tink` | 7 |
| `historyofcityofs00hitt` | 5 |
| `historyofcalifor02hittuoft` | 11 |
| `historyofcalifor03hitt` | 10 |
| `historyofcalifor04hitt` | 1 |
| `historyofcalifor01hitt` | 1 |
| `historicalsketch00blan` | 33 |
| `historyofwillame00lang` | 44 |
| `historyoforegon01banc` | 103 |
| `historyoforegon02banc` | 27 |
| `historyoforegon100gray` | 35 |
| `portraitbiographwo00inchap` | 5 |
| `adventuresoffirs00ross` | 25 |
| `astoriaoranecdo02irvigoog` | 5 |
| `astoriaoranecdo00irvigoog` | 21 |
| `cihm_15234` | 13 |
| `centennialhistor01gast` | 89 |
| `centennialhistor02gast` | 9 |
| `centennialhistor03gast` | 16 |
| `centennialhistor04gast` | 11 |
| `portraitbiographwvor00chap` | 8 |
| `historyofsouther00wall` | 33 |
| `quarterlyoforego01oreg` | 48 |
| `quarterlyoforego13oreg` | 70 |
| `quarterlyoforego15oreg` | 4 |
| `quarterlyoforego04oreg` | 10 |
| `illustratedhisto00hine` | 16 |
| `illustratedhisto00stee` | 82 |
| `historicsketches00gilb` | 72 |
| `illustratedhisto01stee` | 17 |
| `historyofwashing01hawt` | 16 |
| `lymanshistoryofo01lyma` | 72 |
| `illustratedhisto00edwa` | 34 |
| `historyofcityofs01durh` | 66 |
| `illustratedhistorkykc00inte` | 56 |
| `illustratedhisto00lyma` | 29 |
| `historyofyakimav01lyma` | 88 |
| `historyofpugetso01pros` | 13 |
| `washingtonhistor14wash` | 8 |
| `WHQ (journals.lib.washington.edu)` | 98 |
| `washington_bagley_1916` | 10 |
| `washington_snowden_1909` | 25 |
| `washington_skagit_1906` | 18 |
| `colorado_hafen_overland_1926` | 1 |
| `colorado_magazine_1923_1929` | 13 |
| `colorado_magazine_1930_1935` | 8 |
| `colorado_magazine_1936_1938` | 5 |
| `colorado_magazine_1939_1948` | 27 |
| `colorado_magazine_1949_1953` | 26 |
| `colorado_magazine_1954_1959` | 12 |
| `colorado_magazine_1960_1978` | 4 |
| `colorado_magazine_complements` | 26 |
| `wahtoyahtaostrai00garr` | 18 |
| `scenesinrockymou00sage` | 4 |
| `historyofcityofd00inolba` | 10 |


## Un point par lieu et adresses précises

Sur la carte, les fiches qui partagent exactement les mêmes coordonnées forment un seul point, dont la taille dépend du nombre de fiches visibles (selon les filtres et la période). Un clic ouvre la liste des fiches du lieu, regroupées par décennie, avec un filtre rapide. Les points dont toutes les fiches ont une localisation hypothétique (région, district) sont dessinés en pâle avec un contour brun et signalés comme « localisation approximative ». Les adresses `index.html#ID` des fiches ne changent pas.

Quand une source donne une adresse précise, la fiche quitte le point générique de la ville et rejoint son propre emplacement. Pour Saint-Louis, les coins de rues cités par Billon (1886) sont reconstitués sur le quadrillage actuel du centre-ville (`scripts/sources_archive/adresses.py`, précision d'environ 50 m) ; la liste est dans `billon_1886_adresses.txt` (une ligne par adresse : nom, années, rues, angle, description, page).

Les concessions verbales de Laclède (1765), que Billon énumère par numéro d'îlot (p. 37-39), sont placées dans la bonne partie de leur îlot (moitié, quart ou sixième) grâce à `billon_1886_ilots.txt`. La numérotation des îlots a été reconstituée et recoupée avec une dizaine d'adresses données ailleurs par Billon : îlots 1 à 12 entre le fleuve et Main, du sud au nord (7 = place d'Armes) ; 27 à 41 entre Main et Second, du nord au sud (34 = îlot de Laclède) ; 52 à 64 entre Second et Third, du sud au nord (59 = îlot de l'église). Les îlots 13 à 26, 42 à 51 et au-delà de 64 (par exemple 18, 44 ou 82) restent non placés faute de repère sûr.
