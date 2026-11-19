# N.-E. Dionne, Chouart et Radisson : odyssée de deux Canadiens-français au XVIIe siècle, Québec, Laflamme et Proulx,
# 1910 (Galerie historique). PDF du Drive de l'auteur (dossier Radisson). Corpus « Recherches », préfixe DN10.
from commun import Corpus
DN = "Dionne, N.-E. (1910), Chouart et Radisson : odyssée de deux Canadiens-français au XVIIe siècle, Québec, Laflamme et Proulx"
C = Corpus('Recherches', 'DN10', DN, page_fmt='p. {}')
F = C.F
F('01', "Baie de Chagouamigon : le petit fort triangulaire de Chouart et Radisson, premier poste du lac Supérieur", 'poste', '1659~/1662~', -90.830, 46.660, 'a', ['Médard Chouart des Groseilliers', 'Pierre-Esprit Radisson'],
  "Longeant la rive sud du lac Supérieur, les deux voyageurs passent la baie de Keweenaw (leur baie de la Trinité) et la rivière Montréal, puis une longue pointe de terre étroite ; au-delà, dans une baie où des Outaouais réfugiés vivent depuis deux ans sur une pointe et les îles voisines, ils élèvent un petit fort de bois triangulaire, entouré d'une palissade de branches. Dionne y voit le premier poste de commerce attesté sur les rives du lac Supérieur. Ils le quittent douze jours plus tard pour gagner le village des Hurons réfugiés, avant d'hiverner dans les terres et de visiter les Nadouessioux.",
  '64-68', "Chronologie discutée : Dionne date ce voyage d'après les Relations et le récit de Radisson, et une note le fait hiverner dans la région en 1661-1662 ; on le place plus souvent en 1659-1660. Point près de Houghton Point (Ashland, Wisconsin), localisation traditionnelle du fort.")
fiches = C.fiches
