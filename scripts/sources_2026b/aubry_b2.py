# Lot aubry_b2 : huit gros livres du dossier Drive FRANCOIS_XAVIER_AUBRY (21 nov. 2026).
# Tous dépassent 10 Mo : texte obtenu par read_file_content (Drive), qui n'en rend que le début.
# Parts lues : Calhoun, p. 1-46 de la correspondance (68 premières pages du PDF) ; Cooke et al. (éd. Bieber),
# introduction et journal de Cooke jusqu'à la p. 75 ; NMHR IX, no 1 (janv. 1934), p. 1-58 ; NMHR VII, no 1,
# p. 1-64 (article de Wyman sur Aubry, p. 1-31, en entier) ; Sherman, t. I, p. 1-68 ; Chapman, p. 1-70 ;
# Twitchell, t. I, p. 1-152 ; Twitchell, t. II : aucune couche texte rendue.
# Les propositions pour l'Atlas Aubry sont dans aubry_b2.md (pas de module, selon les consignes).
# Pages : pagination imprimée. Préfixe FXC.
from commun import Corpus

COOKE = "Bieber, Ralph P. (éd.), avec Averam B. Bender, Exploring Southwestern Trails, 1846-1854, by Philip St. George Cooke, William Henry Chase Whiting, Francois Xavier Aubry, Glendale, Arthur H. Clark, 1938 (réimpr. Philadelphie, Porcupine Press, 1974) (PDF, Drive de l'auteur, dossier FRANCOIS_XAVIER_AUBRY/01_LIVRES)"
CALHOUN = "Abel, Annie Heloise (éd.), The Official Correspondence of James S. Calhoun while Indian Agent at Santa Fé and Superintendent of Indian Affairs in New Mexico, Washington, Government Printing Office, 1915 (PDF, Drive de l'auteur, dossier FRANCOIS_XAVIER_AUBRY/01_LIVRES)"
NMHR9 = "Bender, A. B., « Government Explorations in the Territory of New Mexico, 1846-1859 », New Mexico Historical Review, vol. IX, no 1, janvier 1934 (PDF, Drive de l'auteur)"

C = Corpus('Recherches', 'FXC', COOKE); F = C.F

F('01', "Ranchos d'Albuquerque : Charbonneau, guide laissé par Kearny au bataillon mormon (octobre 1846)", 'exploration', '1846-10-18/1846-10-24', -106.643, 35.162, 'a',
  ['Charbonneau', 'Philip St. George Cooke', 'Stephen W. Kearny', 'Henry S. Turner', 'Antoine Leroux'],
  "Le 15 octobre 1846, en quittant le Rio Grande pour la Gila, le général Kearny détache plusieurs guides chargés de reconnaître, plus au sud, une route praticable aux chariots du bataillon mormon de Cooke. Le 18 octobre, aux mines de cuivre (Copper Mines), le capitaine Henry S. Turner écrit à Cooke que le chef apache Red Sleeve promet de lui envoyer des jeunes gens comme guides ; aucun ne parlant espagnol, il est probable, ajoute-t-il, que « Charbonneaux » saura les comprendre et se faire comprendre d'eux par signes. Le 24 octobre, aux ranchs d'Albuquerque, où il échange ses trois plus mauvaises mules, Cooke rencontre Charbonneau, l'un des guides laissés pour lui. Celui-ci rapporte avoir examiné une route en partie différente de celle du général, plus longue, qui descend davantage le fleuve pour rejoindre le chemin d'El Paso aux mines de cuivre ; Cooke juge le rapport favorable, mais l'examen insuffisant. Cooke appelle ailleurs Charbonneau un « guide métis ». Des autres guides arrivés le 2 novembre, seul Antoine Leroux n'était pas plus ou moins ivre, selon Cooke.",
  '26-28, 74-75',
  "Bieber (p. 75, n. 149, d'après Stella M. Drumm, 1938) voit en lui « probablement » un fils de Toussaint Charbonneau, l'interprète de Lewis et Clark ; l'identification n'est pas certaine. Complète F-charbonneau-21 et ZB-charbonneaux-riviere-sa (guide de Cooke de Santa Fe à San Diego), qui ne mentionnent ni la rencontre d'Albuquerque ni la lettre de Turner. Point approximatif à Los Ranchos de Albuquerque.")

F('02', "Santa Fe : Céran St. Vrain juge la situation la pire depuis son arrivée (5 octobre 1849)", 'personnage', '1849-10-05', -105.9384, 35.6874, 'a',
  ['Céran St. Vrain', 'James S. Calhoun', 'William W. Bent', 'Hugh N. Smith'],
  "Le 5 octobre 1849, l'agent indien James S. Calhoun écrit de Santa Fe au commissaire Medill que les rumeurs de troubles s'aggravent : un Mexicain vient d'être tué de dix-huit flèches à trois milles de la ville, et des Indiens d'Ildefonso et de Santo Domingo signalent des Navajos dans tous les coins du pays. Il ajoute que l'un des propriétaires de Bent's Fort a retiré tous ses biens du fort et l'a fait brûler. « M. St. Vrain », établi depuis longtemps dans le pays, digne de toute confiance et intelligent, lui dit que jamais la situation n'a été aussi mauvaise depuis qu'il y habite. Folger et d'autres le confirment, dont Hugh N. Smith, délégué d'une convention réunie à Santa Fe le 24 septembre. L'éditrice identifie le témoin comme Céran St. Vrain, et le propriétaire de Bent's Fort comme William W. Bent.",
  '41-42',
  "Les identifications sont celles des notes d'Annie H. Abel (p. 42, n. 1 et 3). Les origines créoles françaises de St. Vrain relèvent du contexte connu et ne sont pas dites par la source. L'atlas a plusieurs fiches St. Vrain à Santa Fe (MM-H5-297-0846, WJ-st-vrain-ceran-santa-fe), aucune sur ce témoignage de 1849. Point approximatif à Santa Fe.",
  source=CALHOUN)

F('03', "Las Vegas (Nouveau-Mexique) : P. M. Papin dans la reconnaissance du Pecos du capitaine Judd (mars 1850)", 'exploration', '1850-03-15/1850-04', -105.2239, 35.5939, 'h',
  ['P. M. Papin', 'Henry B. Judd', 'R. H. Kern', 'Ambrose E. Burnside', 'J. H. Dickerson', 'Estephan Corunna'],
  "Au printemps 1850, le capitaine Henry B. Judd, du 3e d'artillerie, mène le long du Pecos une reconnaissance destinée à choisir le site d'un poste militaire. Le 15 mars, il quitte Las Vegas avec la compagnie légère C, montée en cavalerie. L'accompagnent les lieutenants J. H. Dickerson et Ambrose E. Burnside, le topographe R. H. Kern et P. M. Papin ; le guide est Estephan Corunna, un Mexicain qui avait été prisonnier des Comanches. Partie d'Anton Chico avec cinq chariots, l'expédition suit un temps la piste des chasseurs de bisons et des marchands qui commercent avec les Comanches, gagne le Bosque Redondo puis le Bosque Grande, à environ 200 milles de Las Vegas.",
  '12-13',
  "Bender ne dit rien de plus de P. M. Papin, ni son rôle ni son origine ; le rattachement à la famille créole Papin de Saint-Louis n'est qu'une hypothèse fondée sur le nom. Il ne peut s'agir de Pierre-Mellicourt Papin, mort en 1849 selon BL88-10. Fiche fragile, à confirmer par le rapport de Judd. Point hypothétique à Las Vegas, lieu du départ.",
  source=NMHR9)

fiches = C.fiches

autoch = [dict(id='A-FXC-01', src='FXC-01', nom="Mines de cuivre de Santa Rita : Apaches — Red Sleeve promet des guides au bataillon de Cooke (18 octobre 1846)",
  theme='rencontre', date='1846-10-18', lon=-108.07, lat=32.8, cert='a',
  nations=['Apaches'], aires=['Sud-Ouest'], francophones=['Charbonneau'],
  description="Le 18 octobre 1846, aux mines de cuivre, le chef apache Red Sleeve s'entretient avec le général Kearny et promet d'envoyer certains de ses jeunes gens conduire le bataillon mormon de Cooke, par une bonne route, jusqu'à la Gila. Ces guides doivent porter eux-mêmes à Cooke la lettre du capitaine Turner, qui demande de bien les traiter. Comme aucun d'eux ne parle espagnol, Turner compte sur le guide Charbonneaux pour communiquer avec eux par signes. Ce sont les dernières instructions que Cooke reçoit de Kearny avant la Californie.",
  note="Bieber, Exploring Southwestern Trails, p. 26-27 (lettre de Turner à Cooke, 18 oct. 1846). Complète la fiche autochtone existante L-arizona-fa-mine-de-cuivre-de-santa-rita-nouveau-mex (Red Sleeve venu au-devant de Kearny), qui ne mentionne pas les guides. Point aux mines de Santa Rita, comme la fiche existante.")]
