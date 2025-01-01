from heapq import heappush, heappop
from algorithms.greedyBfsHeuristic import manhattanDistance
from utils.gridAlgorithms import gridToGraph

def heuristic(current, remaining):
    return min(manhattanDistance(current, tile) for tile in remaining)

def aStar(start, cleanable_tiles, grid):
    # AStar

    graph = gridToGraph(start, cleanable_tiles, grid)
    all_cleanable = set(cleanable_tiles)
    visited = set()
    full_path = []

    current = start
    while visited != all_cleanable:
        priority_queue = [(0, current, [], 0)]
        local_visited = set()
        best_path = None

        while priority_queue:
            f, node, path, g = heappop(priority_queue)

            if node in local_visited:
                continue
            local_visited.add(node)

            if node in all_cleanable and node not in visited:
                best_path = path + [node]
                visited.add(node)
                break

            for neighbor in graph.get(node, []):
                if neighbor not in local_visited:
                    g_new = g + 1
                    h = heuristic(neighbor, all_cleanable - visited)
                    heappush(priority_queue, (g_new + h, neighbor, path + [node], g_new))

        if best_path:
            full_path.extend(best_path[:-1])
            current = best_path[-1]
        else:
            return None

    full_path.append(current)
    return full_path

