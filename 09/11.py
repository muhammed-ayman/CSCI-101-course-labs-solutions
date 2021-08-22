def countList(l):
    if l == []:
        return 0
    return countList(l[0:-1]) + 1

print(countList([1,2,3,4]))
