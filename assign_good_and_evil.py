from dsc40graph import UndirectedGraph
from collections import deque

def assign_good_and_evil(graph):
    label = {}
    for start in graph.nodes:
        if start not in label:
            label[start] = 'good'
            queue = deque([start])

            while queue:
                curr = queue.popleft()
                curr_label = label[curr]
                if curr_label == 'good':
                	next_label = 'evil'
                else:
                	next_label = 'good'
                for neighbor in graph.neighbors(curr):

                    if neighbor not in label:
                        label[neighbor] = next_label
                        queue.append(neighbor)

                    elif label[neighbor] == curr_label:
                        return None
    return label



# example_graph = UndirectedGraph()
# example_graph.add_edge('Michigan', 'OSU')
# example_graph.add_edge('USC', 'OSU')
# example_graph.add_edge('USC', 'UCB')
# example_graph.add_node('UCSD')

# print(assign_good_and_evil(example_graph))