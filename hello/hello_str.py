import datetime
import calendar
data_list = calendar.timegm(datetime.datetime.utcnow().timetuple())
b = calendar.timegm(datetime.datetime.now().timetuple())

c = datetime.datetime.fromtimestamp(data_list + (data_list - b) + 8 * 3600)
print str(c)

data_list = '1.2'
print int(float(data_list))

step = 'url=/login,username=admin@hvtel.com,password=Admin123,duration=123'
print step
t = step
step = {}
for i in str(t).split(','):
    key,o, value = i.partition('=')
    step.update({key: value})
print step

url = step.pop('url')
print url
print
print step