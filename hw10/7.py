import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = plt.axes(projection='3d')
x = np.random.randint(-1000, 1000, size = 500)
y = np.random.randint(-1000, 1000, size = 500)
z = np.random.randint(-1000, 1000, size = 500)
ax.scatter(x, y, z, c = "green")
ax.scatter(range(-100, 400), y, z, c = "blue")
ax.scatter(x, y, z, c = "red")
plt.show()
