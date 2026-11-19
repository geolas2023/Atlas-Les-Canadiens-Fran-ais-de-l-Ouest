# Étienne Brûlé : Donald H. Kent, « The Myth of Etienne Brulé », Pennsylvania History, vol. 43, n° 4, 1976, p. 291-306 ;
# Jules Tremblay, « La sépulture d'Étienne Brûlé », Mémoires de la Société royale du Canada, 3e série, t. IX, 1915, sect. I, p. 145-170
# (PDF du Drive de l'auteur, dossier ETIENNE_BRULE). Préfixes KE76 et TB15.
from commun import Corpus
KE = "Kent, Donald H. (1976), « The Myth of Etienne Brulé », Pennsylvania History, vol. 43, n° 4, p. 291-306"
TB = "Tremblay, Jules (1915), « La sépulture d'Étienne Brûlé », Mémoires de la Société royale du Canada, 3e série, t. IX, section I, p. 145-170"
C1 = Corpus('Recherches', 'KE76', KE, page_fmt='p. {}')
C1.F('01', "Carantouan et la Susquehanna : le voyage d'Étienne Brûlé (1615-1616), un mythe ?", 'exploration', '1615-09~/1616-04~', -76.52, 42.00, 'h', ['Étienne Brûlé', 'Samuel de Champlain'],
  "Selon son propre récit, rapporté par Champlain dans ses Voyages de 1619, Étienne Brûlé aurait visité en 1615 le village allié de Carantouan, puis descendu une rivière jusqu'à la mer pendant l'hiver 1615-1616 : les historiens américains en ont fait le premier Blanc à explorer la Susquehanna et la Pennsylvanie, plaçant Carantouan sur la Chemung, au nord d'Athens. Donald Kent montre que tout repose sur cette seule source, supprimée de l'édition de 1632 des Voyages, racontée par un homme mal famé dans une situation délicate : rien ne permet de situer Carantouan ni d'identifier la rivière. Restent à Brûlé d'autres « premières » : le lac Supérieur, le saut Sainte-Marie, le cuivre du lac Supérieur et sans doute le dictionnaire huron de Sagard.",
  '291-306', "Point hypothétique sur la Chemung, au nord d'Athens (Pennsylvanie), emplacement que Kent récuse.")
C2 = Corpus('Recherches', 'TB15', TB, page_fmt='p. {}')
C2.F('01', "Toanché (pointe de Penetanguishene) : la mort et la sépulture d'Étienne Brûlé (juin 1633)", 'evenement', '1633-06', -79.95, 44.82, 'a', ['Étienne Brûlé', 'Aénons', 'Jean de Brébeuf'],
  "Arrivé en Huronie en 1610 dans le canot d'Aénons, chef du village de Toanché (tribu de l'Ours), Brûlé y vécut avec sa famille. En juin 1633, il y est mis à mort et mangé ; ses restes ne furent jamais portés à l'ossuaire de la fête des Morts. Le village est abandonné et remplacé par Oenrio et Toanché II ; en 1634, Brébeuf, débarqué au port de Toanché, passe devant « l'endroit où le pauvre Estienne Bruslé avait été barbarement et traîtreusement assommé ». Jules Tremblay situe la fosse sur la moitié est du lot 1 de la 17e concession du canton de Tiny (comté de Simcoe), sur la ferme des Grozelle, où les labours ont révélé un site de village huron.",
  '145-152', "Localisation proposée par Tremblay (1915) ; point approximatif sur la pointe de Penetanguishene (Ontario).")
fiches = C1.fiches + C2.fiches
