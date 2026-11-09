# Comprehensive Course: K-Means Clustering Algorithm

Welcome to the complete reference and learning guide for the **K-Means Clustering Algorithm**. This course covers everything from foundational mathematical principles to advanced implementation details, evaluation metrics, and practical applications.

---

## Module 1: Introduction to Unsupervised Learning & Clustering

### 1.1 Supervised vs. Unsupervised Learning
* **Supervised Learning:** Models are trained using labelled datasets where each input $X$ has an associated ground-truth output $Y$. Examples include Classification and Regression.
* **Unsupervised Learning:** Models explore unlabeled data $X$ to discover underlying structures, patterns, or groupings without explicit target labels. Examples include Clustering and Dimensionality Reduction.

### 1.2 What is Clustering?
Clustering is the task of partitioning a dataset $D = \{x_1, x_2, \dots, x_N\}$ of $N$ observations into $K$ distinct, non-overlapping groups (clusters) $C = \{C_1, C_2, \dots, C_K\}$.
* **High Intra-cluster Similarity:** Data points inside the same cluster should be as close/similar to each other as possible.
* **Low Inter-cluster Similarity:** Data points in different clusters should be as distinct/far from each other as possible.

---

## Module 2: Mathematical Foundations of K-Means

### 2.1 Problem Formulation & Objective Function
K-Means formulates clustering as an optimization problem. Let:
* $X = \{x_1, x_2, \dots, x_N\} \subset \mathbb{R}^d$ be the dataset of $N$ points in $d$-dimensional space.
* $\mu_k \in \mathbb{R}^d$ be the centroid (mean) of cluster $C_k$.
* $r_{ik} \in \{0, 1\}$ be an indicator binary variable:
  $$r_{ik} = \begin{cases} 1 & \text{if } x_i \in C_k \\ 0 & \text{else} \end{cases}$$

The objective is to minimize the **Within-Cluster Sum of Squares (WCSS)**, also known as **Inertia** or the distortion function:

$$J = \sum_{i=1}^{N} \sum_{k=1}^{K} r_{ik} \| x_i - \mu_k \|^2$$

where $\| x_i - \mu_k \|^2$ represents the squared Euclidean distance between observation $x_i$ and cluster center $\mu_k$.

### 2.2 Distance Metrics
While Euclidean distance is standard, distance metrics shape the cluster boundary geometry:
* **Euclidean Distance ($L_2$-norm):**
  $$d(x, y) = \sqrt{\sum_{j=1}^{d} (x_j - y_j)^2}$$
* **Manhattan Distance ($L_1$-norm):**
  $$d(x, y) = \sum_{j=1}^{d} |x_j - y_j|$$
* **Cosine Distance:**
  $$d(x, y) = 1 - \frac{x \cdot y}{\|x\| \|y\|}$$

*Note: Standard K-Means optimizes for $L_2$ Euclidean distance because the centroid $\mu_k$ that minimizes the sum of squared $L_2$ distances is mathematically guaranteed to be the arithmetic mean of the cluster points.*

---

## Module 3: Algorithm Architecture (Lloyd's Algorithm)

The classic K-Means algorithm (Lloyd's Algorithm) is an iterative Coordinate Descent procedure:

```
+-------------------------------------------------------+
|                1. INITIALIZATION                      |
|     Select K initial centroids randomly or via K-Means++ |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|               2. ASSIGNMENT STEP                      |
|     Assign each x_i to the nearest centroid mu_k      |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|                 3. UPDATE STEP                        |
|     Recalculate mu_k as mean of points in C_k         |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|              4. CONVERGENCE CHECK                     |
|    Have centroids stopped moving or reached max iter? |
+-------------------------------------------------------+
            |                              |
           NO                             YES
            |                              |
            +------------<-----------------+---> [ STOP ]
```

### Step 1: Initialization
Select $K$ initial cluster centers $\{\mu_1^{(0)}, \mu_2^{(0)}, \dots, \mu_K^{(0)}\}$.

### Step 2: Expectation / Assignment Step
Fix centroids $\mu_k$ and assign each data point $x_i$ to its closest centroid:

$$C_k^{(t)} = \left\{ x_i : \| x_i - \mu_k^{(t)} \|^2 \le \| x_i - \mu_j^{(t)} \|^2, \; \forall j, 1 \le j \le K \right\}$$

### Step 3: Maximization / Update Step
Fix assignments $C_k$ and re-calculate each centroid by taking the arithmetic mean of all points assigned to that cluster:

$$\mu_k^{(t+1)} = \frac{1}{|C_k^{(t)}|} \sum_{x_i \in C_k^{(t)}} x_i$$

### Step 4: Convergence Criteria
Iterate Steps 2 and 3 until any of the following conditions are met:
1. Centroids move less than a pre-defined threshold $\epsilon$: $\|\mu_k^{(t+1)} - \mu_k^{(t)}\| < \epsilon$.
2. Data point assignments no longer change.
3. Maximum iteration limit (`max_iter`) is reached.

---

## Module 4: Initialization Strategies

Initialization heavily dictates whether K-Means converges to a global minimum or gets trapped in a local minimum.

### 4.1 Random Initialization
* Randomly selects $K$ observations from the dataset as initial centers.
* **Drawback:** Highly sensitive to initial choices; can cause poor clustering or slow convergence.

### 4.2 K-Means++ Algorithm
K-Means++ introduces a probabilistic scheme to select initial centroids that are well-separated:

1. Choose the first centroid $\mu_1$ uniformly at random from $X$.
2. For each data point $x_i$, compute $D(x_i)$, the shortest Euclidean distance from $x_i$ to the closest centroid already chosen.
3. Select the next centroid $\mu_k$ randomly from $X$ with probability proportional to $D(x_i)^2$:
   $$P(x_i) = \frac{D(x_i)^2}{\sum_{j=1}^{N} D(x_j)^2}$$
4. Repeat Steps 2 and 3 until $K$ centroids are chosen.

---

## Module 5: Determining the Optimal Number of Clusters ($K$)

Choosing $K$ is often non-trivial in real-world applications. Two main quantitative methods are used:

### 5.1 The Elbow Method
Plot the WCSS (Inertia) against a range of candidate values for $K$:

$$J(K) = \sum_{k=1}^{K} \sum_{x_i \in C_k} \| x_i - \mu_k \|^2$$

* As $K$ increases, WCSS naturally decreases (reaching 0 when $K = N$).
* Identify the **"elbow" point** on the curve where the marginal reduction in WCSS sharply declines.

### 5.2 Silhouette Analysis
Evaluates how well-separated the clusters are. For each point $i$:
* $a(i)$: Mean intra-cluster distance between point $i$ and all other points in the same cluster.
* $b(i)$: Mean nearest-cluster distance between point $i$ and all points in the nearest neighboring cluster.

The Silhouette Coefficient $s(i)$ is defined as:

$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}, \quad s(i) \in [-1, +1]$$

* **$s(i) \approx +1$:** Point is well-matched to its own cluster and far from neighbors.
* **$s(i) \approx 0$:** Point lies on or near the decision boundary.
* **$s(i) \approx -1$:** Point may be misassigned.

The average Silhouette Score across all points is calculated for each $K$; the $K$ that maximizes this average score is selected.

---

## Module 6: Data Preprocessing & Practical Considerations

### 6.1 Feature Scaling (Crucial Step)
Because K-Means uses Euclidean distance, features with larger numeric scales dominate distance calculations.
* **Standardization (Z-Score Normalization):**
  $$x' = \frac{x - \mu}{\sigma}$$
* **Min-Max Scaling:**
  $$x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$

### 6.2 High Dimensionality (Curse of Dimensionality)
In high dimensions, distance metrics lose contrast ($D_{\max} \approx D_{\min}$), making distance-based clustering less effective.
* **Mitigation:** Perform Dimensionality Reduction (e.g., PCA, t-SNE, UMAP) prior to applying K-Means.

---

## Module 7: Complete Python Implementation

### 7.1 Scratch Implementation
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
            # Assignment Step
            distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
            labels = np.argmin(distances, axis=1)
            
            # Update Step
            new_centroids = np.array([X[labels == k].mean(axis=0) if np.sum(labels == k) > 0 
                                      else self.centroids[k] for k in range(self.k)])
            
            # Convergence Check
            if np.all(np.abs(new_centroids - self.centroids) < self.tol):
                break
                
            self.centroids = new_centroids
            
        return labels

    def predict(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)
```

### 7.2 Production Implementation using Scikit-Learn
```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import numpy as np

# 1. Dummy Data Generation
X = np.random.rand(500, 5)

# 2. Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Model Training with K-Means++
kmeans = KMeans(
    n_clusters=4,
    init='k-means++',
    n_init=10,
    max_iter=300,
    random_state=42
)

cluster_labels = kmeans.fit_predict(X_scaled)

# 4. Evaluation
inertia = kmeans.inertia_
sil_score = silhouette_score(X_scaled, cluster_labels)

print(f"Inertia (WCSS): {inertia:.4f}")
print(f"Silhouette Score: {sil_score:.4f}")
```

---

## Module 8: Variations and Relatives of K-Means

1. **Mini-Batch K-Means:** Uses small random subsets (batches) of data to update centroids at each step. Significantly reduces computation time for massive datasets.
2. **K-Medoids (PAM - Partitioning Around Medoids):** Uses actual data points (medoids) instead of mean values as centers. More robust to noise and outliers.
3. **K-Modes / K-Prototypes:** Adaptations designed to handle categorical data (K-Modes) or mixed numerical/categorical data (K-Prototypes).

---

## Module 9: Summary Comparison Matrix

| Property | K-Means |
| :--- | :--- |
| **Type** | Partitional Unsupervised Clustering |
| **Computational Complexity** | $O(N \cdot K \cdot I \cdot d)$ where $I$ = iterations, $d$ = dimensions |
| **Assumed Cluster Shape** | Convex, spherical clusters |
| **Sensitivity** | Sensitive to feature scaling, outliers, and initial seed choice |
| **Key Strengths** | Highly scalable, simple to implement, linear time complexity |
| **Key Weaknesses** | Must pre-specify $K$, struggles with non-spherical shapes and varying density |