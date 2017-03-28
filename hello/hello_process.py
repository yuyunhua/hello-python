import os
import time
from multiprocessing import Process


def target(index):
    os.environ['test'] = index
    time.sleep(3)
    assert index == os.environ['test']


def main():
    processes = []

    for index in range(10):
        p = Process(name='p_' + str(index), target=target, args=(str(index)))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


if __name__ == '__main__':
    main()
