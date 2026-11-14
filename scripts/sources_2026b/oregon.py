# René Bergeron, La légende de l'Oregon était vraie. La grande migration vers l'Ouest des Canadiens français
# par la piste de l'Oregon (brochure illustrée, 49 p.). Pages : pagination imprimée de la brochure.
from commun import Corpus
C = Corpus('Piste de l\'Oregon', 'OR',
           "Bergeron, René, La légende de l'Oregon était vraie. La grande migration vers l'Ouest des Canadiens français par la piste de l'Oregon, Laval, René Bergeron éditeur, s. d.")
F = C.F

F('01', "Saint-Louis, porte de l'Ouest", 'migration', '1841/1869', -90.19, 38.63, 'c', [],
  "Chaque printemps de 1841 à l'arrivée du chemin de fer (1869), les émigrants vers l'Oregon convergent vers Saint-Louis, ville fondée en 1764, puis remontent le Missouri en vapeur jusqu'à Independence. Parmi eux, des Canadiens français venus du Canada, de l'Est et des vieux établissements du Midwest (Saint-Charles, Sainte-Geneviève, Kaskaskia).", '4; 10')
F('02', 'Independence (Missouri), départ de la piste', 'migration', '1843-04/1843-05', -94.42, 39.09, 'c', [],
  "Au printemps 1843, près de mille émigrants campent autour d'Independence pour former le premier grand convoi vers l'Oregon. Les cent premiers kilomètres empruntent la piste de Santa Fe.", '10; 13')
F('03', 'Traversier Papin sur la rivière Kansas (Topeka)', 'commerce', '1844~/1859', -95.68, 39.06, 'a', ['Joseph Papin', 'Louis Papin'],
  "Vers 1844, Joseph Papin, fils du Montréalais Louis Papin, met en service un traversier (Pappan's ferry) sur la rivière Kansas ; il sert les émigrants jusqu'à la fin des années 1850.", '15')
F('04', 'Rock Creek (Kansas) : Amable Aubry dit Francoeur, forgeron', 'famille', '1841/1845', -96.23, 39.2, 'h', ['Amable Aubry dit Francoeur', 'Pélagie Gonville'],
  "Amable Aubry dit Francoeur, marié à Pélagie Gonville, une Kansa, est forgeron dans la région entre 1841 et 1845. L'auteur le croit probablement oncle de François-Xavier Aubry.", '15',
  "Lien de parenté avec F.-X. Aubry présenté comme probable par l'auteur, sans preuve citée. Emplacement de Rock Creek approximatif (vallée de la Kansas). À verser aussi à l'Atlas Aubry.")
F('05', 'Fort Laramie : James Bordeaux, commandant', 'poste', '1834/1849~', -104.558, 42.203, 'c', ['James Bordeaux'],
  "Construit en 1834 au confluent de la Laramie et de la North Platte par William Sublette, le poste de traite est ensuite commandé par le Canadien français James Bordeaux avant de devenir Fort Laramie.", '20')
F('06', 'Fort Laramie : magasin de Jules Lamoureux', 'commerce', '1860~', -104.558, 42.203, 'c', ['Jules Lamoureux'],
  "Vers 1860, Jules Lamoureux, natif de Saint-Hyacinthe, tient le magasin du fort, bien garni mais cher. En 1850, la garnison avait compté 50 000 voyageurs (44 000 vers la Californie, 6 000 vers l'Oregon).", '20')
F('07', 'Pont de Jean-Baptiste Richard sur la North Platte', 'commerce', '1852', -106.27, 42.86, 'a', ['Jean-Baptiste Richard'],
  "En 1852, Jean-Baptiste Richard, né au Missouri, bâtit un pont à péage sur la North Platte ; il en tire 40 000 $ la première année et l'annonce jusqu'au Missouri.", '21')
F('08', 'Pont et poste de Louis Guinard (Fort Caspar)', 'poste', '1859/1867', -106.37, 42.84, 'c', ['Louis Guinard'],
  "En 1859, Louis Guinard, Canadien français né au Québec et émigré en 1846, construit un nouveau pont et un poste de traite. L'armée bâtit Fort Caspar sur son emplacement en 1862 pour protéger le télégraphe ; pont et fort sont incendiés en 1867.", '21; 22')
F('09', 'South Pass : André Vallée, guide de Robert Stuart', 'exploration', '1812', -108.9, 42.36, 'a', ['André Vallée', 'Robert Stuart'],
  "En 1812, au retour d'Astoria vers Saint-Louis, Robert Stuart et le guide André Vallée, employés d'Astor, franchissent le col de South Pass, futur passage de la piste de l'Oregon resté méconnu une trentaine d'années.", '7; 24')
F('10', 'Fort Bridger : Théodore Talbot', 'exploration', '1843-09-07', -110.385, 41.318, 'a', ['Théodore Talbot'],
  "Le 7 septembre 1843, Théodore Talbot, de l'expédition Frémont, note dans son journal le passage difficile de Big Hill, au-delà de Fort Bridger.", '25')
F('11', 'Fort Boise : François Payette, commandant', 'poste', '1835/1844', -116.99, 43.79, 'a', ['François Payette', 'John C. Frémont'],
  "De 1835 à 1844, le fort de la Compagnie de la baie d'Hudson est commandé par François Payette, né à L'Assomption. Il accueille les Whitman (1836), John Sutter (1838) et Frémont (8 octobre 1843), qui loue son hospitalité.", '29')
F('12', 'Saint-Cuthbert : retraite de François Payette', 'migration', '1844', -73.24, 46.15, 'a', ['François Payette'],
  "À sa retraite en 1844, François Payette achète une ferme sur le rang Nord de la rivière Chicot, à Saint-Cuthbert (comté de Berthier).", '29')
F('13', 'Mission Whitman (Waiilatpu) : Charles Campeau', 'exploration', '1836-07-04', -118.464, 46.042, 'a', ['Charles Campeau', 'Marcus Whitman'],
  "Le 4 juillet 1836, le groupe de Marcus et Narcissa Whitman, accompagné de l'interprète Charles Campeau, qui parle le nez-percé, franchit les Rocheuses avec un chariot couvert, une première.", '7; 30')
F('14', 'Fort Walla Walla : Pierre-Chrysologue Pambrun', 'poste', '1832/1841-05-15', -118.98, 46.06, 'c', ['Pierre-Chrysologue Pambrun'],
  "Pierre-Chrysologue Pambrun, natif de L'Islet, commande de 1832 à 1841 le poste de la Compagnie de la baie d'Hudson (ancien fort Nez-Percés, 1818). Il y meurt le 15 mai 1841 des suites d'une chute de cheval.", '30')
F('15', 'Fort Walla Walla : arrivée des abbés Blanchet et Demers', 'religion', '1838-11-18', -118.98, 46.06, 'c', ['François-Norbert Blanchet', 'Modeste Demers', 'Pierre-Chrysologue Pambrun'],
  "Le 18 novembre 1838, Pambrun reçoit les deux premiers missionnaires catholiques de l'Oregon : Modeste Demers (Saint-Nicolas) et François-Norbert Blanchet (Montmagny), futur archevêque d'Oregon City.", '30')
F('16', 'Fort Walla Walla : Jean-Baptiste Toupin, interprète', 'commerce', '1824/1841', -118.98, 46.06, 'c', ['Jean-Baptiste Toupin'],
  "Né à Maskinongé, Jean-Baptiste Toupin est interprète au fort de 1824 à 1841, puis s'établit dans la vallée de la Willamette, près de l'actuelle Salem.", '30')
F('17', 'Walla Walla : J.-B. Brouillet, vicaire général', 'religion', '1847', -118.34, 46.065, 'a', ['Jean-Baptiste Brouillet'],
  "Jean-Baptiste Brouillet, de la région de Montréal, arrive en 1847 comme vicaire général du diocèse de Walla Walla (Nisqually), l'année du drame de la mission Whitman.", '30')
F('18', 'Fort Vancouver : John McLoughlin', 'poste', '1825/1845', -122.661, 45.625, 'c', ['John McLoughlin'],
  "John (Jean-Baptiste) McLoughlin, né à Rivière-du-Loup en 1784, commande Fort Vancouver et aide les émigrants américains ; accusé de les favoriser, il quitte la Compagnie de la baie d'Hudson en 1845.", '2; 32')
F('19', 'Oregon City, terminus de la piste', 'etablissement', '1843/1850~', -122.606, 45.357, 'c', ['John McLoughlin', 'Modeste Demers'],
  "Les émigrants y sont accueillis par leurs compatriotes : chapelle catholique, moulin à blé de McLoughlin, scieries, une centaine de maisons. Modeste Demers en devient le premier curé.", '33')
F('20', 'French Prairie (Champoeg, Saint-Paul, Gervais, Butteville)', 'etablissement', '1830/1839', -122.97, 45.21, 'a',
  ['Michel Laframboise', 'Joseph Gervais', 'Étienne Lucier', 'Jean-Baptiste Desportes', 'Pierre Bélèque', 'Louis Forcier'],
  "Dans les années 1830, d'anciens engagés de la traite s'établissent les premiers dans la vallée de la Willamette (Laframboise, Desportes, Gervais, Perrault, Lucier, Lacoste, Bélèque, Longpré, Fournier, Plante, Picard, Roy, Forcier…). À la fin de la décennie, 65 à 70 familles occupent la Prairie française et fondent Butteville, Saint-Paul, Saint-Louis et Gervais.", '34',
  "L'auteur cite Tassé (1878) : 700 à 800 Canadiens en Oregon en 1838.")
F('21', 'Expéditions Frémont : les Canadiens français', 'exploration', '1842/1848', -101.0, 41.1, 'h',
  ['John C. Frémont', 'Basile Lajeunesse', 'François Lajeunesse', 'Clément Lambert', 'Jean-Baptiste Bernier', 'Alexis Godey'],
  "La plupart des hommes des expéditions de Frémont sont des Canadiens français du Missouri et du Nouveau-Mexique : Basile et François Lajeunesse, Clément Lambert, Descôteaux, J.-B. Bernier, Alexis Godey… L'auteur en dresse la liste (Archambault, Ayot, Badeau, Beaulieu, Benoit, Cadotte, Charbonneau, etc.).", '35; 39',
  "Point symbolique sur la vallée de la Platte, suivie par la première expédition (1842).")
F('22', 'Kaskaskia : Lucien Maxwell, petit-fils de Pierre Ménard', 'famille', '1818', -89.914, 37.92, 'a', ['Lucien Maxwell', 'Pierre Ménard'],
  "Lucien Maxwell, chef des chasseurs de Frémont, est né à Kaskaskia ; sa mère Odile est fille de Pierre Ménard, natif de Chambly et premier lieutenant-gouverneur de l'Illinois.", '41')
F('23', 'Hiver 1848-1849 : trois Canadiens morts dans les San Juan', 'evenement', '1848-12/1849-01', -106.6, 37.7, 'h', ['John C. Frémont'],
  "Lors de la quatrième expédition de Frémont, prise dans les neiges des montagnes San Juan, dix hommes meurent de faim et de froid, dont trois Canadiens français.", '44')

fiches = C.fiches
