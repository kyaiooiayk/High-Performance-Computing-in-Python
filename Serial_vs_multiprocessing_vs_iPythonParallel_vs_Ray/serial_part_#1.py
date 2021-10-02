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

# Check # CPUs
print('Number of CPUs in the system: {}'.format(os.cpu_count()))


print("")
print("********************")
print("Repeated serial runs")
print("********************")

def complex_operation(input_index):
    """Complex operation
    
    Just simulates some complex and faily time consuming operations.
    """
    print("Complex operation. Input index: {:2d}".format(input_index))
    iterations_count = round(1e7)
    [math.exp(i) * math.sinh(i) for i in [1] * iterations_count]


@timebudget
def run_complex_operations(operation, input):
    """Run complex operations
    
    Executes several times to better estimate the processing time. It divides the
    long-running operation into a batch of smaller ones. It does this by dividing the
    input values into several subsets and then processing the inputs from those
    subsets in parallel.
    """
    for i in input:
        operation(i)

input = range(10)
run_complex_operations(complex_operation, input)


"""
On my laptop it took less than 30 secs. Can we imrove it
using python? We can use the multiprocessing python package 
to concurrently start several process. Its Pool object 
automatically divides input into subsets and distributes them 
among many processes. See next script called 
serial_vs_multithreading_part_#2.py
"""
