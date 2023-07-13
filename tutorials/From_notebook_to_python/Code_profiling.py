#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Timing-your-code" data-toc-modified-id="Timing-your-code-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Timing your code</a></span></li><li><span><a href="#Profile-your-code" data-toc-modified-id="Profile-your-code-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Profile your code</a></span></li></ul></div>

# # Introduction

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Code profiling
#
# </font>
# </div>

# # Timing your code
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - `%timeit`: times only the line and runs the line it many times and gives more statistics.
# - `%%timeit`: times the whole cell and runs the it many times and gives more statistics.
#
#
# - `%time` and `%%time` times it but extecuted it only **once**.
#
# </font>
# </div>

# In[1]:


get_ipython().run_cell_magic("timeit", "-n1000", "l = [k for k in range(10**2)]\n")


# In[2]:


get_ipython().run_line_magic("timeit", "-n1000 l = [k for k in range(10**2)]")

get_ipython().run_line_magic("timeit", "-n10 l = [k for k in range(10**2)]")


# In[3]:


# This would not work!
get_ipython().run_line_magic("timeit", "-n1000")
l = [k for k in range(10**2)]


# In[4]:


get_ipython().run_line_magic("time", "l = [k for k in range(10**2)]")


# In[5]:


# Saving the output
o = get_ipython().run_line_magic("timeit", "-o l = [k for k in range(10**2)]")


# In[6]:


print(o)


# <div class="alert alert-info">
# <font color=black>
#
# - Setting the number of runs `-r` and/or loops `-n`
#
# </font>
# </div>

# In[3]:


# Set number of runs to 2 (-r2)
# Set number of loops to 10 (-n10)
import numpy as np

get_ipython().run_line_magic("timeit", "-r2 -n10 rand_nums = np.random.rand(1000)")


# In[11]:


times = get_ipython().run_line_magic(
    "timeit", "-r10 -n10 -o rand_nums = np.random.rand(1000)"
)


# In[12]:


times.timings


# In[13]:


print(times.best)
print(times.worst)


# # Profile your code
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - `%prun`  = Run code with the profiler
# - `%lprun` = Run code with the line-by-line profiler
# - `%memit` = Measure the memory use of a single statement
# - `%mprun` = Run code with the line-by-line memory profiler
#
# </font>
# </div>

# In[7]:


import sys

get_ipython().run_line_magic("load_ext", "line_profiler")
get_ipython().run_line_magic("load_ext", "memory_profiler")


# In[8]:


def sum_of_lists(N):
    total = 0
    for i in range(5):
        L = [j ^ (j >> i) for j in range(N)]
        total += sum(L)
    return total


# In[9]:


# to access the output on the output cell rather than a popup window
# https://github.com/ipython/ipython/issues/2091/
p = get_ipython().run_line_magic("prun", "- r sum_of_lists(1000000)")
p.stream = sys.stdout
p.print_stats()


# In[10]:


p = get_ipython().run_line_magic("lprun", "- rf sum_of_lists sum_of_lists(5000)")
p.stream = sys.stdout
p.print_stats()


# In[11]:


p = get_ipython().run_line_magic("memit", "sum_of_lists(5000)")


# <div class="alert alert-info">
# <font color=black>
#
# - To be able to use `mprun` magic command, we have to store the function locally.
# - This is done automatically my writing `%%file sum_of_lists.py` which saves a local file
# called `file sum_of_lists.py`
#
# </font>
# </div>

# In[21]:


get_ipython().system("ls")


# In[28]:


"""
# This command -> %%file will write a local file on disk
"""


# In[29]:


get_ipython().run_cell_magic(
    "file",
    "sum_of_lists.py",
    "def sum_of_lists(N): \n    total = 0\n    for i in range(5): \n            L=[j^(j>>i) for j in range(N)] \n            total += sum(L)\n    return total\n",
)


# In[30]:


# In[32]:


# You now have to import the function explcitly
from sum_of_lists import sum_of_lists

m = get_ipython().run_line_magic("mprun", "-rf sum_of_lists sum_of_lists(5000)")
m.stream = sys.stdout
m
# We'll delete the file as it is not needed!
get_ipython().system("rm sum_of_lists.py")


# In[16]:


"""
m does not have a print_stats()
so at the moment I do not know how I would pull that data!
"""
dir(m)


# In[ ]:
