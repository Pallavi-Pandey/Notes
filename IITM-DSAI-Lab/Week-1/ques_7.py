# question 7
import numpy as np
rng = np.random.default_rng(seed=42)

# Define faces and corresponding probabilities
faces = [1, 2, 3]
probabilities = [0.2, 0.3, 0.5]

# Roll the die 1000 times
X = rng.choice(faces, size=1000, p=probabilities)

# Count the number of times 3 appears
count_3 = np.count_nonzero(X == 3)

print("Number of occurrences of 3:", count_3)
