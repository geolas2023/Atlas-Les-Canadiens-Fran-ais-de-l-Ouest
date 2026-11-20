# David Dary, The Santa Fe Trail. Its History, Legends, and Lore (New York, Knopf, 2000), PDF du Drive lu en entier
# via le visualiseur (392 pages). Corpus « Recherches », préfixe DY00. La plupart des épisodes français du livre
# (Mallet, Vial, LaLande, Clamorgan, Philibert, Chouteau-De Mun, Saint-Vrain, Aubry, Lamy, Maxwell) sont déjà dans
# l'atlas ; ne sont retenus ici que les deux points absents.
from commun import Corpus
DY = "Dary, David (2000), The Santa Fe Trail. Its History, Legends, and Lore, New York, Alfred A. Knopf"
C = Corpus('Recherches', 'DY00', DY, page_fmt='p. {} (PDF)')
F = C.F
fiches = C.fiches

F('01', "Rivière Canadienne (enclave du Texas) : un nommé Pratte, premier tué de l'attaque contre la caravane de J. H. Carr (1er janvier 1833)", 'evenement', '1833-01-01/1833-01-02', -102.5, 35.6, 'h',
  ['Pratte', 'J. H. Carr', 'Mitchell'],
  "Le 1er janvier 1833, une douzaine de traiteurs, apparemment menés par J. H. Carr, reviennent de Santa Fe vers le Missouri avec un convoi de mules et plus de dix mille dollars en or et en argent. À environ 200 milles au nord-est de Santa Fe, près de la rivière Canadienne, des Indiens, probablement des Kiowas, les attaquent. Selon le Missouri Republican du 3 mars 1833, cité par Dary, un homme nommé Pratte est tué le premier, alors qu'il tente de rattraper une mule loin du camp ; un nommé Mitchell est tué ensuite. Retranchés, les traiteurs tiennent un jour et demi, jusqu'à ce que les assaillants les laissent partir. Toutes les mules ayant été tuées, ils abandonnent l'or et marchent vers l'est : cinq atteignent le Missouri, trois un établissement creek, et deux disparaissent. La nouvelle de l'attaque pousse le Congrès à créer en mars 1833 un régiment de « rangers » montés, qui escorte la caravane du printemps.",
  '153-154', "Dary ne donne pas le prénom de Pratte ni son lien éventuel avec la famille Pratte de Saint-Louis. Point placé approximativement sur la rivière Canadienne, dans l'enclave du Texas.")
F('02', "Chihuahua : « deux respectables dames françaises » venues par la piste de Santa Fe, selon Josiah Gregg (vers 1831-1844)", 'personne', '1831/1844', -106.07, 28.635, 'a',
  ['Josiah Gregg'],
  "Racontant son départ de 1831 avec la caravane de Charles Bent, où voyageait une famille espagnole bannie en 1829 qui rentrait au Mexique, Josiah Gregg note dans Commerce of the Prairies (1844) que d'autres femmes ont traversé les prairies jusqu'à Santa Fe à diverses époques. Il dit avoir connu parmi elles deux respectables dames françaises, qui résident alors (en 1844) à Chihuahua. Dary cite ce passage parmi les rares mentions de voyageuses sur la piste.",
  '144-145', "Gregg ne nomme pas ces deux femmes. Point placé à Chihuahua, leur lieu de résidence en 1844.")
