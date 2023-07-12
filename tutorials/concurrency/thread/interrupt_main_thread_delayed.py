# https://superfastpython.com/interrupt-the-main-thread-in-python/
# SuperFastPython.com

# example of main thread cannot be interrupting while sleeping
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
    # block for a long time
    print("Main thread waiting...")
    sleep(7)
except KeyboardInterrupt:
    # terminate main thread
    print("Main interrupted! Exiting.")
    sys.exit()
