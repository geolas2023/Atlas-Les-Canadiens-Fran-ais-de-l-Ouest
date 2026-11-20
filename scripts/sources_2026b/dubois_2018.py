# S. Dubois, E. Gagnet Leumas et M. Richardson, Speaking French in Louisiana, 1720-1955: Linguistic Practices of the
# Catholic Church, Baton Rouge, LSU Press, 2018 (PDF du Drive de l'auteur, dossier LOUISIANA ; 164 000 caractères
# lisibles, soit l'introduction et les chapitres 1 à 3 environ, lus le 20 nov. 2026). Préfixe DU18.
# Le livre s'appuie sur la correspondance de l'archevêché de La Nouvelle-Orléans (Antebellum Correspondence, 1803-1859).
from commun import Corpus
DU = "Dubois, Sylvie, Emilie Gagnet Leumas et Malcolm Richardson (2018), Speaking French in Louisiana, 1720-1955: Linguistic Practices of the Catholic Church, Baton Rouge, Louisiana State University Press"
C = Corpus('Recherches', 'DU18', DU, page_fmt='p. {}')
F = C.F

F('01', "Avoyelles : le curé Louis Alaux mendie de porte en porte (1835)", 'religion', '1835', -92.07, 31.13, 'a', ['Louis Alaux', 'Antoine Blanc'],
  "En 1835, le père Louis Alaux, curé des Avoyelles, écrit à l'évêque Blanc qu'il doit mendier de porte en porte pour vivre, qu'il est couvert d'insultes, menacé du fouet « comme le dernier des esclaves », vilipendé et calomnié : voilà, dit-il, ce que les paroissiens des Avoyelles infligent au deuxième prêtre qu'on leur envoie. Les auteurs citent sa lettre parmi les témoignages sur la misère des curés de campagne et le peu d'empressement des fidèles dans les années 1830.",
  'chap. 2', "Point à Marksville, chef-lieu de la paroisse des Avoyelles.")
F('02', "Paroisse de l'Assomption : au séminaire, l'anglais devient un « commandement » (1841)", 'religion', '1841', -91.03, 30.0, 'a', ['Armengol (père)', 'Antoine Blanc'],
  "Dès 1839, prêtres et religieuses signalent dans leurs lettres la nouvelle coutume des élèves de parler anglais entre eux. En 1841, le père Armengol écrit en français à Mgr Blanc, de la paroisse de l'Assomption, que tout le monde au séminaire s'efforce de parler anglais depuis qu'il en a fait un commandement après la visite de l'évêque. Blanc, soucieux de former un clergé bilingue, envoie aussi ses prêtres français apprendre l'anglais à Bardstown (Kentucky) ou aux Barrens (Missouri).",
  'chap. 2', "Point approximatif sur le bayou Lafourche ; les auteurs ne nomment pas le séminaire.")
F('03', "Faubourg Lafayette (La Nouvelle-Orléans) : Notre-Dame-de-Bon-Secours, la française, entre l'allemande et l'irlandaise (1854)", 'religion', '1854', -90.075, 29.927, 'a', ['Rulland (père)'],
  "Dans l'ancien faubourg Lafayette, les rédemptoristes desservent trois églises nationales : Saint Mary's Assumption pour les Allemands et Saint Alphonsus pour les Irlandais, face à face de part et d'autre d'une rue étroite, et Notre-Dame-de-Bon-Secours pour les Français, un peu plus loin. En 1854, le père Rulland écrit à son supérieur que les catholiques allemands exigent qu'on ne loue plus de bancs aux Français, à qui ils reprochent d'occuper leur église. Les annales comptent les premières communions par nationalité : les Français y sont toujours moins nombreux que les Allemands et les anglophones.",
  'chap. 2', "Point approximatif près des églises Saint Mary's et Saint Alphonsus (rue Constance).")
F('04', "Carrollton : « il n'y a plus d'autre sermon qu'en anglais » (1859)", 'religion', '1859', -90.125, 29.945, 'a', [],
  "En 1859, des paroissiens de Carrollton, aujourd'hui quartier de La Nouvelle-Orléans, se plaignent à l'archevêché que les derniers dimanches il n'y a eu d'autre sermon qu'en anglais, ce qui indispose les Français et les Allemands, alors que les autres prêtres savent les trois langues. Pour les auteurs, les Louisianais, bilingues dans les affaires, tenaient à la langue du sermon et de la confession.",
  'chap. 2', "Point au quartier de Carrollton.")
fiches = C.fiches
