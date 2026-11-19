# Élise Marienstras, La résistance indienne aux États-Unis, XVIe-XXIe siècle, Paris, Gallimard, coll. Folio histoire,
# nouv. éd. 2014 (epub du Drive de l'auteur, pack « Histoire des États-Unis »). Préfixe MR14.
from commun import Corpus
MR = "Marienstras, Élise (2014), La résistance indienne aux États-Unis, XVIe-XXIe siècle, Paris, Gallimard, coll. Folio histoire"
C = Corpus('Recherches', 'MR14', MR, page_fmt='{}')
F = C.F
F('01', "Vallée de la Tuscarawas (Ohio) : la vision du prophète delaware Neolin (hiver 1762)", 'religion', '1762', -81.4400, 40.6600, 'a', ['Neolin'],
  "Au lendemain de la chute de la Nouvelle-France, dans l'hiver 1762, le prophète delaware Neolin a une vision : le Maître de la Vie lui ordonne de renoncer à l'eau-de-vie, de cesser les guerres entre nations et de chasser les Blancs des terres qu'il a faites pour les Indiens. Ce grand réveil religieux, relayé chez les Onondagas puis jusqu'au prophète seneca Handsome Lake, forme avec la guérilla de 1763 le premier mouvement panindien, contre les Anglais qui ont remplacé les Français dans les forts de l'Ohio et des Grands Lacs.",
  "Ch. « Le jeu international », section « Le messianisme »", "Neolin vivait dans les villages delawares de la Tuscarawas ; point approximatif (Bolivar, Ohio), le livre ne situant pas la vision.")
F('02', "Rivière Ecorse, près du Détroit : le conseil de Pontiac des dix-huit nations (5 mai 1763)", 'rencontre', '1763-05-05', -83.1450, 42.2440, 'a', ['Pontiac'],
  "Dès 1761, les Senecas envoient au Détroit un collier de wampum rouge invitant Delawares, Chaouanons, Outaouais, Hurons, Sauteux et Potéouatamis à se joindre aux Six Nations pour chasser les Anglais. Le 5 mai 1763, devant les émissaires de dix-huit nations, le chef outaouais Pontiac expose que l'ennemi est l'Anglais : on ne peut plus être ravitaillé par les Français « comme autrefois », et les Anglais vendent deux fois plus cher des marchandises qui ne valent rien. Les nations unies se donnent un chef religieux et un chef de guerre ; quelques jours plus tard commence le siège du fort.",
  "Ch. « Le jeu international », section « La révolte de Pontiac »", "Point au conseil tenu au village potéouatami de la rivière Ecorse, au sud du Détroit (localisation d'après la tradition historiographique, le livre ne la précise pas). Marienstras rappelle l'initiative seneca, d'après Anthony Wallace.")
fiches = C.fiches
