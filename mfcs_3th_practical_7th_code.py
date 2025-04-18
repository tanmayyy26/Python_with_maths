import matplotlib.pyplot as plt
import numpy as np

# Define the function and create the graph
x = np.linspace(-10, 10, 100)
y = np.exp(x)

plt.plot(x, y, label='y = exp(x)', color='red')

# Add labels, title, and grid
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph of the Function y = exp(x)')
plt.grid(True)
plt.legend()

plt.show()