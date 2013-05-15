from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,15,100)
y1 = norm.pdf(x, 4, 1)
y2 = norm.pdf(x, 7, 2)

plt.figure(1)
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()

