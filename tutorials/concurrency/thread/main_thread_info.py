# https://superfastpython.com/threading-in-python/

# example of getting the main thread
from threading import main_thread

# get the main thread
thread = main_thread()
# report properties for the main thread
print(f"name={thread.name}, daemon={thread.daemon}, id={thread.ident}")
