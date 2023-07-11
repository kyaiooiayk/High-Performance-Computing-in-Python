# https://superfastpython.com/thread-close/
# SuperFastPython.com

# example of closing a thread by returning
from random import random
from time import sleep
from threading import Thread
import sys


# task function
def task():
    # loop forever
    while True:
        # generate a random value between 0 and 1
        value = random()
        print(f".{value}")
        # block
        sleep(value)
        # check if we should forcefully close the thread
        if value > 0.9:
            print("Closing thread by return")
            return
        elif value < 0.9 and value > 0.8:
            print("Closing thread by sys.exit()")
            sys.exit()
        elif value < 0.8 and value > 0.7:
            print("Closing thread by raise")
            raise Exception("Stop now!")


# create and configure the new thread
thread = Thread(target=task)
# start the new thread
thread.start()
# wait for the thread to terminate
thread.join()
# main continues on
print("Main continuing on...")
