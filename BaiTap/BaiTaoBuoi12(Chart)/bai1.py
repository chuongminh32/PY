import numpy as np
import matplotlib.pyplot as plt

# Define the function
def polynomial(x):
    return 3 * x**5 + 20 * x**4 - 10 * x**3 - 240 * x**2 - 250 * x + 200

# Generate x values
x = np.linspace(-6, 4, 400)
y = polynomial(x)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'r--', linewidth=3, label=r"$y = 3x^5 + 20x^4 - 10x^3 - 240x^2 - 250x + 200$")

# Adding title and labels
plt.title("Fifth Degree Polynomial", fontsize=14, weight='bold')
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)

# Set the axis range
plt.xlim(-6, 4)
plt.ylim(-1200, 400)

# Show grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
