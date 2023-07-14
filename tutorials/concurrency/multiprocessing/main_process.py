# https://superfastpython.com/main-process-in-python/
# SuperFastPython.com


# example of checking if a process is the main process via its type
from multiprocessing import current_process
from multiprocessing import parent_process
from multiprocessing import Process

# get the main process
process = current_process()
# report the type of the main process
print(type(process))


# return True if the process is the main process, false otherwise
def is_main_process():
    # process is the main process if it has a specific type
    return not issubclass(type(current_process()), Process)


# check if this is the main process
print(f"Main Process: {is_main_process()}")


# return True if the process is the main process, false otherwise
def is_main_process():
    # process is the main process if it has no parent process
    return parent_process() == None


# check if this is the main process
print(f"Main Process: {is_main_process()}")


# return True if the process is the main process,  false otherwise
def is_main_process():
    # process is the main process if its name is 'MainProcess'
    return current_process().name == "MainProcess"


# check if this is the main process
print(f"Main Process: {is_main_process()}")
