a = {'a': 1, 'b': 2, 'c': 3}

for (key, value) in a.iteritems():
    print key, value

print 'a' in a

print a.pop('a')
if 'c' in a:
    print a.pop('c')

print a
print a.update({})
print a
b = {}
print b.update(a)
print b