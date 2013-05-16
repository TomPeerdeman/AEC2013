from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,15,200)
y1 = norm.pdf(x, 4, 1)*0.3
y2 = norm.pdf(x, 7, 1.5)*0.7

plt.figure(1)

p1, = plt.plot(x, y1, color="blue")
p2, = plt.plot(x, y2, color="red")

px = y1 + y2
P1x = y1 / px
P2x = y2 / px

p3, = plt.plot(x, P1x, linestyle="dashed", color="blue")
p4, = plt.plot(x, P2x, linestyle="dashed", color="red")

plt.legend([p3, p4, p1, p2], ["P(C=1|x)", "P(C=2|x)", "pxc(x,C=1)", "pxc(x,C=2)"])

plt.show()

