# Francis J. Yealy, s.j., Sainte Genevieve: The Story of Missouri's Oldest Settlement, Sainte-Geneviève, Bicentennial
# Historical Committee, 1935 (PDF du Drive de l'auteur, dossier SAINTE_GENEVIEVE_OLD_MINES_HISTORY ; texte lu jusqu'au ch. VI). Préfixe YE35.
from commun import Corpus
YE = "Yealy, Francis J. (1935), Sainte Genevieve: The Story of Missouri's Oldest Settlement, Sainte-Geneviève (Missouri), Bicentennial Historical Committee"
C = Corpus('Recherches', 'YE35', YE, page_fmt='{}')
F = C.F
F('01', "Le Grand Champ : la paroisse Saint-Joachim, premier nom de Sainte-Geneviève (1732)", 'etablissement', '1732', -90.035, 37.965, 'a', ['Jean-Paul Mercier', 'Louis Poulin'],
  "La tradition fixait la fondation de Sainte-Geneviève à 1735 ; deux cartes de 1755 et le mémoire du père Watrin suggéraient plutôt 1749-1752. Yealy retient une date plus ancienne : le 25 mai 1732, le père Mercier, supérieur de la mission de Cahokia, écrit au Séminaire de Québec qu'il a confié des papiers à « un certain Louis Poulin, de la paroisse Saint-Joachim ». Le premier village, au bord du fleuve face à Kaskaskia, s'appelait donc déjà Saint-Joachim ; en 1881, on y retrouva une margelle de puits gravée « 1732 ». Les mineurs qui, après la faillite de la Compagnie de Law (1720), portaient leur plomb au fleuve en furent sans doute les premiers habitants.",
  "ch. III, p. 21-28", "Point sur l'ancien site du Grand Champ, au sud de la ville actuelle ; le village a été emporté par le fleuve.")
F('02', "Sainte-Geneviève : le premier registre paroissial s'ouvre sur le mariage d'André de Guire dit La Rose (26 février 1759)", 'religion', '1759-02-26', -90.035, 37.965, 'c', ['André de Guire dit La Rose', 'Marie La Boissière', 'Jean-Baptiste de Guire dit La Rose'],
  "Les registres de Sainte-Geneviève commencent le 26 février 1759 par le mariage d'André de Guire dit La Rose et de Marie La Boissière, veuve de Joseph Baron. En 1825, le vieil habitant Julien Labruyère témoignera qu'un Baptiste La Rose, très âgé, avait été le premier colon du vieux village ; Yealy identifie deux Jean-Baptiste de Guire dit La Rose, l'un mort en 1773, l'autre, natif de Montréal, mort en 1781. La plus ancienne pièce connue du village est une vente de terrain de décembre 1754, de Laurent Gabourie à Jean-Baptiste Saint-Gemme Beauvais.",
  "ch. III, p. 28-31", "Point sur le site du vieux village.")
F('03', "Les Grandes Eaux de 1785 : Sainte-Geneviève monte aux Petites Côtes", 'evenement', '1785-04~/1794', -90.0498, 37.9806, 'c', ['François Vallé'],
  "Vers 1784, le fleuve ronge la berge du vieux village ; au printemps 1785, les « Grandes Eaux » submergent le village et ses terres de douze à quinze pieds. Les habitants rebâtissent sur les hauteurs, aux Petites Côtes, où presque toutes les maisons sont transportées dès 1787 ; le vieux site n'est abandonné qu'en 1791 et l'église, démontée, n'est remontée dans le nouveau village que trois ans plus tard. Le lieutenant-gouverneur Zenon Trudeau écrira en 1798 que les inondations tourmentaient le vieux village depuis plus de soixante ans.",
  "ch. III et VI", "Point au centre historique actuel de Sainte-Geneviève.")
fiches = C.fiches
