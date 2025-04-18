#fitting of straight line, parabola and exponential curves to the data
#straight line
import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([2, 6, 7, 8, 10, 11, 11, 10, 9])

# Fit the parabola y = ax^2 + bx + c
a, b, c = np.polyfit(x, y, 2)

# Print the coefficients
print(f"Fitted parabola: y = ({a:.2f})x^2 + ({b:.2f})x + ({c:.2f})")

# Plotting
plt.scatter(x, y, label="Data", color='blue')
plt.plot(x, a * x**2 + b * x + c, color="green", label=f"Fitted parabola: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}")

plt.legend()
plt.show()