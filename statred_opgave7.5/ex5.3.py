from pylab import *
import numpy as np

a = imread('data/trui.png')
figure(1)
subplot(1,2,1)
imshow(a)
d = a[100:126,100:126]
subplot(1,2,2)
imshow(d)
savefig('figures/trui_with_detail.pdf',bbox_inches='tight')
print(d.shape)

# Dit kan wel eens h,w zijn
w,h = a.shape
X = np.empty((53824, 625), dtype=float)

for x in xrange(0, w-24):
	for y in xrange(0, h-24):
		X[:][x*25+y-1] = a[x:(x + 25), y:(y + 25)].reshape(625)

# empty vector for m
m = np.zeros((625),dtype=float)
e = np.zeros((625,625),dtype=float)
# calc mean
for x in X:
	m += x
	e += (x*np.transpose(x))
M = (1.0/shape(X)[0])*m
S = (e - shape(X)[0]*M*np.transpose(M))/(shape(X)[0]-1)

summ = 0.0
for me in M:
	summ += m
print summ

def eigensort(M):
	d, U = np.linalg.eig(M)
	si = np.argsort(d)[-1::-1]
	d = d[si]
	U = U[:, si]
	return (d, U)

d, U = eigensort(S)

figure(2)
#bar(range(10), d[:10])
plot(range(10), d[:10])
savefig('figures/eigen.pdf')
