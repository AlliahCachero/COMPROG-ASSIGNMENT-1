import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
x = x[x != 0]

y = (x**2 + x + 10) / (2*x)

plt.plot(x, y, label='$y = \\frac{x^2 + x + 10}{2x}$')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = \\frac{x^2 + x + 10}{2x}$')

plt.grid(True)

plt.legend()

plt.show()