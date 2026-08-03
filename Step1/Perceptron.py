import numpy as np


class Perceptron:

    def __init__(self,lr=0.05,n_iterations=1000):
        self.n_iterations=n_iterations
        self.lr=lr
        self.bias=None
        self.weights=None

    def activation(self,x):
        return np.where(x>=0,1,0)

    def fit(self,X,y):
        m,n=X.shape

        self.weights=np.zeros(n)
        self.bias=0

        for _ in range(self.n_iterations):

            for i in range(m):
                linear=np.dot(X[i],self.weights)+self.bias 
                y_pred=self.activation(linear)

                update=self.lr*(y[i]-y_pred)

                self.weights+= update*X[i]
                self.bias+= update

    def predict(self,X):
        linear=np.dot(X,self.weights)+self.bias
        return self.activation(linear)

    def accuracy(self,X,y):
        predictions=self.predict(X)
        return np.mean(predictions==y)
    

def main():

    np.random.seed(42)

    n_samples = 200

    X = np.random.randn(n_samples, 2)

    # Linearly separable dataset
    y = (3 * X[:, 0] - 2 * X[:, 1] + 1 > 0).astype(int)

    model = Perceptron(
        lr=0.01,
        n_iterations=100
    )

    model.fit(X, y)

    predictions = model.predict(X)

    print("========== RESULTS ==========")
    print("Weights :", model.weights)
    print("Bias    :", model.bias)
    print("Accuracy:", model.accuracy(X, y))

    print("\nFirst 10 Predictions")
    print("------------------------------")

    for actual, pred in zip(y[:10], predictions[:10]):
        print(f"Actual: {actual}   Predicted: {pred}")


if __name__ == "__main__":
    main()