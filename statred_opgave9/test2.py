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

bestparam = svm_parameter()
bestperc = 0.0
bestC = 0.0
bestG = 0.0
# Do grid search
for c in range(-3, 16, 2):
	for gamma in range(-3, 16, 2):
		nv += 1
		nv %= len(v)
		
		# create an empty confusion matrix
		confusion=zeros((len(Colors),len(Colors)))

		prob = svm_problem(y[v[nv]].tolist(), X[v[nv]].tolist())
		param = svm_parameter('-q -c ' + str(2**c) + ' -g ' + str(2**gamma))
		svm = svm_train(prob, param)

		for xv in range(0, 10):
			if(xv != nv):
				for i in v[xv]:
					predictedClass, notused1, notused2 = svm_predict([0], [X[i].tolist()], svm);
					confusion[y[i], predictedClass[0]]+=1

		# Calculate the accuracy of the SVM
		totalmiss= 0.0;
		total = 0.0;
		for i in range(-1,len(Colors)):
			for j in range(-1, len(Colors)):
				if i != j:
					totalmiss+=confusion[i,j]
				total += confusion[i,j]
		perc = totalmiss / total * 100.0;
		perc = 100.0 - perc;
		if bestperc < perc:
			bestC = c
			bestG = gamma
			bestperc = perc
			bestparam = param		
		# TODO: Test accuracy using svm_predict & save result?
# Show the results to the user
print '\n~ ~ ~ ~ ~ ~'
print 'Best parameters: '
print bestparam
print "\n" + str(2**bestC) + "," + str(2**bestG)
print 'Best Accuracy'
print str(perc) + '%'


