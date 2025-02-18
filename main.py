from algorithms.astar import aStar
from algorithms.dfsBacktracking import dfs
from algorithms.dijkstra import dijkstra
from algorithms.greedyBfsHeuristic import greedy
from algorithms.tsp import tsp
from utils.compare import compareAlgorithms
from utils.display import displayResults
from utils.grid import findCleanableTitles, getStartingPosition, loadGridFromFile, getExampleFiles

def main():
    examples = getExampleFiles()
    for example in examples:
        grid = loadGridFromFile(example)
        start = getStartingPosition(grid)
        cleanable_tiles = findCleanableTitles(grid)

        algorithms = {
            "DFS": dfs,
            "Gr/BFS": greedy,
            "Dijkstra": dijkstra,
            "A*": aStar,
            "TPS": tsp
        }

        times, results = compareAlgorithms(algorithms, start, cleanable_tiles, grid)
        displayResults(grid, start, algorithms, results, times)


if __name__ == "__main__":
    main()
