def wrapper_1(func):
    def wrapper(*args):
        print 'start wrapper_1'
        print 'wrapper_1 {}'.format(str(args))
        flag = func(*args)
        print 'wrapper_1 {}'.format(flag)
        print 'end wrapper_1'

    return wrapper


def wrapper_2(func):
    def wrapper(*args):
        print 'start wrapper_2'
        flag = func(*args)
        print 'wrapper_2 {}'.format(flag)
        print 'end wrapper_2'

    return wrapper


transactions = {}


def transaction(name):
    print '-----------------------------------------'

    def wrap(func):
        print '################################################'
        transactions.update({name: func})

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    return wrap


@transaction('adddddddddd')
def a():
    print 'a'


# transaction('hello, word')(a)()

a()
a()
print '--'
print transactions
transactions.get('adddddddddd')()
