# SuperFastPython.com
# example of a thread closing itself via an exception
from random import random
from time import sleep
from threading import Thread
import threading

# handle exceptions in new thread
def handler(args):
    print(f'Got: {args.exc_value}')

# custom function to be executed in a new thread
def task():
    # loop forever
    while True:
        # generate a random value between 0 and 1
        value = random()
        print(f'.{value}')
        # block
        sleep(value)
        # check if we should close the thread
        if value > 0.9:
            print('Closing thread')
            raise Exception('Stop now!')

# protect the entry point
if __name__ == '__main__':
    # register a handler for exception in a new thread
    threading.excepthook = handler
    # create and configure the new thread
    thread = Thread(target=task)
    # start the new thread
    thread.start()
    # wait for the thread to terminate
    thread.join()
    # main continues on
    print('Main continuing on...')
