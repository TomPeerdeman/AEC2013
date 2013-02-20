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

# Caculate the shortest path from node startnode to endnode in a recursive way
def shortestPathRecursive(graph, startnode, endnode, visited):
	numnodes = len(graph)
	
	# This node is being visited, so add it
	visited.append(startnode)
	
	# No path found, so lowest cost is inf
	lowcost = float('inf');
	# Node list of the path with the lowest cost
	lowvisited = []
	
	for node in range(0, numnodes):
		cost = graph[startnode][node]
		
		# Don't visit the node if:
		# 1. There is no path.
		# 2. I want to visit myself (again)
		# 3. I already did visit this node (anti cykel)
		if(cost > 0 and node != startnode and node not in visited):
			if(node == endnode):
				# We have found the end node trough startnode, add the endnode to the path and return the path
				visited.append(endnode)
				return cost, visited
			else:
				# Check for a path from node to the endnode. 
				# Copy the visited list so the current visited list isn't overwritten
				ncost, nvisited = shortestPathRecursive(graph, node, endnode, list(visited))
				ncost = ncost + cost
				
				if(ncost > cost and ncost < lowcost):
					# A path to the endnode is found and it's better than the ones we might have already found
					lowcost = ncost
					lowvisited = nvisited
	
	if(lowcost != float('inf')):
		# There was a path found, return it
		return lowcost, lowvisited
	
	# No path to endnode found trough this node
	return -1, visited
	
NODES = 13
graph = generateGraph(NODES)
printGraph(graph)
print shortestPathRecursive(graph, 0, NODES - 1, [])