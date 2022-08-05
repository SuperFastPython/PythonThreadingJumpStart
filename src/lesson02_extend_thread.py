# SuperFastPython.com
# example of extending the thread class
from time import sleep
from threading import Thread

# custom thread class
class CustomThread(Thread):
    # override the run function
    def run(self):
        # block for a moment
        sleep(1)
        # report a message
        print('This is another thread')

# protect the entry point
if __name__ == '__main__':
    # create the thread
    thread = CustomThread()
    # start the thread
    thread.start()
    # wait for the thread to finish
    print('Waiting for the thread to finish')
    thread.join()
