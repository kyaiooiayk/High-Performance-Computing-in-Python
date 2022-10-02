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

iterations_count = round(1e7)

def complex_operation(input_index):
    print("Complex operation. Input index: {:2d}".format(input_index))

    [math.exp(i) * math.sinh(i) for i in [1] * iterations_count]

def complex_operation_numpy(input_index):
    print("Complex operation (numpy). Input index: {:2d}".format(input_index))

    data = np.ones(iterations_count)
    np.exp(data) * np.sinh(data)

@timebudget
def run_complex_operations(operation, input, pool):
    pool.map(operation, input)

processes_count = 10

if __name__ == '__main__':
    processes_pool = Pool(processes_count)
    print('Without NumPy')
    run_complex_operations(complex_operation, range(10), processes_pool)
    print('\nNumPy')
    run_complex_operations(complex_operation_numpy, range(10), processes_pool) 
    
    
"""
Many calculations for specialized libraries like NumPy are unaffected by the GIL and can use threads and other techniques to work in parallel. This section of the tutorial goes over the benefits of combining NumPy and multiprocessing.

It is faster is because most processing in NumPy is vectorized. With vectorization, the underlying code is effectively “parallelized” because the operation can calculate multiple array elements at once, rather than looping through them one at a time. 
"""