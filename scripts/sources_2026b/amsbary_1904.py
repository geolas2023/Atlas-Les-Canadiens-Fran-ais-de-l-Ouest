# Wallace Bruce Amsbary, Ballads of Bourbonnais, Indianapolis, Bobbs-Merrill, 1904, PDF archive.org du Drive de l'auteur
# (dossier Kankakee). Corpus « Recherches », préfixe AM04.
from commun import Corpus
AM = "Amsbary, Wallace Bruce (1904), Ballads of Bourbonnais, Indianapolis, Bobbs-Merrill"
C = Corpus('Recherches', 'AM04', AM, page_fmt='p. {}')
F = C.F
F('01', "Bourbonnais (Illinois) : la colonie canadienne du Kankakee mise en ballades (1904)", 'migration', '1904', -87.879, 41.150, 'c', ['Charles Chiniquy'],
  "En introduction à ses poèmes en anglais imitant le parler des Canadiens français de l'Illinois, Amsbary résume l'histoire de la colonie : traders et voyageurs du Bas-Canada achètent des terres avant 1835, la mission catholique naît à Bourbonnais Grove, puis Chiniquy attire au début des années 1850 un grand nombre de colons et fonde Sainte-Anne. Il évalue la colonie à environ sept mille personnes ; Bourbonnais, avec ses quelque cinq cents habitants, compterait alors le collège Saint-Viateur et le couvent Sainte-Catherine, et Momence, Saint-George, Sainte-Marie, Manteno, Papineau, L'Érable et Kankakee auraient une bonne part de Français. Les ballades mettent en scène des noms de la région (Legris, Contois, Boudreau, Frochette) et le fils d'un colon venu avec Chiniquy, capitaine d'un vapeur sur le Kankakee.",
  '15-16, 93', "Source littéraire : les ballades sont des fictions en dialecte ; seuls les chiffres de l'introduction sont repris, tels que donnés par l'auteur.")
fiches = C.fiches
