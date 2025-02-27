import heapq

from utils.gridAlgorithms import gridToGraph


def dijkstra(start, cleanable_tiles, grid):
    # Dijkstra
    graph = gridToGraph(start, cleanable_tiles, grid)

    def find_shortest_path(start, end):
        priority_queue = [(0, start, [])]
        visited = set()

        while priority_queue:
            cost, current, path = heapq.heappop(priority_queue)

            if current == end:
                return path + [current]

            if current in visited:
                continue
            visited.add(current)

            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + 1, neighbor, path + [current]))

        return []

    points_to_visit = cleanable_tiles[:]

    total_path = []
    current_point = start

    while points_to_visit:
        shortest_path = None
        next_point = None

        for point in points_to_visit:
            if point == current_point:
                continue

            path = find_shortest_path(current_point, point)

            if not shortest_path or len(path) < len(shortest_path):
                shortest_path = path
                next_point = point

        if next_point:
            total_path += shortest_path[1:]
            current_point = next_point
            points_to_visit.remove(current_point)

    if set(cleanable_tiles) != set(total_path):
        return None
    return [start]+total_path