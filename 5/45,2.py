from math import exp


def f(x):
    return exp(x) + x - 5


def d(a, b):
    while min(abs(f(a)), abs(f(b))) > 1e-10:
        c = (a + b) / 2

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    if abs(f(a)) < abs(f(b)):
        return a
    else:
        return b


x = d(1, 2)

print(x)
# 1.3065586410230026