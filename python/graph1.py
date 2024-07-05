import matplotlib.pyplot as plt

# Data points
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create a plot
plt.plot(x, y, label='y = x^2')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sample Plot')

# Add a legend
plt.legend()

# Show the plot
plt.show()