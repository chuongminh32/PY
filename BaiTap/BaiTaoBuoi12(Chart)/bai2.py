import numpy as np
import matplotlib.pyplot as plt

# Define the functions
x1 = np.linspace(-3 * np.pi, 0, 400)
y1 = 1.5 * np.sin(x1)

theta = np.linspace(0, 3 * np.pi, 400)
r = 2 + np.cos(10 * theta) + 2 * np.sin(5 * theta)

x2 = np.linspace(0, 3 * np.pi, 400)
y2 = 1.5 * np.sin(x2)

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the first function
plt.plot(x1, y1, 'r--', label=r"$y = 1.5 \sin(x)$ with x in [-3$\pi$; 0]")

# Plot the second function (polar plot)
plt.polar(theta, r, 'g-', label=r"$r = 2 + \cos(10\theta) + 2 \sin(5\theta)$")

# Plot the third function
plt.plot(x2, y2, 'b:', label=r"$y = 1.5 \sin(x)$ with x in [0; 3$\pi$]")

# Add title and labels
plt.title("Function Plots with Different Styles", fontsize=14, weight='bold')
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)

# Set custom ticks for x and y axes
plt.xticks(np.linspace(-10, 10, 9))  # Custom ticks for Ox
plt.yticks(np.arange(-6, 7, 2))  # Custom ticks for Oy

# Display the grid and legend
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()

# Show the plot
plt.show()
