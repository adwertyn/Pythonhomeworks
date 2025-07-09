import numpy as np
random_matrix = np.random.randint(1, 100, (3,3))
column_vector = np.array([[1],[2],[3]])
print(random_matrix @ column_vector)