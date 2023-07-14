# https://superfastpython.com/threads-in-processes-with-python/
# SuperFastPython.com

# example of starting threads in child processes
from random import random
from time import sleep
from threading import Thread
from threading import current_thread
from multiprocessing import Process
from multiprocessing import current_process


# task executed by new threads
def thread_task():
    # block for a moment
    sleep(3 * random())
    # report a message
    process_name = current_process().name
    thread_name = current_thread().name
    print(f">thread {thread_name} in process {process_name} done.", flush=True)


# task executed by new processes
def process_task():
    # configure new threads
    threads = [Thread(target=thread_task) for _ in range(3)]
    # start new threads
    for thread in threads:
        thread.start()
    # wait for threads to finish
    for thread in threads:
        thread.join()
    # report message
    process_name = current_process().name
    print(f"Process {process_name} done.", flush=True)


# protect the entry point
if __name__ == "__main__":
    # configure child processes
    processes = [Process(target=process_task) for _ in range(5)]
    # start new processes
    for child in processes:
        child.start()
    # wait for processes to finish
    for child in processes:
        child.join()
    # report message
    print("Main process done.", flush=True)
