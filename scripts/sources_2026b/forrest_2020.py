# Alan Forrest, The Death of the French Atlantic: Trade, War, and Slavery in the Age of Revolution, Oxford, Oxford University
# Press, 2020 (PDF du Drive de l'auteur, dossier FUR_TRADE_USA). Livre atlantique ; un passage sur la Louisiane. Préfixe FO20.
from commun import Corpus
FO = "Forrest, Alan (2020), The Death of the French Atlantic: Trade, War, and Slavery in the Age of Revolution, Oxford, Oxford University Press"
C = Corpus('Recherches', 'FO20', FO, page_fmt='PDF p. {}')
F = C.F
F('01', "La Nouvelle-Orléans, 1809 : les réfugiés de Saint-Domingue chassés de Cuba", 'evenement', '1809', -90.0645, 29.9584, 'c', ['William C. C. Claiborne'],
  "Après la vente de la Louisiane (1803), la colonie peu peuplée devient la seconde destination des familles françaises de Saint-Domingue déjà exilées ailleurs. En 1809, expulsés de Cuba, des milliers de réfugiés, souvent venus de Santiago, affluent à La Nouvelle-Orléans : le gouverneur William Claiborne affrète des navires pour les amener de La Havane et obtient du président qu'ils soient traités en cas particulier, malgré la loi interdisant l'entrée d'esclaves. La ville devient le pivot de la diaspora de Saint-Domingue et la population de langue française s'en trouve renforcée.",
  '238-239', "Point au Vieux Carré.")
fiches = C.fiches
