# Prédiction des résultats de matchs de football internationaux
Étudiant(e) 1 : Joud Atallah, Étudiant(e) 2 : Walid Hdilou, Étudiant(e)
3 : Amine Kaoutar
2026-05-22

- [Introduction et Contexte Métier](#sec-intro)
  - [Contexte du Projet](#contexte-du-projet)
  - [Objectif Analytique](#objectif-analytique)
- [Acquisition et Préparation des Données (Data
  Wrangling)](#sec-wrangling)
  - [Chapitre 1 : Acquisition
    Multi-Sources](#chapitre-1--acquisition-multi-sources)
- [📥 Étape 1 : Acquisition des Données &
  Multi-Sources](#inbox_tray-étape-1--acquisition-des-données--multi-sources)
  - [Chapitre 2 : Nettoyage et Préparation
    (Wrangling)](#chapitre-2--nettoyage-et-préparation-wrangling)
- [🧹 Étape 2 : Préparation & Nettoyage des Données (Data
  Wrangling)](#broom-étape-2--préparation--nettoyage-des-données-data-wrangling)
- [Visualisation Multidimensionnelle (Insights)](#sec-viz)
  - [Chapitre 3 : Travaux Pratiques d’Exploration
    Visuelle](#chapitre-3--travaux-pratiques-dexploration-visuelle)
- [📊 Étape 3 : Visualisation — l’histoire du football
  international](#bar_chart-étape-3--visualisation--lhistoire-du-football-international)
- [Analyse Exploratoire des Données (EDA)](#sec-eda)
  - [Chapitre 4 : Travaux Pratiques d’Exploration
    (EDA)](#chapitre-4--travaux-pratiques-dexploration-eda)
- [🔎 Étape 4 : Analyse Exploratoire des Données
  (EDA)](#mag_right-étape-4--analyse-exploratoire-des-données-eda)
- [Modélisation et Apprentissage](#sec-modelling)
  - [Chapitre 5 : Travaux Pratiques de Modélisation (ML &
    DL)](#chapitre-5--travaux-pratiques-de-modélisation-ml--dl)
- [🧠 Étape 5 : Modélisation — Prédiction du résultat des matchs
  internationaux](#brain-étape-5--modélisation--prédiction-du-résultat-des-matchs-internationaux)
- [Évaluation Métrique et Validation](#sec-evaluation)
  - [Chapitre 6 : Travaux Pratiques d’Évaluation &
    Robustesse](#chapitre-6--travaux-pratiques-dévaluation--robustesse)
- [🧪 Étape 6 : Évaluation et phase à élimination
  directe](#test_tube-étape-6--évaluation-et-phase-à-élimination-directe)
- [Data Storytelling et Communication](#sec-storytelling)
  - [Chapitre 7 : Travaux Pratiques de
    Storytelling](#chapitre-7--travaux-pratiques-de-storytelling)
- [📢 Étape 7 : Data Storytelling et communication des
  résultats](#loudspeaker-étape-7--data-storytelling-et-communication-des-résultats)
  - [Présentation des Résultats (Livrables
    Interactifs)](#présentation-des-résultats-livrables-interactifs)
- [Utilisation de l’Intelligence Artificielle](#sec-ai)
  - [Cartographie de l’utilisation de
    l’IA](#cartographie-de-lutilisation-de-lia)
  - [Principes de Rigueur et
    Responsabilité](#principes-de-rigueur-et-responsabilité)
- [Bibliographie](#bibliographie)

# Introduction et Contexte Métier

Ce projet s’inscrit dans le cadre du Projet Fil Rouge de la formation
Data Science & IA d’IPSSI. L’équipe a choisi de s’attaquer à une
problématique d’actualité : **prédire le résultat des matchs
internationaux de football**, avec en ligne de mire la Coupe du Monde
FIFA 2026 organisée aux États-Unis, au Canada et au Mexique.

## Contexte du Projet

Le football international est un terrain d’application particulièrement
riche pour la Data Science. Les compétitions y sont nombreuses, l’enjeu
économique et médiatique colossal, et les données librement disponibles
couvrent **plus de 150 ans d’histoire** : le premier match international
officiel oppose l’Écosse à l’Angleterre en 1872. Notre dataset principal
recense aujourd’hui plus de **47 000 rencontres** entre sélections
nationales.

Pourtant, prédire l’issue d’un match reste un défi. Niveau intrinsèque
des équipes, dynamique récente, avantage du terrain, enjeu de la
compétition, écart de classement FIFA, contexte historique — autant de
signaux à combiner sans tomber dans le piège de la fuite de données (par
exemple en utilisant une information qui n’existait pas encore au moment
du match).

L’objectif de ce projet est de construire un pipeline de Data Science
**complet et reproductible**, depuis l’acquisition des données jusqu’à
un modèle prédictif rigoureusement évalué. Au-delà de l’exercice
technique, l’enjeu métier est double :

- **expliquer** quels facteurs structurent réellement l’issue d’une
  rencontre internationale ;
- **prédire** les résultats à venir — en particulier ceux des 72 matchs
  programmés de la CDM 2026.

L’analyse quantitative est ici indispensable car l’intuition
footballistique, aussi documentée soit-elle, ne suffit pas à arbitrer
entre des hypothèses contradictoires : le classement FIFA est-il
vraiment un bon prédicteur ? L’avantage à domicile résiste-t-il à l’ère
des matchs en terrain neutre ? Le profil offensif d’une équipe se
transmet-il d’une décennie à l’autre ? Seul un traitement statistique de
l’historique permet de trancher.

## Objectif Analytique

La variable cible est le **résultat du match du point de vue de l’équipe
recevante**, codé en trois modalités : `home_win`, `draw`, `away_win`.
Il s’agit donc d’une tâche de **classification multi-classes**.

Le couplage multi-sources est au cœur de notre démarche. Quatre jeux de
données complémentaires sont fusionnés au sein du notebook
`01_acquisition` :

- les **résultats historiques** (`results.csv`, dataset
  *martj42/international_football_results*) fournissent la trame
  principale — date, équipes, score, tournoi, ville, pays, neutralité du
  terrain ;
- les **classements FIFA mensuels** (1992–2024) ajoutent un signal de
  niveau relatif des équipes, joint temporellement par `pd.merge_asof`
  pour éviter toute fuite ;
- les jeux annexes **`shootouts`** (tirs au but), **`goalscorers`**
  (buteurs) et **`former_names`** (anciens noms d’équipes) enrichissent
  et fiabilisent les jointures sur l’ensemble de l’historique.

Les livrables attendus à l’issue du Jalon 1 (exploration) sont :

1.  un jeu de données **propre, fusionné et historiquement cohérent**
    (`data/processed/matches_clean.csv`, ~30 500 matchs exploitables) ;
2.  un **audit visuel** de l’histoire du football international (volume,
    tournois majeurs, dominantes nationales, intensité offensive, ratios
    de victoire) ;
3.  une **analyse exploratoire** statistique dégageant **cinq insights
    majeurs** qui orienteront la modélisation du Jalon 2.

------------------------------------------------------------------------

# Acquisition et Préparation des Données (Data Wrangling)

Le succès de tout projet de Data Science repose sur la qualité de la
préparation des données ([McKinney 2020](#ref-pandas2020)). Cette
section documente l’audit de qualité et les étapes de nettoyage
appliquées à vos jeux de données bruts.

## Chapitre 1 : Acquisition Multi-Sources

# 📥 Étape 1 : Acquisition des Données & Multi-Sources

Cette étape correspond au premier chapitre du pipeline de Data Science :
identifier, importer et consolider nos jeux de données bruts issus de
différentes sources.

**Projet :** prédire le résultat de matchs de football internationaux,
avec pour objectif final d’estimer le vainqueur de la Coupe du Monde
2026.

**Sources mobilisées :**

| Source | Fichier | Origine |
|----|----|----|
| Résultats des matchs (principale) | `results.csv` | Kaggle — *International football results from 1872* (martj42) |
| Séances de tirs au but | `shootouts.csv` | Kaggle (martj42) |
| Buteurs match par match | `goalscorers.csv` | Kaggle (martj42) |
| Anciens noms de pays | `former_names.csv` | Kaggle (martj42) |
| Classement FIFA historique (1992 → 2024) | `fifa_ranking-2024-06-20.csv` | Kaggle — *FIFA World Ranking* |

> ⚠️ Le classement FIFA est **historisé** : chaque match reçoit le
> classement réellement en vigueur **à sa date**, et non un classement
> actuel. C’est indispensable pour une prédiction fiable — appliquer un
> classement futur à un match passé serait une *fuite de données*.

### 1. Initialisation de l’environnement

### 2. Chargement de la source de données principale

Notre jeu de données principal est `results.csv` : il recense **un match
international par ligne** depuis 1872 (équipes, score, compétition,
ville, pays, terrain neutre). C’est la base de notre futur modèle de
prédiction.

### 3. Intégration de données secondaires (Multi-Sources)

Pour enrichir l’analyse, nous mobilisons **quatre sources
complémentaires**. Les trois premières proviennent du même dataset
Kaggle que les résultats. La quatrième est l’**historique du classement
mondial FIFA** : une ligne = le classement d’une équipe à une date de
publication donnée, depuis 1992.

### 4. Fusion des sources

C’est l’étape clé. Elle enchaîne trois opérations :

1.  **Filtrage temporel** — le classement FIFA n’existe que depuis
    fin 1992. On ne conserve donc que les matchs joués **à partir du
    31/12/1992** (les matchs antérieurs n’ont aucun classement
    disponible).

2.  **Jointure temporelle du classement FIFA** — pour chaque match, on
    récupère le classement **en vigueur à sa date** grâce à
    `pd.merge_asof`, qui associe la dernière publication du classement
    *antérieure ou égale* à la date du match (`direction='backward'`).
    On le fait deux fois : équipe à domicile, puis équipe à l’extérieur.
    ⚠️ Associer un classement *postérieur* au match serait une **fuite
    de données** et fausserait la prédiction.

3.  **Jointure des tirs au but** — au niveau du match (clé : date +
    équipes).

Au passage, on **harmonise les noms d’équipes** : quelques pays sont
orthographiés différemment dans les deux sources (ex. *USA* vs *United
States*, *Czechia* vs *Czech Republic*). On aligne les noms du
classement sur ceux de `results.csv` pour que la jointure fonctionne.

Les buteurs (`goalscorers`) et les anciens noms (`former_names`) sont
chargés mais pas fusionnés ici : ils seront exploités plus tard (analyse
des buts à l’EDA, uniformisation fine des noms au Wrangling).

### 5. Consignation des données consolidées

Nous sauvegardons le tableau consolidé dans `data/processed/`. Il
servira de point d’entrée à l’étape suivante (**02 — Data Wrangling**),
qui se chargera de le nettoyer.

## Chapitre 2 : Nettoyage et Préparation (Wrangling)

# 🧹 Étape 2 : Préparation & Nettoyage des Données (Data Wrangling)

Cette étape correspond au deuxième chapitre du pipeline. L’objectif :
**auditer** la qualité des données issues de l’acquisition, puis les
**nettoyer** rigoureusement à l’aide de notre module
`src/data_clean.py`.

**Donnée d’entrée :** `data/processed/matches_merged.csv` — les 30 583
matchs consolidés à l’étape 1 (résultats + classements FIFA historisés +
tirs au but).

### 1. Initialisation et imports

### 2. Chargement du dataset et audit initial

On charge la sortie de l’étape 1 et on inspecte sa qualité : dimensions,
types des colonnes, doublons et taux de valeurs manquantes.

### 3. Uniformisation des formats de dates

La colonne `date` est chargée comme du texte. On la convertit en type
`datetime` et on trie les matchs par ordre chronologique via
`dc.clean_dates` — indispensable pour les analyses temporelles et le
futur découpage chronologique du modèle.

### 4. Anomalies et matchs non exploitables

Deux contrôles :

- **Validité des scores** — un nombre de buts est un entier positif.
  `dc.handle_outliers` met à `NaN` toute valeur physiquement impossible
  (score négatif ou absurde).
- **Matchs non joués** — 72 rencontres de la Coupe du Monde 2026 sont
  déjà au calendrier mais **n’ont pas encore de score**. Leur résultat
  étant inconnu, on les retire du jeu d’entraînement, mais on les
  **conserve à part** : ce sont précisément les matchs que le modèle
  devra prédire (objectif final du projet).

### 5. Imputation des valeurs manquantes

- **Classements FIFA** — environ 5 % des équipes (sélections non membres
  de la FIFA : Catalogne, Zanzibar…) n’ont pas de classement. On leur
  attribue un rang fictif « non classé » (**220**, au-delà du dernier
  rang réel qui est 211) et **0** point.
- **Tirs au but** — une valeur manquante signifie simplement « pas de
  séance de tirs au but ». On rend cette absence explicite avec la
  valeur `Aucun`.

### 6. Sauvegarde des données propres

On enregistre deux fichiers dans `data/processed/` :

- `matches_clean.csv` — les matchs joués, nettoyés, prêts pour
  l’exploration (étapes 3 et 4) ;
- `matches_a_predire.csv` — les matchs futurs de la CDM 2026, mis de
  côté pour la prédiction finale.

------------------------------------------------------------------------

# Visualisation Multidimensionnelle (Insights)

Nous présentons ici les résultats visuels clés permettant de dégager des
insights exploitables pour les décideurs, en s’appuyant sur notre module
`src/utils_viz.py`.

## Chapitre 3 : Travaux Pratiques d’Exploration Visuelle

# 📊 Étape 3 : Visualisation — l’histoire du football international

Cette étape est consacrée à la visualisation. On explore l’**histoire du
football international** à travers six graphiques, à l’aide de notre
module `src/utils_viz.py`.

**Donnée d’entrée :** `data/raw/results.csv` — l’historique **complet**
des matchs (1872 → 2026). Ces visualisations décrivent l’histoire du
football : elles utilisent toutes les données disponibles, et non la
seule période d’entraînement du modèle (1992+).

### 1. Préparation de l’environnement

### 2. Chargement et préparation

On charge l’historique complet des matchs, on écarte les rencontres non
encore jouées, puis on enrichit le tableau avec `dc.feature_engineering`
(`year`, `decade`, `total_goals`…). On prépare aussi la liste des
**tournois majeurs**.

### 3. Nombre de matchs par année

L’activité footballistique année par année. Les deux guerres mondiales
et la pandémie de Covid-19 ressortent comme des **creux nets** dans le
nombre de matchs.

### 4. Tournois avec le plus de matchs

Les compétitions qui ont accueilli le plus grand nombre de rencontres
dans l’histoire (matchs amicaux exclus : ce ne sont pas un tournoi).

### 5. Équipes les plus présentes en tournois majeurs

Parmi les grands tournois (Coupe du Monde et championnats continentaux),
quelles sélections ont disputé le plus de matchs ?

### 6. Nombre moyen de buts par match et par décennie

Le football est-il devenu plus ou moins offensif au fil des décennies ?

### 7. Meilleurs ratios de victoires en tournois majeurs

Les sélections les plus performantes dans les grands tournois — ratio
victoires / matchs joués —, parmi celles ayant disputé au moins 30
matchs majeurs (seuil qui écarte les ratios non significatifs).

### 8. Évolution du pourcentage de matchs joués par jour de la semaine

Sept *small multiples*, un par jour de la semaine, montrent la part de
matchs disputés ce jour-là année après année, jusqu’à 2018 exclu (on
écarte les années marquées par la pandémie de Covid-19 et celles encore
en cours). On distingue ainsi nettement les jours « traditionnels » du
football international.

------------------------------------------------------------------------

# Analyse Exploratoire des Données (EDA)

Dans cette section, nous analysons les relations statistiques
fondamentales qui régissent votre domaine d’étude au sein du jeu de
données.

## Chapitre 4 : Travaux Pratiques d’Exploration (EDA)

# 🔎 Étape 4 : Analyse Exploratoire des Données (EDA)

Cette étape **clôt le Jalon 1**. L’objectif : explorer et résumer les
propriétés statistiques de nos données, les enrichir par **feature
engineering**, et dégager les **insights majeurs** qui guideront la
modélisation.

**Donnée d’entrée :** `data/processed/matches_clean.csv` — les 30 511
matchs nettoyés (depuis 1992), classements FIFA inclus.

### 1. Préparation de l’environnement

### 2. Chargement des données nettoyées

On charge le jeu de données nettoyé issu de l’étape 2 (Data Wrangling).

### 3. Statistiques descriptives

Résumé statistique global des variables numériques, puis une analyse par
groupe : les buts marqués selon que le match se joue sur terrain neutre
ou non.

### 4. Distribution des variables numériques

Avant de croiser les variables, on examine la **distribution univariée**
de chacune des principales variables numériques (chapitres 4.2.1
*Tendance Centrale* et 4.2.2 *Dispersion* du cours). Pour chaque
variable, l’histogramme est superposé d’une courbe **KDE** (densité
lissée) et de deux lignes verticales : la **moyenne** (rouge) et la
**médiane** (verte).

L’écart entre moyenne et médiane est un indicateur direct de
l’**asymétrie** de la distribution (chapitre 4.2.4, *moyenne vs
médiane*). Pour une distribution symétrique, les deux se confondent.
Pour une distribution **asymétrique à droite** (cas typique des
compteurs de buts : beaucoup de petits scores, quelques scores énormes),
la moyenne est tirée vers les valeurs extrêmes alors que la médiane
reste centrale.

### 5. Ingénierie de variables (Feature Engineering)

On applique `dc.feature_engineering` pour créer les variables dérivées :
indicateurs temporels (`year`, `decade`), variables de match
(`goal_difference`, `total_goals`), écart de classement FIFA
(`rank_difference`) et la **variable cible** `result` (victoire domicile
/ nul / victoire extérieur).

### 6. Distribution de la cible — `result`

La variable cible `result` a trois modalités : `home_win`, `draw`,
`away_win`. Le **count plot** ci-dessous visualise leur fréquence et
confirme un **déséquilibre marqué** : les victoires à domicile dominent
(≈ 48 %), suivies des victoires extérieures (≈ 28 %), les matchs nuls
étant minoritaires (≈ 23 %).

Ce déséquilibre devra être pris en compte au Jalon 2 (par exemple via
`class_weight='balanced'` ou un échantillonnage stratifié).

### 7. Boxplots — dispersion par classe de résultat

Le **boxplot** (chapitre 4.2.2 du cours, *dispersion*) est la façon la
plus directe de comparer la dispersion d’une variable numérique entre
plusieurs groupes. La boîte représente l’**intervalle interquartile**
(IQR : 25ᵉ → 75ᵉ percentile), la barre centrale la **médiane**, et les
points isolés les **outliers**.

On compare ici la dispersion de `goal_difference` (écart de buts) et
`total_goals` (intensité offensive du match) selon le résultat. On
s’attend à voir un `goal_difference` très négatif pour les victoires
extérieures, très positif pour les victoires à domicile, et serré autour
de 0 pour les nuls.

### 8. Analyse des corrélations

On mesure les liens entre variables numériques avec deux coefficients :
**Pearson** (relations linéaires) et **Spearman** (relations monotones,
plus robuste aux valeurs extrêmes). Le point d’intérêt : l’écart de
classement FIFA (`rank_difference`). *Couvre §4.3.2 du cours.*

### 9. Pairplot — vision globale des relations

Le `pairplot` (chapitre 4.3.1 du cours) est l’outil classique pour
visualiser **toutes les relations bivariées** entre quelques variables
clés, avec la distribution univariée sur la diagonale. Ici, on colore
chaque point par le **résultat du match** : on voit immédiatement les
zones où chaque classe (`home_win`, `away_win`, `draw`) se concentre.

On échantillonne **2 000 matchs aléatoires** : le pairplot complet sur
30 511 points serait très lent à rendre et illisible.

### 10. Matrice de corrélation massive (toutes les variables)

Pour aller plus loin que les seules variables numériques de la section
précédente, on encode **toutes** les variables qualitatives (texte,
booléen, catégorie) en codes catégoriels
(`.astype('category').cat.codes`), puis on calcule la matrice de
corrélation complète. La heatmap met ainsi en lumière les éventuelles
structures cachées impliquant `home_team`, `away_team`, `tournament`,
`city`, `country`, `result`, etc.

⚠️ Les codes catégoriels sont arbitraires (ordre alphabétique des
modalités). Les coefficients impliquant ces variables encodées signalent
des **dépendances éventuelles**, pas une relation linéaire interprétable
— à manipuler avec précaution.

### 11. Le classement FIFA prédit-il le résultat ?

On croise l’issue du match avec le fait que l’équipe à domicile soit, ou
non, mieux classée que son adversaire — un premier aperçu du pouvoir
prédictif du classement. C’est un cas typique de *split-apply-combine*
(chapitre 4.4.1 du cours).

### 12. Pivot table — taux de victoire croisé

Au-delà du simple `groupby`, le **pivot table** (chapitre 4.4.2 du
cours) permet de croiser deux dimensions et de visualiser l’effet
conjoint sur une troisième. Ici, on croise :

- **lignes** : `tournoi_majeur` (Coupe du Monde / continentaux /
  Confederations Cup, ou autre) ;
- **colonnes** : `neutral` (terrain neutre ou non) ;
- **cellules** : taux de victoire à domicile (%).

C’est la façon la plus directe de confirmer que l’**avantage à domicile
disparaît effectivement sur terrain neutre**, et de voir si la nature du
tournoi joue un rôle indépendant.

### 13. Binning — taux de victoire par classe d’écart de classement

Au-delà du simple binaire « mieux classé / moins bien classé » étudié en
section 11, on découpe `rank_difference` en **5 classes** via `pd.cut`
(chapitre 4.4.3 du cours, *binning / discrétisation*). Le bar plot
révèle une **progression monotone** du taux de victoire à domicile en
fonction de l’écart de classement — un signal très exploitable pour la
modélisation au Jalon 2.

### 14. Synthèse — insights majeurs

À l’issue de l’exploration, cinq constats structurent la suite du projet
:

1.  **Avantage du terrain marqué.** L’équipe à domicile l’emporte dans
    **48,5 %** des matchs (contre 28,1 % pour l’extérieur et 23,3 % de
    nuls). Sur terrain neutre, l’écart de buts se réduit nettement (1,56
    contre 1,35, contre 1,70 contre 1,02 à domicile).

2.  **Le classement FIFA est le signal le plus fort.** Quand l’équipe à
    domicile est mieux classée que son adversaire, elle gagne **64,7 %**
    du temps ; quand elle est moins bien classée, ce taux chute à 31,1 %
    (et elle perd 43,3 % du temps). Le binning par classes d’écart
    confirme une progression nettement monotone.

3.  **L’écart de classement est corrélé à l’écart de buts** (Pearson
    0,47, Spearman 0,48) : plus le fossé de classement est grand, plus
    la victoire tend à être large.

4.  **Cible à trois classes déséquilibrée** : les victoires à domicile
    dominent. Ce déséquilibre devra être pris en compte lors de la
    modélisation (classe majoritaire).

5.  **Pas de tendance temporelle** : les corrélations avec l’année sont
    quasi nulles (≈ 0) → l’année n’apportera pas d’information
    prédictive.

➡️ Ces constats orientent le Jalon 2 : le **classement FIFA** et
l’**avantage du terrain** seront les variables clés du futur modèle de
prédiction.

------------------------------------------------------------------------

# Modélisation et Apprentissage

Le pipeline complet intègre à la fois la branche analytique tabulaire
(Machine Learning) et la branche d’analyse visuelle ou de signaux
complexes (Deep Learning CNN) :

``` mermaid
graph TD
    A[Données Brutes Multi-Sources CSV/API] -->|Formatage & Alignement| B(data_clean.clean_dates)
    C[Données Externes Complémentaires] -->|Imputation & Interpolation| D(data_clean.impute_missing_values)
    B & D -->|Gestion Outliers| E[Jeu de données Propre & Fusionné]
    E -->|Extraction Temporelle/Caractéristiques| F[Feature Engineering]
    F -->|Splits Temporels ou Stratifiés| G[Modèle Machine Learning Tabulaire]
    H[Flux Multimédias Réels Images/Signaux] -->|Prétraitement d'images/signaux| I[Réseau Convolutif CNN TensorFlow]
    G -->|Prédictions de la Problématique Métier| J[Livrables & Aide à la Décision]
    I -->|Détection de Motifs Complexes| J
    
    style E fill:#e0f2fe,stroke:#0284c7,stroke-width:2px
    style J fill:#f0fdf4,stroke:#16a34a,stroke-width:2px
    style G fill:#fef3c7,stroke:#d97706,stroke-width:2px
    style I fill:#fef3c7,stroke:#d97706,stroke-width:2px
```

## Chapitre 5 : Travaux Pratiques de Modélisation (ML & DL)

# 🧠 Étape 5 : Modélisation — Prédiction du résultat des matchs internationaux

Cette étape est le cœur du **Jalon 2**. On entraîne deux modèles
d’apprentissage supervisé pour prédire l’issue d’un match (`home_win` /
`draw` / `away_win`), avec en ligne de mire la **Coupe du Monde FIFA
2026**.

**Donnée d’entrée :** `data/processed/matches_clean.csv` — 30 511 matchs
nettoyés (1993 → mars 2026), classements FIFA inclus.

**Approche — alignée sur le chapitre 5 du cours :**

- Tâche : **classification multi-classes** sur données tabulaires (§5.2
  du cours).
- Deux modèles, exactement ceux que le cours implémente en Python :
  - **Random Forest** — méthode d’ensemble par *Bagging* (§5.6.1) ;
  - **XGBoost** — méthode d’ensemble par *Boosting* (§5.6.2).
- Concepts clés (§5.7) mobilisés : compromis biais-variance,
  sur-ajustement, importance d’une baseline.

**Deux apports de cette version :**

1.  un *feature engineering* enrichi — on reconstruit l’**historique
    réel de chaque équipe** (buts marqués/encaissés, forme récente,
    force des adversaires) ;
2.  une **analyse par groupe** — on applique le modèle aux 72 matchs de
    la phase de groupes de la CDM 2026 et on dresse le **classement des
    12 groupes**.

### 1. Préparation de l’environnement

### 2. Feature engineering — l’historique de chaque équipe

Le classement FIFA seul est une photo figée : il ne dit rien de la
**dynamique** d’une équipe (attaque prolifique ? défense fragile ? bonne
forme récente ?). On reconstruit donc, pour chaque match, le passé de
chaque équipe.

**Méthode — table « longue ».** Chaque match est dédoublé en deux lignes
(une par équipe), pour suivre chaque sélection comme un fil
chronologique :

| Variable construite | Signification |
|----|----|
| `goals` / `goals_suf` | buts marqués / encaissés par l’équipe ce match-là |
| `game_points` | points du match (3 victoire / 1 nul / 0 défaite) |
| `game_points_rank` | points **pondérés par la force de l’adversaire** : battre le 1ᵉʳ mondial vaut bien plus que battre le 200ᵉ |

⚠️ **Anti-fuite de données.** Toutes les moyennes seront **décalées d’un
match** (`.shift(1)`) : un match ne « voit » jamais son propre résultat,
uniquement ceux qui le précèdent.

#### Moyennes glissantes par équipe

Pour chaque équipe, triée dans l’ordre chronologique, on calcule deux
types de moyennes — toujours **décalées d’un match** :

- **moyenne sur tout le passé** (`expanding`) → le niveau de fond de
  l’équipe ;
- **moyenne sur les 5 derniers matchs** (`_l5`, *rolling*) → la **forme
  récente**.

On obtient ainsi, pour chaque équipe : buts marqués (`goals_mean`), buts
encaissés (`goals_suf_mean`), rang moyen des adversaires affrontés
(`rank_mean`, une mesure de la difficulté du calendrier) et points
pondérés (`game_points_rank_mean`).

### 3. Variables différentielles (`create_db`) et cible

Un modèle prédit mieux à partir d’**écarts** entre les deux équipes qu’à
partir de valeurs absolues. On dérive donc, pour chaque indicateur, la
différence domicile − extérieur — c’est la logique de la fonction
`create_db` du notebook Kaggle de référence.

**12 variables explicatives finales :**

| Variable | Sens |
|----|----|
| `rank_dif` | écart de classement FIFA actuel |
| `goals_dif` / `goals_dif_l5` | écart d’attaque (global / forme récente) |
| `goals_suf_dif` / `goals_suf_dif_l5` | écart de fragilité défensive |
| `goals_per_ranking_dif` | efficacité offensive corrigée de la force du calendrier |
| `dif_rank_agst` / `dif_rank_agst_l5` | écart de difficulté des adversaires affrontés |
| `dif_points_rank` / `dif_points_rank_l5` | écart de performance pondérée par la force adverse |
| `is_friendly_0` / `is_friendly_1` | match amical ou enjeu réel (one-hot) |

La **cible** `result` est déduite directement des scores
(`0 = away_win`, `1 = draw`, `2 = home_win`). Les scores eux-mêmes
(`home_score`, `away_score`) ne sont **jamais** donnés au modèle : ce
serait une fuite de données évidente.

#### Séparation entraînement / test

On encode la cible numériquement puis on réalise un **split stratifié
80/20** (les proportions de classes sont conservées dans les deux jeux).
Le jeu de test ne sera utilisé qu’à la toute fin, pour mesurer la
capacité de **généralisation** des modèles (§5.7 du cours).

### 4. Baseline naïve

Avant tout modèle ML, on établit la performance d’un **prédicteur
trivial** qui prédit toujours la classe majoritaire (`home_win`). C’est
la référence à battre : sans elle, impossible de savoir si un modèle
apprend réellement quelque chose (cf. §5.7 du cours).

### 5. Modèle 1 — Random Forest (§5.6.1 du cours, *Bagging*)

> *« Le Bagging consiste à entraîner de nombreux modèles de manière
> indépendante et en parallèle sur des sous-ensembles aléatoires de vos
> données. C’est un jury d’assises. \[…\] La Forêt Aléatoire crée des
> centaines d’arbres de décision. Force : très robuste contre le
> sur-ajustement. »*

On instancie exactement comme le cours, en ajustant `n_estimators` et
`max_depth` pour notre volume de données. `class_weight='balanced'`
compense le déséquilibre des classes observé en EDA.

### 6. Modèle 2 — XGBoost (§5.6.2 du cours, *Boosting*)

> *« Le Boosting fonctionne de manière séquentielle. Chaque nouvel arbre
> est construit spécifiquement pour corriger les erreurs (les résidus)
> des précédents. XGBoost : le standard industriel, ultra-optimisé et
> régularisé. »*

On instancie `XGBClassifier` exactement comme dans le cours
(`n_estimators=100, learning_rate=0.1`). XGBoost gère nativement les
cibles multi-classes.

### 7. Comparaison des modèles + matrice de confusion

On compare les deux modèles sur le jeu de **test** (jamais vu pendant
l’entraînement), et on visualise la **matrice de confusion** du meilleur
d’entre eux pour identifier ses erreurs typiques — en particulier sur
les matchs nuls, la classe minoritaire.

### 8. Importance des variables

Le Random Forest expose nativement l’**importance de chaque variable**
(importance de Gini). On vérifie ainsi quelles caractéristiques pèsent
réellement dans la décision : les variables d’historique enrichi (buts,
points pondérés) apportent-elles plus que le simple classement ?

### 9. Prédiction des 72 matchs de la phase de groupes (CDM 2026)

On applique le meilleur modèle aux **72 matchs programmés de la phase de
groupes** (`data/processed/matches_a_predire.csv`) — soit les 48 équipes
réparties en 12 groupes de 4.

Pour chaque équipe, on calcule sa **forme actuelle** : les mêmes
moyennes (buts, points pondérés, force du calendrier) mais cette fois
sur **l’intégralité** de son historique connu, jusqu’à mars 2026. On
reconstruit les 12 variables différentielles, puis on prédit l’issue de
chaque match ainsi que les **probabilités** des trois résultats
possibles.

### 10. Classement des 12 groupes — qui sort de sa poule ?

On reconstitue maintenant le **classement de chaque groupe** à partir
des prédictions. La répartition officielle des 48 équipes (tirage du 5
décembre 2025) est fournie par le module `src/wc2026.py`.

**Comment on classe les équipes ?** Comme dans un vrai classement de
football : **par points** (3 victoire / 1 nul / 0 défaite), à partir des
6 matchs internes au groupe.

Problème : le modèle prédit très rarement le match nul, donc beaucoup
d’équipes terminent **à égalité de points**. On les départage avec les
**points espérés** (`xPts`) :

$$xPts = \sum_{\text{3 matchs}} \big( 3 \times P(\text{victoire}) + 1 \times P(\text{nul}) \big)$$

C’est l’**espérance mathématique** du nombre de points, compte tenu des
probabilités du modèle. `xPts` joue ici le rôle que tient la différence
de buts dans un vrai classement — un critère fin que notre modèle (qui
prédit une *issue*, pas un *score*) ne peut pas fournir directement.

**Format CDM 2026 :** les **2 premiers** de chaque groupe + les **8
meilleurs 3ᵉˢ** se qualifient → 32 équipes pour les 16ᵉˢ de finale.
C’est cette liste qui servira de point de départ au notebook 06.

#### Vainqueurs de groupe et équipes qualifiées

### 11. Synthèse — modélisation

1.  **Les deux modèles battent largement la baseline naïve** (~48.5 %) :
    le *feature engineering* enrichi (historique de buts, forme récente,
    force du calendrier) apporte un vrai signal prédictif.
2.  **Le passage du classement FIFA seul aux 12 variables
    différentielles fait progresser la précision de test** — voir le
    tableau récapitulatif du §7. Les variables d’historique
    (`dif_points_rank`, `goals_per_ranking_dif`, `goals_suf_dif`)
    figurent en tête de l’importance, aux côtés du `rank_dif`.
3.  **Random Forest et XGBoost** restent au coude-à-coude, conformément
    à la littérature sur les données tabulaires (§5.1 du cours : *les
    arbres dominent encore le tabulaire face au Deep Learning*).
4.  **Phase de groupes CDM 2026** : les 72 matchs sont prédits, puis
    agrégés en **classement des 12 groupes** via les points espérés
    (`xPts`). On en déduit les 12 vainqueurs de groupe et les **32
    équipes qualifiées** pour les 16ᵉˢ de finale.
5.  **Limites identifiées** : la classe `draw` reste sous-prédite
    (matchs nuls intrinsèquement difficiles) ; chaque match est prédit
    indépendamment.

➡️ Le notebook suivant (`06_evaluation`) approfondira l’évaluation
(validation croisée temporelle, métriques par classe) puis exploitera la
liste des 32 qualifiés pour **simuler la phase à élimination directe**
et désigner le vainqueur de la Coupe du Monde.

------------------------------------------------------------------------

# Évaluation Métrique et Validation

Au-delà de l’*accuracy* — que le cours qualifie de « métrique de vanité
» — le modèle est évalué avec la batterie d’indicateurs adaptés aux
classes déséquilibrées : matrice de confusion, précision, rappel,
F1-score et ROC-AUC. Les hyperparamètres sont ensuite optimisés par
recherche aléatoire en validation croisée. Le modèle ainsi validé est
enfin appliqué au **bracket officiel de la phase à élimination directe**
: la simulation des 16ᵉˢ de finale jusqu’à la finale, complétée par une
validation sur 20 000 simulations du tournoi, désigne le **champion du
monde 2026 prédit** et quantifie l’incertitude de la compétition.

## Chapitre 6 : Travaux Pratiques d’Évaluation & Robustesse

# 🧪 Étape 6 : Évaluation et phase à élimination directe

Sixième étape du pipeline, alignée sur le **chapitre 6 du cours** («
Évaluation des Modèles »). Elle poursuit deux objectifs :

1.  **Évaluer rigoureusement** le modèle du notebook 05 — au-delà de la
    simple *accuracy*, avec les métriques que le cours juge
    indispensables : matrice de confusion, précision, rappel, F1-score,
    ROC-AUC (§6.1), puis optimisation des hyperparamètres (§6.2).
2.  **Simuler la phase à élimination directe** de la Coupe du Monde 2026
    — appliquer le modèle évalué au bracket officiel (16ᵉˢ de finale →
    finale) pour répondre à la question finale du projet : **qui sera
    champion du monde ?**

**Données d’entrée :** `matches_clean.csv` (entraînement) et
`cdm2026_qualifies.csv` — les 32 équipes qualifiées produites par le
notebook 05.

### 1. Préparation de l’environnement

### 2. Reprise du modèle du notebook 05

On reconstruit ici le **meilleur modèle du notebook 05** (XGBoost) : on
recharge les 30 511 matchs, on réapplique le *feature engineering*
enrichi (historique de chaque équipe : buts, forme récente, force des
adversaires → 12 variables différentielles), puis on ré-entraîne XGBoost
sur le **même split stratifié 80/20** pour garantir la cohérence avec le
notebook précédent.

### 3. Évaluation approfondie du modèle (§6.1 du cours)

> *« En 2026, l’industrie a enfin compris que l’Accuracy est souvent une
> métrique de vanité. »* — chapitre 6 du cours.

L’accuracy seule ne suffit pas, surtout sur des **classes
déséquilibrées** (ici `home_win` 48 %, `away_win` 28 %, `draw` 23 %). On
mobilise donc la batterie de métriques du cours :

- **Matrice de confusion** — le « bilan sanguin » du modèle : où se
  trompe-t-il ?
- **Précision** (sur mes alertes, combien sont vraies ?) et **Rappel**
  (sur les cas réels, combien j’en capture ?), par classe.
- **F1-score** — moyenne harmonique précision/rappel, indispensable en
  classes déséquilibrées.
- **ROC-AUC** — capacité du modèle à séparer les classes (1.0 = parfait,
  0.5 = hasard).

### 4. Optimisation des hyperparamètres (§6.2 du cours)

Les hyperparamètres (`n_estimators`, `max_depth`, `learning_rate`…) ne
sont pas appris par le modèle : on les règle nous-mêmes. Le cours
présente trois approches : **Grid Search**, **Random Search**, et
l’**optimisation bayésienne** (Optuna, devenu le standard 2026).

On applique ici un **Random Search** via `RandomizedSearchCV` de
scikit-learn : il échantillonne des combinaisons au hasard et les évalue
en **validation croisée 3 plis**. Plus rapide qu’un Grid Search
exhaustif, sans dépendance supplémentaire.

> 💡 *Le cours recommande Optuna (algorithme TPE) pour les projets de
> production : il « apprend » de ses essais précédents au lieu de
> chercher à l’aveugle. Random Search reste suffisant pour notre volume
> de données.*

### 5. Phase à élimination directe — qui sera champion du monde ?

On applique maintenant le modèle au **bracket officiel de la CDM 2026**
(source : Wikipédia, *2026 FIFA World Cup knockout stage*), encodé dans
`src/wc2026.py` : 16ᵉˢ de finale (32 équipes) → 8ᵉˢ → quarts → demies →
**finale**.

**Trois principes de simulation :**

1.  **Neutralisation de l’avantage du terrain.** En phase finale, les
    matchs sont sur terrain neutre. Comme le modèle a appris un fort
    avantage à domicile, on prédit chaque match **dans les deux sens**
    (A reçoit B, puis B reçoit A) et on **moyenne** les probabilités.
    L’asymétrie domicile/extérieur s’annule.
2.  **Pas de match nul possible.** Un match à élimination directe a
    forcément un vainqueur : la probabilité de nul est redistribuée, et
    l’équipe la plus probable se qualifie (le nul correspondrait à une
    qualification aux tirs au but, qui favorise statistiquement le
    favori).
3.  **Affectation des 8 troisièmes.** La FIFA place les 8 meilleurs 3ᵉˢ
    via une table de combinaisons. On calcule une **affectation valide**
    respectant les contraintes d’éligibilité de chaque match des 16ᵉˢ.

#### 5.1 Simulation déterministe du bracket

À chaque tour, on fait avancer l’équipe la **plus probable**. On déroule
ainsi les 16ᵉˢ jusqu’à la finale.

#### Le parcours du champion

#### 5.2 Robustesse — probabilités de titre par simulation répétée

La simulation déterministe désigne un seul champion, mais elle ignore
les **surprises** (un favori à 60 % perd tout de même 4 fois sur 10).
Pour mesurer la **robustesse** de la prédiction, on rejoue le tournoi
**un grand nombre de fois** : à chaque match, le vainqueur est tiré au
hasard selon sa probabilité. La fréquence de victoire finale de chaque
équipe donne sa **probabilité de titre**.

### 6. Synthèse — évaluation et prédiction finale

1.  **Au-delà de l’accuracy** (§6.1 du cours) : la matrice de confusion
    et le F1-score confirment un modèle solide sur `home_win` /
    `away_win` mais quasi aveugle sur les matchs nuls (`draw`) — limite
    intrinsèque, le nul étant peu prévisible.
2.  **Optimisation des hyperparamètres** (§6.2) : le Random Search en
    validation croisée 3 plis n’apporte qu’un gain marginal — le modèle
    de base XGBoost était déjà bien réglé.
3.  **Phase à élimination directe** : en appliquant le modèle au bracket
    officiel (avantage du terrain neutralisé), on simule l’intégralité
    du tournoi des 16ᵉˢ de finale jusqu’à la finale.
4.  **Prédiction finale** : le modèle désigne un **champion du monde
    2026** ; la validation par **20 000 simulations** du tournoi
    confirme qu’il s’agit du favori le plus probable, tout en
    quantifiant l’incertitude réelle de la compétition.
5.  **Limites** : pas de gestion des blessures, suspensions ni dynamique
    de tournoi ; le modèle reste une estimation probabiliste — le
    football garde sa part d’imprévu.

➡️ Le notebook `07_communication` restituera ces résultats sous forme de
*data storytelling* à destination d’un public non technique.

------------------------------------------------------------------------

# Data Storytelling et Communication

Un modèle qui ne convainc pas n’a aucune valeur. Cette dernière étape
**traduit** les résultats techniques en un récit clair pour un public
non spécialiste : structuration du message selon les frameworks SCQA et
de la pyramide de Minto (la réponse d’abord), traduction des métriques
en langage courant, et surtout communication **honnête de
l’incertitude** — la prédiction finale est annoncée non comme une
certitude, mais comme une probabilité assumée.

## Chapitre 7 : Travaux Pratiques de Storytelling

# 📢 Étape 7 : Data Storytelling et communication des résultats

Dernière étape du cycle de la donnée, alignée sur le **chapitre 7 du
cours** (« Communication des Résultats »). Un modèle, aussi performant
soit-il, ne vaut rien s’il ne convainc pas : *« un modèle parfait qui ne
convainc pas le comité de direction est un modèle mort »* (cours, §7.1).

Cette étape **traduit** les résultats techniques des notebooks 05 et 06
en un récit clair, destiné à un public non technique (médias sportifs,
supporters, décideurs d’une fédération). On mobilise les outils du cours
:

- le framework **SCQA** (Situation, Complication, Question, Answer) et
  la **pyramide de Minto** (la réponse d’abord) pour structurer le récit
  ;
- le framework **O.I.A.** (Observation → Insight → Action) pour que
  chaque résultat réponde à la question *« So what ? »* ;
- une communication **honnête de l’incertitude** (§7.3) — la marque d’un
  expert, pas d’un devin.

### 1. Préparation de l’environnement

### 2. Reprise des résultats des notebooks 05 et 06

On recharge les livrables produits par les étapes précédentes du
pipeline :

- `cdm2026_qualifies.csv` — les 32 équipes qualifiées et le classement
  des 12 groupes (notebook 05) ;
- `cdm2026_podium.csv` — le podium issu de la simulation déterministe du
  bracket (notebook 06) ;
- `cdm2026_titres.csv` — la **probabilité de titre** de chaque équipe,
  estimée en rejouant le tournoi 20 000 fois (notebook 06).

### 3. Le récit — structurer le message (SCQA + pyramide de Minto)

> **La réponse d’abord.** La pyramide de Minto impose de donner la
> conclusion *avant* les détails. Voici donc, en une phrase :

> ## 🏆 Le Brésil est le grand favori de la Coupe du Monde 2026.

Le récit complet, structuré selon le framework **SCQA** du cours :

| Étape | Le récit |
|----|----|
| **S — Situation** | La Coupe du Monde 2026 réunit 48 équipes dans un format inédit (12 groupes, 104 matchs). Notre projet a construit un modèle d’apprentissage automatique entraîné sur **plus de 30 000 matchs internationaux** (1993 → 2026). |
| **C — Complication** | Prédire un tournoi à élimination directe est un défi : l’aléa du football, l’avantage du terrain à neutraliser, et 104 matchs où la moindre surprise change tout. |
| **Q — Question** | Peut-on désigner un favori **crédible** et, surtout, **quantifier honnêtement** sa probabilité de soulever le trophée ? |
| **A — Answer** | Oui. Le modèle XGBoost simule l’intégralité du tournoi : il désigne le **Brésil** comme favori — mais dans une compétition qui reste très ouverte. |

#### Traduire la technique en langage clair (le « dictionnaire du Data Translator »)

Le cours insiste : on ne présente jamais une métrique brute à un
non-spécialiste, on la **traduit**.

| Métrique technique | Traduction pour le grand public |
|----|----|
| Accuracy = 0.588 | Le modèle voit juste **environ 3 fois sur 5** — là où parier systématiquement sur l’équipe à domicile ne réussit que dans 48 % des cas. |
| ROC-AUC = 0.730 | Le modèle **sépare nettement** les équipes qui vont gagner de celles qui vont perdre (0.5 = pile ou face, 1.0 = parfait). |
| Probabilité de titre = 23 % | Si l’on rejouait la Coupe du Monde 100 fois, le Brésil la gagnerait environ **23 fois** — favori net, mais loin d’une certitude. |

### 4. Visualisations pour la restitution

#### 4.1 Le grand favori — probabilités de titre

La visualisation centrale du projet : la probabilité, pour chaque
nation, de remporter la Coupe du Monde 2026 (issue de 20 000 simulations
du tournoi).

#### 4.2 Le podium prédit et les 12 vainqueurs de groupe

#### 4.3 Un tableau de bord interactif pour la restitution

Le cours (§7.2) rappelle qu’*« en 2026, fournir un rapport PDF statique
à un décideur n’est plus suffisant »*. Les graphiques ci-dessus,
parfaits pour un rapport écrit, gagnent à être déclinés en **tableau de
bord interactif** permettant le *drill-down* : survol pour lire une
valeur, filtrage par tour, navigation par thème.

C’est l’objet du livrable `dashboard.html`. Construit avec **Plotly**
(la bibliothèque de graphiques web interactifs recommandée par le
cours), il s’agit d’un **tableau de bord autonome** — un fichier HTML
unique, ouvrable dans n’importe quel navigateur, sans installation ni
serveur. Il organise les résultats du projet en **six vues** accessibles
depuis une barre latérale :

- **Vue d’ensemble** — course au titre, probabilité du champion et part
  d’incertitude ;
- **Jeu de données** — volume de matchs, buts par décennie, répartition
  des résultats et poids de l’écart de classement FIFA ;
- **Modèle** — comparaison Baseline / Random Forest / XGBoost, variables
  influentes, classes mal détectées ;
- **Phase finale** — bracket simulé des 16ᵉˢ à la finale, filtrable par
  tour, et podium projeté ;
- **Équipes** — probabilités de titre et meilleurs vainqueurs de groupe
  (xPts) ;
- **Décision** — trois messages clés et récapitulatif des indicateurs.

Tous les chiffres affichés sont chargés depuis les fichiers produits par
les notebooks 05 et 06 (`cdm2026_qualifies.csv`, `cdm2026_titres.csv`,
`cdm2026_podium.csv`) : le tableau de bord est donc strictement cohérent
avec ce rapport. Il constitue le **livrable de communication** du
projet, au-delà du rapport PDF.

### 5. Transparence et communication de l’incertitude (§7.3 du cours)

> *« Un dirigeant préférera toujours un expert qui maîtrise ses marges
> d’erreur plutôt qu’un devin qui se trompe avec aplomb. »* — chapitre 7
> du cours.

Annoncer « le Brésil sera champion » serait une **faute de
communication**. Le résultat honnête est probabiliste : le Brésil est
favori **avec 23 % de chances** — ce qui signifie qu’il échouerait plus
de **3 fois sur 4**. Le graphique ci-dessous montre à quel point le
tournoi reste ouvert.

#### Les deux visages de l’incertitude, et les limites du modèle

Le cours distingue deux incertitudes — utile pour expliquer *pourquoi*
la prédiction n’est pas une certitude :

- **Incertitude aléatoire** (irréductible) : le football est
  imprévisible par nature — un poteau, un carton rouge, un exploit
  individuel. Aucune donnée ne supprimera jamais cette part de hasard.
- **Incertitude épistémique** (réductible) : elle vient des **limites de
  notre modèle**, et *peut* être réduite :
  - le modèle ignore les **compositions d’équipe** (blessures,
    suspensions, forme des joueurs clés) ;
  - il prédit une **issue** (victoire/nul/défaite), pas un score, ni la
    dynamique d’un tournoi ;
  - il ne sait quasiment pas prévoir les **matchs nuls** (rappel ≈ 3 %,
    vu au notebook 06) ;
  - les **données récentes** (amicaux 2025-2026, qualifications) pèsent
    autant qu’un match de 1995.

**Pistes d’amélioration** (réduction de l’incertitude épistémique) :
intégrer les effectifs réels, pondérer les matchs par leur ancienneté,
ajouter des données de performance des joueurs.

### 6. Recommandations et conclusion

En appliquant une dernière fois le framework **O.I.A.** du cours à
l’ensemble du projet :

**🔎 Observation.** À partir de 30 000+ matchs internationaux, un modèle
XGBoost (précision 59 %, ROC-AUC 0.73) a simulé toute la Coupe du Monde
2026, de la phase de groupes à la finale.

**💡 Insight.** Le Brésil ressort favori (**23 % de probabilité de
titre**), devant l’Argentine (14 %) et la France (11 %). Mais aucune
équipe ne dépasse 25 % : **la compétition est ouverte**, et les
variables les plus prédictives sont l’écart de classement FIFA et la
performance récente pondérée par la force des adversaires.

**🎯 Action — recommandations.**

1.  **Pour une rédaction sportive / des supporters** : communiquer le
    Brésil comme favori, *toujours* assorti de sa probabilité (23 %) —
    un récit honnête et engageant, pas une fausse certitude.
2.  **Pour une fédération** : utiliser les probabilités de qualification
    par tour comme outil d’**aide à la préparation** (identifier les
    adversaires probables).
3.  **Pour la suite du projet** : enrichir le **tableau de bord
    interactif** (`dashboard.html`) de nouvelles vues et compléter le
    modèle avec les données d’effectifs pour réduire l’incertitude
    épistémique.

------------------------------------------------------------------------

#### 🌉 Conclusion du projet

Ce notebook clôt le **cycle complet de la donnée** : acquisition →
nettoyage → visualisation → analyse exploratoire → modélisation →
évaluation → **communication**. Parti d’un simple fichier de résultats
de matchs, le projet aboutit à une prédiction chiffrée, évaluée et —
surtout — **honnêtement communiquée** du vainqueur de la Coupe du Monde
2026.

> 🏆 **Prédiction finale : le Brésil, favori de la Coupe du Monde 2026
> (23 % de probabilité de titre).**

## Présentation des Résultats (Livrables Interactifs)

<div class="panel-tabset">

### 📺 Diaporama de Soutenance (RevealJS)

Ci-dessous est intégré le squelette de votre diaporama de soutenance
RevealJS. Utilisez-le pour présenter votre démarche aux décideurs de
façon professionnelle.

<iframe src="slides.html" width="100%" height="500px" style="border: 1px solid #e2e8f0; border-radius: 8px; background: white;">

</iframe>

### 📊 Tableau de bord interactif

Le livrable de restitution du projet est un **tableau de bord autonome**
: `dashboard.html`, un fichier unique ouvrable dans n’importe quel
navigateur, sans installation. Il synthétise l’ensemble du pipeline en
**six vues** que l’on parcourt depuis une barre latérale.

| Vue | Contenu |
|----|----|
| **Vue d’ensemble** | Course au titre, probabilité du champion et part d’incertitude. |
| **Jeu de données** | Volume de matchs, buts par décennie, répartition des résultats, poids de l’écart de classement FIFA. |
| **Modèle** | Comparaison Baseline / Random Forest / XGBoost, variables influentes, classes mal détectées. |
| **Phase finale** | Bracket simulé des 16ᵉˢ à la finale, filtrable par tour, et podium projeté. |
| **Équipes** | Probabilités de titre et meilleurs vainqueurs de groupe (xPts). |
| **Décision** | Trois messages clés et récapitulatif des indicateurs. |

Chaque chiffre du tableau de bord est issu directement des notebooks 05
et 06 : il est donc strictement cohérent avec le présent rapport. Le
favori désigné — le **Brésil, 23,4 % de chance de titre** — y est
présenté comme un scénario probable et non comme une certitude,
conformément à la démarche de communication honnête de l’incertitude.

> **Pour l’explorer :** ouvrir le fichier `dashboard.html` situé à la
> racine du dépôt.

</div>

------------------------------------------------------------------------

# Utilisation de l’Intelligence Artificielle

Dans une démarche de transparence scientifique et académique, cette
section détaille la manière dont les outils d’Intelligence Artificielle
(IA) générative ont été intégrés tout au long de la réalisation de ce
projet.

## Cartographie de l’utilisation de l’IA

| Outil d’IA | Cas d’usage (Pourquoi ?) | Méthode d’utilisation (Comment ?) | Rôle et Validation Humaine |
|:---|:---|:---|:---|
| **\[Outil d’IA\]** | *\[À compléter par les étudiants\]* | *\[À compléter par les étudiants\]* | *\[À compléter par les étudiants\]* |

## Principes de Rigueur et Responsabilité

1.  **Responsabilité intellectuelle** : L’équipe assume l’entière
    responsabilité des analyses, des choix de modèles et des conclusions
    présentées dans ce rapport.
2.  **Lutte contre les hallucinations** : Chaque suggestion technique a
    fait l’objet d’une validation empirique.
3.  **Protection des données** : Aucun jeu de données confidentiel ou
    sensible n’a été soumis à des modèles tiers en ligne.

------------------------------------------------------------------------

# Bibliographie

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-pandas2020" class="csl-entry">

McKinney, Wes. 2020. *Python for Data Analysis: Data Wrangling with
Pandas, NumPy, and IPython*. O’Reilly Media.

</div>

</div>
