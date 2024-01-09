import os
import numpy as np
from sklearn.cluster import KMeans

np.random.seed(42)
X = np.random.rand(10**5, 2)
kmeans = KMeans(n_clusters = 60, random_state = 42).fit(X)

os.system(f"./demo 256 {10**8}")