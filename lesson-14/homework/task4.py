import numpy as np

# Koeffitsientlar matriksi
A = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

# Natijalar vektori
B = np.array([12, -5, 15])

# Tenglamani yechish
currents = np.linalg.solve(A, B)

print("I1, I2, I3 =", currents)
