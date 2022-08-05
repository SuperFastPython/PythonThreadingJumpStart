# SuperFastPython.com
# example of getting access to the main thread
from threading import main_thread

# protect the entry point
if __name__ == '__main__':
    # get the main thread
    thread = main_thread()
    # report details
    print(thread)
