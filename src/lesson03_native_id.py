# SuperFastPython.com
# example of reporting the thread native identifier
from threading import Thread

# protect the entry point
if __name__ == '__main__':
    # create the thread
    thread = Thread()
    # report the thread identifier
    print(thread.native_id)
    # start the thread
    thread.start()
    # report the thread identifier
    print(thread.native_id)
