import numpy as np


class LinearRegression:
    def __init__(self, lr=0.01, n_iterations=1000, penalty=None, lambda_=0.01):
        self.lr = lr
        self.n_iterations = n_iterations
        self.penalty = penalty
        self.lambda_ = lambda_
        self.weights = None
        self.bias = None
        self.losses = []

    def fit(self, X, y):
        m, n = X.shape

        # Initialize parameters
        self.weights = np.zeros(n)
        self.bias = 0

        # Gradient Descent
        for _ in range(self.n_iterations):

            # Predictions
            y_pred = self.predict(X)

            # Compute gradients
            dw = (1 / m) * np.dot(X.T, (y_pred - y))
            db = (1 / m) * np.sum(y_pred - y)

            # L2 Regularization (Ridge)
            if self.penalty == "l2":
                dw += (self.lambda_ / m) * self.weights

            # L1 Regularization (Lasso)
            elif self.penalty == "l1":
                dw += (self.lambda_ / m) * np.sign(self.weights)

            # Update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

            # Compute MSE loss
            loss = np.mean((y_pred - y) ** 2)

            # Add regularization term to the loss
            if self.penalty == "l2":
                loss += (self.lambda_ / (2 * m)) * np.sum(self.weights ** 2)

            elif self.penalty == "l1":
                loss += (self.lambda_ / m) * np.sum(np.abs(self.weights))

            self.losses.append(loss)

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias


def main():
    np.random.seed(42)

    # Create synthetic dataset
    X = 2 * np.random.rand(100, 1)

    # True equation:
    # y = 4 + 3x + noise
    y = 4 + 3 * X[:, 0] + np.random.randn(100)

    # Train model
    model = LinearRegression(
        lr=0.05,
        n_iterations=1000,
        penalty=None  
    )

    model.fit(X, y)

    predictions = model.predict(X)

    print("========== RESULTS ==========")
    print("Learned weight :", model.weights)
    print("Learned bias   :", model.bias)
    print("Final loss     :", model.losses[-1])

    print("\nFirst 10 Predictions")
    print("-------------------------------")
    for actual, pred in zip(y[:10], predictions[:10]):
        print(f"Actual: {actual:.2f}   Predicted: {pred:.2f}")


if __name__ == "__main__":
    main()

