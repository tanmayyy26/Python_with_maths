import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([2, 3, 4, 5, 6])
y = np.array([144, 172.8, 207.4, 248.8, 298.5])

# Linearizing the equation y = a * b^x
log_y = np.log(y)  # Take the natural logarithm of y
# Fit linear model 
coeffs = np.polyfit(x, log_y, 1)
log_b = coeffs[0]
log_a = coeffs[1]

# Convert back from log scale
a = np.exp(log_a)
b = np.exp(log_b)

# Print coefficients
print(f"Fitted curve: y = ({a:.2f}) * ({b:.2f})^x")

# Plotting the data points
plt.scatter(x, y, label="Data", color="blue")

# Plot fitted curve
x_values = np.linspace(min(x), max(x), 100)
y_fitted = a * (b ** x_values)
plt.plot(x_values, y_fitted, color="orange", label=f"Fitted curve: y = {a:.2f} * {b:.2f}^x")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Fitting y = a * b^x")
plt.legend()
plt.show()