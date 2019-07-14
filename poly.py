def poly(x=1,y=2,z=3):
    return x+y+z

print(poly(20))
print(poly(5,4))

inp = input()
num = int(inp)
numb =bin(num).lstrip("0b").rstrip("L")
print(oct(num).lstrip("0o").rstrip("L"))
print(numb)
print(int(numb,2))
