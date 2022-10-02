"""
What? How to use Ray for running python jobs in parallel

References: https://www.anyscale.com/blog/parallelizing-python-code
            https://gist.github.com/mGalarnyk/30c8672620c8655a37940be935899a57
"""

# Import modules
import math
import numpy as np
from timebudget import timebudget
import ray

iterations_count = round(1e7)

@ray.remote
def complex_operation(input_index):
    print("Complex operation. Input index: {:2d}".format(input_index))

    [math.exp(i) * math.sinh(i) for i in [1] * iterations_count]

@ray.remote
def complex_operation_numpy(input_index):
    print("Complex operation (numpy). Input index: {:2d}".format(input_index))

    data = np.ones(iterations_count)
    np.exp(data) * np.sinh(data)

@timebudget
def run_complex_operations(operation, input):    
    ray.get([operation.remote(i) for i in input])

ray.init()

input = range(8)
print('Without NumPy')
run_complex_operations(complex_operation, input)
print('NumPy')
run_complex_operations(complex_operation_numpy, input)