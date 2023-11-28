import matplotlib.pyplot as plt, numpy as np

x = np.linspace(0, 0.6, 30)
y = np.array([i + np.random.uniform(-0.05, 0.05) for i in x])
plt.title("Best fit line using regression method")
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.scatter(x, y)
plt.plot(x, x, c = "red")
plt.show()
