# Priscilla Shannon Gutiérrez, « Carlos Beaubien » (Taos County, New Mexico, notice biographique, v. 2007).
# Fichier RTF du Drive de l'auteur (HISTOIRE_LIVRES/CHARLES_BEAUBIEN), relu en entier le 19 novembre 2026.
# Le texte avait déjà nourri les fiches DRV-02, 05, 16-19 ; une seule information restait absente. Préfixe PSG.
from commun import Corpus
S = "Gutiérrez, Priscilla Shannon (v. 2007), « Carlos Beaubien », Taos County, New Mexico (notice biographique en ligne)"
C = Corpus('Recherches', 'PSG', S, page_fmt='{}')
F = C.F
F('01', "Chihuahua : Charles Beaubien, marchand, avec la guía no 23 (1826)", 'evenement', '1826', -106.08, 28.635, 'a', ['Charles Beaubien'],
  "En 1826, Beaubien obtient du gouvernement mexicain l'une des premières guías, la no 23, pour aller commercer à Chihuahua. Sa caravane emporte 2 000 verges de tissu, cinq douzaines de miroirs, des parapluies, des rubans, cent paires de souliers, des boutons, des peignes et de la rassade. L'affaire est profitable : Beaubien, peu porté sur la vie au grand air, commence à se voir en marchand plutôt qu'en trappeur, avant de se fixer à Taos et d'y épouser Pabla Lovato en décembre 1827.",
  '', "Gutiérrez ne cite pas la source de la guía ; Weber (1971) et Grassham (1983) figurent dans sa bibliographie.")
fiches = C.fiches
