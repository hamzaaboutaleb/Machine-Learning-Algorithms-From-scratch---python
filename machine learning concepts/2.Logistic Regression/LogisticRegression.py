import numpy as np 

class LogisticRegression:

    def __init__(self,lr=0.001,n_iterations=1000,alpha=0.01,penalty=None):
        self.penalty=penalty
        self.alpha=alpha
        self.weights=None 
        self.bias=None
        self.lr=lr
        self.n_iterations 

    def sigmoid(self,z):
        return 1/(1+np.exp(-z))

    def fit(self,X,y):
        
        m,n=X.shape 
        self.weights=np.zeros(n)
        self.bias=0

        for _ in range(self.n_iterations): 
            y_pred=np.dot(self.X,self.weights)+self.bias

            dw=(1/m)*np.dot(X.T,y_pred-y)
            db=(1/m)*np.sum(y_pred-y)

            if self.penalty=="L1":
                dw+=self.alpha*np.sign(self.weights)
            elif self.penalty=="L2":
                dw+=self.alpha*self.weights

            self.weights-=self.lr*dw
            self.bias-=self.lr*db
    def predict_proba(self,X):
        z=np.dot(X,self.weights)+self.bias
        return self.sigmoid(z)
    def predict(self,X):
        predict_probabilities=self.predict_proba(X)
        return (self.predict_proba>=0.5).astype(int)

    def log_loss(self, y_true, y_proba):
        eps = 1e-15
        y_proba = np.clip(y_proba, eps, 1 - eps)

        return -np.mean(
            y_true * np.log(y_proba)
            + (1 - y_true) * np.log(1 - y_proba)
        )

    def accuracy(self, y_true, y_pred):
        return np.mean(y_true == y_pred)

    # Precision
    def precision(self, y_true, y_pred):
        tp = np.sum((y_true == 1) & (y_pred == 1))
        fp = np.sum((y_true == 0) & (y_pred == 1))

        return tp / (tp + fp) if (tp + fp) > 0 else 0.0

    # Recall
    def recall(self, y_true, y_pred):
        tp = np.sum((y_true == 1) & (y_pred == 1))
        fn = np.sum((y_true == 1) & (y_pred == 0))

        return tp / (tp + fn) if (tp + fn) > 0 else 0.0

    # F1-score
    def f1_score(self, y_true, y_pred):
        p = self.precision(y_true, y_pred)
        r = self.recall(y_true, y_pred)

        return 2 * p * r / (p + r) if (p + r) > 0 else 0.0
