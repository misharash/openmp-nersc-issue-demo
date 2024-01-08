import os
import numpy as np
from sklearn.cluster import KMeans

np.random.seed(42)
X, Y = np.random.rand(2, 10**5, 2)
kmeans = KMeans(n_clusters = 60, random_state = 42).fit(X)
Y_labels = kmeans.predict(Y)

os.system(f"OMP_PROC_BIND=spread OMP_PLACES=threads OMP_NUM_THREADS=256 ./demo 256 {10**8}")