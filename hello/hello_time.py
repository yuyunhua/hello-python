import time

print time.strftime('(%Z) %Y-%m-%d %H:%M:%S', time.localtime())

# timestamp
print time.time()
print time.localtime(time.time())

print 1489044670