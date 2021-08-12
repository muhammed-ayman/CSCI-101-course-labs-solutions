import convertFahrenheit

degree = float(input('Enter Degree in Fahrenheit: '))
result = convertFahrenheit.convertFahrenheit(degree)
print(f'Celisus = {result[0]}, Kelvin = {result[1]}')
