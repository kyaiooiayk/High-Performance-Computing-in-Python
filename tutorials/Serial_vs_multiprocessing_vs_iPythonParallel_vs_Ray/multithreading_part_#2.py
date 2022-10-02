"""
What? Compare pure serial vs. parallel jobs in python

Reference: https://www.anyscale.com/blog/parallelizing-python-code
           https://gist.github.com/mGalarnyk
"""

# Import modules
import math, os
import numpy as np
from timebudget import timebudget
from multiprocessing import Pool

def complex_operation(input_index):
    """Complex operation
    
    Just simulates some complex and faily time consuming operations.
    """
    print("Complex operation. Input index: {:2d}".format(input_index))
    iterations_count = round(1e7)
    [math.exp(i) * math.sinh(i) for i in [1] * iterations_count]


@timebudget
def run_complex_operations(operation, input, pool):
    pool.map(operation, input)

processes_count = 10
if __name__ == '__main__':
    print("")
    print("*********************")
    print("Using multiprocessing")
    print("*********************")
    processes_pool = Pool(processes_count)
    run_complex_operations(complex_operation, range(10), processes_pool) 

 
"""
In theory the time improvement could be reduced by total number
of processore avilable but this is never realised in full because
there is always some overhead done by python. What other options we have?
Use specialised library not affected by GIL such as numpy. See part #3. 
"""