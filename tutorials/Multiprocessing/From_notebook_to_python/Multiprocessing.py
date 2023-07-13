#!/usr/bin/env python
# coding: utf-8

# # Introduction

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Multiprocessing
# 
# </font>
# </div>

# # Import modules

# In[1]:


import multiprocessing


# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - If you have forty cores available, then your script should ideally be able to do forty things at once.
# - However my Apple machines says:
#     
# Hardware Overview:<br>
# 
# Model Name:	MacBook Pro<br>
# Model Identifier:	MacBookPro13,3<br>
# Processor Name:	Intel Core i7<br>
# Processor Speed:	2.6 GHz<br>
# Number of Processors:	1<br>
# Total Number of Cores:	4<br>
# L2 Cache (per Core):	256 KB<br>
# L3 Cache:	6 MB<br>
# Memory:	16 GB<br>
# Boot ROM Version:	428.0.0.0.0<br>
# SMC Version (system):	2.38f7<br>
# Serial Number (system):	C02SXDLLGTFL<br>
# Hardware UUID:	52FC23EF-766A-5A25-82B8-8D0614E96355<br>
# 
# <br></font>
# </div>

# In[2]:


print(multiprocessing.cpu_count())


# # The multiprocessing modules

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - Multiprocessing allows your script to do lots of things at once by actually running multiple copies of your script in parallel
# - One of these copies is known as the **master copy**, and is the one that is used to control all of worker copies.
# - For this reason it is not recommended to use via ipython!
# - It forces you to write it in a particular way. All imports should be at the top of the script, followed by all function and class definitions. This is to ensure that all copies of the script have access to the same modules, functions and classes.
# - Then, you should ensure that only the master copy of the script runs the code by protecting it behind an if **__name__ == "__main__"** statement.
# - The multiprocessing.Pool provides an excellent mechanism for the parallelisation of map/reduce style calculations.
# 
# <br></font>
# </div>

# # How to run multiprocessing

# ## Step #1

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - Create a new script called **pool.py** and type into it.
# 
# <br></font>
# </div>

# In[1]:


get_ipython().system('ls')


# In[ ]:


from functools import reduce
from multiprocessing import Pool, cpu_count, current_process

def square(x):
    """Function to return the square of the argument"""
    #print("Worker %s calculating square of %s" % (current_process().pid, x))
    return x * x

if __name__ == "__main__":
    """
    You must now protect the code being run by
    the master copy of the script by placing it
    in this block
    """
    
    # print the number of cores
    print("Number of cores available equals %s" % cpu_count())
    
    # create a pool of workers
    """
    
    """
    with Pool(processes = cpu_count()) as pool:
        # create an array of 5000 integers, from 1 to 5000
        r = range(1, 5001)

        result = pool.map(square, r)

    total = reduce(lambda x, y: x + y, result)

    print("The sum of the square of the first 5000 integers is %s" % total)


# ## Step #2

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - Run the script using the command
# - The "!" allows you to run a commnad as if you were doing it from python sheel direcly
# - We are forced to do it because it is not advisable to run multiprocessing form ipython
# 
# <br></font>
# </div>

# In[5]:


get_ipython().system('python pool.py')


# # Synchronous function

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - The Pool.map function allows you to map a single function across an entire list of data. 
# - But what if you want to apply lots of different functions? 
# - To do this you need to use **apply()**
# - Let's create a script called poolapply.py and type into it
# 
# <br></font>
# </div>

# In[ ]:


import time
from multiprocessing import Pool, current_process

def slow_function(nsecs):
    """
    Function that sleeps for 'nsecs' seconds, returning
    the number of seconds that it slept
    """

    print("Process %s going to sleep for %s second(s)" % (current_process().pid, nsecs))

    # use the time.sleep function to sleep for nsecs seconds
    time.sleep(nsecs)

    print("Process %s waking up" % current_process().pid)

    return nsecs

if __name__ == "__main__":
    print("Master process is PID %s" % current_process().pid)

    with Pool() as pool:
        r = pool.apply(slow_function, [5])

    print("Result is %s" % r)


# In[10]:


get_ipython().system('python poolapply.py')


# # Asynchronous

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - A major problem of Pool.apply is that the master process is blocked until the worker has finished processing the applied function.
# - **apply_async()** is an asynchronous version of apply that applies the function in a worker process, but without blocking the master.
# - Let's create a new script called **applyasync.py** and copy into it
# 
# <br></font>
# </div>

# In[ ]:


import time
from multiprocessing import Pool, current_process

def slow_add(nsecs, x, y):
    """
    Function that sleeps for 'nsecs' seconds, and
    then returns the sum of x and y
    """
    print("Process %s going to sleep for %s second(s)" % (current_process().pid,nsecs))

    time.sleep(nsecs)

    print("Process %s waking up" % current_process().pid)

    return x + y

if __name__ == "__main__":
    print("Master process is PID %s" % current_process().pid)

    with Pool() as pool:
        """
        The apply_async function is identical to apply, except that it returns control 
        to the master process immediately. This means that the master process is free to
        continue working (e.g. here, it apply_asyncs a second slow_add function). In this
        case, it allows us to run two slow_sums in parallel. 
        """
        r1 = pool.apply_async(slow_add, [1, 6, 7])
        r2 = pool.apply_async(slow_add, [1, 2, 3])

        """
        The master process is then blocked using wait() to wait 
        for the result of the first and the second call
        """
        r1.wait()
        print("Result one is %s" % r1.get())

        r2.wait()
        print("Result two is %s" % r2.get())


# In[12]:


get_ipython().system('ls')


# In[14]:


# Remember we cannot run it directly from ipython but have to run it directly in the cmd line
get_ipython().system('python applyasync.py')


# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - An issue with running a function asynchronously is that the return value of the function **is not** available immediately. 
# - This means that, when running an asynchronous function, you don't get the return value directly. 
# - Instead, apply_async returns a placeholder for the return value. 
# - This placeholder is called a **future**, and is a variable that in the future will be given the result of the function.
# - We can explore this more using the script **future.py**
# 
# <br></font>
# </div>

# In[ ]:


import time
from multiprocessing import Pool

def slow_add(nsecs, x, y):
    """
    Function that sleeps for 'nsecs' seconds, and
    then returns the sum of x and y
    """
    time.sleep(nsecs)
    return x + y

def slow_diff(nsecs, x, y):
    """
    Function that sleeps for 'nsecs' seconds, and
    then retruns the difference of x and y
    """
    time.sleep(nsecs)
    return x - y

def broken_function(nsecs):
    """Function that deliberately raises an AssertationError"""
    time.sleep(nsecs)
    raise ValueError("Called broken function")

if __name__ == "__main__":
    futures = []

    with Pool() as pool:
        futures.append(pool.apply_async(slow_add, [3, 6, 7]))
        futures.append(pool.apply_async(slow_diff, [2, 5, 2]))
        futures.append(pool.apply_async(slow_add, [1, 8, 1]))
        futures.append(pool.apply_async(slow_diff, [5, 9, 2]))
        futures.append(pool.apply_async(broken_function, [4]))

        while True:
            all_finished = True

            print("\nHave the workers finished?")

            for i, future in enumerate(futures):
                if future.ready():
                    print("Process %s has finished" % i)
                else:
                    all_finished = False
                    print("Process %s is running..." % i)

            if all_finished:
                break

            time.sleep(1)

        print("\nHere are the results.")

        for i, future in enumerate(futures):
            if future.successful():
                print("Process %s was successful. Result is %s" % (i, future.get()))
            else:
                print("Process %s failed!" % i)

                try:
                    future.get()
                except Exception as e:
                    print("    Error = %s : %s" % (type(e), e))


# In[15]:


get_ipython().system('ls')


# In[19]:


get_ipython().system('python future.py')


# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - Note that the exception raised by broken_function is held safely in its associated future. 
# - This is indicated by .successful() returning False, thereby allowing us to handle the exception in a try...except block that is put around the .get() function (if you .get() a future that contains an exception, then that exception is raised).
# 
# <br></font>
# </div>

# # Asynchronous Mapping

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - Asynchronous functions allow you to give different tasks to different members of the multiprocessing.Pool. 
# - However, giving functions one by one is not very efficient. 
# - It would be good to be able to combine mapping with asynchronous functions, i.e. be able to give different mapping tasks simultanously to the pool of workers. 
# - Fortunately, Pool.map_async provides exactly that - an asynchronous parallel map.
# - Let's crete a script called **asyncmap.py**
# 
# <br></font>
# </div>

# In[ ]:


from functools import reduce
from multiprocessing import Pool, current_process
import time

def add(x, y):
    """Return the sum of the arguments"""
    print("Worker %s is processing add(%s, %s)" % (current_process().pid, x, y))
    time.sleep(1)
    return x + y

def product(x, y):
    """Return the product of the arguments"""
    print("Worker %s is processing product(%s, %s)" % (current_process().pid, x, y))
    time.sleep(1)
    return x * y

if __name__ == "__main__":

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    # Now create a Pool of workers
    with Pool() as pool:
        sum_future = pool.starmap_async(add, zip(a,b), chunksize = 5)
        product_future = pool.starmap_async(product, zip(a,b))

        sum_future.wait()
        product_future.wait()

    total_sum = reduce(lambda x, y: x + y, sum_future.get())
    total_product = reduce(lambda x, y: x + y, product_future.get())

    print("Sum of sums of 'a' and 'b' is %s" % total_sum)
    print("Sum of products of 'a' and 'b' is %s" % total_product)


# In[23]:


get_ipython().system('ls')


# In[25]:


get_ipython().system('python asyncmap.py')


# # Chunking

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - Giving work one by one can be very inefficient for quick tasks, as the time needed by a worker process to stop and get new work can be longer than it takes to actually complete the task. 
# - To solve this problem, you can control how many work items are handed out to each worker process at a time. 
# - This is known as chunking, and the number of work items is known as the chunk of work to perform.
# - **ATTENTION**: using chunksize would suggest to pool that each worker be given a chunk of five pieces of work. Note that this is just a suggestion, and pool may decide to use a slightly smaller or larger chunk size depending on the amount of work and the number of workers available.
# 
# <br></font>
# </div>

# # Conclusion

# <div class="alert alert-block alert-danger">
# <font color=black><br>
# 
# - TBC
# 
# <br></font>
# </div>

# # References

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://github.com/chryswoods/siremol.org/blob/master/chryswoods.com/parallel_python/multiprocessing.md<br>
# 
# </font>
# </div>

# In[ ]:




