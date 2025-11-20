from dsc40graph import UndirectedGraph
from collections import deque

def cluster(graph, weights, level):

	clusters = []
	visited = {node:"undiscovered" for node in graph.nodes}

	for start in graph.nodes:
		if visited[start] == "visited":
			continue
		pending = deque([start])
		component = set()
		visited[start] = "visited"

		while pending:
			u = pending.popleft()
			component.add(u)

			for v in graph.neighbors(u):
				if visited[v] == "undiscovered" and weights(u, v) >= level:
					visited[v] = "visited"
					pending.append(v)

		clusters.append(frozenset(component))
	return frozenset(clusters)