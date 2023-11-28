import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 50, 0.01)
y1 = np.sin(x * np.pi / 25)
y2 = np.sin(x * np.pi / 25 + np.pi / 2)
y3 = np.sin(x * np.pi / 25 - np.pi / 2)
y4 = np.sin(x * np.pi / 25 + np.pi)

plt.grid()

plt.plot(x, y1, color='blue')
plt.plot(x, y2, color='orange')
plt.plot(x, y3, color='red')
plt.plot(x, y4, color='green')

plt.legend()

plt.show()
