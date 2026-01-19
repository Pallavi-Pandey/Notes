import numpy as np

# Recreate the matrix A using the given seed
rng = np.random.default_rng(seed=42)
A = rng.integers(0, 5, (10, 3))

# Sum the row vectors (summing along axis 0 gives sum of columns)
a, b, c = A.sum(axis=0)

A, (a, b, c)

print(A)
print("ques 1 : value of a =", a)
print("ques 2 : value of b =", b)
print("ques 3 : value of c =", c)
