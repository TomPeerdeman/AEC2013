from pylab import *
import numpy as np

# Sample dimensions
sh = 25
sw = 25

# Plot an eigenvector image
def plotEigenVec(n, data):
	subplot(2,3,n)
	imshow(np.reshape(data, (sh, sw)))

# Original code found from 'Handout_5_PCA.pdf' page 4
def eigensort(M):
	d, U = np.linalg.eig(M)
	si = np.argsort(d)[-1::-1]
	d = d[si]
	U = U[:, si]
	return (d, U)

# Create a reconstruction from a detail of the image
def plotReconstruction(k, imgDetail, M, U):
	x = np.reshape(imgDetail, samplesize)
	y = np.dot(np.transpose(U), x - M)
	xapprox = np.dot(U[:,:k], y[:k]) + M

	plt.subplot(1,2,1, title='Original')
	imshow(imgDetail)
	plt.subplot(1,2,2, title='Reconstruction')
	imshow(np.reshape(xapprox, (sh, sw)))

# Search for the k main eigenvalues
def getk(d):
	total = np.sum(d)
	ktotal = 0.0
	k = 0
	while (ktotal / total) < 0.99:
		ktotal += d[k]
		k += 1
	return k

print "Loading image..."
a = imread('data/trui.png')

# Save all images in grayscale
gray()

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

# Search the number of eigenvalues that matter the most
print "Searching for k main eigenvectors..."
k = getk(d)
print "\tFound k=" + str(k)

# reconstruct a piece of the image only using the most important eigenvectors
print "Reconstructing the image detail from (50,175) to (75,200)..."
figure(3).suptitle('Reconstruction')
plotReconstruction(k, a[50:75, 175:200], M, U)
savefig('figures/k_reconstruction.pdf')

print "Done"

