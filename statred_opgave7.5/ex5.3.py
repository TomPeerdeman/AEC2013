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
Xl = []
for x in range(0, w-24):
	for y in range(0, h-24):
		Xl.append(np.reshape(a[x:(x + 25), y:(y + 25)], 625));
X = np.array(Xl)
X = np.transpose(X)
print shape(X)	
