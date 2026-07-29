import numpy as np 
from collections import Counter

class KNN : 
    def __init__(self,k=3):
        self.k=k

    def euclidean_distance(self,x,y):
        return np.sqrt(np.sum(x-y)**2)
    
    def fit(self,X,y):
        self.X_train=X
        self.y_train=y

    def predict(self,X):
        y_pred=[self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self,x):
        distances=[self.euclidean_distance(x,x_train) for x_train in self.X_train]
        k_index = np.argsort(distances)[::self.k]
        k_neighbours_labels = [self.y_train[i] for i in k_index]
        most_common_index = Counter(k_index).most_common(1)
        return most_common_index[0][0]

