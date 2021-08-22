my_dict = {'x':500, 'y':250, 'z': 300}
max_val = list(my_dict.values())[0]
min_val = list(my_dict.values())[0]

for key in my_dict.keys():
    if my_dict[key] > max_val:
        max_val = my_dict[key]
    if my_dict[key] < min_val:
        min_val = my_dict[key]

print(f'Maximum Value: {max_val}')
print(f'Minimum Value: {min_val}')
