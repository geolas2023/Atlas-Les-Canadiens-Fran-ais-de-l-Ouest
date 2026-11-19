# Barry Jean Ancelet, « Québec, Acadie et Louisiane : l'influence des retrouvailles » (article, Université de la
# Louisiane à Lafayette, s.d., après 2000). PDF du Drive de l'auteur (dossier Louisiane). Corpus « Recherches », préfixe ANC.
from commun import Corpus
AN = "Ancelet, Barry Jean (s.d.), « Québec, Acadie et Louisiane : l'influence des retrouvailles », article"
C = Corpus('Recherches', 'ANC', AN, page_fmt='p. {}')
F = C.F
F('01', "Lafayette : du bicentenaire du Grand Dérangement au CODOFIL (1955-1974)", 'evenement', '1955/1974', -92.0198, 30.2241, 'c', ['James Domengeaux', 'Wade Martin', 'Allen Babineaux', 'Léonard Forest', 'Edith Butler'],
  "En 1955, Acadiens du Nord et Cadiens de Louisiane se retrouvent pour le bicentenaire du Grand Dérangement. Un Comité de l'héritage français, formé en 1965 pour le bicentenaire de l'arrivée des Acadiens en Louisiane (Wade Martin, Allen Babineaux, James Domengeaux), mène en 1968 à la création du Conseil pour le développement du français en Louisiane (CODOFIL), agence de l'État même qui avait banni le français des écoles en 1916. La même année, le cinéaste Léonard Forest et des personnages de son documentaire Les Acadiens de la dispersion, dont une jeune Edith Butler, viennent en Louisiane pour sa première. Le Conseil se dote ensuite d'une politique populaire, visible en 1974 avec le premier Festival de musique acadienne.",
  '1-3', "Article non daté, postérieur aux Congrès mondiaux acadiens. Point à Lafayette, siège du CODOFIL.")
fiches = C.fiches
