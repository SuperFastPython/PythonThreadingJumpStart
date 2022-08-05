# SuperFastPython.com
# example of threads sharing data with global variables
from time import sleep
from threading import Thread

# custom function to be executed in a new thread
def task():
    # block for a moment
    sleep(1)
    # correctly scope the global variable
    global data
    # store data in the global variable
    data = 'Hello from a new thread'

# protect the entry point
if __name__ == '__main__':
    # define the global variable
    data = None
    # create a new thread
    thread = Thread(target=task)
    # start the thread
    thread.start()
    # wait for the thread to finish
    thread.join()
    # report the global variable
    print(data)
