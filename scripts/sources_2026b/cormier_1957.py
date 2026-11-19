# Louis-Philippe Cormier, « La presse française de l'Illinois », Revue d'histoire de l'Amérique française, vol. 11, n° 3 (1957),
# p. 361-392, PDF Érudit du Drive de l'auteur. Corpus « Recherches », préfixe CO57.
from commun import Corpus
CO = "Cormier, Louis-Philippe (1957), « La presse française de l'Illinois », Revue d'histoire de l'Amérique française, vol. 11, n° 3, p. 361-392"
C = Corpus('Recherches', 'CO57', CO, page_fmt='p. {}')
F = C.F
CHI = (-87.6320, 41.8820)
F('01', "Nauvoo : Colonie icarienne, premier journal de langue française de l'Illinois (1854)", 'etablissement', '1854-07-19/1854-12-27', -91.3850, 40.5500, 'c', ['Étienne Cabet'],
  "Le premier titre de la liste chronologique de Cormier est la Colonie icarienne, « journal d'organisation sociale » de la communauté utopiste fondée à Nauvoo par Étienne Cabet. L'hebdomadaire paraît du 19 juillet au 27 décembre 1854 (22 numéros).",
  '386-387')
F('02', "Kankakee : Le Journal de l'Illinois d'Alexandre Grandpré et C. Petit (1857-1863)", 'etablissement', '1857-01-02/1863~', -87.8610, 41.1200, 'c', ['Alexandre Grandpré', 'C. Petit'],
  "Fondé le 2 janvier 1857 à Kankakee, Le Journal de l'Illinois se dit indépendant en tout, neutre en rien. Il passe quelques mois à Chicago (de l'automne 1857 à l'été 1858) avant de revenir à Kankakee. Cormier corrige la date de 1855 que lui donneront plus tard ses successeurs.",
  '387')
F('03', "Kankakee puis Chicago : Le Courrier de l'Illinois, le journal de Grandpré (1868-1896)", 'etablissement', '1868/1896-06-18', -87.8610, 41.1200, 'c', ['Alexandre Grandpré'],
  "Fondé en 1868 sous le nom de Courrier de l'Ouest, devenu vers 1875 le Courrier de l'Illinois, l'hebdomadaire d'Alexandre Grandpré a pour devise « Notre nationalité avant tout ». Neutre au départ, il se déclare républicain en 1876. Il passe à Chicago vers 1880 et à huit pages en 1890. Le 18 juin 1896, Grandpré le vend à la Franco-American Publishing Co. Pour Cormier, ses 36 ans de publication sont la « belle période » de la presse française de l'Illinois.",
  '386-389')
F('04', "Chicago : L'Amérique de Guéroult et Pinta, où Louis Fréchette annonce son cabinet d'avocat (1869-1870)", 'etablissement', '1869-09-07/1870', *CHI, 'c', ['Guéroult', 'Samuel-E. Pinta', 'Louis Fréchette'],
  "Bi-hebdomadaire publié au 162, rue Madison par Guéroult et le Louisianais Pinta, L'Amérique paraît à partir du 7 septembre 1869. Une annonce aux marchands y estime à 20 000 personnes la population de langue française de Chicago. Parmi les petites annonces figure celle de L. H. Fréchette, avocat, consultable au bureau de rédaction. Pinta avait déjà publié L'Observateur en 1861 ; Fréchette fonda plus tard un éphémère journal du même nom.",
  '387-388')
F('05', "Chicago : Le Figaro illustré, hebdomadaire français à gravures (1886-1887)", 'etablissement', '1886-10-30/1887', -87.6295, 41.8790, 'c', ['C. Gentilé', 'A. Gouêre', 'L. R. de Sainte-Foy'],
  "Publié au 296, rue Dearborn par la French Publishing Co., Le Figaro illustré promet 416 pages et 156 gravures par an, imprimées sur papier glacé. Il paraît au moins trois mois.",
  '389')
F('06', "Bourbonnais : Le Cercle français du collège Saint-Viateur et Le Journal de Bourbonnais (1885-1888)", 'religion', '1885/1888', -87.8880, 41.1530, 'c', [],
  "Le collège Saint-Viateur publie en 1885 Le Cercle français. Un Journal de Bourbonnais existe en 1888 : le Courrier de l'Illinois du 14 décembre en reprend une nouvelle.",
  '388-389')
F('07', "Chicago : Le Combat du docteur Elzéar Paquin (vers 1889-1893)", 'etablissement', '1889/1893~', *CHI, 'c', ['Elzéar Paquin'],
  "Le Combat, fondé par le médecin Elzéar Paquin, est si discret que le Courrier de l'Illinois demande en 1890, par une lettre satirique, s'il est mort ou vivant. Les historiens lui donnent deux ans d'existence, mais Paquin affirme à la convention de 1893 l'avoir publié pendant quatre ans.",
  '389')
F('08', "Chicago : les journaux de Louis-J. Bachand-Vertefeuille, du Courrier de l'Ouest au Courrier franco-américain (1894-1931)", 'etablissement', '1894/1931~', -87.6470, 41.8740, 'c', ['Louis-J. Bachand-Vertefeuille', 'Philippe Masson', 'Anatole Bachand'],
  "Bachand-Vertefeuille lance Le Bulletin officiel des sociétés de langue française (1894). Il devient en 1903 seul propriétaire du Courrier de l'Ouest (successeur bi-hebdomadaire du journal de Grandpré, dirigé d'abord par Philippe Masson), puis tente un quotidien, Le Petit Journal de Chicago (juin-juillet 1903). Le Courrier-Canadien fusionne ensuite les titres de Kankakee, de Saint-Paul et de Minneapolis ; il devient en 1905 Le Courrier franco-américain, organe de l'Union des sociétés canadiennes-françaises catholiques, publié à l'édifice New Era et inscrit aux annuaires jusqu'en 1931. Cormier y voit la seconde période, plus conformiste, liée au déclin de la colonie.",
  '386, 389-392', "Point placé à l'angle Harrison et Halsted (édifice New Era).")
fiches = C.fiches
