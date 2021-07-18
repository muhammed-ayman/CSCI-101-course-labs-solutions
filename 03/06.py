sal = input('Enter salaries:').split(' ')
tax = float(input('Enter tax:'))
salAfterTax = []
for v in sal:
    x = int(v) - int(v)*tax
    salAfterTax.append(x)
print(salAfterTax)
