
n = int(input('Enter N > '))

if n < 0:
    print('Negative Number')
else:
    sum = 0
    for i in range(n):
        sum += (i+1)**2
    print(sum)
