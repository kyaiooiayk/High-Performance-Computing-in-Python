#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Options-to-speed-up-the-computation" data-toc-modified-id="Options-to-speed-up-the-computation-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Options to speed-up the computation</a></span></li><li><span><a href="#Python" data-toc-modified-id="Python-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Python</a></span></li><li><span><a href="#NumPy" data-toc-modified-id="NumPy-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>NumPy</a></span></li><li><span><a href="#Numba" data-toc-modified-id="Numba-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Numba</a></span></li><li><span><a href="#Cython" data-toc-modified-id="Cython-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Cython</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** NumPy vs. Numba vs. Cython
# 
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[1]:


import random
import numpy as np
import numba


# # Options to speed-up the computation
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Vectorisation via `NumPy` which makes use of Python’s vectorization capabilities to improve excecution time.
# - Dynamic compiling via `Numba` which allows to dynamically compile pure Python code using LLVM technology.
# - Static compiling via `Cython` which is a hybrid language that combines Python and C; it allows one, for instance, to use static type declarations and to statically compile such adjusted code.
# - Multiprocessing and hypertrading is not considered here because this is just a different way to run the code optimised in one of the three ways just descibed.
# 
# </font>
# </div>

# # Python
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Let's write a simple algortihm that computs the average of some random numbers.
# - This is done in pure python, which will then set the standard.
# 
# </font>
# </div>

# In[3]:


def average_py(n):
    s = 0  
    for i in range(n):
        s += random.random()  
    return s / n  


# In[4]:


n = 10000000  


# In[5]:


# Time it once
get_ipython().run_line_magic('time', 'average_py(n)')


# In[6]:


# Time it several times for a more realibale estimate
get_ipython().run_line_magic('timeit', 'average_py(n)')


# In[7]:


# Uses a list comprehension instead of the function.
get_ipython().run_line_magic('time', 'sum([random.random() for _ in range(n)]) / n')


# # NumPy 
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - The strength of NumPy lies in its vectorization capabilities.
# - The looping takes place one level deeper based on optimized and compiled routines provided by `NumPy`.
# 
# </font>
# </div>

# In[8]:


def average_np(n):
    s = np.random.random(n)
    return s.mean()


# In[9]:


get_ipython().run_line_magic('time', 'average_np(n)')


# In[10]:


get_ipython().run_line_magic('timeit', 'average_np(n)')


# In[11]:


# How much data did we actually used?
s = np.random.random(n)
s.nbytes  


# <div class="alert alert-info">
# <font color=black>
# 
# - **Where is the catch??** Keep an eye on the memory (RAM)!
# - The price you paid (which does not mean it is bad!) for the speedup is a significantly higher memory usage.
# - This is due to the fact that NumPy attains speed by preallocating data that can be processed in the compiled layer. 
# - As a consquence, there is no way, given this approach, to work with **streamed data**. This increased memory usage might even be prohibitively large depending on the algorithm or problem at hand.
# 
# </font>
# </div>

# # Numba
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Numba is a package that allows the dynamic compiling of pure Python code by the use of LLVM. 
# - The combination of pure Python with Numba beats the NumPy version **and preserves** the memory efficiency of the original loop-based implementation. 
# - It is also obvious that the application of Numba in such simple cases comes with hardly any program‐ ming overhead.
# - One issue is that it can be highly **memory-intensive**. This is because vectorization tends to create many intermediate arrays before producing the final calculation. Another issue is that not all algorithms can be vectorized. In these kinds of settings, we need to go back to loops. Fortunately, there are alternative ways to speed up Python loops that work in almost any setting. For example, in the last few years, a new Python library called Numba has appeared that **solves** the main problems with vectorization listed above.
#     
# </font>
# </div>

# In[12]:


average_nb = numba.jit(average_py)  


# In[13]:


get_ipython().run_line_magic('time', 'average_nb(n)')


# In[14]:


# The compiling happens during runtime, leading to some overhead.
get_ipython().run_line_magic('time', 'average_nb(n)')


# In[15]:


# From the second execution (with the same input data types), the execution is faster.
get_ipython().run_line_magic('timeit', 'average_nb(n)')


# <div class="alert alert-info">
# <font color=black>
# 
# - **Where is the catch?** No Free Lunch
# - The application of Numba sometimes seems like magic when one compares the performance of the Python code to the compiled version, especially given its ease of use. 
# - However, there are many use cases for which Numba is not suited and for which performance gains are hardly observed or even impossible to achieve.
# 
# </font>
# </div>

# # Cython
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `Cython` allows one to statically compile Python code. 
# - However, the application is not as simple as with Numba since the code generally needs to be changed to see significant speed improvements.
# - The code needs to be done several times as it will be shown down below.
#     
# </font>
# </div>

# In[16]:


get_ipython().run_line_magic('load_ext', 'Cython')


# In[17]:


get_ipython().run_cell_magic('cython', '-a', 'import random  \ndef average_cy1(int n):  \n    """\n    Adds static type declarations for the variables n, i, and s.\n    """\n    cdef int i  \n    cdef float s = 0  \n    for i in range(n):\n        s += random.random()\n    return s / n\n')


# In[18]:


get_ipython().run_line_magic('time', 'average_cy1(n)')


# In[19]:


get_ipython().run_line_magic('timeit', 'average_cy1(n)')


# <div class="alert alert-info">
# <font color=black>
# 
# - Some speedup is observed, but not even close to that achieved by, for example, the NumPy version. 
# - A bit more Cython optimization is necessary to beat even the Numba version:
# - This further optimized Cython version, `average_cy2`, is now a bit faster than the Numba version. However, the effort has also been a bit larger. Compared to the NumPy version, Cython also preserves the memory efficiency of the original loop-based implementation.
# 
# </font>
# </div>

# In[20]:


get_ipython().run_cell_magic('cython', '', "\n#Imports a random number generator from C.\nfrom libc.stdlib cimport rand  \n\n# Imports a constant value for the scaling of the random numbers.\ncdef extern from 'limits.h':  \n    int INT_MAX  \ncdef int i\ncdef float rn\nfor i in range(5):\n    # Adds uniformly distributed random numbers from the interval (0, 1), after scal‐ ing\n    rn = rand() / INT_MAX  \n    print(rn)\n")


# In[21]:


get_ipython().run_cell_magic('cython', '-a', "# Imports a random number generator from C.\nfrom libc.stdlib cimport rand  \n\n# Imports a constant value for the scaling of the random numbers.\ncdef extern from 'limits.h':  \n    int INT_MAX  \ndef average_cy2(int n):\n    cdef int i\n    cdef float s = 0\n    for i in range(n):\n        # Adds uniformly distributed random numbers from the interval (0, 1), after scal‐ ing\n        s += rand() / INT_MAX  \n    return s / n\n")


# In[22]:


get_ipython().run_line_magic('time', 'average_cy2(n)')


# In[23]:


get_ipython().run_line_magic('timeit', 'average_cy2(n)')


# <div class="alert alert-info">
# <font color=black>
# 
# - **If there is much to add, why would developer use it?
# - Cython allows developers to tweak code for performance as much as possible or as little as sensible—starting with a pure Python version, for instance, and adding more and more elements from C to the code. 
# - Esentially the improvement **at will** is the the main selling point for `cython`.
# - The compilation step itself can also be parameterized to further optimize the compiled version.  
# 
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://github.com/yhilpisch/py4fi2nd/blob/master/code/ch10/10_performance_python.ipynb
# - https://llvm.org/
# - Hilpisch, Yves. Python for finance: mastering data-driven finance. O'Reilly Media, 2018.
# - https://github.com/QuantEcon/lecture-python-programming.notebooks/blob/master/need_for_speed.ipynb
#     
# </font>
# </div>

# In[ ]:




