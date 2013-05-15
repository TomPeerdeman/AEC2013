from pylab import tile, sum, argmin, array, argmax, amax
from collections import Counter
import operator

class NNbk:
	def __init__(self, X, c):
		self.n, self.N = X.shape
		self.X = X
		self.c = c

		cs = Counter(c).items();
		# Extract the names of the classes
		self.cnames = zip(*cs)[0]
		# Calculate max value of the 2d array
		self.max = amax(X)
	
	def classify(self, x, k):
		d = self.X - tile(x.reshape(self.n,1), self.N)
		
		# Occurrence of a class
		occd = {x: 0 for x in self.cnames}
		for i in range(k):
			dsq = sum(d*d,0)
			minindex = argmin(dsq)
			occd[self.c[minindex]] += 1
			# Prevent next iter giving this index again
			d[:, minindex] = self.max + 1

		# Return the name of the class that occurred most
		return max(occd.iteritems(), key=operator.itemgetter(1))[0]
