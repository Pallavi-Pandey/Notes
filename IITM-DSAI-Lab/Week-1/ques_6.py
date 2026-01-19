import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define the function
f = lambda x: x * np.sin(x) - np.exp(-x) / (x**2)

# Find the root near π using a more precise method
root = fsolve(f, 3.14, full_output=True)

if root[2] == 1:  # Check if solution converged
    x_root = root[0][0]
    print(f"The root is approximately: {x_root:.5f}")
    print(f"Function value at root: {f(x_root):.2e}")
    
    # Verification plot
    x = np.linspace(3.0, 3.3, 200)
    y1 = x * np.sin(x)
    y2 = np.exp(-x) / (x**2)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='x*sin(x)')
    plt.plot(x, y2, label='e^(-x) / x^2')
    plt.axvline(x=x_root, color='r', linestyle='--', label=f'Root at x = {x_root:.5f}')
    plt.scatter(x_root, f(x_root) + np.exp(-x_root)/(x_root**2), color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Intersection of x*sin(x) and e^(-x)/x^2')
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("Failed to find root. Try a different initial guess.")

print("ques 6 : ", x_root)
