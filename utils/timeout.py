import threading
from queue import Queue


def runWithTimeout(func, args=(), kwargs={}, timeout=15000000000):
    result = Queue()

    def wrapper():
        result.put(func(*args, **kwargs))

    thread = threading.Thread(target=wrapper)
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        return "TIME LIMIT EXCEEDED"
    return result.get()
