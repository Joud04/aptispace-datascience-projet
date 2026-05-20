# Prédiction des résultats de matchs de football internationaux
Étudiant(e) 1 : Joud Atallah, Étudiant(e) 2 : Walid Hdilou, Étudiant(e)
3 : Amine Kaoutar
2026-05-20

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
- [🧠 Étape 5 : Modélisation (Machine Learning & Deep Learning)
  (Squelette
  Étudiant)](#brain-étape-5--modélisation-machine-learning--deep-learning-squelette-étudiant)
- [Évaluation Métrique et Validation](#sec-evaluation)
  - [Chapitre 6 : Travaux Pratiques d’Évaluation &
    Robustesse](#chapitre-6--travaux-pratiques-dévaluation--robustesse)
- [🧪 Étape 6 : Évaluation Métrique & Robustesse (Squelette
  Étudiant)](#test_tube-étape-6--évaluation-métrique--robustesse-squelette-étudiant)
- [Data Storytelling et Communication](#sec-storytelling)
  - [Chapitre 7 : Travaux Pratiques de
    Storytelling](#chapitre-7--travaux-pratiques-de-storytelling)
- [📢 Étape 7 : Data Storytelling & Communication (Squelette
  Étudiant)](#loudspeaker-étape-7--data-storytelling--communication-squelette-étudiant)
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

### 4. Ingénierie de variables (Feature Engineering)

On applique `dc.feature_engineering` pour créer les variables dérivées :
indicateurs temporels (`year`, `decade`), variables de match
(`goal_difference`, `total_goals`), écart de classement FIFA
(`rank_difference`) et la **variable cible** `result` (victoire domicile
/ nul / victoire extérieur).

### 5. Analyse des corrélations

On mesure les liens entre variables numériques avec deux coefficients :
**Pearson** (relations linéaires) et **Spearman** (relations monotones,
plus robuste aux valeurs extrêmes). Le point d’intérêt : l’écart de
classement FIFA (`rank_difference`).

### 6. Matrice de corrélation massive (toutes les variables)

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

### 7. Le classement FIFA prédit-il le résultat ?

On croise l’issue du match avec le fait que l’équipe à domicile soit, ou
non, mieux classée que son adversaire — un premier aperçu du pouvoir
prédictif du classement.

### 8. Synthèse — insights majeurs

À l’issue de l’exploration, cinq constats structurent la suite du projet
:

1.  **Avantage du terrain marqué.** L’équipe à domicile l’emporte dans
    **48,5 %** des matchs (contre 28,1 % pour l’extérieur et 23,3 % de
    nuls). Sur terrain neutre, l’écart de buts se réduit nettement (1,56
    contre 1,35, contre 1,70 contre 1,02 à domicile).

2.  **Le classement FIFA est le signal le plus fort.** Quand l’équipe à
    domicile est mieux classée que son adversaire, elle gagne **64,7 %**
    du temps ; quand elle est moins bien classée, ce taux chute à 31,1 %
    (et elle perd 43,3 % du temps).

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

# 🧠 Étape 5 : Modélisation (Machine Learning & Deep Learning) (Squelette Étudiant)

Cette étape correspond au cinquième chapitre du cours. L’objectif est
d’implémenter d’une part un modèle de Machine Learning tabulaire (ex:
RandomForest) et d’autre part un réseau de neurones convolutif (CNN)
sous TensorFlow pour traiter des images ou signaux complexes.

### 1. Préparation de l’environnement

### 2. Modélisation Tabulaire (Machine Learning)

**À COMPLÉTER PAR L’ÉTUDIANT :** Entraînez un modèle d’apprentissage
supervisé (ex: forêt aléatoire) sur les caractéristiques extraites de
votre jeu de données.

### 3. Modélisation Vision / Deep Learning (CNN & TensorFlow)

**À COMPLÉTER PAR L’ÉTUDIANT :** Pour des motifs complexes
(images/signaux), mettez en place un réseau convolutif (Conv2D, Pooling,
Dense) pour classifier ou enrichir vos prédictions.

------------------------------------------------------------------------

# Évaluation Métrique et Validation

## Chapitre 6 : Travaux Pratiques d’Évaluation & Robustesse

# 🧪 Étape 6 : Évaluation Métrique & Robustesse (Squelette Étudiant)

Cette étape correspond au sixième chapitre du cours. L’objectif est de
mettre en place un protocole d’évaluation rigoureux (splits d’évaluation
adaptés) et de calculer les métriques clés de performance pour valider
scientifiquement la qualité de vos modèles.

### 1. Préparation de l’environnement

### 2. Évaluation du modèle Tabulaire

**À COMPLÉTER PAR L’ÉTUDIANT :** Calculez et interprétez les métriques
d’erreur sur vos prédictions (MAE, RMSE, R²).

### 3. Protocole de Validation Croisée (Out-of-Fold / Chronologique)

**À COMPLÉTER PAR L’ÉTUDIANT :** Décrivez et codez (ou documentez) une
stratégie de validation croisée adaptée au comportement temporel de vos
données pour valider la robustesse de votre modèle sans fuite
d’information.

------------------------------------------------------------------------

# Data Storytelling et Communication

## Chapitre 7 : Travaux Pratiques de Storytelling

# 📢 Étape 7 : Data Storytelling & Communication (Squelette Étudiant)

Cette étape correspond au septième et dernier chapitre de data science.
L’objectif est de synthétiser vos résultats pour des profils métiers ou
décideurs et de proposer des visualisations interactives ou dynamiques
pour valoriser vos conclusions.

### 1. Préparation de l’environnement

### 2. Synthèse métier et Storytelling

**À COMPLÉTER PAR L’ÉTUDIANT :** Traduisez vos métriques techniques en
impacts stratégiques (par exemple, gains financiers, réduction de coûts,
amélioration de la sécurité, etc.).

### 3. Visualisation Interactive (Plotly)

**À COMPLÉTER PAR L’ÉTUDIANT :** Générez un graphique interactif (par
exemple en utilisant Plotly ou des éléments OJS dans le document final)
pour permettre aux décideurs d’interagir dynamiquement avec vos données.

## Présentation des Résultats (Livrables Interactifs)

<div class="panel-tabset">

### 📺 Diaporama de Soutenance (RevealJS)

Ci-dessous est intégré le squelette de votre diaporama de soutenance
RevealJS. Utilisez-le pour présenter votre démarche aux décideurs de
façon professionnelle.

<iframe src="slides.html" width="100%" height="500px" style="border: 1px solid #e2e8f0; border-radius: 8px; background: white;">

</iframe>

### 📊 Exemple de Dashboard Dynamique (OJS / Plotly)

Voici un exemple minimal de code montrant comment intégrer un graphique
dynamique contrôlé par un composant d’interface utilisateur en
Observable JS (OJS).

``` {ojs}
//| echo: true
// Boutons de sélection interactifs OJS
viewof selectedCategory = Inputs.select(["Toutes", "A", "B", "C"], {value: "Toutes", label: "Filtrer par Catégorie :"})
```

``` {ojs}
//| echo: false
// Données simulées réactives
data = [
  {timestamp: "2026-05-18T00:00:00Z", value: 10.5, category: "A"},
  {timestamp: "2026-05-18T02:00:00Z", value: 12.1, category: "A"},
  {timestamp: "2026-05-18T04:00:00Z", value: 14.7, category: "A"},
  {timestamp: "2026-05-18T05:00:00Z", value: 15.2, category: "A"},
  {timestamp: "2026-05-18T06:00:00Z", value: 16.0, category: "B"},
  {timestamp: "2026-05-18T07:00:00Z", value: 18.3, category: "B"},
  {timestamp: "2026-05-18T09:00:00Z", value: 21.5, category: "B"},
  {timestamp: "2026-05-18T10:00:00Z", value: 22.0, category: "B"},
  {timestamp: "2026-05-18T12:00:00Z", value: 25.4, category: "C"},
  {timestamp: "2026-05-18T13:00:00Z", value: 26.1, category: "C"},
  {timestamp: "2026-05-18T15:00:00Z", value: 28.9, category: "C"},
  {timestamp: "2026-05-18T16:00:00Z", value: 30.2, category: "C"}
]

// Filtrage réactif de la donnée
filteredData = selectedCategory === "Toutes" 
  ? data 
  : data.filter(d => d.category === selectedCategory)

// Tracé interactif avec la librairie Plotly
Plotly.newPlot('dynamic-chart', [{
  x: filteredData.map(d => d.timestamp),
  y: filteredData.map(d => d.value),
  type: 'scatter',
  mode: 'lines+markers',
  marker: {color: '#1A73E8', size: 8},
  line: {shape: 'spline', color: '#1A73E8', width: 3}
}], {
  title: 'Évolution Dynamique des Valeurs (Filtrée)',
  margin: {t: 50, b: 50, l: 50, r: 50},
  paper_bgcolor: 'rgba(0,0,0,0)',
  plot_bgcolor: 'rgba(0,0,0,0)',
  xaxis: {gridcolor: '#E5E7EB'},
  yaxis: {gridcolor: '#E5E7EB'}
})
```

<div id="dynamic-chart"
style="width:100%; height:400px; background: white; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">

</div>

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
