
# A:

sum = 0
n = int(input('Enter N > '))

for i in range(n):
    sum += i+1
print(sum)

# B:

sum = 0
n = int(input('Enter N > '))

for i in range(1,n+1):
    sum += i
    to_print = ''
    for j in range(1,i+1):
        if j != i:
            to_print += f'{j}+'
        else:
            to_print += f'{j} ='
    print(f'{to_print} {sum}')

# C:

sum = 0
n = int(input('Enter N > '))

for i in range(n):
    sum += i+1

if sum%5 == 0:
    sum = 0
    for i in range(1,n+1):
        sum += i
        to_print = ''
        for j in range(1,i+1):
            if j != i:
                to_print += f'{j}+'
            else:
                to_print += f'{j} ='
        print(f'{to_print} {sum}')
else:
    print(f'Sum={sum}')
