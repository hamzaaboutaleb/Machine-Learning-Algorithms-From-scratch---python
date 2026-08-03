import numpy as np
from collections import Counter 

class KNN :

    def __init__(self,k=3):
        self.k = k
        self.X_train=None
        self.y_train=None


    def euclidean_distance(self,x,y):
        return np.sqrt(np.sum((x-y)**2))

    def fit(self,X,y):
        self.X_train=X
        self.y_train=y

    def _predict(self,x):
        distances = [self.euclidean_distance(x,x_train) for x_train in self.X_train]
        closest_k_neighbors = np.argsort(distances)[:self.k]
        indices_k_neighbors=[self.y_train[i] for i in closest_k_neighbors]
        most_common_label = Counter(indices_k_neighbors).most_common(1)[0][0]
        return most_common_label

    def predict(self,X): 
        predicted_labels=[self._predict(x) for x in X]
        return np.array(predicted_labels)
    def accuracy(self,X,y):
        predictions=self.predict(X)
        return np.mean(predictions==y)
if __name__ == "__main__":

    np.random.seed(42)

    class0 = np.random.randn(50, 2)
    class1 = np.random.randn(50, 2) + np.array([3, 3])

    X = np.vstack((class0, class1))
    y = np.array([0] * 50 + [1] * 50)

    model = KNN(k=5)

    model.fit(X, y)

    predictions = model.predict(X)

    print("Accuracy:", model.accuracy(X, y))

    print("\nFirst 10 Predictions")

    for actual, pred in zip(y[:10], predictions[:10]):
        print(f"Actual: {actual}  Predicted: {pred}")