
n = int(input('Enter the count of numbers you need to input > '))
nums = []

for i in range(n):
    nums.append(int(input(f'Enter Number {i+1} > ')))

odd_sum=0
even_sum=0
odd_count=0
even_count=0

for i in nums:
    if i%2 == 0:
        even_sum += i
        even_count += 1
    else:
        odd_count += 1
        odd_sum += i

if even_count != 0:
    print(f'Even Average = {even_sum/even_count}')
if odd_count != 0:
    print(f'Odd Average = {odd_sum/odd_count}')
