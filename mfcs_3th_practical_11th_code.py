import matplotlib.pyplot as plt
import numpy as np

# Define the function and create the graph
x = np.linspace(0, 5, 100)         # Changed upper limit to 5 for better visualization
y = np.exp(x)                      # e^x

plt.plot(x, y, label='y = e^x', color='blue')

# Add labels, title, and grid
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph of the Function y = e^x")
plt.grid(True)
plt.legend()
plt.show()
