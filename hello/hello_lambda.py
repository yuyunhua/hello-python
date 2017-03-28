f = lambda x: x * x
print [f(x) for x in range(10)]

print [lambda x: x * x for x in range(10)]

f = range(10)

f = [x * x for x in f]
print f
