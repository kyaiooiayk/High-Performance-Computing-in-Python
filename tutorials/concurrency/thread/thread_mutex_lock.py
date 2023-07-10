# https://superfastpython.com/threading-in-python/

# example of a mutual exclusion (mutex) lock
from time import sleep
from random import random
from threading import Thread
from threading import Lock


# work function
def task(lock, identifier, value):
    # acquire the lock
    with lock:
        print(f">thread {identifier} got the lock, sleeping for {value}")
        sleep(value)


# create a shared lock
lock = Lock()
# start a few threads that attempt to execute the same critical section
for i in range(10):
    # start a thread
    Thread(target=task, args=(lock, i, random())).start()
# wait for all threads to finish...
