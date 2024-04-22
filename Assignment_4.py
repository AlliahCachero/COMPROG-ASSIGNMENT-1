import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)

y = x**4 + x**3 + x**2 + x + 1

plt.plot(x, y, label='$y = x^4 + x^3 + x^2 + x + 1$')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = x^4 + x^3 + x^2 + x + 1$')

plt.grid(True)

plt.legend()

plt.show()