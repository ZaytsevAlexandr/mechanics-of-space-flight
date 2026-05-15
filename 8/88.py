import numpy as np
from scipy.integrate import solve_ivp


def r2bp(t, y):
    r = y[:3]
    v = y[3:]

    rn = np.linalg.norm(r)

    a = -r / rn ** 3

    return np.concatenate((v, a))


def residue(v0, t0, tf, r0, rf):
    y0 = np.concatenate((r0, v0))

    sol = solve_ivp(r2bp, [t0, tf], y0, method='RK45')

    r = sol.y[:3, -1]

    return r - rf


v0 = np.array([0, 1, 0])
r0 = np.array([1, 0, 0])
rf = np.array([1, 0, 0])

res = residue(v0, 0, 2 * np.pi, r0, rf)

print(res)
# [-0.07548976  0.20973479  0.        ]