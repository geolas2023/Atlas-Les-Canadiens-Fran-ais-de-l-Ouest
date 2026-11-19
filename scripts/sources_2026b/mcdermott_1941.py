# John Francis McDermott, A Glossary of Mississippi Valley French, 1673-1850 (Saint-Louis, Washington University Studies,
# Language and Literature n° 12, 1941), PDF du Drive de l'auteur. Corpus « Recherches », préfixe MD41 : sobriquets et noms de lieux.
from commun import Corpus
MD = "McDermott, John Francis (1941), A Glossary of Mississippi Valley French, 1673-1850, Saint-Louis, Washington University Studies, Language and Literature n° 12"
C = Corpus('Recherches', 'MD41', MD, page_fmt='p. {} (PDF)')
F = C.F
F('01', "Saint-Louis, dit « Paincourt » : un sobriquet colonial mal compris", 'toponymie', '1764/1804', -90.1866, 38.6268, 'c', [],
  "Sous le régime colonial, Saint-Louis était surnommé Paincourt. Selon McDermott, le sobriquet vient de ce que la ville vivait du commerce plutôt que de l'agriculture ; on l'a interprété à tort comme un signe de pauvreté. Il renvoie à son article « Paincourt and Poverty », où il montre que les inventaires des habitants décrivent un niveau de vie confortable.",
  '128')
F('02', "Sainte-Geneviève, dite « Misère », et Kaskaskia, dite « Pouilleux » : des sobriquets d'une rive à l'autre", 'toponymie', '1750~/1804', -90.0418, 37.9814, 'c', [],
  "Le glossaire de McDermott relève que Sainte-Geneviève était surnommée Misère, pour signifier en plaisantant que le bourg comptait peu. En représailles, Kaskaskia, sur l'autre rive du Mississippi, reçut le sobriquet de Pouilleux, au sens de méprisable.",
  '122, 145', "Point placé à Sainte-Geneviève ; Kaskaskia est en face, sur la rive illinoise.")
F('03', "Carondelet, dit « Vide-Poche »", 'toponymie', '1767~/1850', -90.2627, 38.5612, 'c', [],
  "Le village de Carondelet, aujourd'hui quartier de Saint-Louis, avait pour sobriquet Vide-Poche.",
  '164')
F('04', "Saint-Charles, le village des « Petites Côtes » (Las Pequeñas Cuestas)", 'toponymie', '1769/1804', -90.4840, 38.7881, 'c', [],
  "Pendant ses premières années, Saint-Charles était appelé l'établissement des Petites Côtes : les escarpements s'y éloignent en douces collines au lieu de tomber à pic dans le Missouri. Les documents espagnols traduisent le nom par Las Pequeñas Cuestas. Selon McDermott, ce n'était pas un sobriquet comme Paincourt ou Misère.",
  '133')
F('05', "Saint-Louis : de Gilles Michel à Joseph Michel dit Taillon, comment le « dit » devient nom de famille", 'famille', '1764/1799', -90.1866, 38.6268, 'c', ['Joseph Michel dit Taillon', 'Gilles Michel', 'Jean Hamilton dit l\'Anglais', 'Antoine Melloche dit Hibernois'],
  "McDermott illustre le surnom « dit » par l'exemple de Gilles Michel, établi au Canada au milieu du XVIIe siècle et aussi appelé Taillon. Cent ans plus tard, son arrière-petit-fils Joseph Michel s'installe à Saint-Louis, où il est appelé Joseph Michel Taillon, Joseph Michel dit Taillon ou Joseph Taillon : le surnom est devenu le nom de famille. Le glossaire cite d'autres surnoms du Saint-Louis colonial, comme Jean Hamilton dit l'Anglais, qui s'engagea en 1767 à bâtir un moulin pour Laclède, ou Antoine Melloche dit Hibernois.",
  '85-86')
fiches = C.fiches
