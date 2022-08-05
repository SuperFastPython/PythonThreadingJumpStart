# SuperFastPython.com
# example of a callback function for a one-off task
from random import random
from time import sleep
from multiprocessing.pool import ThreadPool

# result callback function
def result_callback(return_value):
    # report a message
    print(f'Callback got: {return_value}')

# custom function to be executed in a worker thread
def task(ident):
    # generate a value
    value = random()
    # report a message
    print(f'Task {ident} with {value}')
    # block for a moment
    sleep(value)
    # return the generated value
    return value

# protect the entry point
if __name__ == '__main__':
    # create and configure the thread pool
    with ThreadPool() as pool:
        # issue tasks to the thread pool
        result = pool.apply_async(task, args=(0,),
            callback=result_callback)
        # close the thread pool
        pool.close()
        # wait for all tasks to complete
        pool.join()
