import numpy as np


class SVMClassifier:
    def __init__(self, lr=0.001, lambda_=0.01, n_iterations=1000):
        self.lr = lr
        self.lambda_ = lambda_
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        m, n = X.shape

        # Convert labels from {0,1} to {-1,+1}
        y = np.where(y <= 0, -1, 1)

        self.weights = np.zeros(n)
        self.bias = 0

        for _ in range(self.n_iterations):

            for idx, x_i in enumerate(X):

                condition = y[idx] * (np.dot(x_i, self.weights) + self.bias) >= 1

                if condition:
                    dw = 2 * self.lambda_ * self.weights
                    db = 0

                else:
                    dw = 2 * self.lambda_ * self.weights - y[idx] * x_i
                    db = -y[idx]

                self.weights -= self.lr * dw
                self.bias -= self.lr * db

    def predict(self, X):
        linear = np.dot(X, self.weights) + self.bias
        return np.where(linear >= 0, 1, 0)

    def accuracy(self, X, y):
        predictions = self.predict(X)
        return np.mean(predictions == y)


def main():

    np.random.seed(42)

    X = np.random.randn(200, 2)

    y = (3 * X[:, 0] - 2 * X[:, 1] + 1 > 0).astype(int)

    model = SVMClassifier(
        lr=0.001,
        lambda_=0.01,
        n_iterations=1000
    )

    model.fit(X, y)

    print("Weights:", model.weights)
    print("Bias:", model.bias)
    print("Accuracy:", model.accuracy(X, y))


if __name__ == "__main__":
    main()