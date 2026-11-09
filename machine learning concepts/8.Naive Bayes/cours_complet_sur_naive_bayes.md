# Cours Complet : L'Algorithme de Classification Naive Bayes (Bayes Naïf)

Bienvenue dans ce cours détaillé sur l'algorithme de **Naive Bayes**. Ce modèle d'apprentissage supervisé probabiliste est largement utilisé pour les problèmes de classification, notamment le traitement du langage naturel (NLP), le filtrage de spams et l'analyse de sentiments.

## Module 1: Introduction & Fondements Probabilistes

### 1.1 Qu'est-ce que Naive Bayes ?

Naive Bayes est un algorithme de classification supervisée fondé sur le **Théorème de Bayes**. Il est qualifié de **"naïf"** car il repose sur une hypothèse simplificatrice majeure : **l'indépendance conditionnelle des variables (caractéristiques)** sachant la classe.

### 1.2 Le Théorème de Bayes

Le théorème de Bayes permet de calculer la probabilité a posteriori d'un événement sachant la réalisation d'un autre événement :

$$
P(Y \mid X) = \frac{P(X \mid Y) \cdot P(Y)}{P(X)}
$$

Où :
* $P(Y \mid X)$ est la **probabilité a posteriori** (Posterior) de la classe $Y$ sachant les données $X$.
* $P(X \mid Y)$ est la **vraisemblance** (Likelihood) d'observer les données $X$ sachant la classe $Y$.
* $P(Y)$ est la **probabilité a priori** (Prior) de la classe $Y$.
* $P(X)$ est la **probabilité marginale** des données (évidence/marginal likelihood).

---

## Module 2: Formulation Mathématique de Naive Bayes

### 2.1 Hypothèse d'Indépendance Conditionnelle

Soit un vecteur de caractéristiques $X = (x_1, x_2, \dots, x_d)$ et une classe $y_k$.

D'après le théorème de Bayes :

$$
P(y_k \mid x_1, x_2, \dots, x_d) = \frac{P(x_1, x_2, \dots, x_d \mid y_k) \cdot P(y_k)}{P(x_1, x_2, \dots, x_d)}
$$

L'hypothèse "naïve" pose que toutes les variables $x_j$ sont indépendantes les unes des autres conditionnellement à la classe $y_k$ :

$$
P(x_1, x_2, \dots, x_d \mid y_k) = \prod_{j=1}^{d} P(x_j \mid y_k)
$$

### 2.2 Règle de Décision (Maximum A Posteriori - MAP)

Puisque le dénominateur $P(X)$ est constant pour toutes les classes $y_k$, la règle de décision choisit la classe qui maximise le numérateur :

$$
\hat{y} = \arg\max_{y_k} \left( P(y_k) \prod_{j=1}^{d} P(x_j \mid y_k) \right)
$$

Pour éviter les sous-flux numériques (underflow) dus à la multiplication de probabilités très petites, on utilise la somme des log-probabilités :

$$
\hat{y} = \arg\max_{y_k} \left( \log P(y_k) + \sum_{j=1}^{d} \log P(x_j \mid y_k) \right)
$$

---

## Module 3: Variantes Principes de Naive Bayes

Selon la nature des caractéristiques $x_j$, différents modèles de probabilité sont appliqués pour estimer la vraisemblance $P(x_j \mid y_k)$.

### 3.1 Gaussian Naive Bayes (Données Continues)

Lorsque les variables sont continues, on suppose qu'elles suivent une loi normale (gaussienne) au sein de chaque classe :

$$
P(x_j \mid y_k) = \frac{1}{\sqrt{2\pi\sigma_{k,j}^2}} \exp \left( -\frac{(x_j - \mu_{k,j})^2}{2\sigma_{k,j}^2} \right)
$$

* $\mu_{k,j}$ est la moyenne de la caractéristique $j$ pour la classe $y_k$.
* $\sigma_{k,j}^2$ est la variance de la caractéristique $j$ pour la classe $y_k$.

### 3.2 Multinomial Naive Bayes (Données Discrètes / Comptages)

Utilisé pour les fréquences d'occurrence (ex. nombre de mots dans un document) :

$$
P(x_j \mid y_k) = \frac{N_{y_k, j} + \alpha}{N_{y_k} + \alpha \cdot d}
$$

* $N_{y_k, j}$ : Nombre total de fois où la variable $j$ apparaît dans la classe $y_k$.
* $N_{y_k}$ : Nombre total d'occurrences de toutes les variables dans la classe $y_k$.
* $\alpha$ : Paramètre de lissage (**Lissage de Laplace** si $\alpha = 1$).

### 3.3 Bernoulli Naive Bayes (Données Binaires)

Utilisé lorsque les variables sont booléennes (présence/absence d'un mot ou d'un attribut) :

$$
P(x_j \mid y_k) = p_{k,j}^{x_j} (1 - p_{k,j})^{(1 - x_j)} \quad \text{où } x_j \in \{0, 1\}
$$

---

## Module 4: Lissage de Laplace (Laplace Smoothing)

### 4.1 Le Problème de la Probabilité Zéro (Zero Frequency Problem)

Si une combinaison donnée de variable et de classe $P(x_j \mid y_k)$ n'apparaît jamais dans le jeu d'entraînement :

$$
P(x_j \mid y_k) = 0 \implies \prod_{j=1}^{d} P(x_j \mid y_k) = 0
$$

La probabilité globale de la classe devient nulle, annulant l'impact des autres caractéristiques.

### 4.2 Solution : Additive / Laplace Smoothing

Pour pallier ce problème, on ajoute une valeur constante $\alpha > 0$ au numérateur et $\alpha \cdot d$ au dénominateur :

$$
P(x_j \mid y_k) = \frac{\text{count}(x_j, y_k) + \alpha}{\text{count}(y_k) + \alpha \cdot d}
$$

---

## Module 5: Implémentation Complète en Python

### 5.1 Implémentation "from scratch" de Gaussian Naive Bayes

```python
import numpy as np

class GaussianNaiveBayesScratch:
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.classes = np.unique(y)
        n_classes = len(self.classes)

        # Initialisation de la moyenne, de la variance et des probabilités a priori
        self.mean = np.zeros((n_classes, n_features))
        self.var = np.zeros((n_classes, n_features))
        self.priors = np.zeros(n_classes)

        for idx, c in enumerate(self.classes):
            X_c = X[y == c]
            self.mean[idx, :] = X_c.mean(axis=0)
            self.var[idx, :] = X_c.var(axis=0)
            self.priors[idx] = X_c.shape[0] / float(n_samples)

    def predict(self, X):
        return np.array([self._predict(x) for x in X])

    def _predict(self, x):
        posteriors = []

        for idx, c in enumerate(self.classes):
            prior = np.log(self.priors[idx])
            class_conditional = np.sum(np.log(self._pdf(idx, x)))
            posterior = prior + class_conditional
            posteriors.append(posterior)

        return self.classes[np.argmax(posteriors)]

    def _pdf(self, class_idx, x):
        mean = self.mean[class_idx]
        var = self.var[class_idx]
        numerator = np.exp(-((x - mean) ** 2) / (2 * var + 1e-9))
        denominator = np.sqrt(2 * np.pi * var + 1e-9)
        return numerator / denominator
```

### 5.2 Implémentation Multinomial Naive Bayes avec Scikit-Learn

```python
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# 1. Données textuelles d'exemple
documents = [
    "Offre exceptionnelle, gagnez de l'argent facilement",
    "Réunion d'équipe demain à 10 heures",
    "Votre facture de téléphone est disponible",
    "Urgent, cliquez ici pour réclamer votre prix gratuit",
    "Le rapport de projet doit être soumis vendredi"
]
labels = [1, 0, 0, 1, 0] # 1: Spam, 0: Non-Spam

# 2. Vectorisation (Extraction de fréquences)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

# 3. Entraînement du modèle Multinomial Naive Bayes
model = MultinomialNB(alpha=1.0) # alpha=1.0 correspond au lissage de Laplace
model.fit(X, labels)

# 4. Prédiction
predictions = model.predict(X)
print("Précision :", accuracy_score(labels, predictions))
```

---

## Module 6: Tableau Récapitulatif

| Propriété | Naive Bayes |
| ----- | ----- |
| **Type** | Classification supervisée probabiliste |
| **Complexité Temporelle (Entraînement)** | $O(N \cdot d)$ — extrêmement rapide |
| **Complexité Temporelle (Prédiction)** | $O(K \cdot d)$ par échantillon |
| **Hypothèse Majeure** | Indépendance conditionnelle des variables sachant la classe |
| **Forces Principales** | Très rapide, efficace sur la haute dimension (ex. texte), peu de données requises |
| **Limites Principales** | L'hypothèse d'indépendance est rarement vraie en pratique ; sensible aux données déséquilibrées |
