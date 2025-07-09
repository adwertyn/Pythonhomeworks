import numpy as np

matrix = np.random.randint(1, 100, (5, 5))
print("Original Matrix:\n", matrix)
max_element = np.max(matrix)
min_element = np.min(matrix)

normalized_matrix = (matrix - min_element) / (max_element - min_element)

print("Normalized Matrix:\n", normalized_matrix)
