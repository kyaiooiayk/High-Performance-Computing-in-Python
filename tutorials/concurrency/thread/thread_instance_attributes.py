# https://superfastpython.com/threading-in-python/
# https://superfastpython.com/how-to-configure-threads-in-python/

from threading import Thread
from threading import current_thread
from threading import get_ident
from threading import get_native_id
from time import sleep

# create the thread
thread = Thread(name="my_thread", daemon=False, target=lambda: sleep(3))
thread.start()

# report the thread name
print(f"Name: {thread.name}")
dummy = current_thread()
# report the name
print(f"Main name: {dummy.name}")


# report the daemon attribute
print(f"is daemon: {thread.daemon}")

# report the thread identifier
print(f"identifier: {thread.ident}")
# get the id for the current thread
identifier = get_ident()
# report the thread id
print(f"main identifier: {identifier}")


# report the native thread identifier
print(f"native identifier: {thread.native_id}")
identifier = get_native_id()
# report the thread id
print(f"native main identifier: {identifier}")

# report the thread is alive
print(f"is alive: {thread.is_alive()}")

# wait for the thread to finish
thread.join()

# report the thread is alive
print(thread.is_alive())
