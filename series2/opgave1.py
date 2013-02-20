import random

def generateGraph(NODES):
	graph = []
	
	random.seed(4321854)
	
	for i in range(0, NODES):
		innerList = []
		for j in range(0, NODES):
			if(i == j):
				innerList.append(0)
			elif(random.randint(0, 1) == 0):
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
	print("\n")

# Dijkstra algorithm, to find the shortest path between two given nodes.
def dijkstra(graph, end):
	nodes = len(graph)
	distances = []
	# initialize, no distances known yet
	for i in range(0, nodes):
		distances.append(-1)
	for i in range(0, nodes):
		for j in range(0, nodes):
			# we can only change if the vertex exists
			if(graph[i][j] != -1):
				# if a distance is known, add the distances, else use the found distance
				if(distances[i] != -1):
					test = graph[i][j] + distances[i]
				else:
					test = graph[i][j]
				# update the distance if the found value is shorter
				if(distances[j] == -1 or test < distances[j]):
					distances[j] = test
	# return the distance to the given node
	return distances[end]

NODES = 10;
generatedGraph = generateGraph(NODES)
printGraph(generatedGraph)
print("Dijkstra found: " + str(dijkstra(generatedGraph, NODES-1)))