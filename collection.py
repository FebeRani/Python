mylist=[1,235,34,54,356,364,43,43,356]

print(mylist)
print(mylist[1:3])
print(mylist[0:3])
print(mylist[3:])
print(mylist[::])
print(mylist[1:6:2])
print(mylist[1::2])
print(mylist[9::-1])
print(mylist[9:5:-1])


mylist.sort()
print(mylist)

mylist.sort(reverse=True)
print(mylist)

mylist.insert(4,1416)
print(mylist)

mylist.remove(43)
print(mylist)

mylist.extend([14,16,28])
print(mylist)
