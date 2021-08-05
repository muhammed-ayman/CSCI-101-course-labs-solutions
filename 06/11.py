
arr_1 = input('Enter 1st Array > ').split()
arr_2 = input('Enter 2nd Array > ').split()
arr_result = []

if len(arr_1) == len(arr_2):
    for i in range(len(arr_1)):
        arr_result.append(int(arr_1[i])-int(arr_2[i]))
else:
    print('Arrays dimensions don\'t match')
    exit()

print(f'Array1 - Array2 = {arr_result}')
