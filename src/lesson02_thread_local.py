# SuperFastPython.com
# example of sharing thread-local storage
from time import sleep
from threading import Thread
from threading import local

# custom function executed in a new thread
def task(shared_local):
    # block for a moment to simulate work
    sleep(1)
    # store a private variable on the thread local
    shared_local.value = 33
    # report the stored value
    print(f'Thread stored: {shared_local.value}')

# protect the entry point
if __name__ == '__main__':
    # create a shared thread-local instance
    local_storage = local()
    # store a private variable on the thread local
    local_storage.value = 100
    # report the stored value
    print(f'Main stored: {local_storage.value}')
    # create a new thread to run the custom function
    thread = Thread(target=task, args=(local_storage,))
    # start the new thread
    thread.start()
    # wait for the thread to terminate
    thread.join()
    # report the stored value
    print(f'Main sees: {local_storage.value}')
