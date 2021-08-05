
finished_assignment= input('Ali did you finish your assignment')
shoes_price = float(input('what is the shoes price?'))

if finished_assignment == 'yes':
    if shoes_price > 900:
        print('the shoes price is',shoes_price,'and dad will pay')
    else:
        print('the shoes price is',shoes_price,'and mom will pay')
else:
    print('finish the assignment first')
