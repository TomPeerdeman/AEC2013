from pylab import tile, sum, argmin, array, argmax, amax, mean, cov, zeros, where
import operator

class MAP:
	def __init__(self, X, c):
		self.n, self.N = X.shape
		self.X = X
		self.c = c
		
		#mu = array(3, 4)
		#cov = array(3, self.)
		cond = zeros(self.N)
		for i in range(0, 3):
			cond = cond + 1.0
			indices = where(self.c==cond)
			print "Indices: " + str(cond[0])
			print indices
			Xa = [X[:,b] for b in indices]
			print "X' :"
			print Xa

		#self.mu = mean(X, axis=0)
		#self.cov = cov(X - self.mu)

	def classify(self, x):
		return 0
