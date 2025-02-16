import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)

y = x**10 - x**8 + x**2 - 8

plt.plot(x, y, label='$y = x^{10} - x^8 + x^2 - 8$')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = x^{10} - x^8 + x^2 - 8$')

plt.grid(True)

plt.legend()

plt.show()