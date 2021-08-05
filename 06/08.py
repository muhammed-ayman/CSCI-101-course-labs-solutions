
n_pressed = True
avg = 0
counter = 0
while n_pressed:
    int_input = int(input('Insert an integer:'))
    check_cont = input('Do you wish to continue? <Y/N>:')
    if check_cont == 'N':
        n_pressed = False
    avg += int_input
    counter += 1

print(f'Average={avg/counter}')
