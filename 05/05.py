vegetables = ['vegetables', 'mushroom', 'mashed potatoes', 'veggie burger']
soap_order = input('Enter the soap you want > ')
meal_order= input('Enter the meal you want > ')

if (soap_order in vegetables) and (meal_order in vegetables):
    print('she loves vegetables')
elif (soap_order not in vegetables) and (meal_order not in vegetables):
    print('she hates vegetables')
else:
    print('she neither hates nor loves vegetables')
