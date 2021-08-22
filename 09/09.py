def addList(l):
    if l == []:
        return 0
    return addList(l[0:-1]) + l[-1]

print(addList([1,2,3,4]))
