from pylab import *
from svmutil import *
import thread
from pca import *

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

# use PCA to make sure only 3 dimensions are used
#G = pca(D, 3)
G=D

# scale the data
minval = G.min()
maxval = G.max()
H = (G - minval)/(maxval-minval)

# get the length of the dataset and perform a permutation
N = len(H)
perm = permutation(arange(0,N))

# create a learning set
learning=perm[N/3:]
print learning

bestparam = svm_parameter()
bestperc = 0.0
for c in range(-3, 16, 2):
	for gamma in range(-3, 16, 2):
		# set parameters
		param = '-c ' + str(2**c) + ' -g ' + str(2**gamma) + ' -q'

		# train the svm
		train= svm_train(y[learning].tolist(), H[learning].tolist(), param)

		# create an empty confusion matrix
		confusion=zeros((len(Colors),len(Colors)))

		# use the trained svm to predict the outcome
		for i in perm:
			predictedClass, notused1, notused2 = svm_predict([0], [H[i].tolist()],train)
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
			bestperc = perc
			bestparam = param
# Show the results to the user
print '\n~ ~ ~ ~ ~ ~'
print 'Best parameters: '
print param
print 'Best Accuracy'
print str(perc) + '%'
