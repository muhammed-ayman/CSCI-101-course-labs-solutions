n = int(input('Enter N > '))

for i in range(1,n+1):
    row = ''
    for j in range(1, i+1):
        mult_result = str(j*i)
        row += mult_result+' '*(4-len(mult_result))
    print(row)
