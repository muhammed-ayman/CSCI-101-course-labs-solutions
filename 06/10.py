num = int(input('Enter the number > '))
factorial = 1
f_counter = 1

while f_counter <= num:
    factorial *= f_counter
    f_counter += 1
    if factorial > 1000000:
        print('factorial limit exceeded!')
        exit()

print(f'{num}!={factorial}')
