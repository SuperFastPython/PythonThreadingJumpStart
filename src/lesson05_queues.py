# SuperFastPython.com
# example of threads sharing data using a queue
from time import sleep
from threading import Thread
from queue import Queue

# custom function to be executed in a new thread
def task(shared_queue):
    # block for a moment
    sleep(1)
    # prepare some data
    item = 'Hello from a new thread'
    # share the data via the queue
    shared_queue.put(item)

# protect the entry point
if __name__ == '__main__':
    # create the shared queue
    queue = Queue()
    # create a new thread
    thread = Thread(target=task, args=(queue,))
    # start the thread
    thread.start()
    # block and wait for data via queue
    data = queue.get()
    # report data from the queue
    print(data)
