# Charles Chiniquy, Lettre du père Chiniquy à M. Brassard, Montréal, bureau de L'Avenir, 1857
# (microfiche ICMH, PDF du Drive de l'auteur, dossier CHINIQUY). Corpus « Recherches », préfixe CQ57.
from commun import Corpus
CQ = "Chiniquy, Charles (1857), Lettre du père Chiniquy à M. Brassard, Montréal, en vente au bureau de L'Avenir (microfiche ICMH)"
C = Corpus('Recherches', 'CQ57', CQ, page_fmt='p. {}')
F = C.F
F('01', "Sainte-Anne (Illinois) : Chiniquy accuse l'abbé Desaulniers de trahison (lettre du 22 avril 1857)", 'religion', '1856-11-26/1857-04-22', -87.714, 41.025, 'c', ['Charles Chiniquy', 'Louis-Moïse Brassard', 'Isaac Desaulniers', "Anthony O'Regan"],
  "De Sainte-Anne, comté de Kankakee, Chiniquy répond à l'abbé Brassard, venu du Canada avec l'abbé Desaulniers pour régler le conflit avec l'évêque de Chicago. Il rappelle que Desaulniers avait fait signer au curé et à la paroisse un acte de soumission, le 26 novembre, en promettant que l'évêque lèverait la censure, sinon qu'il plaiderait leur cause à Saint-Louis et jusqu'à Rome ; il l'accuse de tout nier depuis. Chiniquy conteste la validité de son excommunication, cite Brassard comme son seul témoin devant le Canada et publie la lettre à Montréal, au bureau du journal libéral L'Avenir.",
  '3-6', "La date imprimée se lit « 1851 » sur la microfiche, mais l'acte de soumission de novembre 1856 et la publication de 1857 indiquent 1857.")
F('02', "Chicago : l'évêque O'Regan retire leur église aux Français et aux Canadiens (vers 1856)", 'religion', '1856~', -87.632, 41.884, 'a', ["Anthony O'Regan", 'Charles Chiniquy'],
  "Dans la même lettre, Chiniquy dénonce l'évêque Anthony O'Regan qui, interrogé par les Français et les Canadiens de Chicago sur son droit de leur ôter leur église pour la donner à une autre congrégation, les aurait mis brutalement à la porte en affirmant qu'il pouvait la vendre.",
  '9', "Témoignage polémique de Chiniquy ; il s'agit de l'église Saint-Louis des Français de Chicago.")
fiches = C.fiches
