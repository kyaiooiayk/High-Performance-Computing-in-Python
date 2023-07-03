#!/usr/bin/env python
# coding: utf-8

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black><br>
#
# **What?** Cython & Numba
#
# **Reference:** https://nbviewer.jupyter.org/github/ethen8181/machine-learning/blob/master/python/cython/cython.ipynb<br>
#
# <br></font>
# </div>

# # Import modules

# In[42]:


import numpy as np
from numba import jit, njit, prange


# In[8]:


get_ipython().run_line_magic("load_ext", "watermark")


# In[9]:


get_ipython().run_line_magic("watermark", "-p numpy,cython,numba")


# # Cython

# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - Cython is designed to give C-like performance with code written in Python
# - For Cython motivation see: https://www.youtube.com/watch?v=_1MSX7V28Po
# - Use **%load_ext cython** to use it in a notebook
#
# <br></font>
# </div>

# ## Option #1 - use it within this notebook

# In[ ]:


get_ipython().run_line_magic("load_ext", "cython")


# In[10]:


get_ipython().run_cell_magic(
    "cython",
    "",
    'def hello_snippet():\n    """\n    after loading the cython magic, we can\n    run the cython code (this code isn\'t \n    different from normal python code)\n    """\n    print(\'hello cython\')',
)


# In[12]:


hello_snippet()


# ## Option #2 - use a stand-alone python script

# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - Write two files: **helloworld.pyx** and **setup.py**
# - After that run **python setup.py build_ext --inplace**
# - The you can import it as **from helloworld import hello**
#
# <br></font>
# </div>

# In[ ]:


# This is the helloworld.pyx
# cython hello world
def hello():
    print("Hello, World!")


# In[ ]:


# This is the setup.py

# compiling the .pyx module
from distutils.core import setup
from Cython.Build import cythonize

# key-value pairs that tell disutils the name
# of the application and which extensions it
# needs to build, for the cython modules, we
# use glob patterns, e.g. *.pyx or simply pass in
# the filename.pyx
setup(
    name="Hello",
    ext_modules=cythonize("*.pyx"),
)


# ## Static typing

# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - Cython extends the Python language with static type declarations.
# - This increases speed by not needing to do type-checks when running the program.
# - The way we do this in Cython is by adding the **cdef** keyword
#
# <br></font>
# </div>

# In[24]:


get_ipython().run_cell_magic(
    "cython",
    "",
    '\ndef example_cython():\n    """simply increment j by 1 for 1000 times"""\n    # declare the integer type before using it\n    cdef int i, j = 0\n    for i in range(1000):\n        j += 1    \n    return j',
)


# In[25]:


def example_python():
    j = 0
    for i in range(1000):
        j += 1
    return j


# In[28]:


get_ipython().run_line_magic("timeit", "-n 10000 example_cython()")


# In[29]:


get_ipython().run_line_magic("timeit", "-n 10000 example_python()")


# ## Functions

# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - To declare functions we use the cpdef keyword.
# - We also specify the return type to be a integer and a two input argument to be integers.
# - There's still an overhead to calling functions, so if the function is small and is in a computationally expensive for loop, then we can add the **inline** keyword in the function declaration. By doing this, it will replace function call solely with the function body, thus reducing the time to call the function multiple times.
#
# <br></font>
# </div>

# In[36]:


get_ipython().run_cell_magic(
    "cython", "", "cpdef int compute_sum(int a, int b):\n    return a + b"
)


# In[37]:


get_ipython().run_line_magic("timeit", "-n 100000 compute_sum(5, 3)")


# In[38]:


get_ipython().run_cell_magic(
    "cython", "", "cpdef inline int compute_sum_mod(int a, int b):\n    return a + b"
)


# In[39]:


get_ipython().run_line_magic("timeit", "-n 100000 compute_sum_mod(5, 3)")


# ## Numpy & MemoryView

# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - Typed memoryviews allow even more efficient numpy manipulation since again
# - This is because it does not incur the python overhead
#
# <br></font>
# </div>

# In[41]:


get_ipython().run_cell_magic(
    "cython",
    "",
    "\nimport numpy as np\n\n# declare memoryviews by using : in the []\ncdef double[:, :] b = np.zeros((3, 3), dtype = 'float64')\nb[1] = 1\n\n# it now prints memoryview instead of original numpy array\nprint(b[0])",
)


# # Numba

# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - Numba is an LLVM compiler for python code, which allows code written in Python to be converted to highly efficient compiled code in real-time.
# - To use it, we simply add a **@jit** (just in time compilation) decorator to our function
# - The argument types will be inferred by Numba when function is called
# - If Numba can't infer the types, it **will fall back** to a python object
# - When this happens, we probably won't see any significant speed up
#
#
# <br></font>
# </div>

# In[97]:


@jit
def pairwise_numba1(X):
    M = X.shape[0]
    N = X.shape[1]
    D = np.zeros((M, M), dtype=np.float64)
    for i in range(M):
        for j in range(i + 1, M):
            d = 0.0
            for k in range(N):
                tmp = X[i, k] - X[j, k]
                d += tmp * tmp

            dist = np.sqrt(d)
            D[i, j] = dist
            D[j, i] = dist

    return D


# In[98]:


# a nice speedup from the raw python code given the
# little amount of effort that we had to put in
# (just adding the jit decorator)
get_ipython().run_line_magic("timeit", "-n 10 pairwise_numba1(X)")


# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - Numba has two compilation modes: nopython mode and object mode.
# - **nopython mode**: faster code but has limitations that force to fall back to object mode
# - To prevent Numba from falling back use 1) @jit(nopython = True) o2 2) @njit
# - To write parallel code by specifying the parallel = True argument to the decorator and changing range to prange to perform explicit parallel loops. Note that we must ensure the loop does not have cross iteration dependencies.
#
# <br></font>
# </div>

# In[100]:


X.shape


# In[102]:


@njit(parallel=True)
def pairwise_numba2(X):
    M = X.shape[0]
    N = X.shape[1]
    D = np.zeros((M, M), dtype=np.float64)
    # Note this is prange NOT the normal range
    for i in prange(M):
        for j in range(i + 1, M):
            d = 0.0
            for k in range(N):
                tmp = X[i, k] - X[j, k]
                d += tmp * tmp

            dist = np.sqrt(d)
            D[i, j] = dist
            D[j, i] = dist

    return D


# In[108]:


get_ipython().run_line_magic("timeit", "-n 100 pairwise_numba2(X)")


# # Conclusion

# <div class="alert alert-block alert-danger">
# <font color=black><br>
#
# - some conclusuion in **bold**
# -
#
# <br></font>
# </div>

# In[ ]:
