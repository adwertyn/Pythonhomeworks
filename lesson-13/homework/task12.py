import numpy as np
matrix1 = np.array(
    [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]
)
matrix2 = np.array(
    [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]]
)
answer = matrix1 @ matrix2
print(answer)