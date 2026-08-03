import numpy as np 


class LogisticRegression:
    def __init__(self,lr=0.01,n_iterations=1000,penalty=None,lambda_=0.01):
        self.lr=lr
        self.n_iterations=n_iterations 
        self.weights=None
        self.bias=None 
        self.lambda_=lambda_
        self.penalty=penalty 
        self.losses=[]

    def sigmoid(self,z):
        z=np.clip(z,-500,500)
        return 1/(1+np.exp(-z))

    def fit(self,X,y):
        m,n=X.shape
        self.weights=np.zeros(n)
        self.bias=0
        for _ in range(self.n_iterations):
            # linear model 
            linear = np.dot(X,self.weights)+self.bias

            #Probabilities 
            y_pred = self.sigmoid(linear)

            dw=(1/m)*np.dot(X.T,y_pred-y)
            db=(1/m)*np.sum(y_pred-y)
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            if self.penalty == "l2":
                dw += (self.lambda_ / m) * self.weights

            # L1 Regularization
            elif self.penalty == "l1":
                dw += (self.lambda_ / m) * np.sign(self.weights)

            epsilon=1e-5 
            y_pred_clip=np.clip(y_pred,epsilon,1-epsilon)

            loss = -np.mean(
                 y * np.log(y_pred_clip)
                + (1 - y) * np.log(1 - y_pred_clip)
            )
            if self.penalty == "l2":
                loss += (self.lambda_ / (2 * m)) * np.sum(self.weights ** 2)

            elif self.penalty == "l1":
                loss += (self.lambda_ / m) * np.sum(np.abs(self.weights))

            self.losses.append(loss)

    def predict_proba(self,X):
        linear= np.dot(X,self.weights)+self.bias
        return self.sigmoid(linear)

    def predict(self,X):
        probabilities=self.predict_proba(X)
        return (probabilities>=0.5).astype(int)

    def accuracy(self,X,y):
        predictions = self.predict(X)
        return np.mean(predictions==y)
    

def main():
    np.random.seed(42)

    # Generate synthetic binary classification dataset
    n_samples = 200

    X = np.random.randn(n_samples, 2)

    # True decision boundary:
    # 3*x1 - 2*x2 + 1 > 0  => class 1
    linear = 3 * X[:, 0] - 2 * X[:, 1] + 1

    probabilities = 1 / (1 + np.exp(-linear))

    y = (probabilities >= 0.5).astype(int)

    # Train the model
    model = LogisticRegression(
        lr=0.1,
        n_iterations=3000,
        penalty=None
    )

    model.fit(X, y)

    predictions = model.predict(X)

    print("========== RESULTS ==========")
    print("Weights :", model.weights)
    print("Bias    :", model.bias)
    print("Final Loss :", model.losses[-1])
    print("Accuracy :", model.accuracy(X, y))

    print("\nFirst 10 Predictions")
    print("------------------------------")
    for actual, pred, prob in zip(
        y[:10],
        predictions[:10],
        model.predict_proba(X[:10])
    ):
        print(
            f"Actual: {actual}   "
            f"Predicted: {pred}   "
            f"Probability: {prob:.4f}"
        )


if __name__ == "__main__":
    main()