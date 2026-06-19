from sklearn.cluster import KMeans


def find_optimal_clusters(X):
    wss = []
    for k in range(1, 11):
        km = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=42)
        km.fit(X)
        wss.append(km.inertia_)
    return wss


def train_kmeans(X, k=5):
    model = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=42)
    labels = model.fit_predict(X)
    return model, labels
