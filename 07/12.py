
items = ['Meat', 'Seafood', 'Milk', 'Bread', 'Oil']

items_available = input('how many available items in the following departments?\nMeat - Seafood - Milk - Bread - Oil>?').split()
items_available = list(map(int, items_available))
items_available_cl = [k for k in items_available]
items_prices = input('what are the prices of the available items in the following departments?\nMeat - Seafood - Milk - Bread - Oil>?').split()
items_prices = list(map(int, items_prices))
promo = '123456'

open = True

while open:
    order = input('how many you want from each of the following:\nMeat - Seafood - Milk - Bread - Oil>?').split()
    order = list(map(int, order))
    is_promo = (input('please enter promo if you have: >?') == promo)
    cost = 0
    for i in range(len(order)):
        if order[i] > items_available[i]:
            if items_available[i] == 0:
                print(f'we are sorry there is no available {items[i]}')
                break
            else:
                print(f'there are only {items_available[i]} {items[i]} available we put it in your cart')
                cost += items_available[i]*items_prices[i]
                if is_promo and items[i] == "Milk":
                    cost -= 30*(items_available[i]*items_prices[i])/100
                items_available[i] = 0
        else:
            cost += order[i]*items_prices[i]
            if is_promo and items[i] == "Milk":
                cost -= 30*(order[i]*items_prices[i])/100
            items_available[i] = items_available[i]-order[i]

    print(f'Dear prospective customer, the total is: {cost} pounds')
    open = (input('is the store still open? >?').lower() == 'yes')

total_sold = 0
for i in range(len(items_available_cl)):
    total_sold += items_available_cl[i]-items_available[i]

meat_per = (items_available_cl[0]-items_available[0])*100/total_sold
seafood_per = (items_available_cl[1]-items_available[1])*100/total_sold
milk_per = (items_available_cl[2]-items_available[2])*100/total_sold
bread_per = (items_available_cl[3]-items_available[3])*100/total_sold
oil_per = (items_available_cl[4]-items_available[4])*100/total_sold

per_list = [meat_per,seafood_per,milk_per,bread_per,oil_per]

for j in range(len(per_list)):
    for i in range(len(per_list)):
        if i+1 != len(per_list):
            if int(per_list[i]) < int(per_list[i+1]):
                per_list[i] , per_list[i+1] = per_list[i+1] , per_list[i]
                items[i] , items[i+1] = items[i+1] , items[i]

print('We sold today:')
for i in range(len(per_list)):
    print(f'{per_list[i]}% {items[i]}')
