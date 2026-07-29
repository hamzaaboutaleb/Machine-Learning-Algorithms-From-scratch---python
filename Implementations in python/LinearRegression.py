import numpy as np

class LinearRegression:

    def __init__(self, lr=0.001, n_iterations=1000, penalty=None, lambda_=0.01):
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

        for i in range(self.n_iterations):

            # Forward propagation
            y_pred = self.predict(X)

            # Compute gradients
            dw = (1/m) * np.dot(X.T, (y_pred - y))
            db = (1/m) * np.sum(y_pred - y)

            # Add penalty to weights gradient
            if self.penalty == "l2":
                # Ridge regression
                dw += (self.lambda_ / m) * self.weights

            elif self.penalty == "l1":
                # Lasso regression
                dw += (self.lambda_ / m) * np.sign(self.weights)


            # Update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db


            # Store loss
            loss = np.mean((y_pred - y) ** 2)

            if self.penalty == "l2":
                loss += (self.lambda_ / (2*m)) * np.sum(self.weights ** 2)

            elif self.penalty == "l1":
                loss += (self.lambda_ / m) * np.sum(np.abs(self.weights))

            self.losses.append(loss)


            # Print progress
            if i % 100 == 0:
                print(f"Iteration {i}, Loss: {loss}")


    def predict(self, X):
        return np.dot(X, self.weights) + self.bias