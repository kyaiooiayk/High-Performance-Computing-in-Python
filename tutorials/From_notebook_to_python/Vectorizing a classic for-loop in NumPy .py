#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Vectorizing" data-toc-modified-id="Vectorizing-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Vectorizing</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Euclidean-Distance" data-toc-modified-id="Euclidean-Distance-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Euclidean Distance</a></span></li><li><span><a href="#Python-vs.-NumPy" data-toc-modified-id="Python-vs.-NumPy-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Python vs. NumPy</a></span></li><li><span><a href="#Time-benchmarks" data-toc-modified-id="Time-benchmarks-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Time benchmarks</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Vectorizing a classic for-loop in NumPy
#
# </font>
# </div>

# # Vectorizing
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# One of the biggest advantages of NumPy, besides its convenient usage, is the speed gain over classic Python loop structures via vectorized arithmetic operations for its `ndarray` objects.
#
# In general, "vectorizing" means that artithmetic operations on elments  in a vector can be done in parallel as an 1-step process.
# In theory, if we forget about additional overheads, a vectorized arithmetic addition, e.g.,
#
# $\begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix} + 1 = \begin{pmatrix} 1+1 \\ 2+1 \\ 3+1 \\ 4+1 \end{pmatrix} = \begin{pmatrix} 2 \\ 3 \\ 4 \\ 5\end{pmatrix}$
#
# could be 4 times faster than adding the constant 1 to every number in sequential order.
#
# In NumPy, some operations that are using the architecture's "BLAS" (Basic Linear Algebra Subroutines) can also take advantage of CPUs with multiple cores and run multiple processes in parallel, for example, the matrix dot product (`numpy.np(A,B)` or `A.dot(B)`).
# Other array operations.
#
# Other arithmetic operations in NumPy, e.g, arithmetic addition, don't make use of BLAS in the current implementation of NumPy. However, those are still overcoming Python's GIL (Global Interpreter Lock) to allow multi-threading (not to be confused with multi-processing), which can still result in a significant speed boost.
#
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[1]:


import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
import timeit
import random

random.seed(123)
from numpy.linalg import norm as np_linalg_norm


# # Euclidean Distance
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# As we can see in the plot, the vectorized code runs a lot faster than our classic Python `for`-loop (note that this graph is plotted on logarithmic scale).
#
# For the following benchmarks, we will use a simple Euclidean distance calculation with the following equation
#
#
# \begin{equation} d = \sqrt{(X_1 - Y_1)^2 + (X_2 - Y_2)^2 + (X_3 - Y_3)^2 + ... (X_d - Y_d)}\end{equation}
#
# But before we skip to the actual benchmark, let us visualize it for a set of 2 3D coordinates:
#
#
# </font>
# </div>

# In[2]:


coords1 = [1, 2, 3]
coords2 = [4, 5, 6]

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")

ax.scatter(
    (coords1[0], coords2[0]),
    (coords1[1], coords2[1]),
    (coords1[2], coords2[2]),
    color="k",
    s=150,
)

ax.plot(
    (coords1[0], coords2[0]),
    (coords1[1], coords2[1]),
    (coords1[2], coords2[2]),
    color="r",
)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.text(x=2.5, y=3.5, z=4.0, s="d = 5.19")

# plt.title('Euclidean distance between 2 3D-coordinates')

plt.show()


# # Python vs. NumPy
# <hr style = "border:2px solid black" ></hr>

# In[3]:


# Small sample data of 3D coordinates
coords1 = [1, 2, 3]
coords2 = [4, 5, 6]
np_c1 = np.array(coords1)
np_c2 = np.array(coords2)


# In[4]:


# Classic For-loop
def eucldist_forloop(coords1, coords2):
    """Calculates the euclidean distance between 2 lists of coordinates."""
    dist = 0
    for (x, y) in zip(coords1, coords2):
        dist += (x - y) ** 2
    return dist**0.5


# In[5]:


# Generator expression
def eucldist_generator(coords1, coords2):
    """Calculates the euclidean distance between 2 lists of coordinates."""
    return sum((x - y) ** 2 for x, y in zip(coords1, coords2)) ** 0.5


# In[6]:


# Vectorized version using NumPy
def eucldist_vectorized(coords1, coords2):
    """Calculates the euclidean distance between 2 lists of coordinates."""
    return np.sqrt(np.sum((coords1 - coords2) ** 2))


# In[7]:


# Using an in-built NumPy function
np.linalg.norm(np_c1 - np_c2)


# In[8]:


print(eucldist_forloop(coords1, coords2))
print(eucldist_generator(coords1, coords2))
print(eucldist_vectorized(np_c1, np_c2))
print(np.linalg.norm(np_c1 - np_c2))


# # Time benchmarks
# <hr style = "border:2px solid black" ></hr>

# In[9]:


funcs = (
    "eucldist_forloop",
    "eucldist_generator",
    "eucldist_vectorized",
    "np_linalg_norm",
)
times = {f: [] for f in funcs}
orders_n = [10**i for i in range(1, 8)]
for n in orders_n:

    c1 = [random.randint(0, 100) for _ in range(n)]
    c2 = [random.randint(0, 100) for _ in range(n)]
    np_c1 = np.array(c1)
    np_c2 = np.array(c2)

    assert (
        eucldist_forloop(c1, c2)
        == eucldist_generator(c1, c2)
        == eucldist_vectorized(np_c1, np_c2)
        == np_linalg_norm(np_c1 - np_c2)
    )

    times["eucldist_forloop"].append(
        min(
            timeit.Timer(
                "eucldist_forloop(c1, c2)",
                "from __main__ import c1, c2, eucldist_forloop",
            ).repeat(repeat=50, number=1)
        )
    )
    times["eucldist_generator"].append(
        min(
            timeit.Timer(
                "eucldist_generator(c1, c2)",
                "from __main__ import c1, c2, eucldist_generator",
            ).repeat(repeat=50, number=1)
        )
    )
    times["eucldist_vectorized"].append(
        min(
            timeit.Timer(
                "eucldist_vectorized(np_c1, np_c2)",
                "from __main__ import np_c1, np_c2, eucldist_vectorized",
            ).repeat(repeat=50, number=1)
        )
    )
    times["np_linalg_norm"].append(
        min(
            timeit.Timer(
                "np_linalg_norm(np_c1 - np_c2)",
                "from __main__ import np_c1, np_c2, np_linalg_norm",
            ).repeat(repeat=50, number=1)
        )
    )


# In[10]:


labels = {
    "eucldist_forloop": "for-loop",
    "eucldist_generator": "generator expression (comprehension equiv.)",
    "eucldist_vectorized": "NumPy vectorization",
    "np_linalg_norm": "numpy.linalg.norm",
}


def plot(times, orders_n, labels):

    colors = ("cyan", "#7DE786", "black", "blue")
    linestyles = ("-", "-", "--", "--")
    fig = plt.figure(figsize=(11, 10))
    for lb, c, l in zip(labels.keys(), colors, linestyles):
        plt.plot(
            orders_n, times[lb], alpha=1, label=labels[lb], lw=3, color=c, linestyle=l
        )
    plt.xlabel("sample size n (items in the list)", fontsize=14)
    plt.ylabel("time per computation in seconds", fontsize=14)
    plt.xlim([min(orders_n) / 10, max(orders_n) * 10])
    plt.legend(loc=2, fontsize=14)
    plt.grid()
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.xscale("log")
    plt.yscale("log")
    plt.title("Python for-loop/generator expr. vs. NumPy vectorized code", fontsize=18)
    plt.show()


# In[11]:


plot(times, orders_n, labels)


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-danger">
# <font color=black>
#
# - However, it’s not without disadvantages. One issue is that it can be highly memory-intensive.
# - For example, the vectorized maximization routine above is far more memory intensive than the non-vectorized version that preceded it.
# - This is because vectorization tends to create many intermediate arrays before producing the final calculation.
#
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://nbviewer.org/github/rasbt/One-Python-benchmark-per-day/blob/master/ipython_nbs/day16_numpy_vectorization.ipynb
# - http://wiki.scipy.org/ParallelProgramming
#
# </font>
# </div>

# In[ ]:
