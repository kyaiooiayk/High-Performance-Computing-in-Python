# SuperFastPython.com
# https://superfastpython.com/auto-start-threads-in-python/

# example of automatically starting a thread
from time import sleep
from threading import Thread


# custom thread class that automatically starts threads when they are constructed
class AutoStartThread(Thread):
    # constructor
    def __init__(self, *args, **kwargs):
        # call the the parent constructor
        super().__init__(*args, **kwargs)
        # start the thread
        self.start()


# task function
def task():
    print("Task starting")
    # block for a moment
    sleep(1)
    # report
    print("Task all done")


# create and start the new thread
thread = AutoStartThread(target=task)
# wait for the new thread to finish
thread.join()
