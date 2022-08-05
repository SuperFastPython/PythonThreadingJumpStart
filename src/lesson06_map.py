# SuperFastPython.com
# example executing multiple tasks with different args
from multiprocessing.pool import ThreadPool

# custom function to be executed in a worker thread
def task(arg):
    # report a message
    print(f'Worker task got {arg}')
    # return a value
    return arg * 2

# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPool() as pool:
        # issue multiple tasks and handle return values
        for result in pool.map(task, range(10)):
            # report result
            print(result)
