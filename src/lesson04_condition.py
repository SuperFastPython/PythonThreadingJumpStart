# SuperFastPython.com
# example of wait/notify with a condition for threads
from time import sleep
from threading import Thread
from threading import Condition

# custom function to be executed in a new thread
def task(shared_condition):
    # block for a moment
    sleep(1)
    # notify a waiting thread that the work is done
    print('Thread sending notification...')
    with shared_condition:
        shared_condition.notify()

# protect the entry point
if __name__ == '__main__':
    # create a condition
    condition = Condition()
    # acquire the condition
    print('Main thread waiting for data...')
    with condition:
        # create a new thread to execute the task
        thread = Thread(target=task, args=(condition,))
        # start the new new thread
        thread.start()
        # wait to be notified by the new thread
        condition.wait()
    # we know the data is ready
    print('Main thread all done')
