# Jean-Charles Houzeau, La terreur blanche au Texas et mon évasion (Bruxelles, 1862), epub du Drive de l'auteur
# (pack « Histoire des États-Unis »). Corpus « Recherches », préfixe HZ62.
from commun import Corpus
HZ = "Houzeau, Jean-Charles (1862), La terreur blanche au Texas et mon évasion, Bruxelles"
C = Corpus('Recherches', 'HZ62', HZ, page_fmt='{}')
F = C.F
F('01', "San Antonio : le savant belge Jean-Charles Houzeau fuit le Comité de vigilance confédéré (13-14 février 1862)", 'evenement', '1857/1862-02-14', -98.4936, 29.4241, 'c', ['Jean-Charles Houzeau', 'H. Guilbeau', 'Alejandro Vidal'],
  "Établi au Texas depuis 1857, d'où il envoie des mémoires à l'Académie de Belgique et des correspondances sur l'esclavage, le géologue et astronome Jean-Charles Houzeau refuse de servir la Confédération. À San Antonio, il voit lyncher un homme acquitté devant la justice de paix. Il rapporte aussi qu'un émigrant alsacien a été assommé et pendu par des soldats, malgré les protestations énergiques de l'agent consulaire français H. Guilbeau. Averti le 13 février 1862 que le Comité de vigilance va venir chez lui, il se fait engager le lendemain comme charretier dans un convoi mexicain de balles de coton, parti de Calaveras.",
  'chap. II-III')
F('02', "Matamoros : Houzeau arrive au Mexique après 35 jours de route en charretier (avril 1862)", 'migration', '1862-02-16/1862-04-12', -97.5040, 25.8697, 'c', ['Jean-Charles Houzeau'],
  "Conduisant six bœufs dans le convoi d'Alejandro Vidal, Houzeau descend vers Brownsville, croise des troupes confédérées qui l'interrogent et atteint Matamoros après trente-cinq journées de marche. Le 12 avril 1862, il y écrit ses lettres au journaliste Van Bemmel. Il y rapporte aussi que le planteur d'origine française Trasimon Landry, au Texas, espérait la réouverture de la traite. Houzeau dirigera plus tard le quotidien bilingue La Tribune de la Nouvelle-Orléans, puis l'Observatoire royal de Belgique.",
  'chap. III et notice')
fiches = C.fiches
