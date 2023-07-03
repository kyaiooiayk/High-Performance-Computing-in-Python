from functools import reduce
from multiprocessing import Pool, current_process
import time


def add(x, y):
    """Return the sum of the arguments"""
    print("Worker %s is processing add(%s, %s)" % (current_process().pid, x, y))
    time.sleep(1)
    return x + y


def product(x, y):
    """Return the product of the arguments"""
    print("Worker %s is processing product(%s, %s)" % (current_process().pid, x, y))
    time.sleep(1)
    return x * y


if __name__ == "__main__":

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    # Now create a Pool of workers
    with Pool() as pool:
        sum_future = pool.starmap_async(add, zip(a, b), chunksize=5)
        product_future = pool.starmap_async(product, zip(a, b))

        sum_future.wait()
        product_future.wait()

    total_sum = reduce(lambda x, y: x + y, sum_future.get())
    total_product = reduce(lambda x, y: x + y, product_future.get())

    print("Sum of sums of 'a' and 'b' is %s" % total_sum)
    print("Sum of products of 'a' and 'b' is %s" % total_product)
