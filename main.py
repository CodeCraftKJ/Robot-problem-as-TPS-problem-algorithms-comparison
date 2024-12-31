from algorithms.dfsBacktracking import dfs
from algorithms.greedyBfsHeuristic import greedy
from algorithms.tsp import tsp
from utils.display import displayResults
from utils.grid import createGrid, findCleanableTitles, getStartingPosition
from utils.compare import compareAlgorithms
from algorithms.dijkstra import dijkstra
from algorithms.astar import aStar

def main():
    grid = createGrid()
    start = getStartingPosition(grid)
    cleanable_tiles = findCleanableTitles(grid)

    algorithms = {
        "DFS with Backtracking": dfs,
        "Greedy BFS + Heuristic": greedy,
        "Dijkstra": dijkstra,
        "A* Star": aStar,
        "TPS Dynamic": tsp
    }

    times, results = compareAlgorithms(algorithms, start, cleanable_tiles, grid)

    displayResults(grid, start, algorithms, results, times)


if __name__ == "__main__":
    main()
