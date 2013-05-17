from pylab import tile, sum, argmin, argmax, amax, mean, cov, zeros, where, empty
import operator

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

	def classify(self, x):
		return 0
