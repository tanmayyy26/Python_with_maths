import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 8, 7]

correlation_matrix = np.corrcoef(x, y)
correlation_xy = correlation_matrix[0, 1]

print("correlation coefficient", correlation_xy)
