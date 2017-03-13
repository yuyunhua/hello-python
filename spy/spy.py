from monitor import *
from sender import Sender


class Main(object):
    @classmethod
    def perform(cls):
        interval = 3
        queue = Queue()

        cm = CpuMonitor(queue, interval)
        sm = SelfMonitor(queue, interval)
        mm = MemoryMonitor(queue, interval)
        nm = NetworkMonitor(queue, interval)
        iom = IoMonitor(queue, interval)
        pm = ProcessesMonitor(queue, interval, ['pycharm'])

        cm.start()
        mm.start()
        nm.start()
        iom.start()
        sm.start()
        pm.start()

        sender = Sender(queue, interval, '192.168.38.178', 8001)
        sender.start()
        sender.join()

if __name__ == '__main__':
    Main().perform()
