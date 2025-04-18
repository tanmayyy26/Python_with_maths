import matplotlib.pyplot as plt
import numpy as np

# Define the function and create a graph
x = np.linspace(0, 10, 100)
y = x

plt.plot(x, y, label='y = x', color='red')

# Add labels, title, and grid
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph of the Function y = x")
plt.grid(True)
plt.legend()
plt.show()
