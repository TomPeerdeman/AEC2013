from pylab import *
a = imread('data/trui.png')
figure(1)
subplot(1,2,1)
imshow(a)
d = a[100:126,100:126]
subplot(1,2,2)
imshow(d)
savefig('figures/trui_with_detail.pdf',bbox_inches='tight')
print(d.shape)