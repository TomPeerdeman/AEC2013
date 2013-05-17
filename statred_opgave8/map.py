from pylab import tile, sum, argmin, argmax, amax, mean, cov, zeros, where, empty, shape
from scipy.stats import norm
import operator
import numpy as np

# Original source:
# http://stackoverflow.com/questions/15120662/compute-probability-over-a-multivariate-normal
def multivariate_pdf(vector, mean, cov):
	quadratic_form = np.dot(np.dot(vector-mean,np.linalg.inv(cov)),np.transpose(vector-mean))
	return np.exp(-.5 * quadratic_form)/ (2*np.pi * np.linalg.det(cov))

class MAP:
	def __init__(self, X, c):
		self.n, self.N = X.shape
		self.X = X
		self.c = c
		
		self.mu = empty((3, self.n))
		self.cov = empty((3, self.n, self.n))
		self.P = empty(3)
		cond = zeros(self.N)
		for i in range(0, 3):
			cond = cond + 1.0
			indices = where(self.c==cond)
			# Xa bevat alle elementen uit X waar de klasse gelijk van is aan i + 1.0
			Xa = [X[:,b] for b in indices]
			# Bovenstaande pakt de xjes in een extra array, dit willen we niet
			Xa = Xa[0]
			Na = shape(Xa)[1]

			self.mu[i] = mean(Xa, axis=1)
			# Tile smeert mu uit zodat we mu kunnen aftrekken van de X matrix
			self.cov[i] = cov(Xa - tile(self.mu[i].T, Na).reshape(self.n, Na))

			# De kans op deze klasse
			self.P[i] = (Na * 1.0) / self.N

		print self.mu
		print self.cov
	
	def classify(self, x):
		y1 = multivariate_pdf(x, self.mu[0], self.cov[0])*self.P[0]
		y2 = multivariate_pdf(x, self.mu[1], self.cov[1])*self.P[1]
		y3 = multivariate_pdf(x, self.mu[2], self.cov[2])*self.P[2]
		px = y1 + y2 + y3
		P1x = y1 / px
		P2x = y2 / px
		P3x = y3 / px
		return argmax([P1x, P2x, P3x]) + 1.0
