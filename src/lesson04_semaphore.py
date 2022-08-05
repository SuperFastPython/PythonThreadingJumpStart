# SuperFastPython.com
# example of a semaphore to limit access to resource
from time import sleep
from random import random
from threading import Thread
from threading import Semaphore

# custom function to be executed in a new thread
def task(shared_semaphore, ident):
    # attempt to acquire the semaphore
    with shared_semaphore:
        # generate a random value between 0 and 1
        val = random()
        # block for a fraction of a second
        sleep(val)
        # report result
        print(f'Thread {ident} got {val}')

# protect the entry point
if __name__ == '__main__':
    # create the shared semaphore
    semaphore = Semaphore(2)
    # create threads
    threads = [Thread(target=task,
        args=(semaphore, i)) for i in range(10)]
    # start new threads
    for thread in threads:
        thread.start()
    # wait for new threads to finish
    for thread in threads:
        thread.join()
