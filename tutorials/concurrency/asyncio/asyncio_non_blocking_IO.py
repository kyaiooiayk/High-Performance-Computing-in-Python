# SuperFastPython.com
# https://superfastpython.com/python-asynchronous-programming/

# example of asynchronous programming with asyncio
import asyncio


# define a coroutine to run as a task
async def task_coroutine():
    # report a message
    print("Hello from the task")
    # sleep a moment
    await asyncio.sleep(4)
    # report another message
    print("Task is all done")


# entry point coroutine
async def main():
    # create the task coroutine
    coro = task_coroutine()
    # wrap in a task object and schedule execution
    task = asyncio.create_task(coro)
    # suspend a moment to allow the task to run
    await asyncio.sleep(0)
    # do other things, like report a message
    print("Main is doing other things...")
    print("Async did not block caller!")

    print("Waiting for the task to complete")
    await task


# entry point into the program
asyncio.run(main())
