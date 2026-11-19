# Martin Nollett Jr., Nollette Family History (généalogie familiale dactylographiée, s. d.), PDF du Drive de l'auteur
# (dossier ILLINOIS_MISSISSIPPI_KANKAKEE_JOLIET_MARQUETTE). Corpus « Recherches », préfixe NOL.
from commun import Corpus
NO = "Nollett, Martin, Jr. (s. d.), Nollette Family History, généalogie familiale (PDF du Drive de l'auteur)"
C = Corpus('Recherches', 'NOL', NO, page_fmt='p. {}')
F = C.F
F('01', "L'Érable (comté d'Iroquois, Illinois) : la famille Nollette, de Napierville à la prairie de l'Illinois (1864-1884)", 'migration', '1864/1884-01-10', -87.8900, 40.7300, 'a', ['Hilaire Nollette', 'Marie Mailloux', 'Félix Nollette', 'Noël Le Vasseur', 'John Dutour'],
  "Né à Napierville en 1823, Hilaire Nollette émigre en Illinois en 1864 avec sa femme Marie Mailloux et leurs enfants. Leur fils Félix est baptisé le 14 avril 1866 à l'église Saint-Jean-Baptiste de L'Érable (prononcé « LaRab »), dans le comté d'Iroquois. En 1871, Hilaire achète une terre près de Pittwood, où l'on cultive le maïs les années sèches et chasse le canard les années humides ; il la revend en 1884. La généalogie rappelle aussi que les Dutour (Paul, Victor et John) avaient acheté en 1852 des terres à Noël Le Vasseur, au nord de Bourbonnais.",
  '2-3', "Point placé à L'Érable (comté d'Iroquois).")
F('02', "Comté de Cherry (Nebraska) : la « French Settlement » de Kewanee, fondée par les Nollette et les Dutour (1884-1885)", 'etablissement', '1884-03/1885-06', -100.5500, 42.9500, 'a', ['Hilaire Nollette', 'Louis Tellier', 'Louis Mosier', 'John Soucie', 'John Dutour', 'Isaac Dutour', 'Nicholas Renville', 'David Gibeau'],
  "En mars 1884, Hilaire et Marie Nollette arrivent avec cinq fils dans le comté de Cherry, au Nebraska, après un arrêt près de Stuart. Hilaire dépose sa demande de homestead à Valentine le 15 mai 1884 et la famille s'installe en octobre dans une maison de rondins de 18 pieds sur 24. Leur secteur, au nord-est du comté près de la frontière du Dakota du Sud, devient la French Settlement, dans la communauté de Kewanee, nommée d'après une ville de l'Illinois. Au printemps 1885 les rejoignent les familles Mosier, Soucey, Dutour, Renville et Gibeau, dont plusieurs s'étaient arrêtées à Spencer et Sheldon, en Iowa.",
  '3-4', "Point placé au nord-est du comté de Cherry ; emplacement exact de Kewanee à vérifier.")
F('03', "Guide Rock (Nebraska) : Victor Detour, de Bourbonnais aux plaines par Nebraska City (1869-1912)", 'migration', '1869-03/1912-05', -98.3290, 40.0720, 'c', ['Victor Detour', 'Catherine Boudreau'],
  "Né près de Montréal en 1822, Victor Detour s'établit vers 1848 à Bourbonnais puis à L'Érable. En mars 1869, il part pour Nebraska City et arrive un jour trop tard pour rejoindre un convoi de fret qui sera massacré près de Kearney ; il renonce alors à aller plus loin. En 1872, il gagne avec ses bœufs le comté de Webster, près de Guide Rock, où son fils de dix ans défriche 40 acres. Il y meurt en mai 1912. Sa femme Catherine Boudreau se souvenait d'avoir fui avec sa famille dans la forêt lorsque l'armée brûla leur ferme en 1837.",
  '7')
fiches = C.fiches
