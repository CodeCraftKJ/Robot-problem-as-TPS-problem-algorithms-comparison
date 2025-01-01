import itertools
from utils.gridAlgorithms import gridToGraph, manhattanDistance

# TODO
def tsp(start, cleanable_tiles, grid):
    # TSP + DP
    graph = gridToGraph(start, cleanable_tiles, grid)
    nodes = list(cleanable_tiles)

    distances = {}
    for node1, node2 in itertools.combinations([start] + nodes, 2):
        dist = manhattanDistance(node1, node2)
        distances[(node1, node2)] = dist
        distances[(node2, node1)] = dist

    min_path = None
    min_cost = float('inf')

    for perm in itertools.permutations(nodes):
        path = [start] + list(perm)
        cost = sum(distances[(path[i], path[i + 1])] for i in range(len(path) - 1))

        if cost < min_cost:
            min_cost = cost
            min_path = path

    return min_path

