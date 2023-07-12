# https://superfastpython.com/interrupt-the-main-thread-in-python/
# SuperFastPython.com

# example of interrupting the main thread and handle with signal handler
from time import sleep
from threading import Thread
from _thread import interrupt_main
from signal import signal
from signal import SIGINT
import sys


# handle single
def handle_sigint(signalnum, frame):
    # terminate
    print("Main interrupted! Exiting.")
    sys.exit()


# task executed in a new thread
def task():
    # block for a moment
    sleep(3)
    # interrupt the main thread
    print("Interrupting main thread now")
    interrupt_main()


# register the signal handler for this process
signal(SIGINT, handle_sigint)
# start the new thread
thread = Thread(target=task)
thread.start()
# wait around
while True:
    print("Main thread waiting...")
    sleep(0.5)
