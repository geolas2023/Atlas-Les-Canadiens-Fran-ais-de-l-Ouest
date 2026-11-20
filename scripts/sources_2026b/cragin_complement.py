# Cragin, Early Far West Notebooks : contrôle de la couverture le 19 nov. 2026 (soir).
# Les 333 pages du PDF du Drive (dossier HISTOIRE_LIVRES/CRAGIN_NOTES) ont été extraites par la visionneuse ;
# tous les noms à consonance française ont été comparés aux 207 fiches Cragin déjà dans l'atlas (C001-C183, F, R).
# Seuls trois passages manquaient. Préfixe CRG.
from commun import Corpus
S = "Cragin, Francis Whittemore, Early Far West Notebooks (1902-1923), Starsmore Center for Local History, Colorado Springs Pioneers Museum ; transcription dactylographiée (Mrs. Shaw), PDF « Cragin notebooks searchable »"
C = Corpus('Cragin', 'CRG', S, page_fmt='p. {}')
F = C.F
F('01', "Rivière Las Animas, en aval de Trinidad : Ramon et Bridger Girard, élevés près de la famille Leroux à Saint-Louis", 'famille', '1840/1908', -104.450, 37.200, 'a', ['Ramon Girard', 'Bridger Girard', 'Antoine Leroux'],
  "Selon Mme Thomas Wallace (née Ida Chene), petite-fille d'Antoine Leroux, Ramon Girard, qui a un ranch sur la rivière Las Animas en aval de Trinidad, a été élevé à Saint-Louis près de la famille Leroux et la connaissait bien ; son frère Bridger Girard vivait aussi près de Trinidad et était déjà mort en 1908. Leroux disait à ses petits-enfants que son père, Louis-Guillaume Leroux, était né en France et avait grandi à Saint-Louis.",
  '115', "Entretien de juin 1908. Point approximatif sur la Purgatoire (Las Animas) en aval de Trinidad.")
F('02', "Clear Creek et rivière Green : DuShay, enterré chez Jim Baker, Baptiste « Lusanne » et Louie DuFrain", 'personne', '1855/1870', -105.040, 39.810, 'a', ['DuShay', 'Baptiste Lusanne', 'Louie DuFrain', 'Jim Baker'],
  "Selon William Shortredge, pionnier du Colorado, deux Français vivaient sur le bas de la Green : Baptiste (Lusanne ? « Loosan ») et DuShay ; ce dernier mourut et fut enterré sur la terre de Jim Baker, sur Clear Creek, au nord de Denver. Cragin note aussi un Louie DuFrain, Français connaissant la famille Robidoux, à retrouver à Pueblo.",
  '324', "Dates non données ; Baker s'établit sur Clear Creek en 1859 (C182).")
F('03', "Ouest de l'Iowa, face à l'embouchure de la Nebraska : Joe Villandrie, venu du Canada vers 1810, tué par un éboulement de berge", 'personne', '1810/1860', -95.860, 41.000, 'h', ['Joe Villandrie'],
  "Un informateur arrivé dans les montagnes à l'automne 1853 rapporte que Joe Villandrie, venu dans l'Ouest vers 1810 depuis le Canada par les Grands Lacs, perdit la vie dans l'ouest de l'Iowa, en face de la rivière Nebraska (Platte), quand une berge s'effondra sur lui.",
  '325', "Point hypothétique sur le Missouri face à l'embouchure de la Platte.")
fiches = C.fiches
