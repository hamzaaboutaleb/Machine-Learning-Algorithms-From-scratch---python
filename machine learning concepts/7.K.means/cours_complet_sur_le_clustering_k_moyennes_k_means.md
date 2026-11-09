# Cours Complet : L'Algorithme de Clustering K-Moyennes (K-Means)

Bienvenue dans le guide de référence complet sur l'algorithme de **clustering des K-Moyennes (K-Means)**. Ce cours couvre l'ensemble des concepts, des fondements mathématiques jusqu'à l'implémentation pratique, les métriques d'évaluation et les variantes avancées.

## Module 1: Introduction à l'Apprentissage Non Supervisé & au Clustering

### 1.1 Apprentissage Supervisé vs. Non Supervisé

* **Apprentissage Supervisé :** Les modèles sont entraînés sur des données étiquetées où chaque variable d'entrée $X$ possède une sortie cible $Y$. Exemples : Classification et Régression.

* **Apprentissage Non Supervisé :** Les modèles explorent des données non étiquetées $X$ pour y découvrir des structures sous-jacentes, des motifs ou des regroupements sans étiquettes cibles. Exemples : Clustering et Réduction de Dimension.

### 1.2 Qu'est-ce que le Clustering ?

Le clustering consiste à partitionner un ensemble de données $D = \{x_1, x_2, \dots, x_N\}$ de $N$ observations en $K$ groupes distincts et disjoints (clusters) $C = \{C_1, C_2, \dots, C_K\}$.

* **Forte Similarité Intra-cluster :** Les points au sein d'un même cluster doivent être aussi proches/similaires que possible.

* **Faible Similarité Inter-cluster :** Les points appartenant à des clusters différents doivent être aussi éloignés/distincts que possible.

---

## Module 2: Fondements Mathématiques des K-Moyennes

### 2.1 Formulation du Problème & Fonction Objectif

Le K-Means formule le clustering comme un problème d'optimisation. Soient :

* $X = \{x_1, x_2, \dots, x_N\} \subset \mathbb{R}^d$ le jeu de données composé de $N$ points dans un espace à $d$ dimensions.

* $\mu_k \in \mathbb{R}^d$ le centroïde (moyenne) du cluster $C_k$.

* $r_{ik} \in \{0, 1\}$ une variable binaire d'appartenance :
  

  $$
  r_{ik} = \begin{cases} 1 & \text{si } x_i \in C_k \\ 0 & \text{sinon} \end{cases}
  $$

L'objectif est de minimiser la **Somme des Carrés Intra-cluster (WCSS - Within-Cluster Sum of Squares)**, également appelée **Inertie** ou fonction de distortion :

$$
J = \sum_{i=1}^{N} \sum_{k=1}^{K} r_{ik} \Vert{} x_i - \mu_k \Vert{}^2
$$

où $\Vert{} x_i - \mu_k \Vert{}^2$ représente la distance euclidienne au carré entre l'observation $x_i$ et le centre de cluster $\mu_k$.

### 2.2 Métriques de Distance

Bien que la distance euclidienne soit la norme, d'autres distances façonnent la géométrie des frontières de décision :

* **Distance Euclidienne (Norme $L_2$) :**
  

  $$
  d(x, y) = \sqrt{\sum_{j=1}^{d} (x_j - y_j)^2}
  $$

* **Distance de Manhattan (Norme $L_1$) :**
  

  $$
  d(x, y) = \sum_{j=1}^{d} \vert{}x_j - y_j\vert{}
  $$

* **Distance Cosinus :**
  

  $$
  d(x, y) = 1 - \frac{x \cdot y}{\Vert{}x\Vert{} \Vert{}y\Vert{}}
  $$

*Remarque : L'algorithme standard K-Means optimise spécifiquement la distance Euclidienne $L_2$ car le centroïde $\mu_k$ qui minimise la somme des distances $L_2$ au carré est rigoureusement garanti d'être la moyenne arithmétique des points du cluster.*

---

## Module 3: Architecture de l'Algorithme (Algorithme de Lloyd)

L'algorithme classique des K-Moyennes (Algorithme de Lloyd) est une procédure itérative de descente par coordonnées :

```
+-------------------------------------------------------+
|                1. INITIALISATION                      |
|   Sélection de K centroïdes (aléatoire ou K-Means++)  |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|               2. ÉTAPE D'AFFECTATION                  |
|     Assigner chaque x_i au centroïde mu_k le plus proche|
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|              3. ÉTAPE DE MISE À JOUR                  |
|     Recalculer mu_k comme moyenne des points de C_k   |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|             4. TEST DE CONVERGENCE                    |
|    Les centroïdes se sont-ils stabilisés ?           |
+-------------------------------------------------------+
            |                              |
           NON                            OUI
            |                              |
            +------------<-----------------+---> [ FIN ]
```

### Étape 1 : Initialisation

Sélectionner $K$ centres de clusters initiaux $\{\mu_1^{(0)}, \mu_2^{(0)}, \dots, \mu_K^{(0)}\}$.

### Étape 2 : Étape d'Expectation / Affectation

Considérer les centroïdes $\mu_k$ fixes et assigner chaque point $x_i$ au centroïde le plus proche :

$$
C_k^{(t)} = \left\{ x_i : \Vert{} x_i - \mu_k^{(t)} \Vert{}^2 \le \Vert{} x_i - \mu_j^{(t)} \Vert{}^2, \; \forall j, 1 \le j \le K \right\}
$$

### Étape 3 : Étape de Maximisation / Mise à jour

Considérer les affectations $C_k$ fixes et recalculer chaque centroïde en prenant la moyenne arithmétique des points assignés :

$$
\mu_k^{(t+1)} = \frac{1}{\vert{}C_k^{(t)}\vert{}} \sum_{x_i \in C_k^{(t)}} x_i
$$

### Étape 4 : Critères de Convergence

Répéter les étapes 2 et 3 jusqu'à ce que l'une des conditions suivantes soit remplie :

1. Le déplacement des centroïdes est inférieur à un seuil défini $\epsilon$ : $\Vert{}\mu_k^{(t+1)} - \mu_k^{(t)}\Vert{} < \epsilon$.
2. L'affectation des points ne change plus.
3. Le nombre maximal d'itérations (`max_iter`) est atteint.

---

## Module 4: Stratégies d'Initialisation

L'initialisation conditionne fortement la convergence vers un minimum global ou le blocage dans un minimum local.

### 4.1 Initialisation Aléatoire

* Choisit aléatoirement $K$ observations du dataset comme centroïdes initiaux.
* **Inconvénient :** Très sensible aux choix initiaux ; peut entraîner un mauvais clustering ou une convergence lente.

### 4.2 L'Algorithme K-Means++

K-Means++ introduit un schéma probabiliste pour choisir des centroïdes initiaux bien espacés :

1. Choisir le premier centroïde $\mu_1$ de manière uniformément aléatoire parmi les points de $X$.
2. Pour chaque point $x_i$, calculer $D(x_i)$, la plus courte distance euclidienne entre $x_i$ et les centroïdes déjà sélectionnés.
3. Choisir le centroïde suivant $\mu_k$ de manière aléatoire avec une probabilité proportionnelle à $D(x_i)^2$ :
   

   $$
   P(x_i) = \frac{D(x_i)^2}{\sum_{j=1}^{N} D(x_j)^2}
   $$

4. Répéter les étapes 2 et 3 jusqu'à avoir sélectionné $K$ centroïdes.

---

## Module 5: Détermination du Nombre Optimal de Clusters ($K$)

Déterminer la meilleure valeur de $K$ est essentiel. Deux méthodes quantitatives principales sont utilisées :

### 5.1 La Méthode du Coude (Elbow Method)

Tracer l'inertie WCSS en fonction d'une plage de valeurs candidates pour $K$ :

$$
J(K) = \sum_{k=1}^{K} \sum_{x_i \in C_k} \Vert{} x_i - \mu_k \Vert{}^2
$$

* À mesure que $K$ augmente, l'inertie diminue naturellement (atteignant 0 quand $K = N$).
* Identifier le **point de rupture ("le coude")** sur la courbe où la réduction relative de l'inertie ralentit nettement.

### 5.2 L'Analyse de Silhouette

Évalue à quel point les clusters sont bien séparés. Pour chaque point $i$ :

* $a(i)$ : Distance moyenne intra-cluster entre le point $i$ et tous les autres points du même cluster.
* $b(i)$ : Distance moyenne au cluster le plus proche pour le point $i$.

Le coefficient de Silhouette $s(i)$ est défini par :

$$
s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}, \quad s(i) \in [-1, +1]
$$

* $s(i) \approx +1$ **:** Le point est très bien classé dans son cluster.
* $s(i) \approx 0$ **:** Le point se situe sur la frontière de décision.
* $s(i) \approx -1$ **:** Le point est probablement mal classé.

---

## Module 6: Prétraitement des Données & Bonnes Pratiques

### 6.1 Normalisation des Variables (Étape Cruciale)

Le K-Means s'appuyant sur la distance euclidienne, les variables à forte amplitude numérique dominent artificiellement les calculs.

* **Standardisation (Score Z) :**
  

  $$
  x' = \frac{x - \mu}{\sigma}
  $$

* **Normalisation Min-Max :**
  

  $$
  x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
  $$

### 6.2 Forte Dimensionnalité (Fléau de la Dimensionnalité)

En haute dimension, les distances relatives perdent en contraste ($D_{\max} \approx D_{\min}$), réduisant l'efficacité des algorithmes basés sur la distance.

* **Solution :** Appliquer une réduction de dimension (ex. PCA, t-SNE, UMAP) avant le K-Means.

---

## Module 7: Implémentation Complète en Python

### 7.1 Implémentation "from scratch" (Sans Bibliothèque ML)

```python
import numpy as np

class KMeansScratch:
    def __init__(self, k=3, max_iters=100, tol=1e-4):
        self.k = k
        self.max_iters = max_iters
        self.tol = tol
        self.centroids = None

    def _kmeans_pp_init(self, X):
        n_samples, _ = X.shape
        centroids = [X[np.random.randint(n_samples)]]
        
        for _ in range(1, self.k):
            dists = np.array([min([np.linalg.norm(x - c)**2 for c in centroids]) for x in X])
            probs = dists / np.sum(dists)
            cum_probs = np.cumsum(probs)
            r = np.random.rand()
            for idx, prob in enumerate(cum_probs):
                if r < prob:
                    centroids.append(X[idx])
                    break
        return np.array(centroids)

    def fit(self, X):
        self.centroids = self._kmeans_pp_init(X)
        
        for _ in range(self.max_iters):
            # Étape d'affectation
            distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
            labels = np.argmin(distances, axis=1)
            
            # Étape de mise à jour
            new_centroids = np.array([X[labels == k].mean(axis=0) if np.sum(labels == k) > 0 
                                      else self.centroids[k] for k in range(self.k)])
            
            # Test de convergence
            if np.all(np.abs(new_centroids - self.centroids) < self.tol):
                break
                
            self.centroids = new_centroids
            
        return labels

    def predict(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)
```

### 7.2 Implémentation avec Scikit-Learn

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import numpy as np

# 1. Génération de données de démonstration
X = np.random.rand(500, 5)

# 2. Standardisation des variables
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Entraînement avec K-Means++
kmeans = KMeans(
    n_clusters=4,
    init='k-means++',
    n_init=10,
    max_iter=300,
    random_state=42
)

cluster_labels = kmeans.fit_predict(X_scaled)

# 4. Évaluation du modèle
inertia = kmeans.inertia_
sil_score = silhouette_score(X_scaled, cluster_labels)

print(f"Inertie (WCSS) : {inertia:.4f}")
print(f"Score de Silhouette : {sil_score:.4f}")
```

---

## Module 8: Variantes de l'Algorithme K-Means

1. **Mini-Batch K-Means :** Utilise des sous-ensembles aléatoires (batches) pour mettre à jour les centroïdes, ce qui réduit considérablement le temps de calcul sur de très grands jeux de données.
2. **K-Médoïdes (PAM) :** Utilise de véritables points du jeu de données (médoïdes) au lieu des moyennes. Plus robuste aux valeurs aberrantes (outliers).
3. **K-Modes / K-Prototypes :** Adaptations conçues pour traiter des données catégorielles (K-Modes) ou mixtes (K-Prototypes).

---

## Module 9: Tableau Récapitulatif

| Propriété | K-Moyennes (K-Means) |
| :--- | :--- |
| **Type** | Clustering non supervisé partitionnel |
| **Complexité Temporelle** | $O(N \cdot K \cdot I \cdot d)$ où $I$ = itérations, $d$ = dimensions |
| **Forme des clusters supposée** | Spherique et convexe |
| **Sensibilité** | Sensible à l'échelle des variables, aux outliers et à l'initialisation |
| **Forces Principales** | Rapide, simple à comprendre, très scalable |
| **Limites Principales** | Nécessite de fixer $K$, inadapté aux formes complexes ou de densités variables |