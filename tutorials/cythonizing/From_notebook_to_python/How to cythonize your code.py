#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-cython?" data-toc-modified-id="What-is-cython?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is cython?</a></span></li><li><span><a href="#Fibonacci" data-toc-modified-id="Fibonacci-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Fibonacci</a></span></li><li><span><a href="#Cythonising" data-toc-modified-id="Cythonising-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Cythonising</a></span></li><li><span><a href="#Cython-and-Python-interaction" data-toc-modified-id="Cython-and-Python-interaction-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Cython and Python interaction</a></span></li><li><span><a href="#Testing" data-toc-modified-id="Testing-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Testing</a></span><ul class="toc-item"><li><span><a href="#Pure-python" data-toc-modified-id="Pure-python-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Pure python</a></span></li><li><span><a href="#Cythonised-python" data-toc-modified-id="Cythonised-python-6.2"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>Cythonised python</a></span></li><li><span><a href="#Pure-Cython" data-toc-modified-id="Pure-Cython-6.3"><span class="toc-item-num">6.3&nbsp;&nbsp;</span>Pure Cython</a></span></li></ul></li><li><span><a href="#No-free-lunch" data-toc-modified-id="No-free-lunch-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>No free lunch</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** How to cythonize your code
# 
# </font>
# </div>

# # What is cython?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - What we commonly call Python is really two different things: the language and the implementation. 
#     - The Python language defines the syntax (hence the language) with which we write code. 
#     - The most common **implementation** is CPython (written in C and Python), which compiles valid Python code into bytecode and then interprets it in real time as the program runs.
# - However, this flexibility has a cost, as it requires the interpreter to run a large number of tasks and checks behind the scenes at run time. 
# - Cython is an attempt to bridge the gap by bringing some of C’s qualities to Python. Cython code mostly looks like Python code, but it also adds optional C-inspired syntax. Most notably, it allows us to declare static types when defining variables/classes/functions.
# - Cython can automatically translate our code into C, which can then be then compiled into CPython extension modules. These compiled modules can be imported and used within Python code with significantly lower overhead than the equivalent Python modules.
# - One of the reason’s for Python’s popularity is the flexibility afforded by its dynamic typing and memory management. 
#     
# </font>
# </div>

# # Fibonacci
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `fib_py.py` is pure python implementation.
# 
# - `fib_py_cy.py` is identical to the pure python implementation and we'll cythonize it to compiled C code without making any manual changes.
# 
# - `fib_cy.pyx` is a pure cythonic implementation. Please note the ending `.pyx`.
# 
# </font>
# </div>

# In[6]:


get_ipython().system('ls')


# # Cythonising
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - In order to run the Cython code, we first have to Cythonize it. 
# - This involves two steps: 
#     - Translating our Python-like code into C code
#     - Compiling the C code into an executable. 
# 
# </font>
# </div>

# In[24]:


get_ipython().system('pwd')


# In[17]:


get_ipython().system('python setup_fibs.py build_ext --inplace')


# <div class="alert alert-info">
# <font color=black>
# 
# - **Step #1** - First, Python checks which of our files has changed since the last Cythonization. 
# - **Step #2** - Each of these is Cythonized, creating a *.c file. The C files are much longer and more complicated than the original Python file, or a true C implementation. The vast majority of this is specialized functions for interfacing between C and Python and handling various errors and exceptions.
# - **Step #3** - Then each `*.c` file is compiled using gcc to create a `*.so` dynamic library, which is able to communicate directly with CPython at runtime (this may be a *.pyd file if you are using Windows without WSL). 
# - Finally, the files are copied from the build/ directory to the working directory, where they can be imported by Python scripts.
# 
# </font>
# </div>

# In[23]:


get_ipython().system('ls')


# # Cython and Python interaction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Because we have used the flag `annotate=True` a `*.html` annotation file s created.
# - As stated in the file this shows the regions of the original Cython file based on how much Python interaction they require at runtime.
# - The idea here is: less yellow line will bring less interaction with python hence less runtime.
# 
# - In the `fib_py_cy.c` file there is no static type information, and thus has significant interaction with the Python interpreter due to the need for dynamic type checking and memory management throughout the loop. 
# - In the `fib_cy.c` file the only interacts with Python happens when calling and returning from the function; the internal computation of the loop is self-contained C code. 
#     
# </font>
# </div>

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# # Testing
# <hr style="border:2px solid black"> </hr>

# ## Pure python

# In[37]:


get_ipython().run_cell_magic('timeit', '', 'from fib_py import fib_py\n#print(fib_py(30))\n')


# ## Cythonised python

# In[35]:


get_ipython().run_cell_magic('timeit', '', 'from fib_py_cy import fib_py\n#print(fib_py(30))\n')


# ## Pure Cython

# In[38]:


get_ipython().run_cell_magic('timeit', '', 'from fib_cy import fib_cy\n#print(fib_cy(30))\n')


# # No free lunch
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# ```
# def fib_cy(int n):
#     cdef int a = 0
#     cdef int b = 1
#     cdef int i # <<---
#     for i in range(n - 1):
#         a, b = a + b, a
#     return a
# ```
# 
# - Notice how the answer produced by the typed Cython integer version is -811192543, rather than the correct answer of 7778742049. The reason for this is that Python3 integers can be unlimited size, while C integers can overflow if they get too big. 
# - This fact would typically be accounted for when cythonising the whole code directly; notice how the Cythonized Python version got the correct answer). 
# - However, in our static Cython code, these types of error checks are not performed. This shows that the speed advantages of Cython are not free – you do lose some of the flexibility & safety of Python, so some care is required. 
# 
# </font>
# </div>

# In[44]:


from fib_py import fib_py
print(fib_py(50))


# In[45]:


from fib_py_cy import fib_py
print(fib_py(50))


# In[46]:


print(fib_cy(50))


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://waterprogramming.wordpress.com/2022/06/29/cythonizing-your-python-code-part-1-the-basics/
# - Kurt W. Smith’s O’Reilly Media book, “Cython: A Guide for Python Programmers“.
# 
# </font>
# </div>

# In[ ]:




