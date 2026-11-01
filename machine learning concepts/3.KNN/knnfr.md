# L'Algorithme des $k$ Plus Proches Voisins (KNN)

### Qu'est-ce que l'algorithme KNN ?
Le KNN (*K-Nearest Neighbors*) est un algorithme d'apprentissage supervisé simple et largement utilisé pour les tâches de **classification** et de **régression**. Il fonctionne en identifiant les $k$ points de données les plus proches d'une entrée donnée et en effectuant des prédictions basées sur la classe majoritaire ou la valeur moyenne de ces voisins.

- Il classe les données en fonction de leur similarité avec les points de données proches.
- Il utilise des **métriques de distance** (comme la distance euclidienne) pour trouver les voisins les plus proches.
- Puisqu'il ne fait aucune hypothèse sur la distribution sous-jacente des données, il s'agit d'une méthode **non paramétrique** et **basée sur les instances** (*instance-based learning*).

> **Apprentissage paresseux (*Lazy Learning*) :** Le KNN est qualifié d'algorithme d'apprentissage paresseux car il n'apprend pas immédiatement à partir de l'ensemble d'entraînement. Au lieu de cela, il stocke l'intégralité du jeu de données et n'effectue les calculs qu'au moment de la classification (lors de la prédiction).

*Exemple :* Supposons que nous souhaitions classifier un nouveau fruit en fonction de sa forme et de sa taille par rapport à des exemples connus (les points verts représentent la Catégorie 1, les points rouges la Catégorie 2). Le nouveau point examine ses voisins les plus proches (dans le cercle) : si la majorité de ses voisins sont rouges, le KNN prédit qu'il appartient à la Catégorie 2.

---

## 1. La valeur de $k$ dans KNN
Dans l'algorithme KNN, $k$ est un hyperparamètre qui définit le nombre de voisins proches à examiner pour prendre une décision.

### Comment choisir la valeur optimale de $k$ ?
- **Si $k$ est trop petit :** Le modèle devient sensible au bruit et aux valeurs aberrantes (*outliers*), ce qui peut mener à du surapprentissage (*overfitting*).
- **Si $k$ est trop grand :** Le modèle devient trop simple, risque de lisser les frontières de décision et de passer à côté de motifs importants (sous-apprentissage / *underfitting*).

### Méthodes statistiques pour sélectionner $k$ :
1. **Validation croisée (*Cross-Validation*) :** Consiste à diviser le jeu de données en $k$ parties, à entraîner le modèle sur certaines et à le tester sur les autres, en répétant l'opération pour trouver le $k$ idéal.
2. **Méthode du coude (*Elbow Method*) :** On trace un graphique représentant le taux d'erreur en fonction des différentes valeurs de $k$. Le point où la courbe change brusquement de direction (formant un « coude ») indique généralement le meilleur choix de $k$.
3. **Privilégier les valeurs impaires :** Pour les problèmes de classification binaire, il est recommandé d'utiliser un nombre impair pour $k$ afin d'éviter les situations d'égalité (*ties*) lors du vote majoritaire.

---

## 2. Métriques de distance utilisées
Le KNN s'appuie sur des mesures géométriques pour identifier les voisins les plus proches :

1. **Distance euclidienne :** Représente la distance en ligne droite entre deux points dans un espace (le plus court chemin à vol d'oiseau).
   $$\sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}$$
2. **Distance de Manhattan (*Taxicab Distance*) :** Calcule la distance en suivant uniquement des mouvements horizontaux et verticaux (comme un taxi se déplaçant dans les rues d'une grille urbaine).
   $$\sum_{i=1}^{n} |x_i - y_i |$$
3. **Distance de Minkowski :** Une formule généralisée qui englobe à la fois la distance euclidienne et la distance de Manhattan grâce à un paramètre $p$ :
   - Si $p = 2$, elle correspond à la **distance euclidienne**.
   - Si $p = 1$, elle correspond à la **distance de Manhattan**.

---

## 3. Fonctionnement de l'algorithme
L'algorithme KNN opère selon le principe de la similarité pour prédire l'étiquette ou la valeur d'un nouveau point de données :

- **Étape 1 : Sélection de la valeur de $k$**  
  Définir le nombre de voisins proches à considérer ($k$).
- **Étape 2 : Calcul des distances**  
  Mesurer la distance entre le point cible et tous les points de l'ensemble d'entraînement (généralement via la distance euclidienne).
- **Étape 3 : Identification des voisins les plus proches**  
  Sélectionner les $k$ points de données présentant les distances les plus faibles par rapport au point cible.
- **Étape 4 : Vote majoritaire ou calcul de la moyenne**  
  - **En classification :** Le modèle applique un vote majoritaire parmi les $k$ voisins et attribue la classe la plus fréquente au point cible (ex. : spam ou non spam, classe majoritaire grise).
  - **En régression :** Le modèle calcule la moyenne des valeurs numériques des $k$ voisins pour prédire la valeur continue du nouveau point.