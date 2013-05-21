from pylab import *

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
	print ind
	if ind is not None:
		d = fromstring(lines[i+1],dtype=int,sep=" ")
		D = append(D,array([d]),axis=0)
		y = append(y,ind)
