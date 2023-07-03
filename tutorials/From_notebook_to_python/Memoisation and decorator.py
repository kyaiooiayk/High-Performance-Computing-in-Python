#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Memoization" data-toc-modified-id="Memoization-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Memoization</a></span></li><li><span><a href="#Baseline---recursive-fibonacci" data-toc-modified-id="Baseline---recursive-fibonacci-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Baseline - recursive fibonacci</a></span></li><li><span><a href="#via-dictionary" data-toc-modified-id="via-dictionary-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>via dictionary</a></span></li><li><span><a href="#via-lru_cache" data-toc-modified-id="via-lru_cache-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>via <code>lru_cache</code></a></span></li><li><span><a href="#via-decorator" data-toc-modified-id="via-decorator-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>via decorator</a></span></li><li><span><a href="#Callable-function" data-toc-modified-id="Callable-function-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Callable function</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Memoisation and decorator
#
# </font>
# </div>

# # Memoization
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - **Memoization** is a technique of recording the intermediate results so that it can be used to avoid repeated calculations and speed up the programs.
# - It can be used to optimize the programs that use **recursion**.
# - In Python, memoization can be done with the help of function **decorators**.
#
# </font>
# </div>

# # Baseline - recursive fibonacci
# <hr style = "border:2px solid black" ></hr>

# In[5]:


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(10)


# # via dictionary
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
#
# - We also presented a way to improve the runtime behaviour of the recursive version by adding a dictionary to memorize previously calculated values of the function.
# - The disadvantage of this method is that the clarity and the beauty of the original recursive implementation is lost.
#
# - The "problem" is that we changed the code of the recursive fib function. The following code doesn't change our fib function, so that its clarity and legibility isn't touched. To this purpose, we define and use a function which we call memoize. memoize() takes a function as an argument. The function memoize uses a dictionary "memo" to store the function results. Though the variable "memo" as well as the function "f" are local to memoize, they are captured by a closure through the helper function which is returned as a reference by memoize(). So, the call memoize(fib) returns a reference to the helper() which is doing what fib() would do on its own plus a wrapper which saves the calculated results. For an integer 'n' fib(n) will only be called, if n is not in the memo dictionary. If it is in it, we can output memo[n] as the result of fib(n).
#
#
# </font>
# </div>

# In[2]:


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib = memoize(fib)
print(fib(10))


# # via `lru_cache`
# <hr style = "border:2px solid black" ></hr>

# In[79]:


from functools import lru_cache


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# A simple example of memoization - in practice, use `lru_cache` from functools


def memoize(f):
    store = {}

    def func(n):
        if n not in store:
            store[n] = f(n)
        return store[n]

    return func


@memoize
def mfib(n):
    return fib(n)


@lru_cache()
def lfib(n):
    return fib(n)


assert fib(10) == mfib(10)
assert fib(10) == lfib(10)

get_ipython().run_line_magic("timeit", "- r1 - n10 fib(30)")
get_ipython().run_line_magic("timeit", "- r1 - n10 mfib(30)")
get_ipython().run_line_magic("timeit", "- r1 - n10 lfib(30)")


# # via decorator
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - We haven't used the Pythonic way of writing a decorator. Instead of writing the statement: `fib = memoize(fib)` we should have **decorated** our `fib` function with: `@memoize`
#
# </font>
# </div>

# In[6]:


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))


# # Callable function
# <hr style = "border:2px solid black" ></hr>

# In[7]:


class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://people.duke.edu/~ccc14/sta-663-2016/A01_CodeOptimization.html
# - https://python-course.eu/advanced-python/memoization-decorators.php
#
# </font>
# </div>

# In[ ]:
