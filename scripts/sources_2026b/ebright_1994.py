# Malcolm Ebright, Land Grants and Lawsuits in Northern New Mexico (1994), PDF du Drive de l'auteur.
# Corpus « Recherches », préfixe EB94 : les concessions mexicaines démesurées accordées à des francophones.
from commun import Corpus
EB = "Ebright, Malcolm (1994), Land Grants and Lawsuits in Northern New Mexico, Albuquerque, University of New Mexico Press"
C = Corpus('Recherches', 'EB94', EB, page_fmt='p. {}')
F = C.F
F('01', "Concession Beaubien-Miranda (Maxwell) : 1 714 764 acres au lieu de 97 000 (1841-1887)", 'etablissement', '1841/1887', -104.92, 36.51, 'c', ['Charles Beaubien', 'Guadalupe Miranda', 'Lucien Maxwell'],
  "Accordée en 1841 par le gouverneur Armijo au Québécois Charles Beaubien et à Guadalupe Miranda, la concession violait la loi mexicaine de colonisation de 1824, qui limitait chaque bénéficiaire à onze lieues carrées (environ 48 500 acres). Confirmée par le Congrès avant tout arpentage, elle s'avéra couvrir 1 714 764 acres une fois mesurée. La Cour suprême valida pourtant la confirmation en la qualifiant de concession nouvelle (de novo) du Congrès. Pour Ebright, ce cas met en doute tout le processus d'adjudication des terres.",
  '27, 39-40', "Position à Cimarron, siège du domaine Maxwell.")
F('02', "Concession Sangre de Cristo : Beaubien et Lee, l'autre géante confirmée par le Congrès (1843-1860)", 'etablissement', '1843/1860', -105.42, 37.2, 'c', ['Charles Beaubien', 'Stephen Luis Lee', 'Narciso Beaubien'],
  "Autre concession d'Armijo à deux personnes (Narciso Beaubien et Stephen Luis Lee, tous deux tués à Taos en 1847 ; Charles Beaubien hérita de la part de son fils et racheta celle de Lee), la Sangre de Cristo, dans la vallée de San Luis, aurait dû être limitée à environ 96 000 acres. Elle fut confirmée puis patentée à 998 764 acres. Avec la Maxwell, elle fut l'une des toutes premières concessions confirmées par les États-Unis.",
  '27, 39', "Ebright donne aussi 2 713 545 acres p. 39, qui est en fait le total combiné des deux concessions donné p. 27. Position à San Luis (Colorado).")
F('03', "Concession de Las Animas (Vigil et St. Vrain) : réduite par le Congrès à 97 000 acres (1843-1869)", 'etablissement', '1843/1869', -104.0, 37.65, 'a', ['Céran St. Vrain', 'Cornelio Vigil'],
  "Contrairement aux concessions Maxwell et Sangre de Cristo, le Congrès appliqua la limite de la loi de 1824 à la concession de Las Animas, accordée par Armijo à Cornelio Vigil et Céran St. Vrain sur la Purgatoire, et ne la confirma qu'à environ 97 000 acres. Ebright souligne l'injustice d'appliquer la limite des onze lieues carrées à certaines concessions et pas à d'autres.",
  '39', "Position approximative au centre de la concession, entre la Purgatoire et l'Apishapa.")
fiches = C.fiches
