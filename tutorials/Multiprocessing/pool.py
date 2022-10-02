from functools import reduce
from multiprocessing import Pool, cpu_count, current_process

def square(x):
    """Function to return the square of the argument"""
    #print("Worker %s calculating square of %s" % (current_process().pid, x))
    return x * x

if __name__ == "__main__":
    """
    You must now protect the code being run by
    the master copy of the script by placing it
    in this block
    """
    
    # print the number of cores
    print("Number of cores available equals %s" % cpu_count())

    # create a pool of workers
    with Pool(processes = cpu_count()) as pool:
        # create an array of 5000 integers, from 1 to 5000
        r = range(1, 5001)
        result = pool.map(square, r)

    total = reduce(lambda x, y: x + y, result)

    print("The sum of the square of the first 5000 integers is %s" % total)