def countList(l):
    if l == []:
        return 0
    to_add = 1 if l[-1]%2==0 else 0
    return countList(l[0:-1]) + to_add

print(countList([1,2,3,4]))
