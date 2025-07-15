import numpy as np

# 1. Define the conversion function
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

# 2. Vectorize the function using numpy
vectorized = np.vectorize(fahrenheit_to_celsius)

# 3. Create the array of Fahrenheit temperatures
temps_fahrenheit = np.array([32, 68, 100, 212, 77])

# 4. Apply the vectorized function
temps_celsius = vectorized(temps_fahrenheit)

print("Fahrenheit:", temps_fahrenheit)
print("Celsius:", temps_celsius)
