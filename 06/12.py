arr1 = input('Enter 1st Array > ').split()
arr2 = input('Enter 2nd Array > ').split()

for i in arr1:
    if i in arr2:
        print('duplicate exist')
        exit()
print('unique values')
