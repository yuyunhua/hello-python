class A(object):
    _a ='d'


    @staticmethod
    def func_1():
        A._a = 'b'
        print A._a

    @classmethod
    def func_3(cls):
        print cls._a

    def func_2(self):
        # self._a = 'c'
        print self._a

# print A._a

#
# class B(object):
#     @staticmethod
#     def func_1():
#         A.___a = 'c'
#         print A.___a
#         print A.___a


# B.func_1()
print A._a
# A.func_3()
A.func_1()
# A().func_2()
A.func_1()
A.func_3()
# print A().a
print A._a
