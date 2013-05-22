from pylab import *
from svmutil import *
import pca

# read the natural spectra and make it into a set for classification

# the colors found in the dataset
Colors = ['black', 'blue', 'brown', 'gray', 'green', 'orange', 'pink', 'red', 'violet', 'white', 'yellow']

# does a line of text contain a color name?
def containsColor( line ):
	for c in Colors:
		if line.find(c)>=0:
			return Colors.index(c), c
	return None, None

# read the file and store spectra in matrix D (rows are the spectra)
# and the classes in vector y

fp = open("data/natural400_700_5.asc")
lines = fp.readlines()

D = zeros((0,61))
y = array([])
for i in range(0,len(lines),2):
	ind, c = containsColor(lines[i])
	if ind is not None:
		d = fromstring(lines[i+1],dtype=int,sep=" ")
		D = append(D,array([d]),axis=0)
		y = append(y,ind)

U, X = pca.pca(D, 3)
# TODO: X needs scaling to [0-1]

minval = X.min()
maxval = X.max()
X = (X - minval)/(maxval-minval)

classes = arange(len(Colors))

ind = arange(len(X))
ind = permutation(ind)
# Learning set
L = ind[0:110]
# Testing set
T = ind[109:]

# Split L into 10 parts
v = []
for i in range(0, 10):
	v.append(L[11 * i:11 * (i + 1)].tolist())

#quit()
nv = 0

# Do grid search
for c in range(-3, 16, 2):
	for gamma in range(-3, 16, 2):
		nv += 1
		nv %= len(v)
		
		vals1 = []
		vals2 = []
		vals3 = []
		for j in range(0, 11):
			vals1.append([])
			vals2.append([])
			vals3.append([])

		for i in v[nv]:
			vals1[int(y[i])].append(X[i][0].tolist())
			vals2[int(y[i])].append(X[i][1].tolist())
			vals3[int(y[i])].append(X[i][2].tolist())
		
		prob1 = svm_problem(classes, vals1)
		prob2 = svm_problem(classes, vals2)
		prob3 = svm_problem(classes, vals3)
		param = svm_parameter('-c ' + str(2**c) + ' -g ' + str(2**gamma))
		svm = svm_train(prob1, param)
		svm = svm_train(prob2, param)
		svm = svm_train(prob3, param)


		# TODO: Test accuracy using svm_predict & save result?
