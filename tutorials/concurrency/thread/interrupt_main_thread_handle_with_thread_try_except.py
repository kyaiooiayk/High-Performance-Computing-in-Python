# https://superfastpython.com/interrupt-the-main-thread-in-python/
# SuperFastPython.com

# example of interrupting the main thread and handle with try-except
from time import sleep
from threading import Thread
from _thread import interrupt_main
import sys


# task executed in a new thread
def task():
    # block for a moment
    sleep(3)
    # interrupt the main thread
    print("Interrupting main thread now")
    interrupt_main()


# start the new thread
thread = Thread(target=task)
thread.start()
# handle being interrupted
try:
    # wait around
    while True:
        print("Main thread waiting...")
        sleep(0.5)
except KeyboardInterrupt:
    # terminate main thread
    print("Main interrupted! Exiting.")
    sys.exit()
