import threading
import time
from threading import Thread


def duration(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        return time.time() - start_time

    return wrapper


class SleepThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        time.sleep(3)


@duration
def main():
    threads = []
    for i in xrange(5):
        thread = SleepThread()
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


class LoopThread(threading.Thread):
    def __init__(self):
        Thread.__init__(self)
        self.stop_flag = False

    def run(self):
        while not self.stop_flag:
            time.sleep(1)
            print time.time()

    def stop(self):
        self.stop_flag = True


def stop_thread():
    loop = LoopThread()
    loop.start()
    time.sleep(5)
    loop.stop()
    while loop.is_alive():
        print '------'
        time.sleep(1)


if __name__ == '__main__':
    # print main()
    stop_thread()
