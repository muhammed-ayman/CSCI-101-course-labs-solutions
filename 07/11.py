n = int(input('Enter N > '))

for i in range(n):
    print(f'{" "*i}*')
for i in range(n):
    print(f'{" "*(n-1-i)}*')
