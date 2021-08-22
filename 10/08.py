my_dict = {'item1':3,'item2':-5,'item3':20}
sumx = 0
for key in my_dict.keys():
    sumx += my_dict[key]

print(sumx)

suma = sum(list([my_dict[key] for key in my_dict.keys()]))
print(suma)
