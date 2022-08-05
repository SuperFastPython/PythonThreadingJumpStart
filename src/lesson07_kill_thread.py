# SuperFastPython.com
# example of killing a thread via its parent process
from time import sleep
from multiprocessing import Process

# custom function to be executed in a new thread
def task():
    # run for ever
    while True:
        # block for a moment
        sleep(1)
        # report a message
        print('Task is running', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create a new process with a new thread
    process = Process(target=task)
    # start the new process and new thread
    process.start()
    # wait a while
    sleep(5)
    # kill the new thread via the new process
    print('Killing the thread via its process')
    process.terminate()
    # wait a while
    sleep(2)
    # all done
    print('All done, stopping')
