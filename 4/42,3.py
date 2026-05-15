from math import sqrt

a = sqrt(2)
k = 0

while abs(a - 2) >= 1e-10:
    a = (sqrt(2)) ** a
    k += 1

print(a)
print(k)

# 1.9999999999145015
# 61