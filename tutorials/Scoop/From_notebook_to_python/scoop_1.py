#!/usr/bin/env python
# coding: utf-8

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black><br>
#
# **What?** scoop
#
# **Reference:** https://github.com/chryswoods/siremol.org/blob/master/chryswoods.com/parallel_python/mapreduce_part3.md<br>
#
# <br></font>
# </div>

# # Running scoop on your single local machine

# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - You must ensure that all use of Scoop is protected within an if __name__ == "__main__" block.
# - You must import all modules and declare all functions at the top of your script, before the if __name__ == "__main__" block.
# - Create a new script called **mapreduce.py** and type into it
#
# <br></font>
# </div>

# In[ ]:


from scoop import futures


def product(x, y):
    """Return the product of the arguments"""
    return x * y


def sum(x, y):
    """Return the sum of the arguments"""
    return x + y


if __name__ == "__main__":
    a = range(1, 101)
    b = range(101, 201)

    results = futures.map(product, a, b)

    total = reduce(sum, results)

    print("Sum of the products equals %d" % total)


# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - Run this script using the command
# - python -m scoop mapreduce.py
#
# <br></font>
# </div>

# ## scoop.futures.mapReduce

# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - In the above example, we used scoop.futures.map to map the sum function.
# - All of the results were then transmitted back to the master process to complete the reduction (sum).
# - This is inefficient, as it means that a lot of data needs to be transmitted back to the master.
# - A better approach is to allow all of the workers in the cluster to perform the reduction as a group, thereby minimising communication.
# - This can be achieved by using the scoop.futures.mapReduce function.
# - This combines the map and reduce into a single function call.
# - Create a new script called **mapreduce_1.py**
# - Run the script using **python -m scoop mapreduce.py**
#
# <br></font>
# </div>

# In[ ]:


from scoop import futures


def product(x, y):
    """Return the product of the arguments"""
    return x * y


def sum(x, y):
    """Return the sum of the arguments"""
    return x + y


if __name__ == "__main__":
    a = range(1, 101)
    b = range(101, 201)

    total = futures.mapReduce(product, sum, a, b)

    print("Sum of the products equals %d" % total)


# # Running Scoop on a Cluster

# <div class="alert alert-block alert-info">
# <font color=black><br>
#
# - Scoop uses **SSH** to connect to and communicate between computers in a cluster.
# - You specify which computers to use for your job using a host file which contains a list of hostnames
# - run **python -m scoop --hostfile hostfile script.py**
# - Scoop comes with in-built support for many cluster schedulers, e.g. Sun Grid Engine (SGE), Torque (PBS-compatible, Moab, Maui) and SLURM.
#
# <br></font>
# </div>

# In[ ]:
