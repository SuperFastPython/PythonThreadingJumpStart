# SuperFastPython.com
# example of getting access to the current thread
from threading import current_thread

# protect the entry point
if __name__ == '__main__':
    # get the current thread
    thread = current_thread()
    # report details
    print(thread)
