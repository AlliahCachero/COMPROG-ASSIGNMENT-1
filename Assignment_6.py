import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)
x = x[x != 0]

y = np.sin(x) / (3*x)

plt.plot(x, y, label='$y = \\frac{\\sin(x)}{3x}$')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = \\frac{\\sin(x)}{3x}$')

plt.grid(True)

plt.legend()

plt.show()