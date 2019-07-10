class One(object):
    def a(self):
        print('class 1')

class T(One):
    def n(self):
        super(T, self).n()
        print('class T')


class Tr(One):
    def a(self):
        super(Tr, self).a()
        print('class Tr')

class f(Tr,T):
    def a(self):
        super(f, self).a()
        print('class 4')

a = One()
b = T()
c = Tr()
d = f()

d.a()