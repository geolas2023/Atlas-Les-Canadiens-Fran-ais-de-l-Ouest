# Honoré Beaugrand, Six mois dans les Montagnes-Rocheuses : Colorado, Utah, Nouveau-Mexique (Montréal, Granger, 1890),
# epub Project Gutenberg du Drive de l'auteur (dossier HISTOIRE_QUEBEC_CANADA_COMPILATION). Voyage de l'hiver 1889-1890.
# Corpus « Recherches », préfixe BG90.
from commun import Corpus
BG = "Beaugrand, Honoré (1890), Six mois dans les Montagnes-Rocheuses : Colorado, Utah, Nouveau-Mexique, préface de Louis Fréchette, Montréal, Granger Frères"
C = Corpus('Recherches', 'BG90', BG, page_fmt='{}')
F = C.F
F('01', "Manitou Springs et le mont Pike : la « Fontaine-qui-bouille » et la « grosse montagne bleue » des trappeurs canadiens", 'toponymie', '1889~/1890', -104.9172, 38.8597, 'c', ['Honoré Beaugrand'],
  "En séjour de santé à Manitou, Beaugrand note que les trappeurs canadiens connaissaient le mont Pike sous le nom de « grosse montagne bleue ». Ils appelaient aussi les sources bicarbonatées de Manitou, que les Américains nomment Shoshone, Navajo, Manitou et Little Chief, la Fontaine-qui-bouille. Il y rencontre des Canadiens parmi les curistes venus d'Europe et d'Amérique.",
  'chap. IV')
F('02', "Avec Pike, à travers les prairies : les interprètes canadiens Rainville et Rousseau (1806)", 'exploration', '1806', -104.8214, 38.8339, 'h', ['Rainville', 'Rousseau', 'Zebulon Pike'],
  "Beaugrand écrit que le détachement envoyé par le gouvernement américain sous le major Pike, après la vente de la Louisiane, traversa les prairies à l'ouest du Mississippi jusqu'aux Rocheuses sous la conduite de deux guides-interprètes canadiens-français, nommés Rainville et Rousseau. Il ajoute qu'un autre Canadien, Carrière, aurait découvert de l'or dans le lit de la Platte en 1835.",
  'chap. IV', "Affirmations de Beaugrand, sans référence : noms à vérifier dans le journal de Pike. Point placé près du mont Pike.")
F('03', "Española : deux marchands canadiens de Lachute, et les familles Beaubien, Mercure, Saint-Vrain et Cloutier du Rio Grande (1890)", 'commerce', '1890', -106.0806, 35.9911, 'c', ['Honoré Beaugrand', 'Charles Bent'],
  "À Española, centre commercial de la vallée des pueblos de San Juan, Santa Clara et San Ildefonso, Beaugrand rencontre deux Canadiens de Lachute qui tiennent de grands magasins et font un commerce important avec les cultivateurs et les éleveurs. Il assure avoir trouvé des compatriotes partout au Colorado et au Nouveau-Mexique : les familles Beaubien, Mercure, Saint-Vrain et Cloutier sont bien connues dans la vallée du Rio Grande. La veuve du gouverneur Bent, une Beaubien selon lui, vit encore à Taos.",
  'chap. X', "Beaugrand se trompe sur la veuve de Bent, Ignacia Jaramillo ; c'est Narciso Beaubien qui fut tué avec Bent en 1847.")
F('04', "Rio Colorado (Grand Canyon) : Félix Lantier, chercheur d'or canadien rencontré par l'expédition Stanton (janvier 1890)", 'personnage', '1889~/1890-01', -111.8, 36.4, 'h', ['Félix Lantier', 'Robert Brewster Stanton', 'Denis Julien'],
  "Beaugrand rapporte que l'expédition de l'ingénieur Stanton, descendant les gorges du Colorado, trouva gravée dans le roc l'inscription « D. JULIEN-1833 » (qu'il transcrit « I. JULIEN »), preuve du passage de voyageurs canadiens 36 ans avant Powell. Plus loin, en janvier 1890, l'expédition aperçut à plus de 5 000 pieds sous le rebord un mineur solitaire qui cherchait des paillettes d'or sur une grève. Il vivait seul de chasse et de pêche depuis plus d'un an : c'était un Canadien français nommé Félix Lantier.",
  'chap. XIII', "Lieu non précisé : point placé dans le Marble Canyon. Le Félix Lantier de Beaugrand reste à identifier.")
F('05', "Santa Fe : un archevêché français, de Mgr Lamy au clergé du Nouveau-Mexique (1875-1890)", 'religion', '1875-06-16/1890', -105.9378, 35.6870, 'c', ['Jean-Baptiste Lamy'],
  "Beaugrand rappelle que Santa Fe fut érigée en archevêché, avec le Colorado et l'Arizona pour suffragants, et que Mgr Jean-Baptiste Lamy reçut le pallium le 16 juin 1875. Il trouve curieux que l'archevêque et la plupart des prêtres du diocèse soient français, alors que l'élément d'origine française ne compte que de rares représentants hors du clergé.",
  'chap. IX')
fiches = C.fiches
