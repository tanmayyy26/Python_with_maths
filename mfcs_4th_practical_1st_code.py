#fitting of straight line, parabola and exponential curves to the data
#straight line
import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 4.1, 6.0, 7.9, 10.1])

# Fit the line y = ax + b
a, b = np.polyfit(x, y, 1)

# Print the coefficients
print(f"Fitted line: y = ({a:.2f})x + ({b:.2f})")

# Plotting
plt.scatter(x, y, label="Data", color='blue')
plt.plot(x, a * x + b, color="green", label=f"Fitted line: y = {a:.2f}x + {b:.2f}")
plt.legend()
plt.show()