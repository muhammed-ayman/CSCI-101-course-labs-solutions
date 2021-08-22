def func(n,r):
    if n==1:
        return 1
    return r*func(n-1,r)

print(func(5,3)) #81
