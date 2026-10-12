
import numpy as np

class LinearRegression:

    def __init__(self, lr=0.001, n_iterations=1000,
                 penalty=None, alpha=0.01):
        self.lr = lr
        self.n_iterations = n_iterations
        self.bias = None
        self.weights = None
        self.penalty = penalty
        self.alpha = alpha

    def fit(self, X, y):
        m, n = X.shape

        self.weights = np.zeros(n)
        self.bias = 0

        for _ in range(self.n_iterations):
            y_pred = np.dot(X, self.weights) + self.bias

            dw = (1 / m) * np.dot(X.T, y_pred - y)
            db = (1 / m) * np.sum(y_pred - y)

            if self.penalty == "L1":
                dw += self.alpha * np.sign(self.weights)

            elif self.penalty == "L2":
                dw += self.alpha * self.weights

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
