import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = plt.axes(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
x1 = [i + np.random.uniform(-0.5, 0.5) for i in x]
y1 = [i + np.random.uniform(-0.5, 0.5) for i in y]
z1 = [i + np.random.uniform(-0.5, 0.5) for i in z]
ax.plot(x, y, z, label='parametric curve')
ax.scatter(x1, y1, z1, c = "green")
ax.legend()
plt.show()
