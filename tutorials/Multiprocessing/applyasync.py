import time
from multiprocessing import Pool, current_process

def slow_add(nsecs, x, y):
    """
    Function that sleeps for 'nsecs' seconds, and
    then returns the sum of x and y
    """
    print("Process %s going to sleep for %s second(s)" % (current_process().pid,nsecs))

    time.sleep(nsecs)

    print("Process %s waking up" % current_process().pid)

    return x + y

if __name__ == "__main__":
    print("Master process is PID %s" % current_process().pid)

    with Pool() as pool:
        r1 = pool.apply_async(slow_add, [1, 6, 7])
        r2 = pool.apply_async(slow_add, [1, 2, 3])

        r1.wait()
        print("Result one is %s" % r1.get())

        r2.wait()
        print("Result two is %s" % r2.get())