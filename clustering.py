# import modul yang dibutuhkan
import pandas as pd
import numpy as np
import pickle
from sklearn.cluster import KMeans

# Membaca dataset
data = pd.read_csv('https://raw.githubusercontent.com/sowmyacr/kmeans_cluster/master/CLV.csv')
X = np.array(data)

# Jumlah cluster
numberOfCluster = 3

# Membuat model KMeans
kmeans = KMeans(
    n_clusters=numberOfCluster,
    init='k-means++',
    max_iter=300,
    n_init=10,
    random_state=1989028,
    precompute_distances='True'
)

kfit = kmeans.fit(X)

freezeCentroids = kmeans.clusterCenters
print(freezeCentroids)
print(freezeCentroids.shape)

# Menyimpan model ke dalam file pickle secara local
with open('freezedCentroids.pkl', 'wb') as f:
    pickle.dump(freezeCentroids, f)
    print('Centroids tersimoabn ke dalam file pickle')
