import functools
import glob

print glob.glob('../*.*')


def para_should_be_int(func):
    @functools.wraps(func)
    def wrapper(*d, **e):
        print type(d)
        print d
        print e
        print type(e)
        print func.__name__
        return func(*d, **e)

    return wrapper


class A(object):
    def __init__(self, arg1, arg2, arg3):
        print "Inside __init__()"
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            print "Inside wrapped_f()"
            print "Decorator arguments:", self.arg1, self.arg2, self.arg3
            returns = f(*args, **kwargs)
            print "After f(*args)"
            return returns

        return wrapper


@A('<para_1>', 2, 3)
def func_1(para_1, para_2):
    print para_1 + para_2
    return para_1 + para_2


print func_1(1, para_2=2)
