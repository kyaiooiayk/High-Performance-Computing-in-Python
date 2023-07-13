#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Types-of-Parallelization" data-toc-modified-id="Types-of-Parallelization-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Types of Parallelization</a></span><ul class="toc-item"><li><span><a href="#Multiprocessing" data-toc-modified-id="Multiprocessing-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Multiprocessing</a></span></li><li><span><a href="#Multithreading" data-toc-modified-id="Multithreading-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Multithreading</a></span></li><li><span><a href="#Advantages-and-Disadvantages" data-toc-modified-id="Advantages-and-Disadvantages-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Advantages and Disadvantages</a></span></li></ul></li><li><span><a href="#Implicit-Multithreading-in-NumPy" data-toc-modified-id="Implicit-Multithreading-in-NumPy-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Implicit Multithreading in NumPy</a></span><ul class="toc-item"><li><span><a href="#A-Matrix-Operation" data-toc-modified-id="A-Matrix-Operation-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>A Matrix Operation</a></span></li><li><span><a href="#A-Comparison-with-Numba" data-toc-modified-id="A-Comparison-with-Numba-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>A Comparison with Numba</a></span></li><li><span><a href="#Multithreading-a-Numba-Ufunc" data-toc-modified-id="Multithreading-a-Numba-Ufunc-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Multithreading a Numba Ufunc</a></span></li></ul></li></ul></div>

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# ## Types of Parallelization
# 
# Large textbooks have been written on different approaches to parallelization but we will keep a tight focus on what’s most useful to us.
# 
# We will briefly review the two main kinds of parallelization commonly used in
# scientific computing and discuss their pros and cons.

# ### Multiprocessing
# 
# Multiprocessing means concurrent execution of multiple processes using more than one processor.
# 
# In this context, a **process** is a chain of instructions (i.e., a program).
# 
# Multiprocessing can be carried out on one machine with multiple CPUs or on a
# collection of machines connected by a network.
# 
# In the latter case, the collection of machines is usually called a
# **cluster**.
# 
# With multiprocessing, each process has its own memory space, although the
# physical memory chip might be shared.

# ### Multithreading
# 
# Multithreading is similar to multiprocessing, except that, during execution, the threads all share the same memory space.
# 
# Native Python struggles to implement multithreading due to some [legacy design
# features](https://wiki.python.org/moin/GlobalInterpreterLock).
# 
# But this is not a restriction for scientific libraries like NumPy and Numba.
# 
# Functions imported from these libraries and JIT-compiled code run in low level
# execution environments where Python’s legacy restrictions don’t apply.

# ### Advantages and Disadvantages
# 
# Multithreading is more lightweight because most system and memory resources
# are shared by the threads.
# 
# In addition, the fact that multiple threads all access a shared pool of memory
# is extremely convenient for numerical programming.
# 
# On the other hand, multiprocessing is more flexible and can be distributed
# across clusters.
# 
# For the great majority of what we do in these lectures, multithreading will
# suffice.

# ## Implicit Multithreading in NumPy
# 
# Actually, you have already been using multithreading in your Python code,
# although you might not have realized it.
# 
# (We are, as usual, assuming that you are running the latest version of
# Anaconda Python.)
# 
# This is because NumPy cleverly implements multithreading in a lot of its
# compiled code.
# 
# Let’s look at some examples to see this in action.

# ### A Matrix Operation
# 
# - The next piece of code computes the eigenvalues of a large number of randomly
# generated matrices.
# - It takes a few seconds to run.
# - you can check this by typing `htop`

# In[2]:


n = 20
m = 1000
for i in range(n):
    X = np.random.randn(m, m)
    λ = np.linalg.eigvals(X)


# This is because NumPy’s `eigvals` routine neatly splits up the tasks and
# distributes them to different threads.

# ### A Comparison with Numba
# 
# To get some basis for comparison for the last example, let’s try the same
# thing with Numba.
# 
# In fact there is an easy way to do this, since Numba can also be used to
# create custom [ufuncs](https://python-programming.quantecon.org/need_for_speed.html#ufuncs) with the [@vectorize](http://numba.pydata.org/numba-doc/dev/user/vectorize.html) decorator.

# In[3]:


from numba import vectorize

@vectorize
def f_vec(x, y):
    return np.cos(x**2 + y**2) / (1 + x**2 + y**2)

grid = np.linspace(-3,3,5000)
x,y = np.meshgrid(grid, grid)
np.max(f_vec(x, y))  # Run once to compile


# In[4]:


get_ipython().run_line_magic('timeit', 'np.max(f_vec(x, y))')


# At least on our machine, the difference in the speed between the
# Numba version and the vectorized NumPy version shown above is not large.
# 
# But there’s quite a bit going on here so let’s try to break down what is
# happening.
# 
# Both Numba and NumPy use efficient machine code that’s specialized to these
# floating point operations.
# 
# However, the code NumPy uses is, in some ways, less efficient.
# 
# The reason is that, in NumPy, the operation `np.cos(x**2 + y**2) / (1 + x**2 + y**2)` generates several intermediate arrays.
# 
# For example, a new array is created when `x**2` is calculated.
# 
# The same is true when `y**2` is calculated, and then `x**2 + y**2` and so on.
# 
# Numba avoids creating all these intermediate arrays by compiling one
# function that is specialized to the entire operation.
# 
# But if this is true, then why isn’t the Numba code faster?
# 
# The reason is that NumPy makes up for its disadvantages with implicit
# multithreading, as we’ve just discussed.

# ### Multithreading a Numba Ufunc
# 
# Can we get both of these advantages at once?
# 
# In other words, can we pair
# 
# - the efficiency of Numba’s highly specialized JIT compiled function and  
# - the speed gains from parallelization obtained by NumPy’s implicit
#   multithreading?  
# 
# 
# It turns out that we can, by adding some type information plus `target='parallel'`.

# In[5]:


@vectorize('float64(float64, float64)', target='parallel')
def f_vec(x, y):
    return np.cos(x**2 + y**2) / (1 + x**2 + y**2)

np.max(f_vec(x, y))  # Run once to compile


# In[6]:


get_ipython().run_line_magic('timeit', 'np.max(f_vec(x, y))')


# Now our code runs significantly faster than the NumPy version.

# - https://github.com/QuantEcon/lecture-python-programming.notebooks/blob/master/parallelization.ipynb

# In[ ]:




