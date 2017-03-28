from threading import Thread
import time


class A(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.result = ''

    def run(self):
        time.sleep(3)
        print 'a'
        self.result = 'hello'


a = A()
print a.start()
print 'hello'
print a.join()

while a.is_alive():
    time.sleep(1)

print a.is_alive()
print a.result
print a.isAlive()
print a.