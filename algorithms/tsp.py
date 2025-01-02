import itertools
from utils.gridAlgorithms import gridToGraph

def tsp(start, cleanable_tiles, grid):
    graph = gridToGraph(start, cleanable_tiles, grid)
    nodes = list(cleanable_tiles)

    distances = {}
    for node1, node2 in itertools.combinations([start] + nodes, 2):
        if node2 in graph.get(node1, {}):
            distances[(node1, node2)] = 1
            distances[(node2, node1)] = 1
        else:
            distances[(node1, node2)] = float('inf')
            distances[(node2, node1)] = float('inf')

    min_path = None
    min_cost = float('inf')

    for perm in itertools.permutations(nodes):
        path = [start] + list(perm)
        cost = 0
        valid_path = True

        for i in range(len(path) - 1):
            edge_cost = distances.get((path[i], path[i + 1]), float('inf'))
            if edge_cost == float('inf'):
                valid_path = False
                break
            cost += edge_cost

        if valid_path and cost < min_cost:
            min_cost = cost
            min_path = path

    return min_path
