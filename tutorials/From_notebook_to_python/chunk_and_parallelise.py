#!/usr/bin/env python
# coding: utf-8

# In[1]:


from functools import wraps
import numpy as np
import multiprocess as mp


# In[2]:


def _get_no_cpu(no_cpu):    
    return mp.cpu_count() if (no_cpu == -1) else no_cpu
    
    
def para(
    func_: None = None,
    no_cpu: int = 1
):    

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            print("argument", *args)
            print("kwargs", *kwargs)
            
            _no_thread = _get_no_cpu(no_cpu)
            
            chunks = np.array_split([*args[0]], _no_thread)

            pool = mp.Pool(processes=_no_thread)
            results = [pool.apply_async(func, args=(x,)) for x in chunks]
            output = [j for p in results for j in p.get()]

            return output

        return wrapper

    if callable(func_):
        return _decorator(func_)
    elif func_ is None:
        return _decorator
    else:
        raise RuntimeWarning("Positional arguments are not supported!")


# In[3]:


import psutil
print("How many LOGICAL CPUs?", psutil.cpu_count(
    logical=True))
print("How many PHYSICAL CPUs?", psutil.cpu_count(
    logical=False))


# In[4]:


import time
def func(x):    
    # Emulate expensive calculation
    def WAIT(x):
        time.sleep(1)
        return x
    
    # Emulate a real ouput
    z = [WAIT(i) for i in x]
    return z
output = func(range(10))
output


# In[9]:


@para(no_cpu=12)
def func(x):    
    # Do expensive calculation
    def WAIT(x):
        time.sleep(1)
        return x
    
    # Emulate a real ouput
    z = [WAIT(i) for i in x]
    return z

output = func(range(10))
output


# In[ ]:





# In[ ]:





# In[ ]:




