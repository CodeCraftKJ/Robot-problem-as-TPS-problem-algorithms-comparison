from utils.timeout import runWithTimeout
import time


def compareAlgorithms(algorithms, start, cleanable_tiles, grid):
    times = {}
    results = {}

    for name, algo in algorithms.items():
        start_time = time.perf_counter()

        try:
            result = runWithTimeout(algo, args=(start, cleanable_tiles, grid))
            end_time = time.perf_counter()
            times[name] = round((end_time - start_time) * 1000, 2)
            results[name] = result

        except TimeoutError:
            times[name] = "TIME LIMIT EXCEEDED"
            results[name] = None

    return times, results
