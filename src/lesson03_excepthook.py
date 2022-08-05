# SuperFastPython.com
# example of handling a thread's unexpected exception
from time import sleep
from threading import Thread
import threading

# custom exception hook
def custom_hook(args):
    # report the failure
    print(f'Thread failed: {args.exc_value}')

# target function that raises an exception
def task():
    # report a message
    print('Working...')
    # block for a moment
    sleep(1)
    # rise an "unexpected" exception
    raise Exception('Something bad happened')

# protect the entry point
if __name__ == '__main__':
    # register the exception hook function
    threading.excepthook = custom_hook
    # create a thread
    thread = Thread(target=task)
    # run the thread
    thread.start()
    # wait for the thread to finish
    thread.join()
    # report that the main thread is not dead
    print('Continuing on...')
