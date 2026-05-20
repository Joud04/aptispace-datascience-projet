"""
Module de visualisation — Projet Fil Rouge Data Science.

Regroupe la charte graphique du projet et cinq fonctions de tracé dédiées à
l'exploration de l'histoire du football international.

Utilisé par le notebook `03_visualisation.ipynb`.
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def set_custom_style(theme='light'):
    """Active une charte graphique homogène pour toutes les figures.

    Paramètres
    ----------
    theme : str
        'light' (fond clair, défaut) ou 'dark' (fond sombre).
    """
    if theme == 'dark':
        plt.style.use('dark_background')
        sns.set_palette('bright')
    else:
        sns.set_theme(style='whitegrid')
        sns.set_palette('deep')

    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['axes.titlesize'] = 13
    plt.rcParams['axes.titleweight'] = 'bold'
    plt.rcParams['axes.labelsize'] = 11


def plot_matches_per_year(df):
    """Nombre de matchs internationaux par année, avec repères historiques.

    Les deux guerres mondiales et la pandémie de Covid-19 sont mises en
    évidence : ce sont des creux nets dans l'activité footballistique.

    Paramètres
    ----------
    df : pandas.DataFrame
        Matchs, avec la colonne `year`.

    Retour
    ------
    matplotlib.figure.Figure
    """
    par_an = df.groupby('year').size()

    fig, ax = plt.subplots()
    ax.plot(par_an.index, par_an.values, color='#1f77b4')
    ax.fill_between(par_an.index, par_an.values, alpha=0.15, color='#1f77b4')

    evenements = [(1914, 1918, 'Première\nGuerre mondiale'),
                  (1939, 1945, 'Seconde\nGuerre mondiale'),
                  (2020, 2021, 'Covid-19')]
    for debut, fin, label in evenements:
        ax.axvspan(debut, fin, alpha=0.25, color='crimson')
        ax.text((debut + fin) / 2, par_an.max() * 0.97, label,
                ha='center', va='top', fontsize=8, color='crimson')

    ax.set_xlabel('Année')
    ax.set_ylabel('Nombre de matchs')
    ax.set_title('Nombre de matchs internationaux par année')
    fig.tight_layout()
    return fig


def plot_top_tournaments(df, n=15):
    """Les `n` tournois ayant accueilli le plus de matchs.

    Les matchs amicaux (`Friendly`) sont exclus : ce ne sont pas un tournoi.

    Paramètres
    ----------
    df : pandas.DataFrame
        Matchs, avec la colonne `tournament`.
    n : int
        Nombre de tournois à afficher.

    Retour
    ------
    matplotlib.figure.Figure
    """
    tournois = df.loc[df['tournament'] != 'Friendly', 'tournament']
    top = tournois.value_counts().head(n).sort_values()

    fig, ax = plt.subplots()
    ax.barh(top.index, top.values, color=sns.color_palette('viridis', len(top)))
    for i, v in enumerate(top.values):
        ax.text(v, i, f' {v}', va='center', fontsize=8)
    ax.set_xlabel('Nombre de matchs')
    ax.set_title(f'Les {n} tournois avec le plus de matchs')
    fig.tight_layout()
    return fig


def plot_teams_most_major(df, major_tournaments, n=15):
    """Les `n` équipes les plus présentes dans les grands tournois.

    Paramètres
    ----------
    df : pandas.DataFrame
        Matchs, avec `tournament`, `home_team`, `away_team`.
    major_tournaments : list[str]
        Liste des tournois considérés comme majeurs.
    n : int
        Nombre d'équipes à afficher.

    Retour
    ------
    matplotlib.figure.Figure
    """
    majeurs = df[df['tournament'].isin(major_tournaments)]
    equipes = pd.concat([majeurs['home_team'], majeurs['away_team']])
    top = equipes.value_counts().head(n).sort_values()

    fig, ax = plt.subplots()
    ax.barh(top.index, top.values, color=sns.color_palette('rocket', len(top)))
    for i, v in enumerate(top.values):
        ax.text(v, i, f' {v}', va='center', fontsize=8)
    ax.set_xlabel('Nombre de matchs en tournois majeurs')
    ax.set_title(f'Les {n} équipes les plus présentes en tournois majeurs')
    fig.tight_layout()
    return fig


def plot_avg_goals_per_decade(df):
    """Nombre moyen de buts par match, par décennie.

    Paramètres
    ----------
    df : pandas.DataFrame
        Matchs, avec les colonnes `decade` et `total_goals`.

    Retour
    ------
    matplotlib.figure.Figure
    """
    moyenne = df.groupby('decade')['total_goals'].mean()

    fig, ax = plt.subplots()
    ax.bar(moyenne.index.astype(str), moyenne.values,
           color=sns.color_palette('crest', len(moyenne)))
    for i, v in enumerate(moyenne.values):
        ax.text(i, v, f'{v:.2f}', ha='center', va='bottom', fontsize=8)
    ax.set_xlabel('Décennie')
    ax.set_ylabel('Buts par match (moyenne)')
    ax.set_title('Nombre moyen de buts par match et par décennie')
    fig.tight_layout()
    return fig


def plot_weekday_evolution(df, year_max=2018):
    """Évolution du pourcentage de matchs joués par jour de la semaine.

    Présente sept petits graphiques (*small multiples*), un par jour de la
    semaine, montrant la part de matchs joués ce jour-là, année par année,
    jusqu'à `year_max` exclu. Le filtre écarte les années marquées par des
    aléas exceptionnels (pandémie de Covid-19) ou non encore complètes.

    Paramètres
    ----------
    df : pandas.DataFrame
        Matchs, avec la colonne `date` (datetime ou convertible).
    year_max : int
        Borne supérieure (exclue) sur l'année.

    Retour
    ------
    matplotlib.figure.Figure
    """
    df = df.copy()
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['dayofweek'] = df['date'].dt.day_name()

    df = df[df['year'] < year_max]
    par_jour = (df.groupby(['year', 'dayofweek']).size()
                  .reset_index(name='n'))
    par_jour['perc'] = par_jour.groupby('year')['n'].transform(
        lambda x: (x / x.sum()) * 100)

    ordre_jours = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                   'Friday', 'Saturday', 'Sunday']
    par_jour['dayofweek'] = pd.Categorical(par_jour['dayofweek'],
                                           categories=ordre_jours,
                                           ordered=True)

    g = sns.relplot(
        data=par_jour, x='year', y='perc',
        col='dayofweek', col_wrap=4,
        hue='dayofweek', kind='line',
        linewidth=2.5, height=3.5, aspect=1.2,
        palette='Set2', legend=False,
    )
    g.set_titles('{col_name}', size=12, fontweight='bold')
    g.set_axis_labels('Année', 'Pourcentage (%)')
    g.fig.suptitle(
        f"Évolution du pourcentage de matchs joués par jour de la "
        f"semaine (< {year_max})",
        y=1.03, fontsize=15, fontweight='bold')
    g.fig.tight_layout()
    return g.fig


def plot_best_win_ratios(df, major_tournaments, n=15, min_matches=30):
    """Les `n` équipes au meilleur ratio de victoires en tournois majeurs.

    Seules les équipes ayant disputé au moins `min_matches` matchs majeurs
    sont retenues, pour écarter les ratios non significatifs.

    Paramètres
    ----------
    df : pandas.DataFrame
        Matchs, avec `tournament`, `home_team`, `away_team`,
        `home_score`, `away_score`.
    major_tournaments : list[str]
        Liste des tournois considérés comme majeurs.
    n : int
        Nombre d'équipes à afficher.
    min_matches : int
        Nombre minimum de matchs majeurs pour être pris en compte.

    Retour
    ------
    matplotlib.figure.Figure
    """
    majeurs = df[df['tournament'].isin(major_tournaments)]

    # Une ligne par participation d'équipe (bp = buts pour, bc = buts contre).
    domicile = majeurs[['home_team', 'home_score', 'away_score']].rename(
        columns={'home_team': 'team', 'home_score': 'bp', 'away_score': 'bc'})
    exterieur = majeurs[['away_team', 'away_score', 'home_score']].rename(
        columns={'away_team': 'team', 'away_score': 'bp', 'home_score': 'bc'})
    participations = pd.concat([domicile, exterieur])
    participations['victoire'] = participations['bp'] > participations['bc']

    stats = participations.groupby('team')['victoire'].agg(['size', 'sum'])
    stats.columns = ['matchs', 'victoires']
    stats = stats[stats['matchs'] >= min_matches]
    stats['ratio'] = stats['victoires'] / stats['matchs']
    top = stats.sort_values('ratio').tail(n)

    fig, ax = plt.subplots()
    ax.barh(top.index, top['ratio'], color=sns.color_palette('flare', len(top)))
    for i, v in enumerate(top['ratio']):
        ax.text(v, i, f' {v:.0%}', va='center', fontsize=8)
    ax.set_xlabel('Ratio de victoires')
    ax.set_title(f'Meilleurs ratios de victoires en tournois majeurs '
                 f'(min. {min_matches} matchs)')
    fig.tight_layout()
    return fig
