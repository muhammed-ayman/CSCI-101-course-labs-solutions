
conversions = {
    '1':0.001,
    '2':1000,
    '3':1000000
}

weight = int(input('Enter weight'))
if weight < 0:
    print('Invalid weight')
    exit()

unit = input('Enter weight unit (1 for mg, 2 for kg, 3 for ton): ')

if unit not in conversions.keys():
    print('Invalid Unit')
    exit()

print(weight*conversions[unit])
