from pylab import *
from svmutil import *
from StringIO import StringIO
import sys
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

print "Reading Dataset"
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

# Use PCA to reduce to 3 dimensions
U, X, M = pca.pca(D, 3)

# Scale values to [0-1]
minval = np.amin(X, axis=0)
maxval = np.amax(X, axis=0)
X = (X - minval)/(maxval-minval)

# randomly shuffle indices of the dataset X
ind = arange(len(X))
ind = permutation(ind)

# Learning set
L = ind[0:140]

# Testing set
T = ind[140:]

# Split L into 10 parts
v = []
vi = []
for i in range(0, 10):
	v.append(L[21 * i:21 * (i + 1)].tolist())
	vi.append(L[0:(21*i)].tolist() + L[21*(i+1):].tolist())

nv = 0
bestperc = 0.0
bestC = 0.0
bestG = 0.0

print "Searching best parameters"

# silence the svm output
bkp_stdout = sys.stdout
sys.stdout = StringIO()

# Do grid search
for c in range(-3, 16, 2):
	for gamma in range(-3, 16, 2):
		nv += 1
		nv %= len(v)
		
		# create an empty confusion matrix
		confusion=zeros((len(Colors),len(Colors)))

		prob = svm_problem(y[vi[nv]].tolist(), X[vi[nv]].tolist())
		param = svm_parameter('-q -c ' + str(2**c) + ' -g ' + str(2**gamma))
		svm = svm_train(prob, param)

		for i in v[nv]:
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
		
		# Check if the accuracy is the best accuracy found yet
		if bestperc < perc:
			bestC = c
			bestG = gamma
			bestperc = perc

# Test on testing set
prob = svm_problem(y[L].tolist(), X[L].tolist())
param = svm_parameter('-q -c ' + str(2**bestC) + ' -g ' + str(2**bestG))
svm = svm_train(prob, param)
confusion=zeros((len(Colors),len(Colors)))

for i in T:
	predictedClass, notused1, notused2 = svm_predict([0], [X[i].tolist()], svm);
	confusion[y[i], predictedClass[0]]+=1

# allow output again
sys.stdout = bkp_stdout
print "\n~ ~ ~ ~ ~\n"

# Show the results to the user
print 'Best parameters: (c, gamma)'
print str(2**bestC) + ", " + str(2**bestG)
print 'Best v-fold accuracy: ' + str(bestperc) + '%'

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
print 'Testing set accuracy: ' + str(perc) + '%'
