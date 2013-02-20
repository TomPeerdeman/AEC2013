import random

def generateGraph(NODES):
	graph = []
	
	random.seed(4321854)
	
	for i in range(0, NODES):
		innerList = []
		for j in range(0, NODES):
			# move to myself? set to Zero
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
				if(cost < lowcost):
					# A direct path to the endnode is found and it's better than the ones we might have already found
					lowcost = cost
					lowvisited = visited
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

def getMinIndex(heap):
	length = len(heap)
	index = 0
	for i in range(1,length):
		if(heap[i][1] < heap[index][1]):
			index = i
	return index

# Dijkstra algorithm, to find the shortest path between two given nodes.
def dijkstra(graph, end):
	nodes = len(graph)
	distances = []
	# initialize, no distances known yet
	for i in range(0, nodes):
		distances.append(-1)
	# create an empty heap
	heap = []
	# add the first node to the heap, the start node.
	# A,B represents from start to A, with distance B
	heap.append([0,0])
	# dont stop until all edges have been looked at
	while not len(heap) == 0:
		# get the lowest weight value to move to a new node
		index = getMinIndex(heap)
		# apply the found index to get the right node
		node = heap.pop(index)
		# no distance found for this location yet?
		if distances[node[0]] == -1:
			# set best distance
			distances[node[0]] = node[1]
			# walk past all nodes
			for i in range(nodes):
				# if i am not myself, continue
				if i != node[0]:
					# if a valid move between nodes is found, add it to the heap
					if graph[node[0]][i] >= 0:
						heap.append([i,node[1]+graph[node[0]][i]])
	return distances[end]

for i in range(2, 14):
	NODES = i
	graph = generateGraph(NODES)
	printGraph(graph)
	print 8
	print "Recursive found: " + str(shortestPathRecursive(graph, 0, NODES - 1, []))
	print("Dijkstra found: " + str(dijkstra(graph, NODES-1)))
	print "\n"
