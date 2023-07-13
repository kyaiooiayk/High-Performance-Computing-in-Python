# ⏱High-Performance-Computing-in-Python
*Parallel computing, cython, numba, multi-processing and multi-threading in Python.*
***

## 📌Motivation
- Python was created for humans and to help them experiment idea faster. Many details such as variable types and memory allocation and deallocation are then left to the runtime to decide.
- The downside is that Python is slower and harder to optimise - than languages like C or Fortran.
- **So, why are we still sticking to python?** No! Most program have few part that are time-critical. Even, for this parts, itis possible to achieve the same speed as C or Fortran.
***

## ⁉Why parallelisation?
- The growth of CPU clock speed (i.e., the speed at which a single chain of logic can be run) has slowed dramatically.
- As a response, hardware makers have increased the number of cores (physical CPUs) embedded in each machine as a differnt avenue to fast execution: parallelisation.
***

## ⁉What is concurrency?
- Concurrency is the capability of having more than one computation in progress at the same time.
- Concurrency is a different type of programming. So not only: procedural, functional and OOP.
- Concurrency is what allows: concurrent, parallel and asynchronous execution.
- ***

## 📦Packages
- Native:
  - Python **multiprocessing** for process-based concurrency. A process refers to a computer program. Multiprocesses are appropriate for CPU-bound tasks, and not I/O-bound tasks.
  - Python **threading** for thread-based concurrency. A thread refers to a thread of execution by a computer program. Because of the GIL, threads are appropriate for I/O-bound tasks, and not CPU-bound tasks.
  - Python **asyncio** for coroutine-based concurrency. A coroutine is a unit of concurrency that is more lightweight than a thread.
- Third parties:
    - ray: a framework for scaling Python applications.
    - tornado: Python web framework and asynchronous networking library.
    - celery: Distributed task queue.
    - sanic: Async Python web server and framework.
    - aiohttp: Asynchronous HTTP client/server framework for asyncio
    - dask: Parallel computing with task scheduling.
    - uvloop: Ultra fast asyncio event loop.
***

## 🏫Available tutorials
- [Caching](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/master/tutorials/Caching.ipynb)
- [Code profiling](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/master/tutorials/Code_profiling.ipynb)
- [Concurrency](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/tree/main/tutorials/concurrency)
- [Cython - Bridging the gap between Python and Fortran](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/master/tutorials/%20Cython%20-%20Bridging%20the%20gap%20between%20Python%20and%20Fortran.ipynb)
- [Cython & Numba, C-like performance](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/master/tutorials/Cython%20%26%20Numba%2C%20C-like%20performance.ipynb)
- [Cython vs. Numba vs. Parakeet on Bubblesort](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/master/tutorials/Cython%20vs.%20Numba%20vs.%20Parakeet%20on%20Bubblesort.ipynb)
- [How to cythonise your code](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/master/tutorials/cythonizing/How%20to%20cythonize%20your%20code.ipynb)
- [How to optimise scikit-learn execution time](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/master/tutorials/How%20to%20optimise%20scikit-learn%20execution%20time.ipynb)
- [Implicit Multithreading in NumPy](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/master/tutorials/Implicit%20Multithreading%20in%20NumPy.ipynb)
- [Memoisation and decorators](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/master/tutorials/Memoisation%20and%20decorator.ipynb)
- [Multiprocessing](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/tree/master/tutorials/Multiprocessing)
- [numba](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/master/tutorials/numba.ipynb)
- [NumPy vs. Numba vs. Cython](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/master/tutorials/NumPy%20vs.%20Numba%20vs.%20Cython.ipynb)
- [Parallel programming with Python (threading, multiprocessing](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/master/tutorials/Parallel%20programming%20with%20Python%20(threading%2C%20multiprocessing).ipynb)
- [Profiling Scikit-Learn Parallel Job](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/tree/master/tutorials/Profiling_SKLearn_Parallel_Jobs)
- [Python's and NumPy's in-place operator functions](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/master/tutorials/Python's%20and%20NumPy's%20in-place%20operator%20functions.ipynb)
- [Scoop](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/tree/master/tutorials/Scoop)
- [Speeding up NumPy array expressions with Numexpr](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/master/tutorials/Speeding%20up%20NumPy%20array%20expressions%20with%20Numexpr.ipynb)
- [Vectorisation](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/master/tutorials/Vectorisation.ipynb)
- [Vectorizing a classic for-loop in NumPy](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/master/tutorials/Vectorizing%20a%20classic%20for-loop%20in%20NumPy%20.ipynb)
- [Atomic operations](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/blob/main/tutorials/Atomic%20operations.ipynb)
***

## 🧑‍🎓Study notes
- [Parallel computing](https://drive.google.com/drive/u/1/folders/13mzxrofldkbdgF_eT5EPZ1cEiCgOT78d)
***

## 📚References
- [The counter-intuitive rise of Python in scientific computing](https://cerfacs.fr/coop/fortran-vs-python)
- [Need for speed](https://github.com/QuantEcon/lecture-python-programming.notebooks/blob/master/need_for_speed.ipynb)
- [Parallelisation](https://github.com/QuantEcon/lecture-python-programming.notebooks/blob/master/parallelization.ipynb)
- [SuperFastPython](https://superfastpython.com/learning-paths/#Threading_Learning_Path)
***
