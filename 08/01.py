def myfun1(x):
    x = x.split()
    s = 0
    for i in range(len(x)):
        s += int(x[i])
    return s

print(myfun1(input('Enter List x: ')))
