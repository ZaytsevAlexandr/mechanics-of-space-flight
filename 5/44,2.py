import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos

e = 0.1

x = np.linspace(0, 2, 1000)

y1 = x - e * np.sin(x)
y2 = np.ones(len(x))

plt.plot(x, y1)
plt.plot(x, y2)

plt.grid()
plt.savefig('44,2result')

x0 = 1

for i in range(100):
    x1 = x0 - (x0 - e * sin(x0) - 1) / (1 - e * cos(x0))
    x0 = x1

print(x1)
# 1.0885977523978936
