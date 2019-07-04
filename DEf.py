from examples import Abc


class Def:
    def __init__(self, c, d):
        self.c = c
        self.d = d

    def method2(self):
        abc = Abc.Abc(4, 6)
        n = abc.method1()
        print(n)


if __name__ == "__main__":
    defs = Def(5, 5)
    defs.method2()
