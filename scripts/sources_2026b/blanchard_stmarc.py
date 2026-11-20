# Dossier HISTOIRE_LIVRES/ELZEAR_BLANCHARD du Drive de l'auteur, relu le 19 novembre 2026 :
# Société d'histoire de Cournoyer, capsule patrimoniale « L'aventure américaine » (225e de Saint-Marc-sur-Richelieu, janv. 2018)
# et Le Cournoyen, vol. 21, n° 4 (juillet 2018), « Les Raynaud-Blanchard de Saint-Marc » (Nicole Lamarre).
# La généalogie d'Elzéar (A-L55, A-L86) était déjà dans l'atlas ; on ajoute les migrants de Saint-Marc. Préfixe BSM.
# L'image d13p_34530105.jpg est une page de registre de Saint-Louis (1840), sans élément nouveau lisible.
from commun import Corpus
S = "Lamarre, Nicole, avec Aurora Loiselle et Lise Blanchard (2018), « L'aventure américaine ; les pionniers et les autres », capsule patrimoniale, Société d'histoire de Cournoyer (225e de Saint-Marc-sur-Richelieu)"
S2 = "Lamarre, Nicole (2018), « Les Raynaud-Blanchard de Saint-Marc », Le Cournoyen, vol. 21, n° 4"
C = Corpus('Recherches', 'BSM', S, page_fmt='p. {}')
F = C.F
F('01', "Oregon : Moyse Loiselle, de Saint-Marc, homme à tout faire du curé Augustin-Magloire Blanchet (vers 1854)", 'migration', '1854', -122.661, 45.626, 'h', ['Moyse Loiselle', 'Augustin-Magloire Blanchet'],
  "Né à Saint-Marc en 1819, fils aîné du capitaine de milice Prudent Loiselle, Moyse refuse à 35 ans de rester fermier chez son père et suit comme employé à tout faire l'abbé Augustin Blanchet, ancien desservant de Saint-Marc et curé de Saint-Charles (1830-1837), lors de sa seconde mission en Oregon. Il quitte ensuite l'Oregon pour accompagner les Sœurs de la Providence à Valparaiso, au Chili, où il épouse une Chilienne et meurt en 1884 sans être revenu au Canada ; sa correspondance avec sa famille de Saint-Marc a été conservée.",
  '1', "La capsule fait de F.-N. Blanchet l'« évêque de Fort Vancouver (Seattle) » : ce sont deux sièges distincts. Point hypothétique à Fort Vancouver.")
F('02', "San Miguel del Vado : Charles Blanchard rejoint son oncle Michel Desmarais après cinq mois de voyage (1864)", 'migration', '1863/1864', -105.444, 35.367, 'c', ['Charles Blanchard', 'Michel Desmarais', 'Frédéric Desmarais', 'Elzéar Blanchard'],
  "En 1863, Charles Blanchard (né à Saint-Marc en 1841), qui a séjourné à Belœil chez son oncle Elzéar Blanchard, prend les « gros chars » pour Saint-Louis et Kansas City avec son cousin Frédéric Desmarais, qui s'établira au Mexique. En 1864, après cinq mois de voyage, il rejoint à San Miguel, au Nouveau-Mexique, son oncle maternel Michel Desmarais, qui y a femme et enfants. Il devient l'homme de confiance et l'associé d'un marchand d'équipement de diligences entre Fort Stanton et Socorro.",
  '1', "Une vingtaine de lettres de Charles (1863-1893) sont conservées par Lise Blanchard. La capsule date l'établissement de Desmarais de 1825, contredit par l'atlas (C071, patriote de 1837) ; « Saint-Louis (Ohio) » corrigé en Saint-Louis.")
F('03', "Las Vegas (Nouveau-Mexique) : les frères Charles, Rodrigue et Napoléon Blanchard, marchands d'outillage agricole (1868-1893)", 'commerce', '1868/1893', -105.218, 35.594, 'c', ['Charles Blanchard', 'Marc-Rodrigue Blanchard', 'Pierre-Napoléon Blanchard', 'Manuel Blanchard'],
  "À Las Vegas, Charles Blanchard monte un commerce d'équipements agricoles et de marchandises de toutes sortes pour les pionniers, que ses frères Rodrigue et Napoléon viennent rejoindre ; ils le mènent de 1868 à 1893 malgré les crises, et Napoléon s'y marie en 1891. Son fils Manuel entre ensuite dans l'affaire. Charles écrit avoir souvent maudit ce pays ; il revient à Saint-Marc à la mort de sa mère en 1878 et envoie une de ses filles passer l'été chez son frère Émile pour apprendre le français. Selon Le Cournoyen, il épouse une Espagnole et meurt en 1914 ; ses frères Pierre-Napoléon (vers 1890) et Joseph-Alfred, forgeron, le rejoignent aux États-Unis.",
  '1-2', "Complète A-L73 (magasin Desmarais puis Blanchard).", source=S + " ; " + S2)
fiches = C.fiches
