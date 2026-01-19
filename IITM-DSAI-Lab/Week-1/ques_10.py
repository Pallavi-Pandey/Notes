import numpy as np
rng = np.random.default_rng(seed=42)

A = rng.integers(0, 100, (100, 200))
B = rng.integers(0, 100, (100, 300))

C = np.concatenate((A, B), axis=1)
mean_10th_row = np.mean(C[9])
print(round(mean_10th_row, 2))
