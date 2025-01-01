from collections import deque
from utils.gridAlgorithms import manhattanDistance

def greedy(start, cleanable_tiles, grid):
    # Greedy BFS + Heuristic
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    cleaned = set()
    path = [start]

    while len(cleaned) < len(cleanable_tiles):

        current = path[-1]
        moved = False

        for direction in directions:
            next_position = moveInDirection(current, direction)

            if 0 <= next_position[0] < rows and 0 <= next_position[1] < cols:
                if next_position in cleanable_tiles and next_position not in cleaned:
                    path.append(next_position)
                    cleaned.add(next_position)
                    moved = True
                    break

        if not moved:
            nearest_cleanable = None
            min_distance = float('inf')

            for tile in cleanable_tiles:
                if tile not in cleaned:
                    distance = manhattanDistance(current, tile)
                    if distance < min_distance:
                        min_distance = distance
                        nearest_cleanable = tile

            if nearest_cleanable:
                bfs_path = bfs(current, nearest_cleanable, grid)
                if bfs_path:
                    path.extend(bfs_path[1:])
                    current = bfs_path[-1]
                    cleaned.add(current)

    return path

def bfs(start, goal, grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    queue = deque([(start, [start])])
    visited = {start}
    shortest_path = None

    while queue:
        current, current_path = queue.popleft()

        if current == goal:
            if shortest_path is None or len(current_path) < len(shortest_path):
                shortest_path = current_path

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != "1" and (nx, ny) not in visited:
                if shortest_path is None or len(current_path) + 1 <= len(shortest_path):
                    visited.add((nx, ny))
                    queue.append(((nx, ny), current_path + [(nx, ny)]))

    return shortest_path

def moveInDirection(current, direction):
    dx, dy = direction
    return current[0] + dx, current[1] + dy

