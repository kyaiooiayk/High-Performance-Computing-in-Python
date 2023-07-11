# https://superfastpython.com/threading-in-python/
# https://superfastpython.com/thread-local-data/

# example of thread local storage
from time import sleep
import threading


# custom target function
def task(value):
    # create a local storage
    local = threading.local()
    # store data
    local.value = value
    # block for a moment
    sleep(value)
    # retrieve value
    print(f"Stored value: {local.value}")


# create and start a thread
threading.Thread(target=task, args=(1,)).start()
# create and start another thread
threading.Thread(target=task, args=(2,)).start()
