import numpy as np


def f(t, y):
    return np.array([y[1], -y[0]])


y = np.array([1, 2])
z = f(0, y)

print(z)

print(f(0, [3, 4]))

try:
    print(f(0, 5))
except Exception as e:
    print(e)

try:
    print(f(0, np.array([[1, 2], [3, 4]])))
except Exception as e:
    print(e)

z[0] = 100

print(y)
print(z)

# y не изменился, потому что функция создает новый массив
# выходная переменная хранится отдельно от входной

# [ 2 -1]
# [ 4 -3]
# 'int' object is not subscriptable
# [[ 3  4]
#  [-1 -2]]
# [1 2]
# [100  -1]