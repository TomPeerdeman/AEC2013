import numpy as np
from nnbk import NNbk

X = np.arange(0, 100)
X = X.reshape(10, 10)
c = np.random.random_integers(0, 1, 10)

nnbk = NNbk(X, c)
print nnbk.classify(np.random.random_integers(0, 10, 10), 3)

