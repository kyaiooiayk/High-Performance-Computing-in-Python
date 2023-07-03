import time
from multiprocessing import Pool, current_process, cpu_count


def slow_function(nsecs):
    """
    Function that sleeps for 'nsecs' seconds, returning
    the number of seconds that it slept
    """

    print("Process %s going to sleep for %s second(s)" % (current_process().pid, nsecs))

    # use the time.sleep function to sleep for nsecs seconds
    time.sleep(nsecs)

    print("Process %s waking up" % current_process().pid)

    return nsecs


if __name__ == "__main__":
    print("Master process is PID %s" % current_process().pid)

    with Pool(processes=cpu_count()) as pool:
        r = pool.apply(slow_function, [5])

    print("Result is %s" % r)
