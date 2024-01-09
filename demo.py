import os
import numpy as np
from sklearn.cluster import KMeans

np.random.seed(42)
X, Y = np.random.rand(2, 10**5, 2)
kmeans = KMeans(n_clusters = 60, random_state = 42).fit(X)
Y_labels = kmeans.predict(Y)

os.environ["OMP_PLACES"] = ",".join("{" + str(i) + "},{" + str(i+128) + "}" for i in range(128))
os.system(f"./demo 256 {10**8}")