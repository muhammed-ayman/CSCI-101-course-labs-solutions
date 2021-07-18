value = int(input('Enter a value:'))
L = input('Enter list of values:').split(' ')
count = 0
for i in L:
    if int(i) <= value:
        count += 1
        print(i)
if count == 0:
    print('All items are greater')
 
