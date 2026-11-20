# Maria R. Audubon (éd.), Audubon and his Journals, New York, Scribner, 1897, vol. 1 : début des « Missouri River
# Journals » (avril-juin 1843, notes d'Elliott Coues). PDF archive.org du Drive (audubonhisjourna01audu), lu en entier.
# Corpus « Recherches », préfixe AJ43 (le vol. 2 est sous AU43).
from commun import Corpus
AJ = "Audubon, Maria R. (éd.) (1897), Audubon and his Journals, vol. 1, New York, Scribner"
C = Corpus('Recherches', 'AJ43', AJ, page_fmt='p. {}')
F = C.F
F('01', "Saint-Louis : l'Omega part avec 101 engagés, surtout Canadiens français et Créoles (25 avril 1843)", 'evenement', '1843-04-25/1843-04-26', -90.184, 38.626, 'c', ['John James Audubon', 'John B. Sarpy', 'Joseph Sire', 'Étienne Provost'],
  "Le 25 avril 1843 à 11 h 30, le vapeur Omega de la compagnie Chouteau quitte Saint-Louis avec Audubon et sa troupe, Sarpy et cent un trappeurs de près d'une douzaine de nationalités, en majorité des Canadiens français ou des Créoles du Missouri, plusieurs ivres. Une fois l'équipage et les « engagés » à bord, Sarpy, registre en main, fait l'appel des noms dans la grande cabine, où les bagages des hommes ont été entassés. Le vapeur atteint Saint-Charles à 4 h 20 le lendemain ; Sarpy y débarque et rentre en voiture.",
  '455-457', "Pages imprimées (PDF p. 513-515). Le vieux Provost voyage sur le même vapeur.")
F('02', "Plantation de Pierre Chouteau père : la chasse aux « muloes » avec le docteur Trudeau (13 avril 1843)", 'evenement', '1843-04-12/1843-04-13', -90.255, 38.636, 'a', ['John James Audubon', 'Pierre Chouteau', 'Pierre Chouteau fils', 'John B. Sarpy', 'Trudeau'],
  "Le 12 avril 1843, Audubon vient avec Sarpy à la plantation de Pierre Chouteau père, à quatre milles à l'ouest de Saint-Louis, pour se procurer des gaufres à poche. Le lendemain, Chouteau fait venir des esclaves avec des bêches pour creuser les galeries des « muloes », nom créole tiré du français « mulots », en présence du docteur Trudeau, de Saint-Louis, et des Chouteau père et fils. Audubon en garde plusieurs vivants quelques jours.",
  '463-464', "Pages imprimées (PDF p. 521-522). Point approximatif à quatre milles à l'ouest du vieux Saint-Louis.")
F('03', "Bellevue : le beau-frère du « vieux Provost » tient le magasin de Sarpy (9 mai 1843)", 'personnage', '1843-05-09', -95.89, 41.137, 'c', ['Étienne Provost', 'Peter A. Sarpy', 'John James Audubon'],
  "À l'escale de Bellevue, Audubon trouve absents Peter Sarpy, frère de celui de Saint-Louis, et l'agent des Indiens, partis sur la Platte à 300 milles de là. Le magasin est tenu par « le beau-frère du vieux Provost », qui fait office de commis. Le poste paraît modeste mais commerce beaucoup avec les Indiens de la Platte ; Audubon voit payer huit cordes de bois avec cinq tasses de sucre et trois de café.",
  '477', "Pages imprimées (PDF p. 537). Le beau-frère n'est pas nommé ; voir l'atlas Provost (L56).")
F('04', "Rivière à Jacques (James River) : le nom d'un chasseur de castor oublié (20 mai 1843)", 'lieu', '1843-05-20', -97.42, 42.87, 'a', ['John James Audubon'],
  "En passant l'embouchure de la James River le 20 mai 1843, Audubon la nomme « la Rivière à Jacques » et explique qu'elle tient son nom d'un homme qui s'était établi sur ses bords une vingtaine d'années plus tôt et y avait gagné de l'argent en récoltant le castor, mort depuis. Coues note que cette origine est connue de peu de gens.",
  '503', "Pages imprimées (PDF p. 561). Point à l'embouchure de la James, près de Yankton.")
F('05', "Fort Pierre : Picotte, Chardon et le chasseur métis Alexis Bombarde (30 mai-2 juin 1843)", 'poste', '1843-05-30/1843-06-02', -100.38, 44.4, 'c', ['Honoré Picotte', 'Francis A. Chardon', 'Alexis Bombarde', 'John James Audubon'],
  "Le 30 mai 1843, Honoré Picotte et Chardon abordent l'Omega dans la yole du Trapper ; le lendemain, Audubon est reçu au fort Pierre, où Picotte lui offre un énorme bois d'élan et des calumets, et lui montre ses ballots de peaux de lièvre. Cinquante engagés et la moitié de la cargaison restent au fort. Au départ, un Indien caché à bord pour tuer Chardon, qui l'avait battu pour vol, est découvert. Chardon confie à Audubon jusqu'à la Yellowstone le chasseur Alexis Bombarde, un métis puissamment bâti aux cheveux longs, « chasseur de premier ordre ».",
  '527-533', "Pages imprimées (PDF p. 588-593).")
fiches = C.fiches
