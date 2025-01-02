import threading
from queue import Queue


def runWithTimeout(func, args=(), kwargs=None, timeout=1):
    if kwargs is None:
        kwargs = {}

    result = Queue()

    def wrapper():
        try:
            result.put(func(*args, **kwargs))
        except Exception as e:
            result.put(e)

    thread = threading.Thread(target=wrapper)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        raise TimeoutError("TIME LIMIT EXCEEDED")

    return result.get()
