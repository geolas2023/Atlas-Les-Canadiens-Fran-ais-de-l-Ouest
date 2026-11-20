# Carmen Bernand, Histoire des peuples d'Amérique, Paris, Fayard, 2019 (édition numérique).
# PDF du Drive de l'auteur (HISTOIRE_LIVRES/AUTOCHTONES), parcouru en entier le 19 novembre 2026 par recherche plein texte
# (Français, Nouvelle-France, Louisiane, Canada, Hurons, Micmacs, Cartier, Champlain...). L'ouvrage porte surtout sur la
# Mésoamérique et les Andes ; les passages sur les Français sont rares. Préfixe BE19 ; pages = pages du PDF.
from commun import Corpus
S = "Bernand, Carmen (2019), Histoire des peuples d'Amérique, Paris, Fayard"
C = Corpus('Recherches', 'BE19', S, page_fmt='p. {} (PDF)')
F = C.F
F('01', "Stadaconé : les colliers d'esurgny offerts à Cartier et à Donnacona (1535-1536)", 'rencontre', '1535-09/1536-05', -71.21, 46.81, 'c', ['Jacques Cartier', 'Donnacona'],
  "Bernand s'appuie sur Cartier pour montrer la valeur des coquillages dans les Amériques : à Stadaconé, les petits coquillages blancs que Cartier appelle esurgny sont « la plus précieuse chose qu'ils aient en ce monde » ; on en fait des colliers dont on use comme « nous faisons d'or et d'argent » et qui, disent les Français, arrêtent les saignements de nez. Au départ de Cartier pour la France avec Donnacona, en 1536, les femmes puis les sujets du chef apportent des colliers et des paquets de peaux de castor et de loup marin, avec un couteau de cuivre rouge venu du Saguenay ; Cartier reçoit aussi son collier.",
  '77-78', "")
F('02', "Pays montagnais, au sud du Saint-Laurent : le père Le Jeune et le chaman Carigonan (hiver 1633-1634)", 'religion', '1633-10/1634-04', -69.5, 47.3, 'h', ['Paul Le Jeune', 'Carigonan'],
  "Bernand évoque l'hiver que le jésuite Paul Le Jeune passe dans la cabane du vieux chaman Carigonan : le jour à chasser, la nuit à débattre dans la fumée de l'immortalité de l'âme. Elle y voit l'exemple des « joutes » entre missionnaires et chamanes, les Indiens tenant les « Robes noires » pour de puissants sorciers capables de répandre les maladies.",
  '317', "Bernand écrit « Hurons » ; Le Jeune hivernait en fait avec des Montagnais (Innus), dans les Appalaches au sud de l'estuaire. Point hypothétique.")
F('03', "Île Royale et Mi'kmaq : les hiéroglyphes de l'abbé Pierre Maillard (années 1740-1750)", 'religion', '1738/1762', -60.78, 45.67, 'h', ['Pierre Maillard'],
  "En Nouvelle-France, l'abbé Pierre Maillard transcrit en pictogrammes le catéchisme de l'abbé Fleury pour en faciliter la lecture aux Mi'kmaq ; Bernand compare ces catéchismes, « bien plus rustiques », aux catéchismes testériens du Mexique, et note que les missionnaires y encourageaient une pensée millénariste en comparant les Mi'kmaq au peuple élu d'Israël.",
  '293, 308', "Point hypothétique à la mission de Maillard, île Sainte-Famille (Chapel Island), Cap-Breton.")
F('04', "Baie Lituya (« Port des Français », Alaska) : La Pérouse chez les Tlingits (juillet 1786)", 'exploration', '1786-07', -137.6, 58.62, 'c', ['Jean-François de La Pérouse'],
  "Au cours de son voyage autour du monde, La Pérouse entre dans la baie Lituya qu'il baptise Port des Français. Les Tlingits prennent La Boussole et L'Astrolabe pour d'énormes oiseaux-tonnerre. Pour La Pérouse, l'étude du marché des pelleteries compte autant que la science ; il dénonce la chasse intensive des mammifères marins et l'inertie des Espagnols.",
  '446', "Bernand le fait remonter de Monterey vers l'Alaska ; en réalité il toucha l'Alaska en juillet 1786 avant de descendre à Monterey en septembre. Date ajoutée d'après le journal de La Pérouse.")
fiches = C.fiches
