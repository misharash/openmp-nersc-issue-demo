import ctypes
from datetime import datetime
import numpy as np
from sklearn.cluster import KMeans

np.random.seed(42)
X = np.random.rand(10**5, 2)
kmeans = KMeans(n_clusters = 60, random_state = 42).fit(X)

args = ("./demo.so", "10", str(10**8))
demo_lib = ctypes.cdll.LoadLibrary(args[0])
c_args = [ctypes.cast(ctypes.create_string_buffer(s.encode()), ctypes.c_char_p) for s in args]
c_args.append(ctypes.c_char_p(None))
argv = (ctypes.c_char_p * len(c_args))(*c_args)
print(datetime.now())
demo_lib.main(ctypes.c_int(len(args)), argv)
print(datetime.now())