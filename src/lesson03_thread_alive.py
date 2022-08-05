# SuperFastPython.com
# example of assessing whether a thread is alive
from threading import Thread

# protect the entry point
if __name__ == '__main__':
    # create the thread
    thread = Thread()
    # report the thread is alive
    print(thread.is_alive())
