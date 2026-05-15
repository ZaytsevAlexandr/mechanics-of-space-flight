import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def r2bp(t, y, mu):
    r = y[:3]
    v = y[3:]

    rn = np.linalg.norm(r)

    a = -mu * r / rn ** 3

    return np.concatenate((v, a))


mu = 1

y0 = [1, 0, 0, 0, 1, 0]

t = np.linspace(0, 2 * np.pi, 1000)

sol = solve_ivp(lambda t, y: r2bp(t, y, mu), [0, 2 * np.pi], y0, method='RK45', t_eval=t, rtol=1e-10, atol=1e-12)

x_exact = np.cos(t)
y_exact = np.sin(t)

plt.plot(sol.y[0], sol.y[1], label='RK45')
plt.plot(x_exact, y_exact, '--', label='exact')

plt.axis('equal')
plt.legend()
plt.grid()
plt.savefig('61result')

