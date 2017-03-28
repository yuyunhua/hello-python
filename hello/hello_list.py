import logging
import json

print [].append('d')
d = ['a']
d.extend(['d'])
print d
print d.pop()
print d

a = []
a.insert(0, 1)
a.insert(0, 2)
a.insert(0, 3)
print a
print a.pop()
print a.pop()


print a

import random
for x in xrange(0,20):
    print random.randint(0,5)
