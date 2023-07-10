# SuperFastPython.com
# https://superfastpython.com/run-function-in-new-thread/

# example of executing a target task function in a separate thread
from time import sleep
from threading import Thread


# a custom function that blocks for a moment
def task(sleep_time, message):
    # block for a moment
    sleep(sleep_time)
    # display a message
    print(message)


# create a thread
thread = Thread(target=task, args=(1.5, "New message from another thread"))
# run the thread
thread.start()
# wait for the thread to finish
print("Waiting for the thread...")
thread.join()
