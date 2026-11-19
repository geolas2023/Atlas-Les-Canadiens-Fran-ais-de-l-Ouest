# Marion Isaacs, The Kankakee River of History (s.d., milieu du XXe siècle), PDF archive.org du Drive de l'auteur
# (dossier Kankakee). Corpus « Recherches », préfixe ISK. Ouvrage de vulgarisation, souvent conjectural.
from commun import Corpus
IS = "Isaacs, Marion (s.d.), The Kankakee River of History, Indiana (archive.org : kankakeeriverofh00isaa)"
C = Corpus('Recherches', 'ISK', IS, page_fmt='p. {} du PDF')
F = C.F
F('01', "Comté de Porter (Indiana) : « Fort Kankakee », enceinte de terre attribuée aux Français (tradition)", 'poste', '1700~/1763', -87.035, 41.265, 'h', [],
  "Selon Isaacs, une enceinte de terre damée d'environ quatre acres, percée de quatorze embrasures et accessible seulement par une levée cachée dans le marais, aurait été élevée sur le Kankakee par les militaires français. Ses restes, réduits à une crête basse, auraient été relevés par un ingénieur local puis visités en 1935 par des chercheurs de Chicago. L'auteur la situe, d'après des « documents Quinaton », dans le canton de Pleasant (comté de Porter), section 22, et la dit abandonnée vers 1763 ; les colons français se seraient alors repliés vers Beaverville et Papineau.",
  '32', "Tradition non confirmée : l'auteur reconnaît que l'histoire du Kankakee relève largement de la conjecture et le même chapitre mêle des théories fantaisistes (Vikings, mineurs de cuivre). Point approximatif près de Kouts.")
fiches = C.fiches
