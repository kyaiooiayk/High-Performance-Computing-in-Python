# https://superfastpython.com/multiprocessing-main-thread/
# SuperFastPython.com


# example of getting the main thread of the main process
from multiprocessing import current_process
from threading import main_thread

# get the current process
process = current_process()
# get the main thread for the main process
thread = main_thread()
# report details
print(f"Process: {process.name}, main thread: {thread}")


# example of getting the main thread for child processes
from multiprocessing import current_process
from multiprocessing import Process
from threading import main_thread


# function executed in child processes
def task():
    # get the current process
    process = current_process()
    # get the main thread for the main process
    thread = main_thread()
    # report details
    print(f"Process: {process.name}, main thread: {thread}", flush=True)


# protect the entry point
if __name__ == "__main__":
    # create child processes
    children = [Process(target=task) for _ in range(5)]
    # start child processes
    for child in children:
        child.start()
    # wait for children processes to terminate
    for child in children:
        child.join()
