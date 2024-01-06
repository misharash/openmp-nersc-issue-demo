import os
import numpy as np

N = 10**10

x = np.linspace(0, np.pi, N)
y = np.sin(x)

os.system(f"./demo 256 {N}")