#!/usr/bin/env python
# coding: utf-8

# ## Speeding up NumPy array expressions with Numexpr

# [Numexpr](https://pypi.python.org/pypi/numexpr/2.4) is a "fast numerical expression evaluator for NumPy". It has a internal Virtual Machine to rewrite code more efficiently by breaking down operations into smaller chunks for the CPU cache. By using a JIT (just-in-time compiler), compilation at runtime is not necessary.
# 
# As listed in the [documentation](https://github.com/pydata/numexpr/blob/master/README.rst), it currently supports the following operators:
# 
# 
#     Logical operators: &, |, ~
#     Comparison operators: <, <=, ==, !=, >=, >
#     Unary arithmetic operators: -
#     Binary arithmetic operators: +, -, *, /, **, %, <<, >>
# 
# The usage is quite simple, we just have to provide the numerical expression that we want to evaluate as a string to the `evaluate` function, e.g., 
# 
#     import numexpr
#     import numpy
#     a = numpy.array([[1, 2]])
#     numexpr.evaluate('a ** 2')
#     >> array([[1, 4]], dtype=int64)

# # Import modules

# In[2]:


import numpy as np
from numexpr import evaluate


# <br>
# <br>

# ## NumPy functions

# In[3]:


def numpy_modulus(A, B):
    return A % B

def numpy_difference(A, B):
    return A - B

def numpy_multiplication(A, B):
    return A * B

def numpy_division(A, B):
    return A / B

def numpy_power(A, B):
    return A ** B

def numpy_squareroot(A, B=None):
    return np.sqrt(A)

def numpy_sum(A, B=None):
    return np.sum(A)

def numpy_log(A, B=None):
    return np.log(A)

def numpy_logic_operator(A, B):
    return A < B

def numpy_complex_expr(A, B):
    return(A*B-4.1*A > 2.5*B)


# <br>
# <br>

# ## Numexpr equivalents

# In[4]:


def numexpr_modulus(A, B):
    return evaluate('A % B')

def numexpr_difference(A, B):
    return evaluate('A - B')

def numexpr_multiplication(A, B):
    return evaluate('A * B')

def numexpr_division(A, B):
    return evaluate('A / B')

def numexpr_power(A, B):
    return evaluate('A ** B')

def numexpr_squareroot(A, B=None):
    return evaluate('sqrt(A)')

def numexpr_sum(A, B=None):
    return evaluate('sum(A)')

def numexpr_log(A, B=None):
    return evaluate('log(A)')

def numexpr_logic_operator(A, B):
    return evaluate('A < B')

def numexpr_complex_expr(A, B):
    return evaluate('A*B-4.1*A > 2.5*B')


# <br>
# <br>

# # Timing

# In[6]:


import timeit

orders_n = [10**n for n in range(1, 5)]

funcs = ['modulus', 'difference', 'multiplication', 
         'division', 'power', 'log', 'sum', 'squareroot',
         'logic_operator', 'complex_expr']

timings_np = {f:[] for f in funcs}
timings_ne = {f:[] for f in funcs}

for n in orders_n:
    for f in funcs:
        A = np.random.rand(n,n)
        B = np.random.rand(n,n)
        timings_np[f].append(min(timeit.Timer('numpy_%s(A, B)' %f, 
                      'from __main__ import A, B, numpy_%s' %f)
                              .repeat(repeat=3, number=1)))
        timings_ne[f].append(min(timeit.Timer('numexpr_%s(A, B)' %f, 
                      'from __main__ import A, B, numexpr_%s' %f)
                              .repeat(repeat=3, number=1)))


# <br>
# <br>

# ## Setting up plots

# In[17]:


import platform
import datetime
import numexpr
import multiprocessing


def print_sysinfo():
    print('\ndate:    :', str(datetime.date.today()))
    print('\nsystem   :', platform.system())
    print('release  :', platform.release())
    print('machine  :', platform.machine())
    print('processor:', platform.processor())
    print('CPU count  :', multiprocessing.cpu_count())
    print('interpreter:', platform.architecture()[0])

    print('\nPython version', platform.python_version())
    print('compiler', platform.python_compiler())
    print('NumPy version', np.__version__)
    print('Numexpr version', numexpr.__version__)
    print('\n\n')


# In[18]:


import prettytable

def summary_table(funcs):
    fit_table = prettytable.PrettyTable(['n=%s' %orders_n[-1], 
                                         'Numexpr function' ,
                                         'rel. performance gain via Numexpr'])
    fit_table.align['Numexpr function'] = 'l'
    for f in funcs:
        fit_table.add_row(['', f, '{:.2f}x'.format(timings_np[f][-1]/timings_ne[f][-1])])
    print(fit_table)


# In[19]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[22]:


import matplotlib.pyplot as plt

def plot_figures(funcs): 
    fig = plt.figure(figsize=(12,20))
    for i,f in enumerate(funcs):
        plt.subplot(len(funcs)/2, 2, i)
        plt.plot([i**2 for i in orders_n], [i*100 for i in timings_np[f]], 
                            alpha=0.5, label='NumPy %s' %f, marker='o')
        plt.plot([i**2 for i in orders_n], [i*100 for i in timings_ne[f]], 
                            alpha=0.5, label='Numexpr %s' %f, marker='o')
        plt.legend(loc='upper left')
        plt.xscale('log')
        plt.yscale('log')
        plt.grid()
        plt.xlabel('number of elements per matrix')
        plt.ylabel('time in milliseconds')    
    plt.show()


# <br>
# <br>

# # Results

# In[23]:


print_sysinfo()
summary_table(funcs)
plot_figures(funcs)


# Since `numexpr` makes use of multi-threading (thereby bypassing Python's GIL - Global Interpreter Lock) we can see an increase in performance for the especially CPU-heavy tasks when we are using `numexpr`, i.e., for larger matrix sizes and especially for more complex vectorized expressions (see the plot in the lower left).

# # References
# - https://nbviewer.org/github/rasbt/One-Python-benchmark-per-day/blob/master/ipython_nbs/day7_numpy_numexpr.ipynb

# In[ ]:




