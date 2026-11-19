# Arthur Buies, Chroniques, tome II : Voyages, Québec, C. Darveau, 1875 (édition Wikisource, epub du Drive de
# l'auteur), chapitre « Départ pour la Californie. Deux mille deux cents lieues en chemin de fer » (juin 1874).
# Corpus « Recherches », préfixe BU75.
from commun import Corpus
BU = "Buies, Arthur (1875), Chroniques, t. II : Voyages, etc., Québec, C. Darveau (éd. Wikisource)"
C = Corpus('Recherches', 'BU75', BU, page_fmt='{}')
F = C.F
F('01', "Chicago, juin 1874 : Arthur Buies dans « la métropole de l'Ouest »", 'personnage', '1874-06-12~/1874-06-13~', -87.640, 41.879, 'c', ['Arthur Buies'],
  "Parti de Montréal le 10 juin 1874 pour la Californie, après une première tentative abandonnée à Toronto, le chroniqueur québécois Arthur Buies traverse l'Ontario en chemin de fer, passe douze heures à Détroit puis arrive à Chicago. Il y marche toute la journée sans s'y attacher : une ville faite en trente ans, dit-il, qu'on peut admirer mais non aimer. Il y prend son billet pour San Francisco.",
  "« Départ pour la Californie », I-II", "Récit d'un voyageur canadien-français dans l'Ouest américain, dix ans avant Routhier (RT93).")
F('02', "Omaha et les plaines : « les Canadiens n'y ont pas encore pénétré » (juin 1874)", 'personnage', '1874-06~', -95.934, 41.257, 'c', ['Arthur Buies'],
  "Après une journée sur les prairies ondulées de l'Illinois, Buies atteint Omaha, « la plus grande ville de l'Ouest vierge », au tiers du chemin entre Montréal et San Francisco. Il décrit ensuite les villages du chemin de fer de l'Union Pacific (Cheyenne, Laramie, Ogden), peuplés surtout d'Allemands. Il note, avec ironie, que les Canadiens émigrés aux États-Unis n'y sont pas encore allés : ils veulent rester à portée du Canada pour revenir au premier appel du gouvernement. Il juge le trajet du « Grand Pacifique » monotone jusqu'aux hauteurs de la Sierra Nevada.",
  "« Départ pour la Californie », III-IV", "Point à Omaha (Nebraska).")
F('03', "San Francisco, juin 1874 : Buies et le Courrier de San-Francisco", 'personnage', '1874-06-20/1874-06-27~', -122.401, 37.791, 'c', ['Arthur Buies'],
  "Arrivé à San Francisco un samedi soir, malade et sans amis, Buies comptait se placer au Courrier de San-Francisco, le journal français de la ville. Ses lettres de recommandation ne lui servent à rien : un rédacteur lui explique que le journal n'est guère qu'un résumé de nouvelles de France et une feuille d'annonces, soutenu par les Français de la ville et de l'intérieur de la Californie. Buies en tire une réflexion : les Français des villes américaines ne forment pas un groupe national, alors que les Canadiens forment une véritable nationalité. Quelques jours plus tard, il reprend le traversier d'Oakland et le Central Pacific pour rentrer au Canada.",
  "« Départ pour la Californie », deuxième partie", "Le samedi d'arrivée est sans doute le 20 juin 1874 (départ le 10). Point au quartier du port de San Francisco.")
fiches = C.fiches
