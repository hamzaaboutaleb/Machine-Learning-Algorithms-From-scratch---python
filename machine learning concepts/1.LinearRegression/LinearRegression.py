import numpy as np 

class LinearRegression: 
    def __init__(self,lr=0.01,n_iterations=1000,penalty=None):
        self.lr=lr
        self.n_iterations=n_iterations
        self.bias=None
        self.weights=None
        self.penalty=penalty

    def fit(self,X,y):
        m,n=X.shape
        self.weights=np.zeros(n)
        self.bias=0
        for _ in range(self.n_iterations):
            y_pred=self.predict(X)

            dw=(1/m)*np.dot(X.T,y_pred-y)
            db=(1/m)*np.sum(y-y_pred)

            self.weights-=self.lr*dw
            self.bias-=self.lr*db



    def predict(self,X):
        return X.dot(self.weights)+self.bias