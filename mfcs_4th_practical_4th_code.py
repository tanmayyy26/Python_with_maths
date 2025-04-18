import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2.98, 4.26, 5.21, 6.10, 6.80, 7.5])

# Fitting the exponential curve y = a * x^b
log_x = np.log(x)
log_y = np.log(y)
b_exp, log_a_exp = np.polyfit(log_x, log_y, 1)
a_exp = np.exp(log_a_exp)  # Convert back from log scale

# Print coefficients
print(f"Fitted power-law: y = ({a_exp:.2f}) * x^({b_exp:.2f})")

# Plotting the data points
plt.scatter(x, y, label="Data", color="blue")

# Plot fitted exponential curve 
x_values = np.linspace(min(x), max(x), 100)
y_exponential = a_exp * (x_values ** b_exp)
plt.plot(x_values, y_exponential, color="purple", label=f"Fitted curve: y = {a_exp:.2f} * x^{b_exp:.2f}")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Fitting an exponential Curve: y = a * x^b")
plt.legend()
plt.grid(True)
plt.show()