# https://superfastpython.com/threading-in-python/

# example of an unhandled exception in a thread
from time import sleep
import threading


# target function that raises an exception
def work():
    print("Working...")
    sleep(1)
    # rise an exception
    raise Exception("Something bad happened")


# custom exception hook
def custom_hook(args):
    # report the failure
    print(f"Thread failed: {args.exc_value}")


# set the exception hook
threading.excepthook = custom_hook
# create a thread
thread = threading.Thread(target=work)
# run the thread
thread.start()
# wait for the thread to finish
thread.join()
# continue on
print("Continuing on...")
