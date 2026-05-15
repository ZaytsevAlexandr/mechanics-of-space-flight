import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-1, 0, 100)
y1 = -x1

x2 = np.linspace(0, 1, 100)
y2 = np.exp(x2) - 1

plt.plot(x1, y1)
plt.plot(x2, y2)

plt.grid()
plt.savefig('15result')
