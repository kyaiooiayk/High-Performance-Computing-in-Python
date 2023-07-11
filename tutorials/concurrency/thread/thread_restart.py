# https://superfastpython.com/restart-a-thread-in-python/


# SuperFastPython.com
# example of reusing a thread
from time import sleep
from threading import Thread


# custom target function
def task():
    # block for a moment
    sleep(1)
    # report a message
    print("Hello from the new thread")


# create a new thread
thread = Thread(target=task)
# start the thread
thread.start()
# wait for the thread to finish
thread.join()

# create a new thread with the same config
# You cannot restart a thread in Python, instead you must create and start a new thread with the same configuration.
thread2 = Thread(target=task)
# start the new thread
thread2.start()
# wait for the new thread to finish
thread2.join()
