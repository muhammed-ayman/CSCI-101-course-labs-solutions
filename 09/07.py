def DispList(a):
    if a == []:
        return
    print(a[-1])
    DispList(a[0:-1])
DispList([2,3,4,10])
"""
10
4
3
2
"""
