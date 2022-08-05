# SuperFastPython.com
# example of setting the thread name in the constructor
from threading import Thread

# protect the entry point
if __name__ == '__main__':
    # create a thread with a custom name
    thread = Thread(name='MyThread')
    # report thread name
    print(thread.name)
