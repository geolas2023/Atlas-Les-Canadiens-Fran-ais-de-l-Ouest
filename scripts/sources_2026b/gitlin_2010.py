# Jay Gitlin, The Bourgeois Frontier: French Towns, French Traders, and American Expansion (New Haven, Yale UP, 2010),
# PDF du Drive de l'auteur (passe complète, 20 nov. 2026 ; le reste recoupe les fiches Chouteau, Robidoux, Beaubien, Campau existantes).
# Corpus « Recherches », préfixe GT10.
from commun import Corpus
GT = "Gitlin, Jay (2010), The Bourgeois Frontier: French Towns, French Traders, and American Expansion, New Haven, Yale University Press"
C = Corpus('Recherches', 'GT10', GT, page_fmt='p. {} (PDF)')
F = C.F
F('01', "Saint-Paul : la justice rendue en français, l'anecdote du major Noah et de l'avocat Brisbin (années 1850)", 'evenement', '1850~/1858~', -93.0900, 44.9440, 'c', ['Charles Flandrau', 'Henry H. Sibley', 'John Brisbin'],
  "D'après les souvenirs du juge Charles Flandrau, rapportés par Gitlin, le français était souvent la langue des affaires à Saint-Paul pendant la période territoriale. Un avocat diplômé de Yale, John Brisbin, plaide longuement en anglais. Son adversaire, le major Noah, associé de Sibley, répond en français ; Brisbin objecte qu'il faut plaider en anglais. Noah réplique qu'il ne fait que traduire l'argument de son confrère, puisque le juge ne comprend pas un mot d'anglais, ce qui était vrai.",
  '193-194')
F('02', "Saint-Paul : les francophones du territoire, de Bazille à Larpenteur, et la querelle en français de l'Écossais McLeod (1843-1877)", 'personnage', '1843/1877', -93.0900, 44.9440, 'c', ['Charles Bazille', 'Benjamin Gervais', 'Louis Robert', 'Louis Desnoyer', 'Auguste Louis Larpenteur', 'Henry H. Sibley', 'Norman Kittson', 'George McLeod', 'Le Boutillier'],
  "Les francophones de Saint-Paul viennent de Prairie du Chien et de Montréal (Charles Bazille), de la Rivière-Rouge (Benjamin Gervais, né à Rivière-du-Loup) ou des communautés créoles de Saint-Louis (Louis Robert, capitaine de vapeur né à Carondelet, et son beau-frère Louis Desnoyer). Auguste Louis Larpenteur, dont la famille avait fui la Restauration en 1816, arrive en 1843 comme commis, engagé surtout parce qu'il parle français. Le gouverneur Sibley, né à Détroit, rédige encore en 1877 une brochure en français sur les obligations ferroviaires de l'État. Le recensement compte 29 natifs de France au Minnesota en 1850 et plus de 800 en 1860. Blessé en 1856, le député écossais George McLeod rabroue en français le docteur Le Boutillier : on peut plier le bras d'un Écossais, pas le casser.",
  '193-194')
F('03', "Minneapolis et Saint-Paul : l'Écho de l'Ouest, Le Canadien et la Ligue républicaine Lafayette-Papineau (fin XIXe siècle)", 'etablissement', '1877~/1900~', -93.2650, 44.9778, 'a', [],
  "La seconde vague, venue du Québec, se donne ses journaux (l'Écho de l'Ouest à Minneapolis, Le Canadien à Saint-Paul) et ses clubs : le Club Démocratie franco-américaine, la Ligue républicaine Lafayette-Papineau, des cercles littéraires et de théâtre. Pour Gitlin, le nom de Papineau marque une « recanadianisation » du Minnesota, rattachée à l'histoire du Québec du XIXe siècle plutôt qu'à celle de la traite.",
  '196-197', "Point placé à Minneapolis ; dates approximatives.")
F('04', "Vallées de la Jocko et de la Mission (Montana) : un village français et des éleveurs métis, Allard, Rivais, Morigeau, Courville (fin XIXe siècle)", 'etablissement', '1870~/1900~', -114.1, 47.35, 'a', ['Allard', 'Rivais', 'Morigeau', 'Courville'],
  "Gitlin signale qu'à la fin du XIXe siècle, on trouve dans les vallées de la Jocko et de la Mission, au Montana (pays salish et kutenai), un village français et nombre d'éleveurs et de traiteurs français et métis prospères, portant les noms d'Allard, Rivais, Morigeau ou Courville.",
  '99', "Point placé entre Arlee (Jocko) et St. Ignatius (Mission).")
fiches = C.fiches
