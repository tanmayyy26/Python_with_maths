import matplotlib.pyplot as plt
import numpy as np

# Define the function and create the graph
x = np.linspace(-10, 10, 100)  
y = np.log(x)  

plt.plot(x, y, label='y = log(x)', color="red")

# Add labels, title, and grid
plt.title('Graph of the Function y = log(x)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend()

plt.show()