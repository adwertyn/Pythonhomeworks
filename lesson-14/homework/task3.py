import numpy as np

# Koeffitsientlar matriksi
A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

# Natijalar vektori
B = np.array([7, 4, 5])

# Tenglamalar sistemasini yechish
solution = np.linalg.solve(A, B)

print("x, y, z =", solution)
