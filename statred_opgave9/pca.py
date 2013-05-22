import numpy as np
import numpy.linalg as la

# Original code found from 'Handout_5_PCA.pdf' page 4
def eigensort(M):
	d, U = la.eig(M)
	si = np.argsort(d)[-1::-1]
	d = d[si]
	U = U[:, si]
	return (d, U)

# Inpiration: http://stackoverflow.com/questions/13224362/pca-analysis-with-python
#           & exercise 7.5.3
def pca(X, k):
	M = np.mean(X, axis = 0)
	X -= M
	S = np.cov(np.transpose(X))
	
	d, U = eigensort(S)
	U = U[:,:k];

	return U, np.transpose(np.dot(np.transpose(U), np.transpose(X)))

