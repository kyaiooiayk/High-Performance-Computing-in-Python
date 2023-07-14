# https://superfastpython.com/process-name/#How_to_Change_the_Process_Name

# SuperFastPython.com
# example of setting the process name via the property
from multiprocessing import Process
from multiprocessing import current_process


# function executed in a new process
def task():
    # get the current process
    process = current_process()
    # report a message
    print(f"Hello from a new process: {process.name}")
    # change the name (while running)
    process.name = "BestWorker"
    # report a message
    print(f"Hello again, this time from: {process.name}")


# entry point
if __name__ == "__main__":
    # create a new process
    process = Process(target=task)

    # Get default name
    print(f"Hello from a new process: {process.name}")

    # set a custom name for the new process
    process.name = "Worker"
    # start the new process
    process.start()
    # wait until the new process has terminated
    process.join()
