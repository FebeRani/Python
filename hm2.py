from os import remove


def removeAll(list,x) :
    list.extend(x)
listx=[14,1,4,40,14,16,2,2,1,16,10,23,28,26,4,]

print(listx) 
listx.remove(4)


#removeAll(list,1)
removeAll(listx,4)
print(listx)



