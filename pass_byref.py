
def reassign(list, s):
    list.append(1)
    s = +5
    print(id(list))


s = 'yo'
print(id(s))
list = [0]
print(id(list))
list1 = list
reassign(list, s)
print(list)
print(list1)


t = s
s = 'kl'
print(id(s))
print(id(t))
