# SuperFastPython.com
# example of creating a daemon thread
from threading import Thread

# protect the entry point
if __name__ == '__main__':
    # create a daemon thread
    thread = Thread(daemon=True)
    # report if the thread is a daemon
    print(thread.daemon)
