# SuperFastPython.com
# example of executing an async one-off task
from multiprocessing.pool import ThreadPool

# custom function to be executed in a worker thread
def task():
    # report a message
    print('This is a worker thread')

# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPool() as pool:
        # issue a task asynchronously
        async_result = pool.apply_async(task)
        # wait for the task to complete
        async_result.wait()
