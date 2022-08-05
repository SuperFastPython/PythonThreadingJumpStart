# SuperFastPython.com
# example of using a barrier with threads
from time import sleep
from random import random
from threading import Thread
from threading import Barrier

# custom function to be executed in a new thread
def task(shared_barrier, ident):
    # generate a unique value between 0 and 10
    value = random() * 10
    # block for a moment
    sleep(value)
    # report result
    print(f'Thread {ident} got: {value}')
    # wait for all other threads to complete
    shared_barrier.wait()

# protect the entry point
if __name__ == '__main__':
    # create a barrier for (5 threads + 1 main thread)
    barrier = Barrier(5 + 1)
    # create the new threads
    threads = [Thread(target=task,
        args=(barrier, i)) for i in range(5)]
    # start the new threads
    for thread in threads:
        # start thread
        thread.start()
    # wait for all new threads to finish
    print('Main thread waiting on all results...')
    barrier.wait()
    # report once all thread are done
    print('All threads have their result')
