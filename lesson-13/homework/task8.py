import numpy as np
matrix1 = np.random.randint(1,100,(5,3))
matrix2 = np.random.randint(1,100,(3,2))
multiplied = np.dot(matrix1, matrix2)
print(multiplied)
