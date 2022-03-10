
# Import modules
from time import time, process_time, perf_counter, monotonic
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from joblib import parallel_backend
import multiprocessing, os, psutil


def train_SKL_model(n_jobs=None):
    """
    Train SKL model.

    This implements just some dummy ML method.
    """
    # define dataset
    X, y = make_classification(
        n_samples=10000, n_features=20, n_informative=15, n_redundant=5, random_state=3
    )
    # define the model
    model = RandomForestClassifier(n_estimators=500, n_jobs=n_jobs)
    # record current time
    #start, p1, t1 = time(), process_time(), thread_time()
    start, p1, t1 = time(), process_time(), perf_counter()
    # fit the model
    model.fit(X, y)
    # record current time
    #end, p2, t2 = time(), process_time(), thread_time()
    end, p2, t2 = time(), process_time(), perf_counter()
    # report execution time
    result = end - start
    #pr, tr = p2 - p1, t2 - t1
    pr, tr = p2 - p1, t2 - t1
    #print(f"wall: {result}, process: {pr}, thread: {tr}")
    print("Naive time: %.6f" %result, "| Process time: %.3f" %pr, " | System time: %.6f" %tr)


def run_profile(train):
    """
    This function provides the number of jobs we want
    sklearn to run in parallel.
    """

    print("")
    print("USING SKLEARN DEFAULT BEHAVIOUR")
    print("Default backend used: loky -> processed-based parallelism")
    
    print("workerNo = 1")
    train(1)

    print("workerNo = None")
    train(None)

    # Thi MAC has 6 phystical CPUs
    print("workerNo = 6, all physical CPU available in this machine")
    train(6)

    # This mac has 6 physical cores
    # but using multithreading this becomes 12
    print("workerNo = 12, all logic CPU available in this machine")
    train(12)

    print("workerNo = -1, all logic CPU available in this machine")
    train(-1)


def run_profile_ctx_manager(backend_type, train):
    """
    I am not sure about it but it seems that this will first 
    span each thread and send the job to it. Is this what
    sklearn is doing already? This link explains it well.
    https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel_backend.html

    It is particularly useful when calling into library code that uses joblib 
    internally but does not expose the backend argument in its own API.
    """

    print("")
    print("EXPOSING THE PARALLEL BACKEND DIRECTLY")

    print(backend_type + ": 1 | workerNo: None")
    with parallel_backend(backend_type, n_jobs=1):
        # Default should be train(-1)
        train()

    print(backend_type + ": 1 | workerNo: -1")
    with parallel_backend(backend_type, n_jobs=1):
        train(-1)

    print(backend_type + ": -1 | workerNo: -1")
    with parallel_backend(backend_type, n_jobs=-1):
        train(-1)

if __name__ == "__main__":
    
    print("=============")
    print("START TESTING")
    print("=============")    

    print("How many virtual cpu [multiprocessing.cpu_count()]?", multiprocessing.cpu_count())
    print("How many virtual cpu [os.cpu_count()]?", os.cpu_count())
    print("How many LOGICAL cpu [psutil.cpu_count(logical = True)]?", psutil.cpu_count(logical = True))
    print("How many PHYSICAL cpu [psutil.cpu_count(logical = False)]?", psutil.cpu_count(logical = False))


    run_profile(train)
    
    print("\n---------------------------")
    run_profile_ctx_manager("loky", train)
    run_profile_ctx_manager("threading", train)
    run_profile_ctx_manager("multiprocessing", train)
