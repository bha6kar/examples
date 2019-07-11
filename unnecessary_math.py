'''
Module showing how doctests can be included with source code
Each '>>>' line is run as if in a python shell, and counts as a test.
The next line, if not '>>>' is the expected output of the previous line.
If anything doesn't match exactly (including trailing spaces), the test fails.
'''

class Mathmul:
    def __init__(self,a,b):
        self.a= a
        self.b= b

    def multiply(self):
        """
        >>> multiply(4, 3)
        12
        >>> multiply('a', 3)
        'aaa'
        """
        c =(self.a * self.b)
        print(c)
        return c

if __name__ == '__main__':
    mul = Mathmul(2,3)
    mul.multiply()