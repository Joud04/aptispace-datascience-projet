"""Structure officielle de la Coupe du Monde FIFA 2026.

Tirage au sort final du 5 décembre 2025 (Kennedy Center, Washington D.C.).
48 équipes réparties en 12 groupes de 4.

Les noms d'équipes suivent **exactement** la convention du dataset du projet
(`matches_clean.csv` / `matches_a_predire.csv`) — ex. « Czech Republic » et non
« Czechia », « Turkey » et non « Türkiye » — afin que les jointures fonctionnent
sans recodage.

Contenu : la phase de groupes (12 groupes) et la phase à élimination directe
(bracket des matchs 73 → 104).
"""

# Phase de groupes : 12 groupes (A → L) de 4 équipes.
GROUPS = {
    'A': ['Mexico', 'South Africa', 'South Korea', 'Czech Republic'],
    'B': ['Canada', 'Bosnia and Herzegovina', 'Qatar', 'Switzerland'],
    'C': ['Brazil', 'Morocco', 'Haiti', 'Scotland'],
    'D': ['United States', 'Paraguay', 'Australia', 'Turkey'],
    'E': ['Germany', 'Curaçao', 'Ivory Coast', 'Ecuador'],
    'F': ['Spain', 'Cape Verde', 'Saudi Arabia', 'Uruguay'],
    'G': ['Belgium', 'Egypt', 'Iran', 'New Zealand'],
    'H': ['Netherlands', 'Japan', 'Sweden', 'Tunisia'],
    'I': ['France', 'Senegal', 'Iraq', 'Norway'],
    'J': ['Argentina', 'Algeria', 'Austria', 'Jordan'],
    'K': ['Portugal', 'DR Congo', 'Uzbekistan', 'Colombia'],
    'L': ['England', 'Croatia', 'Ghana', 'Panama'],
}


def team_to_group():
    """Renvoie un dictionnaire {nom_equipe: lettre_du_groupe}."""
    return {team: g for g, teams in GROUPS.items() for team in teams}


def all_teams():
    """Renvoie la liste des 48 équipes qualifiées."""
    return [team for teams in GROUPS.values() for team in teams]


# ---------------------------------------------------------------------------
# Phase à élimination directe (source : Wikipédia, 2026 FIFA World Cup
# knockout stage). 32 qualifiés : 1er + 2e de chaque groupe + 8 meilleurs 3es.
# ---------------------------------------------------------------------------

# 16es de finale (matchs 73 → 88). Chaque case est un emplacement :
#   ('W', 'A') = vainqueur du groupe A
#   ('R', 'A') = 2e (runner-up) du groupe A
#   ('T', [groupes]) = 3e issu de l'un des groupes éligibles (table FIFA).
ROUND_OF_32 = {
    73: (('R', 'A'), ('R', 'B')),
    74: (('W', 'C'), ('R', 'F')),
    75: (('W', 'E'), ('T', ['A', 'B', 'C', 'D', 'F'])),
    76: (('W', 'F'), ('R', 'C')),
    77: (('R', 'E'), ('R', 'I')),
    78: (('W', 'I'), ('T', ['C', 'D', 'F', 'G', 'H'])),
    79: (('W', 'A'), ('T', ['C', 'E', 'F', 'H', 'I'])),
    80: (('W', 'L'), ('T', ['E', 'H', 'I', 'J', 'K'])),
    81: (('W', 'G'), ('T', ['A', 'E', 'H', 'I', 'J'])),
    82: (('W', 'D'), ('T', ['B', 'E', 'F', 'I', 'J'])),
    83: (('W', 'H'), ('R', 'J')),
    84: (('R', 'K'), ('R', 'L')),
    85: (('W', 'B'), ('T', ['E', 'F', 'G', 'I', 'J'])),
    86: (('R', 'D'), ('R', 'G')),
    87: (('W', 'J'), ('R', 'H')),
    88: (('W', 'K'), ('T', ['D', 'E', 'I', 'J', 'L'])),
}

# Tours suivants : chaque match oppose les vainqueurs de deux matchs précédents.
# 8es (89-96), quarts (97-100), demies (101-102), finale (104).
BRACKET = {
    89: (73, 75), 90: (74, 77), 91: (76, 78), 92: (79, 80),
    93: (83, 84), 94: (81, 82), 95: (86, 88), 96: (85, 87),
    97: (89, 90), 98: (93, 94), 99: (91, 92), 100: (95, 96),
    101: (97, 98), 102: (99, 100),
    104: (101, 102),
}

# Match pour la 3e place : les deux perdants des demi-finales.
THIRD_PLACE_MATCH = (101, 102)
