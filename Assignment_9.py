import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)
x = x[x != 0]

y = (x**3 / (2*x)) - 10*x

plt.plot(x, y, label='$y = \\frac{x^3}{2x} - 10x$')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = \\frac{x^3}{2x} - 10x$')

plt.grid(True)

plt.legend()

plt.show()