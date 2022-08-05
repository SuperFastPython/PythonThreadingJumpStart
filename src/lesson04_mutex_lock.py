# SuperFastPython.com
# example of protecting a critical section with a mutex
from time import sleep
from random import random
from threading import Thread
from threading import Lock

# custom function to be executed in a new thread
def task(shared_lock, ident, value):
    # acquire the lock
    with shared_lock:
        # report a message
        print(f'>{ident} got lock, sleeping {value}')
        # block for a fraction of a second
        sleep(value)

# protect the entry point
if __name__ == '__main__':
    # create the shared mutex lock
    lock = Lock()
    # create a number of threads with different args
    threads = [Thread(target=task,
        args=(lock, i, random())) for i in range(10)]
    # start the threads
    for thread in threads:
        thread.start()
    # wait for all threads to finish
    for thread in threads:
        thread.join()
