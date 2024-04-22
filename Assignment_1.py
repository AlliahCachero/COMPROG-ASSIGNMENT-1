import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)

y = x**2 - 10

plt.plot(x, y, label='$y = x^2 - 10$')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = x^2 - 10$')

plt.grid(True)

plt.legend()

plt.show()