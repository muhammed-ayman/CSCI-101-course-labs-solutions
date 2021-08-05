n1 = float(input('Enter #1 > '))
n2 = float(input('Enter #2 > '))
n3 = float(input('Enter #3 > '))

nums = [n1, n2, n3]

for j in range(len(nums)):
    for i in range(len(nums)):
        if i+1 != len(nums):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]

print(nums)
