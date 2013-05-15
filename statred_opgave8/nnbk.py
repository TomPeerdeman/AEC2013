from pylab import tile, sum, argmin, array, zeros, argmax
from collections import Counter
class NNbk:
	def __init__(self, X, c):
		self.n, self.N = X.shape
		self.X = X
		self.c = c
		cs = Counter(c).items();
		self.nc = len(cs)
		self.cnames = zip(*cs)[0]
	
	def classify(self, x, k):
		d = self.X - tile(x.reshape(self.n,1), self.N)
		
		occ = zeros(self.nc);
		for i in range(k):
			dsq = sum(d*d,0)
			print dsq
			minindex = argmin(dsq)
			occ[self.c[minindex]] += 1
			# Prevent next iter giving this index again
			d[minindex][:] = float('inf')

		return self.cnames[argmax(occ)];
