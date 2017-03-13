import os
import time
from Queue import Queue
from threading import Thread
import re
import psutil


class AddTimestamp(object):
    def __init__(self, key):
        self.key = str(key)

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            now_time = time.strftime('(%Z) %Y-%m-%d %H:%M:%S', time.localtime())
            data = {
                'time': now_time,
                'type': self.key,
                'data': result
            }
            return data

        return wrapper


class Monitor(Thread):
    def __init__(self, queue, interval=5):
        Thread.__init__(self)
        self.interval = interval
        self.queue = queue
        self.flag = True

    def run(self):
        while self.flag:
            assert isinstance(self.queue, Queue)
            self.queue.put(self.monitor())

    def monitor(self):
        return ''


class HostMonitor(Monitor):
    @AddTimestamp('Host')
    def monitor(self):
        # todo
        time.sleep(self.interval)
        return {}


class MemoryMonitor(Monitor):
    @AddTimestamp('Memory')
    def monitor(self):
        time.sleep(self.interval)
        used = psutil.virtual_memory().used
        return {'used': used}


class NetworkMonitor(Monitor):
    @AddTimestamp('Network')
    def monitor(self):
        time.sleep(self.interval)
        connections_count = len(psutil.net_connections())

        return {'connections_count': connections_count}


class IoMonitor(Monitor):
    @AddTimestamp('IO')
    def monitor(self):
        time.sleep(self.interval)
        # todo
        return {}


class CpuMonitor(Monitor):
    @AddTimestamp('CPU')
    def monitor(self):
        return {"cpu_percent": psutil.cpu_percent(interval=self.interval)}


class ProcessMonitor(Monitor):
    def __init__(self, queue, interval, pid, keyword):
        Monitor.__init__(self, queue, interval)
        self.pid = pid
        if keyword == '@self':
            self.monitor = AddTimestamp('Self').__call__(self.monitor)
        else:
            self.monitor = AddTimestamp('Process').__call__(self.monitor)

    def monitor(self):
        data = {
            'pid': self.pid,
        }
        try:
            p = psutil.Process(self.pid)
            percent = p.cpu_percent(self.interval) / psutil.cpu_count()
            memory_info = p.memory_info()
            data.update({
                'command_line': ' '.join(p.cmdline()),
                'rss': memory_info.rss,
                'mss': memory_info.vms,
                'cpu_percent': percent,
                'threads_count': p.num_threads(),
                'name': p.name()
            })
        except psutil.NoSuchProcess:
            self.flag = False
        finally:
            return data


class SelfMonitor(ProcessMonitor):
    def __init__(self, queue, interval):
        ProcessMonitor.__init__(self, queue, interval, os.getpid(), '@self')


class ProcessesMonitor(Monitor):
    def __init__(self, queue, interval, keywords):
        Monitor.__init__(self, queue, interval)
        self.keywords = keywords
        assert isinstance(keywords, list)
        self.running = []
        self.monitoring = []

    @AddTimestamp('MonitoringProcesses')
    def monitor(self):
        time.sleep(self.interval)

        for process in psutil.process_iter():
            if process.pid not in self.monitoring:
                try:
                    command_line = ' '.join(process.cmdline())
                except psutil.AccessDenied:
                    command_line = ''

                for keyword in self.keywords:
                    if re.search(keyword, command_line):
                        ProcessMonitor(self.queue, self.interval, process.pid, keyword).start()
                        self.monitoring.append(process.pid)
                        break

        for pid in self.monitoring:
            if not psutil.pid_exists(pid):
                self.monitoring.remove(pid)

        return {'monitoring_processes': self.monitoring}
