from pylab import tile, sum, argmin, argmax, amax, mean, cov, zeros, where, empty, shape
import operator

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

	def classify(self, x):
		return 0
