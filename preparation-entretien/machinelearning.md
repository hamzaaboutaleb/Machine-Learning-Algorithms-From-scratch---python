### Qu'est ce que le theoreme central limite et pourquoi est-il important ? 
Le théorème central limite (TCL) est un théorème fondamental en statistiques qui stipule que lorsqu'on prélève un grand nombre d'échantillons indépendants et de même distribution dans une population, la distribution de leurs moyennes tend vers une loi normale, quelle que soit la distribution initiale de la population, à condition que celle-ci possède une moyenne et une variance finies.
- Il est important parce qu'il permet d'utiliser les propriétés de la loi normale pour effectuer des estimations et des inférences statistiques, même lorsque les données d'origine ne suivent pas une distribution normale.

En pratique, il est notamment utilisé pour :
- Construire des intervalles de confiance.
- Réaliser des tests d'hypothèses.
- Estimer les paramètres d'une population à partir d'un échantillon.
- Analyser les résultats d'expériences et de tests A/B.

## Qu'est-ce que l'echantillonnage ? Quels sont les types de methods que vous connaissez ? 
L'échantillonnage est une technique statistique qui consiste à sélectionner un sous-ensemble d'individus ou d'observations à partir d'une population afin de l'étudier et de tirer des conclusions sur l'ensemble de cette population.

L'objectif est d'obtenir des informations fiables sans avoir besoin d'étudier toute la population, ce qui permet de réduire le temps, les coûts et les ressources nécessaires.

On distingue principalement deux grandes catégories de méthodes d'échantillonnage :

### 1. Échantillonnage probabiliste (Probability Sampling)

Chaque individu de la population possède une probabilité connue et non nulle d'être sélectionné.

Les principales méthodes sont :

**1. Échantillonnage aléatoire simple (Simple Random Sampling)**

Chaque individu possède la même probabilité d'être sélectionné. La sélection se fait généralement de manière aléatoire.

*Exemple :* Sélectionner aléatoirement 100 clients parmi une base de données de 10 000 clients.

**2. Échantillonnage systématique (Systematic Sampling)**

On sélectionne les individus à intervalles réguliers après avoir choisi un point de départ aléatoire.

*Exemple :* Sélectionner un client tous les 10 clients dans une liste.

**3. Échantillonnage stratifié (Stratified Sampling)**

La population est divisée en groupes homogènes appelés strates, puis un échantillon est sélectionné dans chaque strate.

*Exemple :* Diviser les clients selon leur tranche d'âge et sélectionner des individus dans chaque groupe.

**4. Échantillonnage par grappes (Cluster Sampling)**

La population est divisée en groupes appelés grappes, puis certaines grappes sont sélectionnées aléatoirement pour être étudiées.

*Exemple :* Sélectionner aléatoirement 5 agences bancaires parmi 50 et étudier les clients de ces agences.

### 2. Échantillonnage non probabiliste (Non-Probability Sampling)

La sélection des individus ne repose pas sur un mécanisme aléatoire. La probabilité de sélection de chaque individu n'est pas nécessairement connue.

Les principales méthodes sont :

**1. Échantillonnage de convenance (Convenience Sampling)**

On sélectionne les individus les plus facilement accessibles.

*Exemple :* Interroger les personnes présentes dans un centre commercial.

**2. Échantillonnage par quotas (Quota Sampling)**

On sélectionne les individus en respectant des proportions prédéfinies selon certaines caractéristiques.

*Exemple :* Interroger 50 % d'hommes et 50 % de femmes.

**3. Échantillonnage par boule de neige (Snowball Sampling)**

Les premiers participants recommandent d'autres participants répondant aux critères de l'étude.

*Exemple :* Étudier une population difficile à atteindre en demandant aux participants de recommander d'autres personnes.

**4. Échantillonnage raisonné (Purposive Sampling)**

Le chercheur sélectionne volontairement les individus qui possèdent des caractéristiques particulières pertinentes pour son étude.

*Exemple :* Interroger uniquement des experts en intelligence artificielle.

### 3. Quelle est la différence entre les deux catégories ?

| Échantillonnage probabiliste | Échantillonnage non probabiliste |
|---|---|
| Sélection aléatoire | Sélection non aléatoire |
| Probabilité de sélection connue | Probabilité généralement inconnue |
| Permet l'inférence statistique sous certaines conditions | Généralisation statistique plus limitée |
| Risque de biais de sélection généralement mieux maîtrisé | Risque de biais de sélection plus important |

### 4. Question complémentaire : Quelle méthode choisiriez-vous ?

Cela dépend de l'objectif de l'étude, de la nature de la population et des ressources disponibles.

Pour une étude statistique visant à généraliser les résultats à une population, je privilégierais une méthode probabiliste, notamment l'échantillonnage aléatoire stratifié lorsque la population contient plusieurs sous-groupes importants.

---

**À retenir pour l'entretien :**

Les deux grandes familles sont :
- Probabilistic Sampling : Simple Random, Systematic, Stratified, Cluster.
- Non-Probabilistic Sampling : Convenience, Quota, Snowball, Purposive.

### Le biais de selection  ? selection bias 

Le biais de sélection est une erreur systématique qui apparaît lorsque la méthode utilisée pour sélectionner les individus d'un échantillon ne représente pas correctement la population étudiée.

Autrement dit, certains individus ont plus de chances d'être sélectionnés que d'autres, ce qui peut rendre l'échantillon non représentatif de la population.

Ce biais peut conduire à des conclusions erronées et à des résultats statistiques peu fiables.

**Exemple concret :**

Imaginons qu'une entreprise souhaite mesurer la satisfaction de l'ensemble de ses clients.

Elle décide d'envoyer un questionnaire uniquement aux clients qui ont récemment effectué un achat.

Le problème est que les clients inactifs ou insatisfaits qui ont cessé d'utiliser le service risquent d'être exclus de l'étude.

L'échantillon risque donc de surestimer le niveau réel de satisfaction des clients.

**Quelles sont les conséquences du biais de sélection ?**


- Obtenir un échantillon non représentatif.
- Produire des estimations statistiques biaisées.
- Tirer des conclusions erronées sur la population.
- Construire des modèles de Machine Learning qui généralisent mal.

**Comment éviter le biais de sélection ?**

- Utiliser des méthodes d'échantillonnage probabilistes.
- S'assurer que les différents sous-groupes de la population sont représentés.
- Éviter d'exclure certaines catégories d'individus sans justification.
- Analyser les caractéristiques de l'échantillon et les comparer à celles de la population.

**Question complémentaire : Quelle est la différence entre le biais de sélection et le biais d'échantillonnage ?**

Le biais de sélection est un problème systématique lié à la manière dont les individus sont sélectionnés ou inclus dans une étude. Le biais d'échantillonnage est un terme plus large qui peut désigner les écarts entre les caractéristiques de l'échantillon et celles de la population. Il faut également distinguer ces biais de l'erreur d'échantillonnage aléatoire, qui est due au hasard.

**Point essentiel à retenir :**

Un échantillon de grande taille n'est pas nécessairement représentatif. Même avec 10 000 observations, une mauvaise méthode de sélection peut produire des résultats biaisés.

### 4. Qu'est-ce que la Data Science ? Quelles sont les différences entre l'apprentissage supervisé et non supervisé ?
### 1. Qu'est-ce que la Data Science ?

**Réponse comme dans un entretien :**

La Data Science est un domaine multidisciplinaire qui combine les statistiques, les mathématiques, la programmation et le Machine Learning afin d'extraire des connaissances pertinentes à partir des données.

Son objectif est de transformer les données brutes en informations exploitables pour comprendre des phénomènes, identifier des tendances, faire des prédictions et aider à la prise de décision.

Elle repose principalement sur plusieurs étapes :
- **Collecte des données :** récupérer les données à partir de différentes sources.
- **Préparation des données :** nettoyer, transformer et traiter les valeurs manquantes.
- **Analyse exploratoire (EDA) :** comprendre les données et identifier les relations entre les variables.
- **Modélisation :** appliquer des méthodes statistiques ou des algorithmes de Machine Learning.
- **Évaluation :** mesurer les performances et la capacité de généralisation du modèle.
- **Déploiement :** intégrer le modèle dans un environnement réel pour produire de la valeur.

### 2. Quelle est la différence entre le Supervised Learning et l'Unsupervised Learning ?

Le Machine Learning est une branche de l'intelligence artificielle qui permet aux systèmes d'apprendre automatiquement à partir des données sans être explicitement programmés pour chaque tâche.

On distingue principalement deux grandes catégories :

**A. Supervised Learning (Apprentissage supervisé)**

L'apprentissage supervisé consiste à entraîner un modèle à partir d'un ensemble de données étiquetées (labeled data).

Cela signifie que chaque observation contient des variables explicatives (features) ainsi qu'une variable cible (target) que le modèle doit apprendre à prédire.

Les deux principales tâches sont :

- **Classification :** prédire une catégorie ou une classe.
- **Régression :** prédire une valeur numérique continue.

*Exemples d'algorithmes :*
- Linear Regression.
- Logistic Regression.
- Decision Trees.
- Random Forest.
- Support Vector Machines (SVM).
- K-Nearest Neighbors (KNN).

*Exemple concret :*

Une banque souhaite prédire si un client risque de ne pas rembourser son crédit. Elle utilise des données historiques contenant les informations des clients et leur statut de remboursement (défaut ou non-défaut).

Le modèle apprend à partir de ces exemples pour prédire le risque de défaut de nouveaux clients.

**B. Unsupervised Learning (Apprentissage non supervisé)**

L'apprentissage non supervisé consiste à entraîner un modèle à partir de données non étiquetées (unlabeled data).

Contrairement à l'apprentissage supervisé, il n'existe pas de variable cible prédéfinie. L'objectif est de découvrir automatiquement des structures, des groupes ou des relations cachées dans les données.

Les principales tâches sont :

- **Clustering :** regrouper les observations similaires.
- **Dimensionality Reduction :** réduire le nombre de variables tout en conservant le maximum d'informations pertinentes.
- **Association Rules :** identifier des relations ou des associations entre différents éléments.

*Exemples d'algorithmes :*
- K-Means.
- DBSCAN.
- Hierarchical Clustering.
- Principal Component Analysis (PCA).
- Apriori.

*Exemple concret :*

Une entreprise souhaite segmenter ses clients selon leurs comportements d'achat.

Elle utilise un algorithme comme K-Means pour regrouper automatiquement les clients présentant des comportements similaires, sans connaître à l'avance les catégories auxquelles ils appartiennent.

### 3. Tableau comparatif

| Critère | Supervised Learning | Unsupervised Learning |
|---|---|---|
| Données | Étiquetées (Labeled) | Non étiquetées (Unlabeled) |
| Variable cible | Présente | Absente |
| Objectif | Prédire une valeur ou une classe | Découvrir des structures cachées |
| Principales tâches | Classification et régression | Clustering et réduction de dimension |
| Évaluation | Métriques comme Accuracy, F1-score, RMSE | Silhouette Score, Davies-Bouldin, etc. |
| Exemples | Random Forest, SVM, Linear Regression | K-Means, DBSCAN, PCA |

### 4. Question complémentaire : Quelle est la différence entre la classification et la régression ?

Les deux sont des tâches d'apprentissage supervisé.

- **Classification :** le modèle prédit une catégorie. Exemple : déterminer si un email est un spam ou non.
- **Régression :** le modèle prédit une valeur numérique continue. Exemple : prédire le prix d'une maison en fonction de ses caractéristiques.

### 5. Question complémentaire : Peut-on combiner les deux approches ?

Oui. Dans certains projets, on peut utiliser les deux approches successivement.

Par exemple, une entreprise peut commencer par utiliser K-Means pour segmenter ses clients (Unsupervised Learning), puis entraîner un modèle de classification pour prédire à quel segment appartient un nouveau client (Supervised Learning).


### 5. Qu'est-ce que le Bias-Variance Trade-off (compromis biais-variance) ?

**Réponse comme dans un entretien :**

Le Bias-Variance Trade-off est un concept fondamental en Machine Learning qui décrit le compromis entre deux sources d'erreur : le biais (Bias) et la variance (Variance).

L'objectif est de trouver un équilibre entre les deux afin de construire un modèle qui généralise bien sur de nouvelles données, et qui ne se contente pas de mémoriser les données d'entraînement.

### 1. Le Bias (Biais)

Le biais représente l'erreur introduite par des hypothèses trop simplificatrices du modèle.

Un modèle avec un biais élevé est généralement trop simple pour apprendre correctement les relations présentes dans les données.

Cela conduit au phénomène de **Underfitting (sous-apprentissage)**.

**Exemple :**

On utilise une régression linéaire pour modéliser une relation fortement non linéaire. Le modèle est trop simple pour capturer correctement cette relation.

Conséquences :
- Erreur élevée sur les données d'entraînement.
- Erreur élevée sur les données de test.
- Le modèle ne capture pas suffisamment les relations présentes dans les données.

### 2. La Variance (Variance)

La variance représente la sensibilité du modèle aux variations des données d'entraînement.

Un modèle avec une variance élevée apprend trop précisément les particularités et le bruit des données d'entraînement.

Cela conduit au phénomène de **Overfitting (surapprentissage)**.

**Exemple :**

On utilise un arbre de décision très profond qui mémorise presque parfaitement les données d'entraînement, y compris leurs erreurs et leur bruit.

Conséquences :
- Erreur très faible sur les données d'entraînement.
- Erreur élevée sur les données de test.
- Mauvaise capacité de généralisation.

### 3. Comprendre le compromis

L'objectif est de trouver un équilibre entre le biais et la variance.

| Critère | High Bias | High Variance |
|---|---|---|
| Problème | Underfitting | Overfitting |
| Complexité du modèle | Trop simple | Trop complexe |
| Erreur d'entraînement | Élevée | Faible |
| Erreur de test | Élevée | Élevée |
| Généralisation | Mauvaise | Mauvaise |

### 4. Comment trouver le bon équilibre ?

Plusieurs techniques permettent de contrôler le biais et la variance :

**Pour réduire le biais :**
- Utiliser un modèle plus complexe.
- Ajouter des variables pertinentes (Features).
- Réduire une régularisation trop forte.
- Améliorer les caractéristiques utilisées.

**Pour réduire la variance :**
- Augmenter la quantité de données d'entraînement.
- Utiliser la régularisation (L1, L2).
- Réduire la complexité du modèle.
- Utiliser le Cross-Validation.
- Appliquer des techniques comme le Bagging.

### 5. Comment évaluer ce compromis ?

On utilise généralement la validation croisée (Cross-Validation) et les courbes d'apprentissage (Learning Curves) pour observer les performances du modèle sur les données d'entraînement et de validation.

L'objectif est d'obtenir une erreur de généralisation aussi faible que possible.

### 6. Question complémentaire : Quelle est la différence entre Overfitting et Underfitting ?

- **Underfitting :** le modèle est trop simple et n'apprend pas suffisamment les relations présentes dans les données.
- **Overfitting :** le modèle apprend trop précisément les données d'entraînement, y compris le bruit, et ne généralise pas correctement.

**À retenir pour l'entretien :**

Le Bias-Variance Trade-off consiste à trouver le bon niveau de complexité d'un modèle pour minimiser son erreur de généralisation. Un bon modèle doit être suffisamment complexe pour apprendre les relations importantes, mais pas au point de mémoriser le bruit des données.

### 6. Qu'est-ce qu'une matrice de confusion (Confusion Matrix) ?

**Réponse comme dans un entretien :**

La matrice de confusion est un outil d'évaluation utilisé en Machine Learning, principalement pour les problèmes de classification.

Elle permet de comparer les prédictions d'un modèle avec les valeurs réelles afin d'identifier les bonnes et les mauvaises classifications.

Dans un problème de classification binaire, elle contient quatre éléments principaux :

### 1. Les quatre composantes de la matrice de confusion

Imaginons un modèle qui doit prédire si un client risque de faire défaut sur son crédit (Positive) ou non (Negative).

| | Prédiction Positive | Prédiction Negative |
|---|---|---|
| **Réalité Positive** | True Positive (TP) | False Negative (FN) |
| **Réalité Negative** | False Positive (FP) | True Negative (TN) |

- **True Positive (TP) :** le modèle prédit positif et la réalité est positive. C'est une prédiction correcte.
- **True Negative (TN) :** le modèle prédit négatif et la réalité est négative. C'est également une prédiction correcte.
- **False Positive (FP) :** le modèle prédit positif alors que la réalité est négative. C'est une fausse alerte.
- **False Negative (FN) :** le modèle prédit négatif alors que la réalité est positive. Le modèle a raté un cas positif.

### 2. Exemple concret

Imaginons un modèle de détection de fraude bancaire testé sur 100 transactions.

| | Prédit : Fraude | Prédit : Non-fraude |
|---|---:|---:|
| **Réel : Fraude** | 30 (TP) | 10 (FN) |
| **Réel : Non-fraude** | 5 (FP) | 55 (TN) |

Interprétation :
- 30 fraudes ont été correctement détectées.
- 55 transactions légitimes ont été correctement identifiées.
- 5 transactions légitimes ont été considérées comme frauduleuses.
- 10 fraudes n'ont pas été détectées.

### 3. Les principales métriques calculées à partir de la matrice

**A. Accuracy (Exactitude)**

Mesure la proportion des prédictions correctes parmi toutes les prédictions.

Accuracy = (TP + TN) / (TP + TN + FP + FN)

**B. Precision (Précision)**

Mesure parmi les prédictions positives, la proportion de celles qui sont réellement positives.

Precision = TP / (TP + FP)

**C. Recall (Rappel / Sensibilité)**

Mesure parmi les cas réellement positifs, la proportion de ceux que le modèle a correctement détectés.

Recall = TP / (TP + FN)

**D. F1-Score**

C'est la moyenne harmonique entre la Precision et le Recall. Il permet de trouver un équilibre entre les deux métriques.

F1 = 2 × (Precision × Recall) / (Precision + Recall)

### 4. Calcul avec notre exemple

Avec TP = 30, TN = 55, FP = 5 et FN = 10 :

| Métrique | Calcul | Résultat |
|---|---|---:|
| Accuracy | (30 + 55) / 100 | 85 % |
| Precision | 30 / (30 + 5) | 85,71 % |
| Recall | 30 / (30 + 10) | 75 % |
| F1-Score | 2 × (0,8571 × 0,75) / (0,8571 + 0,75) | 80 % |

### 5. Question complémentaire : Quelle est la différence entre Precision et Recall ?

La Precision répond à la question : parmi les éléments que le modèle a prédits comme positifs, combien sont réellement positifs ?

Le Recall répond à la question : parmi tous les éléments réellement positifs, combien le modèle a-t-il réussi à détecter ?

**Exemple dans la détection de fraude :**

- Une Precision élevée signifie que le système génère peu de fausses alertes.
- Un Recall élevé signifie que le système détecte une grande proportion des fraudes réelles.

Le choix dépend du problème métier. Dans la détection de fraude, on cherche souvent à obtenir un Recall élevé pour éviter de manquer des transactions frauduleuses, tout en maintenant une Precision acceptable.

### 6. Question complémentaire : Pourquoi l'Accuracy peut-elle être trompeuse ?

L'Accuracy peut être trompeuse lorsque les classes sont déséquilibrées (Imbalanced Dataset).

Par exemple, si 99 % des transactions sont légitimes et 1 % frauduleuses, un modèle qui prédit toujours « non-fraude » obtient 99 % d'Accuracy, mais ne détecte aucune fraude.

Dans ce cas, il est préférable d'examiner également la Precision, le Recall, le F1-Score et la matrice de confusion.

### 7. What do you understand by the term Normal Distribution (Loi normale) ?

**Réponse comme dans un entretien :**

La distribution normale, également appelée loi gaussienne, est une distribution de probabilité continue caractérisée par une courbe en forme de cloche, symétrique autour de sa moyenne.

Elle décrit la manière dont les valeurs d'une variable se répartissent autour de leur moyenne. La majorité des observations se situent près de la moyenne, tandis que les valeurs extrêmes sont moins fréquentes.

Elle est caractérisée par deux paramètres principaux :

- **Mean (μ) :** représente la moyenne et détermine le centre de la distribution.
- **Standard Deviation (σ) :** représente l'écart-type et détermine la dispersion des valeurs autour de la moyenne.

### 1. Les principales caractéristiques de la loi normale

- Elle est symétrique autour de la moyenne.
- La moyenne, la médiane et le mode sont égaux.
- L'aire totale sous la courbe est égale à 1 (100 %).
- La distribution est définie par sa moyenne et son écart-type.
- Les valeurs proches de la moyenne sont plus fréquentes que les valeurs extrêmes.

### 2. La règle empirique (68-95-99.7)

Dans une distribution normale :

- **68 %** des observations se trouvent dans l'intervalle [μ - σ, μ + σ].
- **95 %** des observations se trouvent dans l'intervalle [μ - 2σ, μ + 2σ].
- **99,7 %** des observations se trouvent dans l'intervalle [μ - 3σ, μ + 3σ].

### 3. Exemple concret

Imaginons que les notes d'un examen suivent une distribution normale avec :

- Moyenne (μ) = 12/20.
- Écart-type (σ) = 2.

On peut déduire que :

- Environ 68 % des étudiants ont une note comprise entre 10 et 14.
- Environ 95 % ont une note comprise entre 8 et 16.
- Environ 99,7 % ont une note comprise entre 6 et 18.

### 4. La formule de la loi normale

La loi normale est définie par sa fonction de densité :

f(x) = (1 / (σ√(2π))) × exp(-((x - μ)² / (2σ²)))

Où :
- x : valeur observée.
- μ : moyenne.
- σ : écart-type.
- π : constante mathématique.

### 5. Qu'est-ce que la loi normale centrée réduite (Standard Normal Distribution) ?

C'est un cas particulier de la loi normale dont la moyenne est égale à 0 et l'écart-type est égal à 1.

On l'obtient grâce à la standardisation des données (Z-score) :

Z = (X - μ) / σ

Cette transformation permet de comparer des observations provenant de distributions différentes.

### 6. Pourquoi la loi normale est-elle importante en Data Science ?

Elle est importante notamment parce que :

- Elle intervient dans de nombreuses méthodes statistiques.
- Elle permet de construire des intervalles de confiance.
- Elle est utilisée dans les tests d'hypothèses.
- Elle intervient dans certains modèles statistiques et algorithmes de Machine Learning.
- Elle permet de détecter des valeurs atypiques (outliers), notamment à l'aide des Z-scores.

**Point essentiel à retenir :**

La loi normale est une distribution symétrique en forme de cloche, caractérisée par sa moyenne et son écart-type. Elle joue un rôle fondamental en statistiques et en inférence statistique.

### 8. What are Correlation and Covariance in Statistics?

**Réponse comme dans un entretien :**

La covariance et la corrélation sont deux mesures statistiques qui permettent d'étudier la relation entre deux variables.

Elles permettent de comprendre comment deux variables évoluent ensemble, notamment si elles ont tendance à augmenter ou à diminuer simultanément.

Cependant, elles présentent une différence importante : la covariance indique le sens de la relation, tandis que la corrélation mesure à la fois le sens et l'intensité de la relation linéaire.

### 1. Covariance (Covariance)

La covariance mesure la manière dont deux variables varient ensemble.

Elle peut prendre trois formes :

- **Covariance positive :** lorsque les deux variables ont tendance à augmenter ou à diminuer ensemble.
- **Covariance négative :** lorsque l'une augmente tandis que l'autre a tendance à diminuer.
- **Covariance nulle :** indique l'absence de relation linéaire détectée par la covariance.

**Exemple :**

Imaginons que nous étudions la relation entre le nombre d'heures de révision et les notes obtenues par les étudiants.

Si les étudiants qui révisent davantage obtiennent généralement de meilleures notes, la covariance entre ces deux variables sera positive.

**Formule :**

Cov(X,Y) = Σ[(Xi - X̄)(Yi - Ȳ)] / (n - 1)

Où :
- Xi et Yi : observations des deux variables.
- X̄ et Ȳ : moyennes respectives.
- n : nombre d'observations.

Pour un échantillon, on utilise généralement n - 1 au dénominateur.

### 2. Correlation (Corrélation)

La corrélation mesure la force et la direction de la relation linéaire entre deux variables.

Contrairement à la covariance, elle est standardisée et possède toujours une valeur comprise entre -1 et +1.

On utilise généralement le coefficient de corrélation de Pearson.

**Interprétation :**

- **r = +1 :** corrélation linéaire positive parfaite.
- **r proche de +1 :** forte corrélation positive.
- **r = 0 :** absence de corrélation linéaire.
- **r proche de -1 :** forte corrélation négative.
- **r = -1 :** corrélation linéaire négative parfaite.

**Formule :**

r = Cov(X,Y) / (σX × σY)

Où :
- Cov(X,Y) : covariance entre X et Y.
- σX : écart-type de X.
- σY : écart-type de Y.

### 3. Différences entre Covariance et Correlation

| Critère | Covariance | Correlation |
|---|---|---|
| Objectif | Mesurer la variation commune | Mesurer la force et la direction de la relation linéaire |
| Valeurs | De -∞ à +∞ | De -1 à +1 |
| Unité | Dépend des unités des variables | Sans unité |
| Interprétation | Plus difficile | Plus facile |
| Sens de la relation | Positif ou négatif | Positif, négatif ou nul |

### 4. Exemple concret en Data Science

Imaginons un dataset contenant les variables suivantes :

- Surface d'une maison (m²).
- Prix de la maison (DH).

Si la surface augmente généralement avec le prix, nous pouvons observer :

- Une covariance positive.
- Une corrélation positive.

La corrélation nous permet notamment de mesurer l'intensité de cette relation linéaire.

### 5. Question complémentaire : Est-ce que corrélation implique causalité ?

Non. Une corrélation entre deux variables ne signifie pas nécessairement que l'une provoque l'autre.

**Exemple :**

On peut observer une corrélation positive entre les ventes de glaces et le nombre de noyades.

Cela ne signifie pas que les glaces provoquent les noyades. Une troisième variable, comme la température estivale, peut expliquer cette relation.

### 6. Question complémentaire : Quelles sont les limites de la corrélation de Pearson ?

- Elle mesure principalement les relations linéaires.
- Elle est sensible aux valeurs aberrantes (Outliers).
- Une corrélation nulle n'exclut pas une relation non linéaire.
- Elle ne permet pas de démontrer une relation de causalité.

Il existe également d'autres coefficients, comme :
- **Spearman :** mesure les relations monotones à partir des rangs.
- **Kendall :** mesure l'association entre les rangs de deux variables.

**À retenir pour l'entretien :**

La covariance indique si deux variables évoluent dans le même sens ou dans des sens opposés. La corrélation va plus loin en mesurant la force et la direction de leur relation linéaire, avec une valeur comprise entre -1 et +1.

# Point Estimate vs Confidence Interval

## 1. Point Estimate (Estimation ponctuelle)

A point estimate is a single value calculated from a sample to estimate an unknown population parameter.

**Example:**

Suppose we want to estimate the average salary of all data scientists in Morocco.

We select a sample of 100 data scientists and calculate their average salary:

- Sample mean: 12,000 MAD

The point estimate of the population mean is therefore:

\[
\hat{\mu} = \bar{x} = 12,000
\]

It gives us one estimated value, but it does not tell us how uncertain that estimate is.

## 2. Confidence Interval (Intervalle de confiance)

A confidence interval is a range of values calculated from sample data that provides an indication of the uncertainty surrounding a point estimate.

**Example:**

Using the same sample, we calculate a 95% confidence interval:

\[
[11,200 \ ;\ 12,800]
\]

We can say that we are 95% confident that the population's average salary lies between 11,200 MAD and 12,800 MAD.

More precisely, a 95% confidence level means that if we repeated the sampling process many times and calculated an interval each time, approximately 95% of those intervals would contain the true population mean.

## 3. Main Differences

| Point Estimate | Confidence Interval |
|---|---|
| Gives one value | Gives a range of values |
| Estimates a population parameter | Estimates a parameter and expresses uncertainty |
| Does not directly show precision | Provides information about precision |
| Example: 12,000 MAD | Example: [11,200 ; 12,800] |

## 4. Confidence Interval Formula

For a population mean, when the population standard deviation is known:

\[
CI = \bar{x} \pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}
\]

Where:

- \(\bar{x}\): Sample mean (point estimate).
- \(z_{\alpha/2}\): Critical value (1.96 for a 95% confidence interval).
- \(\sigma\): Population standard deviation.
- \(n\): Sample size.
- \(\frac{\sigma}{\sqrt{n}}\): Standard error.

When the population standard deviation is unknown, we generally use the sample standard deviation and Student's t-distribution.

## 5. What You Should Remember for an Interview

A point estimate provides a single best estimate of a population parameter, while a confidence interval provides a range of plausible values and quantifies the uncertainty associated with that estimate.

**Important:** A narrower confidence interval generally indicates greater precision. Increasing the sample size usually reduces the width of the interval, assuming other factors remain constant.