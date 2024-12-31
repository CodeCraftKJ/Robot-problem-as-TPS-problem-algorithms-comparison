def dfs(start, cleanable_tiles, grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    visited = set()
    cleaned = set()
    path = [start]

    def is_adjacent(p1, p2):
        return abs(p1[0] - p2[0]) <= 1 and abs(p1[1] - p2[1]) <= 1

    def clean_from(current):
        nonlocal path

        if not is_adjacent(current, path[-1]):
            stack = path[:]
            stack.pop()
            while not is_adjacent(current, path[-1]):
                path.append(stack.pop())

        if current in cleanable_tiles and current not in cleaned:
            cleaned.add(current)
            path.append(current)

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] != "1":
                visited.add((nx, ny))
                clean_from((nx, ny))

    visited.add(start)
    clean_from(start)

    if cleaned == set(cleanable_tiles):
        return path

    return None
