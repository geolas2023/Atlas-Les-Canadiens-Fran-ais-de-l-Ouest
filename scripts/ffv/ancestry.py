# Étapes tirées de documents consultés sur Ancestry (session de l'utilisateur), 13 nov. 2026.
# (nom, lon, lat, debut, fin, edtf, certitude, phase, description, source, note)
A = "Ancestry.com (consulté le 13 nov. 2026) : "
C50 = "1850 United States Federal Census, NARA M432"
C60 = "1860 United States Federal Census, NARA M653"
C70 = "1870 United States Federal Census, NARA M593"
DR = "Quebec, Canada, Vital and Church Records (Drouin Collection), 1621-1968"
ADD = {
 'leduc': [
  ("Tecolote (« Tuckelata ») : le ménage de « Morris L. Dusch » au recensement de 1850", -105.281, 35.459, 1850.8, 1850.85, "1850", "certaine", "Pueblo, Huerfano, Mora, Adobe Creek",
   "L'index d'Ancestry donne à « Morris L. Dusch » 48 ans (né vers 1802) et le Canada comme lieu de naissance ; il partage le logement no 1505 avec Elma (Elena) Dusch, 14 ans, et Petra, moins d'un an (la María Pedra de Lecompte). Ancestry lui associe le nom « Amado Ledoux ».",
   A+C50+", Tuckelata, San Miguel, N.-M., bobine 469, p. 77b, ligne 18, logement 1505", "Âge divergent : 48 ans selon l'index d'Ancestry, 42 selon Lecompte ; à trancher sur l'image (ligne 18). Naissance vers 1802 ou 1808."),
 ],
 'lesperance': [
  ("Sorel : l'acte de baptême (10 oct. 1791)", -73.116, 46.040, 1791.77, 1791.78, "1791-10-10", "certaine", "Canada",
   "Le registre de Saint-Pierre de Sorel confirme le baptême de Pierre Lesperance le 10 octobre 1791, fils légitime de Pierre Lesperance et de Marguerite Lein. Un arbre de Geneanet le rattache aux Bonami dit Lespérance, ce qui éclaire la signature de 1839, « Pedro Buen-amigo Esperanza » : Buen-amigo traduit Bonami.",
   A+DR+", Sorel, St-Pierre, baptême du 10 oct. 1791 ; Geneanet Community Trees Index (« Pierre Bonami dit Lespérance »)", "Découverte : le patronyme d'origine Bonami dit Lespérance."),
  ("Tecolote : fermier au recensement de 1850", -105.279, 35.456, 1850.8, 1850.85, "1850", "certaine", "Nouveau-Mexique",
   "« Pedro Lesperance », 55 ans, né au Canada, fermier, terre de 1 200 $ ; logement no 1467, avec Cesaria (1 an), Tamslada Lina (25 ans) et Cimiano Lucero (24 ans).",
   A+C50+", Tuckelata, San Miguel, N.-M., bobine 469, p. 75b, ligne 23", "Âge sous-estimé (55 au lieu de 58-59)."),
  ("Sorel : baptême du neveu « Pedrito » (30 juin 1839)", -73.12, 46.043, 1839.49, 1839.5, "1839-06-30", "certaine", "Nouveau-Mexique",
   "Pierre, fils de Joseph Lesperance et de Marie Ocoin (Hocquin ?), est baptisé à Saint-Pierre de Sorel le 30 juin 1839 : il a bien 18 ans en 1857, quand son oncle l'appelle au Nouveau-Mexique. Ancestry signale ensuite un Pedro Lesperance maître de poste et inscrit au registre fédéral.",
   A+DR+", Sorel, St-Pierre, baptême du 30 juin 1839 ; U.S. Appointments of Postmasters (suggestion)", "Confirme le récit de Lecompte (p. 194)."),
  ("San Gerónimo : tanneur de 79 ans (recensement de 1870)", -105.371, 35.557, 1870.5, 1870.6, "1870", "certaine", "Nouveau-Mexique",
   "« Pedro Lesperance », 79 ans, né au Canada vers 1791, tanneur, terre de 700 $ et biens de 510 $, poste de Las Vegas ; vit avec Dolores (60 ans), son épouse Dolores Garcia, et Nicolasa Cordova (25 ans).",
   A+C70+", San Geronimo, San Miguel, N.-M., bobine 895, p. 200B, logement 76", None),
 ],
 'chalifoux': [
  ("Costilla (comté de Taos) : « Batis Chalifoux » au recensement de 1860", -105.43, 37.08, 1860.5, 1860.6, "1860", "certaine", "Fermier",
   "60 ans, né au Canada, fermier, 500 $ de terre et 500 $ de biens, illettré ; bureau de poste Fernando de Taos, logement no 1440. L'index ne liste que lui dans le ménage.",
   A+C60+", Costilla, Taos, N.-M., bobine 715, p. 127", "Lecompte cite le précinct de Culebra avec sa femme Mariana et deux fils : vérifier sur l'image les lignes voisines."),
 ],
 'beaubien': [
  ("Nicolet : baptême d'Alexis Hyppolite Beaubien selon Drouin (21 juin 1800 ?)", -72.618, 46.226, 1800.47, 1800.48, "1800-06-21", "approximative", "Canada",
   "L'index Drouin d'Ancestry date le baptême d'Alexis Hyppolite Beaubien du 21 juin 1800 à la cathédrale Saint-Jean-Baptiste de Nicolet, alors que Murphy, d'après le certificat de 1862, le place le 21 octobre 1800.",
   A+DR+", Nicolet, St-Jean-Baptiste, 21 juin 1800", "Divergence de date (juin ou octobre) à vérifier sur l'image du registre."),
  ("Taos : le marchand et sa famille au recensement de 1850", -105.576, 36.405, 1850.8, 1850.85, "1850", "certaine", "Juge",
   "Charles Beaubien, 50 ans, né au Canada, marchand, terre de 500 $ (logement no 1 de la Division nord de Taos), avec Maria Paula (30 ans), Maria Juana (13), Maria Teodora (8), Maria Petra (6) et Pablo (2).",
   A+C50+", Northern Division, Taos, N.-M., bobine 469, p. 91a", None),
 ],
 'charbonneau': [
  ("Secret Ravine (Township 9, comté de Placer) : recensement de 1860", -121.14, 38.83, 1860.5, 1860.6, "1860", "certaine", "Californie",
   "« John B. Chorbonnean », 57 ans, seul au logement no 700, bureau de poste Secret Ravine. L'index lit « Maine » comme lieu de naissance, sans doute une mauvaise lecture de « Mo. » (Missouri).",
   A+C60+", Township 9, Placer, Calif., bobine 62, p. 621", None),
 ],
 'bordeaux': [
  ("Fort Laramie : le traiteur et ses sept enfants au recensement de 1860", -104.43, 42.18, 1860.5, 1860.6, "1860", "certaine", "Traiteur indépendant",
   "« James Bardeau », 45 ans, né au Missouri, traiteur, biens de 5 000 $, poste de Fort Laramie (comté non organisé du Territoire du Nebraska) : Louisa (19 ans), Antoine (14), Louis (12), John (7), Susan (4), Alexander (2) et Henry (2 mois). Sa femme Marie n'apparaît pas dans l'index. Ancestry y associe aussi son gendre Clément Lamoureaux.",
   A+C60+", Unorganized County, Nebraska Territory, bobine 665, p. 238, logement 89", "Prospérité confirmée (Burton, 1860)."),
 ],
 'moncravie': [
  ("Comté de Jones (Nebraska) : « Daniels Ranch » au recensement de 1860", -97.20, 40.13, 1860.5, 1860.6, "1860", "approximative", "Nebraska",
   "John B. Moncravie, 63 ans, né en France, interprète, seul au logement no 314 ; bureau de poste « Daniels Ranch », comté de Jones (actuel comté de Jefferson, vallée de la Little Blue), ce qui localise sa ferme pillée de 1858.",
   A+C60+", Jones County, Nebraska Territory, bobine 665, p. 700", "Localisation précisée : comté de Jones (1856-1867), aujourd'hui comté de Jefferson."),
 ],
 'pariseau': [
  ("Comté de Marion : « Pierre Pariso » et Marie au recensement de 1850", -122.87, 45.185, 1850.8, 1850.85, "1850", "approximative", "Prairie française",
   "L'index d'Ancestry relève un « Pierre Pariso » et une Mary Pariso née au Canada vers 1833, la jeune Marie Dompierre épousée en juillet 1850.",
   A+C50+", Marion, Oregon Territory", "Âge de Pierre mal indexé (né vers 1818 selon l'index ; 1793 selon Munnick)."),
 ],
 'larpenteur': [
  ("Township de Sioux (comté de Harrison, Iowa) : recensement de 1860", -95.99, 41.84, 1860.5, 1860.6, "1860", "certaine", "Iowa et Dakota",
   "Charles Larpenteur, né en France vers 1808, et son fils Charles J., né vers 1845 au « Dakota Territory », recensés à Sioux Township, le pays de sa ferme « Fountainebleau ».",
   A+C60+", Sioux, Harrison, Iowa", "Charles fils est né à Fort Alexander en 1842 selon Pfaller."),
 ],
 'sarpy': [
  ("St. Mary (comté de Mills, Iowa) : recensement de 1860", -95.84, 41.05, 1860.5, 1860.6, "1860", "certaine", "Bellevue",
   "« P. A. Sarpy », recensé à St. Mary, comté de Mills (Iowa), où il avait fondé un bureau de poste et le St. Mary Gazette ; l'index le dit né vers 1804 en « Louisiana » (la Haute-Louisiane : Saint-Louis).",
   A+C60+", St Mary, Mills, Iowa", "Précise l'emplacement de St. Mary (comté de Mills)."),
 ],
}
