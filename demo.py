import os

print(os.environ)

import numpy as np
from sklearn.cluster import KMeans

np.random.seed(42)
X = np.random.rand(10**5, 2)
kmeans = KMeans(n_clusters = 60, random_state = 42).fit(X)

print(os.environ)

os.environ["OMP_PLACES"] = ",".join("{" + str(i) + "},{" + str(i+128) + "}" for i in range(128))
os.system(f"./demo 256 {10**8}")