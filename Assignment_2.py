import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)

y = x**3 + x - 100

plt.plot(x, y, label='$y = x^3 + x - 100$')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = x^3 + x - 100$')

plt.grid(True)

plt.legend()

plt.show()