import time
import numpy as np
from scipy.integrate import solve_ivp


def r2bp(t, y):
    r = y[:3]
    v = y[3:]
    rn = np.linalg.norm(r)
    a = -r / rn ** 3
    return np.concatenate((v, a))


def pos(t):
    sol = solve_ivp(r2bp, [0, t], y0, rtol=1e-10, atol=1e-12)
    return sol.y[:3, -1]


def dichotomy(a, b):
    start = time.time()
    while abs(b - a) > 1e-10:
        c = (a + b) / 2
        if pos(a)[0] * pos(c)[0] <= 0:
            b = c
        else:
            a = c
    t = (a + b) / 2
    r = pos(t)
    return t, r, time.time() - start


def interpolation(a, b, n=200):
    start = time.time()
    t = np.linspace(a, b, n)
    sol = solve_ivp(r2bp, [a, b], y0, t_eval=t, rtol=1e-10, atol=1e-12)
    x = sol.y[0]

    for i in range(len(t) - 1):
        if x[i] * x[i + 1] <= 0:
            j = max(0, min(i - 2, len(t) - 5))
            tt = t[j:j + 5]
            xx = x[j:j + 5]
            p = np.polyfit(tt, xx, 4)
            roots = np.roots(p)
            roots = roots[np.isreal(roots)].real
            roots = roots[(roots >= t[i]) & (roots <= t[i + 1])]
            tr = roots[0]
            r = pos(tr)
            return tr, r, time.time() - start


y0 = np.array([1, 0, 0, 0, 1.1, 0], dtype=float)

td, rd, timed = dichotomy(1, 3)
ti, ri, timei = interpolation(1, 3)

print("Метод дихотомии")
print(td)
print(rd)
print(timed)

print("Интерполяция 4 порядка")
print(ti)
print(ri)
print(timei)

print("Разница по времени выхода")
print(abs(td - ti))

# Метод дихотомии
# 1.6433462209824938
# [1.00289204e-11 1.21000000e+00 0.00000000e+00]
# 0.19904041290283203
# Интерполяция 4 порядка
# 2.643346220991232
# [-0.84167553  1.10211752  0.        ]
# 0.05205082893371582
# Разница по времени выхода
# 1.0000000000087383