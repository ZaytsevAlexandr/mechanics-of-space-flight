import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def rhs(t, u):
    y = u[:6]
    p = u[6:].reshape(6, 6)
    r = y[:3]
    v = y[3:]
    rn = np.linalg.norm(r)
    a = -r / rn ** 3
    da = -np.eye(3) / rn ** 3 + 3 * np.outer(r, r) / rn ** 5
    A = np.zeros((6, 6))
    A[:3, 3:] = np.eye(3)
    A[3:, :3] = da
    dp = A @ p
    return np.concatenate((v, a, dp.reshape(-1)))


calls = 0


def segment(t0, t1, y0):
    global calls
    calls += 1
    u0 = np.concatenate((y0, np.eye(6).reshape(-1)))
    sol = solve_ivp(rhs, [t0, t1], u0, method='RK45', rtol=1e-10, atol=1e-12)
    u = sol.y[:, -1]
    return u[:6], u[6:].reshape(6, 6)


def residue(x, t, r0, rf):
    v0 = x[:3]
    y1 = x[3:9]
    y2 = x[9:15]
    y0 = np.concatenate((r0, v0))

    f0, p0 = segment(t[0], t[1], y0)
    f1, p1 = segment(t[1], t[2], y1)
    f2, p2 = segment(t[2], t[3], y2)

    res = np.concatenate((f0 - y1, f1 - y2, f2[:3] - rf))

    J = np.zeros((15, 15))
    J[:6, :3] = p0[:, 3:]
    J[:6, 3:9] = -np.eye(6)
    J[6:12, 3:9] = p1
    J[6:12, 9:15] = -np.eye(6)
    J[12:15, 9:15] = p2[:3, :]

    return res, J


r0 = np.array([1, 0, 0], dtype=float)
rf = np.array([0, 1.2, 0], dtype=float)
t = np.linspace(0, np.pi / 2, 4)

x = np.zeros(15)
x[:3] = [0, 1, 0]
x[3:9] = [0.5, 0.5, 0, -0.5, 1, 0]
x[9:15] = [0.2, 1, 0, -1, 0.5, 0]

start = time.time()

for i in range(20):
    res, J = residue(x, t, r0, rf)
    print(i, calls, np.linalg.norm(res))

    if np.linalg.norm(res) < 1e-10:
        break

    dx = np.linalg.solve(J, -res)
    x = x + dx

finish = time.time()

v0 = x[:3]
print(v0)
print(calls)
print(finish - start)

y0 = np.concatenate((r0, v0))
tt = np.linspace(t[0], t[-1], 500)
sol = solve_ivp(lambda t, u: rhs(t, np.concatenate((u, np.eye(6).reshape(-1))))[:6], [t[0], t[-1]], y0, t_eval=tt,
                rtol=1e-10, atol=1e-12)

plt.plot(sol.y[0], sol.y[1])
plt.scatter([r0[0], rf[0]], [r0[1], rf[1]])
plt.axis('equal')
plt.grid()
plt.savefig('91result')

# 0 3 0.6209055759668414
# 1 6 0.22679876022528103
# 2 9 0.0069908406190307875
# 3 12 5.538124524342334e-06
# 4 15 3.541941250668532e-12
# [-0.04082325  1.12021287  0.        ]
# 15
# 0.06999659538269043