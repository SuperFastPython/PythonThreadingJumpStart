# SuperFastPython.com
# example of a thread stopping itself via calling sys.exit()
from time import sleep
from threading import Thread
import sys

# custom function to be executed in a new thread
def task():
    # wait a moment
    sleep(1)
    # report a message
    print('Thread exiting now')
    # exit the thread
    sys.exit(0)
    # this is never reached
    print('Can you see me?')

# protect the entry point
if __name__ == '__main__':
    # create a new thread
    thread = Thread(target=task)
    # start the thread
    thread.start()
    # wait a moment
    sleep(2)
    # report a message
    print('Main all done')
