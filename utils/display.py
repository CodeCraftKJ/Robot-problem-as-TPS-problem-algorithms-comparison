from utils.grid import displayMultipleGrids, updateGrid
def displayResults(grid, start, algorithms, results, times):

    print("\n[INFO] Wyniki algorytmów (długość ścieżki i czas wykonania):\n")
    for name, result in results.items():
        if result:
            path_length = len(result)
            time_taken = times[name]
            print(f"{name}: Długość: {path_length}, Czas: {time_taken} ms, Ścieżka: {result}")
        else:
            print(f"{name}: Ścieżka nie została odnaleziona")

    print("\n[INFO] Wizualizacja ścieżek (pozycja początkowa):\n")
    algorithm_names = list(algorithms.keys())
    grids = [updateGrid(grid, start, []) for _ in range(len(algorithms))]
    displayMultipleGrids(grids, grid, algorithm_names)

    active_paths = {name: iter(result) if result else None for name, result in results.items()}
    current_positions = {name: start for name in algorithm_names}
    previous_positions = {name: [] for name in algorithm_names}

    step = 0
    while True:
        grids = []
        all_finished = True

        for name in algorithm_names:
            if active_paths[name]:
                try:
                    next_position = next(active_paths[name])
                    previous_positions[name].append(current_positions[name])
                    current_positions[name] = next_position
                    all_finished = False
                except StopIteration:
                    active_paths[name] = None

            updated_grid = updateGrid(grid, current_positions[name], previous_positions[name])
            grids.append(updated_grid)

        if step > 0:
            displayMultipleGrids(grids, grid, algorithm_names)

        if all_finished:
            print("\n[INFO] Wszystkie algorytmy zakończyły działanie.")
            break

        step += 1
        input()