"""Construit data/lieux.geojson et data/trajets.geojson de l'Atlas Jolliet.

Sources :
  G  = Ernest Gagnon, Louis Jolliet, découvreur du Mississipi et du pays des Illinois, premier seigneur de l'île d'Anticosti,
       2e éd., Montréal, Beauchemin, 1913 (archive.org : louisjollietdc00gagnuoft).
  R  = Récit des voyages et des découvertes du R. Père Jacques Marquette […], Albany, Weed, Parsons, 1855
       (archive.org : recitdesvoyagese00marq).
  B  = BAnQ, Documents officiels et Relations sur les voyages de Louis Jolliet, fonds P1000, S3, D1035
       (https://numerique.banq.qc.ca/patrimoine/details/52327/3103023).
"""
import json, datetime, os

G = "Gagnon, Louis Jolliet (2e éd., 1913)"
R = "Récit des voyages du P. Marquette (1855)"
B = "BAnQ, P1000,S3,D1035, Documents officiels et Relations sur les voyages de Louis Jolliet"

def dec(edtf):
    """Date EDTF (AAAA, AAAA-MM, AAAA-MM-JJ, ~ toléré) -> année décimale (milieu de la période)."""
    d = edtf.replace('~', '').replace('?', '')
    p = [int(x) for x in d.split('-')]
    if len(p) == 1:
        return round(p[0] + 0.5, 4)
    if len(p) == 2:
        j = datetime.date(p[0], p[1], 15)
    else:
        j = datetime.date(*p)
    debut = datetime.date(j.year, 1, 1)
    n = 366 if j.year % 4 == 0 else 365
    return round(j.year + ((j - debut).days + 0.5) / n, 4)

LIEUX = []
def L(id, nom, lon, lat, edtf, precision, certitude, categorie, description, sources, note=''):
    a, b = (edtf.split('/') + [None])[:2]
    LIEUX.append({"type": "Feature", "geometry": {"type": "Point", "coordinates": [lon, lat]},
                  "properties": {"id": id, "nom": nom, "debut": dec(a), "fin": dec(b or a), "date_edtf": edtf,
                                 "precision": precision, "certitude": certitude, "categorie": categorie,
                                 "description": description, "sources": sources, "note": note, "type": "lieu"}})

TRAJETS = []
def T(id, nom, coords, edtf, certitude, mode, description, sources, note=''):
    a, b = edtf.split('/')
    TRAJETS.append({"type": "Feature", "geometry": {"type": "LineString", "coordinates": coords},
                    "properties": {"id": id, "nom": nom, "debut": dec(a), "fin": dec(b), "date_edtf": edtf,
                                   "certitude": certitude, "mode": mode, "description": description,
                                   "sources": sources, "note": note, "type": "trajet"}})

QUEBEC = [-71.205, 46.812]

# ---------------------------------------------------------------- Jeunesse à Québec
L('L01', "Québec : baptême de Louis Jolliet", -71.2066, 46.8128, '1645-09-21', 'jour', 'certaine', 'naissance',
  "Louis Jolliet est baptisé le 21 septembre 1645 dans l'église de l'Immaculée-Conception de Québec par le jésuite Barthélemy Vimont, qui fait office de curé. Il est le fils de Jean Jolliet et de Marie d'Abancour. Ses parrain et marraine sont Louis Maheu et Françoise Giffard. Québec ne compte alors que quelques centaines d'habitants.",
  f"{B}, fichiers 7-8 (acte de baptême et traduction) ; {G}, p. 27-31.",
  "L'acte donne la date du baptême ; la date exacte de la naissance n'est pas connue.")
L('L02', "Québec : clerc tonsuré au séminaire de Mgr de Laval", -71.2055, 46.8137, '1662-08-10', 'jour', 'certaine', 'vie',
  "Élève des jésuites, Louis Jolliet reçoit la tonsure et les ordres mineurs le 10 août 1662, deux jours avant le départ de Mgr de Laval pour la France. Au retour de l'évêque, en septembre 1663, il compte parmi les premiers élèves du séminaire de Québec. Il est aussi musicien : les jésuites l'invitent à souper avec Germain Morin, « officiers de musique », le 1er janvier 1665, et il est le seul organiste nommé par les chroniques de la colonie.",
  f"{G}, p. 38-39, 159-164.")
L('L03', "Québec : soutenance de philosophie au collège des Jésuites", -71.2077, 46.8131, '1666-07-02', 'jour', 'certaine', 'vie',
  "Le 2 juillet 1666, Louis Jolliet soutient des thèses de logique au collège des Jésuites de Québec. L'intendant Jean Talon prend part à la dispute et remarque le jeune homme, qu'il choisira plus tard pour les grandes découvertes. L'année suivante, Jolliet renonce à l'état ecclésiastique.",
  f"{G}, p. 40, 65.")

T('T01', "Voyage en France", [QUEBEC, [-70.5, 47.3], [-68.0, 48.9], [-64.5, 49.6], [-61.0, 48.3], [-59.4, 47.4], [-57.0, 46.6],
                             [-52.0, 46.2], [-40.0, 46.4], [-25.0, 46.6], [-10.0, 46.3], [-1.6, 46.1], [-1.15, 46.16]],
  '1667-08-28/1667-10', 'hypothetique', 'mer',
  "Le 28 août 1667, Louis Jolliet s'embarque à Québec sur le Saint-Sébastien pour la France. Il y passe l'hiver, sans doute pour apprendre l'hydrographie et le commerce, avant de revenir au Canada l'année suivante pour se lancer dans la traite des fourrures.",
  f"{G}, p. 41-43.",
  "Le port d'arrivée n'est pas connu : La Rochelle, principal port de départ vers le Canada, est retenue par hypothèse. La route suit le fleuve, le golfe et le détroit de Cabot.")
T('T02', "Retour au Canada", [[-1.15, 46.16], [-1.6, 46.1], [-10.0, 46.8], [-25.0, 47.2], [-40.0, 47.0], [-52.0, 46.4], [-57.0, 46.7],
                             [-59.4, 47.5], [-61.2, 48.4], [-64.5, 49.7], [-68.0, 49.0], [-70.5, 47.4], QUEBEC],
  '1668-05/1668-07', 'hypothetique', 'mer',
  "Jolliet rentre de France au printemps de 1668 et s'associe aussitôt à la traite vers les pays d'en haut.",
  f"{G}, p. 43.",
  "Date et route reconstituées : Gagnon indique seulement le retour en 1668.")

# ---------------------------------------------------------------- Les grands lacs (1669-1671)
T('T03', "Vers les mines de cuivre du lac Supérieur", [[-73.56, 45.50], [-74.0, 45.53], [-75.7, 45.42], [-76.9, 45.9], [-78.5, 46.3],
                             [-79.45, 46.32], [-80.4, 46.05], [-81.2, 45.95], [-82.5, 46.0], [-83.9, 46.35], [-84.35, 46.5], [-85.5, 46.7], [-87.5, 47.0]],
  '1669-04/1669-07', 'hypothetique', 'terre',
  "Sur l'ordre de l'intendant Talon, Jolliet part avec Jean Péré pour reconnaître les mines de cuivre du lac Supérieur, dont les missionnaires ont rapporté des échantillons. Il emprunte la route des canots de traite : l'Outaouais, la Mattawa, le lac Nipissing et la rivière des Français, puis la baie Georgienne et le Sault-Sainte-Marie.",
  f"{G}, p. 43-47.",
  "Tracé reconstitué par la route habituelle des canots ; le point d'arrivée sur le lac Supérieur est symbolique.")
L('L04', "Tinaouataoua : rencontre avec Dollier de Casson et Galinée", -79.98, 43.27, '1669-09-24', 'jour', 'approximative', 'decouverte',
  "Le 24 septembre 1669, au village iroquois de Tinaouataoua, à l'ouest du lac Ontario, Jolliet rencontre les sulpiciens Dollier de Casson et René de Bréhant de Galinée, partis avec Cavelier de La Salle. Il revient des grands lacs, où Talon l'a envoyé chercher les mines de cuivre, Galinée note sa rencontre dans son journal ; peu après, La Salle se sépare des deux prêtres, qui gagnent l'Ouest par le lac Érié.",
  f"{G}, p. 44-47.",
  "Site de Tinaouataoua placé près de l'actuelle Hamilton (Ontario), selon l'identification courante.")
L('L05', "Sault-Sainte-Marie : prise de possession de l'Ouest", -84.35, 46.495, '1671-06-14', 'jour', 'certaine', 'decouverte',
  "Le 14 juin 1671, au Sault-Sainte-Marie, Simon-François Daumont de Saint-Lusson prend possession au nom du roi des pays des grands lacs devant les délégués de quatorze nations. Le père Allouez harangue l'assemblée et l'on chante le Te Deum. Louis Jolliet assiste à la cérémonie, comme Jacques Largillier et Pierre Porteret, futurs compagnons de Marquette.",
  f"{G}, p. 48-58, 169.")

# ---------------------------------------------------------------- Le Mississippi (1672-1674)
T('T04', "De Lachine à Michillimakinac", [[-73.68, 45.43], [-74.0, 45.53], [-75.7, 45.42], [-76.9, 45.9], [-78.5, 46.3], [-79.45, 46.32],
                             [-80.4, 46.05], [-81.2, 45.95], [-82.5, 45.95], [-83.6, 45.9], [-84.73, 45.86]],
  '1672-10/1672-12-08', 'approximative', 'terre',
  "Chargé par Frontenac de découvrir la mer du Sud par la grande rivière Mississipi, Jolliet quitte Lachine à l'automne 1672 avec cinq hommes. Il a signé le 1er octobre un contrat de société de traite avec son frère Zacharie et François de Chavigny. Il remonte l'Outaouais et gagne la baie Georgienne : environ 350 lieues et une cinquantaine de portages. Il arrive à la mission Saint-Ignace de Michillimakinac le 8 décembre.",
  f"{G}, p. 63-68, 135 ; {R}, p. 5-6.")
L('L06', "Saint-Ignace de Michillimakinac : la rencontre avec Marquette", -84.73, 45.866, '1672-12-08/1673-05-17', 'jour', 'certaine', 'escale',
  "Le 8 décembre 1672, jour de l'Immaculée-Conception, Jolliet arrive à la mission Saint-Ignace avec les ordres de Frontenac et de Talon pour le père Jacques Marquette. L'hiver se passe à recueillir les renseignements des Indiens qui ont fréquenté ces pays et à tracer une carte des rivières, des nations et du cours de la grande rivière. Le 17 mai 1673, ils partent sur deux canots d'écorce avec cinq hommes, munis de blé d'Inde et de viande boucanée.",
  f"{R}, p. 5-8 ; {G}, p. 67-80.",
  "Le manuscrit de Sainte-Marie donne le 17 mai pour le départ ; Thévenot (1681) donne le 13 mai.")
T('T05', "De Michillimakinac aux Mascoutens", [[-84.73, 45.866], [-85.6, 45.75], [-86.6, 45.55], [-87.3, 45.3], [-87.62, 45.10], [-87.75, 44.9],
                             [-88.0, 44.55], [-88.06, 44.45], [-88.25, 44.27], [-88.45, 44.02], [-88.75, 43.95], [-88.95, 43.80]],
  '1673-05-17/1673-06-07', 'approximative', 'terre',
  "Les deux canots longent le nord du lac Michigan jusqu'à la baie des Puants. Ils remontent la rivière aux Renards, dont les rapides et les roches coupantes blessent les pieds des hommes qui traînent les canots, et traversent le lac Winnebago jusqu'au bourg des Mascoutens.",
  f"{R}, p. 9-19 ; {G}, p. 78-82.")
L('L07', "Village de la Folle Avoine", -87.62, 45.10, '1673-05', 'mois', 'approximative', 'decouverte',
  "Première nation rencontrée : les Folles Avoines (Menominees), à l'embouchure de leur rivière. Marquette décrit la récolte du riz sauvage, en septembre, depuis les canots. Les Folles Avoines tentent de dissuader les voyageurs : la grande rivière serait pleine de monstres et d'un démon qui engloutit les canots, et les nations du sud cassent la tête aux étrangers.",
  f"{R}, p. 9-14 ; {G}, p. 81.",
  "Village placé à l'embouchure de la rivière Menominee (Marinette, Wisconsin).")
L('L08', "Mission Saint-François-Xavier (baie des Puants)", -88.06, 44.45, '1673-06/1674-05', 'circa', 'certaine', 'escale',
  "Au fond de la baie des Puants, la mission jésuite de Saint-François-Xavier (De Pere, Wisconsin) est la dernière étape avant l'inconnu. Les voyageurs y passent à l'aller, en juin 1673, et y reviennent à la fin de septembre, après quatre mois de voyage. Jolliet et Marquette s'y séparent ; le père y passe l'hiver et l'été 1674, malade, avant de repartir pour les Illinois le 25 octobre 1674.",
  f"{R}, p. 14-17, 92, 145-148 ; {G}, p. 133, 299.",
  "Gagnon fait passer l'hiver à Jolliet au Sault-Sainte-Marie (voir cette étape) ; un document de son annexe le place à la mission avec Marquette.")
L('L09', "Bourg des Mascoutens", -88.95, 43.80, '1673-06-07/1673-06-10', 'jour', 'approximative', 'decouverte',
  "Le 7 juin 1673, les voyageurs arrivent au bourg des Mascoutens, la Nation du Feu, où vivent aussi des Miamis et des Kikapous. C'est le terme des découvertes françaises. Une croix ornée de peaux blanches, de ceintures rouges, d'arcs et de flèches se dresse au milieu du village. Le 9 juin, Jolliet demande aux anciens deux guides ; le 10, deux Miamis conduisent les canots vers la rivière qui mène au Mississipi.",
  f"{R}, p. 17-24 ; {G}, p. 82-84.",
  "Bourg situé sur la haute rivière aux Renards, à l'ouest du lac Winnebago (secteur de Berlin, Wisconsin) ; emplacement discuté.")
L('L10', "Portage de la Ouisconsing", -89.46, 43.54, '1673-06-10', 'jour', 'certaine', 'decouverte',
  "Les deux guides miamis conduisent les canots à travers les marais et les détours de la haute rivière aux Renards jusqu'à un portage de 2 700 pas, puis aident à porter les canots jusqu'à la Ouisconsing (Wisconsin) et s'en retournent. Les Français quittent les eaux qui coulent vers Québec pour entrer dans un pays inconnu.",
  f"{R}, p. 24-26 ; {G}, p. 84.",
  "Portage de l'actuelle ville de Portage (comté de Columbia, Wisconsin).")
T('T06', "La Ouisconsing jusqu'au Mississipi", [[-89.46, 43.54], [-89.75, 43.30], [-90.1, 43.18], [-90.6, 43.15], [-90.9, 43.05], [-91.17, 42.99]],
  '1673-06-10/1673-06-17', 'certaine', 'fleuve',
  "Pendant sept jours, les canots descendent la Ouisconsing, large rivière au fond de sable semée d'îles et de battures, entre des prairies, des bois et des coteaux. Les guides ont parlé d'une mine de plomb près de ses rives.",
  f"{R}, p. 25-27 ; {G}, p. 85-89.")
L('L11', "Entrée dans le Mississipi", -91.17, 42.99, '1673-06-17', 'jour', 'certaine', 'decouverte',
  "Le 17 juin 1673, à l'embouchure de la Ouisconsing, par 42 degrés et demi selon Jolliet, les voyageurs entrent dans le Mississipi « avec une joie qu'on ne peut expliquer ». Marquette nomme la grande rivière Conception, selon son vœu à la Vierge. Les jours suivants, ils voient des bisons (« pisikious »), des cygnes et des poissons monstrueux qui heurtent les canots.",
  f"{R}, p. 26-37 ; {G}, p. 89-95.")
T('T07', "La descente du Mississipi", [[-91.17, 42.99], [-91.1, 42.5], [-90.65, 42.0], [-90.4, 41.5], [-91.0, 40.9], [-91.45, 40.42], [-91.4, 39.9],
                             [-90.9, 39.4], [-90.6, 39.0], [-90.17, 38.89], [-90.12, 38.81], [-90.2, 38.5], [-89.95, 38.0], [-89.52, 37.4], [-89.15, 37.0],
                             [-89.5, 36.5], [-89.6, 36.0], [-90.05, 35.15], [-90.4, 34.8], [-90.6, 34.5], [-91.0, 34.1], [-91.05, 33.95]],
  '1673-06-17/1673-07-16', 'certaine', 'fleuve',
  "Les canots descendent le Mississipi un mois durant, de 42 degrés et demi à environ 33 degrés. Ils passent les rochers peints du Piasa, l'embouchure tumultueuse de la Pekitanouï (Missouri), le rocher de la Tour et l'Ouabouskigou (Ohio). Plus au sud viennent les cannes et les maringouins, puis les villages armés de fusils de Mitchigamea et d'Akansea.",
  f"{R}, p. 27-90 ; {G}, p. 89-118.")
L('L12', "Village des Peouarea (Illinois)", -91.45, 40.42, '1673-06-25', 'jour', 'approximative', 'decouverte',
  "Le 25 juin 1673, des traces de pas sur la rive droite mènent Jolliet et Marquette, seuls et sans armes, à un village de la nation des Illinois, les Peouarea, près de la rivière Moingouena (Des Moines). Ils sont reçus avec le calumet et un grand festin de sagamité, de poisson, de chien et de bison. Le grand chef leur offre un jeune esclave et un calumet, et tente de les détourner de descendre plus bas. La carte de Jolliet compte 300 cabanes à ce village.",
  f"{R}, p. 37-61 ; {G}, p. 96-103.",
  "Village placé sur la rive ouest, un peu en aval de l'embouchure de la Des Moines (Iowa), d'après Gagnon ; emplacement discuté.")
L('L13', "Les monstres peints du Piasa", -90.17, 38.89, '1673-06', 'circa', 'approximative', 'decouverte',
  "En longeant de hauts rochers, les voyageurs aperçoivent deux monstres peints en rouge, en vert et en noir, grands comme un veau, avec des cornes de chevreuil, des yeux rouges, une barbe de tigre et une queue qui s'enroule autour du corps. Les Indiens n'osent les regarder. Marquette en fait le croquis.",
  f"{R}, p. 62-65 ; {G}, p. 103-104.",
  "Falaises de l'actuelle Alton (Illinois).")
L('L14', "Embouchure de la Pekitanouï (Missouri)", -90.12, 38.81, '1673-06', 'circa', 'certaine', 'decouverte',
  "Peu après les monstres peints, un amas d'arbres entiers, de branches et d'îlots flottants sort avec fracas de l'embouchure de la Pekitanouï, si violent que l'eau en est toute boueuse. Marquette espère trouver par cette rivière la route de la mer Vermeille et de la Californie.",
  f"{R}, p. 65-68 ; {G}, p. 104-105.")
L('L15', "Embouchure de l'Ouabouskigou (Ohio)", -89.15, 37.0, '1673-07', 'circa', 'certaine', 'decouverte',
  "Les voyageurs passent l'embouchure de l'Ouabouskigou (Ohio), par environ 36 degrés. Les Chaouanons qui vivent sur ses rives sont, dit-on, si nombreux qu'on compte jusqu'à 23 villages dans un seul quartier.",
  f"{R}, p. 69-72 ; {G}, p. 105-106.")
L('L16', "Mitchigamea : le calumet sauve les voyageurs", -90.6, 34.5, '1673-07', 'circa', 'approximative', 'decouverte',
  "Vers 33 degrés, des guerriers du village de Mitchigamea s'arment d'arcs, de casse-têtes et de boucliers et se jettent à l'eau pour saisir les canots ; un casse-tête lancé passe au-dessus de leur tête. Marquette élève le calumet ; les anciens arrêtent les jeunes gens et invitent les Français à débarquer. Un vieillard leur sert d'interprète vers Akansea.",
  f"{R}, p. 77-81 ; {G}, p. 116.",
  "Village placé près de l'actuelle Helena (Arkansas) ; emplacement discuté.")
L('L17', "Akansea : le terme du voyage", -91.05, 33.95, '1673-07-16/1673-07-17', 'jour', 'approximative', 'decouverte',
  "Au village d'Akansea, sur la rive gauche presque en face de l'embouchure de l'Arkansas, les voyageurs sont reçus avec le calumet. Un jeune homme qui comprend l'illinois leur apprend que la mer n'est qu'à dix jours de canot, mais que des nations armées par les Espagnols barrent la route. Jolliet et Marquette décident de rebrousser chemin plutôt que de tomber aux mains des Espagnols et de perdre le fruit du voyage. Le chef déjoue un complot contre eux et leur offre un calumet.",
  f"{R}, p. 81-90 ; {G}, p. 117-125.",
  "Gagnon place le village sur la rive gauche (est), un peu au nord de l'embouchure de l'Arkansas.")
T('T08', "Le retour par la rivière des Illinois", [[-91.05, 33.95], [-91.0, 34.1], [-90.6, 34.5], [-90.05, 35.15], [-89.6, 36.0], [-89.5, 36.5], [-89.15, 37.0],
                             [-89.52, 37.4], [-89.95, 38.0], [-90.2, 38.5], [-90.12, 38.81], [-90.45, 38.97], [-90.6, 39.4], [-90.4, 39.85],
                             [-90.0, 40.2], [-89.59, 40.69], [-89.3, 40.95], [-88.98, 41.32], [-88.4, 41.4], [-88.08, 41.5], [-87.9, 41.7],
                             [-87.75, 41.82], [-87.62, 41.89], [-87.75, 42.6], [-87.85, 43.4], [-87.6, 44.2], [-87.9, 44.55], [-88.06, 44.45]],
  '1673-07-17/1673-09-25', 'approximative', 'fleuve',
  "Le 17 juillet 1673, les canots quittent Akansea et remontent péniblement le courant. Vers 38 degrés, ils prennent la rivière des Illinois, la plus belle et la plus commode qu'ils aient vue, bordée de prairies et de bois. Ils s'arrêtent trois jours chez les Peorias. Un chef des Kaskaskias et sa jeunesse les conduisent ensuite jusqu'au lac des Illinois (Michigan) par le portage de Chicago, puis ils longent la côte ouest du lac jusqu'à la baie des Puants.",
  f"{R}, p. 90-92 ; {G}, p. 125-133.")
L('L18', "Village des Peorias (rivière des Illinois)", -89.59, 40.69, '1673-08', 'circa', 'approximative', 'decouverte',
  "Au retour, les voyageurs passent trois jours chez les Peorias, sur la rivière des Illinois. Marquette prêche dans les cabanes et, au moment de partir, baptise un enfant mourant qu'on lui apporte au bord de l'eau.",
  f"{R}, p. 90-91 ; {G}, p. 125.",
  "Village placé près de l'actuelle Peoria (Illinois).")
L('L19', "Kaskaskia, grand bourg des Illinois", -88.98, 41.32, '1673-08/1677-04-27', 'circa', 'approximative', 'decouverte',
  "Au grand bourg des Kaskaskias, sur la rivière des Illinois, Marquette promet de revenir enseigner la foi. Il tient parole : arrivé le 8 avril 1675, il réunit en pleine prairie 500 chefs et anciens et 1 500 jeunes gens et fonde le Jeudi saint et le jour de Pâques la mission de la Conception. En avril 1677, le père Allouez trouve le bourg grossi de huit nations, dans 351 cabanes.",
  f"{R}, p. 92-100, 135-140 ; {G}, p. 128, 169.",
  "Bourg placé près de l'actuelle Utica (Illinois), face au Rocher (Starved Rock).")
L('L20', "Portage de Chicago", -87.75, 41.82, '1673-09', 'circa', 'approximative', 'decouverte',
  "Guidés par les Kaskaskias, Jolliet et Marquette passent du bassin du Mississipi à celui du lac des Illinois par le court portage entre la rivière des Plaines et la rivière Chicago. Jolliet y voit l'avenir : un simple canal d'une demi-lieue suffirait, dit-il, pour aller en barque du lac Érié jusqu'au golfe du Mexique.",
  f"{R}, p. 92 ; {G}, p. 128-131 ; {B}, fichiers 13-28 et 37-47 (Relation de la découverte de la mer du Sud, 1674).",
  "L'idée du canal est rapportée par la Relation rédigée par le père Dablon d'après le récit de Jolliet.")
T('T09', "De la baie des Puants au Sault-Sainte-Marie", [[-88.06, 44.45], [-87.6, 44.9], [-87.0, 45.4], [-86.0, 45.75], [-84.73, 45.866],
                             [-84.3, 46.0], [-84.1, 46.25], [-84.35, 46.49]],
  '1673-10/1673-11', 'hypothetique', 'terre',
  "Après avoir quitté Marquette, Jolliet regagne Saint-Ignace de Michillimakinac, puis le Sault-Sainte-Marie, où il passe l'hiver à mettre au propre son journal et sa carte.",
  f"{G}, p. 133-134.",
  "Gagnon déduit cet itinéraire du récit de l'accident de 1674 ; un document de son annexe place l'hivernage à la mission Saint-François-Xavier.")
L('L21', "Sault-Sainte-Marie : l'hivernage de 1673-1674", -84.33, 46.51, '1673-11/1674-05', 'circa', 'approximative', 'escale',
  "Jolliet passe l'hiver de 1673-1674 au Sault-Sainte-Marie. Il y laisse aux jésuites une copie de son journal, que détruira un incendie. À la fin de mai 1674, il repart pour Québec avec deux canotiers, dont le jeune esclave peouarea reçu au Mississipi.",
  f"{G}, p. 133-135, 143.",
  "Lieu d'hivernage discuté (voir la mission Saint-François-Xavier).")
T('T10', "Du Sault-Sainte-Marie à Lachine par les lacs", [[-84.35, 46.49], [-84.1, 46.2], [-83.5, 45.9], [-82.4, 44.6], [-82.42, 43.0],
                             [-82.6, 42.6], [-83.1, 42.1], [-82.0, 42.0], [-80.4, 42.55], [-79.06, 43.08], [-79.0, 43.4], [-77.5, 43.7],
                             [-76.48, 44.22], [-75.9, 44.35], [-75.0, 44.95], [-74.3, 45.2], [-73.68, 45.43]],
  '1674-05-25/1674-07-15', 'hypothetique', 'terre',
  "À la fin de mai 1674, Jolliet quitte le Sault avec deux canotiers. Selon Gagnon, il descend par les lacs Huron, Érié et Ontario, passe le fort Frontenac et les Mille-Îles et arrive aux rapides du Sault-Saint-Louis.",
  f"{G}, p. 135-136.",
  "Itinéraire proposé par Gagnon ; la route de l'Outaouais, plus habituelle, n'est pas exclue.")
L('L22', "Fort Frontenac (Cataracoui)", -76.48, 44.23, '1674-07', 'circa', 'approximative', 'escale',
  "Sur la route du retour, Jolliet passe au fort Frontenac, que le gouverneur vient de faire construire à Cataracoui, à la tête du Saint-Laurent. La Relation de 1674 compte sur ce fort pour faciliter la communication de Québec avec le lac Érié.",
  f"{G}, p. 135-136 ; {B}, fichiers 13-28 et 37-47 (Relation, 1674).",
  "Passage déduit de l'itinéraire proposé par Gagnon.")
L('L23', "Naufrage au Sault-Saint-Louis", -73.62, 45.42, '1674-07~', 'circa', 'certaine', 'naufrage',
  "En vue de Montréal, au pied du Sault-Saint-Louis (rapides de Lachine), le canot de Jolliet chavire. Deux hommes et le jeune esclave peouarea se noient ; Jolliet reste quatre heures dans l'eau avant d'être sauvé par des pêcheurs. Il perd sa cassette, son journal et sa carte : « il ne m'est rien resté que la vie », écrit-il à Mgr de Laval.",
  f"{B}, fichiers 24-28 et 45-47 (lettre de Jolliet du 10 octobre 1674) ; {G}, p. 136-137, 316.",
  "Gagnon corrige la date de la mi-août en mi-juillet 1674.")
T('T11', "Du Sault-Saint-Louis à Québec", [[-73.62, 45.42], [-73.55, 45.5], [-73.2, 45.85], [-72.55, 46.33], [-72.0, 46.55], QUEBEC],
  '1674-07~/1674-08-01', 'approximative', 'fleuve',
  "Sauvé des eaux, Jolliet est conduit à Ville-Marie, puis descend à Québec, où la population l'accueille.",
  f"{G}, p. 137-138.")
L('L24', "Québec : la Relation de la découverte de la mer du Sud", -71.2072, 46.8125, '1674-08-01/1674-11-14', 'jour', 'certaine', 'vie',
  "À Québec, le supérieur des jésuites Claude Dablon rédige d'après le récit de Jolliet la « Relation de la découverte de la mer du Sud », datée du 1er août 1674. Jolliet redessine de mémoire la carte perdue et la présente à Frontenac, qui l'envoie à Colbert le 14 novembre. Le 10 octobre, il écrit à Mgr de Laval le récit du voyage et de son naufrage. Il a 29 ans.",
  f"{B}, fichiers 13-28 (manuscrit), 29-36 (édition de 1944) et 37-47 (transcription) ; {G}, p. 138-149.")

# ---------------------------------------------------------------- Le second voyage de Marquette (1674-1675)
L('L25', "Hivernage de Marquette au portage de Chicago", -87.68, 41.84, '1674-12/1675-03-29', 'mois', 'approximative', 'escale',
  "Reparti de la baie des Puants le 25 octobre 1674 avec Pierre Porteret et Jacques Largillier, Marquette, repris de son flux de sang, hiverne dans une cabane à deux lieues du portage, sur la rivière qui mène aux Illinois. Un chirurgien et Pierre Moreau, dit la Toupine, qui traitent dans un village voisin, lui apportent des bleuets et du blé. Il repart le 29 mars 1675 pour le bourg des Kaskaskias.",
  f"{R}, p. 93-96, 145-169 (journal autographe de Marquette) ; {G}, p. 169-170.",
  "Compagnon de Jolliet en 1673, Marquette est suivi ici jusqu'à sa mort.")
L('L26', "Mort du père Marquette", -86.45, 43.95, '1675-05-19', 'jour', 'approximative', 'mort',
  "Revenant des Illinois par la côte est du lac Michigan, Marquette, à bout de forces, désigne à ses deux compagnons une éminence à l'embouchure d'une rivière. Il y meurt le samedi 19 mai 1675 dans une cabane d'écorce, le crucifix sous les yeux. Porteret et Largillier l'enterrent au son de la clochette et plantent une grande croix. En 1677, des Kiskakons ramènent ses ossements à la mission Saint-Ignace.",
  f"{R}, p. 100-117 ; {G}, p. 169-177.",
  "Embouchure de la rivière qui porte aujourd'hui son nom (Ludington, Michigan) ; l'emplacement exact est discuté.")

# ---------------------------------------------------------------- Le seigneur et l'hydrographe
L('L27', "Québec : mariage avec Claire-Françoise Bissot", -71.2066, 46.8128, '1675-10-07', 'jour', 'certaine', 'vie',
  "Le 1er octobre 1675, dans la maison de Jacques de Lalande à la basse-ville, Louis Jolliet, 30 ans, signe son contrat de mariage avec Claire-Françoise Bissot, 19 ans, fille du défunt François Bissot et de Marie Couillard. Le mariage est célébré le 7 octobre à Notre-Dame de Québec par Henri de Bernières, en présence de Charles Bazire, de Jean-Baptiste Le Gardeur de Repentigny et de Jean Juchereau de la Ferté. Par sa femme, Jolliet entre dans la famille des pêcheries de la côte nord.",
  f"{B}, fichiers 5-6 (acte de mariage) ; {G}, p. 179-191.")
L('L28', "Québec : l'assemblée sur la traite de l'eau-de-vie", -71.2048, 46.8115, '1678-10-26', 'jour', 'certaine', 'vie',
  "Le 26 octobre 1678, au château Saint-Louis, Frontenac réunit une vingtaine de notables pour donner leur avis sur la vente de l'eau-de-vie aux Indiens. L'avis de Jolliet est consigné au procès-verbal de l'assemblée.",
  f"{G}, p. 200-205.")
L('L29', "Îles de Mingan", -63.9, 50.22, '1679-03-10/1690-10', 'jour', 'approximative', 'concession',
  "Le 10 mars 1679, l'intendant Duchesneau concède à Jolliet et à son beau-père Jacques de Lalande les îles et îlets de Mingan, sur la côte nord du golfe, pour la pêche et la traite. Le roi ratifie la concession le 29 mai 1680. Jolliet y construit une maison et un magasin, que la flotte de Phips détruit en 1690.",
  f"{G}, p. 213-215, 240-241, 248.",
  "Établissement placé dans l'archipel de Mingan ; emplacement précis inconnu.")
T('T12', "Vers la baie d'Hudson par le Saguenay et le lac Mistassini", [QUEBEC, [-70.6, 47.25], [-69.72, 48.14], [-70.3, 48.4], [-71.05, 48.42],
                             [-71.7, 48.5], [-72.2, 48.75], [-72.15, 49.2], [-72.4, 50.0], [-73.0, 50.6], [-73.6, 51.0], [-74.3, 51.3],
                             [-75.5, 51.45], [-76.2, 51.45], [-77.2, 51.5], [-78.0, 51.45], [-78.75, 51.48]],
  '1679-05-13/1679-06-25', 'approximative', 'terre',
  "Le 13 mai 1679, Jolliet part de Québec pour reconnaître les postes anglais de la baie d'Hudson. Il remonte le Saguenay jusqu'au lac Saint-Jean, puis la longue rivière Péribonca jusqu'au lac des Mistassins, descend la rivière de Rupert et traverse le lac Nemiskau. Il compte 343 lieues de détours, 160 en ligne droite, et 122 portages.",
  f"{G}, p. 216-219.")
L('L30', "Tadoussac", -69.72, 48.14, '1679-05', 'mois', 'certaine', 'escale',
  "Au poste de Tadoussac, à l'embouchure du Saguenay, Jolliet s'engage dans la route des Montagnais vers le nord. Le jésuite Antoine Silvy l'accompagne peut-être, selon le registre de Tadoussac.",
  f"{G}, p. 216, 224.")
L('L31', "Lac des Mistassins", -73.6, 51.0, '1679-06', 'circa', 'approximative', 'escale',
  "Jolliet traverse le grand lac des Mistassins, au cœur du pays des Cris, sur la route des canots entre le Saint-Laurent et la baie James.",
  f"{G}, p. 217.")
L('L32', "Le fort anglais de la rivière de Rupert", -78.75, 51.48, '1679-06-25~/1679-07', 'circa', 'approximative', 'decouverte',
  "À l'embouchure de la rivière de Rupert, Jolliet trouve le poste anglais de la Compagnie de la Baie d'Hudson. Les Anglais le reçoivent bien et cherchent à l'attirer à leur service. Il rapporte au gouverneur qu'ils sont maîtres de la traite des nations du nord et qu'il faut les déloger.",
  f"{G}, p. 219-223.",
  "Poste placé à l'embouchure de la rivière de Rupert (Waskaganish).")
T('T13', "Retour par la rivière Mistassini", [[-78.75, 51.48], [-78.0, 51.45], [-76.2, 51.45], [-74.3, 51.3], [-73.6, 51.0], [-72.9, 50.4],
                             [-72.6, 49.6], [-72.25, 48.9], [-71.7, 48.5], [-71.05, 48.42], [-70.3, 48.4], [-69.72, 48.14], [-70.6, 47.25], QUEBEC],
  '1679-07/1679-10-27', 'approximative', 'terre',
  "Jolliet revient par la rivière Mistassini, que les Indiens appellent Kokigaousipi, jusqu'au lac Saint-Jean, et rentre à Québec le 27 octobre 1679, après sept mois d'absence. Il dresse une carte de sa route, datée du 8 novembre.",
  f"{G}, p. 223-227.")
L('L33', "Île d'Anticosti : la seigneurie de Jolliet", -63.6, 49.55, '1680-03/1690-10', 'mois', 'hypothetique', 'concession',
  "En mars 1680, Duchesneau concède à Jolliet en fief et seigneurie l'île d'Anticosti, à l'embouchure du Saint-Laurent, en récompense de la découverte du pays des Illinois. Le roi ratifie la concession le 29 mai 1680 et donne à Jolliet le titre d'hydrographe. En 1681, Jolliet s'y établit avec sa famille : douze personnes, deux arpents défrichés, deux bêtes à cornes et six fusils. Il y hiverne deux fois dans une maison qu'il a bâtie et y fait la pêche et la traite.",
  f"{G}, p. 228-241, 304-305.",
  "L'emplacement de l'établissement sur l'île n'est pas connu : le point est symbolique.")
L('L34', "Québec : adjudication de terres pour Villeray et Vitré", -71.235, 46.80, '1685-02-19', 'jour', 'certaine', 'vie',
  "Par un acte signé à Québec le 19 février 1685, Louis Jolliet reconnaît que, s'il s'est rendu adjudicataire le 13 février devant le lieutenant général de la prévôté de terres de la côte Sainte-Geneviève, dite Saint-Agnan (880 livres), et d'une maison avec place et jardin à la haute-ville (680 livres), il n'a agi que pour faire plaisir à Louis Rouer de Villeray et à M. de Vitré, à leur prière. Il s'engage à leur passer tous les actes nécessaires. La transcription est suivie d'un acte du notaire Gilles Rageot.",
  f"{B}, fichiers 1-4 (manuscrit autographe et transcriptions).",
  "Point placé sur la côte Sainte-Geneviève, à l'ouest de la haute-ville ; emplacement des terres approximatif.")
L('L35', "Québec : carte du fleuve et demande d'un navire", -71.2048, 46.8118, '1685-11-18', 'jour', 'certaine', 'vie',
  "Le 18 novembre 1685, le gouverneur Denonville demande au ministre une gratification pour Jolliet, qui a fait 46 voyages sur le fleuve et en a levé la carte, dessinée par Franquelin, et une barque pour achever la reconnaissance du golfe. Il insiste le 8 mai 1686 : il faut à Québec un maître de navigation.",
  f"{G}, p. 241-244.")
L('L36', "Le pillage d'Anticosti et de Mingan par Phips", -63.75, 49.85, '1690-08~', 'circa', 'hypothetique', 'combat',
  "En 1690, en route vers Québec, la flotte de Sir William Phips pille et détruit l'établissement fortifié de Jolliet à Anticosti et son poste de Mingan. Jolliet perd l'essentiel de ses biens.",
  f"{G}, p. 248, 293.",
  "Date et lieu précis inconnus ; Gagnon signale la perte sans la dater.")
L('L37', "Siège de Québec : Claire Bissot prisonnière de Phips", -70.95, 46.93, '1690-10-16/1690-10-24', 'jour', 'certaine', 'combat',
  "Prises plus tôt sur une barque près de Tadoussac, la femme de Jolliet et sa mère, Mme de Lalande, sont prisonnières à bord de la flotte de Phips qui assiège Québec du 16 au 23 octobre 1690. Mme de Lalande négocie l'échange des prisonniers. Le 24, la flotte en retraite mouille à l'Arbre-Sec, à l'île d'Orléans.",
  f"{G}, p. 185, 248-250.")
L('L38', "Naufrage de Rainsford à la pointe ouest d'Anticosti", -64.52, 49.87, '1690-10-28/1691-06-28', 'jour', 'approximative', 'naufrage',
  "Au retour de l'expédition contre Québec, le brigantin du capitaine John Rainsford fait naufrage le 28 octobre 1690 (calendrier julien) à la pointe ouest d'Anticosti, la future pointe aux Anglais. Le chirurgien meurt le 20 décembre, puis une quarantaine d'hommes. Le 25 mars 1691, cinq hommes partent en chaloupe et atteignent Boston le 9 mai ; Rainsford y ramène dix-sept survivants le 28 juin.",
  f"{G}, p. 250-252.",
  "Épisode de la seigneurie de Jolliet rapporté par Gagnon d'après Cotton Mather.")

# ---------------------------------------------------------------- Le Labrador (1694)
T('T14', "De Québec à Mingan", [QUEBEC, [-70.5, 47.3], [-69.3, 48.2], [-67.9, 49.05], [-66.4, 49.95], [-65.2, 50.05], [-64.2, 50.15], [-63.9, 50.2]],
  '1694-04-28/1694-06-05', 'approximative', 'cote',
  "Le 28 avril 1694, le Saint-François quitte Québec avec Jolliet, son fils Louis (18 ans), un récollet, des cadets et quatorze hommes d'équipage, à destination de Mingan, du détroit de Belle-Isle et du « Labrador océanique ». Le navire fait plusieurs mouillages pour la traite et la pêche avant de quitter Mingan au début de juin.",
  f"{G}, p. 253-260.")
T('T15', "Le long de la côte du Labrador", [[-63.9, 50.2], [-61.5, 50.15], [-59.8, 50.3], [-58.5, 50.85], [-57.3, 51.35], [-56.7, 51.6], [-55.7, 52.05],
                             [-55.55, 52.25], [-55.75, 52.38], [-55.62, 52.6], [-55.75, 52.95], [-56.2, 53.4], [-56.7, 53.65], [-57.4, 54.2],
                             [-58.0, 54.75], [-59.4, 55.05], [-59.85, 55.35], [-60.2, 55.47], [-60.45, 55.65], [-60.6, 55.8]],
  '1694-06-05/1694-08-12', 'hypothetique', 'cote',
  "Du début de juin au 12 août 1694, Jolliet longe la côte nord du golfe, franchit le détroit de Belle-Isle et remonte la côte du Labrador en nommant les baies et les havres : Saint-Louis, Saint-François, Saint-Michel, Sainte-Claire. Il note les latitudes, la déclinaison de l'aiguille et les glaces, et rencontre les Inuits.",
  f"{B}, fichiers 9-12 (journal manuscrit de 1694) ; {G}, p. 259-278.",
  "Tracé reconstitué d'après les latitudes estimées par Jolliet (53°44′ à 55°45′), qui sont approximatives ; l'identification moderne des baies est incertaine.")
L('L39', "Îles Saint-Jacques : la croix de Jolliet", -57.3, 51.35, '1694-07~', 'circa', 'hypothetique', 'decouverte',
  "Après environ un mois de navigation depuis Mingan, le Saint-François atteint les îles Saint-Jacques, face à la baie de Misfina, d'où l'on voit Terre-Neuve. Jolliet plante une croix sur l'une des îles.",
  f"{G}, p. 260.",
  "Îles non identifiées avec certitude, à l'entrée du détroit de Belle-Isle.")
L('L40', "Pointe du Détour (détroit de Belle-Isle)", -55.65, 52.2, '1694-07-09/1694-07-11', 'jour', 'approximative', 'escale',
  "Le soir du 9 juillet 1694, le navire atteint les îles Balsamon, à l'entrée du détroit de Belle-Isle. On voit des glaces en mer le 10. Le 11, il double la pointe du Détour, à la sortie du détroit, que Gagnon identifie au cap Charles.",
  f"{G}, p. 261.")
L('L41', "Baie Saint-Louis et havre Saint-François", -55.72, 52.45, '1694-07-13/1694-07-17', 'jour', 'hypothetique', 'decouverte',
  "Le 13 juillet, Jolliet entre dans une baie qu'il nomme Saint-Louis ; feux et coups de canon n'attirent personne. Le 15, des canots inuits approchent et Jolliet traite avec les deux premiers visiteurs, Capitena Joannis et Kamicterineac. Le 16, il entre dans un havre qu'il nomme Saint-François, du nom de l'armateur François Pachot.",
  f"{G}, p. 262-265.")
L('L42', "Village inuit du chef Guignac", -56.9, 53.73, '1694-07-23/1694-07-25', 'jour', 'hypothetique', 'decouverte',
  "Vers 53°44′ selon Jolliet, le navire mouille devant un village inuit de neuf cabanes. Le 25 juillet, Jolliet descend à terre avec huit hommes armés. Le chef Guignac l'accueille et lui fait visiter le village ; les Inuits chantent et dansent. Le récollet avait visité le village la veille.",
  f"{G}, p. 266-274.",
  "Latitude estimée par Jolliet ; le village serait vers la baie Sandwich ou l'inlet Hamilton.")
L('L43', "Baie de Pachot et baie Sainte-Claire", -60.55, 55.75, '1694-08-04/1694-08-12', 'jour', 'hypothetique', 'decouverte',
  "Le 4 août, le Saint-François entre dans une baie que Jolliet nomme Pachot et y reste trois jours. Le 11, huit canots et quatre chaloupes annoncent le chef Amaillouk, qui arrive le 12 avec 22 canots et trois chaloupes. Le navire quitte ce jour-là la baie que Jolliet nomme Sainte-Claire, en l'honneur de la patronne de sa femme. Faute de vivres et de bons câbles, on décide à l'unanimité de rentrer.",
  f"{G}, p. 275-278.",
  "Point le plus au nord du voyage (vers 55°45′ selon Jolliet) ; position reconstituée.")
T('T16', "Retour du Labrador", [[-60.6, 55.8], [-59.0, 55.3], [-57.6, 54.3], [-56.2, 53.3], [-55.55, 52.4], [-55.7, 52.05], [-57.0, 51.45],
                             [-59.0, 50.4], [-61.5, 50.05], [-64.0, 49.95], [-66.5, 49.7], [-68.2, 48.95], [-69.4, 48.15], [-70.5, 47.3], QUEBEC],
  '1694-08-13/1694-10', 'hypothetique', 'mer',
  "Rentré à Québec à l'automne 1694, Jolliet fait rapport à Frontenac et trouve le château Saint-Louis démoli et en reconstruction. Il tire de son voyage une carte du Labrador, qu'il datera du 23 octobre 1699.",
  f"{G}, p. 278-282.",
  "Date et route du retour non précisées par Gagnon.")

# ---------------------------------------------------------------- Dernières années
T('T17', "Voyage en France (pilote de La Charente)", [QUEBEC, [-70.5, 47.3], [-68.0, 48.9], [-64.5, 49.6], [-61.0, 48.3], [-59.4, 47.4],
                             [-57.0, 46.6], [-52.0, 46.2], [-40.0, 46.4], [-25.0, 46.6], [-10.0, 46.3], [-1.6, 46.1], [-1.15, 46.16]],
  '1695-11/1696-01', 'hypothetique', 'mer',
  "À la fin de novembre 1695, sur l'ordre de l'intendant Champigny, Jolliet pilote le navire du roi La Charente hors du golfe, tâche difficile si tard en saison. Il passe en France, où il présente ses cartes à M. de Lagny et demande le poste d'hydrographe.",
  f"{G}, p. 282-285.",
  "Port d'arrivée inconnu ; La Rochelle retenue par hypothèse.")
T('T18', "Retour de France", [[-1.15, 46.16], [-1.6, 46.1], [-10.0, 46.8], [-25.0, 47.2], [-40.0, 47.0], [-52.0, 46.4], [-57.0, 46.7],
                             [-59.4, 47.5], [-61.2, 48.4], [-64.5, 49.7], [-68.0, 49.0], [-70.5, 47.4], QUEBEC],
  '1696-05/1696-07', 'hypothetique', 'mer',
  "Jolliet revient de France en 1696.",
  f"{G}, p. 283.",
  "Date et route reconstituées.")
L('L44', "Québec : professeur d'hydrographie", -71.2077, 46.8131, '1697-04-30', 'jour', 'certaine', 'vie',
  "Par brevet du 30 avril 1697, le roi nomme Louis Jolliet professeur d'hydrographie à Québec, où il projetait depuis longtemps d'ouvrir une classe de navigation. Le 23 octobre 1699, il date une carte du Labrador et de la baie d'Hudson dédiée à Villebois.",
  f"{G}, p. 229, 282-285, 321.")
L('L45', "Seigneurie Jolliet (rivière Etchemin)", -71.17, 46.70, '1697-04-30', 'jour', 'approximative', 'concession',
  "Le même jour, 30 avril 1697, Frontenac et Champigny concèdent à Jolliet une petite seigneurie au sud de Québec : des îlets de la rivière Etchemin au-dessus du premier sault, avec trois lieues de front sur autant de profondeur, voisine de la seigneurie de Lauzon. C'est la seule de ses trois seigneuries qui porte son nom ; il ne l'exploitera pas lui-même.",
  f"{G}, p. 285-288.",
  "Point placé sur la rivière Etchemin, en amont de Saint-Romuald ; limites approximatives.")
L('L46', "Mort de Louis Jolliet", -59.17, 50.83, '1700-05-04/1700-10-18', 'circa', 'hypothetique', 'mort',
  "Louis Jolliet signe pour la dernière fois un acte de la paroisse de Québec le 4 mai 1700. Le 18 octobre suivant, Callières et Champigny annoncent sa mort au ministre ; Franquelin reçoit sa charge d'hydrographe. Selon Pierre Margry, il serait mort et aurait été enterré dans une île en face du Gros Mécatina, sur la côte nord. Sa veuve, Claire Bissot, meurt à Québec le 1er mars 1710.",
  f"{G}, p. 283-293, 322.",
  "Lieu et date de la mort incertains : le point suit l'hypothèse de Margry, que Gagnon juge mal établie.")

os.makedirs('data', exist_ok=True)
for nom, feats in (('lieux', LIEUX), ('trajets', TRAJETS)):
    json.dump({"type": "FeatureCollection", "features": feats}, open(f'data/{nom}.geojson', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(LIEUX), 'lieux,', len(TRAJETS), 'trajets')
