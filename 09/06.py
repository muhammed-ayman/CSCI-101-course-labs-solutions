def showList(a):
    if a == []:
        return
    print(a[0])
    showList(a[1:])

showList([2,3,4,10])
"""
2
3
4
10
"""
