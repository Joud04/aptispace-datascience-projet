# Mon Super Projet Data Science
Étudiant(e) 1 : \[Insérer Prénom Nom\], Étudiant(e) 2 : \[Insérer Prénom
Nom\], Étudiant(e) 3 : \[Insérer Prénom Nom\]
2026-05-18

- [Introduction et Contexte Métier](#sec-intro)
  - [Contexte du Projet](#contexte-du-projet)
  - [Objectif Analytique](#objectif-analytique)
- [Acquisition et Préparation des Données (Data
  Wrangling)](#sec-wrangling)
  - [Audit de Qualité](#audit-de-qualité)
  - [Algorithme de Nettoyage](#algorithme-de-nettoyage)
  - [Travaux Pratiques de Wrangling](#travaux-pratiques-de-wrangling)
- [🧹 Jalon 1 : Data Wrangling & Nettoyage (Squelette
  Étudiant)](#broom-jalon-1--data-wrangling--nettoyage-squelette-étudiant)
- [Analyse Exploratoire des Données (EDA)](#sec-eda)
  - [Statistiques Descriptives](#statistiques-descriptives)
  - [Ingénierie de Variables (Feature
    Engineering)](#ingénierie-de-variables-feature-engineering)
  - [Travaux Pratiques d’Exploration Visuelle
    (EDA)](#travaux-pratiques-dexploration-visuelle-eda)
- [📊 Jalon 1 : Analyse Exploratoire des Données (EDA) & Visualisation
  (Squelette
  Étudiant)](#bar_chart-jalon-1--analyse-exploratoire-des-données-eda--visualisation-squelette-étudiant)
- [Visualisation Multidimensionnelle (Insights)](#sec-viz)
  - [Profils d’Activité Journalière](#profils-dactivité-journalière)
  - [Corrélations Globales](#corrélations-globales)
- [Modélisation et Apprentissage](#sec-modelling)
  - [Schéma Global du Pipeline de
    Données](#schéma-global-du-pipeline-de-données)
  - [Modélisation Tabulaire (Prédiction
    Vélos)](#modélisation-tabulaire-prédiction-vélos)
- [🧠 Jalon 2 : Modélisation Prédictive de Trafic (Squelette
  Étudiant)](#brain-jalon-2--modélisation-prédictive-de-trafic-squelette-étudiant)
  - [Modélisation Vision (Analyse
    d’Images)](#modélisation-vision-analyse-dimages)
- [📷 Jalon 2 : Brique de Vision par Ordinateur (CNN & TensorFlow)
  (Squelette
  Étudiant)](#camera-jalon-2--brique-de-vision-par-ordinateur-cnn--tensorflow-squelette-étudiant)
- [Évaluation Métrique et Validation](#sec-evaluation)
  - [Stratégie de Validation
    Chronologique](#stratégie-de-validation-chronologique)
  - [Résultats et Interprétation](#résultats-et-interprétation)
- [Data Storytelling et Communication](#sec-storytelling)
  - [Recommandations pour la
    Métropole](#recommandations-pour-la-métropole)
  - [Limites et Perspectives](#limites-et-perspectives)
- [Bibliographie](#bibliographie)

# Introduction et Contexte Métier

*À rédiger par les étudiants : Présentez ici le contexte global du
projet de transition écologique de la métropole, les enjeux sociétaux de
la mobilité active, les questions scientifiques soulevées et la
problématique métier que vous cherchez à résoudre.*

## Contexte du Projet

*À rédiger par les étudiants — Pistes de réflexion :* - *Quels sont les
objectifs environnementaux globaux de la métropole en matière de
réduction d’empreinte carbone et de pollution ?* - *En quoi la promotion
de la mobilité active (vélo) et des transports en commun (bus)
constitue-t-elle un levier d’action stratégique ?* - *Pourquoi l’analyse
quantitative des données de trafic est-elle indispensable pour piloter
les infrastructures urbaines ?*

\[Rédiger votre paragraphe de contexte ici\]

## Objectif Analytique

*À rédiger par les étudiants — Pistes de réflexion :* - *Quelles sont
les variables cibles principales (ex: bike_count) et la tâche prédictive
globale ?* - *Comment le couplage de données physiques (météo,
pollution, trafic) et d’images (brique de vision CNN) permet-il
d’adopter une approche multi-sources ?* - *Quels sont les livrables
analytiques attendus pour aider la métropole dans ses prises de
décisions stratégiques ?*

\[Rédiger votre paragraphe d’objectifs ici\]

------------------------------------------------------------------------

# Acquisition et Préparation des Données (Data Wrangling)

Le succès de tout projet de Data Science repose sur la qualité de la
préparation des données ([McKinney 2020](#ref-pandas2020)). Cette
section documente l’audit de qualité et les étapes de nettoyage
appliquées au jeu de données de capteurs brut.

## Audit de Qualité

*À rédiger par les étudiants : Présentez un audit critique complet du
fichier de données brutes. Indiquez la liste des anomalies physiques et
typologiques détectées (formats de dates, outliers physiques, taux de
valeurs manquantes).*

\[Rédiger votre audit de données ici\]

## Algorithme de Nettoyage

*À rédiger par les étudiants : Justifiez et détaillez l’enchaînement de
vos opérations de traitement (uniformisation des dates, masquage des
outliers physiques par NaN, imputation temporelle). Faites référence aux
fonctions correspondantes de votre module `src/data_clean.py`.*

\[Rédiger la justification méthodologique ici\]

## Travaux Pratiques de Wrangling

# 🧹 Jalon 1 : Data Wrangling & Nettoyage (Squelette Étudiant)

Ce notebook correspond à la première étape du **Jalon 1**. L’objectif
est d’importer le jeu de données brut
(`data/raw/raw_sensor_traffic.csv`), d’effectuer un audit complet de sa
qualité (données manquantes, anomalies physiques, formats incohérents)
et de le nettoyer à l’aide de votre package personnalisé
`src.data_clean`.

### 1. Importation des packages et chargement des données

### 2. Audit initial des données

**À faire par l’étudiant :** Explorez le dataset brut pour évaluer sa
structure et identifier les problèmes à corriger : - Quelles sont les
dimensions du dataset ? - Quels sont les types de données par colonne
(détectez les incohérences) ? - Reste-t-il des valeurs nulles ? Quel est
le taux de valeurs manquantes par variable ? - Y a-t-il des lignes
dupliquées ?

### 3. Nettoyage et uniformisation des Dates

**À faire par l’étudiant :** Appliquez la fonction `clean_dates` de
votre module `src.data_clean` pour convertir la colonne `timestamp` en
type Datetime uniforme, en gérant les formats mixtes présents dans le
fichier brut.

### 4. Identification et Traitement des Outliers (Anomalies physiques)

**À faire par l’étudiant :** Analysez les statistiques descriptives
globales du jeu de données pour identifier les valeurs physiques
aberrantes. Appliquez ensuite votre fonction `handle_outliers` de
`src.data_clean` pour remplacer ces anomalies par des valeurs
appropriées ou par `NaN`.

### 5. Imputation des valeurs manquantes

**À faire par l’étudiant :** Traitez à présent l’ensemble des valeurs
manquantes (les `NaN` initiaux combinés avec ceux issus du traitement
des outliers). Veillez à trier chronologiquement vos données par station
avant d’appliquer votre fonction `impute_missing_values` pour garantir
la cohérence temporelle.

### 6. Sauvegarde des données propres

Enregistrez votre DataFrame nettoyé dans
`data/processed/cleaned_traffic_weather.csv` afin de l’exploiter dans
les étapes suivantes (exploration et modélisation).

------------------------------------------------------------------------

# Analyse Exploratoire des Données (EDA)

Dans cette section, nous analysons les relations statistiques
fondamentales qui régissent la mobilité active (vélos) et les transports
en commun (bus) au sein de la métropole.

## Statistiques Descriptives

*À rédiger par les étudiants : Présentez une vue d’ensemble descriptive
rapide de vos variables nettoyées.*

\[Rédiger les statistiques descriptives ici\]

## Ingénierie de Variables (Feature Engineering)

*À rédiger par les étudiants : Expliquez l’intérêt mathématique et
l’impact sur les modèles prédictifs d’extraire des composantes
temporelles cycliques (comme l’encodage sinus / cosinus des heures).*

\[Rédiger votre explication de l’ingénierie de variables ici\]

## Travaux Pratiques d’Exploration Visuelle (EDA)

# 📊 Jalon 1 : Analyse Exploratoire des Données (EDA) & Visualisation (Squelette Étudiant)

Ce notebook est dédié à la découverte de relations clés et à l’analyse
visuelle de nos flux de déplacements. À partir du jeu de données propre
généré précédemment, nous allons enrichir nos variables explicatives et
appeler les fonctions de notre module de visualisation `src.utils_viz`
pour générer des graphiques professionnels.

### 1. Importation des packages et configuration du style

### 2. Ingénierie de variables temporelles

**À faire par l’étudiant :** Appliquez la fonction `feature_engineering`
de `src.data_clean` pour enrichir votre DataFrame en caractéristiques de
temps classiques (heures, jours de la semaine, mois) et trigonométriques
(sinus, cosinus).

### 3. Visualisations Professionnelles

#### A. Profils de déplacements journaliers

**À faire par l’étudiant :** Appliquez la fonction
`plot_traffic_density` de votre module `src.utils_viz` pour tracer
l’évolution journalière moyenne horaire comparant le transit des vélos
et des bus pour la station **ST_01**.

#### B. Matrice de corrélation multi-variables

**À faire par l’étudiant :** Appliquez la fonction
`plot_correlation_matrix` de votre module `src.utils_viz` pour calculer
et afficher graphiquement la carte thermique des corrélations de
Spearman sur les variables :
`['bike_count', 'bus_count', 'temperature', 'humidity', 'pm25']`.

#### C. Température vs Mobilité Active sous impact Pollution

**À faire par l’étudiant :** Générez le nuage de points de la relation
température vs cyclistes coloré selon la pollution PM2.5, ajusté par la
tendance quadratique, en utilisant votre fonction
`plot_weather_vs_active_transit`.

### 4. Synthèse des insights clés

Sur la base de vos figures, listez les **3 à 5 observations majeures**
sur les comportements de mobilité et de pollution de la métropole. Ces
observations alimenteront votre rapport final.

------------------------------------------------------------------------

# Visualisation Multidimensionnelle (Insights)

Nous présentons ici les résultats visuels clés permettant de dégager des
insights exploitables pour les décideurs publics, en s’appuyant sur
notre module `src/utils_viz.py`.

*À rédiger par les étudiants : Présentez et commentez en détail vos 3 à
5 insights majeurs découverts lors de l’exploration descriptive
visuelle. Intégrez et justifiez les figures clés générées.*

## Profils d’Activité Journalière

``` python
#| label: fig-traffic-density
#| fig-cap: "Profil horaire moyen des déplacements (Vélos vs Bus)."
#| echo: false
# TODO: Utiliser uv.plot_traffic_density() de votre module pour tracer la figure
```

\[Commenter la figure et décrire vos observations ici\]

## Corrélations Globales

``` python
#| label: fig-correlation
#| fig-cap: "Matrice de corrélation de Spearman entre variables."
#| echo: false
# TODO: Utiliser uv.plot_correlation_matrix() de votre module pour tracer la figure
```

\[Commenter la figure et décrire vos observations ici\]

------------------------------------------------------------------------

# Modélisation et Apprentissage

## Schéma Global du Pipeline de Données

Le pipeline complet intègre à la fois la branche analytique tabulaire
(Machine Learning) et la branche d’analyse visuelle (Deep Learning CNN)
:

``` mermaid
graph TD
    A[Données Capteurs Brutes CSV] -->|Formatage & Alignement| B(data_clean.clean_dates)
    C[Données Météo & Pollution] -->|Imputation & Interpolation| D(data_clean.impute_missing_values)
    B & D -->|Gestion Outliers| E[Jeu de données Propre & Fusionné]
    E -->|Extraction Temporelle| F[Feature Engineering]
    F -->|Splits Temporels Chronologiques| G[Modèle Machine Learning Tabulaire]
    H[Flux Caméras Trafic en Temps Réel] -->|Prétraitement d'images 64x64| I[Réseau Convolutif CNN TensorFlow]
    G -->|Prédictions de Flux de Mobilité| J[Livrables & Aide à la Décision Métropole]
    I -->|Détection de Congestion| J
    
    style E fill:#e0f2fe,stroke:#0284c7,stroke-width:2px
    style J fill:#f0fdf4,stroke:#16a34a,stroke-width:2px
    style G fill:#fef3c7,stroke:#d97706,stroke-width:2px
    style I fill:#fef3c7,stroke:#d97706,stroke-width:2px
```

## Modélisation Tabulaire (Prédiction Vélos)

*À rédiger par les étudiants : Expliquez le choix de votre algorithme
d’apprentissage supervisé (Forêt Aléatoire) et décrivez l’importance des
variables explicatives.*

\[Détailler votre modélisation ici\]

### Travaux Pratiques de Modélisation Tabulaire

# 🧠 Jalon 2 : Modélisation Prédictive de Trafic (Squelette Étudiant)

Dans ce notebook du **Jalon 2**, l’objectif est d’implémenter un
pipeline complet d’apprentissage supervisé pour prédire le nombre
horaire de cyclistes (`bike_count`) à l’aide de Scikit-Learn.

Vous devrez mettre en œuvre une stratégie de découpage train/test
chronologique pour respecter la causalité des séries temporelles.

### 1. Préparation de l’environnement

### 2. Définition des variables et split chronologique

**À faire par l’étudiant :** - Identifiez vos colonnes prédictives
(features numériques et temporelles) et la colonne cible
(`bike_count`). - Configurez un split temporel simple : utilisez par
exemple les 12 premiers jours pour l’entraînement (`Train`) et les 3
derniers jours pour l’évaluation (`Test`). N’utilisez pas de découpage
aléatoire !

### 3. Entraînement du modèle de Forêt Aléatoire

**À faire par l’étudiant :** - Instanciez et entraînez un modèle
`RandomForestRegressor` sur vos données d’entraînement. - Générez les
prédictions `y_pred` du modèle sur l’ensemble de test.

### 4. Évaluation métrique

**À faire par l’étudiant :** Calculez et affichez les scores
d’évaluation requis : - **MAE** (Mean Absolute Error) - **RMSE** (Root
Mean Squared Error) - **R²** (Coefficient de détermination)

Reportez ces valeurs finales dans le tableau de votre rapport Quarto !

### 5. Importance des variables et Visualisation chronologique

**À faire par l’étudiant :** - Extrayez et tracez l’importance relative
de chaque caractéristique prédictive dans votre forêt d’arbres. - Tracez
un graphique temporel comparant la courbe des observations de test
réelles (`y_test`) et celle des prédictions (`y_pred`).

## Modélisation Vision (Analyse d’Images)

*À rédiger par les étudiants : Expliquez l’intérêt de la brique de Deep
Learning d’images pour classifier le trafic. Détaillez l’architecture de
votre réseau de neurones convolutif (CNN) conçu sous TensorFlow/Keras
(conv, pooling, dense, dropout, activation) et commentez les courbes
d’apprentissage obtenues.*

\[Détailler votre architecture CNN et analyse ici\]

### Travaux Pratiques de Vision par Ordinateur (CNN)

# 📷 Jalon 2 : Brique de Vision par Ordinateur (CNN & TensorFlow) (Squelette Étudiant)

Ce notebook est dédié à la brique d’analyse d’images du **Jalon 2**.
L’objectif est de concevoir un Réseau de Neurones Convolutif (CNN) sous
TensorFlow/Keras pour classifier l’état du trafic routier à partir
d’images de caméras urbaines.

### 1. Préparation de l’environnement

### 2. Génération du jeu d’images synthétiques

Pour travailler de manière autonome sans importer de lourdes bases
d’images externes, nous mettons à votre disposition cette fonction
utilitaire générant des images simulées en $64    imes 64$ pixels de
route vide (Classe 0) vs route congestionnée (Classe 1).

### 3. Split d’évaluation (Entraînement / Validation)

**À faire par l’étudiant :** Divisez vos données d’images `X_images` et
`y_labels` en $80\%$ pour l’entraînement et $20\%$ pour la validation.

### 4. Conception de l’architecture du CNN

**À faire par l’étudiant :** Instanciez un réseau convolutif séquentiel
Keras comprenant : - Une première couche `Conv2D` (ex: 16 filtres de
3x3) suivie d’un `MaxPooling2D`. - Une seconde couche `Conv2D` (ex: 32
filtres de 3x3) suivie d’un `MaxPooling2D`. - Une couche `Flatten` pour
aplatir le tenseur. - Une couche fully-connected `Dense` régularisée par
du `Dropout`. - Une couche `Dense` finale de classification binaire
(avec activation sigmoïde).

### 5. Compilation, Entraînement et Visualisation

**À faire par l’étudiant :** - Compilez le modèle en sélectionnant
l’optimiseur `'adam'` et la fonction de perte binaire adaptée. -
Entraînez votre CNN sur environ 15 époques. - Récupérez les historiques
de perte (`loss`) et précision (`accuracy`) et tracez les courbes
d’apprentissage d’entraînement vs validation.

------------------------------------------------------------------------

# Évaluation Métrique et Validation

## Stratégie de Validation Chronologique

*À rédiger par les étudiants : Expliquez pourquoi un découpage
d’évaluation aléatoire classique violerait le principe de causalité
temporelle et comment vous avez configuré une validation temporelle
rigoureuse.*

\[Rédiger la section de validation ici\]

## Résultats et Interprétation

*À rédiger par les étudiants : Complétez le tableau d’évaluation
ci-dessous en reportant vos résultats de modélisation.*

| Modèle | MAE (cyclistes) | RMSE (cyclistes) | $R^2$ (%) |
|----|----|----|----|
| Baseline Historique | \[À compléter\] | \[À compléter\] | \[À compléter\] |
| **Forêt Aléatoire** | **\[À compléter\]** | **\[À compléter\]** | **\[À compléter\]** |

\[Interpréter et comparer les métriques d’erreur calculées ici\]

------------------------------------------------------------------------

# Data Storytelling et Communication

## Recommandations pour la Métropole

*À rédiger par les étudiants : Formulez des recommandations
stratégiques, opérationnelles et innovantes pour aider les décideurs
publics sur la base de vos découvertes analytiques et prédictives.*

\[Rédiger vos recommandations ici\]

## Limites et Perspectives

*À rédiger par les étudiants : Identifiez honnêtement les biais ou
limites de votre approche et proposez des pistes d’amélioration futures
(ex: intégration de données externes réelles, modélisation plus
poussée).*

\[Rédiger les limites et perspectives ici\]

Ce document dynamique a été compilé en Quarto ([Team
2024](#ref-quarto2024)).

------------------------------------------------------------------------

# Bibliographie

<div id="refs" class="references csl-bib-body hanging-indent"
entry-spacing="0">

<div id="ref-pandas2020" class="csl-entry">

McKinney, Wes. 2020. *Python for Data Analysis: Data Wrangling with
Pandas, NumPy, and IPython*. O’Reilly Media.

</div>

<div id="ref-quarto2024" class="csl-entry">

Team, Quarto Development. 2024. “Quarto Dynamic Publishing System:
Collaborative Scientific and Technical Publishing.” 2024.
<https://quarto.org/>.

</div>

</div>
