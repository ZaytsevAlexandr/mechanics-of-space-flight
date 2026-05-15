from math import e


def f(t, y):
    return y


def RK4(t0, tf, y0, h):
    t = t0
    y = y0

    while t < tf:
        k1 = f(t, y)
        k2 = f(t + h / 2, y + h * k1 / 2)
        k3 = f(t + h / 2, y + h * k2 / 2)
        k4 = f(t + h, y + h * k3)

        y = y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t = t + h

    return y


a = 1
b = 3
h = 0.01

while abs(b - a) > 1e-10:
    T = (a + b) / 2

    yT = RK4(0, T, 1, h)

    if yT < e ** 2:
        a = T
    else:
        b = T

print(T)
# 2.0000000000582077