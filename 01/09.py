import math

n = float(input('Enter the number of grams: '))

kilograms = math.floor(n/1000)
grams = n-kilograms*1000

print('Kilograms:',kilograms,', Grams:',grams)
