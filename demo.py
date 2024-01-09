import os

env_orig = set(os.environ.items())

import numpy as np
from sklearn.cluster import KMeans

np.random.seed(42)
X = np.random.rand(10**5, 2)
kmeans = KMeans(n_clusters = 60, random_state = 42).fit(X)

env_new = set(os.environ.items())
print(f"{env_orig - env_new = }")
print(f"{env_new - env_orig = }")

os.environ["OMP_PLACES"] = ""
os.system(f"./demo 256 {10**8}")