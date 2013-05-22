import numpy as np
import numpy.linalg as la

def pca(X, k):
	M = np.mean(X, axis = 0)
	X -= M
	S = np.cov(np.transpose(X))
	
	d, U = la.eig(S)
	si = np.argsort(d)[-1::-1]
	d = d[si]
	U = U[:, si]

	Y = np.dot(np.transpose(U), X)
	return np.dot(U[:,:k], Y[:k]) + M

