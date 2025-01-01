from algorithms.astar import aStar
from algorithms.dfsBacktracking import dfs
from algorithms.dijkstra import dijkstra
from algorithms.greedyBfsHeuristic import greedy
from algorithms.tsp import tsp
from utils.compare import compareAlgorithms
from utils.display import displayResults
from utils.grid import findCleanableTitles, getStartingPosition, loadGridFromFile
import os


def main():
    grid_folder = 'examples'
    grid_files = [f for f in os.listdir(grid_folder) if f.endswith('.txt')]

    for filename in grid_files:
        file_path = os.path.join(grid_folder, filename)

        grid = loadGridFromFile(file_path)
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
