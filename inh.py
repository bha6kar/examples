class One(object):
    def a(self):
        print('clssss 1')


class T(One):
    def n(self):
        super(T, self).n()
        print('clssss T')


class Tr(One):
    def a(self):
        super(Tr, self).a()
        print('clssss Tr')


class f(Tr, T):
    def a(self):
        #super(f, self).a()
        print('clssss 4')


a = One()
b = T()
c = Tr()
d = f()

d.a()
