from dsc40graph import DirectedGraph
from collections import deque

def biggest_descendent(graph, root, value):
	result = {}
	def dfs(u):
		best = value[u]
		for v in graph.neighbors(u):
			best = max(best, dfs(v))

		result[u] = best
		return best

	dfs(root)
	return result



# edges = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 8), (4, 9), (3, 6), (3, 7)]
# g = DirectedGraph()
# for edge in edges: g.add_edge(*edge)
# value = {1: 2, 2: 1, 3: 4, 4: 8, 5: 5, 6: 2, 7: 10, 8:3, 9: 9}
# print(biggest_descendent(g, 1, value))