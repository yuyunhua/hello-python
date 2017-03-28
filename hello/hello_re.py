import re

s = 'a==b===c===d====e'
print re.sub('=+', '=', s)
print re.subn('=+', '=', s)
print type(re.match('a=+', s))
print type(re.search('=+', s))
print re.findall('=+', s)
print re.split('=+', s)
