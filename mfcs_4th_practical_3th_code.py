#fitting of straight line, parabola and exponential curves to the data
#straight line
import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1.6, 4.5, 13.8, 40.2, 125, 300])

log_y = np.log(y)
b_exp, log_a_exp = np.polyfit(x, log_y, 1)
a_exp = np.exp(log_a_exp)

# Print the coefficients
print(f"Fitted exponential: y = ({a_exp:.2f}) * exp({b_exp:.2f} * x)")

# Plotting the data points
plt.scatter(x, y, label="Data", color="blue")

# Plot the fitted exponential curve
x_values = np.linspace(min(x), max(x), 100)
y_exponential = a_exp * np.exp(b_exp * x_values)
plt.plot(x_values, y_exponential, color="purple", label=f"Fitted exponential: y = {a_exp:.2f} * exp({b_exp:.2f} * x)")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Fitting an Exponential Curvey=a*e^bx")
plt.legend()
plt.show()