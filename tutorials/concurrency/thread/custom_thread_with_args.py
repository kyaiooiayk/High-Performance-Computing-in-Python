# https://superfastpython.com/extend-thread-class/

# example of extending the Thread class and passing arguments
from time import sleep
from threading import Thread


# custom thread class
class CustomThread(Thread):
    # override the constructor
    def __init__(self, value):
        # execute the base constructor
        Thread.__init__(self)
        # store the value
        self.value = value

    # override the run function
    def run(self):
        # block for a moment
        sleep(self.value)
        # display a message
        print(f"This is coming from another thread: {self.value}")
        # store return value
        self.value = 99


# create the thread
thread = CustomThread(0.5)
# start the thread
thread.start()
# wait for the thread to finish
print("Waiting for the thread to finish")
thread.join()
# get the value returned from run
value = thread.value
print(f"Got: {value}")
