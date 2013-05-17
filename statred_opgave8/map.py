from pylab import tile, sum, argmin, argmax, amax, mean, cov, zeros, where, empty
from scipy.stats import norm
import operator
import numpy as np

def multivariate_pdf(vector, mean, cov):
	quadratic_form = np.dot(np.dot(vector-mean,np.linalg.inv(cov)),np.transpose(vector-mean))
	return np.exp(-.5 * quadratic_form)/ (2*np.pi * np.linalg.det(cov))

class MAP:
	def __init__(self, X, c):
		self.n, self.N = X.shape
		self.X = X
		self.c = c
		
		self.mu = empty((3, 4))
		self.cov = empty((3, 4, 4))
		cond = zeros(self.N)
		for i in range(0, 3):
			cond = cond + 1.0
			indices = where(self.c==cond)
			# Xa bevat alle elementen uit X waar de klasse gelijk van is aan i + 1.0
			Xa = [X[:,b] for b in indices]
			# Bovenstaande pakt de xjes in een extra array, dit willen we niet
			Xa = Xa[0]

			self.mu[i] = mean(Xa, axis=1)
			# Tile smeert mu uit zodat we mu kunnen aftrekken van de X matrix
			self.cov[i] = cov(Xa - tile(self.mu[i].T, len(Xa[0])).reshape(4, len(Xa[0])))

		print self.mu
		print self.cov
	
	def classify(self, x):
		y1 = multivariate_pdf(x, self.mu[0], self.cov[0])*(1./3.)
		y2 = multivariate_pdf(x, self.mu[1], self.cov[1])*(1./3.)
		y3 = multivariate_pdf(x, self.mu[2], self.cov[2])*(1./3.)
		px = y1 + y2 + y3
		P1x = y1 / px
		P2x = y2 / px
		P3x = y3 / px
		return argmax([P1x, P2x, P3x])
