# George E. Hyde, Life of George Bent Written from His Letters (éd. Savoie Lottinville, Norman, University of Oklahoma
# Press, 1968), PDF du Drive de l'auteur. Corpus « Recherches », préfixe GB68 : Edmond Guerrier, fils métis de
# William Guerrier, interprète et éclaireur.
from commun import Corpus
GB = "Hyde, George E. (1968), Life of George Bent Written from His Letters, éd. Savoie Lottinville, Norman, University of Oklahoma Press"
C = Corpus('Recherches', 'GB68', GB, page_fmt='p. {}')
F = C.F
EG = 'Edmond Guerrier'
F('01', "Camp cheyenne de la Smoky Hill : Edmond Guerrier et George Bent écrivent la lettre de paix de Black Kettle (fin août 1864)", 'evenement', '1864-08', -101.75, 38.85, 'h', [EG, 'George Bent', 'Julia Bent', 'Black Kettle', 'Edward W. Wynkoop'],
  "Fils du traiteur William Guerrier et d'une Cheyenne, Edmond Guerrier, beau-frère de George Bent (il a épousé Julia Bent), assiste au conseil où les chefs décident de demander la paix et de rendre les captifs blancs. Sous leur dictée, Guerrier et Bent rédigent deux lettres identiques signées « Black Kettle et autres chefs », l'une pour le commandant du fort Lyon, l'autre pour l'agent Colley. Les porteurs, One Eye et Eagle Head, sont d'abord jetés au cachot par le major Wynkoop ; la démarche mène à la rencontre de Camp Weld, puis au camp de Sand Creek.",
  '83, 142', "Position hypothétique du camp, vers les fourches de la Smoky Hill.")
F('02', "Fort Lyon : Edmond Guerrier, rescapé de Sand Creek, se rend aux soldats (hiver 1864-1865)", 'evenement', '1864-12/1865-01', -103.08, 38.08, 'a', [EG, 'George Bent', 'Scott J. Anthony'],
  "Présent au camp de Sand Creek lors du massacre du 29 novembre 1864, Edmond Guerrier évalue les morts à 148, chiffre que les historiens opposent aux 400 à 500 annoncés par Chivington. Avec George Bent, blessé à la hanche, il trouve des chevaux au camp sioux de la Solomon et revient vers l'Arkansas ; en vue du fort Lyon et du ranch de William Bent, découragé, il descend se rendre. Le major Anthony l'interroge sur les camps cheyennes ; Guerrier ne livre rien d'utile et tait la présence de Bent tout près.",
  '159, 164-165')
F('03', "Pawnee Fork : Guerrier, interprète de Hancock face à Roman Nose (avril 1867)", 'evenement', '1867-04-14/1867-04-15', -99.55, 38.22, 'c', [EG, 'Roman Nose', 'Bull Bear', 'Winfield S. Hancock', 'George A. Custer'],
  "Interprète du général Hancock lors de l'approche du grand village cheyenne et sioux de la Pawnee Fork, Edmond Guerrier, ami de Roman Nose et cousin de sa femme, assiste à la confrontation où Bull Bear retient Roman Nose prêt à tuer le général. Envoyé de nuit dans le village pour signaler tout départ, il voit Sioux et Cheyennes s'enfuir ; ses sympathies allant aux Indiens, il ne se presse pas de faire son rapport, et le village est vide quand la cavalerie de Custer l'encercle.",
  '260-261', "Position du village, une trentaine de milles à l'ouest du fort Larned.")
F('04', "Route de la Smoky Hill : Guerrier, éclaireur de Custer, avertit un Cheyenne (avril 1867)", 'evenement', '1867-04', -99.6, 38.95, 'a', [EG, 'George A. Custer', 'Bill Comstock', 'Wild Bill Hickok'],
  "Lancé avec Bill Comstock, Wild Bill Hickok et des éclaireurs delawares sur la piste des fuyards de la Pawnee Fork, au-delà des relais de Lookout et Stormy Hollow, Guerrier chevauche trois milles en avant de la colonne. Apercevant un Cheyenne revenu chercher des poneys, il lui fait signe de fuir, puis rapporte à Custer que les Indiens se sont dispersés. Custer ne les rattrape jamais.",
  '261-262', "Position approximative à l'ouest du fort Hays.")
fiches = C.fiches
