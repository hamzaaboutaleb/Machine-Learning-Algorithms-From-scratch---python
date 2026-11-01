# La Régression Logistique

### Qu'est-ce que la régression logistique ?
La régression logistique est un algorithme d'apprentissage supervisé (*supervised machine learning*) principalement utilisé pour résoudre des **problèmes de classification**. Contrairement à la régression linéaire qui prédit des valeurs continues, la régression logistique prédit la **probabilité** qu'une entrée appartienne à une classe spécifique.

- Elle est principalement utilisée pour la **classification binaire**, où la sortie prend l'une de deux catégories possibles (ex. : Oui/Non, Vrai/Faux, 0 ou 1).
- Elle utilise la **fonction sigmoïde** pour transformer les scores bruts en une valeur de probabilité comprise strictement entre 0 et 1.

---

## 1. Types de régression logistique
1. **Régression logistique binomiale :** Utilisée lorsque la variable dépendante possède exactement deux catégories. C'est la forme la plus courante pour la classification binaire.
2. **Régression logistique multinomiale :** Utilisée lorsque la variable dépendante comporte trois catégories ou plus sans ordre logique particulier (ex. : type de fruit : pomme, banane, orange).
3. **Régression logistique ordinale :** Utilisée lorsque la variable dépendante comporte trois catégories ou plus possédant un ordre naturel (ex. : niveau de satisfaction : faible, moyen, élevé).

---

## 2. Hypothèses fondamentales
Pour garantir la fiabilité et la robustesse d'un modèle de régression logistique, plusieurs conditions doivent être réunies :
1. **Observations indépendantes :** Chaque point de données doit être indépendant des autres (pas de corrélation temporelle ou structurelle cachée entre les observations).
2. **Variable dépendante binaire :** La variable cible est généralement binaire (pour les problèmes multiclasses, on utilise des extensions comme la régression Softmax).
3. **Linéarité des log-cotes (*log-odds*) :** Les variables indépendantes doivent entretenir une relation linéaire avec le logarithme des cotes de la variable dépendante.
4. **Absence de valeurs aberrantes extrêmes (*outliers*) :** Les valeurs extrêmes peuvent fausser l'estimation des coefficients et dégrader les performances du modèle.
5. **Taille d'échantillon suffisante :** Un jeu de données suffisamment grand est nécessaire pour obtenir des estimations stables et fiables.

---

## 3. Comprendre la fonction sigmoïde
- La fonction sigmoïde est l'élément central de la régression logistique. Elle convertit n'importe quel nombre réel en une probabilité comprise entre 0 et 1.
- Sa représentation graphique forme une **courbe en S** (courbe logistique). Elle est idéale pour modéliser des probabilités puisque ces dernières ne peuvent dépasser les bornes 0 et 1.
- Pour prendre une décision de classification, on définit un **seuil de décision** (*threshold*), généralement fixé à **0,5** :
  - Si la sortie de la sigmoïde est **$\ge 0,5$**, l'entrée est classée dans la **Classe 1**.
  - Si elle est **$< 0,5$**, l'entrée est classée dans la **Classe 0**.

---

## 4. Fonctionnement et mécanisme
La régression logistique calcule d'abord une combinaison linéaire des caractéristiques d'entrée ($z = wX + b$), puis applique la fonction sigmoïde pour obtenir une probabilité.

1. **Combinaison linéaire :**
   $$z = w_1x_1 + w_2x_2 + ... + w_kx_k + b$$
   *(Où $z$ est une valeur continue, similaire à la sortie d'une régression linéaire).*
2. **Application de la fonction sigmoïde ($\sigma$) :**
   $$\sigma(z) = \frac{1}{1 + e^{-z}}$$
   Cette étape transforme la variable continue en une probabilité de prédiction de classe comprise entre 0 et 1.

---

## 5. Équation de la régression logistique et des cotes (*Odds*)
Le modèle s'appuie sur la notion de **cotes** (*odds*), qui représentent le rapport entre la probabilité qu'un événement se produise et la probabilité qu'il ne se produise pas :
$$\text{Odds} = \frac{p}{1 - p}$$

En appliquant le logarithme népérien aux cotes, on obtient le **log-logit** (ou log-cotes), qui relie linéairement les caractéristiques au modèle :
$$\text{Logit}(p) = \ln\left(\frac{p}{1 - p}\right) = wX + b$$

En isolant la probabilité $p$ (ou $P(Y=1)$), on obtient l'équation finale de la régression logistique :
$$P(Y=1 | X) = \frac{1}{1 + e^{-(wX + b)}}$$

---

## 6. Fonction de vraisemblance (*Likelihood function*)
L'objectif de l'optimisation est de trouver les poids $w$ et le biais $b$ qui **maximisent la vraisemblance** d'observer les données réelles (méthode de l'estimation du maximum de vraisemblance - *Maximum Likelihood Estimation*, MLE). 
Contrairement à la régression linéaire où l'on minimise les moindres carrés, on utilise ici une fonction de coût basée sur l'entropie croisée (*Binary Cross-Entropy*).

---

## Terminologie clé
1. **Variables indépendantes :** Caractéristiques d'entrée ou prédicteurs utilisés pour estimer la cible.
2. **Variable dépendante :** Variable cible catégorielle que l'on cherche à prédire.
3. **Cotes (*Odds*) :** Rapport de la probabilité qu'un événement se réalise sur la probabilité qu'il ne se réalise pas.
4. **Log-cotes (*Log-odds* ou *Logit*) :** Logarithme népérien des cotes, modélisé comme une combinaison linéaire des entrées.
5. **Coefficient ($w$) :** Paramètres estimés mesurant l'influence de chaque variable indépendante sur la variable cible.
6. **Intercept ($b$) :** Terme constant représentant les log-cotes lorsque toutes les variables d'entrée sont égales à zéro.
7. **Maximum de Vraisemblance (MLE) :** Méthode d'optimisation pour estimer les paramètres du modèle.

---

## Métriques d'évaluation pour la régression logistique
L'évaluation d'un modèle de classification requiert des métriques adaptées au-delà de la simple précision globale :
- **Matrice de confusion :** Tableau croisant les prédictions du modèle et les valeurs réelles (Vrais Positifs, Faux Positifs, Vrais Négatifs, Faux Négatifs).
- **Précision (*Precision*) :** Proportion de prédictions positives correctes parmi l'ensemble des prédictions positives.
- **Rappel (*Recall* ou Sensibilité) :** Proportion de vrais positifs détectés parmi l'ensemble des positifs réels.
- **Score F1 (*F1-Score*) :** Moyenne harmonique entre la précision et le rappel.
- **Courbe ROC et AUC :** Mesure la capacité du modèle à discriminer les classes à différents seuils de décision.