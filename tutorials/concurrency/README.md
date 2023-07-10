# Concurrency
***

## ⁉️What is concurrency?
- Concurrency is the capability of having more than one computation in progress at the same time.
- Concurrency is a different type of programming. So not only: procedural, functional and OOP.
- Concurrency is what allows: concurrent, parallel and asynchronous execution.
- Concurrency is not Parallelism. While concurrency implies that multiple tasks are in process simultaneously, it does not imply that they are running together in parallel.
***

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

## What is for what: decision matrix?
    
| Python module | Type of concurrency | Request & Execution | What they work on/ what they create? | Memory management | Usage | Control | Protection |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| `multiprocessing` | Process-based | | A process refers to a computer program. Each process is in fact one instance of the Python interpreter that executes Python instructions (Python byte-code). | Processes do not have shared memory, instead, data is transmitted between processes using inter-process communication. | CPU-bound tasks | Operating system controls when a process is suspended, resumed and executed. | Requires `if __name__ == '__main__'` |
| `threading` | Thread-based within a process | | A thread refers to a thread of execution by a computer program. Every Python program is a process with one thread called the main thread used to execute your program instructions. | | IO-bound tasks | Operating system controls when a thread is suspended, resumed and executed. | |
| `asyncio` | Coroutine-based within a thread | An action is requested but not performed at the same time. The function call will not wait and we can request data later. It allows called to perform other activities. | A coroutine is a unit of concurrency that is more lightweight than a thread. A single thread may execute many coroutines in an event loop. | | Non-blocking I/O | Coroutines themselves controls when a process is suspended, resumed and executed. | |

![image](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/assets/89139139/21a2d169-01e6-4649-9b8d-668a2aaff1df)
![image](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/assets/89139139/81d69a11-4279-4ee1-8f40-4652446315da)

## CPU-bound vs. IO-bound?
- A **CPU-bound** task is a type of task where the limiting factor is the speed of the CPU than the limit of IO. Examples:
    - Calculating points in a fractal
    - Estimating P
    - Factoring primes
    - Parsing HTML, JSON, etc. documents
    - Processing text and running simulations. 
- A **IO-bound** task is a type of task where the limiting factor is the the IO speed. These are operation that involve reading from or writing to a device, file, or socket connection. Examples:
    - Reading or writing a file from the hard drive.
    - Reading or writing to standard output, input, or error (stdin, stdout, stderr).
    - Printing a document.
    - Downloading or uploading a file.
    - Querying a server.
    - Querying a database.
    - Taking a photo or recording a video
- A 4GHz CPU can execute 4 billion instructions per second. Compare to CPU speed, IO is much much slower
- **Important**: typically, processes are used for CPU-bound tasks and threads are used for IO-bound tasks, and this is a good heuristic, but this does not have to be the case. Again, this is an heuristic rule. At the end of the day, try and take what works best for you. 
***

## How do I choose the best approach?
- **First question: CPU-bound vs. IO-bound?**

![image](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/assets/89139139/523a7f76-c20e-4279-8bbb-9c24ba634624)

- **Second question: Many Ad Hoc Tasks vs. One Complex Task?** Issue one or many ad hoc tasks that may benefit from a pool of reusable workers. 

![image](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/assets/89139139/398c57d2-50fe-4741-86ed-68d32a282fea)

- **Third question: Pool vs. Executor?** Both provide pools of workers. The similarities are many and the differences are few and subtle.

![image](https://github.com/kyaiooiayk/High-Performance-Computing-in-Python/assets/89139139/d5f63025-2755-4e38-abe7-43cae1e64eaf)

***

## References
- [Superfastpython](https://superfastpython.com)
- [How to choose btw APIs?](https://superfastpython.com/python-concurrency-choose-api/)
- [Notes on high-performing computing](https://drive.google.com/drive/u/1/folders/13mzxrofldkbdgF_eT5EPZ1cEiCgOT78d)
- [Python Concurrency Glossary](https://superfastpython.com/python-concurrency-glossary/)
***
