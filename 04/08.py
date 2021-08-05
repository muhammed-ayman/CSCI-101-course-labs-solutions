
n1 = int(input('Enter N1 > '))
n2 = int(input('Enter N2 > '))

if n1 > n2:
    n1,n2 = n2,n1

counter = 0
sum = 0
for i in range(n1+1,n2):
    sum += i
    counter += 1

print(f'Sum={sum}, Average={sum/counter}')
