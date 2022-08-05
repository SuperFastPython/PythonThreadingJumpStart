# SuperFastPython.com
# example of running a function in a new thread
from time import sleep
from threading import Thread

# custom function to be executed in a new thread
def task():
    # block for a moment
    sleep(1)
    # report a message
    print('This is from another thread')

# protect the entry point
if __name__ == '__main__':
    # create a new thread instance
    thread = Thread(target=task)
    # start executing the function in the new thread
    thread.start()
    # wait for the thread to finish
    print('Waiting for the thread...')
    thread.join()
