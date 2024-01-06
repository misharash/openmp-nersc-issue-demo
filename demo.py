import os
import numpy as np

x = np.linspace(0, np.pi, 10**6)
y = np.sin(x)

os.system(f"./demo 256 {10**10}")