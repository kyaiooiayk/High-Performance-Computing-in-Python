# SuperFastPython.com
# https://superfastpython.com/concurrent-programming/

# example of executing a coroutine using the event loop
import asyncio
import time


# custom coroutine
async def custom_coro(message):
    # report the message
    time.sleep(1)
    print(message)


# create and execute coroutine
asyncio.run(custom_coro("Hi from a coroutine"))
