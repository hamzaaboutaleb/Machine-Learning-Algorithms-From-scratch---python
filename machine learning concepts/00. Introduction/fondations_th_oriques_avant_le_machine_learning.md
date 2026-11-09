# Fondations et Préréquis Théoriques avant d'Aborder le Machine Learning

Ce document regroupe les concepts essentiels qu'il convient de maîtriser avant d'étudier ou de mettre en œuvre des algorithmes d'apprentissage automatique. Il pose le cadre théorique, la typologie des données, les métriques fondamentales et les pièges méthodologiques classiques.

---

## 1. La Cartographie des Disciplines

Avant d'aborder les modèles, il est nécessaire de situer les domaines les uns par rapport aux autres :

```
+-----------------------------------------------------------------------+
| DATA SCIENCE (Science des Données)                                    |
| Domaine interdisciplinaire : Mathématiques, Statistiques, Informatique|
| et Connaissance Métier.                                               |
|                                                                       |
|   +---------------------------------------------------------------+   |
|   | INTELLIGENCE ARTIFICIELLE (IA)                                |   |
|   | Ensemble de théories et techniques visant à simuler           |   |
|   | l'intelligence et la logique humaine.                         |   |
|   |                                                               |   |
|   |   +-------------------------------------------------------+   |   |
|   |   | MACHINE LEARNING (Apprentissage Automatique)          |   |   |
|   |   | Extraction automatique de règles à partir de données  |   |   |
|   |   | via l'optimisation de modèles statistiques.           |   |   |
|   |   |                                                       |   |   |
|   |   |   +-----------------------------------------------+   |   |   |
|   |   |   | DEEP LEARNING (Apprentissage Profond)         |   |   |   |
|   |   |   | Modèles fondés sur des réseaux de neurones    |   |   |   |
|   |   |   | artificiels complexes à multiples couches.    |   |   |   |
|   |   |   +-----------------------------------------------+   |   |   |
|   |   +-------------------------------------------------------+   |   |
|   +---------------------------------------------------------------+   |
+-----------------------------------------------------------------------+
```

---

## 2. Typologie et Taxonomie des Données

La nature des données détermine le choix des méthodes d'analyse et les prétraitements obligatoires.

```
                                    TYPOLOGIE DES DONNÉES
                                              |
                 +----------------------------+----------------------------+
                 |                                                         |
                 v                                                         v
        DONNÉES QUANTITATIVES                                     DONNÉES QUALITATIVES
             (Numériques)                                            (Catégorielles)
                 |                                                         |
         +-------+-------+                                         +-------+-------+
         |               |                                         |               |
         v               v                                         v               v
     Discrètes       Continues                                 Nominales       Ordinales
  (ex: Décomptes)  (ex: Taille)                             (ex: Couleurs)   (ex: Niveaux)
```

### 2.1 Variables Quantitatives (Numériques)
* **Continues :** Peuvent prendre une infinité de valeurs dans un intervalle donné ($\mathbb{R}$). *Exemples : salaire, température, poids.*
* **Discrètes :** Prennent des valeurs isolées, généralement des entiers ($\mathbb{N}$). *Exemples : nombre d'enfants, nombre de clics.*

### 2.2 Variables Qualitatives (Catégorielles)
* **Nominales :** Catégories sans ordre ni hiérarchie sous-jacente. *Exemples : genre, pays, couleur.*
* **Ordinales :** Catégories possédant une relation d'ordre explicite. *Exemples : niveau d'études (Bac, Licence, Master), échelle de satisfaction (Faible, Moyen, Élevé).*

---

## 3. Les Grands Paradigmes d'Apprentissage

En Machine Learning, le type d'apprentissage dépend directement de la présence ou de l'absence d'une variable cible (étiquette / *label*).

```
                                  PARADIGMES D'APPRENTISSAGE
                                              |
     +-------------------+--------------------+-------------------+-------------------+
     |                   |                    |                   |                   |
     v                   v                    v                   v                   v
Apprentissage       Apprentissage        Apprentissage       Apprentissage       Apprentissage
  Supervisé         Non Supervisé        Semi-Supervisé     par Renforcement      Auto-Supervisé
 (Supervised)       (Unsupervised)      (Semi-Supervised)    (Reinforcement)     (Self-Supervised)
```

### 3.1 Apprentissage Supervisé (*Supervised Learning*)
* **Entrées :** Un jeu de données $D = \{(x_1, y_1), (x_2, y_2), \dots, (x_N, y_N)\}$ où $x_i$ représente les caractéristiques (*features*) et $y_i$ l'étiquette cible (*target*).
* **Objectif :** Apprendre une fonction $f: X \rightarrow Y$ capable de prédire $y$ sur de nouvelles données.
* **Tâches clés :**
  * **Classification :** La cible $y$ est discrète (ex: détection de spams, diagnostic médical).
  * **Régression :** La cible $y$ est continue (ex: prédiction du prix d'un bien immobilier).

### 3.2 Apprentissage Non Supervisé (*Unsupervised Learning*)
* **Entrées :** Un jeu de données $D = \{x_1, x_2, \dots, x_N\}$ **sans aucune étiquette** $y$.
* **Objectif :** Découvrir la structure sous-jacente, l'organisation ou les relations cachées au sein des données.
* **Tâches clés :**
  * **Clustering (Partitionnement) :** Regroupement des observations similaires.
  * **Réduction de Dimensionnalité :** Compression de l'espace des variables tout en conservant l'information essentielle.
  * **Détection d'Anomalies :** Identification des observations s'écartant significativement du comportement global.

### 3.3 Apprentissage Semi-Supervisé (*Semi-Supervised Learning*)
Combine un petit volume de données étiquetées avec une grande quantité de données non étiquetées afin d'améliorer la précision de l'apprentissage à moindre coût.

### 3.4 Apprentissage par Renforcement (*Reinforcement Learning*)
Un agent interagit de manière dynamique avec un environnement et apprend à exécuter une séquence d'actions optimales en fonction de signaux de récompense ou de pénalité.

### 3.5 Apprentissage Auto-Supervisé (*Self-Supervised Learning*)
Le modèle génère ses propres étiquettes cibles directement à partir de la structure interne des données brutes (largement utilisé pour le pré-entraînement des grands modèles de langage et en vision par ordinateur).

---

## 4. Concepts Mathématiques de Base : Espaces et Distances

La majorité des méthodes statistiques et algorithmiques reposent sur la mesure de la proximité ou de la séparation entre des observations représentées sous forme de vecteurs dans un espace à $d$ dimensions ($\mathbb{R}^d$).

Soient deux observations $x = (x_1, x_2, \dots, x_d)$ et $y = (y_1, y_2, \dots, y_d)$ :

### 4.1 Distance Euclidienne (Norme $L_2$)
Mesure la distance en ligne droite dans un espace euclidien :

$$
d_2(x, y) = \sqrt{\sum_{i=1}^{d} (x_i - y_i)^2}
$$

### 4.2 Distance de Manhattan (Norme $L_1$)
Mesure la somme des différences absolues le long des axes des coordonnées :

$$
d_1(x, y) = \sum_{i=1}^{d} \vert{}x_i - y_i\vert{}
$$

### 4.3 Distance de Minkowski (Généralisation $L_p$)
Généralise les distances $L_1$ et $L_2$ via le paramètre $p \ge 1$ :

$$
d_p(x, y) = \left( \sum_{i=1}^{d} \vert{}x_i - y_i\vert{}^p \right)^{\frac{1}{p}}
$$

### 4.4 Distance / Similarité Cosinus
Mesure l'angle formé par deux vecteurs, indépendamment de leur norme/magnitude :

$$
\text{Similaríté Cosinus}(x, y) = \frac{x \cdot y}{\Vert{}x\Vert{}_2 \Vert{}y\Vert{}_2} = \frac{\sum_{i=1}^{d} x_i y_i}{\sqrt{\sum_{i=1}^{d} x_i^2} \sqrt{\sum_{i=1}^{d} y_i^2}}
$$

$$
\text{Distance Cosinus} = 1 - \text{Similarité Cosinus}(x, y)
$$

---

## 5. Prétraitement des Données (*Preprocessing*)

Les données brutes sont rarement directement exploitables par des modèles mathématiques. L'étape de prétraitement est indispensable.

### 5.1 Mise à l'Échelle des Caractéristiques (*Feature Scaling*)
Lorsque des variables possèdent des ordres de grandeur ou des unités différents, les variables à forte variance domineront artificiellement les calculs de distance.

* **Standardisation (Z-Score Normalization) :**
  Transforme la variable pour lui donner une moyenne nulle ($\mu = 0$) et un écart-type unitaire ($\sigma = 1$).
  

  $$
  x' = \frac{x - \mu}{\sigma}
  $$

* **Normalisation Min-Max :**
  Rassemble l'ensemble des valeurs dans un intervalle fermé défini, généralement $[0, 1]$.
  

  $$
  x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
  $$

### 5.2 Encodage des Variables Catégorielles
Les modèles numériques ne peuvent pas effectuer d'opérations algébriques sur des chaînes de caractères.

* **Encodage Ordinal (*Ordinal Encoding*) :** Attribue un entier séquentiel à chaque catégorie (adapté uniquement aux variables ordinales).
* **Encodage One-Hot (*One-Hot Encoding*) :** Crée $K$ colonnes binaires ($0$ ou $1$) pour une variable nominale à $K$ catégories afin d'éviter d'instaurer une relation d'ordre artificielle.

---

## 6. Problématiques Théoriques et Erreurs Méthodologiques

### 6.1 Le Dilemme Biais-Variance (*Bias-Variance Tradeoff*)

Toute erreur de prédiction d'un modèle se décompose en trois éléments :

$$
\text{Erreur Totale} = \text{Biais}^2 + \text{Variance} + \text{Erreur Irréductible}
$$

* **Biais :** Erreur due à des hypothèses trop simplificatrices du modèle. Un biais élevé entraîne un **Sous-apprentissage (*Underfitting*)**.
* **Variance :** Sensibilité du modèle aux fluctuations et au bruit du jeu d'entraînement. Une variance élevée entraîne un **Surapprentissage (*Overfitting*)**.

```
    SOUS-APPRENTISSAGE                   ÉQUILIBRE                   SURAPPRENTISSAGE
       (Sous-ajusté)                    (Optimal)                     (Sur-ajusté)
    
     x   x      x   x              x   x      x   x              x   x      x   x
       x   x  x                      x   x  x                      x   x  x
     x   x      x   x              x   x      x   x              x   x      x   x
     -----------------             -----------------             -----------------
     Modèle trop simple            Modèle équilibré              Modèle trop complexe
     (Erreur élevée partout)       (Bonne généralisation)       (Apprend le bruit par cœur)
```

### 6.2 Le Fléau de la Dimensionnalité (*Curse of Dimensionality*)
Lorsque le nombre de dimensions $d$ augmente :
* Le volume de l'espace croît de manière exponentielle.
* Les données deviennent éparses (*sparse*).
* Les distances relatives entre les points convergent vers une valeur quasi-constante ($\lim_{d \to \infty} \frac{D_{\max} - D_{\min}}{D_{\min}} = 0$), rendant la notion de proximité spatiale peu informative.

### 6.3 Fuite de Données (*Data Leakage*)
La fuite de données survient lorsque des informations issues du jeu de test ou du futur sont accidentellement introduites dans l'étape d'entraînement du modèle ou de prétraitement (ex: calculer la moyenne globale pour une standardisation avant d'effectuer le découpage *Train/Test*).

---

## 7. Le Cycle de Vie d'un Projet (Workflow Standard)

```
+------------------+     +------------------+     +------------------+
| 1. DÉFINITION    | --> | 2. NETTOYAGE &   | --> | 3. PRÉTRAITEMENT |
|    DU PROBLÈME   |     |    EXPLORATION   |     |    (SCALING...)  |
+------------------+     +------------------+     +------------------+
                                                           |
                                                           v
+------------------+     +------------------+     +------------------+
| 6. DÉPLOIEMENT & | <-- | 5. ÉVALUATION &  | <-- | 4. SÉPARATION    |
|    MONITORING    |     |    OPTIMISATION  |     |    TRAIN / TEST  |
+------------------+     +------------------+     +------------------+
```

1. **Définition du Problème :** Traduction du besoin métier en une tâche formelle (Classification, Régression, Clustering).
2. **Exploration et Nettoyage (*EDA*) :** Gestion des valeurs manquantes, analyse des distributions et traitement des valeurs aberrantes (*outliers*).
3. **Prétraitement :** Normalisation, encodage et réduction de dimensionnalité.
4. **Partitionnement du Jeu de Données :** Séparation stricte en sous-ensembles d'Entraînement (*Train*), de Validation et de Test (*Test*).
5. **Évaluation :** Mesure des performances via des métriques adaptées à la tâche.
6. **Déploiement et Suivi :** Intégration en production et surveillance du décalage des données (*Data Drift*).