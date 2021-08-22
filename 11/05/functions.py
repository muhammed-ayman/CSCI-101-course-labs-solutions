customers = []

def addCustomer(customers_list):
    name = input('Enter the Customer Name > ')
    id = int(input('Enter the Customer ID > '))
    balance = float(input('Enter the Customer balance > '))
    customer = {
        'name': name,
        'id': id,
        'balance': balance
    }
    customers_list.append(customer)
    return customers_list

def printCustomers(customers_list):
    for customer in customers_list:
        print(customer)

def applyTax(customers_list, tax_value):
    for customer in customers_list:
        customer['balance'] *= (1-tax_value/100)
    return customers_list

def deposit(customers_list, customer_id, deposit_value):
    for customer in customers_list:
        if customer['id'] == customer_id:
            customer['balance'] += deposit_value
    return customers_list

def withdraw(customers_list, customer_id, withdraw_value):
    for customer in customers_list:
        if customer['id'] == customer_id:
            customer['balance'] -= withdraw_value
    return customers_list
