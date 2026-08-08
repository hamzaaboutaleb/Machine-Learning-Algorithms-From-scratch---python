import numpy as np

class MultinomialNaiveBayes:

    def __init__(self, alpha=1.0):
        self.alpha = alpha
        self.classes = None
        self.feature_log_prob = None
        self.class_log_prior = None

    def fit(self, X, y):
        X = np.asarray(X)
        y = np.asarray(y)

        self.classes = np.unique(y)

        n_classes = len(self.classes)
        n_features = X.shape[1]

        # Store log P(class)
        self.class_log_prior = np.zeros(n_classes)

        # Store log P(feature | class)
        self.feature_log_prob = np.zeros((n_classes, n_features))

        for i, cls in enumerate(self.classes):

            # Samples belonging to this class
            X_class = X[y == cls]

            # Number of samples in this class
            n_class_samples = X_class.shape[0]

            # Prior probability P(class)
            self.class_log_prior[i] = np.log(
                n_class_samples / X.shape[0]
            )

            # Total count of each feature for this class
            feature_counts = X_class.sum(axis=0)

            # Total number of feature occurrences
            total_count = feature_counts.sum()

            # Laplace smoothing
            smoothed_counts = feature_counts + self.alpha

            smoothed_total = total_count + self.alpha * n_features

            # P(feature | class)
            probabilities = smoothed_counts / smoothed_total

            # Store log probabilities
            self.feature_log_prob[i] = np.log(probabilities)

        return self

    def predict(self, X):
        X = np.asarray(X)

        predictions = []

        for x in X:

            # Start with log prior
            log_probs = self.class_log_prior.copy()

            # Add log P(feature | class) for every feature
            log_probs += x @ self.feature_log_prob.T

            # Choose class with highest probability
            predicted_class = self.classes[np.argmax(log_probs)]

            predictions.append(predicted_class)

        return np.array(predictions)

    def predict_proba(self, X):
        X = np.asarray(X)

        probabilities = []

        for x in X:

            log_probs = self.class_log_prior.copy()
            log_probs += x @ self.feature_log_prob.T

            # Convert log probabilities back to probabilities
            probs = np.exp(log_probs)

            # Normalize
            probs = probs / probs.sum()

            probabilities.append(probs)

        return np.array(probabilities)