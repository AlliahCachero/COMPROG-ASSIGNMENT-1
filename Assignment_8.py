import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)
x = x[x != 0]

y = np.cos(x) / (5*x)

plt.plot(x, y, label='$y = \\frac{\\cos(x)}{5x}$')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = \\frac{\\cos(x)}{5x}$')

plt.grid(True)

plt.legend()

plt.show()