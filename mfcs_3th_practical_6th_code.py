import matplotlib.pyplot as plt
import numpy as np

# Define the function and create the graph
x = np.linspace(-10, 10, 100)
y = x*x + 4*x + 9

plt.plot(x, y, label='y = x^2 + 4*x + 9', color='red')

# Add labels, title, and grid
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph of the Function y = x^2 + 4*x + 9')
plt.grid(True)
plt.legend()
plt.show()