# ⁉️What is concurrency?
- Concurrency is the capability of having more than one computation in progress at the same time.
- Concurrency is a different type of programming. So not only: procedural, functional and OOP. 
- Concurrency is what allows: concurrent, parallel and asynchronous execution.
- Concurrency is not Parallelism. While concurrency implies that multiple tasks are in process simultaneously, it does not imply that they are running together in parallel.
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

## What is for what: decision matrix?
   
| Python native package | Type of concurrency | What they work on/ what they create? | Memory management | Usage | Control |
| :-: | :-: | :-: | :-: | :-: | :-: |
| Python multiprocessing | Process-based concurrency | A process refers to a computer program. Each process is in fact one instance of the Python interpreter that executes Python instructions (Python byte-code). | Processes do not have shared memory, instead, data is transmitted between processes using inter-process communication. | Use it for CPU-boind bound tasks | Operating system controls when a process is suspended, resumed and executed. |
| Python threading | Thread-based concurrenc | A thread refers to a thread of execution by a computer program. Every Python program is a process with one thread called the main thread used to execute your program instructions. | | Use it for I/O-bound task | Operating system controls when a thread is suspended, resumed and executed. |
| Python asyncio | Coroutine-based concurrency | A coroutine is a unit of concurrency that is more lightweight than a thread. A single thread may execute many coroutines in an event loop. | | Non-blocking I/O | Coroutines themselves controls when a process is suspended, resumed and executed. |
***

## References
- [Superfastpython](https://superfastpython.com)
***