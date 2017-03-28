from urlparse import urlparse, urljoin

o = urlparse('http://www.Cwi.nl:80/%7Eguido/Python.html?username=hello&password=world')
print o
print o.scheme
print o.hostname
print o.password

a = urljoin('http://www.baidu.com/ddd', 'd/a.html')

print a
print type(a)
print urlparse(a)




def a(i):
    if i > 5:
        return i, 5
    return i


c = {'a': 1, 'b': 'a'}

import urllib
print urljoin('http://www.baidu.com/d', 'f/e.html', False) + '?' + urllib.urlencode(c)

d = 'http://pet-hub.calix.local:8080/job/FA%20Plus%20Automation/job/FA%20Plus%20Web%20Automation%20-%20Report/311/'
print urlparse(d).params is None

d = urlparse('/search-result?filter=ROL104029&page=1')
print d
print d.query is None
print d.query == ''
print d.query

