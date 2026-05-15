import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4 * np.pi, 1000)
a = [0.01, 0.1, 1.0, 10.0]

plt.figure(figsize=(8, 6))

for i in a:
    y = np.exp(-i * x) * np.sin(i * x)
    plt.plot(x, y, linewidth=2, label=f'a={i}')

plt.xlabel('x', fontsize=12)
plt.ylabel('f(x,a)', fontsize=12)
plt.legend(fontsize=12)
plt.grid()

plt.savefig('21result.png', dpi=300)
