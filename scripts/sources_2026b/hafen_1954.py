# LeRoy R. Hafen, « When Was Bent's Fort Built? », The Colorado Magazine, vol. 31, n° 2 (avril 1954), p. 105-119
# (PDF du Drive de l'auteur, dossier PROJET). Corpus « Recherches », préfixe HF54.
from commun import Corpus
HF = "Hafen, LeRoy R. (1954), « When Was Bent's Fort Built? », The Colorado Magazine, vol. 31, n° 2, p. 105-119"
C = Corpus('Recherches', 'HF54', HF, page_fmt='p. {}')
F = C.F
F('01', "Taos : Céran St. Vrain espère fournir « Provoe & Leclere » (21 avril 1824)", 'commerce', '1824-03/1824-04-21', -105.5745, 36.4075, 'c', ['Céran St. Vrain', 'Étienne Provost', 'François Leclerc', 'Bernard Pratte'],
  "Parti du Missouri à l'automne 1823, Céran St. Vrain arrive à Taos en mars 1824 après cinq mois d'un voyage d'hiver. Le 21 avril, il écrit à Bernard Pratte, qui l'a sans doute équipé, que les affaires sont mauvaises, mais qu'il compte vendre ses marchandises à « Provoe & Leclere », Étienne Provost et son associé François Leclerc, à leur retour de chasse, ou à défaut acheter des mules au Sonora. En février 1825, il équipe à Taos Thomas « Pegleg » Smith et neuf hommes pour la San Juan et le Colorado.",
  '107-108', "Lettre publiée par Dale L. Morgan, Provo, Pioneer Mormon City (1942), p. 24-25.")
F('02', "Fort Bent : bâti en 1833, et non en 1826 ou 1828", 'poste', '1833', -103.4295, 38.0408, 'c', ['Céran St. Vrain', 'Charles Bent', 'William Bent'],
  "Contre une tradition reprise par Grinnell et George Bent, qui place sur l'Arkansas une palissade des Bent et de St. Vrain dès 1826, Hafen montre que Charles et William Bent n'arrivent dans la région qu'en 1829 et que l'association avec Céran St. Vrain ne se noue qu'à Santa Fe, le 6 janvier 1831. Les rares sources contemporaines (Matt Field en 1839, William Waldo, la correspondance de l'Upper Missouri Outfit) indiquent que le fort William, ou fort Bent, fut construit à l'été 1833.",
  '105-119')
fiches = C.fiches
