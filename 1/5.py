import numpy as np

v = np.array([5, 9, -1, 2, 8, 2, 0, 4])
w = v.copy()
w[2:5] = 0
s = w.sum()
w += 3
e = np.concatenate((v, w))

print(v)
print(w)
print(s)
print(e)
print(e.max())
print(e.min())
print(np.sort(e))

# [ 5  9 -1  2  8  2  0  4]
# [ 8 12  3  3  3  5  3  7]
# 20
# [ 5  9 -1  2  8  2  0  4  8 12  3  3  3  5  3  7]
# 12
# -1
# [-1  0  2  2  3  3  3  3  4  5  5  7  8  8  9 12]