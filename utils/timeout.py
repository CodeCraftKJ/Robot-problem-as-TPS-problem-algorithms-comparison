import threading
from queue import Queue

#TODO
def runWithTimeout(func, args=(), kwargs=None, timeout=1):
    if kwargs is None:
        kwargs = {}

    result = Queue()

    def wrapper():
        result.put(func(*args, **kwargs))

    thread = threading.Thread(target=wrapper)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        return "TIME LIMIT EXCEEDED"

    return result.get()
