import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 4*x + 4
x = np.linspace(-10, 10, 400)
y = f(x)
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='blue', linewidth=2, label=r'$f(x) = x^2 - 4x + 4$')

plt.title('Plot of $f(x) = x^2 - 4x + 4$')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis
plt.legend(loc='upper left')

plt.show()
