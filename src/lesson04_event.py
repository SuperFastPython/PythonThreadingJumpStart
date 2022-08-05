# SuperFastPython.com
# example of using an event object with threads
from time import sleep
from random import random
from threading import Thread
from threading import Event

# custom function to be executed in a new thread
def task(shared_event, number):
    # wait for the event to be set
    print(f'Thread {number} waiting...')
    shared_event.wait()
    # begin work, generate a random number
    value = random()
    # block for a fraction of a second
    sleep(value)
    # report a message
    print(f'Thread {number} got {value}')

# protect the entry point
if __name__ == '__main__':
    # create a shared event object
    event = Event()
    # create a suite of threads
    threads = [Thread(target=task,
        args=(event, i)) for i in range(5)]
    # start all threads
    for thread in threads:
        thread.start()
    # block thread a moment
    print('Main thread blocking...')
    sleep(2)
    # trigger all threads
    event.set()
    # wait for all threads to terminate
    for thread in threads:
        thread.join()
