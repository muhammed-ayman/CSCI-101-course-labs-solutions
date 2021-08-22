def multList(l):
    if l == []:
        return 1
    return multList(l[0:-1]) * l[-1]

print(multList([1,2,3,4]))
