import random

def generateGraph(NODES):
	graph = []
	
	random.seed(4321854)
	
	for i in range(0, NODES):
		innerList = []
		for j in range(0, NODES):
			if(random.randint(0, 1) == 0):
				innerList.append(random.randint(1, 100))
			else:
				innerList.append(-1);

		graph.append(innerList)
		
	return graph
  
# helper function, shows the matrix in an understandable way
def printGraph(graph):
  rows = len(graph)
  for i in range(0, rows):
    print(graph[i])
	
printGraph(generateGraph(10))