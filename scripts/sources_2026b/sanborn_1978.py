# Margaret Sanborn, The Grand Tetons. The Story of the Men Who Tamed the Western Wilderness (New York, Putnam, 1978),
# PDF du Drive, lu en entier via le visualiseur. Corpus « Recherches », préfixe SB78 : les Canadiens français autour
# de Jackson Hole et des rendez-vous (Godin, Charbonneau et les Trois Tétons sont déjà couverts ailleurs).
from commun import Corpus
SB = "Sanborn, Margaret (1978), The Grand Tetons. The Story of the Men Who Tamed the Western Wilderness, New York, G. P. Putnam's Sons"
C = Corpus('Recherches', 'SB78', SB, page_fmt='p. {}')
F = C.F
fiches = C.fiches

F('01', "Rendez-vous des Rocheuses : Antoine Clément, chasseur métis canadien-français de William Drummond Stewart pendant six saisons (vers 1833-1838)", 'personne', '1833/1838', -110.1, 42.9, 'a',
  ['Antoine Clément', 'William Drummond Stewart', 'Alfred Jacob Miller'],
  "Selon Sanborn, Antoine Clément, homme des montagnes qu'elle qualifie de « French-Canadian half-breed », est pendant six saisons le compagnon de chasse de l'Écossais William Drummond Stewart, qui fréquente chaque été les rendez-vous de la traite des fourrures. Le rendez-vous de 1838 est le dernier de Stewart : à son retour à Saint-Louis, il apprend la mort de son frère et doit rentrer en Écosse recueillir ses titres. Au printemps 1839, alors que Clément se trouve à Saint-Louis, Stewart écrit de La Nouvelle-Orléans à William Sublette pour qu'Antoine lui trouve des calebasses propres à faire des louches et des bouteilles, et des cardinaux à garder en cage pour les emporter en Angleterre.",
  '140-141', "Point placé dans la vallée de la Green River, lieu habituel des rendez-vous de ces années ; Sanborn ne localise pas les saisons de chasse de Clément.")
F('02', "Saint-Louis : Antoine Clément part pour l'Écosse avec Stewart et devient valet au château de Murthly (1839-1842)", 'personne', '1839-05/1842-08', -90.19, 38.627, 'a',
  ['Antoine Clément', 'William Drummond Stewart', 'Alfred Jacob Miller'],
  "Fin mai 1839, Stewart s'embarque pour l'Écosse avec dix-huit tableaux de Miller, deux Indiens (sans doute des Shoshones) et Antoine Clément. À Murthly, il recrée un coin d'Ouest américain : il fait venir de jeunes cerfs, des bisons et des graines de plantes indigènes, et dort sur des robes de bison étendues sur un divan. Arrivé en septembre 1840 comme artiste en résidence, Alfred Jacob Miller trouve Clément « metamorphosed into a Scotch valet » : les peaux de daim graisseuses ont fait place à un habit noir complet, et sa seule tâche est de servir à table. Clément, Stewart et les deux Indiens ne repartent pour l'Amérique qu'en août 1842.",
  '141-142', "Point placé à Saint-Louis, où se trouve Clément avant le départ de 1839 ; le séjour lui-même se passe au château de Murthly, dans le Perthshire, hors du cadre de la carte.")
F('03', "Saint-Louis : Antoine Clément, « de retour dans son élément », chasseur de l'expédition de plaisance de Stewart vers les Rocheuses (avril 1843)", 'evenement', '1843-04', -90.19, 38.627, 'c',
  ['Antoine Clément', 'William Drummond Stewart', 'William Sublette', 'Jean-Baptiste Charbonneau', 'William Clark Kennerly', 'Jefferson Kennerly Clark'],
  "Après un hiver à La Nouvelle-Orléans, où il écrit son roman Altowan, Stewart organise un dernier voyage sentimental vers le Wyoming. La troupe qui se réunit à Saint-Louis en avril 1843 compte environ quatre-vingts personnes, sous la conduite de William Sublette. Elle comprend des fils de grandes familles de la ville (un Clark, un Kennerly, un Chouteau), deux lieutenants de l'armée, Baptiste Charbonneau, fils de Sacagawea, de vieux hommes des montagnes avec leurs femmes indiennes, et le chasseur Antoine Clément, que Sanborn dit « back in his element ».",
  '142-143')
F('04', "Rendez-vous de la traite : le duel de Kit Carson contre Shunar, « ce bravache français » (années 1830)", 'evenement', '1835', -111.17, 43.73, 'h',
  ['Shunar', 'Kit Carson'],
  "Sanborn raconte le duel dans sa description des rendez-vous de Pierre's Hole. La rivalité pour une même jeune femme en serait la cause. Ivre, Shunar, que Carson appelle « le grand bravache des montagnes », va à cheval de camp en camp, fusil chargé, défier tout Français, Américain, Espagnol ou Hollandais en combat singulier. Carson accepte et galope à sa rencontre, pistolet en main. Les chevaux se touchent, et les deux hommes tirent au même instant : la balle de Carson traverse le bras de Shunar, celle de Shunar effleure les cheveux de Carson et lui brûle l'œil de poudre. Selon la tradition, Carson va chercher un autre pistolet et tue Shunar ; lui-même écrit seulement qu'on n'eut plus d'ennuis avec « ce bravache français » pendant le reste du séjour.",
  '106', "Sanborn ne date ni ne localise précisément le duel ; elle le place dans son tableau général des rendez-vous de Pierre's Hole, où le point est posé. D'autres sources le situent au rendez-vous de 1835 sur la Green River.")
