import matplotlib.pyplot as plt
import numpy as np

# Define the function and draw the graph
x = np.linspace(-10, 10, 100)
y = x * x

# Plot the graph
plt.plot(x, y, label='y = x^2', color='red')

# Add labels, title, and grid
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph of the Function y = x²')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
