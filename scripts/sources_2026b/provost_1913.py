# Missouri State Board of Health, certificat de décès n° 27938 (Saint-Louis, 8 août 1913) de Mary Rose Pillsbury,
# PDF du Drive de l'auteur (dossier Provost / Saint-Louis). Corpus « Recherches », préfixe PV13.
from commun import Corpus
DC = "Missouri State Board of Health, Bureau of Vital Statistics, certificat de décès n° 27938 (enregistré n° 7234), Mary Rose Pillsbury, Saint-Louis, 8 août 1913"
C = Corpus('Recherches', 'PV13', DC, page_fmt='p. {}')
F = C.F
F('01', "Saint-Louis : mort de Mary Rose Pillsbury, « fille d'Étienne Provo » (8 août 1913)", 'famille', '1830-05-01/1913-08-11', -90.2585, 38.5845, 'h', ['Mary Rose Pillsbury', 'Étienne Provost', 'Madeleine Delor'],
  "Le certificat de décès de Mary Rose Pillsbury, veuve, morte à 83 ans au 4231 South 37th Street et inhumée au cimetière Calvary le 11 août 1913, la dit née à Saint-Louis le 1er mai 1830, fille d'« Etienne Provo », né au Canada, et de « Madelin Delor », née à Saint-Louis. La date de naissance tombe un an après le mariage d'Étienne Provost (1829) ; s'il s'agit bien de sa fille, ce serait l'une des rares traces de sa descendance. Le nom de la mère ne correspond toutefois à aucune des formes connues de l'épouse (Salle dit Lajoie, Lambert, Lombard) : Delor évoque plutôt la famille de Clément Delor de Tréget, fondateur de Carondelet.",
  '', "Déclarant : Charles G. Grimm, même adresse. Filiation à vérifier dans les registres de baptême de la vieille cathédrale (mai 1830).")
fiches = C.fiches
