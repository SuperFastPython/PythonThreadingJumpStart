# SuperFastPython.com
# example of stopping a new thread gracefully
from time import sleep
from threading import Thread
from threading import Event

# custom function to be executed in a new thread
def task(shared_event):
    # execute a task in a loop
    for _ in range(5):
        # block for a moment
        sleep(1)
        # check for stop
        if shared_event.is_set():
            break
        # report a message
        print('Worker thread running...')
    print('Worker closing down')

# protect the entry point
if __name__ == '__main__':
    # create the shared event
    event = Event()
    # create and configure a new thread
    thread = Thread(target=task, args=(event,))
    # start the new thread
    thread.start()
    # block for a while
    sleep(3)
    # stop the worker thread
    print('Main stopping thread')
    event.set()
    # wait for the new thread to finish
    thread.join()
