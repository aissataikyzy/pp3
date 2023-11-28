import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 17, 100)
x = np.sin(theta)
y = np.cos(theta)
ax.plot(x, y, z)

z_dots = 15*np.random.random(100)
x_dots = np.sin(z_dots)
y_dots = np.cos(z_dots)
ax.scatter3D(x_dots, y_dots, z_dots, c=z, cmap="Reds")

plt.show()
