import os
import numpy as np

x = np.linspace(0, np.pi, 10**7)
y = np.sin(x)
z = np.cos(x)
yz = y * z

filt = np.logical_and(y < 0.5, z > -0.5)
yy = y[filt]
zz = z[filt]

idx = np.where(filt)
yyy = y[idx]
zzz = z[idx]

np.savetxt("tmp.txt", np.column_stack((y, z))[:10**4])
tmp = np.loadtxt("tmp.txt")

print("Done with numpy")

os.system(f"./demo 256 {10**9}")