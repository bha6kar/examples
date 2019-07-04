

class Abc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def method1(self):
        c = self.a + self.b
        print(c)
        return c


if __name__ == "__main__":
    call = Abc(2, 3)
    call.method1()
