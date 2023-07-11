# SuperFastPython.com
# https://superfastpython.com/stop-a-thread-in-python/

# example of stopping a new thread
from time import sleep
from threading import Thread
from threading import Event


# custom task function
def task(event):
    # execute a task in a loop
    for i in range(5):
        print(i, "/5 going to sleep")
        # block for a moment
        sleep(1)
        # check for stop
        if event.is_set():
            break
        # report a message
        print("Worker thread running...")
    print("Worker closing down")


# create the event
event = Event()
# create and configure a new thread
thread = Thread(target=task, args=(event,))
# start the new thread - start looping as per task
thread.start()
# block for a while the main thread
sleep(3)
# main thread wakes up stop the worker thread
print("Main stopping thread")
event.set()
# wait for the new thread to finish
thread.join()
