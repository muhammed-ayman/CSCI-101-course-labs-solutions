arr1 = input('Enter 1st Array > ').split()
arr2 = input('Enter 2nd Array > ').split()

arr_result = []

for i in arr1:
    count = 0
    for j in arr2:
        if i == j:
            count += 1
    arr_result.append(count)

print(arr_result)
