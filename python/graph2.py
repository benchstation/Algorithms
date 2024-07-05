import numpy as np
import matplotlib.pyplot as plt

# Define the piecewise function
def h(x):
    if x < -1 or x > 2:
        return x**2 - x - 2
    else:
        return -x**2 + x + 2

# Vectorize the function for plotting
h_vectorized = np.vectorize(h)

# Create an array of x values
x = np.linspace(-3, 4, 400)

# Calculate the corresponding y values
y = h_vectorized(x)

# Plot the function
plt.plot(x, y, label='h(x) = |x^2 - x - 2|', color='b')

# Add labels and title
plt.xlabel('x')
plt.ylabel('h(x)')
plt.title('Graph of h(x) = |x^2 - x - 2|')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

# Show the plot
plt.show()