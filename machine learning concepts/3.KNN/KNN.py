
import numpy as np
from collections import Counter


class KNN:

    def __init__(self, k=3):
        self.k = k

    def euclidean_distance(self, x, y):
        return np.sqrt(np.sum((x - y) ** 2))

    def fit(self, X, y):
        self.X_train = np.asarray(X)
        self.y_train = np.asarray(y)

    def predict(self, X):
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)

    def _predict(self, x):
        distances = [
            self.euclidean_distance(x, x_train)
            for x_train in self.X_train
        ]

        closest_k = np.argsort(distances)[:self.k]

        indicators_closest_k = [
            self.y_train[i] for i in closest_k
        ]

        most_common_label = Counter(
            indicators_closest_k
        ).most_common(1)

        return most_common_label[0][0]
