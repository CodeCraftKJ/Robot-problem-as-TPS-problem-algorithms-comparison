

def manhattanDistance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def gridToGraph(start, cleanable_tiles, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    graph = {}

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != "1":
                node = (r, c)
                neighbors = []

                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "1":
                        neighbors.append((nr, nc))

                if neighbors:
                    graph[node] = neighbors

    return graph