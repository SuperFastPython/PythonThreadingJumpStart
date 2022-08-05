# SuperFastPython.com
# example of getting a list of active threads
from time import sleep
from threading import Thread
import threading

# custom function to be executed in a new thread
def task():
    # block for a moment
    sleep(1)

# protect the entry point
if __name__ == '__main__':
    # create a number of new threads
    threads = [Thread(target=task) for _ in range(5)]
    # start the new threads
    for thread in threads:
        thread.start()
    # get a list of all running threads
    running_threads = threading.enumerate()
    # report a count of active threads
    print(f'Active Threads: {len(running_threads)}')
    # report each in turn
    for thread in running_threads:
        print(thread)
