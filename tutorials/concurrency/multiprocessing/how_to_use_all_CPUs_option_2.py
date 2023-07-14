# https://superfastpython.com/python-use-all-cpu-cores/
# SuperFastPython.com

# example of a program that uses all cpu cores
import math
from multiprocessing import Pool


# define a cpu-intensive task
def task(arg):
    return sum([math.sqrt(i) for i in range(1, arg)])


# protect the entry point
if __name__ == "__main__":
    # report a message
    print("Starting task...")
    # create the process pool
    with Pool(12) as pool:
        # perform calculations
        results = pool.map(task, range(1, 50000))
    # report a message
    print("Done.")
