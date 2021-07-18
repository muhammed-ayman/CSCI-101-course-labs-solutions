#Method 1
L = input('Enter list of values:').split()
for i in range(len(L)):
    if int(L[i]) > 0:
        print(L[i])

#Method 2
L = input('Enter list of values:').split()
for i in L:
    if int(i) > 0:
        print(i)
