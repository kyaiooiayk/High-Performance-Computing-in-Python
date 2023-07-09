# https://superfastpython.com/what-is-a-thread-in-python/
# https://superfastpython.com/thread-life-cycle-in-python/
    
# SuperFastPython.com
# example of extending the Thread class
from time import sleep
from threading import Thread
 
# custom thread class
class CustomThread(Thread):
    # override the run function
    def run(self):
        # block for a moment
        sleep(1)
        # display a message
        print('This is coming from another thread')
 
# create the thread
thread = CustomThread()
# start the thread
thread.start()
# wait for the thread to finish
print('Waiting for the thread to finish')
thread.join()