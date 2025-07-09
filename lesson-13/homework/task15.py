import numpy as np
matrix = np.arange(25).reshape(5,5)

row_sums = np.sum(matrix, axis=1)
column_sums = np.sum(matrix, axis=0)

print("Row-wise sums:", row_sums)
print("Column-wise sums:", column_sums)