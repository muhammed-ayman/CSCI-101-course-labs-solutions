from helpers import *

program_msg = """
1- Add customer
2- Print All customers
3- Apply Tax
4- Deposit
5- Withdraw
6- EXIT
"""

while True:
    req = input('Enter a choice <1-6>')
    if req not in [str(i) for i in range(1,7)]:
        print('Invalid input')
        continue
    if req == '1':
        customers = addCustomer(customers)
    elif req == '2':
        printCustomers(customers)
    elif req == '3':
        tax_value = float(input('Enter the tax value > '))
        applyTax(customers, tax_value)
    elif req == '4':
        deposit_value = float(input('Enter the deposit value > '))
        customer_id = int(input('Enter Customer\'s ID > '))
        deposit(customers, customer_id, deposit_value)
    elif req == '5':
        withdraw_value = float(input('Enter the withdraw value > '))
        customer_id = int(input('Enter Customer\'s ID > '))
        withdraw(customers, customer_id, withdraw_value)
    elif req == '6':
        exit()
