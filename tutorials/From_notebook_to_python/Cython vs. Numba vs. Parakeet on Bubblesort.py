#!/usr/bin/env python
# coding: utf-8

# # Cython vs. Numba vs. Parakeet on Bubblesort

# A long story short: The "worst-case" complexity of the Bubblesort algorithm (i.e., "Big-O")  $\Rightarrow \pmb O(n^2)$

# ## Bubble sort implemented in (C)Python

# In[1]:


def python_bubblesort(a_list):
    """ Bubblesort in Python for list objects. """
    length = len(a_list)
    swapped = 1
    for i in xrange(0, length):
        if swapped: 
            swapped = 0
            for ele in xrange(0, length-i-1):
                if a_list[ele] > a_list[ele + 1]:
                    temp = a_list[ele + 1]
                    a_list[ele + 1] = a_list[ele]
                    a_list[ele] = temp
                    swapped = 1
    return a_list


# In[2]:


def python_bubblesort_ary(np_ary):
    """ Bubblesort in Python for NumPy arrays. """
    length = np_ary.shape[0]
    swapped = 1
    for i in xrange(0, length):
        if swapped: 
            swapped = 0
            for ele in xrange(0, length-i-1):
                if np_ary[ele] > np_ary[ele + 1]:
                    temp = np_ary[ele + 1]
                    np_ary[ele + 1] = np_ary[ele]
                    np_ary[ele] = temp
                    swapped = 1
    return np_ary


# ### Bubble sort implemented in Cython

# Maybe we can speed things up a little bit via [Cython's C-extensions for Python](http://cython.org). Cython is basically a hybrid between C and Python and can be pictured as compiled Python code with type declarations.  
# Since we are working in an IPython notebook here, we can make use of the very convenient *IPython magic*: It will take care of the conversion to C code, the compilation, and eventually the loading of the function.  
# 
# Note that the static type declarations that we add via `cdef` are note required for Cython to work, but it will speed things up tremendously.

# In[3]:


get_ipython().run_line_magic('load_ext', 'cythonmagic')


# In[4]:


get_ipython().run_cell_magic('cython', '', 'import numpy as np\ncimport numpy as np\ncimport cython\n@cython.boundscheck(False) \n@cython.wraparound(False)\ncpdef cython_bubblesort(inp_ary):\n    """ The Cython implementation of Bubblesort with NumPy memoryview."""\n    cdef unsigned long length, i, swapped, ele, temp\n    cdef long[:] np_ary = inp_ary\n    length = np_ary.shape[0]\n    swapped = 1\n    for i in xrange(0, length):\n        if swapped: \n            swapped = 0\n            for ele in xrange(0, length-i-1):\n                if np_ary[ele] > np_ary[ele + 1]:\n                    temp = np_ary[ele + 1]\n                    np_ary[ele + 1] = np_ary[ele]\n                    np_ary[ele] = temp\n                    swapped = 1\n    return inp_ary\n')


# ### Bubble sort implemented in Numba

# Numba is using the [LLVM compiler infrastructure](http://llvm.org) for compiling Python code to machine code. Its strength is to work with NumPy arrays to speed-up the code. If you want to read more about Numba, please see refer to the original [website and documentation](http://numba.pydata.org/numba-doc/0.13/index.html).

# In[5]:


from numba import jit as numba_jit
@numba_jit
def numba_bubblesort(np_ary):
    """ The NumPy implementation of Bubblesort on NumPy arrays."""
    length = np_ary.shape[0]
    swapped = 1
    for i in xrange(0, length):
        if swapped: 
            swapped = 0
            for ele in xrange(0, length-i-1):
                if np_ary[ele] > np_ary[ele + 1]:
                    temp = np_ary[ele + 1]
                    np_ary[ele + 1] = np_ary[ele]
                    np_ary[ele] = temp
                    swapped = 1
    return np_ary


# ### Bubble sort implemented in  parakeet

# Similar to Numba,  [parakeet](http://www.parakeetpython.com) is a Python compiler that optimizes the runtime of numerical computations based on the NumPy data types, such as NumPy arrays.
# 
# The usage is also similar to Numba where we just have to put the `jit` decorator on top of the function we want to optimize.

# In[6]:


from parakeet import jit as para_jit
@para_jit
def parakeet_bubblesort(np_ary):
    """ The parakeet implementation of Bubblesort on NumPy arrays."""
    length = np_ary.shape[0]
    swapped = 1
    for i in xrange(0, length):
        if swapped: 
            swapped = 0
            for ele in xrange(0, length-i-1):
                if np_ary[ele] > np_ary[ele + 1]:
                    temp = np_ary[ele + 1]
                    np_ary[ele + 1] = np_ary[ele]
                    np_ary[ele] = temp
                    swapped = 1
    return np_ary


# ## Verifying that all implementations work correctly

# In[7]:


import random
import copy
import numpy as np
random.seed(4354353)

l = np.asarray([random.randint(1,1000) for num in xrange(1, 1000)])
l_sorted = np.sort(l)
for f in [python_bubblesort, python_bubblesort_ary, cython_bubblesort, 
          numba_bubblesort, parakeet_bubblesort]:
    assert(l_sorted.all() == f(copy.copy(l)).all())
print('Bubblesort works correctly')


# ## Timing

# In[8]:


import timeit
import copy
import numpy as np

funcs = ['python_bubblesort',
         'python_bubblesort_ary',
         'cython_bubblesort',
         'numba_bubblesort',
         'parakeet_bubblesort'
         ]

orders_n = [10**n for n in range(1, 6)]
timings = {f:[] for f in funcs}

for n in orders_n:
    l = [np.random.randint(n) for num in range(n)]
    for f in funcs:
        l_copy = copy.deepcopy(l)
        if f != 'python_bubblesort':
            l_copy = np.asarray(l_copy)
        timings[f].append(min(timeit.Timer('%s(l_copy)' %f, 
                      'from __main__ import %s, l_copy' %f)
                              .repeat(repeat=3, number=10)))


# ### Setting up the plots

# In[13]:


import platform
import multiprocessing
from cython import __version__ as cython__version__
from llvm import __version__ as llvm__version__
from numba import __version__ as numba__version__
from parakeet import __version__ as parakeet__version__

def print_sysinfo():
    
    print '\nPython version  :', platform.python_version()
    print 'compiler        :', platform.python_compiler()
    print 'Cython version  :', cython__version__
    print 'NumPy version   :', np.__version__
    print 'Numba version   :', numba__version__
    print 'llvm version    :', llvm__version__
    print 'parakeet version:', parakeet__version__
    
    print '\nsystem     :', platform.system()
    print 'release    :', platform.release()
    print 'machine    :', platform.machine()
    print 'processor  :', platform.processor()
    print 'CPU count  :', multiprocessing.cpu_count()
    print 'interpreter:', platform.architecture()[0]
    print '\n\n'


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


import matplotlib.pyplot as plt

def plot(timings, title, ranked_labels, labels, orders_n):
    plt.rcParams.update({'font.size': 12})

    fig = plt.figure(figsize=(11,10))
    for lb in ranked_labels:
        plt.plot(orders_n, timings[lb], alpha=0.5, label=labels[lb], 
                 marker='o', lw=3)
    plt.xlabel('sample size n (items in the list)')
    plt.ylabel('time per computation in milliseconds')
    plt.xlim([min(orders_n) / 10, max(orders_n)* 10])
    plt.legend(loc=2)
    plt.grid()
    plt.xscale('log')
    plt.yscale('log')
    plt.title(title)
    plt.show()


# In[16]:


import prettytable

def summary_table(ranked_labels):
    fit_table = prettytable.PrettyTable(['n=%s' %orders_n[-1], 
                                         'bubblesort function' ,
                                         'time in millisec.',
                                         'rel. performance gain'])
    fit_table.align['bubblesort function'] = 'l'
    for entry in ranked_labels:
        fit_table.add_row(['', labels[entry[1]], round(entry[0]*100, 3), 
                           round(ranked_labels[0][0]/entry[0], 2)])
        # times 100 for converting from seconds to milliseconds: (time*1000 / 10-loops)
    print(fit_table)


# ## Results

# In[17]:


title = 'Performance of Bubblesort in Python, Cython, parakeet, and Numba'

labels = {'python_bubblesort':'(C)Python Bubblesort - Python lists', 
          'python_bubblesort_ary':'(C)Python Bubblesort - NumPy arrays',  
          'cython_bubblesort': 'Cython Bubblesort - NumPy arrays',
          'numba_bubblesort': 'Numba Bubblesort - NumPy arrays',
          'parakeet_bubblesort': 'parakeet Bubblesort - NumPy arrays'
          }

ranked_by_time = sorted([(time[1][-1],time[0]) for time in timings.items()], reverse=True)

print_sysinfo()
plot(timings, title, [l for t,l in ranked_by_time], labels, orders_n)
summary_table(ranked_by_time)


# Note that the relative results also depend on what version of Python, Cython, Numba, parakeet, and NumPy you are using. Also, the compiler choice for installing NumPy can account for differences in the results.  

# # References

# - https://nbviewer.org/github/rasbt/One-Python-benchmark-per-day/blob/master/ipython_nbs/day4_2_cython_numba_parakeet.ipynb

# <br>
# <br>
