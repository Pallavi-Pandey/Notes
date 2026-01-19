import numpy as np
rng = np.random.default_rng(seed=42)
X = rng.integers(0, 5, 1000)

# Reshape to (20,50) row-major (default)
M = X.reshape((20, 50))

# Extract 30th column and 20th row using 1-based indexing
x = M[:, 29]   # 30th column -> index 29
y = M[19, :]   # 20th row -> index 19

# Compute L2 norm of x
l2_norm_x = np.linalg.norm(x, ord=2)

# Compute outer product x y^T (x as column vector, y as row vector)
outer = np.outer(x, y)

# Count zeros in outer
num_zeros = np.count_nonzero(outer == 0)

M, x, y, round(l2_norm_x, 2), num_zeros

print("ques 4 : ", round(l2_norm_x, 2))
print("ques 5 : ", num_zeros)
