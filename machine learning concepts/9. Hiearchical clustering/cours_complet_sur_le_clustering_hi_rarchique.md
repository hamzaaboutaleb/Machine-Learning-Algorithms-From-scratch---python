# Cours Complet : Le Clustering Hiérarchique (Hierarchical Clustering)

Bienvenue dans ce cours dédié au **Clustering Hiérarchique**, une méthode populaire d'apprentissage non supervisé qui construit une hiérarchie de clusters sous forme d'arbre, appelée **dendrogramme**. Contrairement à l'algorithme des K-Moyennes (K-Means), il ne nécessite pas de spécifier au préalable le nombre de clusters.

## Module 1: Introduction au Clustering Hiérarchique

### 1.1 Qu'est-ce que le Clustering Hiérarchique ?

Le clustering hiérarchique est une méthode de partitionnement non supervisée qui vise à regrouper les observations selon une structure arborescente. Elle permet d'examiner la structure des données à différents niveaux de granularité.

### 1.2 Les deux approches fondamentales

1. **Approche Agglomérative (Bottom-Up - De bas en haut) :**
   * **Principe :** Chaque point commence dans son propre cluster individuel. À chaque étape, les deux clusters les plus proches sont fusionnés.
   * **Point d'arrêt :** L'ensemble des points se retrouve dans un unique cluster global (la racine).
   * *Il s'agit de la méthode la plus utilisée en pratique.*

2. **Approche Divisive (Top-Down - De haut en bas) :**
   * **Principe :** Toutes les observations débutent au sein d'un seul et unique grand cluster. À chaque étape, le cluster le plus hétérogène est divisé en sous-clusters.
   * **Point d'arrêt :** Chaque observation forme un cluster individuel.

## Module 2: Fondements Mathématiques & Métriques

Le fonctionnement du clustering agglomératif repose sur deux notions distantes : la **distance entre deux points** et la **distance entre deux clusters** (critère de liaison).

### 2.1 Distances entre points (Distance Metrics)

Soient deux observations $x_i, x_j \in \mathbb{R}^d$ :

* **Distance Euclidienne ($L_2$) :**
  $$
  d(x_i, x_j) = \sqrt{\sum_{k=1}^{d} (x_{ik} - x_{jk})^2}
  $$

* **Distance de Manhattan ($L_1$) :**
  $$
  d(x_i, x_j) = \sum_{k=1}^{d} |x_{ik} - x_{jk}|
  $$

* **Distance Cosinus :**
  $$
  d(x_i, x_j) = 1 - \frac{x_i \cdot x_j}{\|x_i\| \|x_j\|}
  $$

### 2.2 Critères de Liaison (Linkage Criteria)

Le critère de liaison définit la distance entre deux ensembles/clusters $C_A$ et $C_B$ :

#### 1. Liaison Simple (Single Linkage)
Calcule la distance entre les deux points les plus proches des deux clusters :
$$
D(C_A, C_B) = \min \{ d(x_i, x_j) : x_i \in C_A, x_j \in C_B \}
$$
* **Caractéristique :** Peux créer un effet de "chaînage" (chaining effect), formant de longs clusters étirés.

#### 2. Liaison Complète (Complete Linkage)
Calcule la distance entre les deux points les plus éloignés des deux clusters :
$$
D(C_A, C_B) = \max \{ d(x_i, x_j) : x_i \in C_A, x_j \in C_B \}
$$
* **Caractéristique :** Produit des clusters de taille compacte et homogène, mais sensible aux valeurs aberrantes (outliers).

#### 3. Liaison Moyenne (Average Linkage / UPGMA)
Calcule la distance moyenne entre toutes les paires d'observations :
$$
D(C_A, C_B) = \frac{1}{|C_A| |C_B|} \sum_{x_i \in C_A} \sum_{x_j \in C_B} d(x_i, x_j)
$$

#### 4. Méthode de Ward (Ward's Linkage)
Minimise l'augmentation de la somme des carrés de l'invariance/variance intra-cluster après fusion :
$$
\Delta \text{ESS}_{AB} = \frac{|C_A| |C_B|}{|C_A| + |C_B|} \|\mu_A - \mu_B\|^2
$$
Où $\mu_A$ et $\mu_B$ sont les centroïdes des clusters $C_A$ et $C_B$.
* **Caractéristique :** Crée des clusters équilibrés et de formes convexes (similaire à K-Means).

## Module 3: Le Dendrogramme

### 3.1 Définition
Un **dendrogramme** est une représentation graphique sous forme d'arbre inversé qui illustre la séquence des fusions (ou divisions) effectuées à chaque étape de l'algorithme.

* **Axe horizontal (x) :** Représente les observations individuelles ou les clusters.
* **Axe vertical (y) :** Représente la distance (ou le niveau de dissociation) à laquelle deux clusters sont fusionnés.

```
Distance (y)
   ^
 4 |         +--------------+
 3 |         |              |
 2 |    +----+----+         |
 1 |    |         |         |
 0 +----+----+----+----+----+----+---> Observations (x)
        x1   x2   x3   x4   x5   x6
```

### 3.2 Sélection du nombre optimal de clusters $K$

Pour choisir le nombre de clusters :
1. Tracez une ligne horizontale à travers le dendrogramme au niveau où la hauteur des lignes verticales est la plus importante (sans croiser de points de fusion horizontaux).
2. Le nombre de lignes verticales coupées par cette ligne horizontale correspond au nombre optimal de clusters $K$.

## Module 4: Algorithme Agglomératif Pas à Pas

```
+-------------------------------------------------------+
|                1. INITIALISATION                      |
|     Chaque observation x_i constitue un cluster       |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|              2. MATRICE DE DISTANCE                   |
|     Calculer les distances entre tous les clusters    |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|                   3. FUSION                           |
|  Trouver et fusionner les 2 clusters les plus proches |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|             4. MISE À JOUR DE LA MATRICE              |
|  Recalculer la distance du nouveau cluster aux autres |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|              5. TEST D'ARRÊT                          |
|   Tous les points sont-ils dans un seul cluster ?    |
+-------------------------------------------------------+
            |                              |
           NON                            OUI
            |                              |
            +------------<-----------------+---> [ FIN ]
```

## Module 5: Implémentation Complète en Python

### 5.1 Génération du Dendrogramme avec SciPy

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# 1. Génération de données fictives (50 observations à 2 dimensions)
np.random.seed(42)
X = np.random.rand(50, 2)

# 2. Calcul des liaisons avec la méthode de Ward
Z = linkage(X, method='ward', metric='euclidean')

# 3. Tracé du dendrogramme
plt.figure(figsize=(10, 6))
plt.title("Dendrogramme du Clustering Hiérarchique (Ward)")
plt.xlabel("Index des points")
plt.ylabel("Distance (Dissimilarité)")
dendrogram(Z, leaf_rotation=90., leaf_font_size=8.)
plt.axhline(y=1.5, color='r', linestyle='--') # Exemple de coupe
plt.show()
```

### 5.2 Utilisation avec Scikit-Learn (AgglomerativeClustering)

```python
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import numpy as np

# 1. Données et prétraitement
X = np.random.rand(200, 4)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Instanciation du modèle avec K=3 clusters
model = AgglomerativeClustering(
    n_clusters=3,
    metric='euclidean',
    linkage='ward'
)

# 3. Entraînement et prédiction des étiquettes
labels = model.fit_predict(X_scaled)

print("Nombre de clusters trouvés :", len(np.unique(labels)))
print("Forme des étiquettes :", labels.shape)
```

## Module 6: Tableau Comparatif

| Propriété | Clustering Hiérarchique | K-Means |
| ----- | ----- | ----- |
| **Complexité Temporelle** | $O(N^3)$ en général, réduisible à $O(N^2 \log N)$ | $O(N \cdot K \cdot I \cdot d)$ — beaucoup plus rapide |
| **Complexité Spatiale** | $O(N^2)$ (stockage de la matrice de distance) | $O(N \cdot d)$ |
| **Nombre de clusters $K$** | Non requis à l'avance (choisi via le dendrogramme) | Requis en paramètre initial |
| **Visualisation** | Excellente via le dendrogramme | Non native (nécessite des projections PCA) |
| **Adaptabilité aux grands volumes** | Faible (inadapté aux très grands jeux de données) | Forte (très scalable) |
| **Reproductibilité** | Déterministe (résultat identique à chaque exécution) | Variable (selon l'initialisation des centroïdes) |
