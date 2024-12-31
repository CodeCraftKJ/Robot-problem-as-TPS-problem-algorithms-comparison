def createGrid():
    return [
        ["1", "S", " ", " ", " ", " ", " ", " ", " ", "1"],
        ["1", " ", " ", " ", " ", " ", " ", " ", " ", "1"],
        ["1", " ", " ", "1", " ", " ", "1", " ", " ", "1"],
        ["1", " ", " ", " ", " ", " ", " ", " ", " ", "1"],
        ["1", " ", " ", " ", "1", " ", " ", " ", " ", "1"],
        ["1", " ", " ", " ", " ", " ", " ", " ", " ", "1"],
        ["1", " ", "1", " ", " ", " ", " ", "1", " ", "1"],
        ["1", " ", " ", " ", " ", " ", " ", " ", " ", "1"]
    ]

def findCleanableTitles(grid):
    return [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == " "]

def getStartingPosition(grid):
    return next((i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "S")

def updateGrid(grid, position, previous_positions):
    new_grid = [row[:] for row in grid]
    for i, j in previous_positions:
        if grid[i][j] == " ":
            new_grid[i][j] = "."
    x, y = position
    new_grid[x][y] = "*"
    return new_grid


def displayMultipleGrids(grids, original_grid, algorithm_names):

    separator = " " * 5
    grid_width = len(original_grid[0])
    grid_height = len(original_grid)
    header = ""

    for name in algorithm_names:
        header += name.center(grid_width * 3) + separator
    print(header.rstrip())

    for row_idx in range(grid_height):
        row_to_print = ""
        for grid_idx, grid in enumerate(grids):
            row_to_print += "".join([f"{cell}".center(3) for cell in grid[row_idx]]) + separator
        print(row_to_print.rstrip())

    print()
