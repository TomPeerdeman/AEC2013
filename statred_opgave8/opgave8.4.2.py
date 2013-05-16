from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,15,200)
y1 = norm.pdf(x, 4, 2.5)
y2 = norm.pdf(x, 7, 2)

plt.figure(1)
plt.plot(x, y1, color="blue")
plt.plot(x, y2, color="red")

px = norm.pdf(x, 4, 1) * 0.3 + norm.pdf(x, 7, 1.5) * 0.7
P1x = norm.pdf(x, 4, 1) * 0.3 / px
P2x = norm.pdf(x, 7, 1.5) * 0.7 / px

plt.plot(x, P1x, linestyle="dashed", color="blue")
plt.plot(x, P2x, linestyle="dashed", color="red")
plt.show()

