from utils.timeout import runWithTimeout
import time


def compareAlgorithms(algorithms, start, cleanable_tiles, grid):
    times = {}
    results = {}

    for name, algo in algorithms.items():
        start_time = time.perf_counter()
        result = runWithTimeout(algo, args=(start, cleanable_tiles, grid), timeout=3000)
        end_time = time.perf_counter()

        if result == "TIME LIMIT EXCEEDED":
            times[name] = "TIME LIMIT EXCEEDED"
            results[name] = None
        else:
            times[name] = round((end_time - start_time) * 1000, 2)
            results[name] = result

    return times, results
