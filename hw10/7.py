import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x_g = np.random.randint(-1500, 1500,size=(500))
y_g = np.random.randint(-1000, -500, size=(500))
z_g = np.random.randint(-1500, 1000, size=(500))

s = ax.scatter(x_g, y_g, z_g, c=z_g, cmap='viridis', linewidth=0.5)
fig.colorbar(s)
plt.show()

