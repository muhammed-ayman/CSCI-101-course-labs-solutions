s1 = input('Enter S1 > ')
s2 = input('Enter S2 > ')

if s1 == s2:
    print('Identical Strings')
else:
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            print(f'mismatch at index {i}')
