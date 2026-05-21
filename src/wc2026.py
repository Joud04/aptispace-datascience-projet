"""Structure officielle de la Coupe du Monde FIFA 2026.

Tirage au sort final du 5 décembre 2025 (Kennedy Center, Washington D.C.).
48 équipes réparties en 12 groupes de 4.

Les noms d'équipes suivent **exactement** la convention du dataset du projet
(`matches_clean.csv` / `matches_a_predire.csv`) — ex. « Czech Republic » et non
« Czechia », « Turkey » et non « Türkiye » — afin que les jointures fonctionnent
sans recodage.

La phase à élimination directe sera ajoutée ici lors du notebook 06.
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
