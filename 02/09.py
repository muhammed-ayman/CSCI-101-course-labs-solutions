
n = int(input('Enter the count of numbers you need to input > '))
nums = []

for i in range(n):
    nums.append(int(input(f'Enter Number {i+1} > ')))

counter = 0
sum = 0

for i in nums:
    if i > 6:
        sum += i
        counter += 1

if counter != 0:
    print(f'Average={sum/counter}')
else:
    print('All Numbers are less than 6')
