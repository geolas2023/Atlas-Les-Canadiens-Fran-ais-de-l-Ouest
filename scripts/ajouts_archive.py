# Corpus « Bibliothèque archive.org » : dépouillement des livres du domaine public d'archive.org sur les francophones
# d'Amérique du Nord hors Québec (novembre 2026, en cours, par lots). Un fichier texte par livre dans scripts/sources_archive/.
# Idempotent : retire toutes les fiches du corpus puis les recrée. À lancer après ajouts_2026_11b.py et avant hub.py.
import json, os, sys, collections
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(R, 'scripts', 'sources_archive'))
from archive_commun import fiches_livre, lire_contextes, CORPUS

D = os.path.join(R, 'scripts', 'sources_archive')
LIVRES = [
    # (fichier, préfixe, description du livre, identifiant archive.org, citation)
    ('morice_1908.txt', 'MO',
     {'court': 'Morice (1908)',
      'ref': "Morice, Adrien-Gabriel (1908), Dictionnaire historique des Canadiens et des Métis français de l'Ouest, Québec, J.-P. Garneau"},
     'dictionnairehist00mori', lambda nom, ref: f"s.v. « {nom.split(',')[0].strip()} »"),
    ('larpenteur_1898.txt', 'LP',
     {'court': 'Larpenteur (1898)',
      'ref': "Larpenteur, Charles (1898), Forty Years a Fur Trader on the Upper Missouri, éd. Elliott Coues, New York, F. P. Harper, 2 vol."},
     lambda ref: 'fortyyearsfurtra01larpiala' if ref.startswith('vol. 1') else 'fortyyearsfurtra02larpiala',
     lambda nom, ref: ref),
    ('tasse_1878.txt', 'TA',
     {'court': 'Tassé (1878)',
      'ref': "Tassé, Joseph (1878), Les Canadiens de l'Ouest, Montréal, Compagnie d'imprimerie canadienne, 2 tomes"},
     lambda ref: 'cihm_33779' if ref.startswith('t. II') else 'cihm_33778',
     lambda nom, ref: ref),
    ('billon_1886.txt', 'BI',
     {'court': 'Billon (1886)',
      'ref': "Billon, Frederic L. (1886), Annals of St. Louis in its Early Days under the French and Spanish Dominations, Saint-Louis"},
     'cihm_00427', lambda nom, ref: ref),
    ('hamon_1891.txt', 'HA',
     {'court': 'Hamon (1891)',
      'ref': "Hamon, Édouard (1891), Les Canadiens-français de la Nouvelle-Angleterre, Québec, N.-S. Hardy"},
     'cihm_39098', lambda nom, ref: ref),
    ('dugas_1896.txt', 'DU',
     {'court': 'Dugas (1896)',
      'ref': "Dugas, Georges (1896), L'Ouest canadien : sa découverte par le sieur de La Vérendrye, son exploitation par les compagnies de traiteurs jusqu'à l'année 1822, Montréal, Cadieux et Derome"},
     'cihm_30150', lambda nom, ref: ref),
    ('dugas_1906.txt', 'DH',
     {'court': 'Dugas (1906)',
      'ref': "Dugas, Georges (1906), Histoire de l'Ouest canadien de 1822 à 1869 : époque des troubles, Montréal, Beauchemin"},
     'histoiredelouest00dugauoft', lambda nom, ref: ref),
    ('dugas_1890.txt', 'DV',
     {'court': 'Dugas (1890)',
      'ref': "Dugas, Georges (1890), Un voyageur des pays d'en haut, Montréal, C.-O. Beauchemin et fils"},
     'unvoyageurdespay00duga', lambda nom, ref: ref),
    ('dugas_1883.txt', 'DG',
     {'court': 'Dugas (1883)',
      'ref': "Dugas, Georges (1883), La première Canadienne du Nord-Ouest, ou biographie de Marie-Anne Gaboury, Montréal, Librairie Saint-Joseph"},
     'lapremirecanadi00duga', lambda nom, ref: ref),
    ('dugas_1889.txt', 'DP',
     {'court': 'Dugas (1889)',
      'ref': "Dugas, Georges (1889), Monseigneur Provencher et les missions de la Rivière-Rouge, Montréal, C.-O. Beauchemin"},
     'monseigneurprove00duga', lambda nom, ref: ref),
    ('houck_1908_v2.txt', 'HK',
     {'court': 'Houck (1908), vol. 2',
      'ref': "Houck, Louis (1908), A History of Missouri from the Earliest Explorations and Settlements until the Admission of the State into the Union, Chicago, R. R. Donnelley, vol. 2"},
     'historyofmissour02houc', lambda nom, ref: ref),
    ('houck_1908_v1.txt', 'H1',
     {'court': 'Houck (1908), vol. 1',
      'ref': "Houck, Louis (1908), A History of Missouri from the Earliest Explorations and Settlements until the Admission of the State into the Union, Chicago, R. R. Donnelley, vol. 1"},
     'historyofmissour01houc', lambda nom, ref: ref),
    ('houck_1908_v3.txt', 'H3',
     {'court': 'Houck (1908), vol. 3',
      'ref': "Houck, Louis (1908), A History of Missouri from the Earliest Explorations and Settlements until the Admission of the State into the Union, Chicago, R. R. Donnelley, vol. 3"},
     'historyofmissour03houc', lambda nom, ref: ref),
    ('spanish_regime_1909_v1.txt', 'SR',
     {'court': 'Houck (1909), Spanish Regime, vol. 1',
      'ref': "Houck, Louis (1909), The Spanish Regime in Missouri: A Collection of Papers and Documents Relating to Upper Louisiana, Chicago, R. R. Donnelley, vol. 1"},
     'spanishregimeinm01houc', lambda nom, ref: ref),
    ('spanish_regime_1909_v2.txt', 'SS',
     {'court': 'Houck (1909), Spanish Regime, vol. 2',
      'ref': "Houck, Louis (1909), The Spanish Regime in Missouri: A Collection of Papers and Documents Relating to Upper Louisiana, Chicago, R. R. Donnelley, vol. 2"},
     'spanishregimeinm02houc', lambda nom, ref: ref),
    ('chittenden_1902_v1.txt', 'CH',
     {'court': 'Chittenden (1902), vol. 1',
      'ref': "Chittenden, Hiram Martin (1902), The American Fur Trade of the Far West, New York, Francis P. Harper, vol. 1"},
     'americanfurtrade01chit', lambda nom, ref: ref),
    ('chittenden_1902_v2.txt', 'CI',
     {'court': 'Chittenden (1902), vol. 2-3',
      'ref': "Chittenden, Hiram Martin (1902), The American Fur Trade of the Far West, New York, Francis P. Harper, vol. 2-3"},
     'americanfurtrade00chit_0', lambda nom, ref: ref),
    ('franchere_1854.txt', 'FR',
     {'court': 'Franchère (1854)',
      'ref': "Franchère, Gabriel (1854), Narrative of a Voyage to the Northwest Coast of America in the Years 1811, 1812, 1813 and 1814, trad. J. V. Huntington, New York, Redfield"},
     'cihm_35175', lambda nom, ref: ref),
    ('masson_1889_v1.txt', 'MA',
     {'court': 'Masson (1889)',
      'ref': "Masson, Louis-Rodrigue (1889), Les Bourgeois de la Compagnie du Nord-Ouest, Québec, A. Côté, vol. 1, « Liste des bourgeois, commis, engagés et voyageurs de la Compagnie du Nord-Ouest après la fusion de 1804 »"},
     'cihm_30414', lambda nom, ref: ref),
    ('masson_1889_v1_recits.txt', 'MB',
     {'court': 'Masson (1889), récits',
      'ref': "Masson, Louis-Rodrigue (1889), Les Bourgeois de la Compagnie du Nord-Ouest, Québec, A. Côté, vol. 1 : journaux de Malhiot (1804-1805), McDonnell (1793-1795), Larocque (1804-1805) et Charles McKenzie (1804-1806)"},
     'cihm_30414', lambda nom, ref: ref),
    ('masson_1890_v2.txt', 'MC',
     {'court': 'Masson (1890)',
      'ref': "Masson, Louis-Rodrigue (1890), Les Bourgeois de la Compagnie du Nord-Ouest, Québec, A. Côté, vol. 2 (deuxième série)"},
     'cihm_30415', lambda nom, ref: ref),
    ('coues_1897_v1.txt', 'CO',
     {'court': 'Coues (1897), vol. 1',
      'ref': "Coues, Elliott (dir.) (1897), New Light on the Early History of the Greater Northwest. The Manuscript Journals of Alexander Henry and of David Thompson, New York, F. P. Harper, vol. 1"},
     'newlightonearlyh01henr', lambda nom, ref: ref),
    ('coues_1897_v2.txt', 'CQ',
     {'court': 'Coues (1897), vol. 2',
      'ref': "Coues, Elliott (dir.) (1897), New Light on the Early History of the Greater Northwest. The Manuscript Journals of Alexander Henry and of David Thompson, New York, F. P. Harper, vol. 2"},
     'newlightonearlyh02henr', lambda nom, ref: ref),
    ('perrault_1910.txt', 'PE',
     {'court': 'Perrault (1910)',
      'ref': "Perrault, Jean-Baptiste (1909-1910), « Narrative of the Travels and Adventures of a Merchant Voyageur… 1783-1820 », éd. J. S. Fox, Michigan Pioneer and Historical Collections, vol. 37"},
     'michiganhistoric37michuoft', lambda nom, ref: ref),
    ('cox_1832.txt', 'CX',
     {'court': 'Cox (1832)',
      'ref': "Cox, Ross (1832), Adventures on the Columbia River, New York, J. & J. Harper"},
     'adventuresoncolu00coxr', lambda nom, ref: ref),
    ('ross_1855.txt', 'RS',
     {'court': 'Ross (1855)',
      'ref': "Ross, Alexander (1855), The Fur Hunters of the Far West, Londres, Smith, Elder & Co., 2 vol."},
     'cihm_40228', lambda nom, ref: ref),
    ('burton_1896.txt', 'BU',
     {'court': 'Burton (1896)',
      'ref': "Burton, Clarence Monroe (1896), Cadillac's Village, or Detroit under Cadillac, with List of Property Owners, 1701 to 1710, Détroit"},
     'cadillacsvillage00burt', lambda nom, ref: ref),
    ('hamlin_1884.txt', 'HM',
     {'court': 'Hamlin (1884)',
      'ref': "Hamlin, Marie Caroline Watson (1884), Legends of le Détroit, Détroit, Thorndike Nourse"},
     'legendsofledtr00haml', lambda nom, ref: ref),
    ('mphc_1904_v33.txt', 'CP',
     {'court': 'Cadillac Papers (1904)',
      'ref': "Burton, C. M. (éd.) (1904), « Cadillac Papers », Michigan Pioneer and Historical Collections, vol. 33, Lansing"},
     'michiganhistoric33michuoft', lambda nom, ref: ref),
    ('mphc_1905_v34.txt', 'CQ2',
     {'court': 'Cadillac Papers (1905)',
      'ref': "Burton, C. M. (éd.) (1905), « Cadillac Papers » (suite), « Cadillac's Records » et « Detroit Rulers », Michigan Pioneer and Historical Collections, vol. 34, Lansing"},
     'michiganhistoric34michuoft', lambda nom, ref: ref),
    ('ross_catlin_1898.txt', 'RC',
     {'court': 'Ross et Catlin (1898)',
      'ref': "Ross, Robert B., et George B. Catlin (1898), Landmarks of Detroit: a History of the City, Détroit, Evening News Association"},
     'landmarksofdetr00ross', lambda nom, ref: ref),
    ('andreas_1884.txt', 'AN',
     {'court': 'Andreas (1884)',
      'ref': "Andreas, A. T. (1884), History of Chicago from the Earliest Period to the Present Time, Chicago, vol. 1"},
     'historyofchicago01andr', lambda nom, ref: ref),
    ('kankakee_1892.txt', 'KK',
     {'court': 'Kankakee (1892)',
      'ref': "Portrait and Biographical Record of Kankakee County, Illinois (1892), Chicago, Lake City Publishing Co."},
     'portraitbiographica00lake', lambda nom, ref: ref),
    ('nebraska_morton_1905.txt', 'NM', {'court': 'Morton (1905)', 'ref': "J. Sterling Morton (dir.), Illustrated History of Nebraska, vol. 1 (1905)"}, 'cu31924092232747', lambda nom, ref: ref),
    ('nebraska_transactions_1885.txt', 'NT', {'court': 'NSHS (1885)', 'ref': "Transactions and Reports of the Nebraska State Historical Society, vol. 1 (1885)"}, 'transactionsrepo00nebr', lambda nom, ref: ref),
    ('nebraska_placenames_1925.txt', 'NP', {'court': 'Fitzpatrick (1925)', 'ref': "Lilian L. Fitzpatrick, Nebraska Place-Names (1925)"}, 'bwb_P8-BLU-581', lambda nom, ref: ref),
    ('nebraska_dakota_1893.txt', 'ND', {'court': 'Warner (1893)', 'ref': "M. M. Warner, Warner's History of Dakota County, Nebraska (1893)"}, 'cu31924028874141', lambda nom, ref: ref),
    ('nebraska_reminiscences_1916.txt', 'NR', {'court': 'DAR (1916)', 'ref': "Nebraska Society of the Daughters of the American Revolution, Collection of Nebraska Pioneer Reminiscences (1916)"}, 'collectionofnebr00daug', lambda nom, ref: ref),
    ('nebraska_andreas_1882.txt', 'NB', {'court': 'Andreas (1882)', 'ref': "A. T. Andreas (éd.), History of the State of Nebraska (1882), Chicago, Western Historical Company"}, 'https://kancoll.org/books/andreas_ne/hon_tabl.html', lambda nom, ref: ref),
    ('idaho_rees_1918.txt', 'IR', {'court': 'Rees (1918)', 'ref': "John E. Rees, Idaho Chronology, Nomenclature, Bibliography (1918)"}, 'idahochronologyn00reesrich', lambda nom, ref: ref),
    ('idaho_brosnan_1918.txt', 'IB', {'court': 'Brosnan (1918)', 'ref': "Cornelius J. Brosnan, History of the State of Idaho (1918)"}, 'historyofstateof00bros', lambda nom, ref: ref),
    ('idaho_northidaho_1903.txt', 'IN', {'court': 'North Idaho (1903)', 'ref': "An Illustrated History of North Idaho (1903), Western Historical Publishing Co."}, 'illustratedhisto00slwe', lambda nom, ref: ref),
    ('idaho_driggs_1926.txt', 'ID', {'court': 'Driggs (1926)', 'ref': "B. W. Driggs, History of Teton Valley, Idaho (1926)"}, 'driggs', lambda nom, ref: ref),
    ('idaho_hawley_1920.txt', 'IH', {'court': 'Hawley (1920)', 'ref': "James H. Hawley (dir.), History of Idaho: The Gem of the Mountains, vol. 1 (1920)"}, 'historyofidahoge01hawl', lambda nom, ref: ref),
    ('idaho_desmet_1847.txt', 'IS', {'court': 'De Smet (1847)', 'ref': "Pierre-Jean De Smet, Oregon Missions and Travels over the Rocky Mountains, in 1845-46 (1847)"}, 'OregonMissionsAndTravels', lambda nom, ref: ref),
    ('idaho_elliott_1884.txt', 'IE', {'court': 'Elliott (1884)', 'ref': "H. N. Elliott (éd.), History of Idaho Territory (1884), San Francisco, Wallace W. Elliott & Co."}, 'historyidaho1884', lambda nom, ref: ref),
    ('irving_bonneville_1837.txt', 'IV', {'court': 'Irving, Bonneville (1837)', 'ref': "Washington Irving, The Adventures of Captain Bonneville (1837 ; éd. Putnam, 1852)"}, 'adventuresofcap00irvi', lambda nom, ref: ref),
    ('idaho_bancroft_1890.txt', 'IK', {'court': 'Bancroft (1890)', 'ref': "Hubert Howe Bancroft, History of Washington, Idaho, and Montana, 1845-1889 (1890)"}, 'historyofwashing31banc', lambda nom, ref: ref),
    ('montana_bancroft_1890.txt', 'MK', {'court': 'Bancroft, Montana (1890)', 'ref': "Hubert Howe Bancroft, History of Washington, Idaho, and Montana, 1845-1889 (1890), partie Montana"}, 'historyofwashing31banc', lambda nom, ref: ref),
    ('montana_palladino_1922.txt', 'MP', {'court': 'Palladino (1922)', 'ref': "Lawrence B. Palladino, Indian and White in the Northwest: A History of Catholicity in Montana, 1831-1891 (2e éd., 1922)"}, 'IndianAndWhiteInTheNW', lambda nom, ref: ref),
    ('montana_contributions_v1_1876.txt', 'M1', {'court': 'Contributions Montana I (1876)', 'ref': "Contributions to the Historical Society of Montana, vol. 1 (1876)"}, 'contributionstohvol1hist1876rich', lambda nom, ref: ref),
    ('montana_contributions_v2_1896.txt', 'M2', {'court': 'Contributions Montana II (1896)', 'ref': "Contributions to the Historical Society of Montana, vol. 2 (1896)"}, 'contributionstohvol2hist1896rich', lambda nom, ref: ref),
    ('montana_contributions_v3_1900.txt', 'M3', {'court': 'Contributions Montana III (1900)', 'ref': "Contributions to the Historical Society of Montana, vol. 3 (1900)"}, 'contributionstohvol3hist1900rich', lambda nom, ref: ref),
    ('montana_contributions_v7_1910.txt', 'M7', {'court': 'Contributions Montana VII (1910)', 'ref': "Contributions to the Historical Society of Montana, vol. 7 (1910)"}, 'contributionstohvol7hist1910rich', lambda nom, ref: ref),
    ('montana_contributions_v8_1917.txt', 'M8', {'court': 'Contributions Montana VIII (1917)', 'ref': "Contributions to the Historical Society of Montana, vol. 8 (1917)"}, 'contributionstoh08mont', lambda nom, ref: ref),
    ('montana_contributions_v9_1923.txt', 'M9', {'court': 'Contributions Montana IX (1923)', 'ref': "Contributions to the Historical Society of Montana, vol. 9 (1923)"}, 'contributionstohvol9hist1923rich', lambda nom, ref: ref),
    ('montana_miller_1894.txt', 'MI', {'court': 'Illustrated History of Montana (1894)', 'ref': "Joaquin Miller (dir.), An Illustrated History of the State of Montana (1894)"}, 'illustratedhisto00mill', lambda nom, ref: ref),
    ('montana_sanders_1913.txt', 'MS', {'court': 'Sanders (1913)', 'ref': "Helen Fitzgerald Sanders, A History of Montana (1913), 3 vol."}, lambda ref: 'historyofmontana11sand' if ref.startswith('vol. 1') else ('historyofmontanab02sand' if ref.startswith('vol. 2') else 'historyofmontana03insand'), lambda nom, ref: ref),
    ('wyoming_coutant_1899.txt', 'WC', {'court': 'Coutant (1899)', 'ref': "C. G. Coutant, The History of Wyoming from the Earliest Known Discoveries, vol. 1 (1899)"}, 'historyofwyoming00cout', lambda nom, ref: ref),
    ('wyoming_bartlett_1918.txt', 'WB', {'court': 'Bartlett (1918)', 'ref': "I. S. Bartlett (dir.), History of Wyoming, vol. 1 (1918)"}, 'historyofwyoming01bart', lambda nom, ref: ref),
    ('wyoming_bozeman_1922.txt', 'WT', {'court': 'Hebard et Brininstool (1922)', 'ref': "Grace Raymond Hebard et E. A. Brininstool, The Bozeman Trail (1922), 2 vol."}, lambda ref: 'bozemantrailhist01heba' if ref.startswith('vol. 1') else 'bozemantrailhist02heba', lambda nom, ref: ref),
    ('wyoming_bartlett_1918_v2.txt', 'W2', {'court': 'Bartlett, vol. 2 (1918)', 'ref': "I. S. Bartlett (dir.), History of Wyoming, vol. 2 (1918)"}, 'historyofwyoming02bart', lambda nom, ref: ref),
    ('wyoming_progressive_1903.txt', 'WP', {'court': 'Progressive Men of Wyoming (1903)', 'ref': "Progressive Men of the State of Wyoming (1903), Chicago, A. W. Bowen & Co., biographies du comté d'Uinta"}, lambda ref: 'https://sites.rootsweb.com/~wyuinttp/' + ref + '.htm', lambda nom, ref: ref),
    ('wyoming_annals_1923.txt', 'WA', {'court': 'Annals of Wyoming (1923-1928)', 'ref': "Annals of Wyoming, vol. 1 à 5 (1923-1928)"}, lambda ref: {'1':'annalsofwyom114192324wyom','2':'annalsofwyom214192425wyom','3':'annalsofwyom314192526wyom','4':'annalsofwyom414192627wyom','5':'annalsofwyom514192728wyom'}[ref.split(',')[0].split()[-1]], lambda nom, ref: ref),
    ('wyoming_bancroft_1890.txt', 'WK', {'court': 'Bancroft, History of Nevada, Colorado, and Wyoming (1890)', 'ref': "H. H. Bancroft, History of Nevada, Colorado, and Wyoming, 1540-1888, San Francisco, The History Company, 1890"}, 'nevcolandwyom00bancroft', lambda nom, ref: ref),
    ('wyoming_annals_1929.txt', 'WN', {'court': 'Annals of Wyoming (1929-1931)', 'ref': "Annals of Wyoming, vol. 6 et 7 (1929-1931)"}, lambda ref: 'annalsofwyom614192930wyom' if ref.startswith('vol. 6') else 'annalsofwyom714193031wyom', lambda nom, ref: ref),
    ('utah_bancroft_1889.txt', 'UB', {'court': 'Bancroft, History of Utah (1889)', 'ref': 'H. H. Bancroft, History of Utah, 1540-1886, San Francisco, The History Company, 1889'}, 'historyofutah00bancrich', lambda nom, ref: ref),
    ('utah_dale_1918.txt', 'UD', {'court': 'Dale, The Ashley-Smith Explorations (1918)', 'ref': 'H. C. Dale, The Ashley-Smith Explorations and the Discovery of a Central Route to the Pacific, 1822-1829, Cleveland, Arthur H. Clark, 1918'}, 'ashleysmithexplo00daleuoft', lambda nom, ref: ref),
    ('utah_fremont_1845.txt', 'UF', {'court': 'Frémont, Report of the Exploring Expedition (1845)', 'ref': "J. C. Frémont, Report of the Exploring Expedition to the Rocky Mountains in the Year 1842, and to Oregon and North California in the Years 1843-'44, Washington, Gales and Seaton, 1845"}, 'reportoftheexplor1845eng', lambda nom, ref: ref),
    ('utah_stansbury_1852.txt', 'US', {'court': 'Stansbury, Exploration and Survey of the Valley of the Great Salt Lake (1852)', 'ref': 'H. Stansbury, Exploration and Survey of the Valley of the Great Salt Lake of Utah, Philadelphie, Lippincott, Grambo, 1852 (éd. 1853)'}, 'explorationsurve001853stan', lambda nom, ref: ref),
    ('utah_remy_1861.txt', 'UR', {'court': 'Remy et Brenchley, A Journey to Great-Salt-Lake City (1861)', 'ref': "J. Remy et J. Brenchley, A Journey to Great-Salt-Lake City, Londres, W. Jeffs, 1861, 2 vol."}, lambda ref: 'ajourneytogreat01brengoog' if ref.startswith('vol. 1') else 'ajourneytogreat00remygoog', lambda nom, ref: ref),
    ('utah_dellenbaugh_1902.txt', 'UL', {'court': 'Dellenbaugh, The Romance of the Colorado River (1902)', 'ref': "F. S. Dellenbaugh, The Romance of the Colorado River, New York, G. P. Putnam's Sons, 1902"}, 'romanceofcolorad00dell', lambda nom, ref: ref),
    ('utah_uhq_1929.txt', 'UQ', {'court': 'Utah Historical Quarterly (1929-1930)', 'ref': "Utah Historical Quarterly, vol. 2 et 3, 1929-1930"}, lambda ref: {'vol. 2, n° 4':'utah-historical-quarterly_1929-10_2_4','vol. 3, n° 1':'utah-historical-quarterly_1930-01_3_1','vol. 3, n° 2':'utah-historical-quarterly_1930-04_3_2','vol. 3, n° 3':'utah-historical-quarterly_1930-07_3_3'}[ref.split(', p.')[0]], lambda nom, ref: ref),
    ('utah_whitney_1892.txt', 'UW', {'court': 'Whitney, History of Utah, vol. 1 (1892)', 'ref': "O. F. Whitney, History of Utah, vol. 1, Salt Lake City, George Q. Cannon & Sons, 1892"}, 'historyofutahcom01whit', lambda nom, ref: ref),
    ('utah_tullidge_1886.txt', 'UT', {'court': 'Tullidge, History of Salt Lake City (1886)', 'ref': "E. W. Tullidge, History of Salt Lake City, Salt Lake City, Star Printing Company, 1886"}, 'historyofsaltlak00tull', lambda nom, ref: ref),
    ('utah_harris_1909.txt', 'UC', {'court': 'Harris, The Catholic Church in Utah (1909)', 'ref': "W. R. Harris, The Catholic Church in Utah, Salt Lake City, Intermountain Catholic Press, 1909"}, 'catholicchurchin0000harr_k0t3', lambda nom, ref: ref),
    ('utah_esshom_1913.txt', 'UE', {'court': 'Esshom, Pioneers and Prominent Men of Utah (1913)', 'ref': "F. Esshom, Pioneers and Prominent Men of Utah, Salt Lake City, Utah Pioneers Book Publishing Company, 1913"}, lambda ref: 'pioneersprominen02essh' if ref.startswith('p. 1084') or ref.startswith('p. 1123') else 'pioneersprominen00esshrich', lambda nom, ref: ref),
    ('utah_burton_1861.txt', 'UN', {'court': 'Burton, The City of the Saints (1861)', 'ref': "R. F. Burton, The City of the Saints, and Across the Rocky Mountains to California, Londres, Longman, Green, 1861"}, 'cityofsaintsacro00burtuoft', lambda nom, ref: ref),
    ('utah_whitney_1893.txt', 'UH', {'court': 'Whitney, History of Utah, vol. 2-3 (1893-1898)', 'ref': "O. F. Whitney, History of Utah, vol. 2 et 3, Salt Lake City, George Q. Cannon & Sons, 1893-1898"}, lambda ref: 'historyofutahcom02whitrich' if ref.startswith('vol. 2') else 'historyofutahcom03whit', lambda nom, ref: ref),
    ('utah_whitney_1904.txt', 'UV', {'court': 'Whitney, History of Utah, vol. 4 (1904)', 'ref': "O. F. Whitney, History of Utah, vol. 4 (biographies), Salt Lake City, George Q. Cannon & Sons, 1904"}, 'historyofutahcom04whit', lambda nom, ref: ref),
    ('nevada_bancroft_1890.txt', 'VB', {'court': 'Bancroft, History of Nevada, Colorado, and Wyoming (1890)', 'ref': "H. H. Bancroft, History of Nevada, Colorado, and Wyoming, 1540-1888, San Francisco, The History Company, 1890"}, 'nevcolandwyom00bancroft', lambda nom, ref: ref),
    ('nevada_fremont_1845.txt', 'VF', {'court': 'Frémont, Report of the Exploring Expedition (1845)', 'ref': "J. C. Frémont, Report of the Exploring Expedition to the Rocky Mountains in the Year 1842, and to Oregon and North California in the Years 1843-'44, Washington, Gales and Seaton, 1845"}, 'reportoftheexplor1845eng', lambda nom, ref: ref),
    ('nevada_angel_1881.txt', 'VA', {'court': 'Angel, History of Nevada (1881)', 'ref': "M. Angel (dir.), History of Nevada, with Illustrations and Biographical Sketches, Oakland, Thompson & West, 1881"}, 'historyofnevada00ange', lambda nom, ref: ref),
    ('nevada_wren_1904.txt', 'VW', {'court': 'Wren, A History of the State of Nevada (1904)', 'ref': "T. Wren (dir.), A History of the State of Nevada, Its Resources and People, New York, Lewis Publishing Company, 1904"}, 'historyofstateof00wren', lambda nom, ref: ref),
    ('nevada_davis_1913.txt', 'VD', {'court': 'Davis, The History of Nevada (1913)', 'ref': "S. P. Davis (dir.), The History of Nevada, Reno et Los Angeles, Elms Publishing Company, 1913, 2 vol."}, lambda ref: 'historyofnevada01davirich' if ref.startswith('vol. 1') else 'historyofnevada02davirich', lambda nom, ref: ref),
    ('nevada_nhs_1913.txt', 'VQ', {'court': 'Nevada Historical Society Papers (1913-1926)', 'ref': "Nevada Historical Society Papers, 1913-1926"}, lambda ref: 'sim_nevada-historical-society-papers_' + ref.split(',')[0], lambda nom, ref: ref),
    ('nevada_dequille_1876.txt', 'VE', {'court': 'De Quille, History of the Big Bonanza (1876)', 'ref': "Dan De Quille (W. Wright), History of the Big Bonanza, Hartford, American Publishing Company, 1876"}, 'historyofbigbona00dequ', lambda nom, ref: ref),
    ('arizona_bancroft_1889.txt', 'ZB', {'court': 'Bancroft, History of Arizona and New Mexico (1889)', 'ref': "H. H. Bancroft, History of Arizona and New Mexico, 1530-1888, San Francisco, The History Company, 1889"}, 'arizonanewmex00bancroft', lambda nom, ref: ref),
    ('arizona_salpointe_1898.txt', 'ZS', {'court': 'Salpointe, Soldiers of the Cross (1898)', 'ref': "J. B. Salpointe, Soldiers of the Cross: Notes on the Ecclesiastical History of New-Mexico, Arizona and Colorado, Banning, St. Boniface's Industrial School, 1898"}, 'soldiersofcrossn00salp', lambda nom, ref: ref),
    ('arizona_portrait_1901.txt', 'ZP', {'court': 'Portrait and Biographical Record of Arizona (1901)', 'ref': "Portrait and Biographical Record of Arizona, Chicago, Chapman Publishing Company, 1901"}, 'portraitbioarizo00chaprich', lambda nom, ref: ref),
    ('arizona_mcclintock_1916_v1.txt', 'ZM', {'court': 'McClintock, Arizona, vol. 1 (1916)', 'ref': "J. H. McClintock, Arizona, Prehistoric, Aboriginal, Pioneer, Modern, vol. 1, Chicago, S. J. Clarke, 1916"}, 'arizonaprehistor01mcclrich', lambda nom, ref: ref),
    ('arizona_mcclintock_1916_v2.txt', 'ZN', {'court': 'McClintock, Arizona, vol. 2 (1916)', 'ref': "J. H. McClintock, Arizona, Prehistoric, Aboriginal, Pioneer, Modern, vol. 2, Chicago, S. J. Clarke, 1916"}, 'arizonaprehistor02mcclrich', lambda nom, ref: ref),
    ('arizona_mcclintock_1916_v3.txt', 'ZT', {'court': 'McClintock, Arizona, vol. 3 (1916)', 'ref': "J. H. McClintock, Arizona, Prehistoric, Aboriginal, Pioneer, Modern, vol. 3, Chicago, S. J. Clarke, 1916"}, 'arizonaprehistor03mcclrich', lambda nom, ref: ref),
    ('arizona_farish_1915.txt', 'ZF', {'court': 'Farish, History of Arizona (1915-1916)', 'ref': "T. E. Farish, History of Arizona, vol. 1 et 2, Phoenix, Filmer Brothers, 1915-1916"}, lambda ref: 'historyofarizona01faririch' if ref.startswith('vol. 1') else 'historyofarizona02faririch', lambda nom, ref: ref),
    ('arizona_farish_1916_v3_8.txt', 'ZX', {'court': 'Farish, History of Arizona, vol. 3-8 (1916-1918)', 'ref': "T. E. Farish, History of Arizona, vol. 3 à 8, Phoenix, Filmer Brothers, 1916-1918"}, lambda ref: 'historyofarizona0' + ref.split(',')[0].split()[-1] + 'faririch', lambda nom, ref: ref),
    ('texas_bancroft_1884.txt', 'XB', {'court': 'Bancroft, North Mexican States and Texas (1884-1889)', 'ref': "H. H. Bancroft, History of the North Mexican States and Texas, 2 vol., San Francisco, 1884-1889"}, lambda ref: 'thenorthmexivol115bancmiss' if ref.startswith('vol. 1') else 'northmexicanst02bancrich', lambda nom, ref: ref),
    ('texas_yoakum_1855.txt', 'XY', {'court': 'Yoakum, History of Texas (1855)', 'ref': "H. Yoakum, History of Texas from its first settlement in 1685 to its annexation to the United States in 1846, 2 vol., New York, Redfield, 1855"}, lambda ref: 'historyoftexasfr01yoak' if ref.startswith('vol. 1') else 'historyoftexasfr02yoak', lambda nom, ref: ref),
    ('texas_parisot_1899.txt', 'XP', {'court': 'Parisot, Reminiscences of a Texas Missionary (1899)', 'ref': "P. F. Parisot, The Reminiscences of a Texas Missionary, San Antonio, Johnson Bros., 1899"}, 'reminiscencesoft00pari', lambda nom, ref: ref),
    ('texas_domenech_1858.txt', 'XD', {'court': 'Domenech, Missionary Adventures in Texas and Mexico (1858)', 'ref': "Abbé Em. Domenech, Missionary Adventures in Texas and Mexico, Londres, Longman, 1858"}, 'missionaryadvent00dome', lambda nom, ref: ref),
    ('texas_reeves_1905.txt', 'XR', {'court': 'Reeves, The Napoleonic Exiles in America (1905)', 'ref': "Jesse S. Reeves, The Napoleonic Exiles in America, 1815-1819, Baltimore, Johns Hopkins Press, 1905"}, 'napoleonicexiles00reev', lambda nom, ref: ref),
    ('texas_bolton_mezieres_1914.txt', 'XM', {'court': 'Bolton, Athanase de Mézières (1914)', 'ref': "H. E. Bolton, Athanase de Mézières and the Louisiana-Texas Frontier, 1768-1780, 2 vol., Cleveland, Arthur H. Clark, 1914"}, lambda ref: 'athanasedemzi02mzuoft' if ref.startswith('vol. 2') else 'athanasedemzi01mz', lambda nom, ref: ref),
    ('texas_thrall_1879.txt', 'XT', {'court': 'Thrall, Pictorial History of Texas (1879)', 'ref': "Homer S. Thrall, A Pictorial History of Texas, St. Louis, N. D. Thompson, 1879"}, 'pictorialhistory01thra', lambda nom, ref: ref),
    ('texas_dallas_1892.txt', 'XL', {'court': 'Memorial and Biographical History of Dallas County (1892)', 'ref': "Memorial and Biographical History of Dallas County, Texas, Chicago, Lewis Publishing Co., 1892"}, 'memorialbiograph00lew', lambda nom, ref: ref),
    ('texas_sowell_1900.txt', 'XS', {'court': 'Sowell, Early Settlers and Indian Fighters of Southwest Texas (1900)', 'ref': "A. J. Sowell, Early Settlers and Indian Fighters of Southwest Texas, Austin, Ben C. Jones & Co., 1900"}, 'earlysettlersind00sowe', lambda nom, ref: ref),
    ('texas_olmsted_1857.txt', 'XO', {'court': 'Olmsted, A Journey through Texas (1857)', 'ref': "Frederick Law Olmsted, A Journey through Texas, New York, Dix, Edwards & Co., 1857"}, 'journeythroughte01olms', lambda nom, ref: ref),
    ('texas_johnson_barker_v3_1914.txt', 'XJ', {'court': 'Johnson et Barker, A History of Texas and Texans, vol. 3 (1914)', 'ref': "Frank W. Johnson, A History of Texas and Texans, éd. E. C. Barker, vol. 3, Chicago, American Historical Society, 1914"}, 'ahistorytexasan01winkgoog', lambda nom, ref: ref),
    ('texas_johnson_barker_v4_1914.txt', 'XK', {'court': 'Johnson et Barker, A History of Texas and Texans, vol. 4 (1914)', 'ref': "Frank W. Johnson, A History of Texas and Texans, éd. E. C. Barker, vol. 4, Chicago, American Historical Society, 1914"}, 'historyoftexaste04john', lambda nom, ref: ref),
    ('texas_bolton_1915.txt', 'XH', {'court': 'Bolton, Texas in the Middle Eighteenth Century (1915)', 'ref': "H. E. Bolton, Texas in the Middle Eighteenth Century, Berkeley, University of California Press, 1915"}, 'TexasInTheMiddle18thC', lambda nom, ref: ref),
    ('texas_brown_1892.txt', 'XW', {'court': 'Brown, History of Texas (1892-1893)', 'ref': "John Henry Brown, History of Texas from 1685 to 1892, 2 vol., St. Louis, L. E. Daniell, 1892-1893"}, lambda ref: 'historyoftexasfr02brow' if ref.startswith('vol. 2') else 'historyoftexasfr01brow', lambda nom, ref: ref),
    ('texas_brown_indianwars_1896.txt', 'XI', {'court': 'Brown, Indian Wars and Pioneers of Texas (c. 1896)', 'ref': "John Henry Brown, Indian Wars and Pioneers of Texas, Austin, L. E. Daniell, c. 1896"}, 'indianwarspionee00brow', lambda nom, ref: ref),
    ('texas_cox_1905.txt', 'XC', {'court': 'Cox, The Journeys of La Salle, vol. 2 (1905)', 'ref': "I. J. Cox (éd.), The Journeys of René Robert Cavelier, Sieur de La Salle, vol. 2, New York, A. S. Barnes, 1905"}, 'journeysrnrober06coxgoog', lambda nom, ref: ref),
    ('texas_dixon_1924.txt', 'XX', {'court': 'Dixon, Men Who Made Texas Free (1924)', 'ref': "Sam Houston Dixon, Men Who Made Texas Free, Houston, Texas Historical Publishing Co., 1924"}, 'menwhomadetexasf00dixo', lambda nom, ref: ref),
    ('texas_swhq_1906_1917.txt', 'XQ', {'court': 'Southwestern Historical Quarterly (1906-1917)', 'ref': "The Quarterly of the Texas State Historical Association / The Southwestern Historical Quarterly, vol. 10, 17, 19 et 20, Austin, 1906-1917"}, lambda ref: 'southwesternhist' + ref.split(',')[0].split()[-1] + 'bark', lambda nom, ref: ref),
    ('texas_dunn_1917.txt', 'XU', {'court': 'Dunn, Spanish and French Rivalry in the Gulf Region (1917)', 'ref': "William Edward Dunn, Spanish and French Rivalry in the Gulf Region of the United States, 1678-1702, Austin, University of Texas, 1917"}, 'spanishfrenchriv01dunn', lambda nom, ref: ref),
    ('texas_foote_1841.txt', 'XV', {'court': 'Foote, Texas and the Texans (1841)', 'ref': "Henry Stuart Foote, Texas and the Texans, 2 vol., Philadelphie, Thomas, Cowperthwait & Co., 1841"}, 'texastexansoradv01foot', lambda nom, ref: ref),
    ('texas_clark_1907.txt', 'XZ', {'court': 'Clark, The Beginnings of Texas (1907)', 'ref': "Robert Carlton Clark, The Beginnings of Texas, 1684-1718, Austin, University of Texas, 1907"}, 'beginningsoftexa00clar', lambda nom, ref: ref),
    ('texas_corner_1890.txt', 'XA', {'court': 'Corner, San Antonio de Bexar (1890)', 'ref': "William Corner, San Antonio de Bexar. A guide and history, San Antonio, Bainbridge & Corner, 1890"}, 'sanantoniodebexa00corn', lambda nom, ref: ref),
    ('texas_kennedy_1841.txt', 'XG', {'court': 'Kennedy, Texas: the Rise, Progress, and Prospects (1841)', 'ref': "William Kennedy, Texas: the rise, progress, and prospects of the Republic of Texas, vol. 1, Londres, R. Hastings, 1841"}, 'texasriseprogre01kenngoog', lambda nom, ref: ref),
    ('louisiane_fortier_1914_v1.txt', 'LF', {'court': 'Fortier, Louisiana, vol. 1 (1914)', 'ref': "Alcée Fortier, Louisiana: comprising sketches of parishes, towns, events, institutions, and persons, vol. 1, Atlanta, Southern Historical Association, 1914"}, 'louisianacompris01fort', lambda nom, ref: ref),
    ('louisiane_fortier_1914_v2.txt', 'LG', {'court': 'Fortier, Louisiana, vol. 2 (1914)', 'ref': "Alcée Fortier, Louisiana: comprising sketches of parishes, towns, events, institutions, and persons, vol. 2, Atlanta, Southern Historical Association, 1914"}, 'louisianacompris02fort', lambda nom, ref: ref),
    ('louisiane_fortier_1914_v3.txt', 'LH', {'court': 'Fortier, Louisiana, vol. 3 (1914)', 'ref': "Alcée Fortier, Louisiana: comprising sketches of counties, towns, events, institutions, and persons, vol. 3, Atlanta, Century Historical Association, 1914"}, 'louisianacompris03fort', lambda nom, ref: ref),
    ('louisiane_perrin_1891.txt', 'LS', {'court': 'Perrin, Southwest Louisiana (1891)', 'ref': "William Henry Perrin (éd.), Southwest Louisiana: Biographical and Historical, New Orleans, Gulf Publishing Co., 1891"}, 'southwestlouisia00perr', lambda nom, ref: ref),
    ('louisiane_gayarre_v1_1854.txt', 'LY', {'court': 'Gayarré, History of Louisiana, vol. 1 (1854)', 'ref': "Charles Gayarré, History of Louisiana, vol. 1 : The French Domination, New York, Redfield, 1854"}, 'historyoflouisia01gayaiala', lambda nom, ref: ref),
    ('louisiane_gayarre_v2_1854.txt', 'LA', {'court': 'Gayarré, History of Louisiana, vol. 2 (1854)', 'ref': "Charles Gayarré, History of Louisiana, vol. 2 : The French Domination, New York, Redfield, 1854"}, 'historyoflouisia02gayaiala', lambda nom, ref: ref),
    ('louisiane_gayarre_v3_1866.txt', 'LC', {'court': 'Gayarré, History of Louisiana, vol. 3 (1866)', 'ref': "Charles Gayarré, History of Louisiana : The Spanish Domination, New York, Widdleton, 1866"}, 'cihm_45094', lambda nom, ref: ref),
    ('louisiane_gayarre_v4_1866.txt', 'LD', {'court': 'Gayarré, History of Louisiana, vol. 4 (1866)', 'ref': "Charles Gayarré, History of Louisiana : The American Domination, New York, Widdleton, 1866"}, 'cihm_45095', lambda nom, ref: ref),
    ('louisiane_latour_1816.txt', 'LE', {'court': 'Latour, Historical Memoir (1816)', 'ref': "Arsène Lacarrière Latour, Historical Memoir of the War in West Florida and Louisiana in 1814-15, Philadelphie, John Conrad, 1816"}, 'historicalmemoi00latogoog', lambda nom, ref: ref),
    ('louisiane_cable_1885.txt', 'LI', {'court': 'Cable, The Creoles of Louisiana (1885)', 'ref': "George W. Cable, The Creoles of Louisiana, Londres, John C. Nimmo, 1885"}, 'creolesoflouisia00cabluoft', lambda nom, ref: ref),
    ('louisiane_fortier_histoire_v3_1904.txt', 'LK', {'court': 'Fortier, A History of Louisiana, vol. 3 (1904)', 'ref': "Alcée Fortier, A History of Louisiana, vol. 3 : The American Domination, part I, 1803-1861, New York, Manzi, Joyant & Co., 1904"}, 'historyoflouisia03fortuoft', lambda nom, ref: ref),
    ('louisiane_fortier_histoire_v2_1904.txt', 'LM', {'court': 'Fortier, A History of Louisiana, vol. 2 (1904)', 'ref': "Alcée Fortier, A History of Louisiana, vol. 2 : The Spanish Domination and the Cession to the United States, 1769-1803, New York, Manzi, Joyant & Co., 1904"}, 'historyoflouisia02fortuoft', lambda nom, ref: ref),
    ('louisiane_fortier_histoire_v1_1904.txt', 'LN', {'court': 'Fortier, A History of Louisiana, vol. 1 (1904)', 'ref': "Alcée Fortier, A History of Louisiana, vol. 1 : Early Explorers and the Domination of the French, 1512-1768, New York, Manzi, Joyant & Co., 1904"}, 'historyoflouisia01fortuoft', lambda nom, ref: ref),
    ('louisiane_bossu_1768.txt', 'LO', {'court': 'Bossu, Nouveaux voyages aux Indes occidentales (1768)', 'ref': "Jean-Bernard Bossu, Nouveaux voyages aux Indes occidentales, première partie, 2e éd., Paris, Le Jay, 1768"}, 'nouveauxvoyagesa00boss_0', lambda nom, ref: ref),
    ('louisiane_french_collections_p2_1851.txt', 'LQ', {'court': 'French, Historical Collections of Louisiana, part II (1851)', 'ref': "B. F. French (éd.), Historical Collections of Louisiana, part II, Philadelphie, Daniels and Smith, 1851"}, 'cihm_36229', lambda nom, ref: ref),
    ('louisiane_french_collections_p5_1853.txt', 'LR', {'court': 'French, Historical Collections of Louisiana, part V (1853)', 'ref': "B. F. French (éd.), Historical Collections of Louisiana, part V : Historical Memoirs from 1687 to 1770, New York, Lamport, Blakeman & Law, 1853"}, 'cihm_36231', lambda nom, ref: ref),
    ('louisiane_french_collections_ns_1869.txt', 'LT', {'court': 'French, Historical Collections of Louisiana and Florida (1869)', 'ref': "B. F. French (éd.), Historical Collections of Louisiana and Florida, new series, New York, J. Sabin & Sons, 1869"}, 'historicalcollec00fren_1', lambda nom, ref: ref),
    ('louisiane_king_creole_families_1921.txt', 'LU', {'court': 'King, Creole Families of New Orleans (1921)', 'ref': "Grace King, Creole Families of New Orleans, New York, Macmillan, 1921"}, 'creolefamiliesof00king', lambda nom, ref: ref),
    ('louisiane_barde_vigilance_1861.txt', 'LV', {'court': 'Barde, Histoire des comités de vigilance aux Attakapas (1861)', 'ref': "Alexandre Barde, Histoire des comités de vigilance aux Attakapas, Saint-Jean-Baptiste (Louisiane), 1861"}, 'histoiredecomit00bard', lambda nom, ref: ref),
    ('louisiane_fortier_studies_1894.txt', 'LX', {'court': 'Fortier, Louisiana Studies (1894)', 'ref': "Alcée Fortier, Louisiana Studies : Literature, Customs and Dialects, History and Education, New Orleans, F. F. Hansell & Bro., 1894"}, 'louisianastudie00fortgoog', lambda nom, ref: ref),
    ('louisiane_king_new_orleans_1895.txt', 'LZ', {'court': 'King, New Orleans : the Place and the People (1895)', 'ref': "Grace King, New Orleans : the Place and the People, New York, Macmillan, 1895"}, 'neworleansplacep00king', lambda nom, ref: ref),
    ('louisiane_chambers_1925_v2.txt', 'LB', {'court': 'Chambers, A History of Louisiana, vol. 2 (1925)', 'ref': "Henry E. Chambers, A History of Louisiana, vol. 2, Chicago et New York, American Historical Society, 1925"}, 'historyoflouisia0002unse', lambda nom, ref: ref),
    ('louisiane_chambers_1925_v3.txt', 'LW', {'court': 'Chambers, A History of Louisiana, vol. 3 (1925)', 'ref': "Henry E. Chambers, A History of Louisiana, vol. 3, Chicago et New York, American Historical Society, 1925"}, 'historyoflouisia0003unse', lambda nom, ref: ref),
    ('louisiane_pittman_1770.txt', 'PI', {'court': 'Pittman, The Present State of the European Settlements on the Mississippi (1770)', 'ref': "Philip Pittman, The Present State of the European Settlements on the Mississippi, Londres, J. Nourse, 1770"}, 'presentstateofeu00pitt', lambda nom, ref: ref),
    ('louisiane_lhq_v1_1917.txt', 'LL', {'court': 'The Louisiana Historical Quarterly, vol. 1 (1917-1918)', 'ref': "The Louisiana Historical Quarterly, vol. 1, nos 1-4, La Nouvelle-Orléans, Louisiana Historical Society, 1917-1918"}, 'per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1917-01-08_1_1', lambda nom, ref: ref),
    ('louisiane_lhq_v2_1919.txt', 'QA', {'court': 'The Louisiana Historical Quarterly, vol. 2 (1919)', 'ref': "The Louisiana Historical Quarterly, vol. 2, nos 1-4, La Nouvelle-Orléans, Louisiana Historical Society, 1919"}, 'per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1919-01_2_1', lambda nom, ref: ref),
    ('louisiane_lhq_v3_1920.txt', 'QB', {'court': 'The Louisiana Historical Quarterly, vol. 3 (1920)', 'ref': "The Louisiana Historical Quarterly, vol. 3, nos 1-4, La Nouvelle-Orléans, Louisiana Historical Society, 1920"}, 'per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1920-01_3_1', lambda nom, ref: ref),
    ('louisiane_lhq_v4_1921.txt', 'QC', {'court': 'The Louisiana Historical Quarterly, vol. 4 (1921)', 'ref': "The Louisiana Historical Quarterly, vol. 4, nos 1-4, La Nouvelle-Orléans, Louisiana Historical Society, 1921"}, 'per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1921-01_4_1', lambda nom, ref: ref),
    ('louisiane_lhq_v5_1922.txt', 'QD', {'court': 'The Louisiana Historical Quarterly, vol. 5 (1922)', 'ref': "The Louisiana Historical Quarterly, vol. 5, nos 1-4, La Nouvelle-Orléans, Louisiana Historical Society, 1922"}, 'per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1922-01_5_1', lambda nom, ref: ref),
    ('louisiane_lhq_v6_1923.txt', 'QE', {'court': 'The Louisiana Historical Quarterly, vol. 6 (1923)', 'ref': "The Louisiana Historical Quarterly, vol. 6, nos 1-4, La Nouvelle-Orléans, Louisiana Historical Society, 1923"}, 'per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1923-01_6_1', lambda nom, ref: ref),
    ('louisiane_lhq_v7_1924.txt', 'QF', {'court': 'The Louisiana Historical Quarterly, vol. 7 (1924)', 'ref': "The Louisiana Historical Quarterly, vol. 7, nos 1-4, La Nouvelle-Orléans, Louisiana Historical Society, 1924"}, 'per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1924-01_7_1', lambda nom, ref: ref),
    ('louisiane_lhq_v8_1925.txt', 'QG', {'court': 'The Louisiana Historical Quarterly, vol. 8 (1925)', 'ref': "The Louisiana Historical Quarterly, vol. 8, nos 1-4, La Nouvelle-Orléans, Louisiana Historical Society, 1925"}, 'per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1925-01_8_1', lambda nom, ref: ref),
    ('louisiane_lhq_v9_1926.txt', 'QH', {'court': 'The Louisiana Historical Quarterly, vol. 9 (1926)', 'ref': "The Louisiana Historical Quarterly, vol. 9, nos 1-4, La Nouvelle-Orléans, Louisiana Historical Society, 1926"}, 'per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1926-01_9_1', lambda nom, ref: ref),
    ('louisiane_lhq_v10_1927.txt', 'QI', {'court': 'The Louisiana Historical Quarterly, vol. 10 (1927)', 'ref': "The Louisiana Historical Quarterly, vol. 10, nos 1-4, La Nouvelle-Orléans, Louisiana Historical Society, 1927"}, 'per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1927-01_10_1', lambda nom, ref: ref),
    ('louisiane_lhq_v11_1928.txt', 'QJ', {'court': 'The Louisiana Historical Quarterly, vol. 11 (1928)', 'ref': "The Louisiana Historical Quarterly, vol. 11, nos 1-4, La Nouvelle-Orléans, Louisiana Historical Society, 1928"}, 'per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1928-01_11_1', lambda nom, ref: ref),
    ('louisiane_lhq_v12_1929.txt', 'QK', {'court': 'The Louisiana Historical Quarterly, vol. 12 (1929)', 'ref': "The Louisiana Historical Quarterly, vol. 12, nos 1-4, La Nouvelle-Orléans, Louisiana Historical Society, 1929"}, 'per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1929-01_12_1', lambda nom, ref: ref),
    ('louisiane_lhq_v13_1930.txt', 'QL', {'court': 'The Louisiana Historical Quarterly, vol. 13 (1930)', 'ref': "The Louisiana Historical Quarterly, vol. 13, nos 1-4, La Nouvelle-Orléans, Louisiana Historical Society, 1930"}, 'per_louisiana-historical-quarterly_the-louisiana-historical-quarterly_1930-01_13_1', lambda nom, ref: ref),
    ('louisiane_plhs_v1_3.txt', 'QM', {'court': 'Publications of the Louisiana Historical Society, vol. 1-3', 'ref': "Publications of the Louisiana Historical Society, vol. I-III, La Nouvelle-Orléans, Louisiana Historical Society (réimpr. AMS Press, 1969)"}, 'louisianahistori01loui', lambda nom, ref: ref),
    ('louisiane_plhs_v4_1908.txt', 'QN', {'court': 'Publications of the Louisiana Historical Society, vol. 4 (1908)', 'ref': "Publications of the Louisiana Historical Society, vol. IV, La Nouvelle-Orléans, Louisiana Historical Society, 1908"}, 'publicationslou01socigoog', lambda nom, ref: ref),
    ('louisiane_plhs_v5_1911.txt', 'QO', {'court': 'Publications of the Louisiana Historical Society, vol. 5 (1911)', 'ref': "Publications of the Louisiana Historical Society, vol. V, La Nouvelle-Orléans, Louisiana Historical Society, 1911"}, 'publicationslou04socigoog', lambda nom, ref: ref),
    ('louisiane_plhs_v6_1912.txt', 'QP', {'court': 'Publications of the Louisiana Historical Society, vol. 6 (1912)', 'ref': "Publications of the Louisiana Historical Society, vol. VI, La Nouvelle-Orléans, Louisiana Historical Society, 1912"}, 'publicationslou03socigoog', lambda nom, ref: ref),
    ('louisiane_plhs_v8_1915.txt', 'QQ', {'court': 'Publications of the Louisiana Historical Society, vol. 8 (1914-1915)', 'ref': "Publications of the Louisiana Historical Society, vol. VIII (1914-1915), La Nouvelle-Orléans, Louisiana Historical Society (réimpr. AMS Press, 1969)"}, 'louisianahistori08loui', lambda nom, ref: ref),
    ('louisiane_plhs_v9_1916.txt', 'QR', {'court': 'Publications of the Louisiana Historical Society, vol. 9 (1916)', 'ref': "Publications of the Louisiana Historical Society, vol. IX, Proceedings and Reports 1916, La Nouvelle-Orléans, Louisiana Historical Society, 1917"}, 'publicationslou06socigoog', lambda nom, ref: ref),
    ('louisiane_plhs_v10_1917.txt', 'QS', {'court': 'Publications of the Louisiana Historical Society, vol. 10 (1917)', 'ref': "Publications of the Louisiana Historical Society, vol. X, Proceedings and Reports 1917, La Nouvelle-Orléans, Louisiana Historical Society (réimpr. AMS Press, 1969)"}, 'louisianahistori10loui', lambda nom, ref: ref),
    ('louisiane_lepage_du_pratz.txt', 'QT', {'court': 'Le Page du Pratz, The History of Louisiana', 'ref': "Le Page du Pratz, The History of Louisiana, trad. anglaise, Londres, T. Becket, 1774 (réimpr. La Nouvelle-Orléans, Pelican Press)"}, 'historyoflouisia00lepa', lambda nom, ref: ref),
    ('louisiane_dumont_1753.txt', 'QV', {'court': 'Dumont, Mémoires historiques sur la Louisiane (1753)', 'ref': "Dumont de Montigny, Mémoires historiques sur la Louisiane, 2 tomes, Paris, Bauche, 1753"}, 'mmoireshistori01dumo', lambda nom, ref: ref),
    ('louisiane_shea_early_voyages_1861.txt', 'QW', {'court': 'Shea, Early Voyages Up and Down the Mississippi (1861)', 'ref': "John Gilmary Shea, Early Voyages Up and Down the Mississippi, Albany, Joel Munsell, 1861"}, 'earlyvoyagesupdo00shea', lambda nom, ref: ref),
    ('louisiane_in_acadia_1893.txt', 'RE', {'court': 'Johnston, In Acadia (1893)', 'ref': "Margaret Avery Johnston (compil.), In Acadia : the Acadians in Story and Song, La Nouvelle-Orléans, F. F. Hansell & Bro., 1893"}, 'inacadiaacadians00john', lambda nom, ref: ref),
    ('louisiane_st_bernard_1906.txt', 'RF', {'court': 'St. Bernard Parish, Louisiana (v. 1906)', 'ref': "St. Bernard Parish, Louisiana, its Natural Resources and Advantages, Parish Immigration League, [vers 1906]"}, 'stbernardparishl00stbe', lambda nom, ref: ref),
    ('louisiane_carroll_alabama_1908.txt', 'RG', {'court': 'Carroll, A Catholic History of Alabama and the Floridas (1908)', 'ref': "Austin Carroll, A Catholic History of Alabama and the Floridas, vol. 1, New York, P. J. Kenedy & Sons, 1908"}, 'CatholicHistoryOfAlabamaAndTheFloridasV1', lambda nom, ref: ref),
    ('ouest_shea_catholic_v1_1886.txt', 'RH', {'court': 'Shea, A History of the Catholic Church, vol. 1 (1886)', 'ref': "John Gilmary Shea, A History of the Catholic Church within the Limits of the United States, vol. 1 : The Catholic Church in Colonial Days, New York, 1886"}, 'AHistoryOfTheCatholicChurchV1', lambda nom, ref: ref),
    ('ouest_shea_catholic_v2_1888.txt', 'RI', {'court': 'Shea, A History of the Catholic Church, vol. 2 (1888)', 'ref': "John Gilmary Shea, Life and Times of the Most Rev. John Carroll (A History of the Catholic Church within the Limits of the United States, vol. 2), New York, 1888"}, 'ahistorycatholi00sheagoog', lambda nom, ref: ref),
    ('ouest_shea_catholic_v3_1890.txt', 'RJ', {'court': 'Shea, A History of the Catholic Church, vol. 3 (1890)', 'ref': "John Gilmary Shea, History of the Catholic Church in the United States, 1808-1843 (A History of the Catholic Church within the Limits of the United States, vol. 3), New York, 1890"}, 'historychurchusa03sheauoft', lambda nom, ref: ref),
    ('ouest_shea_catholic_v4_1892.txt', 'RK', {'court': 'Shea, A History of the Catholic Church, vol. 4 (1892)', 'ref': "John Gilmary Shea, A History of the Catholic Church in the United States, 1843-1866 (A History of the Catholic Church within the Limits of the United States, vol. 4), New York, 1892"}, 'historychurchusa04sheauoft', lambda nom, ref: ref),
    ('mississippi_pmhs_v3_1900.txt', 'RL', {'court': 'Publications of the Mississippi Historical Society, vol. 3 (1900)', 'ref': "Publications of the Mississippi Historical Society, vol. 3 (1900), Mississippi Historical Society"}, 'publicationsofmi3190unse', lambda nom, ref: ref),
    ('mississippi_pmhs_v4_1901.txt', 'RM', {'court': 'Publications of the Mississippi Historical Society, vol. 4 (1901)', 'ref': "Publications of the Mississippi Historical Society, vol. 4 (1901), Mississippi Historical Society"}, 'publicationsmis05rilegoog', lambda nom, ref: ref),
    ('mississippi_pmhs_v5_1902.txt', 'RN', {'court': 'Publications of the Mississippi Historical Society, vol. 5 (1902)', 'ref': "Publications of the Mississippi Historical Society, vol. 5 (1902), Mississippi Historical Society"}, 'publicationsmis09socigoog', lambda nom, ref: ref),
    ('mississippi_pmhs_v6_1902.txt', 'RO', {'court': 'Publications of the Mississippi Historical Society, vol. 6 (1902)', 'ref': "Publications of the Mississippi Historical Society, vol. 6 (1902), Mississippi Historical Society"}, 'publicationsmis07socigoog', lambda nom, ref: ref),
    ('mississippi_pmhs_v7_1903.txt', 'RP', {'court': 'Publications of the Mississippi Historical Society, vol. 7 (1903)', 'ref': "Publications of the Mississippi Historical Society, vol. 7 (1903), Mississippi Historical Society"}, 'publicationsmis05socigoog', lambda nom, ref: ref),
    ('mississippi_pmhs_v8_1904.txt', 'RQ', {'court': 'Publications of the Mississippi Historical Society, vol. 8 (1904)', 'ref': "Publications of the Mississippi Historical Society, vol. 8 (1904), Mississippi Historical Society"}, 'publicationsmis00rilegoog', lambda nom, ref: ref),
    ('mississippi_pmhs_v9_1906.txt', 'RR', {'court': 'Publications of the Mississippi Historical Society, vol. 9 (1906)', 'ref': "Publications of the Mississippi Historical Society, vol. 9 (1906), Mississippi Historical Society"}, 'publicationsmis00socigoog', lambda nom, ref: ref),
    ('mississippi_pmhs_v11_1910.txt', 'RW', {'court': 'Publications of the Mississippi Historical Society, vol. 11 (1910)', 'ref': "Publications of the Mississippi Historical Society, vol. 11 (1910), Mississippi Historical Society"}, 'publicationsmis01socigoog', lambda nom, ref: ref),
    ('mississippi_pmhs_cent1_1916.txt', 'RT', {'court': 'Publications of the Mississippi Historical Society, série du centenaire, vol. 1 (1916)', 'ref': "Publications of the Mississippi Historical Society, série du centenaire, vol. 1 (1916), Mississippi Historical Society"}, 'publicationsofmi12rowl', lambda nom, ref: ref),
    ('mississippi_pmhs_cent4_1921.txt', 'RU', {'court': 'Publications of the Mississippi Historical Society, série du centenaire, vol. 4 (1921)', 'ref': "Publications of the Mississippi Historical Society, série du centenaire, vol. 4 (1921), Mississippi Historical Society"}, 'publicationsofmi04rowl', lambda nom, ref: ref),
    ('mississippi_pmhs_cent5_1925.txt', 'RV', {'court': 'Publications of the Mississippi Historical Society, série du centenaire, vol. 5 (1925)', 'ref': "Publications of the Mississippi Historical Society, série du centenaire, vol. 5 (1925), Mississippi Historical Society"}, 'publicationsofmi0005vari', lambda nom, ref: ref),
    ('mississippi_hamilton_colonial_mobile_1910.txt', 'RX', {'court': 'Hamilton, Colonial Mobile (1910)', 'ref': "Peter J. Hamilton, Colonial Mobile, éd. revue, Boston, Houghton Mifflin, 1910"}, 'colonialmobilehi01hami', lambda nom, ref: ref),
    ('mississippi_rowland_v1_1907.txt', 'RY', {'court': 'Rowland, Mississippi, vol. 1 (1907)', 'ref': "Dunbar Rowland (éd.), Mississippi : Comprising Sketches of Towns, Events, Institutions, and Persons, vol. 1, Atlanta, Southern Historical Publishing Association, 1907"}, 'mississippicompr01rowl', lambda nom, ref: ref),
    ('mississippi_rowland_v2_1907.txt', 'RZ', {'court': 'Rowland, Mississippi, vol. 2 (1907)', 'ref': "Dunbar Rowland (éd.), Mississippi : Comprising Sketches of Towns, Events, Institutions, and Persons, vol. 2, Atlanta, Southern Historical Publishing Association, 1907"}, 'mississippicompr02rowl', lambda nom, ref: ref),
    ('mississippi_natchez_catholic_1886.txt', 'SA', {'court': 'Sketch of the Catholic Church in Natchez (1886)', 'ref': "Sketch of the Catholic Church in the City of Natchez, Miss., on the Occasion of the Consecration of its Cathedral, Natchez, 1886"}, 'SketchOfTheCatholicChurchInTheCity', lambda nom, ref: ref),
    ('mississippi_old_biloxi_1920.txt', 'SB', {'court': 'Rowland, Old Biloxi (1920)', 'ref': "Dunbar Rowland, Old Biloxi, the First Settlement in Mississippi, Jackson, 1920"}, 'oldbiloxifirstse00rowl', lambda nom, ref: ref),
    ('mississippi_cushman_1899.txt', 'SC', {'court': 'Cushman, History of the Choctaw, Chickasaw and Natchez Indians (1899)', 'ref': "H. B. Cushman, History of the Choctaw, Chickasaw and Natchez Indians, Greenville (Texas), 1899"}, 'cu31924073559761', lambda nom, ref: ref),
    ('mississippi_claiborne_1880.txt', 'SD', {'court': 'Claiborne, Mississippi as a Province, Territory and State (1880)', 'ref': "J. F. H. Claiborne, Mississippi, as a Province, Territory, and State, vol. 1, Jackson, Power & Barksdale, 1880"}, 'cu31924028795405', lambda nom, ref: ref),
    ('mississippi_lowry_1891.txt', 'SE', {'court': 'Lowry et McCardle, A History of Mississippi (1891)', 'ref': "Robert Lowry et William H. McCardle, A History of Mississippi, Jackson, R. H. Henry & Co., 1891"}, 'ahistorymississ00mccagoog', lambda nom, ref: ref),
    ('mississippi_goodspeed_v1_1891.txt', 'SF', {'court': 'Goodspeed, Memoirs of Mississippi, vol. I (1891)', 'ref': "Biographical and Historical Memoirs of Mississippi, vol. I, Chicago, Goodspeed Publishing Co., 1891"}, 'biographicalhist11good', lambda nom, ref: ref),
    ('mississippi_goodspeed_v2_1891.txt', 'SG', {'court': 'Goodspeed, Memoirs of Mississippi, vol. II (1891)', 'ref': "Biographical and Historical Memoirs of Mississippi, vol. II, Chicago, Goodspeed Publishing Co., 1891"}, 'biographicalhist21good', lambda nom, ref: ref),
    ('mississippi_monette_v1_1846.txt', 'SH', {'court': 'Monette, Valley of the Mississippi, vol. I (1846)', 'ref': "John W. Monette, History of the Discovery and Settlement of the Valley of the Mississippi, vol. I, New York, Harper & Brothers, 1846"}, 'cihm_38028', lambda nom, ref: ref),
    ('mississippi_monette_v2_1846.txt', 'SI', {'court': 'Monette, Valley of the Mississippi, vol. II (1846)', 'ref': "John W. Monette, History of the Discovery and Settlement of the Valley of the Mississippi, vol. II, New York, Harper & Brothers, 1846"}, 'cihm_38029', lambda nom, ref: ref),
    ('mississippi_english_dominion_1911.txt', 'SJ', {'court': 'Mississippi Provincial Archives, English Dominion (1911)', 'ref': "Dunbar Rowland (éd.), Mississippi Provincial Archives, 1763-1766: English Dominion, vol. I, Nashville, Brandon, 1911"}, 'mississippiprovi01missuoft', lambda nom, ref: ref),
    ('mississippi_territorial_archives_1905.txt', 'SK', {'court': 'Mississippi Territorial Archives 1798-1803 (1905)', 'ref': "Dunbar Rowland (éd.), Mississippi Territorial Archives, 1798-1803, vol. I, Nashville, Brandon, 1905"}, 'mississippiterri01missuoft', lambda nom, ref: ref),
    ('mississippi_wailes_1854.txt', 'SL', {'court': 'Wailes, Agriculture and Geology of Mississippi (1854)', 'ref': "B. L. C. Wailes, Report on the Agriculture and Geology of Mississippi, Philadelphia, Lippincott, Grambo & Co., 1854"}, 'reportonagricult00miss', lambda nom, ref: ref),
    ('mississippi_rowland_v3_1907.txt', 'SM', {'court': 'Rowland, Mississippi, vol. III : Contemporary Biography (1907)', 'ref': "Dunbar Rowland (éd.), Mississippi, vol. III : Contemporary Biography, Atlanta, Southern Historical Publishing Association, 1907"}, 'mississippicompr03rowl', lambda nom, ref: ref),
    ('louisiane_margry_v4.txt', 'QX', {'court': 'Margry, Découvertes et établissements, t. IV', 'ref': "Pierre Margry, Découvertes et établissements des Français dans l'ouest et dans le sud de l'Amérique septentrionale, t. IV (1694-1703), Paris"}, 'mmoiresetdocum04marg', lambda nom, ref: ref),
    ('louisiane_margry_v5.txt', 'QY', {'court': 'Margry, Découvertes et établissements, t. V', 'ref': "Pierre Margry, Découvertes et établissements des Français dans l'ouest et dans le sud de l'Amérique septentrionale, t. V (1683-1724), Paris"}, 'mmoiresetdocum05marg', lambda nom, ref: ref),
    ('ouest_margry_v6.txt', 'QZ', {'court': 'Margry, Découvertes et établissements, t. VI', 'ref': "Pierre Margry, Découvertes et établissements des Français dans l'ouest et dans le sud de l'Amérique septentrionale, t. VI : Exploration des affluents du Mississippi et découverte des Montagnes Rocheuses (1679-1754), Paris, 1886"}, 'cihm_09946', lambda nom, ref: ref),
    ('ouest_margry_v1.txt', 'RA', {'court': 'Margry, Découvertes et établissements, t. I', 'ref': "Pierre Margry, Découvertes et établissements des Français dans l'ouest et dans le sud de l'Amérique septentrionale, t. I : Voyages des Français sur les grands lacs et découverte de l'Ohio et du Mississippi (1614-1684), Paris"}, 'dcouverteett01marg', lambda nom, ref: ref),
    ('ouest_margry_v2.txt', 'RB', {'court': 'Margry, Découvertes et établissements, t. II', 'ref': "Pierre Margry, Découvertes et établissements des Français dans l'ouest et dans le sud de l'Amérique septentrionale, t. II : Lettres de Cavelier de La Salle (1678-1685), Paris"}, 'dcouverteett02marg', lambda nom, ref: ref),
    ('ouest_margry_v3.txt', 'RD', {'court': 'Margry, Découvertes et établissements, t. III', 'ref': "Pierre Margry, Découvertes et établissements des Français dans l'ouest et dans le sud de l'Amérique septentrionale, t. III : Recherche des bouches du Mississippi et voyage à travers le continent (1669-1698), Paris"}, 'dcouverteett03marg', lambda nom, ref: ref),
    ('louisiane_fortier_histoire_v4_1904.txt', 'LJ', {'court': 'Fortier, A History of Louisiana, vol. 4 (1904)', 'ref': "Alcée Fortier, A History of Louisiana, vol. 4 : The American Domination, part II, 1861-1903, New York, Goupil & Co., 1904"}, 'historyoflouisia04fortuoft', lambda nom, ref: ref),
    ('arizona_sitgreaves_1853.txt', 'ZG', {'court': 'Sitgreaves, Report of an Expedition down the Zuni and Colorado Rivers (1853)', 'ref': "L. Sitgreaves, Report of an Expedition down the Zuni and Colorado Rivers, Washington, R. Armstrong, 1853"}, 'reportanexpidit00sitggoog', lambda nom, ref: ref),
    ('arizona_cooke_1878.txt', 'ZK', {'court': 'Cooke, The Conquest of New Mexico and California (1878)', 'ref': "P. St. G. Cooke, The Conquest of New Mexico and California, New York, G. P. Putnam's Sons, 1878"}, 'conquestofnewmex00cookrich', lambda nom, ref: ref),
    ('arizona_ahr_1930.txt', 'ZH', {'court': 'Arizona Historical Review (1930)', 'ref': "Arizona Historical Review, vol. 3, 1930"}, 'arizonahistorica03univ', lambda nom, ref: ref),
    ('utah_tullidge_1889.txt', 'UG', {'court': "Tullidge's Histories, vol. 2 (1889)", 'ref': "E. W. Tullidge, Tullidge's Histories, vol. 2, Northern Utah and Southern Idaho, Salt Lake City, Juvenile Instructor, 1889"}, 'tullidgeshistori02tull', lambda nom, ref: ref),
]

d = json.load(open(f'{R}/data/lieux.geojson', encoding='utf-8'))
garde = [f for f in d['features'] if not f['properties']['corpus'].startswith(CORPUS)]
from adresses import coin, ilot
from lieux_ouest import G as _G
from archive_commun import cle_personne, beau_nom, slug

def appliquer_adresses(fs, fichier, pre, livre, ident):
    """Place à leur adresse précise les fiches dont la source donne un coin de rues ; crée la fiche si elle n'existe pas."""
    deplacees = creees = 0
    for ligne in open(fichier, encoding='utf-8'):
        if not ligne.strip() or ligne.startswith('#'): continue
        brut, annees, rues, angle, quoi, page = [x.strip() for x in ligne.split('|')]
        r1, r2 = rues.split('/')
        lon, lat, lib = coin(r1, r2, angle or None)
        a0 = int(annees[:4])
        a1 = int(annees.split('-')[1]) if '-' in annees else a0
        k = cle_personne(brut)
        cible = [f for f in fs if f['properties']['id'].endswith(tuple(['-saint-loui', '-saint-loui-2', '-saint-loui-3', '-saint-loui-4']))
                 and cle_personne(f['properties'].get('_brut', '')) == k and int(f['properties']['debut']) == a0]
        nom = beau_nom(brut)
        if cible:
            f = cible[0]; p = f['properties']
            f['geometry']['coordinates'] = [lon, lat]
            p['nom'] = f"{lib} : {nom}"
            p['certitude'] = 'approximative'
            p['description'] += f" Emplacement : {lib.split(', ', 1)[1]} ({quoi}), d'après Billon, {page} ; position reconstituée sur le plan du village (± 50 m)."
            deplacees += 1
        else:
            idf = f"{pre}-{slug(brut)}-adr-{slug(r1 + '-' + r2)}"
            fs.append({"type": "Feature", "geometry": {"type": "Point", "coordinates": [lon, lat]}, "properties": {
                "id": idf, "nom": f"{lib} : {nom}", "corpus": f"{CORPUS} · {livre['court']}", "theme": 'personnage',
                "date_edtf": f"{a0}/{a1}" if a1 != a0 else str(a0), "debut": a0, "fin": a1 + 0.999, "precision": "annee",
                "certitude": 'approximative', "personnages": [nom],
                "description": f"{lib}, {a0 if a0 == a1 else f'{a0}-{a1}'}. {nom} {quoi}. D'après {livre['court']} ; position reconstituée sur le plan du village (± 50 m).",
                "sources": f"{livre['ref']}, {page} ; texte intégral : archive.org, {ident}.",
                "note": "Adresse tirée du texte intégral (OCR) d'archive.org ; l'emplacement du coin de rues est reconstitué sur le quadrillage actuel du centre-ville de Saint-Louis.",
                "livre": livre['court'], "voir_aussi": [{"url": f"https://archive.org/details/{ident}", "texte": "Lire le livre sur archive.org →"}]}})
            creees += 1
    print(f"  adresses : {deplacees} fiches placées à leur adresse, {creees} fiches d'adresse créées")
    return fs

def appliquer_ilots(fs, fichier, livre):
    """Place dans son îlot numéroté la fiche restée au point générique de Saint-Louis."""
    x0, y0 = _G['Saint-Louis'][:2]
    n_ok, manques = 0, []
    for ligne in open(fichier, encoding='utf-8'):
        if not ligne.strip() or ligne.startswith('#'): continue
        brut, annee, num, partie, page = [x.strip() for x in ligne.split('|')]
        lon, lat, lib, entre = ilot(int(num), partie)
        k = cle_personne(brut)
        cible = [f for f in fs if cle_personne(f['properties'].get('_brut', '')) == k and int(f['properties']['debut']) == int(annee)
                 and abs(f['geometry']['coordinates'][0] - x0) < 1e-6 and abs(f['geometry']['coordinates'][1] - y0) < 1e-6]
        if not cible:
            manques.append(brut); continue
        f = cible[0]; p = f['properties']
        f['geometry']['coordinates'] = [lon, lat]
        p['nom'] = f"{lib} : {beau_nom(brut)}"
        p['certitude'] = 'approximative'
        p['description'] += (f" Emplacement : {lib.split(', ', 1)[1]} du plan du village tracé par Laclède et Auguste Chouteau, {entre}"
                             f" (concessions de 1765 énumérées par Billon, {page}) ; position reconstituée sur le quadrillage actuel (± 50 m).")
        n_ok += 1
    print(f"  îlots : {n_ok} fiches placées dans leur îlot" + (f" ; non trouvées : {manques}" if manques else ''))
    return fs

nouv, bilan = [], []
for fic, pre, livre, ident, citer in LIVRES:
    ctxf = os.path.join(D, fic.replace('.txt', '_contextes.txt'))
    fs, inconnus, sans_date = fiches_livre(os.path.join(D, fic), pre, livre, ident, citer,
                                           contextes=lire_contextes(ctxf) if os.path.exists(ctxf) else None)
    adrf = os.path.join(D, fic.replace('.txt', '_adresses.txt'))
    if os.path.exists(adrf):
        fs = appliquer_adresses(fs, adrf, pre, livre, ident)
    ilf = os.path.join(D, fic.replace('.txt', '_ilots.txt'))
    if os.path.exists(ilf):
        fs = appliquer_ilots(fs, ilf, livre)
    nouv += fs
    bilan.append((livre['court'], len(fs), sans_date, sorted(inconnus)))
for f in nouv: f['properties'].pop('_brut', None)
ids = [f['properties']['id'] for f in nouv]
dbl = [i for i, n in collections.Counter(ids).items() if n > 1]
assert not dbl, dbl
# Corrections et renvois particuliers
for f in nouv:
    p = f['properties']
    if p['id'] == 'MO-aubry-francois-xavier-santa-fe':
        p['note'] = "Morice date la mort d'Aubry de 1855 ; elle eut lieu le 18 août 1854 à Santa Fe. " + p['note']
        p['voir_aussi'].append({"url": "https://geolas2023.github.io/Atlas-Aubry/index.html#lieu=L31", "texte": "La mort d'Aubry dans l'Atlas Aubry →"})
    if p['corpus'].endswith('Tassé (1878)') and 'François-Xavier Aubry' in p['personnages']:
        p['voir_aussi'].append({"url": "https://geolas2023.github.io/Atlas-Aubry/", "texte": "Aubry dans l'Atlas Aubry →"})
d['features'] = garde + nouv
json.dump(d, open(f'{R}/data/lieux.geojson', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for b in bilan:
    print(f"{b[0]} : {b[1]} fiches ; {b[2]} lieux sans date ignorés" + (f" ; lieux inconnus : {b[3]}" if b[3] else ''))
print(f"Total Bibliothèque archive.org : {len(nouv)} ; atlas : {len(d['features'])}")
