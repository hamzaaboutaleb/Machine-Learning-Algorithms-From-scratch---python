import numpy as np


class SVR:
    def __init__(self, lr=0.001, lambda_=0.01, epsilon=0.1, n_iterations=1000):
        self.lr = lr
        self.lambda_ = lambda_
        self.epsilon = epsilon
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        m, n = X.shape

        self.weights = np.zeros(n)
        self.bias = 0

        for _ in range(self.n_iterations):

            for idx, x_i in enumerate(X):

                prediction = np.dot(x_i, self.weights) + self.bias

                error = prediction - y[idx]

                if abs(error) <= self.epsilon:
                    dw = 2 * self.lambda_ * self.weights
                    db = 0

                elif error > self.epsilon:
                    dw = 2 * self.lambda_ * self.weights + x_i
                    db = 1

                else:
                    dw = 2 * self.lambda_ * self.weights - x_i
                    db = -1

                self.weights -= self.lr * dw
                self.bias -= self.lr * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

    def mse(self, X, y):
        predictions = self.predict(X)
        return np.mean((predictions - y) ** 2)


def main():

    np.random.seed(42)

    X = 2 * np.random.rand(200, 1)

    y = 4 + 3 * X[:, 0] + np.random.randn(200)

    model = SVR(
        lr=0.001,
        lambda_=0.01,
        epsilon=0.2,
        n_iterations=2000
    )

    model.fit(X, y)

    print("Weights:", model.weights)
    print("Bias:", model.bias)
    print("MSE:", model.mse(X, y))


if __name__ == "__main__":
    main()