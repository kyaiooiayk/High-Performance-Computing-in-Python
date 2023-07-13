#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-vectorisation?" data-toc-modified-id="What-is-vectorisation?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is vectorisation?</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Example" data-toc-modified-id="Example-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Vectorisation
# 
# </font>
# </div>

# # What is vectorisation?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
#  
# - Python is not the fastest programming language. So when you need to process a large amount of homogeneous data quickly, you’re told to rely on **vectorization**.
# 
# - Let’s say we have a few million numbers in a list or array, and we want to do some mathematical operations on them. Since we know they are all numbers, and if we’re doing the same operation on all of the numbers, we can **vectorise** the operation, i.e. take advantage of this **homogeneity** of data and operation.
#     
# - In python this means that a batch operation implemented in a fast language: say C.
#     
# - Vectorization is used to speed up the Python code without using loop. 
#  
# - Recall that NumPy’s ND-arrays are **homogeneous**. this measn that an array can only contain data of a single type. For instance, an array can contain 8-bit integers or 32-bit floating point numbers, but not a mix of the two. This is in stark contrast to Python’s lists and tuples, which are entirely unrestricted in the variety of contents they can possess; a given list could simultaneously contain strings, integers, and other objects. 
# 
# - This restriction on an array’s contents comes at a great benefit; in “knowing” that an array’s contents are homogeneous in data type, NumPy is able to delegate the task of performing mathematical operations on the array’s contents to optimized, compiled C code. This is a process that is referred to as **vectorization**. 
#     
# - The outcome of this can be a tremendous speedup relative to the analogous computation performed in Python, which **must painstakingly check** the data type of every one of the items as it iterates over the arrays, since Python typically works with lists with unrestricted contents.
# 
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[1]:


from contextlib import contextmanager
from subprocess import Popen
from os import getpid
from signal import SIGINT
from time import sleep, time
from resource import getrusage, RUSAGE_SELF


# # Example
# <hr style = "border:2px solid black" ></hr>

# In[2]:


events = [
    "instructions",
    "cache-references",
    "cache-misses",
    "avx_insts.all",
]


@contextmanager
def perf():
    """Benchmark this process with Linux's perf util.

    Example usage:

        with perf():
            x = run_some_code()
            more_code(x)
            all_this_code_will_be_measured()
    """
    p = Popen([
        # Run perf stat
        "perf", "stat",
        # for the current Python process
        "-p", str(getpid()),
        # record the list of events mentioned above
        "-e", ",".join(events)])
    # Ensure perf has started before running more
    # Python code. This will add ~0.1 to the elapsed
    # time reported by perf, so we also track elapsed
    # time separately.
    sleep(0.1)
    start = time()
    try:
        yield
    finally:
        print(f"Elapsed (seconds): {time() - start}")
        print("Peak memory (MiB):",
              int(getrusage(RUSAGE_SELF).ru_maxrss / 1024))
        p.send_signal(SIGINT)


# In[3]:


from random import random
DATA = [random() for _ in range(30_000_000)]


# In[4]:


with perf():    
    mean = sum(DATA) / len(DATA)
    result = [DATA[i] - mean for i in range(len(DATA))]


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://pythonspeed.com/articles/vectorization-python/
# - https://www.geeksforgeeks.org/vectorization-in-python/
# - https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/VectorizedOperations.html
# 
# </font>
# </div>

# In[ ]:




