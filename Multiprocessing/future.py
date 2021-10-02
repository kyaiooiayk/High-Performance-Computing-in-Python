import time
from multiprocessing import Pool

def slow_add(nsecs, x, y):
    """
    Function that sleeps for 'nsecs' seconds, and
    then returns the sum of x and y
    """
    time.sleep(nsecs)
    return x + y

def slow_diff(nsecs, x, y):
    """
    Function that sleeps for 'nsecs' seconds, and
    then retruns the difference of x and y
    """
    time.sleep(nsecs)
    return x - y

def broken_function(nsecs):
    """Function that deliberately raises an AssertationError"""
    time.sleep(nsecs)
    raise ValueError("Called broken function")

if __name__ == "__main__":
    futures = []

    with Pool() as pool:
        futures.append(pool.apply_async(slow_add, [3, 6, 7]))
        futures.append(pool.apply_async(slow_diff, [2, 5, 2]))
        futures.append(pool.apply_async(slow_add, [1, 8, 1]))
        futures.append(pool.apply_async(slow_diff, [5, 9, 2]))
        futures.append(pool.apply_async(broken_function, [4]))

        while True:
            all_finished = True

            print("\nHave the workers finished?")

            for i, future in enumerate(futures):
                if future.ready():
                    print("Process %s has finished" % i)
                else:
                    all_finished = False
                    print("Process %s is running..." % i)

            if all_finished:
                break

            time.sleep(1)

        print("\nHere are the results.")

        for i, future in enumerate(futures):
            if future.successful():
                print("Process %s was successful. Result is %s" % (i, future.get()))
            else:
                print("Process %s failed!" % i)

                try:
                    future.get()
                except Exception as e:
                    print("    Error = %s : %s" % (type(e), e))