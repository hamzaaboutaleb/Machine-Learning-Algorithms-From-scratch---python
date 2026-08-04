import numpy as np 

class Kmeans : 

    def __init__(self,n_clusters=3,max_iters=100,tol=1e-4):
        self.n_clusters=n_clusters
        self.max_iters=max_iters
        self.tol=tol
        self.centroids=None

    def fit(self,X):
        n_samples,n_features=X.shape

        # randomly initialize the centroids 
        random_indices= np.random.choice(n_samples,self.n_clusters,replace=False)
        self.centroids=X[random_indices]

        for _ in range(self.max_iters):

            # assigns each sample to the nearest centroids
            labels=self._assign_clusters(X)

            # compute new centroids 
            new_centroids=self._compute_centroids(X,labels)

            #check convergence
            shift=np.linalg.norm(new_centroids-self.centroids)

            self.centroids= new_centroids 
            if shift<self.tol:
                break

    def predict(self,X):
        return self._assign_clusters(X)

    def _assign_clusters(self,X):
        labels=[]
        for sample in X:
            distances=[self._euclidean_distance(sample,centroid) for centroid in self.centroids]
            labels.append(np.argmin(distances))
        return np.array(labels)

    def _compute_centroids(self,X,labels):
        centroids=[]
        for cluster in range(self.n_clusters):
            cluster_points=X[labels==cluster]

            if len(cluster_points)==0:
                # keep previous centroids if cluster become empty
                centroids.append(self.centroids[cluster])
            else:
                centroids.append(np.mean(cluster_points,axis=0))

        return np.array(centroids)

    def _euclidean_distance(self,x,y):
        return np.sqrt(np.sum((x-y)**2))

def main():

    np.random.seed(42)

    cluster1 = np.random.randn(100, 2) + np.array([0, 0])
    cluster2 = np.random.randn(100, 2) + np.array([5, 5])
    cluster3 = np.random.randn(100, 2) + np.array([0, 5])

    X = np.vstack((cluster1, cluster2, cluster3))

    model = Kmeans(
        n_clusters=3,
        max_iters=100
    )

    model.fit(X)

    labels = model.predict(X)

    print("Centroids:")
    print(model.centroids)

    print("\nFirst 20 Cluster Assignments")
    print(labels[:20])


if __name__ == "__main__":
    main()