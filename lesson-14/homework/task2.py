import numpy as np

def custom_power(x, p):
    return x ** p

vectorized_power = np.vectorize(custom_power)
bases = np.array([2, 3, 4, 5])
powers = np.array([1, 2, 3, 4])

results = vectorized_power(bases, powers)
print("Bases: ", bases)
print("Powers:", powers)
print("Results:", results)
