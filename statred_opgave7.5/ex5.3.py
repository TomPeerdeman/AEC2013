from pylab import *
import numpy as np

# Sample dimensions
sh = 25
sw = 25

def plotEigenVec(n, data):
	subplot(2,3,n)
	imshow(np.reshape(data, (sh, sw)))

def eigensort(M):
	d, U = np.linalg.eig(M)
	si = np.argsort(d)[-1::-1]
	d = d[si]
	U = U[:, si]
	return (d, U)

print "Loading image..."
a = imread('data/trui.png')

h, w = a.shape
samplesize = sh * sw
N = (h - sh + 1) * (w - sw + 1)

print "Inserting samples..."
# Insert all the samples into the X matrix
X = np.zeros((N, samplesize), dtype=float)
for x in xrange(0, w - sw + 1):
	for y in xrange(0, h- sh + 1):
		X[:][x * sw + y - 1] = np.reshape(a[x:(x + sw), y:(y + sh)], samplesize)

print "Calculating mean and covariance..."
# Empty vector for m
m = np.zeros((samplesize),dtype=float)
e = np.zeros((samplesize,samplesize),dtype=float)
# Calc mean and cov matrix
for x in X:
	m += x
	e += (np.outer(x, x))
M = (1.0 / N) * m
S = (e - N * np.outer(M, M))/(N - 1)

print "Calculating eigenvectors and eigenvalues..."
# Calculate the eigenvectors & eigenvalues, sort them by eigenvalues desc
d, U = eigensort(S)

print "Plotting the data..."
# Plot the eigenvalues
figure(1).suptitle('Scree diagram')
bar(range(len(d)), d)
savefig('figures/eigenvalues.pdf')

# Plot the first 6 eigenvectors
figure(2).suptitle('First 6 eigenvectors')
for i in xrange(6):
	plotEigenVec(i, U[i])

savefig('figures/eigenvectors.pdf')

print "Done"

