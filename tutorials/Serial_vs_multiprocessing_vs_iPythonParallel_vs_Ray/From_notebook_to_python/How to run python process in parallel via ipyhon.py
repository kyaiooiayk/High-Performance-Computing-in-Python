#!/usr/bin/env python
# coding: utf-8

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black><br>
#
# **What?** How to run python process in parallel via ipyhon
#
# <br></font>
# </div>

# # Installing iPyhton parallel

# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - **Step #1:** pip install ipyparallel
# - **Step #2:** jupyter serverextension enable --py ipyparallel
# - **Step #3:** jupyter nbextension install --py ipyparallel
# - **Step #4:** upyter nbextension enable --py ipyparallel
#
# <br></font>
# </div>

# # How to run the code

# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - Open a fresh new terminal
# - Start the cluster via **ipcluster start**
# - Then wait untill you see on the command line **Engines appear to have started successfully**. This may take up to 30 seconds.
#
# <br></font>
# </div>

# In[30]:


import math
import numpy as np
from timebudget import timebudget
import ipyparallel as ipp

iterations_count = round(1e7)


def complex_operation(input_index):
    print("Complex operation. Input index: {:2d}".format(input_index))

    [math.exp(i) * math.sinh(i) for i in [1] * iterations_count]


def complex_operation_numpy(input_index):
    print("Complex operation (numpy). Input index: {:2d}".format(input_index))

    data = np.ones(iterations_count)
    np.exp(data) * np.sinh(data)


@timebudget
def run_complex_operations(operation, input, pool):
    pool.map(operation, input)


client_ids = ipp.Client()
pool = client_ids[:]

input = range(10)
print("Without NumPy")
run_complex_operations(complex_operation, input, pool)
print("NumPy")
run_complex_operations(complex_operation_numpy, input, pool)


# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# -  Shut done the cluser with **ipcluster stop** and wait until you see the program finishes. This may take up to 30 seconds.
# - Clean any temp files with **ipcluster clean**
#
# <br></font>
# </div>

# # Second method - more elegant

# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - Allocate a cluster (collection of IPython engines for use in parallel)
# - Run a collection of tasks on the cluster
# - Wait interactively for results
# - Cleanup resources after the task is done
#
# <br></font>
# </div>

# In[3]:


import os

print("Number of CPUs in the system: {}".format(os.cpu_count()))


# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - We can see ths machine has 8 CPUs.
# - The cluste will automatically start 8 **engines**.
# - Given a total amount of jobs in number of 100, the programm will send them in **batches of 8**.
#
# <br></font>
# </div>

# In[22]:


import time, math
import ipyparallel as ipp

task = [i / (i + 1) for i in range(round(1e7))]

task_durations = [1] * 16

# request a cluster
with ipp.Cluster() as rc:
    # get a view on the cluster
    view = rc.load_balanced_view()

    # submit the tasks
    asyncresult = view.map_async(time.sleep, task_durations)

    # wait interactively for results
    asyncresult.wait_interactive()

    # retrieve actual results
    result = asyncresult.get()


# In[21]:


print(result)


# # References

# <div class="alert alert-block alert-warning">
# <font color=black><br>
#
# - [Code example to be run in parallel](https://www.anyscale.com/blog/parallelizing-python-code)
# - [How to install and acitvate iPython](https://ipyparallel.readthedocs.io/en/latest/)
#
# <br></font>
# </div>

# In[ ]:
