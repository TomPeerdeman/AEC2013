from pylab import tile, sum, argmin, array, argmax, amax, mean, cov
import operator

class MAP:
	def __init__(self, X, c):
		self.n, self.N = X.shape
		self.X = X
		self.c = c
		
				

		self.mu = mean(X, axis=0)
		self.cov = cov(X - self.mu)

	def classify(self, x):
		return 0
