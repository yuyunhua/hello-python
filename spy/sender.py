import json
import socket
import time
from Queue import Queue
from telnetlib import Telnet
from threading import Thread


class Sender(Thread):
    def __init__(self, queue, interval, host, port):
        Thread.__init__(self)
        self.queue = queue
        self.interval = interval
        self.host = host
        self.port = port
        self.tc = None
        self.messages = []

    def run(self):
        while True:
            size = self.queue.qsize()
            for i in range(0, size):
                self.messages.insert(0, self.queue.get())

            assert isinstance(self.queue, Queue)

            if len(self.messages) > 0:
                self.send()
            else:
                time.sleep(1)

    @classmethod
    def format_message(cls, message):
        return json.dumps(message)

    def send(self):
        connected = False
        while len(self.messages) > 0:
            message = self.messages.pop()
            try:
                if not connected:
                    self.tc = Telnet(self.host, self.port)
                    connected = True
                self.tc.write(self.format_message(message) + '\n')
            except socket.error:
                connected = False
                self.messages.append(message)
                time.sleep(10)
