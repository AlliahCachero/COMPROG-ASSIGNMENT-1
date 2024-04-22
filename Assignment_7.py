import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)

y = x**3 + 2*x**2 - 10*x + 3

plt.plot(x, y, label='$y = x^3 + 2x^2 - 10x + 3$')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = x^3 + 2x^2 - 10x + 3$')

plt.grid(True)

plt.legend()

plt.show()