"""
Module de nettoyage des données — Projet Fil Rouge Data Science.

Regroupe les fonctions réutilisables des phases de Data Wrangling et d'EDA :
chargement des données, uniformisation des dates, traitement des valeurs
aberrantes, imputation des valeurs manquantes et ingénierie de variables.

Utilisé par les notebooks `02_wrangling`, `03_visualisation` et `04_eda`.
"""
import numpy as np
import pandas as pd


def load_raw_data(path):
    """Charge un fichier CSV dans un DataFrame pandas.

    Paramètres
    ----------
    path : str
        Chemin vers le fichier CSV à charger.

    Retour
    ------
    pandas.DataFrame
        Le contenu du fichier.
    """
    return pd.read_csv(path)


def clean_dates(df, date_col):
    """Convertit une colonne en type datetime puis trie le DataFrame par date.

    Les valeurs non reconnues comme des dates deviennent `NaT` (Not a Time).

    Paramètres
    ----------
    df : pandas.DataFrame
        Le tableau à traiter.
    date_col : str
        Nom de la colonne temporelle à uniformiser.

    Retour
    ------
    pandas.DataFrame
        Copie du tableau, colonne convertie et lignes triées par date croissante.
    """
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    return df.sort_values(date_col).reset_index(drop=True)


def handle_outliers(df, cols, min_val, max_val):
    """Remplace par NaN les valeurs situées hors de l'intervalle plausible.

    Sert à neutraliser les valeurs physiquement impossibles (ex. un score
    négatif) avant l'étape d'imputation.

    Paramètres
    ----------
    df : pandas.DataFrame
        Le tableau à traiter.
    cols : list[str]
        Colonnes numériques à contrôler.
    min_val, max_val : float
        Bornes basse et haute des valeurs plausibles (incluses).

    Retour
    ------
    pandas.DataFrame
        Copie du tableau, valeurs hors bornes mises à NaN.
    """
    df = df.copy()
    for col in cols:
        hors_bornes = (df[col] < min_val) | (df[col] > max_val)
        df.loc[hors_bornes, col] = np.nan
    return df


def impute_missing_values(df, cols, method):
    """Impute (remplit) les valeurs manquantes des colonnes indiquées.

    Paramètres
    ----------
    df : pandas.DataFrame
        Le tableau à traiter.
    cols : list[str]
        Colonnes dont les valeurs manquantes doivent être imputées.
    method : str ou scalaire
        Stratégie d'imputation :
        - 'median', 'mean' : statistique de la colonne (colonnes numériques) ;
        - 'interpolate'    : interpolation linéaire (séries temporelles) ;
        - 'mode'           : valeur la plus fréquente ;
        - toute autre valeur : utilisée telle quelle comme valeur de
          remplissage constante (ex. 0, 220, 'Aucun').

    Retour
    ------
    pandas.DataFrame
        Copie du tableau avec les valeurs manquantes imputées.
    """
    df = df.copy()
    for col in cols:
        if method == 'median':
            df[col] = df[col].fillna(df[col].median())
        elif method == 'mean':
            df[col] = df[col].fillna(df[col].mean())
        elif method == 'interpolate':
            df[col] = df[col].interpolate()
        elif method == 'mode':
            df[col] = df[col].fillna(df[col].mode().iloc[0])
        else:
            # 'method' est interprétée comme une valeur de remplissage constante.
            df[col] = df[col].fillna(method)
    return df


def feature_engineering(df, date_col):
    """Crée des variables dérivées utiles à l'analyse et à la modélisation.

    À partir d'un tableau de matchs nettoyé, ajoute :
    - des variables temporelles : `year`, `month`, `decade` ;
    - des variables de match : `goal_difference`, `total_goals`, `result` ;
    - l'écart de classement FIFA entre les deux équipes : `rank_difference`
      (uniquement si les colonnes de classement sont présentes).

    Paramètres
    ----------
    df : pandas.DataFrame
        Tableau de matchs (colonnes `home_score`, `away_score` ; éventuellement
        `home_rank`, `away_rank`).
    date_col : str
        Nom de la colonne de date.

    Retour
    ------
    pandas.DataFrame
        Copie du tableau enrichie des nouvelles colonnes.
    """
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])

    # Variables temporelles.
    df['year'] = df[date_col].dt.year
    df['month'] = df[date_col].dt.month
    df['decade'] = (df['year'] // 10) * 10

    # Variables de match.
    df['goal_difference'] = df['home_score'] - df['away_score']
    df['total_goals'] = df['home_score'] + df['away_score']

    # Résultat du match, du point de vue de l'équipe à domicile (variable cible).
    conditions = [df['home_score'] > df['away_score'],
                  df['home_score'] < df['away_score']]
    df['result'] = np.select(conditions, ['home_win', 'away_win'], default='draw')
    # Résultat indéterminé pour un match non joué (score absent).
    df.loc[df['home_score'].isna() | df['away_score'].isna(), 'result'] = np.nan

    # Écart de classement FIFA, uniquement si les colonnes sont disponibles
    # (positif = l'équipe à domicile est mieux classée que l'adversaire).
    if {'home_rank', 'away_rank'}.issubset(df.columns):
        df['rank_difference'] = df['away_rank'] - df['home_rank']

    return df
