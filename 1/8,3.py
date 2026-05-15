import numpy as np

B = np.array([[2, 3], [1, 4]])
C = np.array([[4, 5], [0, 8]])
D = np.array([[5, 6], [4, 2]])
c = np.array([1, 2])
d = np.array([1, 3])

A = np.linalg.inv(B) @ C + (C @ np.linalg.inv(D)).T + B ** 2
b = c + B @ d

x = np.linalg.solve(A, b)

print(A)
print(b)
print(x)

# [[ 8.05714286 10.48571429]
#  [ 0.12857143 15.34285714]]
# [12 15]
# [0.21941816 0.97581493]