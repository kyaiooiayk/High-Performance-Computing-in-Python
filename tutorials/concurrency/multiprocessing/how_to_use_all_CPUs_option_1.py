#

# SuperFastPython.com
# example of a program that uses all cpu cores
import math
from concurrent.futures import ProcessPoolExecutor


# define a cpu-intensive task
def task(arg):
    return sum([math.sqrt(i) for i in range(1, arg)])


# protect the entry point
if __name__ == "__main__":
    # report a message
    print("Starting task...")
    # create the process pool
    with ProcessPoolExecutor(12) as exe:
        # perform calculations
        results = exe.map(task, range(1, 50000))
    # report a message
    print("Done.")
