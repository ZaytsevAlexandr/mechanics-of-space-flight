import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def EqHarmonicOscillator(t, y):
    return [y[1], -y[0]]


t0 = 0
tf = 20
y0 = [0, 1]

t = np.linspace(t0, tf, 1000)

sol = solve_ivp(EqHarmonicOscillator, [t0, tf], y0, method='RK45', t_eval=t)

y1_exact = np.sin(t)
y2_exact = np.cos(t)

plt.figure(figsize=(10, 5))

plt.plot(t, y1_exact, label='y1 exact')
plt.plot(t, sol.y[0], '--', label='y1 RK45')

plt.plot(t, y2_exact, label='y2 exact')
plt.plot(t, sol.y[1], '--', label='y2 RK45')

plt.legend()
plt.grid()
plt.savefig('56result')

