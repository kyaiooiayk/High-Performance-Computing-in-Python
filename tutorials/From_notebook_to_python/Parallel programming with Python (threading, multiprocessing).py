#!/usr/bin/env python
# coding: utf-8

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black><br>
#
# **What?** Parallel programming with Python (threading, multiprocessing)
#
# **Reference:** https://nbviewer.jupyter.org/github/ethen8181/machine-learning/blob/master/python/parallel.ipynb<br>
#
# <br></font>
# </div>

# # Import modules

# In[ ]:


import math
import time
import logging
import requests
import threading
import multiprocessing
import concurrent.futures
from joblib import Parallel, delayed

get_ipython().run_line_magic("load_ext", "watermark")


# In[ ]:


get_ipython().run_line_magic("watermark", "-p joblib,requests")


# # Introduction

# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - A **process** is a program that is in execution. In other words, code that are running (e.g. Jupyter notebook, Google Chrome, Python interpreter). Multiple processes are always running in parallel in a parallel.
# - A process can spawn multiple **threads (sub-processes)** to handle subtasks. They live inside processes and share the same memory space (they can read and write to the same variables). Ideally, they run in parallel, but not necessarily.
#
# <br></font>
# </div>

# # Threading

# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - When we run a program whic takes for a few seconds, we would have to wait for that portion to wake up before we can continue with the rest of the program.
# - The concurrency of threads can bypass this behavior.
#
# <br></font>
# </div>

# In[ ]:


def sleeper(n_time):
    name = threading.current_thread().name
    print("I am {}. Going to sleep for {} seconds".format(name, n_time))
    time.sleep(n_time)
    print("{} has woken up from sleep".format(name))


# In[ ]:


# we call .start to start executing the function from the thread
n_time = 4
thread = threading.Thread(target=sleeper, name="thread1", args=(n_time,))
thread.start()


# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - To demonstrate the **concurrency property**, i.e. we don't have to wait for the calling thread to finish before running the rest of our program.
#
# <br></font>
# </div>

# In[ ]:


# hello is printed "before" the wake up message from the function
thread = threading.Thread(target=sleeper, name="thread2", args=(n_time,))
thread.start()

print()
print("hello, still doing something even if thread2 has not finished")


# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - Sometimes, we don't want Python to switch to the main thread until the thread has finished.
# - To do this, we can use **.join** method.
# - It blocks the interpreter from accessing or executing the main program until the thread finishes it task.
#
# <br></font>
# </div>

# In[ ]:


# hello is printed "after" the wake up message from the function
thread = threading.Thread(target=sleeper, name="thread3", args=(n_time,))
thread.start()
print("waiting rhread3 to finish before moving on")
thread.join()

print()
print("hello")


# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - The following code chunk showcase how to initialize and utilize multiple threads.
# - it doesn't take n_threads * n_time amount of time to finish all the task!
#
# <br></font>
# </div>

# In[ ]:


n_time = 5
n_threads = 5
start = time.time()

# create n_threads number of threads and store them in a list
threads = []
for i in range(n_threads):
    name = "\nthread{}".format(i)
    thread = threading.Thread(target=sleeper, name=name, args=(n_time,))
    threads.append(thread)
    # we can start the thread while we're creating it, or move
    # this to its own loop (as shown below)
    thread.start()

# we could instead start the thread in a separate loop
# for thread in threads:
#     thread.start()

# ensure all threads have finished before executing main program
for thread in threads:
    thread.join()

elapse = time.time() - start
print()
print("Elapse time: ", elapse)


# # concurrent.futures

# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - This provides high level API for launching asynchronous tasks.
# - ATTENTION: it will not work in ipython!
# - see this discussion: https://stackoverflow.com/questions/15900366/all-example-concurrent-futures-code-is-failing-with-brokenprocesspool
#
# <br></font>
# </div>

# In[ ]:


# example from the documentation page
# https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor-example
def is_prime(n):
    """
    References
    ----------
    https://math.stackexchange.com/questions/1343171/why-only-square-root-approach-to-check-number-is-prime
    """
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False

    return True


PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
]

with concurrent.futures.ProcessPoolExecutor() as executor:
    for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
        print("{} is prime: {}".format(number, prime))


# # Comparison: multi-processing vs. multi-threading

# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - **Serial approach**: We're running the tasks one after the other. Each run is executed by the same thread of the same process.
# - **multiprocessing will not work OK in ipython!**
# - To make multiprocessing work in ipython see this discussion: https://stackoverflow.com/questions/50937362/multiprocessing-on-python-3-jupyter
# - **Multi-threading approach**: takes advantage of the fact that the tasks can be executed concurrently. The execution time is also cut down to a quarter, **even though nothing** is running in parallel.
# - If we had managed to use multi-processing, we'd have seen that the threaded approach is quicker than the truly parallel one. That's due to the overhead of spawning processes. As we noted previously, spawning and switching processes is much more expensive and requires more resources.
#
# <br></font>
# </div>

# In[11]:


print("Number of cpu : ", multiprocessing.cpu_count())


# In[75]:


def only_sleep(dummy=0):
    """Wait for a timer to expire"""
    process_name = multiprocessing.current_process().name
    thread_name = threading.current_thread().name
    print("Process Name: {}, Thread Name: {}".format(process_name, thread_name))

    time.sleep(2)


def crunch_numbers():
    """Do some computations"""
    process_name = multiprocessing.current_process().name
    thread_name = threading.current_thread().name
    print("\nProcess Name: {}, Thread Name: {}".format(process_name, thread_name))

    x = 0
    while x < 10000000:
        x += 1


# In[78]:


def experiment(target, n_workers, onIpython=True):
    """
    run the target function serially, using threads,
    using process and output the run time
    """

    # Run tasks serially
    start_time = time.time()
    for _ in range(n_workers):
        target()

    end_time = time.time()
    print("Serial time=", end_time - start_time)
    print()

    if onIpython == False:
        # Run tasks using processes
        print("Run tasks using processes")
        start_time = time.time()
        processes = [multiprocessing.Process(target=target) for _ in range(n_workers)]

        # If we create a process object, nothing will happen until we start it
        for i, process in enumerate(processes):
            # process.start()
            process.run()

        for process in processes:
            process.join()

        end_time = time.time()
        print("Parallel time=", end_time - start_time)
        print()

    # Run tasks using threads
    print("\nRun tasks using threads")
    start_time = time.time()
    threads = [threading.Thread(target=target) for _ in range(n_workers)]
    for thread in threads:
        thread.start()

    # Wait of all the process before moving on
    for thread in threads:
        thread.join()

    end_time = time.time()
    print("Threads time=", end_time - start_time)


# In[79]:


n_workers = 4
experiment(target=only_sleep, n_workers=n_workers)


# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - Let's perform the same routine but this time on the crunch_numbers function.
# - This task was design to be CPU intensive.
# - You can see that multi-threading performs very similarly to serial approach.
# - **Why?** Crunch_numbers performs computations and Python doesn't perform real parallelism, the threads are basically running one after the other until they all finish. In fact it might even be slower, as we need to take into account the overhead of launching multiple threads.
#
# <br></font>
# </div>

# In[80]:


n_workers = 4
experiment(target=crunch_numbers, n_workers=n_workers)


# # Conclusion

# <div class="alert alert-danger">
# <font color=black>
#
# - The bottmo line is that:
# - For CPU (**CPU bound**) itensive operations such as crunching number use multi-processing
# - For I/O (**I/O bound**) intensive operations such as checking websites downtime use multi-threading.
#
# </font>
# </div>

# In[ ]:
