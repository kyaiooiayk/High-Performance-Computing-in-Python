#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-are-they?" data-toc-modified-id="What-are-they?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What are they?</a></span></li><li><span><a href="#Atomic-operations" data-toc-modified-id="Atomic-operations-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Atomic operations</a></span></li><li><span><a href="#Non-Atomic-operations" data-toc-modified-id="Non-Atomic-operations-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Non-Atomic operations</a></span></li><li><span><a href="#Recommendations" data-toc-modified-id="Recommendations-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Recommendations</a></span></li><li><span><a href="#How-to-force-operations-to-be-atomic" data-toc-modified-id="How-to-force-operations-to-be-atomic-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>How to force operations to be atomic</a></span></li><li><span><a href="#References" data-toc-modified-id="References-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Atomic operations
# 
# </font>
# </div>

# # What are they?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - An atomic operation is executed without interruption.
# - What happens in concurrent programming where context switch is a possibility?. The operating system controls what threads execute and what is paused via a context switch. 
# - A thread cannot be context switched in the middle of an atomic operation.
# - This means that an atomic operations is thread-safe (context-switch safe) as we can expect them to be completed once started.
#     
# </font>
# </div>

# # Atomic operations
# <hr style = "border:2px solid black" ></hr>

# In[1]:


# assignment is atomic
x = 44
y = 33
x = y


# In[7]:


# assigning a property is atomic
class X():
    value = ""


x = X()
x.value = 33
x.value


# In[9]:


a = []
b = 1
# adding a value is atomic
a.append(b)
a


# In[14]:


a = [1, 2]
b = [3, 4]
# adding a list to a list is atomic
a.extend(b)
a


# In[15]:


# getting a value from a list is atomic
a = [1,2,3]
value = a[2]
value


# In[17]:


a = [1,2,3]
# removing a value from a list is atomic
value = a.pop()
print(value, a)


# # Non-Atomic operations
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Most operations are not atomic in Python.
# - This means that these operations are not thread-safe.
# - In this section we will discuss a few non-atomic operations that when used in concurrent programs can lead to a concurrent failure condition or bug called a race condition.
# 
# </font>
# </div>

# In[19]:


# adding and subtracting is not atomic
a =1
a = a + 1
a


# <div class="alert alert-info">
# <font color=black>
# 
# - The reason for this is at least three operations are involved, they are:
#     - Read the value of the variable.
#     - Calculate the new value for the variable
#     - Assign the calculated value of the variable.
# 
# </font>
# </div>

# In[20]:


a = [1,2,3]
a = [4,5,6]
# access and assign is not atomic
a[0] = b[0]


# # Recommendations
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - **Rule of thumb** in most cases, you should act as they are not available.
# - Thus follow this rules:
#     - The operations may not be atomic if the code is executed by a different Python interpreter.
#     - The behavior of the reference Python interpreter may change in the future.
#     - Other programmers who have to read your code may not be as intimately familiar with Python atomic operations.
#     - You may introduce more complex race conditions, e.g. operations are atomic but multiple such operations in a batch are not protected.  
# 
# </font>
# </div>

# # How to force operations to be atomic
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - In concurrency programming, it is common to have critical sections of code that may be executed by multiple threads simultaneously which must be protected.
# - These sections can be protected using locks such as the mutual exclusion lock (mutex) provided in the `threading.Lock` class.
# - Using the lock to protect a block of code **does NOT** prevent the thread from being context switched in the middle of an instruction or between instructions in the block.
# - Instead, **it prevents other threads** from executing the same block while a thread holds the lock.
# 
# </font>
# </div>

# ```python
# from threading import Lock
# from threading import Thread
# from random import random
# from time import sleep
# 
# # example of a mutual exclusion (mutex) lock
# 
# 
# # work function
# def task(lock, identifier, value):
#     # acquire the lock
#     with lock:
#         print(f">thread {identifier} got the lock, sleeping for {value}")
#         sleep(value)
# 
# 
# # create a shared lock
# lock = Lock()
# # start a few threads that attempt to execute the same critical section
# for i in range(10):
#     # start a thread
#     Thread(target=task, args=(lock, i, random())).start()
# # wait for all threads to finish...
# ```

# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [Thread atomic operation | Superfastpython](https://superfastpython.com/thread-atomic-operations/)
# - [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#Threading)
#     
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[26]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv -m')


# In[ ]:




